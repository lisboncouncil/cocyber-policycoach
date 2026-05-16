---
config: C0+web
context_id: ctx-H
policy_id: P2
policy_name: Data Protection Policy
policy_short: dataprot
metadata:
  config: C0+web
  model: gpt-4.1-2025-04-14
  input_tokens: 1440
  output_tokens: 2095
  total_tokens: 3535
  latency_s: 38.186
  tool_calls: []
  raw_provider_id: resp_02ed0b5d2b54518b0069fb701f037c81939ebb8cb363230caf
sources_count: 0
sources: []
prompt_chars: 4671
answer_chars: 8309
generated_at_unix: 1778085955
---

---

# Data Protection Policy

**Organisation:** Azienda Sanitaria Locale — Small Public Hospital (Province-Level), Italy  
**Effective Date:** 2024-07-01  
**Policy Owner:** Head of Administration (DPO)  
**Review Cycle:** Annual (or upon significant regulatory or operational changes)  
**Approved by:** General Director  
**Working Language:** English (operational translation to Italian mandatory for staff training and awareness)

---

## 1. Purpose

This Data Protection Policy establishes the principles, roles, and controls for the secure and lawful management of personal and special category (health) data within the hospital, in compliance with the General Data Protection Regulation (GDPR, Regulation EU 2016/679), relevant Italian law (D.Lgs. 196/2003 as amended), NIS2 Directive (EU 2022/2555), applicable regional health regulations, and the Linee Guida AGID for public administration. The policy also aligns with international best practices, including ISO/IEC 27001:2022 (selected controls) and NIST Cybersecurity Framework 2.0, within the hospital’s resource and operational constraints.

---

## 2. Scope

This policy applies to all personal data processed by the hospital, including special category data (health data, minors' data, employee data) in electronic and paper form. It covers:

- All staff (clinical, administrative, technical), contractors, and third parties with access to hospital information systems.
- All data processing activities related to patient care, administration, and hospital operations.
- All IT systems, medical devices with data storage capability, workstations, mobile devices, and paper records.

---

## 3. Roles and Responsibilities

| Role                    | Responsibilities                                                                                             |
|-------------------------|-------------------------------------------------------------------------------------------------------------|
| **Data Controller**     | Hospital, represented by the General Director or delegate (DPO): overall responsibility for compliance.     |
| **Data Protection Officer (DPO)** | Advises on data protection, monitors compliance, point of contact for Garante Privacy and data subjects. |
| **Hospital IT Staff (internal and MSP)** | Implements technical and organisational controls, reports incidents, supports DPO.             |
| **Clinical/Administrative/Technical Staff** | Follows policy requirements, attends training, reports breaches or suspected incidents.           |
| **External MSP/Vendors** | Bound by contract to comply with hospital's data protection obligations and report incidents.               |

*References: GDPR Art. 4(7), ISO/IEC 27001:2022 A.5.3, NIS2 Art. 21*

---

## 4. Principles

All personal data processing must adhere to the following principles:

- **Lawfulness, Fairness, and Transparency** (GDPR Art. 5(1)(a))
- **Purpose Limitation** (GDPR Art. 5(1)(b))
- **Data Minimisation** (GDPR Art. 5(1)(c))
- **Accuracy** (GDPR Art. 5(1)(d))
- **Storage Limitation** (GDPR Art. 5(1)(e))
- **Integrity and Confidentiality** (GDPR Art. 5(1)(f); NIS2 Art. 21)
- **Accountability** (GDPR Art. 5(2); ISO/IEC 27001 A.5.1)

---

## 5. Requirements and Controls

### 5.1. Legal Basis and Data Subject Rights

- All processing of personal and health data must have a valid legal basis (GDPR Art. 6, Art. 9).  
- Data subjects must be informed of their rights and provided with transparent privacy notices (GDPR Art. 12–14; Provvedimenti Garante Privacy in sanità).
- Requests for access, rectification, erasure, restriction, and objection must be handled without undue delay (GDPR Art. 15–21).

*References: GDPR, D.Lgs. 196/2003*

---

### 5.2. Data Classification and Handling

- Information assets must be classified by sensitivity: public, internal, personal, special category (health) (ISO/IEC 27001:2022 A.5.12).
- Special category data must only be accessed by authorised personnel and processed with enhanced controls (GDPR Art. 9; AGID Misure Minime 2.0 Area 4).

---

### 5.3. Access Control and Identity Management

- All users must authenticate via unique credentials (Active Directory, SPID/CIE federation) (ISO/IEC 27001:2022 A.5.18; NIS2 Art. 21(2)(d)).
- Access is granted based on least privilege and role-based access (GDPR Art. 32(1)(b); AGID Misure Minime 2.0 Area 4).
- Access reviews must occur at least annually and upon staff role change or termination (ISO/IEC 27001:2022 A.5.18).

---

### 5.4. Technical Security Measures

- Network segmentation between clinical and administrative VLANs must be maintained; PACS restricted as an “island” (ISO/IEC 27001:2022 A.8.20; NIST CSF PR.AC-5).
- Anti-virus and endpoint protection must be active on all supported workstations (AGID Misure Minime 2.0 Area 5).
- Legacy systems must be isolated wherever feasible and monitored for vulnerabilities (AGID Misure Minime 2.0 Area 5).
- VPN required for remote access to hospital systems (ISO/IEC 27001:2022 A.8.23).

---

### 5.5. Data Storage, Retention, and Backup

- Personal and health data stored only as long as necessary for clinical or legal purposes (GDPR Art. 5(1)(e); D.Lgs. 196/2003).
- Nightly on-premises backups and weekly off-site tape backups must be maintained; backups must be encrypted (AGID Misure Minime 2.0 Area 6; NIST CSF PR.IP-4).
- Disaster recovery tests to be conducted at least every 18 months, with documented results (ISO/IEC 27001:2022 A.5.30).

---

### 5.6. Data Breach and Incident Management

- All suspected or confirmed data breaches must be reported to the DPO immediately and escalated to the external MSP as per documented incident procedures (GDPR Art. 33, 34; NIS2 Art. 23; AGID Linee Guida 2022).
- Data breaches must be notified to Garante Privacy within 72 hours, and to data subjects when required (GDPR Art. 33, 34).
- An incident response runbook is to be developed and reviewed annually (NIS2 Art. 21(2)(f); ISO/IEC 27001:2022 A.5.25).

---

### 5.7. Third Party and Supply Chain Security

- MSPs and vendors must be contractually bound to GDPR and NIS2 compliance, including reporting obligations (GDPR Art. 28; NIS2 Art. 21(2)(e)).
- Third-party access must be logged and regularly reviewed (ISO/IEC 27001:2022 A.5.22).

---

### 5.8. Physical Security and Device Management

- Physical access to IT rooms and data archives restricted to authorised personnel (ISO/IEC 27001:2022 A.7.2; AGID Misure Minime 2.0 Area 3).
- Mobile devices at point-of-care must be protected by PIN/password and physical security measures; incidents of loss or theft must be immediately reported (Provvedimenti Garante Privacy 2015; ISO/IEC 27001:2022 A.8.1).

---

### 5.9. Training and Awareness

- All staff must receive at least 2 hours of data protection and cybersecurity training per year, with additional induction for new hires (GDPR Art. 39(1)(b); NIS2 Art. 20(2)).
- Training records must be maintained by HR and reported to the DPO annually.

---

## 6. Exceptions

Any exceptions to this policy must be formally approved by the General Director, with documented risk assessment and mitigation measures, and reported to the DPO. Exceptions may not contravene mandatory legal or regulatory requirements.

---

## 7. Monitoring and Review

- Compliance with this policy is monitored by the DPO and subject to periodic internal review and audit (ISO/IEC 27001:2022 A.5.36).
- The policy shall be reviewed annually, or upon significant change in law, regulation, or hospital operations.
- Audit findings, incidents, and breaches will be reported to hospital management and used to update the policy and controls.

---

## 8. References

- **EU GDPR** (Regulation EU 2016/679): [Text](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- **D.Lgs. 196/2003** as amended by D.Lgs. 101/2018
- **NIS2 Directive** (EU 2022/2555): [Text](https://eur-lex.europa.eu/eli/dir/2022/2555/oj)
- **Linee Guida AGID per la sicurezza informatica nella PA** (2022)
- **Provvedimenti Garante Privacy in sanità** (2015–2023)
- **ISO/IEC 27001:2022** (selected controls: A.5, A.7, A.8)
- **NIST Cybersecurity Framework 2.0** (selected functions: Identify, Protect, Detect, Respond, Recover)
- **AGID Misure Minime per la PA** (2.0, 2019)
- **Regional FSE Regulations**

---

**End of Policy Document**
