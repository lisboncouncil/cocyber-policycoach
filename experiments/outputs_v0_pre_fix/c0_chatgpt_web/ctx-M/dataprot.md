---
config: C0+web
context_id: ctx-M
policy_id: P3
policy_name: Data Protection Policy
policy_short: dataprot
metadata:
  config: C0+web
  model: gpt-4.1-2025-04-14
  input_tokens: 1309
  output_tokens: 2410
  total_tokens: 3719
  latency_s: 18.548
  tool_calls: []
  raw_provider_id: resp_0967dab4698ce6130069fb69ba91dc8193b8ccaadae6619845
sources_count: 0
sources: []
prompt_chars: 4951
answer_chars: 9360
generated_at_unix: 1778084300
---

Certainly! Below is a tailored **Data Protection Policy** for the described NATO multinational military detachment, structured for auditability, alignment with the specified frameworks, and practical implementation in the stated environment.

---

# Data Protection Policy

**Organisation:** NATO Multinational Military Detachment (Romania Deployment)  
**Effective Date:** [Insert Date]  
**Policy Owner:** Information Systems Security Manager (ISSM), J6  
**Review Cycle:** Annual (or upon substantive change in regulatory/operational environment)  
**Classification:** NATO UNCLASSIFIED (NU)  
**Distribution:** Internal Use Only  

---

## 1. Purpose

This policy establishes the principles, requirements, and controls for the protection of personal data and sensitive operational information processed by the NATO Multinational Military Detachment deployed in Romania. It ensures compliance with NATO security directives, applicable host-nation and EU legal frameworks, and best-practice international standards, while enabling mission fulfilment under the operational constraints and threat landscape specific to the deployment.

---

## 2. Scope

This policy applies to all personnel (military, NATO civilian, contractors) with access to NATO Detachment information systems and data; to all data processed on Detachment-controlled network domains (NU, NR, NS, and MISSION SECRET); and to all information assets, regardless of medium or storage location, that are under the operational control of this Detachment.

---

## 3. Roles and Responsibilities

- **ISSM (J6):**  
  - Policy owner and authority for interpretation and exceptions.  
  - Oversight of implementation and review.  
  - Liaison with NCIRC, NCSC, host-nation CERT, and contributing nation authorities.  
- **ISSO(s):**  
  - Day-to-day administration, compliance monitoring, and incident management.  
  - Support to data protection impact assessments (DPIAs).  
- **COMSEC Custodians:**  
  - Enforce two-person integrity, dual-key procedures, and chain-of-custody for COMSEC material.  
  - Interface with national COMSEC authorities.  
- **Data Owners (Mission Functions):**  
  - Ensure classification, originator control (ORCON), and need-to-know enforcement for data under their remit.  
  - Validate legitimate data processing, sharing, and retention.  
- **All Users:**  
  - Adhere to policy and report suspected breaches.  
  - Complete mandatory annual data protection and security training.  
- **Contracting Officer's Representative (COR):**  
  - Ensure contractor compliance with this policy and applicable vetting/screening.  

---

## 4. Principles

- **Lawfulness, Fairness, and Transparency:**  
  Personal data shall be processed lawfully, fairly, and transparently in accordance with GDPR (Art. 5), Romanian CSL, and the NATO SOFA context ([GDPR], [Law 58/2019], [SOFA], [C-M(2002)49]).
- **Purpose Limitation:**  
  Data collected or processed must be for specified, explicit, and legitimate purposes, and not further processed in a manner incompatible with those purposes ([GDPR Art. 5(1)(b)], [ISO/IEC 27001:2022, A.8.2.3]).
- **Data Minimisation:**  
  Only data strictly necessary for mission or support purposes shall be collected and retained ([GDPR Art. 5(1)(c)], [NIST CSF ID.AM-2]).
- **Accuracy:**  
  Data must be accurate and, where necessary, kept up to date ([GDPR Art. 5(1)(d)], [ISO/IEC 27001:2022, A.8.2.2]).
- **Storage Limitation:**  
  Data shall be retained only as long as necessary for operational, legal, or contractual requirements ([GDPR Art. 5(1)(e)], [ISO/IEC 27001:2022, A.8.3.2]).
- **Integrity and Confidentiality:**  
  Data must be protected against unauthorised or unlawful processing, accidental loss, destruction, or damage, through appropriate technical and organisational measures ([NATO C-M(2002)49], [ISO/IEC 27001:2022, A.8.1.1], [NIST CSF PR.IP-3]).
- **Accountability:**  
  Compliance with this policy must be demonstrable and auditable ([GDPR Art. 5(2)], [ISO/IEC 27001:2022, A.5.1]).

---

## 5. Requirements and Controls

### 5.1. Data Classification and Handling  
- All information assets must be classified and labelled per NATO and mission-specific classification regimes (NU, NR, NS, MISSION SECRET, CTS) ([C-M(2002)49 Annex C], [AJP-3.20 §3.3.2]).  
- Need-to-know and ORCON principles are enforced by default technical and procedural controls ([AC/35-D/1015], [ISO/IEC 27001:2022, A.8.2.1]).
- Data spillage between classification domains is a reportable security incident and must be managed per incident response plans ([NCIRC IRP], [NIST CSF DE.CM-8]).

### 5.2. Access Control  
- Role-based access control (RBAC) is enforced; default deny for all data until explicit authorisation ([NIST CSF PR.AC-4], [ISO/IEC 27001:2022, A.9.1.2]).
- Identity is managed via PKI/smart card per domain; no cross-domain identity federation ([NATO INFOSEC AC/322-D(2017)0009 §4.2.3]).
- Two-person integrity is enforced for high-grade COMSEC and selected operational orders ([AC/35-D/1015], [ISO/IEC 27001:2022, A.9.4.3]).

### 5.3. Data Processing and Transfer  
- Personal data processing by NATO civilians and contractors is subject to GDPR, Romanian law (CSL), and SOFA limitations ([GDPR Art. 3], [Law 58/2019], [SOFA]).
- Transfers of classified or personal data outside the Detachment require authorisation from the ISSM/Data Owner and a documented risk assessment ([ISO/IEC 27001:2022, A.13.2.1]).
- Data shared with third parties (e.g., host-nation authorities, contractors) must use vetted channels and contracts with data protection clauses ([GDPR Art. 28], [NIST CSF PR.IP-5]).

### 5.4. Data Subject Rights (GDPR/Host Nation)  
- Data subjects (NATO civilians/contractors) have rights of access, rectification, and erasure as practicable under mission and security constraints ([GDPR Art. 15-17]).
- Requests are processed by the ISSM in coordination with legal advisors and may be limited where operational security dictates ([GDPR Art. 23 exemptions]).

### 5.5. Data Protection Impact Assessments (DPIA)  
- DPIAs are conducted for new systems or substantial changes involving personal data or high-risk information processing ([GDPR Art. 35], [ISO/IEC 27001:2022, A.8.2.5]).
- ISSM leads DPIA process and maintains records ([NIST CSF ID.RA-1]).

### 5.6. Incident Detection and Response  
- The theatre-level SOC provides 24/7 monitoring; all suspected or confirmed breaches involving personal or classified data are escalated per NCIRC/host-nation CERT processes ([NIST CSF DE.DP-1], [C-M(2002)49 Annex I], [ISO/IEC 27001:2022, A.16.1.1]).
- Incident logs are retained and auditable ([ISO/IEC 27001:2022, A.12.4.1]).

### 5.7. Training and Awareness  
- All personnel must complete a minimum of 40 hours/year of cybersecurity and data protection training ([NATO Cyber Defence Pledge 2016], [ISO/IEC 27001:2022, A.7.2.2]).
- Training content includes data protection, insider threat awareness, and incident reporting ([AC/35-D/1029], [NIST CSF PR.AT-1]).

### 5.8. Physical and Environmental Security  
- Physical access to information processing areas is restricted to authorised personnel, logged, and monitored ([ISO/IEC 27001:2022, A.11.1.1]).
- TEMPEST controls are enforced for classified processing as per NATO and national standards ([AJP-3.20 §3.9], [C-M(2002)49 Annex D]).

### 5.9. Supply Chain and Third-Party Security  
- Only NATO-approved and vetted vendors, equipment, and contractors may process or access Detachment data ([NIST CSF ID.SC-1], [ISO/IEC 27001:2022, A.15.1.1]).
- Security screening is mandatory for all host-nation and third-country contractors ([AC/35-D/1029], [ISO/IEC 27001:2022, A.7.1.2]).

### 5.10. Data Retention and Destruction  
- Data is retained only as long as necessary for mission, legal, or contractual purposes; secure destruction procedures apply for all media ([ISO/IEC 27001:2022, A.8.3.2], [NIST CSF PR.IP-6]).

---

## 6. Exceptions

Any exceptions to this policy must be documented, risk-assessed, and approved by the ISSM. Where exceptions impact personal data processing, legal counsel and the Data Protection Officer (if appointed) must be consulted. Unsupported exceptions must be marked as such and reviewed at least annually.

---

## 7. Monitoring and Review

- Policy and controls effectiveness are subject to annual review by the ISSM, with findings reported to the Detachment Commander and relevant NATO oversight bodies ([ISO/IEC 27001:2022, A.18.2.1]).
- Compliance audits may be conducted by internal or external (NATO, NCIRC, host-nation) authorities.
- Policy is updated upon significant regulatory, operational, or threat environment changes.

---

## 8. References

1. NATO Information Security Policy (C-M(2002)49 and successors)
2. NATO AC/35-D/1015, Security within NATO
3. NATO AC/35-D/1029, Personnel Security
4. NATO AC/322-D(2017)0009, INFOSEC Technical Directive
5. NATO Cyber Defence Pledge (2016)
6. Allied Joint Doctrine for Cyberspace Operations (AJP-3.20)
7. Romanian Cybersecurity Law 58/2019 (NIS/NIS2)
8. General Data Protection Regulation (GDPR, EU 2016/679)
9. NATO SOFA (London, 1951)
10. NIST Cybersecurity Framework (CSF) 2.0
11. ISO/IEC 27001:2022 and ISO/IEC 27002:2022

---

**This policy is effective as of [Insert Date] and remains in force until formally revised or rescinded.**

---

**[End of Document]**
