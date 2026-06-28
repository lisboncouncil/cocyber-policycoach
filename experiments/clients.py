#!/usr/bin/env python3
"""IWAPS 2026 — homogeneous clients for the four configurations under test.

Each function accepts a fully-rendered user prompt (the "policy task" with
organisational profile expanded) and returns a uniform dict:

    {
        "answer":   str,            # the generated policy text
        "sources":  list[dict],     # citation-like records, may be empty
        "metadata": {
            "config":          str,        # "C0" | "C0+web" | "C1" | "C2"
            "model":           str,
            "input_tokens":    int | None,
            "output_tokens":   int | None,
            "total_tokens":    int | None,
            "latency_s":       float,
            "tool_calls":      list[str],  # names of tools the model invoked
            "raw_provider_id": str | None, # provider-side id (run/response)
        }
    }

The four configurations are intentionally minimal — anything beyond the
declared difference (system prompt, RAG tool, web search) is held constant
to keep the comparison fair.
"""

from __future__ import annotations
import json
import os
import time
from pathlib import Path
from typing import Any

import requests
from openai import OpenAI

# ---------------------------------------------------------------------------
# Constants and clients
# ---------------------------------------------------------------------------

# Paths are resolved from the environment so no machine-specific paths are
# committed. SECRETS defaults to a local "secrets" dir next to this package.
SECRETS = Path(os.environ.get("POLICYCOACH_SECRETS", Path(__file__).resolve().parent / "secrets"))
EXP = Path(__file__).resolve().parent

# Prefer the standard env var; fall back to a key file under SECRETS.
OPENAI_KEY = os.environ.get("OPENAI_API_KEY") or (SECRETS / "openai_api_key").read_text().strip()
_openai = OpenAI(api_key=OPENAI_KEY)

# Loaded lazily for C1 (it depends on c1_setup.json existing).
_C1_META: dict | None = None
def _c1_meta() -> dict:
    global _C1_META
    if _C1_META is None:
        _C1_META = json.loads((EXP / "c1_setup.json").read_text())
    return _C1_META

C2_BASE_URL = "http://localhost:5050"
C2_COLLECTION = "cyfun_enriched"

GENERATION_MODEL = "gpt-4.1"           # used by C0, C0+web, and C1
GENERATION_MODEL_GPT5 = "gpt-5.5"      # used by C0_5+web (newest frontier model, GA 2026-04-23)
TEMPERATURE = 0.7                       # consumer-default-like


# ---------------------------------------------------------------------------
# C0 — ChatGPT-default benchmark (no tool, no system prompt)
# ---------------------------------------------------------------------------

def generate_c0(prompt: str) -> dict[str, Any]:
    t0 = time.perf_counter()
    resp = _openai.chat.completions.create(
        model=GENERATION_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=TEMPERATURE,
    )
    dt = time.perf_counter() - t0
    msg = resp.choices[0].message
    answer = msg.content or ""
    return {
        "answer": answer,
        "sources": [],
        "metadata": {
            "config": "C0",
            "model": resp.model,
            "input_tokens": resp.usage.prompt_tokens if resp.usage else None,
            "output_tokens": resp.usage.completion_tokens if resp.usage else None,
            "total_tokens": resp.usage.total_tokens if resp.usage else None,
            "latency_s": round(dt, 3),
            "tool_calls": [],
            "raw_provider_id": resp.id,
        },
    }


# ---------------------------------------------------------------------------
# C0+web — ChatGPT with web search (Responses API + web_search_preview)
# ---------------------------------------------------------------------------

def generate_c0_web(prompt: str) -> dict[str, Any]:
    t0 = time.perf_counter()
    resp = _openai.responses.create(
        model=GENERATION_MODEL,
        input=prompt,
        tools=[{"type": "web_search_preview"}],
        temperature=TEMPERATURE,
    )
    dt = time.perf_counter() - t0

    answer = ""
    sources: list[dict] = []
    tool_calls: list[str] = []
    for item in resp.output or []:
        item_type = getattr(item, "type", None)
        if item_type == "message":
            for block in getattr(item, "content", []) or []:
                if getattr(block, "type", None) == "output_text":
                    answer += getattr(block, "text", "") or ""
                    for ann in getattr(block, "annotations", []) or []:
                        if getattr(ann, "type", None) == "url_citation":
                            sources.append({
                                "type": "url_citation",
                                "url": getattr(ann, "url", None),
                                "title": getattr(ann, "title", None),
                                "start_index": getattr(ann, "start_index", None),
                                "end_index": getattr(ann, "end_index", None),
                            })
        elif item_type and item_type.endswith("_call"):
            tool_calls.append(item_type)

    usage = getattr(resp, "usage", None)
    return {
        "answer": answer,
        "sources": sources,
        "metadata": {
            "config": "C0+web",
            "model": getattr(resp, "model", GENERATION_MODEL),
            "input_tokens": getattr(usage, "input_tokens", None) if usage else None,
            "output_tokens": getattr(usage, "output_tokens", None) if usage else None,
            "total_tokens": getattr(usage, "total_tokens", None) if usage else None,
            "latency_s": round(dt, 3),
            "tool_calls": tool_calls,
            "raw_provider_id": resp.id,
        },
    }


# ---------------------------------------------------------------------------
# C0_5+web — Frontier+web benchmark on the newest available GPT (gpt-5.5)
# Same setup as C0+web but with the most recent OpenAI frontier model.
# Added late in the experiment to verify that the C2 advantage holds even
# against a model release one month before submission.
# ---------------------------------------------------------------------------

def generate_c0_5_web(prompt: str) -> dict[str, Any]:
    t0 = time.perf_counter()
    resp = _openai.responses.create(
        model=GENERATION_MODEL_GPT5,
        input=prompt,
        tools=[{"type": "web_search_preview"}],
    )
    dt = time.perf_counter() - t0

    answer = ""
    sources: list[dict] = []
    tool_calls: list[str] = []
    for item in resp.output or []:
        item_type = getattr(item, "type", None)
        if item_type == "message":
            for block in getattr(item, "content", []) or []:
                if getattr(block, "type", None) == "output_text":
                    answer += getattr(block, "text", "") or ""
                    for ann in getattr(block, "annotations", []) or []:
                        if getattr(ann, "type", None) == "url_citation":
                            sources.append({
                                "type": "url_citation",
                                "url": getattr(ann, "url", None),
                                "title": getattr(ann, "title", None),
                                "start_index": getattr(ann, "start_index", None),
                                "end_index": getattr(ann, "end_index", None),
                            })
        elif item_type and item_type.endswith("_call"):
            tool_calls.append(item_type)

    usage = getattr(resp, "usage", None)
    return {
        "answer": answer,
        "sources": sources,
        "metadata": {
            "config": "C0_5+web",
            "model": getattr(resp, "model", GENERATION_MODEL_GPT5),
            "input_tokens": getattr(usage, "input_tokens", None) if usage else None,
            "output_tokens": getattr(usage, "output_tokens", None) if usage else None,
            "total_tokens": getattr(usage, "total_tokens", None) if usage else None,
            "latency_s": round(dt, 3),
            "tool_calls": tool_calls,
            "raw_provider_id": resp.id,
        },
    }


# ---------------------------------------------------------------------------
# C1 — Cloud RAG, OpenAI Assistant + file_search on shared KB
# ---------------------------------------------------------------------------

def generate_c1(prompt: str) -> dict[str, Any]:
    meta = _c1_meta()
    t0 = time.perf_counter()
    thread = _openai.beta.threads.create()
    _openai.beta.threads.messages.create(
        thread_id=thread.id, role="user", content=prompt,
    )
    run = _openai.beta.threads.runs.create_and_poll(
        thread_id=thread.id, assistant_id=meta["assistant_id"],
    )
    dt = time.perf_counter() - t0

    answer = ""
    sources: list[dict] = []
    tool_calls: list[str] = []

    if run.status == "completed":
        msgs = _openai.beta.threads.messages.list(
            thread_id=thread.id, order="desc", limit=1,
        )
        if msgs.data and msgs.data[0].content:
            block = msgs.data[0].content[0]
            answer = block.text.value
            for a in (block.text.annotations or []):
                if getattr(a, "type", None) == "file_citation":
                    fc = a.file_citation
                    sources.append({
                        "type": "file_citation",
                        "file_id": getattr(fc, "file_id", None),
                        "text": getattr(a, "text", None),
                    })

        # Inspect run steps for invoked tools (e.g. file_search).
        steps = _openai.beta.threads.runs.steps.list(
            thread_id=thread.id, run_id=run.id,
        )
        for s in steps.data:
            details = getattr(s, "step_details", None)
            for tc in getattr(details, "tool_calls", []) or []:
                tool_calls.append(getattr(tc, "type", "unknown"))

    usage = run.usage
    return {
        "answer": answer,
        "sources": sources,
        "metadata": {
            "config": "C1",
            "model": run.model,
            "input_tokens": getattr(usage, "prompt_tokens", None) if usage else None,
            "output_tokens": getattr(usage, "completion_tokens", None) if usage else None,
            "total_tokens": getattr(usage, "total_tokens", None) if usage else None,
            "latency_s": round(dt, 3),
            "tool_calls": tool_calls,
            "raw_provider_id": run.id,
            "run_status": run.status,
            "thread_id": thread.id,
        },
    }


# ---------------------------------------------------------------------------
# C2 — Private RAG, PolicyCoach (Kimi K2.5 on Nebius EU) via REST
# ---------------------------------------------------------------------------

def _generate_c2_like(prompt: str, config_label: str, timeout_s: int = 600) -> dict[str, Any]:
    """Shared body for C2 and C2b — both call the PolicyCoach REST endpoint;
    they differ only in the chat model the server is currently configured with.
    The model is read from the /health response for traceability."""
    t0 = time.perf_counter()
    r = requests.post(
        f"{C2_BASE_URL}/conversation",
        json={"collectionName": C2_COLLECTION, "message": prompt},
        timeout=timeout_s,
    )
    dt = time.perf_counter() - t0
    r.raise_for_status()
    payload = r.json()

    sources: list[dict] = []
    for s in payload.get("sources", []) or []:
        sources.append({
            "type": "kb_source",
            "source": s.get("source"),
            "title": s.get("title"),
        })

    # Pull the actual model in use from /health to keep metadata honest
    actual_model = "(unknown)"
    try:
        h = requests.get(f"{C2_BASE_URL}/health", timeout=5).json()
        actual_model = h.get("chat_model", "(unknown)")
    except Exception:
        pass

    md = payload.get("metadata", {}) or {}
    return {
        "answer": payload.get("answer", "") or "",
        "sources": sources,
        "metadata": {
            "config": config_label,
            "model": actual_model,
            "input_tokens": md.get("input_tokens"),
            "output_tokens": md.get("output_tokens"),
            "total_tokens": md.get("total_api_tokens") or md.get("tokens_used"),
            "latency_s": round(dt, 3),
            "tool_calls": ["rag_retrieval"] if md.get("chunks_retrieved") else [],
            "raw_provider_id": payload.get("sessionId"),
            "chunks_retrieved": md.get("chunks_retrieved"),
            "server_version": payload.get("serverVersion"),
        },
    }


def generate_c2(prompt: str, timeout_s: int = 600) -> dict[str, Any]:
    return _generate_c2_like(prompt, config_label="C2", timeout_s=timeout_s)


def generate_c2b(prompt: str, timeout_s: int = 600) -> dict[str, Any]:
    """C2b — same architecture as C2 (private RAG, EU + DPA + curated KB +
    PolicyCoach system prompt) but with a different open-weight chat model
    (e.g. DeepSeek V4 Pro). The PolicyCoach server must be reconfigured with
    the desired CHAT_MODEL env var before invoking this client."""
    return _generate_c2_like(prompt, config_label="C2b", timeout_s=timeout_s)


# ---------------------------------------------------------------------------
# Dispatcher
# ---------------------------------------------------------------------------

CONFIG_FUNCTIONS = {
    "C0":       generate_c0,
    "C0+web":   generate_c0_web,
    "C0_5+web": generate_c0_5_web,
    "C1":       generate_c1,
    "C2":       generate_c2,
    "C2b":      generate_c2b,
}


def generate(config: str, prompt: str) -> dict[str, Any]:
    if config not in CONFIG_FUNCTIONS:
        raise ValueError(f"unknown config {config!r}; expected one of {list(CONFIG_FUNCTIONS)}")
    return CONFIG_FUNCTIONS[config](prompt)


# ---------------------------------------------------------------------------
# CLI smoke
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import sys
    cfg = sys.argv[1] if len(sys.argv) > 1 else "C0"
    msg = sys.argv[2] if len(sys.argv) > 2 else "What is the purpose of an Information Security Policy?"
    out = generate(cfg, msg)
    print(f"\n--- {cfg} ---")
    print(f"model: {out['metadata']['model']}")
    print(f"tokens: in={out['metadata']['input_tokens']} out={out['metadata']['output_tokens']}")
    print(f"latency: {out['metadata']['latency_s']}s")
    print(f"tool_calls: {out['metadata']['tool_calls']}")
    print(f"sources: {len(out['sources'])}")
    print(f"answer (first 400 chars):\n{out['answer'][:400]}")
