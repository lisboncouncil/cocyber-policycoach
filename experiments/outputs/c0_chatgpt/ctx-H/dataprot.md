---
config: C0
context_id: ctx-H
policy_id: P2
policy_name: Data Protection Policy
policy_short: dataprot
metadata:
  config: C0
  model: gpt-4.1-2025-04-14
  input_tokens: 1146
  output_tokens: 2813
  total_tokens: 3959
  latency_s: 27.257
  tool_calls: []
  raw_provider_id: chatcmpl-DcZZbTF0SIXs3Cmskscwr5fk4oM0v
sources_count: 0
sources: []
prompt_chars: 4671
answer_chars: 11146
generated_at_unix: 1778085605
---

---
# Data Protection Policy

**Organisation**: [Hospital Name Redacted]  
**Type**: Small Public Hospital (Province-Level, Generalist), Italy  
**Governing Entity**: Servizio Sanitario Nazionale – ASL Regionale  
**Policy Owner**: Director General (Data Controller)  
**Effective Date**: [Insert Date]  
**Policy Review Cycle**: Annual (or upon regulatory or organisational change)  
**Working Language**: Italian (official version: English for audit and compliance)

---

## 1. Purpose

This Data Protection Policy establishes the principles and minimum controls for the collection, processing, storage, transmission, and disposal of personal data—particularly special categories of health data—processed by [Hospital Name Redacted], in compliance with:

- Regulation (EU) 2016/679 (GDPR)
- Codice in materia di protezione dei dati personali (D.Lgs. 196/2003, as amended)
- NIS2 (Directive EU 2022/2555)
- AGID security guidelines for the Public Administration
- Garante Privacy sectoral provisions for healthcare
- Regional regulations on the Fascicolo Sanitario Elettronico (FSE)
- ISO/IEC 27001:2022 (target framework)
- NIST Cybersecurity Framework (CSF) 2.0 (guidance)

The goal is to safeguard the confidentiality, integrity, and availability of personal and health data, ensuring patient safety and regulatory compliance.

---

## 2. Scope

This policy applies to:

- All personal data processed by the hospital, including special categories (health data, minors’ data, employee data)
- All staff (clinical, administrative, technical), contractors, and external service providers (including MSPs)
- All information systems, workstations, mobile devices, and physical records under the hospital’s control
- All processing activities, including storage, transmission, backup, and disposal

---

## 3. Roles and Responsibilities

| Role | Responsibilities | Reference |
|------|------------------|-----------|
| **Data Controller** (Direttore Generale) | Overall accountability for data protection | GDPR Art. 4, 24 |
| **Data Protection Officer (DPO)** | Independent monitoring, advice, training, liaison with Garante Privacy | GDPR Art. 37–39 |
| **IT Manager** (internal + MSP) | Implementation of technical and organisational controls, access management, incident response | ISO 27001:2022 A.5.7, A.8, A.18 |
| **Clinical/Administrative Heads** | Ensure staff awareness, compliance within units, report incidents | AGID, NIS2, GDPR Art. 32 |
| **All Staff** | Adhere to policy, report breaches or risks, attend mandatory training | GDPR Art. 32, ISO 27001:2022 A.7.2.2 |
| **External Service Providers (e.g., MSP)** | Comply with data processing agreements, cooperate during incidents, follow minimum measures | GDPR Art. 28, NIS2 Art. 21 |

---

## 4. Data Protection Principles

This policy is based on the following principles:

1. **Lawfulness, Fairness, and Transparency**  
   Data must be processed lawfully, fairly, and in a transparent manner.  
   _Source: GDPR Art. 5(1)(a); ISO 27001:2022 A.18.1.1_

2. **Purpose Limitation**  
   Data collected for specified, explicit, and legitimate purposes only.  
   _Source: GDPR Art. 5(1)(b)_

3. **Data Minimisation**  
   Data must be adequate, relevant, and limited to what is necessary.  
   _Source: GDPR Art. 5(1)(c); NIST CSF ID.AM-1_

4. **Accuracy**  
   Data must be accurate and, where necessary, kept up to date.  
   _Source: GDPR Art. 5(1)(d)_

5. **Storage Limitation**  
   Data must not be kept longer than necessary for the purposes for which it is processed.  
   _Source: GDPR Art. 5(1)(e); AGID_

6. **Integrity and Confidentiality**  
   Data must be processed in a manner that ensures appropriate security, including protection against unauthorised or unlawful processing, accidental loss, destruction, or damage.  
   _Source: GDPR Art. 5(1)(f); ISO 27001:2022 A.8, A.13; NIS2 Art. 21_

7. **Accountability**  
   The hospital is responsible for, and must be able to demonstrate, compliance with these principles.  
   _Source: GDPR Art. 5(2)_

---

## 5. Data Protection Requirements and Controls

All controls below are to be implemented with due regard for the operational and resource constraints of the organisation, and in a manner that does not impede emergency clinical workflows.

### 5.1. Legal Basis and Records of Processing

- Maintain a Record of Processing Activities (ROPA) as per GDPR Art. 30, including all categories of data processed, purposes, and recipients.
- Ensure all processing is based on an appropriate legal basis (consent, legal obligation, vital interests, etc.)  
  _Source: GDPR Art. 6, 9, 30_

### 5.2. Data Subject Rights

- Enable and facilitate exercise of rights: access, rectification, erasure, restriction, objection, data portability.  
  _Source: GDPR Art. 12–23_
- Ensure procedures for responding to data subject requests within statutory timelines (30 days).  
  _Source: GDPR Art. 12.3_

### 5.3. Data Protection by Design and by Default

- Integrate data protection into all new and modified systems and processes (“privacy by design”).
- Apply data minimisation and pseudonymisation where feasible (e.g., in test environments).  
  _Source: GDPR Art. 25; ISO 27001:2022 A.5.7; AGID_

### 5.4. Access Control and Identity Management

- Grant access to personal data strictly on a need-to-know and least-privilege basis (role-based access controls).
- Enforce strong authentication for all users accessing clinical and administrative systems (prefer SPID/CIE federation where available).  
  _Source: ISO 27001:2022 A.9; AGID Misure Minime; NIS2 Art. 21_
- Conduct quarterly access reviews for EHR, PACS, and other critical systems.  
  _Source: ISO 27001:2022 A.9.2.5_

### 5.5. Secure Processing, Transmission, and Storage

- All personal data in transit over external networks must be encrypted (TLS 1.2 or higher).  
  _Source: AGID, ISO 27001:2022 A.10.1.1_
- Sensitive data at rest on servers and backups must be protected through logical access controls; encryption to be implemented where technically feasible.  
  _Source: AGID, NIS2, ISO 27001:2022 A.8.1.1_
- Mobile devices containing personal data must use device encryption and PIN/password protection.  
  _Source: Garante Provv. 2015, ISO 27001:2022 A.8.1.2_
- Storage of personal data on local workstation drives is prohibited unless justified and authorised by IT.  
  _Source: AGID Misure Minime_

### 5.6. Backups and Business Continuity

- Maintain daily backups (NAS) and weekly off-site backups (tape) for all critical systems containing personal data.
- Test restoration of backups at least annually; document test results.  
  _Source: ISO 27001:2022 A.17.1.3; AGID_
- Ensure that RTO targets for EHR (4h) and ADT/PS (1h) are met.
- Maintain and test manual fallback procedures for clinical continuity.  
  _Source: NIS2 Art. 21; ISO 27001:2022 A.17.1.1_

### 5.7. Incident Response and Breach Notification

- Document and maintain an incident response procedure for personal data breaches, including escalation to the MSP and notification of the DPO.  
  _Source: GDPR Art. 33–34, ISO 27001:2022 A.16.1.5_
- Notify the Garante Privacy and affected data subjects of personal data breaches as required by GDPR Art. 33–34.
- Maintain an incident log.

### 5.8. Supplier and MSP Management

- All external service providers (including the MSP) must sign a data processing agreement (DPA) and comply with the hospital’s security requirements.  
  _Source: GDPR Art. 28, NIS2 Art. 21_
- Conduct an annual review of supplier security controls (questionnaire or attestation).
- Ensure MSP access to systems is logged and auditable.

### 5.9. Physical Security

- Restrict access to clinical and administrative areas where personal data is processed or stored.
- Implement controls to mitigate theft of mobile devices (asset registers, cable locks, staff awareness).
- Secure paper records in lockable cabinets; limit printing of health data.  
  _Source: Garante Provv. 2015, ISO 27001:2022 A.11_

### 5.10. Data Retention and Disposal

- Apply data retention schedules in line with legal and regional requirements (e.g., health data: 10 years minimum).  
  _Source: D.Lgs. 196/2003, regional FSE regulations_
- Ensure secure deletion or destruction of data and media at end-of-life (e.g., certified wiping, shredding).  
  _Source: ISO 27001:2022 A.8.3.2, AGID_

### 5.11. Staff Training and Awareness

- All staff must complete mandatory data protection and cybersecurity training (minimum 2 hours/year).
- Training to address phishing, handling of special category data, and incident reporting.
- Provide targeted induction training for new/joining staff.  
  _Source: ISO 27001:2022 A.7.2.2, NIS2 Art. 21_

### 5.12. Data Protection Impact Assessment (DPIA)

- Conduct DPIAs for new projects or significant changes involving high-risk processing of health data (e.g., new clinical apps, device integrations).  
  _Source: GDPR Art. 35_

### 5.13. Logging and Monitoring

- Maintain audit logs of access to EHR, PACS, and other core clinical systems.
- Ensure logs are retained for at least 6 months and are regularly reviewed for anomalies.  
  _Source: AGID Linee Guida, ISO 27001:2022 A.12.4.1_
- Given resource constraints, monitoring is focused on AV console alerts and MSP reports; SIEM not in place.

---

## 6. Exceptions

- Any deviation from this policy must be formally requested in writing, justified (e.g., clinical emergency, technical limitation), and approved by the DPO and Data Controller.
- Temporary exceptions must be time-bound and reviewed at least quarterly.
- All exceptions and their rationales must be documented.

---

## 7. Monitoring and Review

- The Data Controller, with the support of the DPO and IT Manager, is responsible for monitoring policy compliance.
- The policy will be reviewed annually, or following changes to applicable laws, regulations, or organisational processes.
- Compliance will be assessed via periodic audits, MSP reports, and incident analysis.
- Non-compliance or repeated incidents will result in corrective actions, up to and including disciplinary measures.

---

## 8. References

- **GDPR (Regulation EU 2016/679)**: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679
- **Codice Privacy (D.Lgs. 196/2003, as amended by D.Lgs. 101/2018)**: https://www.garanteprivacy.it/web/guest/home/docweb/-/docweb-display/docweb/1311248
- **NIS2 Directive (EU 2022/2555)**: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022L2555
- **Linee Guida AGID per la sicurezza nella PA**: https://www.agid.gov.it/it/sicurezza
- **AGID Misure Minime di Sicurezza ICT**: https://www.agid.gov.it/sites/default/files/repository_files/misure_minime_sicurezza_pa.pdf
- **Provvedimenti Garante Privacy in sanità**: https://www.garanteprivacy.it/web/guest/home/docweb/-/docweb-display/docweb/948481
- **ISO/IEC 27001:2022**: [ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection]
- **NIST Cybersecurity Framework 2.0**: https://www.nist.gov/cyberframework
- **Regional FSE Regulations**: [Refer to Regione-specific documentation]

---

**End of Policy**

