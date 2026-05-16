---
config: C2
context_id: ctx-H
policy_id: P2
policy_name: Data Protection Policy
policy_short: dataprot
metadata:
  config: C2
  model: moonshotai/Kimi-K2.5
  input_tokens: 25321
  output_tokens: 7869
  total_tokens: 33190
  latency_s: 34.942
  tool_calls:
  - rag_retrieval
  raw_provider_id: 8b442014-c9af-4ff9-866e-5f67c1b8f8ad
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
answer_chars: 17134
generated_at_unix: 1778086610
---

 <policy title="Data Protection Policy">

| Field | Value |
|---|---|
| **Document ID** | POL-DATA-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Internal — Restricted |
| **Owner** | Data Protection Officer (DPO) / IT Manager |
| **Approved by** | Direttore Generale (CEO) |
| **Approval date** | [DD/MM/YYYY] |
| **Next review date** | [DD/MM/YYYY] |
| **Review cycle** | Annual (and upon significant regulatory change) |

---

## 1. Purpose

This Data Protection Policy establishes the framework for processing personal data at [Organisation] in compliance with the General Data Protection Regulation (GDPR (EU) 2016/679), the Italian Privacy Code (D.Lgs 196/2003 as amended by D.Lgs 101/2018), and the NIS2 Directive (EU) 2022/2555 (as an essential entity in the health sector). It ensures the confidentiality, integrity, and availability of personal data—particularly special category health data—processed in the Cartella Clinica Elettronica (CCE/FSE), PACS/RIS, LIS, ADT, and other clinical systems, while respecting patient safety and 24/7 operational requirements.

---

## 2. Scope

This policy applies to:

- All personal data processing activities, including special category health data (Article 9 GDPR), employee data, and data concerning minors
- All personnel: clinical staff (130), administrative staff (50), technical/facility staff (20), contractors, and the Managed Service Provider (MSP)
- All systems processing personal data: CCE/FSE, PACS, RIS, LIS, ADT, Pharmacy management, 220 workstations (including 35 legacy clinical kiosks), and 60 mobile point-of-care devices
- Third-party processors (MSP, medical device vendors, cloud services) operating under Article 28 GDPR contracts
- Physical and electronic records across all wards: internal medicine, general surgery, paediatrics, long-term care, and emergency first aid

---

## 3. Roles and Responsibilities

### 3.1 Data Protection Officer (DPO)
- Ensure compliance with GDPR, Italian Privacy Code, and NIS2 obligations *GDPR (EU) 2016/679 — Article 37*
- Maintain the register of processing activities (Art 30 GDPR)
- Liaise with the Garante per la Protezione dei Dati Personali and data subjects
- Advise on Data Protection Impact Assessments (DPIAs) for high-risk processing

### 3.2 IT Manager (acting as Information Security Officer)
- Implement technical and organisational security measures (TOMs) in coordination with the MSP
- Maintain the asset inventory of data-bearing systems *ISO/IEC 27001:2022 — Annex A 5.9*
- Execute data breach response procedures and document incidents

### 3.3 Managed Service Provider (MSP) — Data Processor
- Implement encryption, access controls, and backup procedures as specified in the Article 28 GDPR Data Processing Agreement (DPA)
- Report suspected personal data breaches to [Organisation] within 4 hours of detection *Directive (EU) 2022/2555 — Article 23*
- Maintain technical security measures per AGID Misure Minime for Public Administration

### 3.4 Department Heads (Clinical and Administrative)
- Act as data owners for their respective wards/units
- Authorise access requests based on clinical need (least privilege)
- Ensure staff handle physical records securely and report breaches immediately

### 3.5 All Employees and Contractors
- Process personal data only for authorised purposes (purpose limitation)
- Report suspected data breaches or lost/stolen devices immediately to IT and the DPO
- Complete mandatory data protection training (2 hours/year)

---

## 4. Policy Principles

Processing of personal data shall adhere to the principles of Article 5 GDPR:

### 4.1 Lawfulness, Fairness, and Transparency
Processing is based on legal grounds under Article 9 GDPR (healthcare provision) and Article 6 (public interest/official authority). Privacy notices are provided to patients via the FSE portal and ward signage.

### 4.2 Purpose Limitation
Data collected for healthcare provision (CCE, PACS) shall not be used for incompatible purposes (e.g., marketing) without explicit consent.

### 4.3 Data Minimization
Only data strictly necessary for the specific healthcare purpose shall be collected and retained *ISO/IEC 27001:2022 — Annex A 5.1*

### 4.4 Accuracy
Clinical and administrative staff must ensure patient data is accurate and updated promptly; rectification requests processed within 30 days *GDPR (EU) 2016/679 — Article 16*

### 4.5 Storage Limitation
Personal data retained only for periods specified by Italian healthcare retention laws (see §5.5).

### 4.6 Integrity and Confidentiality
Appropriate security measures (encryption, access control) protect against unauthorised processing, accidental loss, or destruction *GDPR (EU) 2016/679 — Article 32*

### 4.7 Accountability
[Organisation] demonstrates compliance through documented policies, DPIAs, and maintaining records of processing activities.

---

## 5. Policy Requirements

### 5.1 Data Classification and Inventory

| Classification Level | Description | Examples | Handling Requirements |
|---|---|---|---|
| **Special Category Health Data** | Data concerning health, genetics, sex life (Art 9 GDPR) | CCE records, PACS images, lab results | Highest protection: encryption at rest/transit, strict access control, audit logging |
| **Sensitive Personal Data** | Employee data, minors' data | HR records, payroll, paediatric patient IDs | Encryption required, limited access |
| **Internal Data** | Operational data not publicly disclosed | Shift schedules, internal memos | Access control, no public disclosure |
| **Public Data** | Data intended for public release | Press releases, public health statistics | No special restrictions |

- An up-to-date inventory of data assets (systems, databases, file shares) containing personal data is maintained by IT and reviewed every 6 months *ISO/IEC 27001:2022 — Annex A 5.9, 5.10*

### 5.2 Lawful Basis for Health Data
Processing of health data is permitted under Article 9(2)(h) GDPR (healthcare provision) and Article 110 of the Italian Privacy Code. For secondary uses (research, statistics), data must be anonymised or pseudonymised where possible *D.Lgs 196/2003 — Article 110-bis*

### 5.3 Data Minimization and Pseudonymization
- Clinical staff shall access only the specific patient records required for their current treatment episode
- Pseudonymization (replacing identifiers with tokens) applied to datasets used for research or quality improvement *GDPR (EU) 2016/679 — Article 32(1)(a)*
- Legacy Windows kiosks (35 units) restricted to read-only access where possible, with compensating network isolation controls

### 5.4 Encryption and Cryptographic Controls

**At Rest:**
- Databases containing CCE, PACS, and LIS data encrypted using AES-256 or equivalent *AGID Misure Minime — Technical Measure 4*
- Mobile point-of-care devices (60 units) encrypted via device-level encryption (BitLocker or equivalent) to mitigate theft risk *NIST CSF 2.0 — PR.DS-1*
- Backup tapes encrypted before off-site transport (weekly)

**In Transit:**
- All remote access to clinical systems via VPN using TLS 1.2 or higher *Directive (EU) 2022/2555 — Article 21(2)(c)*
- Email containing health data sent only through encrypted channels (PEC or TLS-secured email gateways)
- Web access to FSE/CCE via HTTPS with strong cipher suites

**Key Management:**
- Encryption keys managed by the MSP under the DPA; keys for backups stored separately from the backup media

### 5.5 Data Retention and Disposal

| Data Category | Retention Period | Legal Basis |
|---|---|---|
| Health records (adults) | 20 years from last update | Italian Civil Code / Healthcare regulations |
| Health records (minors) | Until patient reaches age 18 + 10 years | Italian Privacy Code provisions |
| Employment records | 10 years from termination | Italian Labour Law |
| System audit logs | 12 months (minimum) | AGID Misure Minime, GDPR Art 5(1)(f) |
| Security incident logs | 5 years | NIS2 implementation requirements |

**Disposal:**
- Electronic media: Secure erasure per DIN 66399 (Level 3) or NIST SP 800-88 Rev 1 (Clear/Purge) before reuse or disposal *ISO/IEC 27001:2022 — Annex A 5.11, 5.12*
- Paper records: Cross-cut shredding (DIN 66399 P-4 or higher)
- Certificates of destruction obtained for all media disposal performed by third parties

### 5.6 Access Control and Authentication

**Identity Management:**
- Unique user accounts for each staff member; shared accounts prohibited except for emergency break-glass procedures *ISO/IEC 27001:2022 — Annex A 5.16, 5.17*
- Integration with regional SPID/CIE federation for patient-facing services; internal Active Directory for staff

**Access Rights:**
- Role-Based Access Control (RBAC): Access granted based on clinical role (doctor, nurse, radiologist, admin) and ward assignment
- Principle of least privilege: Access to CCE/PACS limited to active treatment teams
- Access reviews conducted every 6 months by Department Heads with IT verification *ISO/IEC 27001:2022 — Annex A 5.18*

**Authentication:**
- Multi-factor authentication (MFA) enforced for:
  - Remote access (VPN) *Directive (EU) 2022/2555 — Article 21(2)(c)*
  - Privileged accounts (system administrators)
  - Access to high-risk systems (PACS admin, CCE databases)
- Password policy per POL-006 (Password Policy): minimum 12 characters, unique per system, managed via approved password manager

**Emergency Access (Break-Glass):**
- Emergency accounts for patient safety situations (e.g., unconscious patient in ER) available with automatic logging and post-event review
- Usage reported to DPO within 24 hours

### 5.7 Third Party Processors and Supply Chain Security

- All processors (MSP, cloud providers, medical device vendors) bound by Article 28 GDPR Data Processing Agreements specifying:
  - Permitted processing purposes
  - Sub-processor notification requirements
  - Security measures (encryption, access controls)
  - Breach notification timelines (4 hours for NIS2 incidents)
  - Audit rights for [Organisation] *GDPR (EU) 2016/679 — Article 28*
- Supply chain risk assessments conducted annually for critical vendors (MSP, PACS vendor) per NIS2 Article 21(2)(d) *Directive (EU) 2022/2555 — Article 21*
- Legacy Windows kiosks managed by vendors under specific security contracts ensuring isolation and patch management

### 5.8 Data Subject Rights Management

Procedures established for:
- **Access (Art 15):** Patients may request their CCE/FSE records; response within 30 days
- **Rectification (Art 16):** Correction of inaccurate health data by clinical staff
- **Erasure (Art 17):** Limited application for health data (overridden by medical retention laws), but accounts for deceased patients
- **Portability (Art 20):** Export of FSE data in structured format (PDF/HL7)
- **Restriction (Art 18):** Processing restricted where accuracy is contested

Requests logged and tracked by the DPO; identity verification required (SPID/CIE or ID card).

### 5.9 Personal Data Breach Response

**Detection and Reporting:**
- All staff must report suspected breaches (unauthorised access, lost device, ransomware) immediately to IT and DPO
- MSP reports technical breaches (unauthorised network access) within 4 hours

**Assessment:**
- DPO assesses likelihood of risk to rights and freedoms within 24 hours
- Documentation in breach register (Art 33(5) GDPR)

**Notification:**
- **Supervisory Authority (Garante):** Within 72 hours if likely to result in risk *GDPR (EU) 2016/679 — Article 33*
- **Data Subjects:** Without undue delay if high risk (e.g., large-scale health data exposure) *GDPR (EU) 2016/679 — Article 34*
- **NIS2 Reporting:** For significant incidents affecting service provision, report to CSIRT Italia within 24 hours (early warning) and 72 hours (full notification) *Directive (EU) 2022/2555 — Article 23*

**Containment:**
- Immediate isolation of affected systems (e.g., disconnect compromised workstation from CCE)
- Preservation of forensic evidence per Cyber Incident Response Plan (POL-008)

### 5.10 Physical Security of Data Assets

- Mobile devices (60 point-of-care tablets/laptops) encrypted and stored in locked cabinets when not in use
- Workstations in clinical areas configured with automatic screen lock (5 minutes inactivity)
- Paper records (patient charts) stored in locked ward offices; access restricted to assigned clinical teams
- Clean desk policy for administrative areas to prevent unauthorised viewing of patient data

---

## 6. Monitoring and Review

- Data protection compliance monitored via annual internal audit (ISO 27001 aligned) and DPO quarterly spot checks
- Access rights reviewed every 6 months (§5.6)
- Encryption status verified monthly by MSP for all servers and mobile devices
- Policy effectiveness reviewed annually by DPO and presented to Direttore Generale
- Review triggered by: significant incidents, regulatory changes (NIS2 implementation), or major system changes (new EHR deployment)

---

## 7. Training and Awareness

- All staff complete 2 hours annual data protection training covering: GDPR principles, phishing awareness, secure handling of health data, breach reporting procedures *GDPR (EU) 2016/679 — Article 39*
- Clinical staff: Specific training on CCE access protocols and patient confidentiality
- New hires: Data protection briefing before system access granted
- Training completion records maintained by HR and DPO for audit purposes

---

## 8. Exceptions

Exceptions to encryption or access control requirements (e.g., legacy medical devices unable to support encryption) require:
- Written risk assessment by IT Manager and DPO
- Compensating controls (network isolation, enhanced monitoring, physical security)
- Approval by Direttore Generale
- Entry in ISMS exception register with review date (maximum 12 months) *ISO/IEC 27001:2022 — Clause 6.1.3*

Emergency break-glass access for patient safety constitutes a temporary exception subject to post-event review (§5.6).

---

## 9. Enforcement

Non-compliance with this policy may result in disciplinary action per [Organisation] HR policies:
- **Minor:** Unintentional data entry error — retraining and documented warning
- **Moderate:** Repeated access violations, sharing credentials — formal disciplinary action
- **Severe:** Intentional data theft, unauthorised disclosure of patient data — dismissal and referral to Garante/law enforcement *D.Lgs 196/2003 — Articles 167-169*

---

## 10. Related Documents

| Document ID | Title |
|---|---|
| POL-001 | Cybersecurity Policy |
| POL-002 | Access Control Policy |
| POL-003 | Asset Management Policy |
| POL-004 | Backup and Recovery Policy |
| POL-006 | Password Policy |
| POL-008 | Cyber Incident Response Plan |
| POL-009 | 10 Golden Rules for Cybersecurity |
| DPA-MSP | Data Processing Agreement with Managed Service Provider |

---

## 11. Definitions

| Term | Definition |
|---|---|
| **Personal Data** | Any information relating to an identified or identifiable natural person (data subject) *GDPR (EU) 2016/679 — Article 4(1)* |
| **Special Category Data** | Personal data revealing racial or ethnic origin, political opinions, religious beliefs, trade union membership, genetic/biometric data, health data, or sex life *GDPR (EU) 2016/679 — Article 9* |
| **Pseudonymization** | Processing in such a manner that the data can no longer be attributed to a specific data subject without additional information *GDPR (EU) 2016/679 — Article 4(5)* |
| **MSP** | Managed Service Provider — external processor managing IT infrastructure |
| **CCE/FSE** | Cartella Clinica Elettronica / Fascicolo Sanitario Elettronico (Electronic Health Record) |
| **DPIA** | Data Protection Impact Assessment *GDPR (EU) 2016/679 — Article 35* |

---

## 12. Compliance and Regulatory References

- **GDPR (EU) 2016/679:** Articles 5 (Principles), 9 (Special categories), 25 (Data protection by design), 28 (Processors), 30 (Records), 32 (Security), 33-34 (Breach notification), 37 (DPO)
- **D.Lgs 196/2003 (Italian Privacy Code):** Articles 11-12 (Retention), 110-bis (Health data), 167-169 (Sanctions)
- **D.Lgs 101/2018:** Adaptation of Italian law to GDPR
- **Directive (EU) 2022/2555 (NIS2):** Articles 21 (Risk management), 23 (Reporting), 27 (Essential entities)
- **AGID Linee Guida:** Misure minime di sicurezza ICT per la PA (Minimum security measures for Public Administration)
- **ISO/IEC 27001:2022:** Annex A 5.1 (Policies), 5.9 (Inventory), 5.10 (Acceptable use), 5.11 (Return of assets), 5.12 (Classification), 5.13 (Labeling), 5.16 (Identity), 5.17 (Authentication), 5.18 (Access rights), 8.1 (User endpoint devices)
- **NIST CSF 2.0:** PR.AC (Access Control), PR.DS (Data Security), RS.AN (Anomalies and Events)

---

## 13. Revision History

| Version | Date | Author | Description of Change |
|---|---|---|---|
| 1.0 | [DD/MM/YYYY] | DPO / IT Manager | Initial release for NIS2/GDPR compliance |

---

## 14. Approval

| Role | Name | Signature | Date |
|---|---|---|---|
| Policy Owner (DPO) | | | |
| Approved by (Direttore Generale) | | | |
| IT Manager | | | |
| Compliance Review (Legal) | | | |

</policy>
