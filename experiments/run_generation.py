#!/usr/bin/env python3
"""IWAPS 2026 — orchestrator for the 32-run generation matrix.

For every (config × context × policy) triple it renders the canonical prompt
and dispatches to the corresponding client in clients.py. Outputs are saved
under outputs/<config_slug>/<context_id>/<policy_short>.md with YAML
frontmatter containing the metadata returned by the client.

Defaults: dry-run prints the matrix. Use --execute to actually call the
APIs. --only filters the matrix (e.g. --only C0,C1 or --only ctx-H).
"""

from __future__ import annotations
import argparse
import json
import sys
import time
from pathlib import Path
from typing import Iterable

import yaml

# Local imports (this file lives under experiments/).
sys.path.insert(0, str(Path(__file__).resolve().parent))
from clients import generate, CONFIG_FUNCTIONS  # type: ignore
sys.path.insert(0, str(Path(__file__).resolve().parent / "prompts"))
from context_renderer import render as render_context  # type: ignore


ROOT = Path(__file__).resolve().parent
CONTEXTS_DIR = ROOT / "contexts"
PROMPTS_DIR = ROOT / "prompts"
OUTPUTS_DIR = ROOT / "outputs"

CONFIG_SLUGS = {
    "C0":       "c0_chatgpt",
    "C0+web":   "c0_chatgpt_web",
    "C0_5+web": "c0_5_chatgpt_web",
    "C1":       "c1_openai_assistant",
    "C2":       "c2_private_rag",
    "C2b":      "c2b_private_rag_deepseek",
}

CONTEXT_FILES = {
    "ctx-H": CONTEXTS_DIR / "hospital.yaml",
    "ctx-M": CONTEXTS_DIR / "military.yaml",
}


def load_policy_tasks() -> tuple[str, list[dict]]:
    spec = yaml.safe_load((PROMPTS_DIR / "policy_tasks.yaml").read_text())
    return spec["template"], spec["policy_tasks"]


def render_prompt(template: str, policy_name: str, context_narrative: str) -> str:
    return template.format(
        policy_name=policy_name, context_narrative=context_narrative,
    )


def matrix(configs: list[str], contexts: list[str], tasks: list[dict]
           ) -> Iterable[tuple[str, str, dict]]:
    for cfg in configs:
        for ctx_id in contexts:
            for t in tasks:
                yield cfg, ctx_id, t


def save_artefact(out_dir: Path, policy_short: str, prompt: str,
                  result: dict, cfg: str, ctx_id: str, task: dict) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    md_path = out_dir / f"{policy_short}.md"
    md = result["answer"] or ""
    frontmatter = {
        "config": cfg,
        "context_id": ctx_id,
        "policy_id": task["id"],
        "policy_name": task["name"],
        "policy_short": task["short"],
        "metadata": result["metadata"],
        "sources_count": len(result["sources"]),
        "sources": result["sources"][:32],   # cap to keep frontmatter readable
        "prompt_chars": len(prompt),
        "answer_chars": len(md),
        "generated_at_unix": int(time.time()),
    }
    yaml_block = yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True)
    md_path.write_text(f"---\n{yaml_block}---\n\n{md}\n")
    return md_path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--execute", action="store_true",
                    help="Actually call APIs. Without this, runs in dry-run mode.")
    ap.add_argument("--only", default="",
                    help="Comma-separated filter on config|ctx|policy ids "
                         "(e.g. 'C1,ctx-H,P1'). Empty = all.")
    args = ap.parse_args()

    template, tasks = load_policy_tasks()

    configs = list(CONFIG_FUNCTIONS.keys())
    contexts = list(CONTEXT_FILES.keys())
    only = {x.strip() for x in args.only.split(",") if x.strip()}

    if only:
        configs = [c for c in configs if not (only & set(CONFIG_FUNCTIONS)) or c in only]
        contexts = [c for c in contexts if not (only & set(CONTEXT_FILES)) or c in only]
        tasks = [t for t in tasks if not (only & {t["id"] for t in tasks}) or t["id"] in only]

    pairs = list(matrix(configs, contexts, tasks))
    print(f"Matrix: {len(configs)} configs × {len(contexts)} contexts × {len(tasks)} policies "
          f"= {len(pairs)} runs ({'EXECUTE' if args.execute else 'dry-run'})")

    # Pre-render context narratives once
    narratives = {ctx_id: render_context(CONTEXT_FILES[ctx_id]) for ctx_id in contexts}

    if not args.execute:
        for cfg, ctx_id, t in pairs:
            print(f"  [DRY] {cfg:7} {ctx_id} {t['id']} {t['name']}")
        return 0

    log_path = OUTPUTS_DIR / "generation_log.jsonl"
    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
    log_fh = log_path.open("a")

    failures = []
    for i, (cfg, ctx_id, t) in enumerate(pairs, 1):
        prompt = render_prompt(template, t["name"], narratives[ctx_id])
        out_dir = OUTPUTS_DIR / CONFIG_SLUGS[cfg] / ctx_id
        print(f"\n[{i:>2}/{len(pairs)}] {cfg:7} {ctx_id} {t['id']} {t['name']} "
              f"...", end="", flush=True)
        t0 = time.perf_counter()
        try:
            result = generate(cfg, prompt)
            dt = time.perf_counter() - t0
            md_path = save_artefact(out_dir, t["short"], prompt, result, cfg, ctx_id, t)
            md = result["metadata"]
            print(f" OK ({dt:.1f}s, {md.get('input_tokens') or '?'} in / "
                  f"{md.get('output_tokens') or '?'} out, sources={len(result['sources'])})")
            log_fh.write(json.dumps({
                "i": i, "config": cfg, "context": ctx_id, "policy": t["id"],
                "ok": True, "dt": round(dt, 3),
                "in_tok": md.get("input_tokens"), "out_tok": md.get("output_tokens"),
                "tool_calls": md.get("tool_calls"),
                "sources_count": len(result["sources"]),
                "answer_chars": len(result["answer"]),
                "out_path": str(md_path),
            }) + "\n")
            log_fh.flush()
        except Exception as exc:
            dt = time.perf_counter() - t0
            print(f" FAIL ({dt:.1f}s): {exc}")
            failures.append((cfg, ctx_id, t["id"], str(exc)))
            log_fh.write(json.dumps({
                "i": i, "config": cfg, "context": ctx_id, "policy": t["id"],
                "ok": False, "dt": round(dt, 3), "error": str(exc),
            }) + "\n")
            log_fh.flush()

    log_fh.close()

    print(f"\n=== summary ===")
    print(f"OK:    {len(pairs) - len(failures)} / {len(pairs)}")
    print(f"FAIL:  {len(failures)}")
    for f in failures:
        print(f"  - {f[0]} {f[1]} {f[2]}: {f[3]}")
    print(f"log:   {log_path}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
