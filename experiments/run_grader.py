#!/usr/bin/env python3
"""IWAPS 2026 — grader stack (code-based + model-based) over generated policies.

For every generated artefact in outputs/<config>/<context>/<policy>.md this
script:

  1. Runs the code-based grader from grader/code_checks.py — deterministic,
     no API call.
  2. For each of the seven rubric criteria, calls Claude Opus 4.7 as
     LLM-judge with a strict JSON output schema (dimension-by-dimension).
  3. Writes one score record per (artefact × criterion) under
     scores/<config>/<context>/<policy>.<criterion>.json
  4. Writes a per-artefact aggregate under scores/<config>/<context>/<policy>.aggregate.json
  5. Appends a JSONL log for the whole run.

Defaults: dry-run prints the matrix. --execute makes API calls.
"""

from __future__ import annotations
import argparse
import json
import os
import sys
import time
from pathlib import Path
from typing import Any

import anthropic
import yaml

ROOT = Path(__file__).resolve().parent
CONTEXTS_DIR = ROOT / "contexts"
PROMPTS_DIR = ROOT / "prompts"
GRADER_DIR = ROOT / "grader"
OUTPUTS_DIR = ROOT / "outputs"
SCORES_DIR = ROOT / "scores"

sys.path.insert(0, str(GRADER_DIR))
from code_checks import run_code_checks  # type: ignore
sys.path.insert(0, str(PROMPTS_DIR))
from context_renderer import render as render_context  # type: ignore

JUDGE_MODEL = "claude-opus-4-7"
JUDGE_MAX_TOKENS = 1500
SECRETS = Path(os.environ.get("POLICYCOACH_SECRETS", ROOT / "secrets"))
ANTHROPIC_KEY = os.environ.get("ANTHROPIC_API_KEY") or (SECRETS / "anthropic_api_key").read_text().strip()
_anthropic = anthropic.Anthropic(api_key=ANTHROPIC_KEY)


CONFIG_SLUGS = {
    "C0":       "c0_chatgpt",
    "C0+web":   "c0_chatgpt_web",
    "C0_5+web": "c0_5_chatgpt_web",
    "C1":       "c1_openai_assistant",
    "C2":       "c2_private_rag",
    "C2b":      "c2b_private_rag_deepseek",
}
SLUG_TO_CONFIG = {v: k for k, v in CONFIG_SLUGS.items()}

CONTEXT_FILES = {
    "ctx-H": CONTEXTS_DIR / "hospital.yaml",
    "ctx-M": CONTEXTS_DIR / "military.yaml",
}


# ---------------------------------------------------------------------------
# Artefact loader
# ---------------------------------------------------------------------------

def parse_artefact(md_path: Path) -> tuple[dict, str]:
    """Return (frontmatter_dict, body) for an artefact saved by run_generation."""
    text = md_path.read_text()
    if not text.startswith("---\n"):
        raise ValueError(f"missing frontmatter in {md_path}")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError(f"unterminated frontmatter in {md_path}")
    fm = yaml.safe_load(text[4:end])
    body = text[end + 5:].lstrip("\n")
    return fm, body


def list_artefacts() -> list[Path]:
    return sorted(OUTPUTS_DIR.glob("*/ctx-*/*.md"))


# ---------------------------------------------------------------------------
# Judge prompt rendering
# ---------------------------------------------------------------------------

JUDGE_SYSTEM = (
    "You are an experienced cybersecurity policy auditor with 15+ years across "
    "healthcare and defence sectors. You have deep working knowledge of NIST CSF "
    "2.0, ISO/IEC 27001, GDPR, NIS2, NATO Information Security Policy, and "
    "Italian sector regulations. You evaluate one criterion at a time. Be strict, "
    "evidence-driven, and concise. If the policy contains no observable signal "
    "for the criterion, return null rather than guess. Output is a single JSON "
    "object. No commentary outside the JSON."
)


def render_judge_user(criterion: dict, context_narrative: str, policy_text: str) -> str:
    bullets = "\n".join(f"- {b}" for b in criterion["what_to_look_for"])
    return f"""### Criterion to evaluate

**{criterion['name']}** (`{criterion['id']}`)

**Definition.** {criterion['definition']}

**What to look for.**
{bullets}

**Scoring anchors.**
- 1 — {criterion['anchors']['1']}
- 3 — {criterion['anchors']['3']}
- 5 — {criterion['anchors']['5']}

(Use 2 and 4 as intermediate values when appropriate.)

**Escape valve.** If the policy provides no observable text that lets you judge this dimension, return `score: null` and explain in `justification`. Do NOT guess.

### Organisation context (input that produced the policy)

{context_narrative}

### Policy under evaluation

```
{policy_text}
```

### Required output (strict JSON, no prose outside)

```json
{{
  "criterion_id": "{criterion['id']}",
  "score": <integer 1..5 OR null>,
  "justification": "<1-3 sentences>",
  "evidence_quotes": [
    "<short verbatim quote from the policy>"
  ]
}}
```

`evidence_quotes` must contain up to 3 verbatim quotes from the policy that support your score. If the score is null, return an empty array.
"""


def call_judge(criterion: dict, context_narrative: str, policy_text: str
               ) -> tuple[dict, dict]:
    """Return (parsed_score_dict, raw_meta_dict)."""
    user = render_judge_user(criterion, context_narrative, policy_text)
    t0 = time.perf_counter()
    resp = _anthropic.messages.create(
        model=JUDGE_MODEL,
        max_tokens=JUDGE_MAX_TOKENS,
        system=JUDGE_SYSTEM,
        messages=[{"role": "user", "content": user}],
    )
    dt = time.perf_counter() - t0

    text_blocks = [b.text for b in resp.content if getattr(b, "type", "") == "text"]
    raw_text = "\n".join(text_blocks).strip()

    # Best-effort JSON extraction (judge is told to return strict JSON, but
    # occasionally wraps it in ```json fences).
    parsed: dict
    try:
        parsed = json.loads(raw_text)
    except json.JSONDecodeError:
        start = raw_text.find("{")
        end = raw_text.rfind("}")
        if start >= 0 and end > start:
            parsed = json.loads(raw_text[start:end + 1])
        else:
            parsed = {"score": None, "justification": "JUDGE_OUTPUT_UNPARSEABLE",
                      "evidence_quotes": [], "criterion_id": criterion["id"]}

    meta = {
        "model": resp.model,
        "input_tokens": resp.usage.input_tokens if resp.usage else None,
        "output_tokens": resp.usage.output_tokens if resp.usage else None,
        "stop_reason": resp.stop_reason,
        "latency_s": round(dt, 3),
        "raw_text": raw_text if "JUDGE_OUTPUT_UNPARSEABLE" in str(parsed) else None,
    }
    return parsed, meta


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--execute", action="store_true")
    ap.add_argument("--only", default="",
                    help="comma-separated config|ctx|policy filter (e.g. 'C1,ctx-H,P1')")
    ap.add_argument("--limit", type=int, default=0,
                    help="grade at most N artefacts (0 = all)")
    args = ap.parse_args()

    rubric = json.loads((GRADER_DIR / "rubric.json").read_text())
    criteria: list[dict] = rubric["criteria"]
    artefacts = list_artefacts()
    if not artefacts:
        print("No artefacts found in outputs/. Run run_generation.py first.")
        return 1

    # Filter
    only = {x.strip() for x in args.only.split(",") if x.strip()}
    if only:
        filtered = []
        for p in artefacts:
            slug = p.parent.parent.name
            ctx = p.parent.name
            policy_short = p.stem
            cfg = SLUG_TO_CONFIG.get(slug, slug)
            tags = {cfg, ctx, policy_short.upper()}
            # check overlap with --only
            if tags & only or any(o in (cfg, ctx, policy_short) for o in only):
                filtered.append(p)
        artefacts = filtered

    if args.limit > 0:
        artefacts = artefacts[:args.limit]

    print(f"Artefacts to grade: {len(artefacts)}  "
          f"(criteria: {len(criteria)}, total judge calls: {len(artefacts) * len(criteria)}) "
          f"[{'EXECUTE' if args.execute else 'dry-run'}]")

    if not args.execute:
        for p in artefacts:
            print(f"  [DRY] {p.relative_to(OUTPUTS_DIR)}")
        return 0

    # Pre-render contexts
    narratives = {ctx: render_context(CONTEXT_FILES[ctx]) for ctx in CONTEXT_FILES}

    log_path = SCORES_DIR / "grader_log.jsonl"
    SCORES_DIR.mkdir(parents=True, exist_ok=True)
    log = log_path.open("a")

    failures = []
    for ai, art_path in enumerate(artefacts, 1):
        rel = art_path.relative_to(OUTPUTS_DIR)
        try:
            fm, body = parse_artefact(art_path)
        except Exception as exc:
            print(f"[{ai}/{len(artefacts)}] {rel}  PARSE_FAIL: {exc}")
            failures.append((str(rel), "parse", str(exc)))
            continue

        cfg = fm["config"]
        ctx = fm["context_id"]
        policy_short = fm["policy_short"]

        out_dir = SCORES_DIR / CONFIG_SLUGS.get(cfg, cfg) / ctx
        out_dir.mkdir(parents=True, exist_ok=True)

        print(f"\n[{ai}/{len(artefacts)}] {cfg:7} {ctx} {fm['policy_id']} "
              f"({len(body)} chars)")

        # 1) code-based
        cb = run_code_checks(body, ctx)
        (out_dir / f"{policy_short}.codecheck.json").write_text(json.dumps(cb, indent=2))
        print(f"    code-based: {cb['checks_passed']}/{cb['checks_total']} checks pass")

        # 2) model-based, dimension-by-dimension
        scores: dict[str, dict] = {}
        for ci, crit in enumerate(criteria, 1):
            try:
                parsed, jmeta = call_judge(crit, narratives[ctx], body)
                scores[crit["id"]] = {"parsed": parsed, "judge_meta": jmeta}
                s = parsed.get("score")
                print(f"    judge {ci}/{len(criteria)} {crit['id']:32} score={s} "
                      f"({jmeta['input_tokens']} in / {jmeta['output_tokens']} out, "
                      f"{jmeta['latency_s']}s)")
            except Exception as exc:
                print(f"    judge {ci}/{len(criteria)} {crit['id']:32} FAIL: {exc}")
                scores[crit["id"]] = {"error": str(exc)}
                failures.append((str(rel), crit["id"], str(exc)))

        # 3) aggregate
        likert = [s["parsed"]["score"] for s in scores.values()
                  if "parsed" in s and isinstance(s["parsed"].get("score"), int)]
        aggregate = {
            "config": cfg,
            "context_id": ctx,
            "policy_id": fm["policy_id"],
            "policy_short": policy_short,
            "code_based": cb,
            "model_based": scores,
            "summary": {
                "likert_scores_present": len(likert),
                "likert_mean": round(sum(likert) / len(likert), 3) if likert else None,
                "code_checks_passed": cb["checks_passed"],
                "code_checks_total": cb["checks_total"],
            },
            "graded_at_unix": int(time.time()),
        }
        (out_dir / f"{policy_short}.aggregate.json").write_text(
            json.dumps(aggregate, indent=2, default=str))

        log.write(json.dumps({
            "i": ai, "artefact": str(rel),
            "config": cfg, "context": ctx, "policy": fm["policy_id"],
            "code_pass": cb["checks_passed"], "code_total": cb["checks_total"],
            "likert_mean": aggregate["summary"]["likert_mean"],
            "likert_scores_present": aggregate["summary"]["likert_scores_present"],
        }) + "\n")
        log.flush()

    log.close()

    print(f"\n=== summary ===")
    print(f"Artefacts graded: {len(artefacts)}")
    print(f"Failures:         {len(failures)}")
    for f in failures[:10]:
        print(f"  - {f[0]}  {f[1]}  {f[2]}")
    print(f"log: {log_path}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
