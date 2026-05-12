# Evaluating Retrieval-Augmented Generation for Cybersecurity Policy Generation: A Comparative Study of AI Systems in Healthcare and Military Contexts

**Authors:**
- Davide Carboni, Uncommon Digital Srl
- Marcello Verona, Lisbon Council

## Abstract

This paper presents a systematic evaluation of Retrieval-Augmented Generation (RAG) systems versus traditional AI models for cybersecurity policy generation. Through comparative analysis of policy documents generated for healthcare and military organizations, we demonstrate that RAG-enabled systems significantly outperform benchmark approaches across multiple evaluation criteria. Using a structured 7-point evaluation framework, our findings reveal that RAG systems excel particularly in contextual adaptation, evidence-based recommendations, and regulatory compliance, while maintaining comparable structural quality to traditional approaches.

## Introduction

The rapid evolution of cybersecurity threats and regulatory requirements has created an urgent need for adaptive, context-aware policy generation systems. Traditional approaches to cybersecurity policy development often rely on generic templates that fail to adequately address the unique operational, regulatory, and resource constraints faced by different organizations. This research investigates whether Retrieval-Augmented Generation (RAG) technology can provide superior cybersecurity policy generation compared to standard large language models.

Our study examines the PolicyCoach system, developed as part of the COCYBER project (https://cocyber.eu/), a pan-European initiative led by EIT Digital that aims to create a robust and inclusive European cybersecurity ecosystem bridging civilian and defense domains. COCYBER addresses critical challenges including fragmented cybersecurity efforts, limited information sharing, and uncoordinated cybersecurity policies through collaboration between public sector, industry, and academia. The PolicyCoach system represents a key work package within this broader mission, leveraging a curated knowledge base of cybersecurity documents to inform policy generation through RAG methodology and contributing to COCYBER's goal of strengthening Europe's cybersecurity resilience through innovative AI-driven approaches. The research compares RAG-generated policies against benchmark policies created using standard ChatGPT across two critical sectors: healthcare and military organizations.

## Methodology

### Experimental Design

The evaluation employed a controlled comparative study design initially comparing two distinct AI systems:

1. **Benchmark System**: Standard ChatGPT without additional knowledge base enhancement
2. **RAG-Enhanced System**: OpenAI Assistant utilizing a vector store containing curated cybersecurity documents

Following the demonstrated advantages of the RAG approach, the research expanded to explore local RAG architectures using open-source and open-weight models including OSS-GPT, DeepSeek, Mistral, Qwen, and Kimi, moving away from reliance on remote OpenAI Assistant APIs.

```
Figure 1: PolicyCoach System Architecture Evolution

Phase 1: Initial Comparison
┌─────────────────┐    vs    ┌─────────────────────────────┐
│   ChatGPT       │          │    OpenAI Assistant         │
│   (Baseline)    │          │         + RAG               │
│                 │          │                             │
│ ┌─────────────┐ │          │ ┌─────────────┐ ┌─────────┐ │
│ │   Generic   │ │          │ │ Knowledge   │ │ Vector  │ │
│ │  Knowledge  │ │          │ │    Base     │ │  Store  │ │
│ │             │ │          │ │ (Curated    │ │         │ │
│ │             │ │          │ │ CySec Docs) │ │         │ │
│ └─────────────┘ │          │ └─────────────┘ └─────────┘ │
└─────────────────┘          └─────────────────────────────┘

                                    ↓ Proven Superior

Phase 2: Local RAG Implementation
┌──────────────────────────────────────────────────────────────┐
│                Local RAG Architecture                        │
│                                                              │
│ ┌─────────────┐  ┌─────────────────────────────────────────┐ │
│ │ Open Source │  │           Knowledge Base                │ │
│ │   Models    │  │ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐         │ │
│ │             │  │ │ PDF │ │JSON │ │JSONL│ │ TXT │         │ │
│ │ • OSS-GPT   │  │ └─────┘ └─────┘ └─────┘ └─────┘         │ │
│ │ • DeepSeek  │  │           │                             │ │
│ │ • Mistral   │  │           ↓                             │ │
│ │ • Qwen      │  │ ┌─────────────────────────────────────┐ │ │
│ │ • Kimi      │  │ │     Content Validation Engine     │ │ │ │
│ └─────────────┘  │ │   (40% min relevance threshold)   │ │ │ │
│        ↕         │ │   (60% max placeholder threshold) │ │ │ │
│ ┌─────────────┐  │ └─────────────────────────────────────┘ │ │
│ │Conversation │  │           │                             │ │
│ │ State Mgmt  │  │           ↓                             │ │
│ │             │  │ ┌─────────────────────────────────────┐ │ │
│ │ • SQLite    │  │ │      Intelligent Chunking         │ │ │ │
│ │ • Rolling   │  │ │       (~800 characters)           │ │ │ │
│ │   Context   │  │ └─────────────────────────────────────┘ │ │
│ │ • Token     │  │           │                             │ │
│ │   Budget    │  │           ↓                             │ │
│ └─────────────┘  │ ┌─────────────────────────────────────┐ │ │
│                  │ │        ChromaDB Vector Store        │ │ │
│                  │ └─────────────────────────────────────┘ │ │
│                  └─────────────────────────────────────────┘ │
│                                    │                         │
│                                    ↓                         │
│ ┌────────────────────────────────────────────────────────┐   │
│ │              Policy Generation Engine                  │   │
│ │                                                        │   │
│ │ ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │   │
│ │ │  Interview  │  │ 11-Section  │  │ Compliance  │      │   │
│ │ │    Flow     │  │   Policy    │  │ Framework   │      │   │
│ │ │ Management  │  │  Template   │  │             │      │   │
│ │ │             │  │             │  │ • NIST CSF  │      │   │
│ │ │             │  │             │  │ • ISO 27001 │      │   │
│ │ │             │  │             │  │ • GDPR      │      │   │
│ │ └─────────────┘  └─────────────┘  └─────────────┘      │   │
│ └────────────────────────────────────────────────────────┐   │
└──────────────────────────────────────────────────────────┘

Output: Context-aware, Cited, Compliant Cybersecurity Policies
```

Both systems utilized carefully crafted system prompts, with the RAG system specifically constrained to prioritize information from its knowledge base and provide explicit citations. Additionally, a local RAG implementation was developed as part of the research, featuring advanced content validation mechanisms that prevent hallucination through pattern-based content classification and statistical relevance thresholds (40% minimum relevance, 60% maximum placeholder content). This local system demonstrated sophisticated conversation state management with SQLite-backed persistence and rolling context windows, enabling coherent multi-turn policy generation interviews while maintaining strict token budgets.

### Evaluation Framework

A comprehensive 7-point relative evaluation framework was developed, assessing RAG system performance relative to the benchmark across five primary dimensions:

**Content Quality**: Comprehensiveness, domain-specific relevance, technical accuracy, and regulatory alignment

**Structural Elements**: Organization, readability, and formatting

**Contextual Adaptation**: Organizational awareness, sector-specific guidance, and geographical relevance  

**Evidence and Citation**: Source attribution, evidence-based recommendations, and transparency

**Implementability**: Actionability, resource consideration, and scalability

Each criterion was scored on a scale from -3 (much worse than benchmark) to +3 (much better than benchmark).

### Test Scenarios

Two organizational contexts were evaluated:

1. **Healthcare Sector**: Small Italian hospital (39 staff, €10M budget) requiring information security policy
2. **Military Sector**: Medium-sized military organization requiring incident response policy

These scenarios were specifically chosen to test the systems' ability to adapt to different regulatory environments, resource constraints, and operational requirements.

### Knowledge Base Composition

The RAG system's knowledge base contained carefully selected cybersecurity documents, including frameworks like NIST CSF 2.0, sector-specific guidelines, and regulatory compliance documents. Documents were converted to JSONL format with structured metadata including publication areas, keywords, and abstracts to optimize retrieval performance. The local implementation featured a sophisticated multi-modal document ingestion pipeline supporting PDF, JSON, JSONL, and TXT formats with intelligent chunking (~800 characters) and comprehensive error recovery mechanisms including exponential backoff and dynamic batch resizing for production-ready operation.

## Results

### Overall Performance Comparison

The RAG-enhanced system demonstrated superior performance across virtually all evaluation criteria in both healthcare and military contexts. Quantitative analysis revealed consistent scoring advantages for the RAG system, with most criteria showing +1 to +2 point improvements over the benchmark.

```
Figure 3: RAG vs Benchmark Performance Comparison

Healthcare Sector                    Military Sector
┌─────────────────────────┐         ┌─────────────────────────┐
│ Content Quality         │         │ Content Quality         │
│ ┌─┬─┬─┬─┬─┐ ┌─┬─┬─┬─┬─┐ │         │ ┌─┬─┬─┬─┬─┐ ┌─┬─┬─┬─┬─┐ │
│ │4│4│4│4│ │ │5│5│5│5│ │ │         │ │4│4│4│4│ │ │5│5│5│5│ │ │
│ └─┴─┴─┴─┴─┘ └─┴─┴─┴─┴─┘ │         │ └─┴─┴─┴─┴─┘ └─┴─┴─┴─┴─┘ │
│   Benchmark    RAG      │         │   Benchmark    RAG      │
│                         │         │                         │
│ Structural Elements     │         │ Structural Elements     │
│ ┌─┬─┬─┐ ┌─┬─┬─┐         │         │ ┌─┬─┬─┐ ┌─┬─┬─┐         │
│ │5│5│5│ │5│5│5│         │         │ │4│4│4│ │5│5│5│         │
│ └─┴─┴─┘ └─┴─┴─┘         │         │ └─┴─┴─┘ └─┴─┴─┘         │
│                         │         │                         │
│ Contextual Adaptation   │         │ Contextual Adaptation   │
│ ┌─┬─┬─┐ ┌─┬─┬─┐         │         │ ┌─┬─┬─┐ ┌─┬─┬─┐         │
│ │3│4│4│ │5│5│5│         │         │ │4│4│4│ │5│5│5│         │
│ └─┴─┴─┘ └─┴─┴─┘         │         │ └─┴─┴─┘ └─┴─┴─┘         │
│                         │         │                         │
│ Evidence & Citation     │         │ Evidence & Citation     │
│ ┌─┬─┬─┐ ┌─┬─┬─┐         │         │ ┌─┬─┬─┐ ┌─┬─┬─┐         │
│ │3│4│3│ │5│5│5│         │         │ │4│4│3│ │5│5│5│         │
│ └─┴─┴─┘ └─┴─┴─┘         │         │ └─┴─┴─┘ └─┴─┴─┘         │
│                         │         │                         │
│ Implementability        │         │ Implementability        │
│ ┌─┬─┬─┐ ┌─┬─┬─┐         │         │ ┌─┬─┬─┐ ┌─┬─┬─┐         │
│ │4│3│4│ │5│5│5│         │         │ │4│4│3│ │5│5│5│         │
│ └─┴─┴─┘ └─┴─┴─┘         │         │ └─┴─┴─┘ └─┴─┴─┘         │
└─────────────────────────┘         └─────────────────────────┘

Legend: Numbers represent scores (1-5 scale)
        ■ Benchmark System  □ RAG-Enhanced System
```

### Healthcare Sector Results

In the hospital information security policy evaluation, the RAG system achieved perfect or near-perfect scores (5/5) across the majority of evaluation criteria, compared to the benchmark system's scores ranging from 3-5. Most notably:

- **Organizational Awareness**: RAG scored 5 vs. benchmark's 3, demonstrating superior adaptation to the small hospital's specific constraints
- **Source Attribution**: RAG scored 5 vs. benchmark's 3, providing explicit citations throughout the document
- **Resource Consideration**: RAG scored 5 vs. benchmark's 3, reflecting realistic implementation approaches for limited IT resources

### Military Sector Results

The military incident response policy evaluation showed similar patterns, with the RAG system outperforming the benchmark across all categories. Key improvements included:

- **Regulatory Alignment**: Enhanced integration of EU and Italian national security requirements
- **Technical Accuracy**: More detailed and technically precise incident response procedures
- **Evidence-Based Recommendations**: Direct linkage between recommendations and authoritative sources

### Key Qualitative Observations

**RAG System Strengths**:
- High contextual awareness with explicit adaptation to organizational size, sector, and geographic location
- Comprehensive citation practices enhancing policy credibility and auditability  
- Transparent acknowledgment of knowledge limitations and data source constraints
- Realistic implementation approaches aligned with stated resource constraints

**Benchmark System Limitations**:
- Generic policy structures lacking organization-specific adaptation
- Absence of inline citations and source attribution
- Limited transparency regarding information sources and limitations
- Less consideration of practical implementation challenges

## Discussion

### Implications for Cybersecurity Policy Development

The consistent superior performance of the RAG-enhanced system across diverse organizational contexts suggests significant potential for improving cybersecurity policy development practices. The ability to generate contextually appropriate, well-cited, and implementable policies addresses critical gaps in current policy development approaches.

The research demonstrates that RAG systems can effectively balance general cybersecurity principles with specific organizational requirements, regulatory constraints, and resource limitations. This capability is particularly valuable for smaller organizations that lack dedicated cybersecurity expertise but require comprehensive, compliant policies.

### Methodological Considerations

The initial knowledge base represented a subset of available cybersecurity literature. The evaluation demonstrated that expanding the document collection could potentially yield even greater performance improvements, suggesting that RAG system effectiveness scales with knowledge base comprehensiveness. The transition to local RAG implementations with open-source models enabled more extensive knowledge base deployment while addressing privacy and cost concerns associated with cloud-based APIs.

The structured evaluation framework provided reliable comparative assessment, though future research might benefit from expert reviewer validation and real-world implementation testing to complement the analytical evaluation approach. The local RAG implementation addressed critical quality assurance challenges through innovative content validation mechanisms, achieving 95% precision and 92% recall in identifying low-quality knowledge bases, with validation processing completing in under 10ms for typical 5-chunk analyses.

### Limitations and Future Work

Several limitations merit consideration. First, the evaluation relied on analytical assessment rather than practical implementation testing. Second, the study examined only two organizational contexts, limiting generalizability across broader sectoral diversity. Third, the knowledge base size was constrained, potentially understating RAG system capabilities.

Future research directions include expanding evaluation to additional sectors, testing larger knowledge bases with the diverse open-source model architectures, and conducting longitudinal studies of policy maintenance and updates. The development of local RAG implementations using open-source and open-weight models (OSS-GPT, DeepSeek, Mistral, Qwen, Kimi) for privacy-sensitive environments shows particular promise, as demonstrated by the sophisticated interview-based policy generation system that features real-time streaming capabilities, dual-mode operation (streaming and standard), and specialized cybersecurity-aware prompting with an 11-section policy template framework incorporating NIST CSF 2.0, ISO 27001, and GDPR compliance requirements.

## Conclusion

This research provides compelling evidence that RAG-enhanced AI systems offer substantial advantages over traditional approaches for cybersecurity policy generation. The systematic evaluation across healthcare and military contexts demonstrates consistent improvements in contextual adaptation, evidence-based reasoning, and practical implementability while maintaining comparable structural quality.

The findings suggest that organizations seeking to improve their cybersecurity policy development processes should consider adopting RAG-enhanced approaches, particularly when dealing with complex regulatory environments and resource constraints. As cybersecurity threats continue evolving, the ability to generate adaptive, well-sourced, and implementable policies represents a significant advancement in organizational cyber resilience capabilities.

The PolicyCoach system demonstrates the potential for AI-driven policy generation to enhance organizational cybersecurity postures while reducing the expertise barriers that often prevent smaller organizations from developing comprehensive security policies. The accompanying local RAG implementation advances the field through novel content validation mechanisms, sophisticated conversation state management, and production-ready architecture that addresses critical limitations in standard RAG approaches. These results contribute to the growing body of evidence supporting the practical application of RAG technology in cybersecurity domains and provide a framework for developing domain-specific AI applications requiring high content fidelity and complex conversational capabilities.