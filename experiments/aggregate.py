#!/usr/bin/env python3
"""IWAPS 2026 — aggregate per-artefact scores into the result tables for §5.

Reads scores/<config>/<context>/<policy>.aggregate.json (produced by
run_grader.py) and emits:

  - results/table1_quality_by_config.md      mean ± std per criterion × config
                                              (collapsed across contexts and
                                              policies). The headline table.
  - results/table2_quality_by_config_ctx.md  per criterion × config × context
                                              (separates ctx-H from ctx-M).
  - results/table3_code_based_by_config.md   code-grader: pass-rate by config.
  - results/table4_compliance_posture.md     non-quality posture: tokens leaving
                                              the perimeter, sources used,
                                              tool calls — derived from
                                              outputs/*/generation_log.jsonl.
  - results/all_scores.tsv                   long-format dump of every score
                                              (one row per artefact × criterion).

These are the artefacts that go straight into §5 of the paper after a final
review pass.
"""

from __future__ import annotations
import json
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCORES_DIR = ROOT / "scores"
OUTPUTS_DIR = ROOT / "outputs"
RESULTS_DIR = ROOT / "results"
GRADER_DIR = ROOT / "grader"

CONFIGS = ["C0", "C0+web", "C0_5+web", "C1", "C2", "C2b"]
CONFIG_SLUGS = {
    "C0":       "c0_chatgpt",
    "C0+web":   "c0_chatgpt_web",
    "C0_5+web": "c0_5_chatgpt_web",
    "C1":       "c1_openai_assistant",
    "C2":       "c2_private_rag",
    "C2b":      "c2b_private_rag_deepseek",
}
SLUG_TO_CONFIG = {v: k for k, v in CONFIG_SLUGS.items()}


def _mean_std(xs: list[float]) -> tuple[float | None, float | None]:
    if not xs:
        return None, None
    m = round(statistics.mean(xs), 2)
    s = round(statistics.pstdev(xs), 2) if len(xs) > 1 else 0.0
    return m, s


def _fmt(m: float | None, s: float | None) -> str:
    if m is None:
        return "—"
    if s is None:
        return f"{m:.2f}"
    return f"{m:.2f} ± {s:.2f}"


def load_aggregates() -> list[dict]:
    out = []
    for path in SCORES_DIR.glob("*/ctx-*/*.aggregate.json"):
        out.append(json.loads(path.read_text()))
    return out


def load_generation_log() -> list[dict]:
    log_path = OUTPUTS_DIR / "generation_log.jsonl"
    if not log_path.exists():
        return []
    out = []
    for line in log_path.read_text().splitlines():
        if line.strip():
            out.append(json.loads(line))
    return out


def table1_quality_by_config(aggregates: list[dict], criteria_order: list[str]) -> str:
    by_cfg_crit: dict[tuple[str, str], list[int]] = {}
    for a in aggregates:
        cfg = a["config"]
        for cid, sc in a.get("model_based", {}).items():
            score = sc.get("parsed", {}).get("score") if "parsed" in sc else None
            if isinstance(score, int):
                by_cfg_crit.setdefault((cfg, cid), []).append(score)
    rows = ["| Criterion | " + " | ".join(CONFIGS) + " |",
            "|---|" + "|".join("---" for _ in CONFIGS) + "|"]
    for cid in criteria_order:
        cells = [cid]
        for cfg in CONFIGS:
            m, s = _mean_std(by_cfg_crit.get((cfg, cid), []))
            cells.append(_fmt(m, s))
        rows.append("| " + " | ".join(cells) + " |")
    # Final row: average across criteria per config
    avg_cells = ["**average**"]
    for cfg in CONFIGS:
        all_scores = [v for (c, _), vs in by_cfg_crit.items() if c == cfg for v in vs]
        m, s = _mean_std(all_scores)
        avg_cells.append(_fmt(m, s))
    rows.append("| " + " | ".join(avg_cells) + " |")
    return "## Table 1 — quality by config (mean ± std, all 7 criteria)\n\n" + "\n".join(rows) + "\n"


def table2_quality_by_config_ctx(aggregates: list[dict], criteria_order: list[str]) -> str:
    out_lines = ["## Table 2 — quality by config × context"]
    for ctx in ["ctx-H", "ctx-M"]:
        sub = [a for a in aggregates if a["context_id"] == ctx]
        if not sub:
            continue
        by_cfg_crit: dict[tuple[str, str], list[int]] = {}
        for a in sub:
            cfg = a["config"]
            for cid, sc in a.get("model_based", {}).items():
                score = sc.get("parsed", {}).get("score") if "parsed" in sc else None
                if isinstance(score, int):
                    by_cfg_crit.setdefault((cfg, cid), []).append(score)
        out_lines.append(f"\n### {ctx}\n")
        out_lines.append("| Criterion | " + " | ".join(CONFIGS) + " |")
        out_lines.append("|---|" + "|".join("---" for _ in CONFIGS) + "|")
        for cid in criteria_order:
            cells = [cid]
            for cfg in CONFIGS:
                m, s = _mean_std(by_cfg_crit.get((cfg, cid), []))
                cells.append(_fmt(m, s))
            out_lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(out_lines) + "\n"


def table3_code_based_by_config(aggregates: list[dict]) -> str:
    by_cfg: dict[str, list[float]] = {}
    by_cfg_partial: dict[str, dict[str, list[float]]] = {}
    for a in aggregates:
        cb = a["code_based"]
        cfg = a["config"]
        ratio = cb["checks_passed"] / cb["checks_total"] if cb["checks_total"] else 0
        by_cfg.setdefault(cfg, []).append(ratio)
        for k, v in cb.get("partial_scores", {}).items():
            by_cfg_partial.setdefault(cfg, {}).setdefault(k, []).append(v)

    lines = ["## Table 3 — code-based grader (pass rate, partial scores)\n"]
    lines.append("| | " + " | ".join(CONFIGS) + " |")
    lines.append("|---|" + "|".join("---" for _ in CONFIGS) + "|")
    cells = ["pass_rate (mean)"]
    for cfg in CONFIGS:
        vals = by_cfg.get(cfg, [])
        m, s = _mean_std([v * 12 for v in vals])  # scale back to absolute
        cells.append(_fmt(m, s))
    lines.append("| " + " | ".join(cells) + " |")

    # All partial scores (consistent set across configs)
    all_partials = sorted({k for d in by_cfg_partial.values() for k in d.keys()})
    for partial in all_partials:
        cells = [partial]
        for cfg in CONFIGS:
            vals = by_cfg_partial.get(cfg, {}).get(partial, [])
            m, s = _mean_std(vals)
            cells.append(_fmt(m, s))
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines) + "\n"


def table4_compliance_posture(gen_log: list[dict]) -> str:
    by_cfg: dict[str, list[dict]] = {}
    for r in gen_log:
        if r.get("ok"):
            by_cfg.setdefault(r["config"], []).append(r)

    lines = ["## Table 4 — compliance posture and runtime stats\n"]
    lines.append("| Metric | " + " | ".join(CONFIGS) + " |")
    lines.append("|---|" + "|".join("---" for _ in CONFIGS) + "|")

    metrics = [
        ("avg input tokens / gen",  lambda rs: [r["in_tok"] for r in rs if r.get("in_tok")]),
        ("avg output tokens / gen", lambda rs: [r["out_tok"] for r in rs if r.get("out_tok")]),
        ("avg sources / gen",       lambda rs: [r.get("sources_count", 0) for r in rs]),
        ("avg latency (s)",         lambda rs: [r["dt"] for r in rs if r.get("dt")]),
        ("avg answer chars",        lambda rs: [r.get("answer_chars", 0) for r in rs]),
    ]
    for name, fn in metrics:
        cells = [name]
        for cfg in CONFIGS:
            xs = fn(by_cfg.get(cfg, []))
            m, s = _mean_std(xs)
            cells.append(_fmt(m, s))
        lines.append("| " + " | ".join(cells) + " |")

    # tool_calls breakdown — count per-config the most common tool calls
    cells = ["tool calls observed"]
    for cfg in CONFIGS:
        tool_counts: dict[str, int] = {}
        for r in by_cfg.get(cfg, []):
            for t in r.get("tool_calls") or []:
                tool_counts[t] = tool_counts.get(t, 0) + 1
        if tool_counts:
            cells.append(", ".join(f"{k}×{v}" for k, v in sorted(tool_counts.items())))
        else:
            cells.append("none")
    lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines) + "\n"


def long_table(aggregates: list[dict]) -> str:
    rows = ["config\tcontext\tpolicy\tcriterion\tscore\tcode_pass\tcode_total"]
    for a in aggregates:
        cb = a["code_based"]
        for cid, sc in a.get("model_based", {}).items():
            score = sc.get("parsed", {}).get("score") if "parsed" in sc else None
            rows.append(
                f"{a['config']}\t{a['context_id']}\t{a['policy_id']}\t"
                f"{cid}\t{'' if score is None else score}\t"
                f"{cb['checks_passed']}\t{cb['checks_total']}"
            )
    return "\n".join(rows) + "\n"


def main() -> int:
    rubric = json.loads((GRADER_DIR / "rubric.json").read_text())
    criteria_order = [c["id"] for c in rubric["criteria"]]
    aggregates = load_aggregates()
    gen_log = load_generation_log()

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Aggregates loaded:  {len(aggregates)}")
    print(f"Generation log rows: {len(gen_log)}")

    if aggregates:
        (RESULTS_DIR / "table1_quality_by_config.md").write_text(
            table1_quality_by_config(aggregates, criteria_order))
        (RESULTS_DIR / "table2_quality_by_config_ctx.md").write_text(
            table2_quality_by_config_ctx(aggregates, criteria_order))
        (RESULTS_DIR / "table3_code_based_by_config.md").write_text(
            table3_code_based_by_config(aggregates))
        (RESULTS_DIR / "all_scores.tsv").write_text(long_table(aggregates))

    if gen_log:
        (RESULTS_DIR / "table4_compliance_posture.md").write_text(
            table4_compliance_posture(gen_log))

    print(f"Results written to: {RESULTS_DIR}")
    for p in sorted(RESULTS_DIR.glob("*.md")) + sorted(RESULTS_DIR.glob("*.tsv")):
        print(f"  - {p.name}")
    return 0


if __name__ == "__main__":
    main()
