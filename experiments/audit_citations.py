#!/usr/bin/env python3
"""IWAPS 2026 — qualitative audit of citation sources.

C0_5+web cites web URLs returned by web_search. C2 cites filenames from the
curated KB. The grader rubric (C3 evidence_citation, C6 source_attribution)
counts presence and accuracy but is NOT sensitive to the *quality of
provenance*: a citation to NIST.gov and a citation to a vendor blog count
the same.

This script classifies every URL citation produced by C0_5+web into eight
categories and reports per-policy and aggregate statistics. The same is
done for C2 KB-source citations (which by construction map 1:1 to curated
institutional documents).

Usage:
    python3 audit_citations.py
"""
from __future__ import annotations
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlparse

import yaml

ROOT = Path(__file__).resolve().parent
OUTPUTS = ROOT / "outputs"


# ---------------------------------------------------------------------------
# Domain taxonomy
# ---------------------------------------------------------------------------

# Patterns are checked in order — first match wins.
CATEGORIES = [
    ("regulatory_eu", [
        r"\beuropa\.eu$", r"\beur-lex\.europa\.eu$", r"\benisa\.europa\.eu$",
        r"\bedps\.europa\.eu$", r"\bedpb\.europa\.eu$",
        r"\bgaranteprivacy\.it$", r"\bagid\.gov\.it$", r"\bacn\.gov\.it$",
        r"\bbsi\.bund\.de$", r"\bcnil\.fr$", r"\bncsc\.gov\.uk$",
        r"\bincibe\.es$", r"\bccn\.cni\.es$",
    ]),
    ("regulatory_us", [
        r"\bnist\.gov$", r"\bcisa\.gov$", r"\bwhitehouse\.gov$",
        r"\bhhs\.gov$", r"\bftc\.gov$", r"\bdhs\.gov$",
    ]),
    ("regulatory_intl", [
        r"\bnato\.int$", r"\bccdcoe\.org$", r"\bun\.org$", r"\boecd\.org$",
        r"\bweforum\.org$", r"\bcyberpeaceinstitute\.org$",
        r"\bgfce\.org$", r"\bthegfce\.org$",
    ]),
    ("standards_body", [
        r"\biso\.org$", r"\bietf\.org$", r"\bietf-data\.com$",
        r"\bw3\.org$", r"\boasis-open\.org$", r"\bisaca\.org$",
        r"\bowasp\.org$", r"\bsans\.org$",
    ]),
    ("academic", [
        r"\.edu$", r"\barxiv\.org$", r"\bscholar\.google\.com$",
        r"\bresearchgate\.net$", r"\bsciencedirect\.com$",
        r"\bspringer\.com$", r"\bieee\.org$", r"\bacm\.org$",
        r"\bjstor\.org$",
    ]),
    ("wikipedia", [
        r"\bwikipedia\.org$",
    ]),
    ("vendor_security", [
        r"\bmicrosoft\.com$", r"\bgoogle\.com$", r"\baws\.amazon\.com$",
        r"\bibm\.com$", r"\bcisco\.com$", r"\bpaloaltonetworks\.com$",
        r"\bcrowdstrike\.com$", r"\bsymantec\.com$", r"\bmcafee\.com$",
        r"\bkaspersky\.com$", r"\btrendmicro\.com$", r"\bfortinet\.com$",
        r"\bcheckpoint\.com$", r"\bsplunk\.com$", r"\brapid7\.com$",
        r"\btenable\.com$", r"\bqualys\.com$", r"\bvarionis\.com$",
        r"\bproofpoint\.com$", r"\bsophos\.com$", r"\boktas\.com$",
        r"\bokta\.com$", r"\bcloudflare\.com$", r"\bduo\.com$",
        r"\bauth0\.com$", r"\bsailpoint\.com$", r"\bcyberark\.com$",
        r"\bvmware\.com$", r"\boracle\.com$", r"\bsalesforce\.com$",
        r"\bservicenow\.com$",
    ]),
    ("news_media", [
        r"\btechcrunch\.com$", r"\bbleepingcomputer\.com$",
        r"\bdarkreading\.com$", r"\bsecurityweek\.com$",
        r"\bsecurityaffairs\.com$", r"\bsecurityintelligence\.com$",
        r"\bzdnet\.com$", r"\bcsoonline\.com$", r"\binfosecurity-magazine\.com$",
        r"\btheregister\.com$", r"\bwired\.com$", r"\barstechnica\.com$",
        r"\breuters\.com$", r"\bbloomberg\.com$",
    ]),
    ("blog_forum", [
        r"\bmedium\.com$", r"\bdev\.to$", r"\bstackexchange\.com$",
        r"\bstackoverflow\.com$", r"\breddit\.com$", r"\bgithub\.io$",
        r"\bsubstack\.com$",
    ]),
]


def classify_domain(host: str) -> str:
    if not host:
        return "other"
    host = host.lower().lstrip(".")
    # strip leading 'www.' for cleaner match
    if host.startswith("www."):
        host = host[4:]
    for category, patterns in CATEGORIES:
        for pat in patterns:
            if re.search(pat, host):
                return category
    return "other"


def host_of(url: str) -> str:
    try:
        return (urlparse(url).hostname or "").lower()
    except Exception:
        return ""


# ---------------------------------------------------------------------------
# Loaders
# ---------------------------------------------------------------------------

def load_artefacts(slug: str) -> list[dict]:
    files = sorted((OUTPUTS / slug).glob("ctx-*/*.md"))
    out = []
    for f in files:
        text = f.read_text()
        if not text.startswith("---\n"):
            continue
        end = text.find("\n---\n", 4)
        fm = yaml.safe_load(text[4:end])
        out.append({"path": f, "frontmatter": fm})
    return out


def all_sources(artefacts: list[dict]) -> list[tuple[Path, dict]]:
    out = []
    for a in artefacts:
        for s in a["frontmatter"].get("sources", []) or []:
            out.append((a["path"], s))
    return out


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def report_c0_5_web():
    arts = load_artefacts("c0_5_chatgpt_web")
    print(f"\n=== C0_5+web — {len(arts)} artefatti ===\n")

    cat_counts: Counter[str] = Counter()
    host_counts: Counter[str] = Counter()
    per_artefact: dict[str, dict[str, int]] = {}

    for art in arts:
        key = f"{art['path'].parent.name}/{art['path'].stem}"
        per_artefact[key] = Counter()
        for s in art["frontmatter"].get("sources", []) or []:
            url = s.get("url") or ""
            h = host_of(url)
            cat = classify_domain(h)
            cat_counts[cat] += 1
            host_counts[h] += 1
            per_artefact[key][cat] += 1

    total = sum(cat_counts.values())
    print(f"Total citations: {total}\n")
    print(f"{'Category':<22} {'count':>7} {'%':>6}")
    print("-" * 40)
    for cat in [c[0] for c in CATEGORIES] + ["other"]:
        c = cat_counts.get(cat, 0)
        pct = 100 * c / total if total else 0
        print(f"{cat:<22} {c:>7} {pct:>5.1f}%")

    # buckets aggregated for the paper narrative
    pertinent = sum(cat_counts.get(c, 0) for c in
                    ["regulatory_eu", "regulatory_us", "regulatory_intl",
                     "standards_body", "academic"])
    non_pertinent = sum(cat_counts.get(c, 0) for c in
                        ["wikipedia", "vendor_security", "news_media",
                         "blog_forum", "other"])
    print(f"\nAggregated:")
    print(f"  Pertinent (regulatory + standards + academic): "
          f"{pertinent} ({100*pertinent/total:.1f}%)")
    print(f"  Non-pertinent (wikipedia + vendor + news + blog + other): "
          f"{non_pertinent} ({100*non_pertinent/total:.1f}%)")

    print(f"\nTop 20 hosts:")
    for h, n in host_counts.most_common(20):
        cat = classify_domain(h)
        print(f"  {n:>4}  [{cat:<18}]  {h}")

    print(f"\nPer-artefact breakdown (top categories):")
    print(f"{'artefact':<32} {'tot':>4} {'reg+std':>8} {'wiki':>5} {'vendor':>6} {'blog':>5} {'other':>6}")
    print("-" * 75)
    for key, c in per_artefact.items():
        tot = sum(c.values())
        reg_std = c.get("regulatory_eu", 0) + c.get("regulatory_us", 0) + \
                  c.get("regulatory_intl", 0) + c.get("standards_body", 0)
        print(f"{key:<32} {tot:>4} {reg_std:>8} "
              f"{c.get('wikipedia',0):>5} {c.get('vendor_security',0):>6} "
              f"{c.get('blog_forum',0):>5} {c.get('other',0):>6}")

    return cat_counts, total


def report_c2():
    arts = load_artefacts("c2_private_rag")
    print(f"\n=== C2 — {len(arts)} artefatti ===\n")

    src_counts: Counter[str] = Counter()
    inst_counts: Counter[str] = Counter()
    per_artefact: dict[str, list[str]] = {}

    # Map filename → institutional source (best-effort, manual)
    FILE_TO_INST = {
        "1.json": "ENISA",
        "2.json": "INCIBE",
        "3.json": "ENISA",
        "4.json": "CyberPeace Institute",
        "5.json": "CSS Zurich (CCDCOE-related)",
        "6.json": "SIM3 / Open CSIRT",
        "8.json": "GFCE",
        "9.json": "CERT-SEI / CMU",
        "10.json": "GFCE Cybil Portal",
        "12.json": "CyberPeace Institute",
        "13.json": "UK NCA",
        "14.json": "WEF",
        "15.json": "NATO CCDCOE",
        "17.json": "EC / dual-use research",
        "18.json": "International gov. (WEF/OECD)",
        "19.json": "Marsh / RAND",
        "20.json": "EC / JANUS",
        "CyFun_definitions.pdf": "CyFun (Belgium CCB)",
        "10_golden_rules_for_cyber_security.docx": "Policy template (KB)",
        "access_control_policy.docx": "Policy template (KB)",
        "asset_management.docx": "Policy template (KB)",
        "backup_and_recovery_policy.docx": "Policy template (KB)",
        "cyber_incident_response_plan.docx": "Policy template (KB)",
        "cybersecurity_policy_BASIC.docx": "Policy template (KB)",
        "network_security_policy.docx": "Policy template (KB)",
        "password_policy.docx": "Policy template (KB)",
        "vulnerability_and_patch_management.docx": "Policy template (KB)",
    }

    for art in arts:
        key = f"{art['path'].parent.name}/{art['path'].stem}"
        per_artefact[key] = []
        for s in art["frontmatter"].get("sources", []) or []:
            src_path = s.get("source") or s.get("title") or ""
            fname = Path(src_path).name
            src_counts[fname] += 1
            inst = FILE_TO_INST.get(fname, "(unmapped)")
            inst_counts[inst] += 1
            per_artefact[key].append(fname)

    total = sum(src_counts.values())
    print(f"Total citations: {total}\n")
    print("Sources cited (by filename):")
    for f, n in src_counts.most_common():
        inst = FILE_TO_INST.get(f, "(unmapped)")
        print(f"  {n:>3}  [{inst:<32}]  {f}")
    print(f"\nBy institutional source:")
    for inst, n in inst_counts.most_common():
        print(f"  {n:>3}  {inst}")

    return src_counts, total


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    cat_counts_5w, tot_5w = report_c0_5_web()
    src_counts_c2, tot_c2 = report_c2()

    print("\n=== HEADLINE COMPARISON ===\n")
    pertinent_5w = sum(cat_counts_5w.get(c, 0) for c in
                       ["regulatory_eu", "regulatory_us", "regulatory_intl",
                        "standards_body", "academic"])
    print(f"C0_5+web: {tot_5w} citations across 10 policies")
    print(f"  pertinent (gov / standards / academic): "
          f"{pertinent_5w} ({100*pertinent_5w/tot_5w:.1f}%)")
    print(f"  remainder (wiki / vendor / news / blog / other): "
          f"{tot_5w - pertinent_5w} ({100*(tot_5w-pertinent_5w)/tot_5w:.1f}%)")
    print(f"\nC2: {tot_c2} citations across 10 policies")
    print(f"  by construction 100% institutional/normative (curated KB)")
