---
config: C2
context_id: ctx-H
policy_id: P5
policy_name: General Cybersecurity Policy
policy_short: infosec
metadata:
  config: C2
  model: moonshotai/Kimi-K2.5
  input_tokens: 25349
  output_tokens: 6141
  total_tokens: 31490
  latency_s: 45.129
  tool_calls:
  - rag_retrieval
  raw_provider_id: 3c894f25-0ff3-4bcd-a562-dde98ccca81d
  chunks_retrieved: 5
  server_version: 1.3.4
sources_count: 4
sources:
- type: kb_source
  source: ./datadir-plus-templates/cybersecurity_policy_BASIC.docx
  title: ./datadir-plus-templates/cybersecurity_policy_BASIC.docx
- type: kb_source
  source: ./datadir-plus-templates/asset_management.docx
  title: ./datadir-plus-templates/asset_management.docx
- type: kb_source
  source: ./datadir-plus-templates/9.json
  title: 'The Sector CSIRT Framework: Developing Sector-Based Incident Response Capabilities'
- type: kb_source
  source: ./datadir-plus-templates/1.json
  title: Best Practices for Cyber Crisis Management
prompt_chars: 4683
answer_chars: 17147
generated_at_unix: 1778086713
---

 <policy title="General Cybersecurity Policy">

| Field | Value |
|---|---|
| **Document ID** | POL-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Internal — All Staff |
| **Owner** | IT Manager / Responsabile della Sicurezza Informatica |
| **Approved by** | Direttore Generale (CEO) |
| **Approval date** | [DD/MM/YYYY] |
| **Next review date** | [DD/MM/YYYY] |
| **Review cycle** | Annual (and upon significant regulatory or organisational change) |

---

## 1. Purpose

This Cybersecurity Policy establishes the minimum security requirements applicable to all departments, systems, and personnel of [Organisation] — a public hospital operating within the Servizio Sanitario Nazionale (SSN) and classified as an **essential entity** under Directive (EU) 2022/2555 (NIS2). 

The policy ensures the protection of patient health data, the continuity of 24/7 clinical services, and compliance with EU and Italian cybersecurity and data protection regulations. It defines a pragmatic, risk-based security framework proportionate to the organisation’s size (200 staff, 80 beds), resource envelope (70,000 EUR annual cybersecurity budget), and reliance on managed service providers (MSP), while prioritising patient safety and clinical availability.

This document supports compliance with:
- NIS2 Directive (EU) 2022/2555 — Articles 21, 23 (risk management and incident reporting)
- GDPR (EU) 2016/679 and D.Lgs. 196/2003 (Codice in materia di protezione dei dati personali)
- AGID Linee Guida per la sicurezza informatica nella PA and Misure minime di sicurezza ICT per le pubbliche amministrazioni
- ISO/IEC 27001:2022 (Information Security Management Systems)
- NIST Cybersecurity Framework 2.0

---

## 2. Scope

This policy applies to:

- **All personnel**: 200 employees (130 clinical, 50 administrative, 20 technical/facility), contractors, agency staff, and students on placement
- **All information systems**: 220 workstations (including 35 legacy Windows clinical kiosks), 60 mobile point-of-care devices, servers, network infrastructure (UTM, VPN), and clinical applications (FSE, PACS/RIS, LIS, ADT, Pharmacy management)
- **All data categories**: Special category health data (Article 9 GDPR), personal data of minors, and employee data processed in the context of hospital operations
- **All third parties**: Managed Service Provider (MSP), medical device vendors, maintenance contractors, and regional ASL/SSN federated services (SPID/CIE)
- **All locations**: Internal medicine, general surgery, paediatrics, long-term care, emergency first aid wards, and administrative offices

---

## 3. Roles and Responsibilities

### 3.1 Direttore Generale (CEO)
- Approve this policy and provide strategic direction and resources for information security
- Appoint the Responsabile della Sicurezza Informatica (IT Manager) and ensure NIS2 Article 21 governance requirements are met
- Receive immediate notification of Critical incidents (ransomware, data breaches affecting >1000 patients, system outages exceeding RTO)

### 3.2 IT Manager / Responsabile della Sicurezza Informatica (Policy Owner)
- Own, maintain, and communicate this policy and subordinate procedures
- Oversee the MSP contract to ensure security obligations are enforced (NIS2 Article 28 supply-chain security)
- Conduct annual risk assessments and report ISMS performance to the Direttore Generale
- Serve as single point of contact for CSIRT Italia and Garante per la Protezione dei Dati in case of incidents

### 3.3 Managed Service Provider (MSP)
- Implement and operate technical controls (firewall, AV, backup, patching) as contracted
- Provide monthly security reports (patch status, backup success, incidents) to the IT Manager
- Maintain 24/7 escalation capability for Critical incidents (ransomware, EHR unavailability)
- Ensure sub-processors meet AGID security requirements for public administration

### 3.4 Clinical Directors (Responsabili di Struttura Complessa)
- Act as Asset Owners for clinical systems in their wards (PACS workstations, mobile devices, kiosks)
- Approve access requests for clinical staff and notify IT of departures within 24 hours (high turnover management)
- Ensure clinical staff comply with security procedures that do not impede emergency workflows

### 3.5 Privacy Officer / Responsabile della Protezione dei Dati (RPD)
- Advise on data protection impact assessments (DPIA) for clinical systems processing health data
- Coordinate breach notification to Garante within 72 hours (GDPR Article 33) and to affected patients where high risk

### 3.6 All Employees and Contractors
- Complete mandatory 2-hour annual cybersecurity awareness training (AGID Misure Minime)
- Report suspected phishing, lost devices, or system anomalies immediately to IT/MSP
- Comply with the 10 Golden Rules for Cybersecurity (POL-009) and Acceptable Use Policy

---

## 4. Policy Principles

### 4.1 Patient Safety and Clinical Availability
Security controls must never impede emergency clinical workflows. Availability targets (RTO 1h for ADT/PS, 4h for EHR) take precedence over investigative activities during active clinical emergencies.

### 4.2 Proportionate Risk Management
Controls are scaled to the organisation’s size (200 staff, 1.5 FTE IT) and threat profile (ransomware, phishing, supply chain). Legacy systems (35 Windows kiosks) are managed through compensating controls (network isolation) rather than aggressive patching that could destabilise patient care.

### 4.3 Clear Accountability Despite Outsourcing
While technical operations are outsourced to the MSP, [Organisation] retains legal accountability for NIS2 and GDPR compliance. The MSP acts under instruction; the IT Manager retains decision authority for security exceptions.

### 4.4 Defense in Depth for Critical Systems
Clinical networks (FSE, PACS) are segmented from administrative VLANs. Internet-facing medical devices are isolated. Multi-factor authentication (MFA) is enforced where technically feasible, particularly for remote access and privileged accounts.

### 4.5 Regulatory Compliance and Transparency
[Organisation] maintains transparency with regulators (AGID, Garante, CSIRT Italia) and collaborates with regional ASL and the national CSIRT. Incident reporting timelines (72 hours for personal data breaches, 24 hours for NIS2 significant incidents) are strictly observed.

---

## 5. Minimum Requirements

### 5.1 Governance and Risk Management
- **Annual Risk Assessment**: Conduct a cybersecurity risk assessment at least annually, or upon significant change (new clinical system, MSP contract renewal), aligned with ISO 27001:2022 Control 5.1.1 and NIS2 Article 21.1. *Source: ISO 27001:2022 5.1.1, NIS2 Art. 21*
- **Asset Inventory**: Maintain an up-to-date inventory of all 220 workstations, 60 mobile devices, clinical systems (FSE, PACS, LIS, ADT), and network components. Medical devices with embedded software are explicitly included. *Source: ISO 27001:2022 5.9, CIS Controls v8.1*
- **MSP Oversight**: Review MSP security practices annually; ensure contract includes right-to-audit and incident notification clauses (24 hours). *Source: NIS2 Art. 28 (supply chain security)*

### 5.2 Asset and Infrastructure Management
- **Maintenance Contracts**: Ensure equipment essential to critical systems (PACS servers, ADT) has documented maintenance contracts or spare parts provisions to meet RTO targets. *Source: ISO 27001:2022 5.11*
- **Anti-Malware**: Deploy approved anti-malware on all 220 endpoints (excluding isolated legacy kiosks where technically incompatible, subject to exception process). Keep signatures updated daily. *Source: AGID Misure Minime (Endpoint Protection)*
- **Network Segmentation**: Maintain separation between clinical VLANs (FSE, PACS island) and administrative networks. Legacy Windows kiosks (35 units) must be isolated in a dedicated VLAN with no internet access and restricted east-west traffic. *Source: ISO 27001:2022 8.21, NIST CSF 2.0 PR.AC-5*

### 5.3 Vulnerability and Patch Management
- **Standard Systems**: Apply critical security patches within 7 days of release for internet-facing systems; 30 days for internal systems. *Source: ISO 27001:2022 5.18, AGID Misure Minime*
- **Legacy/Medical Devices**: For systems where patching is infeasible (legacy kiosks, embedded medical devices), implement compensating controls: network isolation, disabled USB ports, application whitelisting, and enhanced monitoring. Document risk acceptance. *Source: ISO 27001:2022 5.18 (risk-based approach)*
- **Vulnerability Scanning**: Conduct internal vulnerability scans quarterly via MSP tools; remediate High/Critical findings within 30 days. *Source: CIS Controls v8.7.5*

### 5.4 Access Management
- **Identity Federation**: Utilise regional SPID/CIE federation for authentication to FSE where supported; maintain on-prem AD for legacy systems. *Source: AGID Linee Guida SPID*
- **High Turnover Management**: Implement automated account deprovisioning within 24 hours of termination notification from HR; quarterly access reviews for clinical shared accounts (kiosks). *Source: ISO 27001:2022 5.16, 5.18*
- **Privileged Access**: Restrict administrative access to PACS and ADT servers to maximum 3 individuals; require MFA for all privileged accounts. *Source: ISO 27001:2022 5.16, NIST CSF 2.0 PR.AC-1*
- **Kiosk Security**: Shared clinical kiosks (35 legacy units) must auto-logout after 5 minutes of inactivity; generic accounts prohibited where possible, otherwise unique per-shift credentials. *Source: ISO 27001:2022 5.15*

### 5.5 Logging and Monitoring
- **Critical Systems Logging**: Enable authentication logs (success/failure) on PACS, ADT, and FSE gateways. Retain logs for 12 months with integrity protection. *Source: ISO 27001:2022 8.15, AGID Misure Minime (Logging)*
- **Review**: IT Manager reviews MSP security logs monthly for anomalies; escalate suspected ransomware activity immediately to CSIRT Italia. *Source: NIS2 Art. 21.2 (monitoring)*

### 5.6 Backup and Recovery
- **Backup Schedule**: Maintain nightly backups to NAS and weekly off-site tape rotation. Encrypt backup data at rest and in transit (AES-256). *Source: ISO 27001:2022 5.30, GDPR Art. 32*
- **DR Testing**: Conduct disaster recovery testing at least annually (correcting current 18-month gap) to validate RTO 4h (EHR) and RTO 1h (ADT/PS). Document test results and remediate gaps. *Source: ISO 27001:2022 5.30, AGID Misure Minime (Business Continuity)*
- **Immutable Backups**: Implement write-once-read-many (WORM) or air-gapped backups for critical clinical data to protect against ransomware deletion. *Source: NIST CSF 2.0 PR.IP-4*

### 5.7 Incident Response
- **Cyber Incident Response Plan (CIRP)**: Maintain documented CIRP (POL-008) including specific ransomware playbooks (isolation procedures, no-payment decision authority resting with Direttore Generale). *Source: ISO 27001:2022 5.24, 5.25, NIS2 Art. 23*
- **Reporting**: Report significant incidents (ransomware, data breaches >1000 records, service outage >4h) to CSIRT Italia within 24 hours and to Garante within 72 hours (if personal data involved). *Source: NIS2 Art. 23, GDPR Art. 33*
- **MSP Escalation**: Define tier-1 (MSP handles), tier-2 (IT Manager engaged), tier-3 (Direttore Generale/CIRP activated) escalation criteria. *Source: ISO 27001:2022 5.26*

### 5.8 Awareness and Training
- **Mandatory Training**: All staff complete 2 hours of security awareness training annually, covering phishing recognition, physical theft prevention (mobile devices), and patient data confidentiality. *Source: ISO 27001:2022 6.3, GDPR Art. 39*
- **High Turnover Adaptation**: Provide condensed 30-minute security briefing upon onboarding for clinical agency staff, covering the 10 Golden Rules and kiosk usage. *Source: AGID Misure Minime (Formazione)*
- **Phishing Simulations**: Conduct quarterly phishing simulations; repeat training for repeat offenders. *Source: NIST CSF 2.0 PR.AT-1*

---

## 6. Exceptions

Exceptions to this policy (e.g., unpatched legacy kiosks, absence of MFA on specific clinical devices) may be granted only where:

1. A documented business/clinical justification exists (e.g., FDA-certified medical device with no patch available)
2. Compensating controls are implemented (network isolation, physical security, enhanced monitoring)
3. The IT Manager approves in writing; high-risk exceptions require Direttore Generale approval
4. The exception is time-limited (maximum 12 months) and recorded in the ISMS exception register
5. Residual risk is formally accepted by the Asset Owner (Clinical Director)

*Source: ISO 27001:2022 5.36 (Policy for exceptions)*

---

## 7. Enforcement

Non-compliance with this policy is treated as a disciplinary matter under the applicable Contratto Collettivo Nazionale del Lavoro (CCNL) for public health employees and [Organisation]'s internal disciplinary code.

| Severity | Examples | Consequence |
|---|---|---|
| Minor | Failure to complete annual training within deadline | Written warning, mandatory retraining within 7 days |
| Moderate | Sharing credentials for clinical kiosks, failure to report lost device within 24h | Formal disciplinary sanction, suspension of system access |
| Severe | Intentional circumvention of security controls, unauthorised data export (insider threat), phishing-induced ransomware infection through gross negligence | Suspension, termination of employment, referral to Ordine dei Medici/Professionisti and law enforcement (Codice Penale Art. 615-ter, 616-bis) |

*Source: D.Lgs. 196/2003 (sanctions), NIS2 Art. 34 (penalties)*

---

## 8. Related Documents

| Document ID | Title |
|---|---|
| POL-002 | Access Control Policy |
| POL-003 | Asset Management Policy (Medical Devices and ICT) |
| POL-004 | Backup and Recovery Policy |
| POL-005 | Network Security Policy (Segmentation and Remote Access) |
| POL-006 | Password Policy |
| POL-007 | Vulnerability and Patch Management Policy |
| POL-008 | Cyber Incident Response Plan (including Ransomware Playbook) |
| POL-009 | 10 Golden Rules for Cybersecurity |
| REG-001 | MSP Security Requirements Schedule |
| REG-002 | Data Breach Notification Procedure (GDPR/NIS2) |

---

## 9. Definitions

| Term | Definition |
|---|---|
| **ASL** | Azienda Sanitaria Locale — Local Health Authority within the SSN |
| **ADT** | Admission, Discharge, Transfer system (patient administration) |
| **FSE** | Fascicolo Sanitario Elettronico (Electronic Health Record) |
| **LIS** | Laboratory Information System |
| **MSP** | Managed Service Provider — external IT service provider |
| **NIS2** | Directive (EU) 2022/2555 on measures for a high common level of cybersecurity |
| **PACS** | Picture Archiving and Communication System (radiology) |
| **RTO** | Recovery Time Objective — maximum acceptable downtime (1h for ADT/PS, 4h for EHR) |
| **RPO** | Recovery Point Objective — maximum acceptable data loss (24h for standard systems, 4h for critical) |
| **SPID/CIE** | Sistema Pubblico di Identità Digitale / Carta d'Identità Elettronica — national identity federation |
| **SSN** | Servizio Sanitario Nazionale — Italian National Health Service |

---

## 10. Compliance and Regulatory References

This policy was developed based on the following frameworks and legal obligations:

- **NIS2 Directive (EU) 2022/2555**: Articles 21 (cybersecurity risk management), 23 (incident reporting), 28 (supply chain security) — *applicable as [Organisation] is an essential entity in the health sector*
- **GDPR (EU) 2016/679**: Articles 5 (principles), 24 (responsibility of controller), 25 (data protection by design), 32 (security of processing), 33 (breach notification) — *health data is special category data under Art. 9*
- **D.Lgs. 196/2003** (Codice Privacy) as amended by D.Lgs. 101/2018: Misure minime di sicurezza, notification obligations
- **AGID (Agenzia per l'Italia Digitale)**: Linee Guida per la sicurezza informatica nella PA; Misure minime di sicurezza ICT per le pubbliche amministrazioni; Circolari AGID on cloud and data centre security
- **ISO/IEC 27001:2022**: Controls 5.1 (Policies), 5.9 (Inventory), 5.16 (Identity), 5.18 (Vulnerability), 5.24 (Planning IR), 5.30 (ICT readiness), 6.3 (Awareness), 8.15 (Logging), 8.21 (Network security)
- **NIST CSF 2.0**: Govern (GV), Protect (PR), Detect (DE), Respond (RS), Recover (RC) functions
- **CIS Controls v8**: Controls 1 (Inventory), 4 (Secure Config), 7 (Continuous Vulnerability Management), 8 (Audit Log Management)

---

## 11. Revision History

| Version | Date | Author | Description of Change |
|---|---|---|---|
| 1.0 | [DD/MM/YYYY] | IT Manager / Responsabile della Sicurezza Informatica | Initial release — aligned with NIS2 essential entity requirements and AGID Misure Minime |

---

## 12. Approval

| Role | Name | Signature | Date |
|---|---|---|---|
| Policy Owner (IT Manager / Responsabile della Sicurezza Informatica) | | | |
| Approved by (Direttore Generale) | | | |
| Privacy Review (Responsabile della Protezione dei Dati) | | | |
| Clinical Governance Review (Direttore Sanitario) | | | |

</policy>
