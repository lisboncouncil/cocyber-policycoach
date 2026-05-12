# Evaluating RAG for Cybersecurity Policy Generation: A Comparative Study

**Authors:**
- Davide Carboni, Uncommon Digital Srl
- Marcello Verona, Lisbon Council

## Abstract

This paper evaluates Retrieval-Augmented Generation (RAG) systems against traditional AI models for cybersecurity policy generation. Through comparative analysis of policies for healthcare and military organizations, RAG systems significantly outperform benchmarks across multiple evaluation criteria, excelling in contextual adaptation, evidence-based recommendations, and regulatory compliance.

## Introduction

**Summary**: Traditional cybersecurity policy development relies on generic templates that fail to address organizational specifics. This research investigates RAG technology's superiority over standard language models through a two-phase evolution from cloud-based to local implementations.

The PolicyCoach system, developed within the COCYBER project (https://cocyber.eu/), represents a pan-European initiative led by EIT Digital to create an inclusive European cybersecurity ecosystem. COCYBER addresses fragmented cybersecurity efforts through collaboration between public sector, industry, and academia. PolicyCoach leverages curated cybersecurity knowledge bases through RAG methodology, comparing against standard ChatGPT across healthcare and military sectors.

```
System Evolution: ChatGPT → OpenAI Assistant+RAG → Local RAG+Open Source Models
┌─────────────┐  Proven    ┌─────────────────┐  Privacy    ┌─────────────────┐
│   ChatGPT   │ Superior → │ OpenAI Assistant│  &Cost   →  │   Local RAG     │
│ (Baseline)  │            │     + RAG       │ Concerns    │ (OSS Models)    │
└─────────────┘            └─────────────────┘             └─────────────────┘
```

## Methodology

**Summary**: Controlled comparative study initially comparing ChatGPT (benchmark) vs. OpenAI Assistant + RAG, then expanding to local RAG with open-source models (OSS-GPT, DeepSeek, Mistral, Qwen, Kimi).

### Experimental Design

Two systems were compared: standard ChatGPT and RAG-enhanced OpenAI Assistant with cybersecurity document vector stores. Following RAG advantages, research expanded to local architectures using open-source models, moving from remote APIs.

The local implementation features advanced content validation (40% minimum relevance, 60% maximum placeholder content thresholds), SQLite-backed conversation persistence, and rolling context windows for multi-turn policy interviews.

### Evaluation Framework

A 7-point relative scoring system assessed RAG performance across five dimensions:
- **Content Quality**: Comprehensiveness, relevance, accuracy, regulatory alignment
- **Structural Elements**: Organization, readability, formatting
- **Contextual Adaptation**: Organizational awareness, sector guidance, geographical relevance
- **Evidence and Citation**: Source attribution, evidence-based recommendations, transparency
- **Implementability**: Actionability, resource consideration, scalability

### Test Scenarios

Two organizational contexts: small Italian hospital (39 staff, €10M budget) requiring information security policy, and medium military organization needing incident response policy. Scenarios tested adaptation to regulatory environments, resource constraints, and operational requirements.

## Results

**Summary**: RAG systems demonstrated superior performance across virtually all criteria, with +1 to +2 point improvements over benchmarks in both sectors.

```
Performance Comparison (Sample - Healthcare Sector):
┌─────────────────────────┐
│ Evaluation Criteria     │ Benchmark │ RAG │ Improvement │
│ Organizational Awareness│     3     │  5  │     +2      │
│ Source Attribution      │     3     │  5  │     +2      │
│ Resource Consideration  │     3     │  5  │     +2      │
│ Technical Accuracy      │     4     │  5  │     +1      │
│ Regulatory Alignment    │     4     │  5  │     +1      │
└─────────────────────────┘
```

### Key Findings

**Healthcare Sector**: RAG achieved perfect scores (5/5) across majority of criteria vs. benchmark scores (3-5), with notable improvements in organizational awareness, source attribution, and resource consideration.

**Military Sector**: RAG outperformed across all categories, showing enhanced EU/Italian regulatory integration, technical precision, and evidence-based recommendations.

**Qualitative Observations**: RAG systems showed high contextual awareness, comprehensive citations, transparent limitation acknowledgment, and realistic implementation approaches. Benchmark systems exhibited generic structures, absent citations, limited transparency, and insufficient implementation consideration.

## Discussion

**Summary**: RAG systems effectively balance general principles with specific organizational requirements, particularly valuable for smaller organizations lacking dedicated cybersecurity expertise. Local implementations address privacy and cost concerns while enabling advanced technical capabilities.

### Technical Innovation Highlights

The local RAG implementation demonstrates several breakthrough capabilities:

**Content Validation Engine**: Achieved 95% precision and 92% recall in quality validation, with <10ms processing for typical analyses through pattern-based content classification and statistical relevance thresholds.

**Multi-Modal Processing**: Sophisticated document ingestion pipeline supporting PDF, JSON, JSONL, and TXT formats with intelligent chunking (~800 characters) and comprehensive error recovery mechanisms.

**Advanced State Management**: SQLite-backed conversation persistence with rolling context windows enabling coherent multi-turn policy generation interviews while maintaining strict token budgets.

### Implications

The consistent RAG superiority across diverse contexts suggests significant potential for improving cybersecurity policy development. Local implementations with open-source models address privacy and cost concerns while enabling extensive knowledge base deployment.

### Limitations and Future Work

Study limitations include analytical rather than practical assessment, limited organizational contexts, and constrained knowledge base size. Future directions encompass sector expansion, larger knowledge bases with diverse open-source architectures, and longitudinal policy maintenance studies. 

The evolution from cloud-based to local RAG implementations using open-source models (OSS-GPT, DeepSeek, Mistral, Qwen, Kimi) shows particular promise for privacy-sensitive environments with real-time streaming capabilities and specialized cybersecurity-aware prompting frameworks incorporating NIST CSF 2.0, ISO 27001, and GDPR compliance requirements.

## Conclusion

**Summary**: RAG systems offer substantial advantages for cybersecurity policy generation through improved contextual adaptation, evidence-based reasoning, and practical implementability. The evolution to local implementations with open-source models addresses critical privacy and cost limitations while advancing technical capabilities.

This research provides compelling evidence for RAG superiority in cybersecurity policy generation across healthcare and military contexts. The two-phase evolution from cloud-based proof-of-concept to sophisticated local implementations demonstrates both the technology's maturity and its practical viability for organizations with varying privacy and resource constraints.

Organizations should consider RAG approaches for complex regulatory environments, particularly as the technology evolves toward local implementations that maintain performance while addressing data sovereignty concerns. The PolicyCoach system's evolution from OpenAI Assistant integration to local RAG with multiple open-source models provides a roadmap for organizations seeking to balance AI capabilities with privacy requirements.

The accompanying local RAG implementation advances the field through novel content validation mechanisms, sophisticated conversation state management, and production-ready architecture that addresses critical limitations in standard RAG approaches, contributing to practical RAG technology application in cybersecurity domains and providing a framework for developing domain-specific AI applications requiring high content fidelity and complex conversational capabilities.