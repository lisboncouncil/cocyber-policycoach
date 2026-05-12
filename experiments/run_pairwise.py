#!/usr/bin/env python3
"""IWAPS 2026 — pairwise judge: C2 (Kimi K2.5) vs C2b (DeepSeek V3.2).

For each of the 10 matching policy+context pairs, sends both artefacts to
Claude Opus in a single call and asks for:
  - Per-criterion scores for A and B (1-5 or null)
  - Per-criterion winner + rationale
  - Overall verdict

Writes results to: results/pairwise_c2_vs_c2b.json
"""

from __future__ import annotations
import json
import sys
import time
from pathlib import Path

import anthropic
import yaml

ROOT = Path(__file__).resolve().parent
OUTPUTS_DIR = ROOT / "outputs"
SCORES_DIR = ROOT / "scores"
RESULTS_DIR = ROOT / "results"
CONTEXTS_DIR = ROOT / "contexts"
GRADER_DIR = ROOT / "grader"
PROMPTS_DIR = ROOT / "prompts"

sys.path.insert(0, str(PROMPTS_DIR))
from context_renderer import render as render_context  # type: ignore

JUDGE_MODEL = "claude-opus-4-7"
SECRETS = Path("/Users/erreclaudea/erre-claudia/secrets")
ANTHROPIC_KEY = (SECRETS / "anthropic_api_key_clodia_5").read_text().strip()
_anthropic = anthropic.Anthropic(api_key=ANTHROPIC_KEY)

CONTEXT_FILES = {
    "ctx-H": CONTEXTS_DIR / "hospital.yaml",
    "ctx-M": CONTEXTS_DIR / "military.yaml",
}

POLICIES = ["accesscontrol", "dataprot", "infosec", "ir", "password"]
CONTEXTS = ["ctx-H", "ctx-M"]

JUDGE_SYSTEM = (
    "You are an experienced cybersecurity policy auditor with 15+ years across "
    "healthcare and defence sectors. Deep working knowledge of NIST CSF 2.0, "
    "ISO/IEC 27001, GDPR, NIS2, NATO Information Security Policy, and Italian "
    "sector regulations. You evaluate two policy artefacts side by side. "
    "Be strict and evidence-driven. Output is a single JSON object. "
    "No commentary outside the JSON."
)


def load_artefact(cfg_slug: str, ctx: str, policy: str) -> str:
    p = OUTPUTS_DIR / cfg_slug / ctx / f"{policy}.md"
    text = p.read_text()
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        return text[end + 5:].lstrip("\n") if end >= 0 else text
    return text


def build_user_prompt(criteria: list[dict], context_narrative: str,
                      policy_a: str, policy_b: str) -> str:
    crit_block = "\n".join(
        f"- **{c['id']}** ({c['name']}): {c['definition']}" for c in criteria
    )
    anchor_block = "\n".join(
        f"  - {c['id']}: 1={c['anchors']['1'][:60]}…  5={c['anchors']['5'][:60]}…"
        for c in criteria
    )
    crit_ids = [c["id"] for c in criteria]
    score_template = {cid: {"score_A": "int|null", "score_B": "int|null",
                             "winner": "A|B|tie", "rationale": "1-2 sentences"}
                      for cid in crit_ids}

    return f"""You are comparing two cybersecurity policy documents (A and B) produced
for the same organisation by different AI systems.

### Organisation context

{context_narrative}

### Criteria (evaluate both policies on each)

{crit_block}

**Scoring anchors (1–5):**
{anchor_block}

Return `null` for score_A or score_B if the policy provides no observable
signal for that criterion (do not guess).

### Policy A

```
{policy_a}
```

### Policy B

```
{policy_b}
```

### Required output (strict JSON, no prose outside)

```json
{{
  "criteria": {json.dumps(score_template, indent=2)},
  "overall": {{
    "winner": "A|B|tie",
    "rationale": "2-4 sentences summarising the key differences"
  }}
}}
```

For `winner` use "A" if Policy A is clearly better overall, "B" if Policy B
is clearly better, "tie" if the gap is negligible.
"""


def call_judge(criteria: list[dict], context_narrative: str,
               policy_a: str, policy_b: str) -> tuple[dict, dict]:
    user = build_user_prompt(criteria, context_narrative, policy_a, policy_b)
    t0 = time.perf_counter()
    resp = _anthropic.messages.create(
        model=JUDGE_MODEL,
        max_tokens=3000,
        system=JUDGE_SYSTEM,
        messages=[{"role": "user", "content": user}],
    )
    dt = time.perf_counter() - t0

    text_blocks = [b.text for b in resp.content if getattr(b, "type", "") == "text"]
    raw_text = "\n".join(text_blocks).strip()

    parsed: dict
    try:
        parsed = json.loads(raw_text)
    except json.JSONDecodeError:
        start = raw_text.find("{")
        end = raw_text.rfind("}")
        if start >= 0 and end > start:
            parsed = json.loads(raw_text[start:end + 1])
        else:
            parsed = {"_parse_error": raw_text[:200]}

    meta = {
        "model": resp.model,
        "input_tokens": resp.usage.input_tokens if resp.usage else None,
        "output_tokens": resp.usage.output_tokens if resp.usage else None,
        "latency_s": round(dt, 3),
    }
    return parsed, meta


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--execute", action="store_true")
    args = ap.parse_args()

    rubric = json.loads((GRADER_DIR / "rubric.json").read_text())
    criteria: list[dict] = rubric["criteria"]

    pairs = [(ctx, pol) for ctx in CONTEXTS for pol in POLICIES]
    n = len(pairs)

    print(f"Pairs: {n}  (1 judge call each, ~{n} API calls) "
          f"[{'EXECUTE' if args.execute else 'dry-run'}]")

    if not args.execute:
        for ctx, pol in pairs:
            print(f"  [DRY] C2 vs C2b  {ctx}  {pol}")
        return 0

    narratives = {ctx: render_context(CONTEXT_FILES[ctx]) for ctx in CONTEXT_FILES}
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    results = []
    for i, (ctx, pol) in enumerate(pairs, 1):
        try:
            policy_a = load_artefact("c2_private_rag", ctx, pol)
            policy_b = load_artefact("c2b_private_rag_deepseek", ctx, pol)
        except FileNotFoundError as e:
            print(f"[{i}/{n}] SKIP — {e}")
            continue

        print(f"[{i}/{n}] C2 vs C2b  {ctx}  {pol}  "
              f"(A={len(policy_a)} B={len(policy_b)} chars) ...", end=" ", flush=True)

        try:
            parsed, meta = call_judge(criteria, narratives[ctx], policy_a, policy_b)
            overall_winner = parsed.get("overall", {}).get("winner", "?")
            print(f"winner={overall_winner}  "
                  f"({meta['input_tokens']} in / {meta['output_tokens']} out, "
                  f"{meta['latency_s']}s)")
        except Exception as exc:
            print(f"FAIL: {exc}")
            parsed, meta = {"_error": str(exc)}, {}

        results.append({
            "ctx": ctx, "policy": pol,
            "config_A": "C2", "config_B": "C2b",
            "result": parsed, "meta": meta,
        })

    out_path = RESULTS_DIR / "pairwise_c2_vs_c2b.json"
    out_path.write_text(json.dumps(results, indent=2, default=str))
    print(f"\nResults written to {out_path}")

    # Quick summary
    winners = [r["result"].get("overall", {}).get("winner") for r in results
               if "result" in r and "_error" not in r.get("result", {})]
    from collections import Counter
    wc = Counter(winners)
    print(f"Overall winners: A(C2)={wc.get('A',0)}  B(C2b)={wc.get('B',0)}  tie={wc.get('tie',0)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
