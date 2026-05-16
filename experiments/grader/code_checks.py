#!/usr/bin/env python3
"""IWAPS 2026 — code-based graders.

Deterministic, model-free checks against a generated policy. Run BEFORE the
LLM-judge so we have an objective baseline that does not depend on any model.

The Anthropic eval blueprint recommends combining code-based, model-based,
and human graders. Code-based graders are fast, reproducible, and immune to
LLM-judge non-determinism, but they only see surface signals — they cannot
tell whether a citation is *correct*, only whether it *exists*. This file
implements the surface signals; depth is left to the LLM-judge.

Output is a single JSON-serialisable dict with three sections:
  - "metrics": raw counts and ratios
  - "checks":  named checks with pass/fail booleans
  - "summary": aggregated 0-1 score plus by-section partial scores

Usage:
    from code_checks import run_code_checks
    result = run_code_checks(policy_text, context_id="ctx-H")
"""

from __future__ import annotations
import json
import re
import sys
from pathlib import Path
from typing import Any


# ---------------------------------------------------------------------------
# Citation patterns
# ---------------------------------------------------------------------------

# Patterns are conservative: they should hit a real citation but tolerate
# ordinary stylistic variation. Each pattern is case-insensitive.
INSTITUTIONAL_SOURCES = {
    "ENISA":           r"\benisa\b",
    "NATO_CCDCOE":     r"\bccdcoe\b|\bnato\s+(?:ccdcoe|cooperative\s+cyber\s+defence)",
    "WEF":             r"\bworld\s+economic\s+forum\b|\bwef\b",
    "INCIBE":          r"\bincibe\b",
    "CyberPeace":      r"\bcyberpeace\s+institute\b",
    "GFCE":            r"\bgfce\b|\bglobal\s+forum\s+on\s+cyber\s+expertise\b",
    "NIST":            r"\bnist\b",
    "EC_JANUS":        r"\bjanus\s+project\b|\beuropean\s+commission\s+janus\b",
    "CyFun":           r"\bcyfun\b|\bcybersecurity\s+fundamentals\b",
}

NORMATIVE_FRAMEWORKS = {
    "NIST_CSF_2_0":    r"\bnist\s+csf\s*2(?:\.0)?\b|\bcybersecurity\s+framework\s*2(?:\.0)?\b",
    "ISO_27001":       r"\biso[/\-\s]*(?:iec\s*)?27001(?::?\s*2022)?\b",
    "ISO_27002":       r"\biso[/\-\s]*(?:iec\s*)?27002(?::?\s*2022)?\b",
    "GDPR":            r"\bgdpr\b|\bregulation\s*\(eu\)\s*2016/679\b",
    "NIS2":            r"\bnis\s*2\b|\bdirective\s*\(eu\)\s*2022/2555\b",
    "AI_Act":          r"\bai\s+act\b|\bregulation\s*\(eu\)\s*2024/1689\b",
    "AGID":            r"\bagid\b",
    "Codice_Privacy":  r"\bcodice\s+(?:in\s+materia\s+di\s+protezione\s+dei\s+dati\s+personali|privacy)\b|\bd\.lgs\.?\s*196/2003\b",
    "NATO_IS_Policy":  r"\bc[\-\s]*m\s*\(?2002\)?\s*49\b|\bnato\s+information\s+security\s+policy\b",
    "AC_35_D_1015":    r"\bac/?35[\-\s]*d/?1015\b",
    "AC_35_D_1029":    r"\bac/?35[\-\s]*d/?1029\b",
    "AJP_3_20":        r"\bajp[\-\s]*3\.?20\b",
    "Romanian_CSL":    r"\blaw\s+58/2019\b|\bromanian\s+cybersecurity\s+law\b",
    "SOFA":            r"\bstatus\s+of\s+forces\s+agreement\b|\bsofa\b",
}

# Patterns that target individual clauses or control identifiers.
# Used for C6_source_attribution (per-control attribution).
CLAUSE_LEVEL_PATTERNS = [
    # GDPR articles: "Art. 32(1)(b)", "Article 33", "Art. 5"
    r"\bart(?:\.|icle)?\s*\d{1,3}(?:\(\d+\))?(?:\([a-z]\))?",
    # ISO 27001 Annex A controls: "A.5.10", "A.8.16"
    r"\bA\.\s*\d{1,2}\.\s*\d{1,2}\b",
    # NIST CSF subcategories: "ID.AM-1", "PR.AC-1"
    r"\b[A-Z]{2}\.[A-Z]{2}-\d+\b",
    # NIST SP references: "SP 800-53 AC-2"
    r"\b(?:SP\s*)?800[\-\s]*\d{1,3}\b",
    # NATO directive references: "AC/322-D(2017)0009"
    r"\bAC/\d{3}[\-\s]*D\(?\d{4}\)?\d+\b",
]

# Patterns indicating *honest* refusal to fabricate (positive signal for C3).
NO_CITATION_HONESTY_PATTERNS = [
    r"\bno\s+citation\s+available\b",
    r"\bunsupported\s+(?:by|in)\s+(?:the\s+)?(?:retrieved|knowledge\s+base)\b",
    r"\bnot\s+sourced\b",
    r"\bcitation\s+pending\b",
    r"\b\[citation\s+needed\]\b",
]

# Generic boilerplate phrases that signal lack of contextualisation.
BOILERPLATE_PATTERNS = [
    r"\bthe\s+organi[sz]ation\s+shall\s+(?:implement|maintain|ensure|establish)\s+appropriate\s+(?:security\s+)?measures\b",
    r"\ball\s+employees\s+(?:must|shall)\s+comply\s+with\s+(?:this\s+)?policy\b",
    r"\bregular\s+(?:reviews|assessments)\s+(?:shall|will)\s+be\s+conducted\b",
]

# Standard policy section headers we expect (Markdown # / ## / ###).
EXPECTED_SECTIONS = [
    "purpose", "scope", "roles", "responsibilities", "principles",
    "requirements", "controls", "exceptions", "monitoring", "review",
    "references",
]

# Mandatory obligations per context.
CONTEXT_OBLIGATIONS = {
    "ctx-H": {
        "breach_notification_72h": r"\b72\s*hours?\b|\bgdpr\s+art(?:\.|icle)?\s*33\b",
        "dpia": r"\bdpia\b|\bdata\s+protection\s+impact\s+assessment\b",
        "special_category_data": r"\bspecial\s+categor(?:y|ies)\s+(?:of\s+)?data\b|\bhealth\s+data\b|\bart(?:\.|icle)?\s*9\b",
        "data_retention": r"\bretention\s+(?:period|policy|schedule)\b|\bdata\s+retention\b",
        "access_logs": r"\baccess\s+logs?\b|\baudit\s+(?:logs?|trail)\b",
        "patient_safety": r"\bpatient\s+safety\b|\bclinical\s+(?:workflow|operation)s?\b",
        "nis2_essential_entity": r"\bessential\s+entity\b|\bnis\s*2\b",
    },
    "ctx-M": {
        "classification_handling": r"\bclassification\s+(?:handling|management)\b|\bclassified\s+information\b|\bn[us][rs]?\b",
        "need_to_know": r"\bneed[\-\s]to[\-\s]know\b",
        "comsec": r"\bcomsec\b|\bcommunications\s+security\b",
        "dual_key": r"\bdual[\-\s]key\b|\btwo[\-\s]person\s+integrity\b",
        "ncirc_reporting": r"\bncirc\b|\bnato\s+computer\s+incident\s+response\b",
        "spillage": r"\bspillage\b|\bcross[\-\s]domain\s+(?:transfer|contamination)\b",
        "tempest": r"\btempest\b",
        "host_nation": r"\bhost[\-\s]nation\b|\bsofa\b",
    },
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _match_count(pattern: str, text: str) -> int:
    return len(re.findall(pattern, text, flags=re.IGNORECASE))


def _any_match(patterns: list[str], text: str) -> int:
    return sum(_match_count(p, text) for p in patterns)


def _section_headers(md: str) -> list[str]:
    """Return lowercased text of every Markdown header in the policy."""
    return [m.group(1).strip().lower()
            for m in re.finditer(r"(?m)^\s*#{1,6}\s+(.+?)\s*$", md)]


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def run_code_checks(policy_text: str, context_id: str) -> dict[str, Any]:
    """Run all code-based checks on a single generated policy."""
    text = policy_text or ""
    word_count = len(re.findall(r"\b\w+\b", text))
    char_count = len(text)
    headers = _section_headers(text)
    header_blob = " | ".join(headers)

    # --- citations ---
    institutional_hits = {k: _match_count(p, text) for k, p in INSTITUTIONAL_SOURCES.items()}
    framework_hits = {k: _match_count(p, text) for k, p in NORMATIVE_FRAMEWORKS.items()}
    clause_hits = sum(_match_count(p, text) for p in CLAUSE_LEVEL_PATTERNS)
    honesty_hits = _any_match(NO_CITATION_HONESTY_PATTERNS, text)
    boilerplate_hits = _any_match(BOILERPLATE_PATTERNS, text)

    distinct_institutional = sum(1 for v in institutional_hits.values() if v)
    distinct_frameworks = sum(1 for v in framework_hits.values() if v)

    # --- structural sections ---
    section_presence = {
        s: any(s in h for h in headers) or bool(re.search(rf"\b{s}\b", text, re.IGNORECASE))
        for s in EXPECTED_SECTIONS
    }
    sections_found = sum(1 for v in section_presence.values() if v)

    # --- header block markers ---
    header_block = {
        "organization_name":   bool(re.search(r"\borgani[sz]ation\b\s*[:\-]", text, re.IGNORECASE)),
        "effective_date":      bool(re.search(r"\beffective\s+date\b\s*[:\-]", text, re.IGNORECASE)),
        "policy_owner":        bool(re.search(r"\bpolicy\s+owner\b\s*[:\-]", text, re.IGNORECASE)),
        "review_cycle":        bool(re.search(r"\breview\s+(?:cycle|frequency)\b\s*[:\-]", text, re.IGNORECASE)),
    }
    header_block_score = sum(header_block.values()) / 4

    # --- mandatory obligations for the context ---
    obligations = CONTEXT_OBLIGATIONS.get(context_id, {})
    obligation_hits = {k: _match_count(p, text) for k, p in obligations.items()}
    obligations_present = sum(1 for v in obligation_hits.values() if v)
    obligations_total = max(len(obligations), 1)

    # --- length sanity ---
    # Floor lowered to 300 because Password Policy and similar focused
    # policies can legitimately be shorter than a top-level InfoSec policy.
    length_ok = 300 <= word_count <= 8000
    length_band = (
        "too_short" if word_count < 300
        else "too_long" if word_count > 8000
        else "ok"
    )

    # --- per-criterion partial scores in 0..1 (used to weight LLM-judge later) ---
    partial = {
        "C1_content_quality_section_coverage": sections_found / len(EXPECTED_SECTIONS),
        "C1_content_quality_header_block":     header_block_score,
        "C2_contextual_adaptation_proxy":      max(0.0, 1.0 - boilerplate_hits / 5),
        "C3_evidence_citation_breadth":        min(1.0, (distinct_institutional + distinct_frameworks) / 6),
        "C3_honesty_bonus":                    1.0 if honesty_hits else 0.0,
        "C5_regulatory_alignment_coverage":    min(1.0, distinct_frameworks / 4),
        "C6_source_attribution_clauses":       min(1.0, clause_hits / 10),
        "C7_resource_consideration_obligations": obligations_present / obligations_total,
        "length_ok":                           1.0 if length_ok else 0.0,
    }

    # --- named pass/fail checks (for run reports) ---
    checks = {
        "has_minimum_word_count":      word_count >= 300,
        "not_excessive_word_count":    word_count <= 8000,
        "has_header_block":            header_block_score >= 0.5,
        "has_section_purpose":         section_presence["purpose"],
        "has_section_scope":           section_presence["scope"],
        "has_section_roles":           section_presence["roles"] or section_presence["responsibilities"],
        "has_section_monitoring":      section_presence["monitoring"] or section_presence["review"],
        "has_section_references":      section_presence["references"],
        "has_at_least_one_framework":  distinct_frameworks >= 1,
        "has_clause_level_attribution": clause_hits >= 1,
        "boilerplate_below_threshold": boilerplate_hits <= 3,
        "context_obligations_majority": obligations_present >= max(1, obligations_total // 2),
    }

    return {
        "context_id": context_id,
        "metrics": {
            "char_count": char_count,
            "word_count": word_count,
            "section_headers_found": len(headers),
            "section_headers_sample": headers[:12],
            "section_presence": section_presence,
            "header_block": header_block,
            "header_block_score": round(header_block_score, 3),
            "institutional_hits": institutional_hits,
            "distinct_institutional": distinct_institutional,
            "framework_hits": framework_hits,
            "distinct_frameworks": distinct_frameworks,
            "clause_level_citation_count": clause_hits,
            "honesty_hits": honesty_hits,
            "boilerplate_hits": boilerplate_hits,
            "obligation_hits": obligation_hits,
            "obligations_present": obligations_present,
            "obligations_total": obligations_total,
            "length_band": length_band,
        },
        "checks": checks,
        "partial_scores": {k: round(v, 3) for k, v in partial.items()},
        "checks_passed": sum(1 for v in checks.values() if v),
        "checks_total": len(checks),
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _self_test() -> None:
    """Quick self-test using the C1 smoke output as a sample."""
    smoke = Path(__file__).resolve().parents[1] / "c1_smoke.json"
    if not smoke.exists():
        print("self-test: c1_smoke.json not found, skipping", file=sys.stderr)
        return
    sample = json.loads(smoke.read_text()).get("answer") or ""
    if not sample:
        print("self-test: empty sample, skipping", file=sys.stderr)
        return
    res = run_code_checks(sample, context_id="ctx-H")
    print(json.dumps(res, indent=2))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        _self_test()
    elif len(sys.argv) == 3:
        policy_text = Path(sys.argv[1]).read_text()
        ctx_id = sys.argv[2]
        print(json.dumps(run_code_checks(policy_text, ctx_id), indent=2))
    else:
        print(f"usage: {sys.argv[0]} [<policy_file> <ctx-H|ctx-M>]", file=sys.stderr)
        sys.exit(2)
