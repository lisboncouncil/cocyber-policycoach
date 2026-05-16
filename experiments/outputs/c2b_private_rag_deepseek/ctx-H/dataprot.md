---
config: C2b
context_id: ctx-H
policy_id: P2
policy_name: Data Protection Policy
policy_short: dataprot
metadata:
  config: C2b
  model: deepseek-ai/DeepSeek-V3.2
  input_tokens: 25604
  output_tokens: 2233
  total_tokens: 27837
  latency_s: 44.304
  tool_calls:
  - rag_retrieval
  raw_provider_id: 898ac060-4747-493b-886a-1e78597c5441
  chunks_retrieved: 5
  server_version: 1.3.4
sources_count: 3
sources:
- type: kb_source
  source: ./datadir-plus-templates/cybersecurity_policy_BASIC.docx
  title: ./datadir-plus-templates/cybersecurity_policy_BASIC.docx
- type: kb_source
  source: ./datadir-plus-templates/asset_management.docx
  title: ./datadir-plus-templates/asset_management.docx
- type: kb_source
  source: ./datadir-plus-templates/1.json
  title: Best Practices for Cyber Crisis Management
prompt_chars: 4671
answer_chars: 9766
generated_at_unix: 1778503508
---

<policy title="Data Protection Policy">

# Data Protection Policy

| Field | Value |
|-------|-------|
| **Document ID** | POL-DP-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Internal – Confidential |
| **Owner** | Data Protection Officer (DPO) / IT Manager |
| **Approved by** | Hospital Director (Direttore Generale) |
| **Approval Date** | [Date of Approval] |
| **Next Review Date** | One year from approval |
| **Review Cycle** | Annual |

---

## 1. Purpose

This Data Protection Policy establishes the framework for the protection of personal and sensitive data, with a specific focus on health data, processed by [Hospital Name], a public hospital within the Italian National Health Service (Servizio Sanitario Nazionale). This policy ensures compliance with the EU General Data Protection Regulation (GDPR) 2016/679, the Italian Privacy Code (D.Lgs. 196/2003 as amended), and the specific regulations for the healthcare sector, including the National Guidelines for the Electronic Health Record (FSE). It aligns with the principles of ISO/IEC 27001:2022 and the NIST Cybersecurity Framework 2.0, tailored to the operational and resource constraints of a regional public hospital.

## 2. Scope

This policy applies to:
- All employees, contractors, consultants, and third parties processing personal data on behalf of the hospital.
- All personal data processed by the hospital, with particular emphasis on "special category data" (health data) as defined by GDPR Article 9.
- All information systems, both physical and digital, used to store, process, or transmit personal data, including:
    - Electronic Health Records (EHR) / Fascicolo Sanitario Elettronico (FSE)
    - Picture Archiving and Communication Systems (PACS/RIS)
    - Laboratory Information Systems (LIS)
    - Admission/Discharge/Transfer (ADT) systems
    - Pharmacy and prescription management systems
    - Administrative and HR systems
    - Email and communication systems

## 3. Roles and Responsibilities

### 3.1 Data Protection Officer (DPO)
- Acts as the primary point of contact for data protection matters.
- Monitors compliance with GDPR and national regulations.
- Serves as the primary contact for the Italian Data Protection Authority (Garante per la protezione dei dati personali).

### 3.2 Hospital Management (Direzione)
- Accountable for ensuring resources are allocated for data protection.
- Approves this policy and ensures its enforcement.

### 3.3 IT Department (and MSP)
- Implements and maintains technical and organizational security measures.
- Manages access controls, encryption, and logging.
- Reports data processing systems and security incidents to the DPO.

### 3.4 Department Heads (Clinical and Administrative)
- Ensure staff in their area comply with this policy.
- Report any suspected data breaches or policy violations.

### 3.4 All Staff (Clinical, Administrative, Technical)
- Complete mandatory data protection and security awareness training.
- Handle personal data only as required for their role and in accordance with this policy.
- Report any suspected data breaches or policy violations immediately.

## 4. Data Protection Principles

The hospital is committed to processing data in accordance with the following principles, as mandated by GDPR Article 5:
- **Lawfulness, Fairness, and Transparency:** Data is processed lawfully, fairly, and transparently.
- **Purpose Limitation:** Data is collected for specified, explicit, and legitimate purposes.
- **Data Minimization:** Only data that is adequate, relevant, and necessary is collected.
- **Accuracy:** Personal data is kept accurate and up-to-date.
- **Storage Limitation:** Data is kept in a form that permits identification for no longer than necessary.
- **Integrity and Confidentiality:** Data is processed securely against unauthorized or unlawful processing, loss, or damage.

## 5. Policy Requirements

### 5.1 Data Classification and Inventory
- An inventory of all systems processing personal data, especially health data, shall be maintained.
- Data shall be classified according to its sensitivity (e.g., public, internal, confidential, restricted/health data).
- A data classification policy shall define handling procedures for each classification level.

### 5.2 Lawful Basis for Processing
- For health data (special category data under GDPR Art. 9), processing is permitted under Article 9(2)(h) for the provision of healthcare.
- Explicit consent will be sought where required by law, but the primary legal basis for processing health data is the provision of preventive or occupational medicine, medical diagnosis, and the provision of health or social care.

### 5.3 Data Subject Rights
The hospital shall establish and document procedures to facilitate the rights of data subjects (patients, staff) as per GDPR Articles 12-23, including the right to access, rectification, erasure ("right to be forgotten"), and data portability. Procedures must not impede clinical workflow or patient safety.

### 5.4 Data Security and Technical Measures
Given the resource constraints (1.5 FTE IT staff, reliance on MSP), the following controls are prioritized:
- **Access Control (GDPR Art. 32, ISO 27001 A.9):** Role-based access control (RBAC) must be enforced for all clinical and administrative systems. The principle of least privilege shall be applied. Multi-factor authentication (MFA) shall be implemented for all remote and privileged access.
- **Encryption (GDPR Art. 32):** All sensitive data at rest (e.g., on servers, NAS, backups) and in transit (e.g., between hospital and MSP, or to regional FSE) must be encrypted using strong, modern algorithms (e.g., AES-256, TLS 1.2+).
- **Network Security:** The existing segmentation (clinical VLANs, admin VLANs, PACS network) shall be maintained and documented. The MSP must provide quarterly reports on network segmentation and firewall rule reviews.
- **Endpoint Protection:** Anti-virus/anti-malware must be installed and updated on all endpoints, including legacy Windows kiosks. A plan for the secure decommissioning or isolation of legacy systems (e.g., Windows 7 kiosks) must be developed within 6 months.
- **Backup and Disaster Recovery (GDPR Art. 32):** The current nightly backup to NAS and weekly off-site tape rotation must be maintained. A full disaster recovery test, including restoration of critical systems (EHR, ADT), must be conducted at least annually. The RTO/RPO for critical systems (EHR: RTO 4h, ADT: RTO 1h) must be validated.
- **Vulnerability Management (NIST CSF: Protect - PR.IP-12):** A process for receiving, monitoring, and addressing vulnerability reports (e.g., from the MSP) must be established. Critical and High severity patches for internet-facing and clinical systems must be applied within SLAs defined in the Vulnerability Management Policy.

### 5.5 Third-Party Risk Management (GDPR Art. 28)
- All third-party processors (MSP, cloud service providers) must be under a Data Processing Agreement (DPA) compliant with GDPR Article 28.
- The MSP contract must be reviewed to ensure it mandates compliance with this policy and includes clear SLAs for incident response and breach notification.

### 5.6 Incident Response and Breach Notification
- A formal incident response plan, aligned with the NIST CSF "Respond" and "Recover" functions, must be documented.
- In the event of a personal data breach, the DPO must be notified immediately. The DPO will assess the risk and, if required, notify the Garante and affected individuals within 72 hours of becoming aware, as per GDPR Art. 33.

### 5.7 Training and Awareness (GDPR Art. 39)
- All staff must complete mandatory data protection and security awareness training annually.
- Clinical staff with high turnover will receive role-specific training on secure handling of patient data during onboarding.

## 6. Exceptions
Any exception to this policy requires documented approval from the DPO and the Hospital Director. Exceptions must be justified by a documented risk assessment and will be reviewed annually.

## 7. Monitoring and Review
- The DPO, in conjunction with the IT department/MSP, will produce a quarterly report on data protection metrics (e.g., access log reviews, incident reports, training completion).
- This policy will be reviewed annually, or following any significant security incident or change in applicable law.

## 8. Enforcement
Violations of this policy may result in disciplinary action, up to and including termination of employment or contracts, and may be reported to the Garante per la protezione dei dati personali.

## 9. References and Compliance
This policy is designed to ensure compliance with:
- **GDPR (EU) 2016/679** (Articles 5, 9, 25, 28, 32-34)
- **Codice in materia di protezione dei dati personali** (D.Lgs. 196/2003 as amended)
- **NIS2 Directive (EU) 2022/2555** (as transposed into Italian law)
- **Linee Guida AGID per la sicurezza ICT nelle PA**
- **ISO/IEC 27001:2022** (Annex A Controls, particularly A.8, A.9, A.13, A.18)
- **NIST Cybersecurity Framework 2.0**

## 10. Document Control

| Version | Date | Author | Changes | Approved By |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | [Date] | [DPO Name] | Initial Draft | [Hospital Director Name] |

---
*This policy document is the property of [Hospital Name] and is to be treated as confidential.*

</policy>

**Sources Consulted:**
*   *GDPR (EU) 2016/679, Articles 5, 6, 9, 28, 32-34.*
*   *Italian Legislative Decree 196/2003 (Codice in materia di protezione dei dati personali).*
*   *ISO/IEC 27001:2022, Annex A Controls.*
*   *NIST Cybersecurity Framework 2.0 (CSF 2.0).*
*   *AGID Linee Guida sulla sicurezza ICT nelle Pubbliche Amministrazioni.*
*   *NIS2 Directive (EU) 2022/2555.*
