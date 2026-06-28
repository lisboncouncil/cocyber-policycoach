#!/usr/bin/env python3
"""
IWAPS 2026 — setup C1 (Cloud RAG proprietary, OpenAI Assistant + file_search).

Creates:
- a vector store with the same KB as PolicyCoach (C2): 27 files from
  external-repos/cocyber3/datadir-plus-templates/
- an Assistant with the same system prompt used by C2
- runs a smoke test with the same query used for the C2 smoke test.

Persists metadata in c1_setup.json and smoke result in c1_smoke.json.
"""

from __future__ import annotations
import json
import os
import sys
import time
from pathlib import Path

from openai import OpenAI

# Paths resolved from the environment; no machine-specific paths committed.
EXP = Path(__file__).resolve().parent
SECRETS = Path(os.environ.get("POLICYCOACH_SECRETS", EXP / "secrets"))
# External KB repo lives outside this repository; point COCYBER3_DIR at it.
COCYBER3 = Path(os.environ.get("COCYBER3_DIR", EXP / "external-repos" / "cocyber3"))

MODEL = "gpt-4.1"
ASSISTANT_NAME = "policycoach-iwaps-c1"
VS_NAME = "policycoach-iwaps-kb"
SMOKE_QUERY = "What is the purpose of an Information Security Policy and what are its mandatory components?"


def main() -> int:
    api_key = os.environ.get("OPENAI_API_KEY") or (SECRETS / "openai_api_key").read_text().strip()
    client = OpenAI(api_key=api_key)

    sp = (COCYBER3 / "system-prompt").read_text()
    print(f"[1/6] system prompt: {len(sp)} chars")

    kb_dir = COCYBER3 / "datadir-plus-templates"
    kb_files = sorted(p for p in kb_dir.iterdir() if p.is_file() and not p.name.startswith("."))
    print(f"[2/6] KB files: {len(kb_files)} totalling "
          f"{sum(p.stat().st_size for p in kb_files)/1024:.0f} KB")

    print("[3/6] creating vector store...")
    vs = client.vector_stores.create(name=VS_NAME)
    print(f"      vector_store_id={vs.id}")

    print(f"[4/6] uploading {len(kb_files)} files & polling batch...")
    file_ids: list[str] = []
    for p in kb_files:
        with open(p, "rb") as fh:
            up = client.files.create(file=fh, purpose="assistants")
        file_ids.append(up.id)
    batch = client.vector_stores.file_batches.create_and_poll(
        vector_store_id=vs.id,
        file_ids=file_ids,
    )
    print(f"      batch.status={batch.status} "
          f"completed={batch.file_counts.completed}/{batch.file_counts.total} "
          f"failed={batch.file_counts.failed}")
    if batch.status != "completed" or batch.file_counts.failed:
        print("      WARNING: some files failed to ingest")

    print("[5/6] creating Assistant...")
    assistant = client.beta.assistants.create(
        name=ASSISTANT_NAME,
        instructions=sp,
        model=MODEL,
        tools=[{"type": "file_search"}],
        tool_resources={"file_search": {"vector_store_ids": [vs.id]}},
    )
    print(f"      assistant_id={assistant.id}  model={assistant.model}")

    setup_meta = {
        "assistant_id": assistant.id,
        "vector_store_id": vs.id,
        "model": assistant.model,
        "name": ASSISTANT_NAME,
        "file_ids": file_ids,
        "files_count": len(file_ids),
        "instructions_chars": len(sp),
        "kb_dir": str(kb_dir),
        "created_at_unix": int(time.time()),
    }
    (EXP / "c1_setup.json").write_text(json.dumps(setup_meta, indent=2))
    print(f"      setup metadata -> {EXP / 'c1_setup.json'}")

    print("[6/6] smoke test...")
    thread = client.beta.threads.create()
    client.beta.threads.messages.create(
        thread_id=thread.id, role="user", content=SMOKE_QUERY,
    )
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id, assistant_id=assistant.id,
    )
    print(f"      run.status={run.status}")

    answer = ""
    annotations: list = []
    if run.status == "completed":
        msgs = client.beta.threads.messages.list(thread_id=thread.id, order="desc", limit=1)
        m = msgs.data[0]
        if m.content:
            block = m.content[0]
            answer = block.text.value
            annotations = list(block.text.annotations or [])
        print(f"      answer.len={len(answer)}  annotations={len(annotations)}")

    smoke = {
        "query": SMOKE_QUERY,
        "thread_id": thread.id,
        "run_id": run.id,
        "status": run.status,
        "model": run.model,
        "answer_len_chars": len(answer),
        "annotations_count": len(annotations),
        "usage": run.usage.model_dump() if run.usage else None,
        "answer": answer,
        "annotations": [
            {
                "type": a.type,
                "text": getattr(a, "text", None),
                "file_citation": getattr(a, "file_citation", None) and a.file_citation.model_dump(),
            }
            for a in annotations
        ],
        "created_at_unix": int(time.time()),
    }
    (EXP / "c1_smoke.json").write_text(json.dumps(smoke, indent=2, default=str))
    print(f"      smoke result -> {EXP / 'c1_smoke.json'}")

    print("\n=== ANSWER (first 1200 chars) ===")
    print(answer[:1200])
    print("\n=== ANNOTATIONS ===")
    for a in annotations[:6]:
        fc = getattr(a, "file_citation", None)
        print(f"  - type={a.type}  file_id={getattr(fc,'file_id',None)}  text={getattr(a,'text','')[:60]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
