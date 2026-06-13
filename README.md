# cocyber-policycoach

Research sandbox and materials for **PolicyCoach** — an AI/RAG system for cybersecurity policy generation, developed in the context of the [COcyber project](https://www.cocyber.eu) (Grant Agreement No. 101158606, Digital Europe DIGITAL-ECCC-2023-DEPLOY-CYBER-04).

---

## Repository contents

### `paper/`

IWAPS 2026 camera-ready paper (Springer LNCS format).

**Title**: *Privacy by Design in AI-Assisted Cybersecurity Policy Generation: Benchmarking Private RAG Against Frontier AI Models*  
**Authors**: Davide Carboni, Marcello Verona — The Lisbon Council  
**Target venue**: IWAPS 2026 @ ARES 2026, Linköping, Sweden, 24–27 August 2026  
**Submission deadline**: 18 May 2026

| File | Description |
|---|---|
| `paper.tex` | LaTeX source (main document) |
| `references.bib` | BibTeX bibliography |
| `paper.pdf` | Compiled PDF (current draft, 8 pages) |
| `llncs.cls` | Springer LNCS document class |
| `splncs04.bst` | LNCS bibliography style |

**Abstract (placeholder — to be written last)**: The paper benchmarks six AI configurations — from unaugmented frontier AI models to a privacy-by-design private RAG on EU-resident open-weight models — on 60 cybersecurity policy generation tasks across two regulated organisational contexts (Italian public hospital, NATO detachment). A two-phase experimental design first selects the private RAG backbone via pairwise ablation (Kimi K2.5 over DeepSeek V3.2), then benchmarks the selected configuration against frontier systems. Evaluation uses a 7-criterion LLM-as-judge rubric derived from the Anthropic research agent grading framework and extended with cybersecurity compliance-specific dimensions. Key finding: private RAG (Kimi K2.5, Nebius EU + DPA) achieves 90% of the quality of the best frontier system (gpt-5.5 + web search) at one-tenth the cost, with full GDPR compliance and a deterministic audit trail.

---

### `experiments/`

Python scripts for the benchmark pipeline and validation tests.

#### Generation and grading

| Script | Description |
|---|---|
| `clients.py` | API clients for all configurations (gpt-4.1, gpt-5.5+web, OpenAI Assistants, Kimi K2.5 private RAG, DeepSeek V3.2 private RAG) |
| `setup_c1.py` | Setup script for OpenAI Assistants RAG (creates assistant + vector store, ingests KB) |
| `run_generation.py` | Generates policy artefacts for all configurations × contexts × policy types |
| `run_grader.py` | LLM-as-judge grader pipeline (Claude Opus 4.7, 7-criterion rubric) |
| `run_pairwise.py` | Pairwise backbone selection: Kimi K2.5 vs DeepSeek V3.2 |
| `aggregate.py` | Aggregates per-artefact scores into summary tables |
| `audit_citations.py` | Code-based check: counts regulatory citations (NIST, ISO 27001, GDPR, NIS2) per artefact |

#### Interview test (no-repeat directive validation)

| Script | Description |
|---|---|
| `run_interview_test.py` | Automated multi-session test against PolicyCoach server (localhost:5050). Simulates 20 organisational profiles across 6 policy types. Detects duplicate questions using interrogative-sentence extraction + SequenceMatcher similarity (threshold 0.75). Claude Haiku 4.5 generates contextual answers. |

#### `experiments/results/`

| File | Description |
|---|---|
| `all_scores.tsv` | Long-format dump of all LLM-judge scores (60 artefacts × 7 criteria) |
| `table1_quality_by_config.md` | Headline: mean scores by configuration |
| `table2_quality_by_config_ctx.md` | Scores split by context (ctx-H vs ctx-M) |
| `table3_code_based_by_config.md` | Code-based check results (citation counts) |
| `table4_compliance_posture.md` | Privacy posture: tokens leaving EU perimeter, latency, cost, sources |
| `pairwise_c2_vs_c2b.json` | Raw pairwise comparison results (Kimi K2.5 vs DeepSeek V3.2, 10/10 in favour of Kimi) |
| `interview_test_*.log` | Session logs for the no-repeat directive test (3 sessions, 20 scenarios each) |
| `interview_test_report.md` | Summary report of Session #3 (definitive): 20/20 policies generated, 0 duplicates |

---

### `archive/`

Historical materials from earlier PolicyCoach development phases.

---

## COcyber project

This work is carried out in the context of the **COcyber** project (*Coordination Between the Cybersecurity Civilian and Defence Spheres*), funded by the European Union under the Horizon Europe programme, Grant Agreement No. 101158606 (Call DIGITAL-ECCC-2023-DEPLOY-CYBER-04). Views and opinions expressed are those of the authors only and do not necessarily reflect those of the European Union or the European Cybersecurity Competence Centre (ECCC).
