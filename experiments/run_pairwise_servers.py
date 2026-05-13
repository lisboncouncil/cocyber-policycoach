#!/usr/bin/env python3
"""Pairwise live test: two PolicyCoach servers head-to-head.

For each scenario: runs a full interview on server A and server B, then
judges the two resulting policies with Claude Opus 4.7.

Usage:
    python3 run_pairwise_servers.py                   # dry-run
    python3 run_pairwise_servers.py --execute         # run all scenarios
    python3 run_pairwise_servers.py --execute --quick # 4 scenarios only
"""

from __future__ import annotations
import json
import re
import time
import uuid
import difflib
import argparse
from datetime import datetime
from pathlib import Path

import requests
import anthropic

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
SERVER_A = "http://localhost:5050"
SERVER_B = "http://localhost:5051"
MODEL_A   = "Kimi K2.5 (reasoning)"
MODEL_B   = "Kimi K2.6 (no-reasoning)"

JUDGE_MODEL      = "claude-opus-4-7"
ANSWER_MODEL     = "claude-haiku-4-5-20251001"
SIMILARITY_THRESHOLD = 0.75
MAX_TURNS        = 25
POLICY_LEN_THRESHOLD = 800

ROOT        = Path(__file__).resolve().parent
RESULTS_DIR = ROOT / "results"
SECRETS     = Path("/Users/erreclaudea/erre-claudia/secrets")
ANTHROPIC_KEY = (SECRETS / "anthropic_api_key_clodia_5").read_text().strip()

# ---------------------------------------------------------------------------
# Scenarios  (quick = first 4, full = all 6)
# ---------------------------------------------------------------------------
SCENARIOS = [
    {
        "id": "ctx-H_password",
        "policy_type": "Password Policy",
        "context_label": "Italian public hospital, 200 staff, Cagliari",
        "profile": {
            "organisation": "Ospedale Regionale di Cagliari",
            "sector": "public healthcare",
            "country": "Italy",
            "employees": 200,
            "regulations": "GDPR, NIS2, Italian healthcare privacy law",
            "it_maturity": "medium — legacy EHR (Dedalus), flat network, on-prem AD",
            "current_policy": "no formal password policy",
            "cloud": "none, on-premise only",
        },
    },
    {
        "id": "ctx-H_dataprot",
        "policy_type": "Data Protection Policy",
        "context_label": "Italian public hospital, 200 staff, Cagliari",
        "profile": {
            "organisation": "Ospedale Regionale di Cagliari",
            "sector": "public healthcare",
            "country": "Italy",
            "employees": 200,
            "regulations": "GDPR Art.9, NIS2, Italian healthcare privacy law",
            "it_maturity": "medium — legacy EHR, no DPO on staff",
            "current_policy": "basic GDPR notice, no formal DP policy",
            "cloud": "none, on-premise only",
        },
    },
    {
        "id": "ctx-M_ir",
        "policy_type": "Incident Response Policy",
        "context_label": "NATO detachment, Romania, 85 personnel",
        "profile": {
            "organisation": "NATO Forward Presence Detachment — Romania",
            "sector": "defence / military",
            "country": "Romania (multinational NATO base)",
            "employees": 85,
            "regulations": "NATO Information Security Policy (C-M(2002)49), GDPR for unclassified personal data",
            "it_maturity": "high — classified network, COMSEC officer, J6",
            "current_policy": "NATO standard procedures; needs local IR policy adaptation",
            "cloud": "no public cloud; NATO SECRET and NATO RESTRICTED systems",
        },
    },
    {
        "id": "ctx-M_accesscontrol",
        "policy_type": "Access Control Policy",
        "context_label": "NATO detachment, Romania, 85 personnel",
        "profile": {
            "organisation": "NATO Forward Presence Detachment — Romania",
            "sector": "defence / military",
            "country": "Romania (multinational NATO base)",
            "employees": 85,
            "regulations": "NATO Information Security Policy, need-to-know principle",
            "it_maturity": "high — classified network, identity management, CAC/PIV cards",
            "current_policy": "NATO baseline access controls; local policy needed",
            "cloud": "no public cloud",
        },
    },
    {
        "id": "ctx-H_ir",
        "policy_type": "Incident Response Policy",
        "context_label": "Italian public hospital, 200 staff, Cagliari",
        "profile": {
            "organisation": "Ospedale Regionale di Cagliari",
            "sector": "public healthcare",
            "country": "Italy",
            "employees": 200,
            "regulations": "GDPR, NIS2 (critical entity), Italian CSIRT notification rules",
            "it_maturity": "medium — no CISO, IT coordinator only",
            "current_policy": "no IR policy; informal escalation procedures",
            "cloud": "none",
        },
    },
    {
        "id": "ctx-M_password",
        "policy_type": "Password Policy",
        "context_label": "NATO detachment, Romania, 85 personnel",
        "profile": {
            "organisation": "NATO Forward Presence Detachment — Romania",
            "sector": "defence / military",
            "country": "Romania (multinational NATO base)",
            "employees": 85,
            "regulations": "NATO Information Security Policy, IA standards",
            "it_maturity": "high — classified and unclassified networks, separate domains",
            "current_policy": "NATO baseline password requirements; local policy needed",
            "cloud": "no public cloud",
        },
    },
]

JUDGE_SYSTEM = (
    "You are an experienced cybersecurity policy auditor with 15+ years across "
    "healthcare and defence sectors. Deep working knowledge of NIST CSF 2.0, "
    "ISO/IEC 27001, GDPR, NIS2, NATO Information Security Policy, and Italian "
    "sector regulations. You evaluate two policy artefacts side by side. "
    "Be strict and evidence-driven. Output is a single JSON object. "
    "No commentary outside the JSON."
)

CRITERIA = [
    {"id": "content_quality",       "name": "Content quality",       "weight": 1},
    {"id": "contextual_adaptation", "name": "Contextual adaptation", "weight": 1},
    {"id": "evidence_citation",     "name": "Evidence citation",     "weight": 1},
    {"id": "implementability",      "name": "Implementability",      "weight": 1},
    {"id": "regulatory_alignment",  "name": "Regulatory alignment",  "weight": 1},
    {"id": "source_attribution",    "name": "Source attribution",    "weight": 1},
    {"id": "resource_consideration","name": "Resource consideration","weight": 1},
]

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def extract_questions(text: str) -> list[str]:
    clean = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
    clean = re.sub(r'\*\*([^*]+)\*\*', r'\1', clean)
    clean = re.sub(r'\([^)]*\?[^)]*\)', '', clean)
    sentences = re.split(r'(?<=[.?!])\s+', clean.strip())
    return [s.strip() for s in sentences if s.strip().endswith('?')]


def question_similarity(a: str, b: str) -> float:
    return difflib.SequenceMatcher(None, a.lower().strip(), b.lower().strip()).ratio()


def is_policy(text: str) -> bool:
    has_header = any(line.startswith(("# ", "## ", "### ")) for line in text.splitlines())
    return len(text) >= POLICY_LEN_THRESHOLD or has_header


def chat(server: str, message: str, session_id: str) -> str:
    resp = requests.post(
        f"{server}/conversation",
        json={"message": message, "sessionId": session_id},
        timeout=180,
    )
    resp.raise_for_status()
    return resp.json().get("answer", "").strip()


def generate_answer(question: str, profile: dict, client: anthropic.Anthropic) -> str:
    ctx = "\n".join(f"  {k}: {v}" for k, v in profile.items())
    resp = client.messages.create(
        model=ANSWER_MODEL,
        max_tokens=200,
        messages=[{"role": "user", "content": (
            "You are being interviewed by a cybersecurity consultant.\n\n"
            f"Your organisation profile:\n{ctx}\n\n"
            f"Question: {question}\n\n"
            "Answer briefly (1-3 sentences). Be specific. No preamble."
        )}],
    )
    return resp.content[0].text.strip()


def interview(server: str, profile: dict, client: anthropic.Anthropic) -> str | None:
    """Run a full interview on `server` and return the final policy text, or None."""
    sid = str(uuid.uuid4())
    asked: list[str] = []
    message = "hello"

    for _ in range(MAX_TURNS):
        try:
            reply = chat(server, message, sid)
        except Exception as e:
            print(f"    [chat error] {e}")
            return None

        if is_policy(reply):
            return reply

        new_qs = extract_questions(reply)
        duplicate = any(
            question_similarity(nq, prev) >= SIMILARITY_THRESHOLD
            for prev in asked for nq in new_qs
        )
        if not duplicate:
            asked.extend(new_qs)

        message = generate_answer(reply, profile, client)
        time.sleep(0.3)

    return None


def judge_pair(policy_a: str, policy_b: str, scenario_id: str,
               client: anthropic.Anthropic) -> dict:
    crit_ids = [c["id"] for c in CRITERIA]
    score_tpl = {cid: {"score_A": "int|null", "score_B": "int|null",
                        "winner": "A|B|tie", "rationale": "1-2 sentences"}
                 for cid in crit_ids}
    prompt = f"""Compare two cybersecurity policies (A and B) for scenario: {scenario_id}.

### Policy A
```
{policy_a[:4000]}
```

### Policy B
```
{policy_b[:4000]}
```

### Criteria
{chr(10).join(f"- **{c['id']}**: {c['name']}" for c in CRITERIA)}

### Required output (strict JSON)
```json
{{
  "criteria": {json.dumps(score_tpl, indent=2)},
  "overall": {{
    "winner": "A|B|tie",
    "rationale": "2-4 sentences"
  }}
}}
```
"""
    resp = client.messages.create(
        model=JUDGE_MODEL,
        max_tokens=3000,
        system=JUDGE_SYSTEM,
        messages=[{"role": "user", "content": prompt}],
    )
    raw = resp.content[0].text.strip()
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        s, e = raw.find("{"), raw.rfind("}")
        if s >= 0 and e > s:
            return json.loads(raw[s:e+1])
        return {"_parse_error": raw[:200]}

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--execute", action="store_true")
    ap.add_argument("--quick", action="store_true", help="Run first 4 scenarios only")
    args = ap.parse_args()

    scenarios = SCENARIOS[:4] if args.quick else SCENARIOS
    mode = "EXECUTE" if args.execute else "dry-run"
    print(f"Pairwise: {MODEL_A} (:{SERVER_A.split(':')[-1]}) vs "
          f"{MODEL_B} (:{SERVER_B.split(':')[-1]})")
    print(f"Scenarios: {len(scenarios)}  [{mode}]")

    if not args.execute:
        for s in scenarios:
            print(f"  [DRY] {s['id']} — {s['policy_type']}")
        return 0

    client = anthropic.Anthropic(api_key=ANTHROPIC_KEY)
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_path = RESULTS_DIR / f"pairwise_servers_{ts}.json"

    results = []
    wins = {"A": 0, "B": 0, "tie": 0, "error": 0}

    for i, sc in enumerate(scenarios, 1):
        print(f"\n[{i}/{len(scenarios)}] {sc['id']} — {sc['policy_type']}")

        print(f"  Interviewing {MODEL_A} ...", end=" ", flush=True)
        t0 = time.perf_counter()
        policy_a = interview(SERVER_A, sc["profile"], client)
        ta = round(time.perf_counter() - t0, 1)
        print(f"{len(policy_a) if policy_a else 'FAIL'} chars  {ta}s")

        print(f"  Interviewing {MODEL_B} ...", end=" ", flush=True)
        t0 = time.perf_counter()
        policy_b = interview(SERVER_B, sc["profile"], client)
        tb = round(time.perf_counter() - t0, 1)
        print(f"{len(policy_b) if policy_b else 'FAIL'} chars  {tb}s")

        if not policy_a or not policy_b:
            print("  SKIP — one server failed to produce a policy")
            wins["error"] += 1
            results.append({"id": sc["id"], "error": "missing policy"})
            continue

        print(f"  Judging ...", end=" ", flush=True)
        verdict = judge_pair(policy_a, policy_b, sc["id"], client)
        winner = verdict.get("overall", {}).get("winner", "?")
        rationale = verdict.get("overall", {}).get("rationale", "")
        wins[winner] = wins.get(winner, 0) + 1
        print(f"winner={winner}")
        print(f"  → {rationale[:120]}")

        results.append({
            "id": sc["id"],
            "policy_type": sc["policy_type"],
            "model_A": MODEL_A,
            "model_B": MODEL_B,
            "len_A": len(policy_a),
            "len_B": len(policy_b),
            "verdict": verdict,
        })
        time.sleep(0.5)

    # Summary
    print(f"\n{'='*60}")
    print(f"RESULTS  A={MODEL_A}  B={MODEL_B}")
    print(f"  A wins : {wins.get('A', 0)}")
    print(f"  B wins : {wins.get('B', 0)}")
    print(f"  Ties   : {wins.get('tie', 0)}")
    print(f"  Errors : {wins.get('error', 0)}")

    out_path.write_text(json.dumps(results, indent=2, default=str))
    print(f"\nResults → {out_path}")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
