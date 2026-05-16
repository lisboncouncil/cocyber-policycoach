---
config: C2b
context_id: ctx-H
policy_id: P4
policy_name: Incident Response Policy
policy_short: ir
metadata:
  config: C2b
  model: deepseek-ai/DeepSeek-V3.2
  input_tokens: 25637
  output_tokens: 1951
  total_tokens: 27588
  latency_s: 41.209
  tool_calls:
  - rag_retrieval
  raw_provider_id: 667fd39e-a947-4908-948a-d507ce1fe7c5
  chunks_retrieved: 5
  server_version: 1.3.4
sources_count: 3
sources:
- type: kb_source
  source: ./datadir-plus-templates/cyber_incident_response_plan.docx
  title: ./datadir-plus-templates/cyber_incident_response_plan.docx
- type: kb_source
  source: ./datadir-plus-templates/1.json
  title: Best Practices for Cyber Crisis Management
- type: kb_source
  source: ./datadir-plus-templates/9.json
  title: 'The Sector CSIRT Framework: Developing Sector-Based Incident Response Capabilities'
prompt_chars: 4675
answer_chars: 8655
generated_at_unix: 1778503731
---

<policy title="Cyber Incident Response Policy">

| Field | Value |
|-------|-------|
| **Document ID** | POL-008 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Internal – Restricted |
| **Owner** | IT Manager / CISO (to be appointed) |
| **Approved by** | Director of the Hospital / Legal Representative |
| **Approval Date** | [DD/MM/YYYY] |
| **Next Review Date** | [DD/MM/YYYY] (One year from approval) |
| **Review Cycle** | Annual |

---

## 1. Purpose

This Cyber Incident Response Policy establishes the framework for the [Hospital Name] to effectively detect, respond to, and recover from cyber security incidents. The policy defines roles, responsibilities, and procedures to ensure a rapid, coordinated, and effective response to incidents that may compromise the confidentiality, integrity, or availability of the hospital's information systems and patient data. This policy supports compliance with GDPR (EU 2016/679), the Italian Privacy Code (D.Lgs. 196/2003 as amended), the NIS2 Directive (EU 2022/2555), and AGID guidelines for the Public Administration.

## 2. Scope

This policy applies to:
- All employees, contractors, and third-party personnel with access to [Hospital Name]'s information systems.
- All information assets, including but not limited to the Electronic Health Record (Fascicolo Sanitario Elettronico), PACS/RIS, LIS, ADT, and pharmacy management systems.
- All incidents affecting the confidentiality, integrity, or availability of hospital data and systems, including those involving patient data (special category data under GDPR).

## 3. Roles and Responsibilities

### 3.1 Incident Response Team (IRT)
The IRT is activated for all confirmed or suspected security incidents. For a small hospital, the core IRT consists of:
*   **IRT Lead (Incident Commander):** Appointed by hospital management. Has overall authority during an incident. (Initially, this may be the senior IT staff member or an appointed manager).
*   **IT/Security Lead:** The 1.5 FTE IT staff member or designated MSP representative. Responsible for technical containment, evidence collection, and system recovery.
*   **Data Protection Officer (DPO) / Privacy Officer:** Manages data breach notifications to the Garante per la protezione dei dati personali and data subjects as required by GDPR.
*   **Clinical Operations Lead:** A senior clinician or department head who can make critical decisions regarding clinical safety and patient care continuity.
*   **Legal/Compliance Officer (or external counsel):** Manages legal, regulatory, and contractual obligations, including notifications to the Garante and other authorities under NIS2 and GDPR.
*   **Communications Lead (if separate from IRT Lead):** Manages internal and external communications.

### 3.2. Managed Service Provider (MSP)
The contracted MSP is responsible for providing technical support and logs as defined in the service level agreement (SLA), including initial detection alerts, forensic data, and remediation support.

## 4. Incident Classification and Severity Levels

Incidents are classified based on their potential impact on patient safety, data protection, and operational continuity.

| Severity | Criteria | Example | Initial Response SLA |
| :--- | :--- | :--- | :--- |
| **SEV-1: Critical** | Widespread system outage, confirmed ransomware, major data breach, direct threat to patient safety. | Ransomware on EHR/PACS, large-scale data exfiltration. | **Immediate.** Activate IRT within 30 minutes. |
| **SEV-2: High** | Significant disruption to clinical or administrative services, potential data breach. | Phishing attack with multiple account compromises, DDoS affecting clinical systems. | **Within 1 hour.** |
| **SEV-3: Moderate** | Isolated system compromise, potential data exposure. | Malware on a single workstation, suspicious activity on a server. | **Within 4 hours.** |
| **SEV-4: Low/Info** | Minor policy violations, unsuccessful scans. | Failed login attempts, non-critical alerts. | **Within 24 hours.** |

## 5. Incident Response Process

The response follows the NIST Incident Handling Steps: Preparation, Detection & Analysis, Containment, Eradication & Recovery, and Post-Incident Activity.

### 5.1. Preparation
*   **Training:** All staff receive annual security awareness training, including incident reporting procedures.
*   **IR Plan Testing:** This plan will be tested via tabletop exercises at least annually.
*   **Contact Lists:** Updated contact lists for the IRT, MSP, Garante, and other authorities are maintained offline.
*   **Technical:** Backups are performed nightly to NAS and weekly off-site tapes. The 4-hour RTO for EHR and 1-hour RTO for ADT/PS are documented.

### 5.2. Detection & Reporting
*   **Sources:** Alerts from AV/EDR, MSP monitoring, user reports (staff are trained to report to [internal hotline/email]).
*   **Initial Analysis:** The IT Lead or MSP performs initial triage to confirm an incident and its severity.

### 5.3. Containment, Eradication & Recovery
*   **Containment:** Immediate actions to limit damage. For a ransomware attack, this may involve isolating infected network segments (e.g., the clinical VLAN) while keeping critical systems online for patient safety.
*   **Eradication:** Removal of malware, patching vulnerabilities, and changing compromised credentials.
*   **Recovery:** Restoring systems from clean backups after ensuring the threat is eradicated. Clinical systems are prioritized based on clinical safety.

### 5.4. Notification & Communication
*   **Internal:** The IRT Lead approves all internal communications. Staff are informed on a need-to-know basis.
*   **External (Regulatory):** The DPO/Legal Officer is responsible for notifying the Garante per la protezione dei dati personali within 72 hours of a confirmed personal data breach (GDPR Art. 33). Notifications to the Italian NIS2 Competent Authority (to be designated) will follow NIS2 requirements.
*   **External (Public/Media):** All external communications are managed by the designated Communications Lead or Hospital Director.

### 5.5. Post-Incident Activity
*   A post-incident review will be held within one week.
*   The IRT Lead will produce a report detailing the root cause, impact, actions taken, and lessons learned.
*   The report will recommend updates to this policy, security controls, and training.

## 6. Specific Procedures for Top Threats

*   **Ransomware on Clinical Systems:** The primary goal is to ensure patient safety. The IRT Lead, in consultation with the Clinical Lead, will decide if critical systems (e.g., life-supporting equipment) can be isolated while containing the threat. Recovery will prioritize systems based on clinical need.
*   **Data Breach (Patient Records):** Immediate activation of IRT. DPO leads assessment of breach scope. Legal/DPO determines notification requirements to Garante and affected individuals per GDPR.
*   **Phishing Attack:** Immediate password resets for affected accounts, user re-education, and analysis of email gateway logs.

## 7. Compliance & Regulatory Reporting

*   **GDPR (Reg. EU 2016/679):** The DPO is responsible for assessing and, if required, notifying the Garante within 72 hours of a personal data breach.
*   **NIS2 Directive (Directive (EU) 2022/2555):** As an essential health service, the hospital must report significant incidents to the relevant Italian NIS2 Competent Authority.
*   **AGID Guidelines:** The response will adhere to the "Linee Guida per la Sicurezza ICT nelle Pubbliche Amministrazioni."

## 8. Training and Testing
*   All staff receive annual security awareness training, including incident reporting.
*   The IRT and key staff will participate in an annual tabletop exercise simulating a ransomware attack on the EHR system.

## 9. Policy Review
This policy will be reviewed annually by the IRT Lead and updated in response to regulatory changes, incident learnings, or significant infrastructure changes.

---
**Approvals**

| Role | Name (and Title) | Signature | Date |
| :--- | :--- | :--- | :--- |
| Policy Owner (CISO/IT Lead) | | | |
| Hospital Director / Legal Rep. | | | |
| Data Protection Officer | | | |

---
**Sources Consulted:**
*   *Relevant Document 1: Cyber Incident Response Plan Template* - Used for structure and core IR lifecycle.
*   *Relevant Document 2: Best Practices for Cyber Crisis Management* - Informs roles and communication plans.
*   *Relevant Document 3: Sector CSIRT Framework* - Informs roadmap and policy structure.
*   GDPR (EU 2016/679), NIS2 Directive (EU 2022/2555), Italian Privacy Code (D.Lgs. 196/2003 as amended).

</policy>
