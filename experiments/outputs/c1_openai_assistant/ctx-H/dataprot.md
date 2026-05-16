---
config: C1
context_id: ctx-H
policy_id: P2
policy_name: Data Protection Policy
policy_short: dataprot
metadata:
  config: C1
  model: gpt-4.1
  input_tokens: 6392
  output_tokens: 3659
  total_tokens: 10051
  latency_s: 80.031
  tool_calls: []
  raw_provider_id: run_gvH4wKlcSWgO2ShcUAjIFJLZ
  run_status: completed
  thread_id: thread_Ff1HNDLPpH9x3ldyj0YZWblC
sources_count: 0
sources: []
prompt_chars: 4671
answer_chars: 16284
generated_at_unix: 1778087041
---

<policy title="Data Protection Policy">

---

**Organization:** [Province-Level Generalist Public Hospital, ASL, Servizio Sanitario Nazionale, Italy]  
**Effective Date:** [2024-06-07]  
**Policy Owner:** Data Protection Officer (DPO) / IT Services Manager  
**Review Cycle:** Annual (minimum); after any significant incident, regulation change, or organizational restructuring

---

## 1. PURPOSE

This Data Protection Policy establishes the guiding framework for the secure and compliant processing of personal data—especially special categories of health and minor data—managed by the hospital. The policy ensures data are handled lawfully, ethically, and with robust safeguards in compliance with GDPR (Regulation EU 2016/679), Codice in materia di protezione dei dati personali (D.Lgs. 196/2003, as amended), NIS2 Directive (EU 2022/2555), AGID security guidelines, Provvedimenti Garante Privacy in healthcare, and industry best practices (ISO/IEC 27001:2022, NIST CSF 2.0).

---

## 2. SCOPE

This policy applies to:

- All hospital staff (clinical, administrative, technical, external MSP)
- All personal data and special category data (including patient records, employee and minor data)
- All IT systems and platforms (EHR/FSE, PACS, RIS, LIS, ADT, pharmacy management)
- Workstations, mobile point-of-care devices, on-premises and cloud infrastructure
- External vendors, contractors, and service providers with access to data or systems
- Physical records where personal data is present
- Operations across all hospital wards/units (internal medicine, general surgery, paediatrics, long-term care, emergency/first aid), both onsite and remote

---

## 3. ROLES AND RESPONSIBILITIES

### 3.1 Data Protection Officer (DPO)*
- Ensures policy adoption and ongoing compliance
- Monitors GDPR and national regulatory developments
- Handles data subject requests and breach notifications
- Approves DPIAs for high-risk processing (*required under GDPR; function fulfilled by regional ASL reference if not directly appointed*)

### 3.2 IT Services Manager (or delegated external MSP)
- Implements technical safeguards for data protection
- Maintains inventory of digital assets processing personal data
- Oversees access management and incident reporting
- Coordinates with DPO for changes affecting data processing

### 3.3 Department Heads / Unit Managers
- Ensure local processes conform to data protection policy
- Support staff training and documentation
- Promptly escalate suspected data breaches

### 3.4 All Staff (employees, contractors, clinical, admin, technical)
- Follow procedures for lawful data handling
- Complete mandatory privacy and cybersecurity training
- Report suspected incidents, data loss, or policy violations

### 3.5 External Suppliers (MSP, medical device/software vendors)
- Adhere to contractually mandated data protection measures
- Support audits and technical assessments
- Notify of any incidents or security weaknesses impacting the hospital

---

## 4. POLICY PRINCIPLES

### 4.1 Lawfulness, Fairness, and Transparency
All data processing must have a clear legal basis, be fair to data subjects, and be transparent regarding purposes and recipients (GDPR Art. 5.1.a; D.Lgs. 196/2003; AGID Linee Guida).

### 4.2 Data Minimisation and Purpose Limitation
Data collected/processed must be strictly limited to what is necessary for delivery of healthcare and supporting hospital operations (GDPR Art. 5.1.b,c).

### 4.3 Integrity and Confidentiality
Personal data, especially health data, must be protected by appropriate technical and organizational measures to prevent unauthorized access, loss, alteration, or disclosure (GDPR Art. 5.1.f; ISO 27001:2022 A.5, A.8).

### 4.4 Accountability and Auditability
The hospital must be able to demonstrate compliance through documentation, records of processing, audits, and incident logs (GDPR Art. 5.2; AGID Misure Minime; NIS2).

### 4.5 Patient Safety Priority (Health Sector-Specific)
Security controls must not obstruct the continuity of life-critical clinical services, and emergency “break-glass” access is permitted under strict audit and documentation (Provvedimenti Garante Privacy in sanità; NIS2; AGID).

---

## 5. POLICY REQUIREMENTS

### 5.1 Data Inventory and Records of Processing

**Requirement:**  
Maintain a complete and updated record of all personal and special category data processing activities, including data categories, purposes, retention periods, lawfulness bases, and data flows (GDPR Art. 30; AGID).

**Process:**  
- Maintain electronic registry of processing as per GDPR Art. 30
- Update records upon introduction or decommissioning of systems
- Review at least annually and after significant IT or process change

**Responsible:** DPO (with IT Manager, department input)  
**Controls:** Inventory tool; periodic reconciliation; asset inventory (ISO 27001:2022 A.5, A.8)

---

### 5.2 Data Classification and Labelling

**Requirement:**  
Classify and label all data and records according to sensitivity and regulatory categories (personal, special category/health, minor, employee).

**Process:**  
- Adopt a three-tier schema: Personal, Special Category (Health/Minors), Administrative/internal
- Enforce via EHR, PACS, LIS, and shared drives where technically feasible

**Responsible:** IT Manager, clinical system owners  
**Controls:** Logical/physical labelling, user guidelines (ISO 27001 A.8, AGID, Garante Privacy)

---

### 5.3 Access Control and Authentication

**Requirement:**  
Restrict access to personal data on a strict need-to-know basis. Enforce individual authentication for all IT systems, with strong passwords and session timeouts (GDPR Art. 32; ISO 27001:2022 A.9).

**Process:**  
- Leverage AD + regional SPID/CIE federation for user access
- Disable shared accounts except where mandated by clinical risk protocol (“break-glass”)
- Mandatory password renewals every 180 days (adaptable based on technological capability)
- Biannual access review, or immediately on staff termination

**Responsible:** IT Manager, MSP, department heads  
**Controls:** AD group policies, system logs, quarterly user recertification

---

### 5.4 Data Encryption and Secure Storage

**Requirement:**  
Encrypt personal/special category data both at rest on portable/mobile devices and during transmission across public networks (GDPR Art. 32; AGID; NIS2).

**Process:**  
- Deploy file/database/table-level encryption on mobile devices where supported
- Enforce VPN for remote access to hospital systems
- Mandatory encryption of backups stored offsite

**Responsible:** IT Manager, MSP  
**Controls:** Encryption tool configuration, quarterly verification, exception documentation

---

### 5.5 Data Retention and Secure Disposal

**Requirement:**  
Retain personal data only for as long as necessary for its processing purpose and in compliance with applicable law. Perform secure deletion or anonymisation upon expiration.

**Process:**  
- Enforce legal retention schedules (per regional FSE/health record law; Codice Privacy; Garante)
- Logically delete/destroy data on decommissioned systems/devices using certified tools
- Document deletion/destruction (maintain logs)

**Responsible:** IT Manager, DPO, department heads  
**Controls:** DELETION logs, end-of-life checklists, offboarding protocols

---

### 5.6 Data Processing by Third Parties (Suppliers/MSP)

**Requirement:**  
Formalise and monitor data processing by third-party service providers under written contracts specifying GDPR-compliant data protection clauses (GDPR Art. 28, 32; NIS2; AGID).

**Process:**  
- Conduct DPIA (Data Protection Impact Assessment) when onboarding new MSP/service handling health data
- Ensure Data Protection Agreements in all contracts
- Annual audit of supplier compliance

**Responsible:** DPO, Procurement, IT Manager  
**Controls:** Contract checklists, compliance audits, supplier portal

---

### 5.7 Data Subject Rights Management

**Requirement:**  
Enable prompt and fully documented response to data subject (patient, staff) requests to exercise rights: access, rectification, erasure, restriction, objection, portability (GDPR Arts. 15–22).

**Process:**  
- Standardise request intake process (forms, email, oral at front desk)
- Log and process requests within 30 days maximum
- Escalate complex/exceptional cases to DPO

**Responsible:** DPO, with support from clinical/HR units  
**Controls:** Request logging system, tracking dashboard, annual report to management

---

### 5.8 Data Breach Management and Incident Response

**Requirement:**  
Promptly detect, contain, and report personal data breaches per GDPR Arts. 33-34 and sector regulations. Document all incidents and report to Garante Privacy/DPO per legal timelines.

**Process:**  
- Activate ad-hoc breach procedure with incident logging
- Notify DPO and (where mandated) Garante Privacy within 72 hours
- Alert data subjects if the breach is likely to impact their rights/freedoms
- Post-incident root cause analysis and lessons learned

**Responsible:** IT Manager/MSP, DPO, Department heads  
**Controls:** Incident logbook, communication templates, root cause documentation

---

## 6. MONITORING AND REVIEW

### 6.1 Monitoring

**What to monitor:**
- Access logs (audit trails) for clinical and admin systems (weekly sample review)
- Backup job success/failure (daily)
- Encryption/antivirus status (monthly; MSP vendor portal)
- Data subject request register (quarterly)

**Responsible:** IT Manager, MSP, DPO  
**Retention:** Logs kept minimum 12 months or per regulatory requirement

### 6.2 Regular Reviews

- Annual comprehensive policy review (DPO-led, includes IT, clinical, admin perspectives)
- Ad-hoc policy update upon major threat, system, or legislative change
- Post-incident review and corrective actions

**Deliverable:** Annual Data Protection Review Report filed with regional ASL and accessible to audit

---

## 7. TRAINING AND AWARENESS

### 7.1 Mandatory Training

**All staff (clinical, administrative, technical) must complete:**
- Privacy and data protection awareness (minimum 2 hours/year)
- Phishing and cyber hygiene training (including runbooks for suspected incidents)
- Specialized training for system/data owners and managers

**Training topics:**
- GDPR basics and data subject rights
- Secure handling of health data
- Incident recognition and reporting
- Physical security of devices

### 7.2 Acknowledgment

- All staff must acknowledge policy completion in HR records
- Training attendance, materials and scores stored securely for reference

---

## 8. INCIDENT RESPONSE

### 8.1 Reporting

**Staff must immediately report:**
- Any suspected data breach, data loss, or unauthorised access
- Lost/stolen devices containing or accessing personal data

**Reporting channels:**
- Direct to IT Manager or DPO (dedicated internal email/telephone)
- Escalation via department head if DPO unavailable
- 24/7 critical clinical incident reporting line

### 8.2 Response Actions

Upon incident report:
1. Classify incident (data involved, impact analysis) — within 4 hours
2. Escalate to IT Manager/MSP and DPO, activate containment measures
3. Log all actions taken and preserve evidence (forensic if needed)
4. Complete regulatory notification (Garante) within 72h
5. Remediate; conduct post-mortem review and system hardening

---

## 9. COMPLIANCE AND AUDIT

### 9.1 Regulatory Compliance

This policy supports compliance with:
- **GDPR (EU 2016/679):** Arts. 5, 6, 9, 28, 30, 32–34
- **D.Lgs. 196/2003 as amended:** National data protection code
- **NIS2 (EU 2022/2555):** Essential entity obligations (health)
- **AGID/Misure Minime:** baseline security for PA
- **Provvedimenti Garante Privacy in Sanità:** healthcare-specific requirements
- **Regional FSE requirements:** health data mandates

### 9.2 Policy Review

- Annual DPO-led review (with IT, admin, clinical stakeholders)
- Immediate update after major tech or regulatory change or breach
- Version and approval tracking in Policy Control Table

### 9.3 Audit Rights

- Regional ASL/auditors may conduct reviews/audits
- Suppliers may be required to provide access for audit of contracted processing
- All findings documented; action plans mandatory for remediation

---

## 10. ENFORCEMENT

### 10.1 Policy Violations

Violations may result in:
- Remedial technical or organizational training/warning (minor)
- Temporary or permanent access restriction, HR disciplinary process (moderate)
- Civil or criminal proceedings in case of gross negligence/malicious acts (severe)
- Regulatory notification/reporting if data breach is involved

**Examples:**
- Unauthorized sharing of patient data (moderate/severe)
- Failure to report breach or lost device (moderate)
- Repeated insecure password handling (minor/moderate)

### 10.2 Documentation

Violations are tracked in HR records, with an anonymized summary provided annually for policy improvement

---

## 11. EXCEPTIONS

### 11.1 Exception Process

- Exception requests must be justified in writing and submitted to DPO or IT Manager
- Approval by DPO (or delegated data controller) mandatory
- Compensating controls considered (e.g., temporary audit, increased monitoring)
- Exceptions time-limited: maximum 6 months, with scheduled review

### 11.2 Emergency Access (“Break-glass” Protocol)

- Permits bypass of normal access controls in clinical emergencies
- All break-glass events must be logged (user, patient, timestamp, reason)
- DPO review of all such accesses monthly

---

## APPENDICES

### Appendix A: Definitions

- **Personal Data:** Any information relating to an identified or identifiable natural person (Art. 4(1) GDPR)
- **Special Category Data:** Includes data concerning health, minors, biometric/genetic data (Art. 9 GDPR)
- **Processing:** Any operation performed on data, including storage, access, transfer, deletion
- **Data Subject:** An individual whose data is processed by the hospital
- **DPO:** Data Protection Officer (GDPR-mandated role)
- **MSP:** Managed Service Provider
- **FSE:** Fascicolo Sanitario Elettronico (Regional Electronic Health Record)

### Appendix B: Forms and Templates

- Data subject request forms (access, rectification)
- Incident/Breach report form
- Exception request template
- Data processing checklist for new systems/services

### Appendix C: Contact Information

- DPO: [Regionally appointed; Contact: dpo@[hospital].it]
- IT Manager: [Contact: it_manager@[hospital].it; phone: xxxxx]
- 24/7 Clinical Incident Line: [internal extension xxxx]
- MSP Service Desk: [msp@[provider].it; phone: xxxxx]

### Appendix D: Technical Controls

- UTM firewall configuration standards
- AV/endpoint management (monthly update push via MSP console)
- Backup configuration policy summary
- Device encryption settings and acceptable use guidelines

---

## DOCUMENT CONTROL

| Version | Date       | Author                       | Changes                                        |
|---------|------------|------------------------------|------------------------------------------------|
| 1.0     | 2024-06-07 | DPO / IT Manager (draft)     | Initial issue                                  |
| 1.1     | [TBD]      | DPO                          | Annual review, update per regulatory changes    |

---

## APPROVAL BLOCK

Policy Approved By:

- **Hospital Director**: _______________ Date: _______________
- **DPO**: _______________ Date: _______________
- **IT Manager**: _______________ Date: _______________

---

## REFERENCES AND SOURCES

This policy was developed using the following frameworks and regulatory instruments:

- *GDPR (Regulation EU 2016/679), especially Arts. 5, 6, 9, 28, 30, 32–34*
- *D.Lgs. 196/2003, “Codice in materia di protezione dei dati personali” as amended by D.Lgs. 101/2018*
- *NIS2 Directive (EU 2022/2555) — Essential Entities (Health)*
- *ISO/IEC 27001:2022 (Controls A.5, A.8, A.9, A.12, A.18)*
- *NIST CSF 2.0 (“Protect”, “Detect”, “Respond” categories)*
- *AGID Linee Guida per la sicurezza informatica nella PA / Misure Minime*
- *Provvedimenti del Garante Privacy in ambito sanitario*
- *Regional regulations for FSE / digital health records*
- *Referenced internal hospital procedures and MSP contractual obligations*

---

</policy>
