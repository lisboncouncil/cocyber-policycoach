---
config: C1
context_id: ctx-H
policy_id: P5
policy_name: General Cybersecurity Policy
policy_short: infosec
metadata:
  config: C1
  model: gpt-4.1
  input_tokens: 6394
  output_tokens: 3968
  total_tokens: 10362
  latency_s: 38.641
  tool_calls: []
  raw_provider_id: run_mT9pfi9eGh74geVM6bBHROde
  run_status: completed
  thread_id: thread_Mopn8OdeBAH0B5brqdRmlkVC
sources_count: 0
sources: []
prompt_chars: 4683
answer_chars: 16418
generated_at_unix: 1778086315
---

<policy title="General Cybersecurity Policy for [Small Public Hospital], Italy">
  
---

## POLICY HEADER BLOCK

**Organization:** [Small Public Hospital], Province-level, ASL-governed, Italy  
**Effective Date:** [Insert date of approval]  
**Policy Owner:** Chief Administrative Officer (with delegated IT responsibility)  
**Review Cycle:** Annual (or sooner if required by regulatory change or incident)

---

## 1. PURPOSE

This General Cybersecurity Policy establishes the principles, responsibilities, and controls for information and cyber risk management at [Small Public Hospital], in support of the safety and continuity of clinical services and the confidentiality, integrity, and availability of patient and operational data. The policy ensures compliance with the applicable legal and regulatory frameworks (GDPR, D.Lgs. 196/2003, NIS2, AGID guidelines, and regional healthcare rules), and aligns with internationally recognised best practices (ISO/IEC 27001:2022; NIST CSF 2.0; AGID “Misure minime”)   .

---

## 2. SCOPE

This policy applies to:
- All personnel (clinical, administrative, technical, temporary staff, contractors, and interns)
- All digital systems, devices, and data assets managed or processed by the hospital, including on-premises, managed, and cloud environments
- All third-party providers and MSPs with information system or data access
- All clinical and administrative units (internal medicine, general surgery, paediatrics, long term care, emergency/first aid)
- All information types, especially special category health data, personal data relating to minors, and staff personal data
- All physical locations under hospital control and all remote access points

---

## 3. ROLES AND RESPONSIBILITIES

### 3.1 Hospital Executive Leadership (Director, Chief Administrative Officer)
- Final accountability for cybersecurity posture and policy enforcement
- Approval of policy and major updates
- Oversight of risk management and regulatory compliance
- Designation of an IT-responsible function (delegated manager)

### 3.2 IT Function / MSP (Internal IT staff, Managed Services Provider)
- Implementation and operational management of technical and procedural controls
- Maintenance of user account management, network, endpoint, and server security
- Safe and compliant backup management and recovery testing
- Escalation and communication of incidents to executive leadership

### 3.3 Information Asset Owners (Head of Clinical, Head of Administration, Head of Technical Services)
- Classification and stewardship of patient, administrative, and operational data
- Initiating access requests, periodic access reviews
- Ensuring correct disposal of physical and electronic records

### 3.4 All Users (Clinical, Administrative, Technical Staff, Contractors)
- Compliance with this and other specific security policies and procedures
- Prompt reporting of suspected information security incidents
- Participation in mandatory cybersecurity awareness training

### 3.5 DPO (Data Protection Officer, as nominated by the ASL)
- Oversight on personal data protection and GDPR compliance
- Consulting on privacy impact assessments for new or changed processing
- Liaison with regulatory authorities and data subjects

---

## 4. POLICY PRINCIPLES

### 4.1 Patient Safety First
Cybersecurity controls must not impede urgent clinical workflows. Any measures must be designed to minimize impact on patient care (NIS2 Art. 21; AGID guidelines).

### 4.2 Defense in Depth
Security must be layered—network, endpoint, and application controls implemented together—to prevent single-point failure (ISO/IEC 27001:2022 A.5.7, A.8.1; NIST CSF PR.AC, PR.PT).

### 4.3 Least Privilege & Need to Know
Users and systems shall only have the minimum access required for assigned duties and only for as long as necessary (GDPR Art. 5(1)(c)-(f); ISO/IEC 27001:2022 A.5.18).

### 4.4 Accountability and Traceability
Actions affecting patient or operational data must be attributable and auditable, with monitoring proportional to data sensitivity and resource limits (GDPR Recital 39, NIS2 Art. 21(2)(f)).

### 4.5 Regulatory Compliance by Design
Security and privacy controls must reflect mandatory requirements under European, national, and regional law, as well as guidelines from AGID and the Garante Privacy (GDPR Art. 24-32, D.Lgs. 196/2003, NIS2, AGID “Misure minime”).

---

## 5. POLICY REQUIREMENTS

### 5.1 Governance and Risk Management

**Control:**  
- A risk-based approach to cybersecurity must be maintained, with annual risk assessments reflecting changes in threat landscape (top threats: ransomware, data leak, supply chain compromise, phishing, device theft)   .

**Process:**  
1. Annual risk assessment (internal or with MSP), documented for audit.
2. Update controls and priorities based on risk results and incident learnings.
3. Integrate results into management review.

**Reference:** ISO 27001:2022 A.5.4, A.5.30; NIS2 Art. 21; AGID.

---

### 5.2 Identity and Access Management

**Control:**  
- User accounts and privileges must be managed centrally via Active Directory (on-prem), with regional SPID/CIE federation for external access.  
- Accounts must be uniquely assigned, promptly deactivated on staff departure, and reviewed at least quarterly by asset owners and IT.  
- Privileged accounts must be strictly limited, logged, and monitored.

**Process:**  
1. Onboarding: ID assigned, initial password changed on first use.
2. Offboarding: Deactivation within 24 hours of role end.
3. Quarterly access review by asset/data owners.

**Reference:** ISO 27001:2022 A.5.18–A.5.20; GDPR Art. 25, 32; AGID “Misure minime” 2.1.

---

### 5.3 Asset Management

**Control:**  
- All workstations, mobile devices, and networked medical devices must be inventoried and assigned an owner.  
- Legacy systems (e.g., kiosks) to be monitored, with compensating controls (network segmentation, usage restriction) if vendor updates are unavailable.
- Unused/obsolete assets must be securely decommissioned.

**Process:**  
1. Maintain asset inventory (updated at least quarterly).
2. Document risk for legacy or unsupported devices.

**Reference:** ISO 27001:2022 A.5.9–A.5.11; NIS2 Art 21(2)(d); AGID.

---

### 5.4 Data Protection and Privacy

**Control:**  
- Special category health and personal data must be processed only for authorised purposes.  
- Encryption at rest and in transit is required where technically feasible (esp. for backups, patient records, portable devices).  
- Regular privacy impact assessments (PIAs/DPIAs) must be conducted for new services or changes.

**Process:**  
1. Classify data at time of collection/system integration.
2. Encrypt data on mobile devices; use password/PIN for access.
3. Monthly checks on backup encryption; annual PIA review.

**Reference:** GDPR Art. 5, 32–34; ISO 27001:2022 A.8.10, A.5.25; AGID; Garante Provvedimenti in sanità.

---

### 5.5 Physical Security

**Control:**  
- Access to IT/server rooms, clinical IT kiosks, and backup storage must be physically controlled; mobile devices locked/stored when not in use.

**Process:**  
1. Visitors signed in and escorted.
2. Report lost/stolen devices immediately.

**Reference:** ISO 27001:2022 A.7.4; AGID; NIS2 Art. 21(2)(i).

---

### 5.6 Network and System Security

**Control:**  
- Segmentation must separate clinical, administrative, and PACS traffic; restrict external remote access to VPN with multi-factor authentication if feasible.  
- Antivirus software must be centrally managed and regularly updated; initial alerting via vendor console.

**Process:**  
1. Quarterly review of firewall and segmentation rules.
2. Monthly antivirus updates, alerts reviewed by IT/MSP.

**Reference:** ISO 27001:2022 A.8.5–8.6, A.5.17; AGID “Misure minime” 2.3, 2.6; NIST CSF PR.PT-1.

---

### 5.7 Backup, Recovery, and Business Continuity

**Control:**  
- Daily on-site backup to NAS; weekly off-site tape backup, encrypted.  
- Recovery times must meet clinical continuity targets: EHR (4h), ADT/emergency (1h).  
- Annual disaster recovery (DR) test required, with lessons learned integrated.

**Process:**  
1. Test restore quarterly for critical systems.
2. Annual full DR test, report to management.
3. Document and remediate test failures.

**Reference:** ISO 27001:2022 A.5.30, A.8.11, A.8.13; NIS2 Art. 21(2)(k); AGID.

---

### 5.8 Supplier and Third-Party Security

**Control:**  
- All service, MSP, and medical device vendors must contractually commit to meet security and privacy requirements (incl. GDPR, NIS2).  
- Third-party system access must be time-bound, logged, and reviewed.

**Process:**  
1. Vendor due diligence in procurement.
2. Annual review of vendor compliance.
3. Immediate deactivation of vendor access post-engagement.

**Reference:** ISO 27001:2022 A.5.19, A.5.22, A.5.21; NIS2 Art. 21(2)(j); AGID.

---

### 5.9 Incident Detection and Response

**Control:**  
- Suspected or confirmed cyber incidents must be reported without delay following documented escalation to the IT function or MSP.
- Major incidents (e.g., ransomware, significant data leak) are escalated to management, ASL, DPO, and, if required, to the Garante Privacy.

**Process:**  
1. Staff report incidents via phone/email or ticketing.
2. IT/MSP logs incidents, performs triage, escalates as needed.
3. Lessons learned incorporated into process/procedure updates.

**Reference:** ISO 27001:2022 A.5.24, A.5.6; GDPR Art. 33–34; NIS2 Art. 23; AGID.

---

### 5.10 Security Awareness and Training

**Control:**  
- All staff must complete at least 2 hours of mandatory cybersecurity training per year (including phishing, data handling, incident reporting).  
- Training content tailored to clinical, administrative, and IT roles.
- Records of participation maintained by HR.

**Process:**  
1. Schedule staff for annual training.
2. Record attendance, conduct ad-hoc refreshers after incidents.

**Reference:** ISO 27001:2022 A.6.3; NIS2 Art. 20; AGID.

---

## 6. MONITORING AND REVIEW

### 6.1 Monitoring

**What to monitor:**
- Logins, privileged actions, and access to special category data  
- Antivirus alerts, backup completion, and network anomalies

**Frequency:**  
- Log review: Monthly, or immediately post-incident  
- Backups and AV: Weekly (automated alerting where feasible)

**Responsible:** IT Function / MSP

**Retention:**  
- Logs and alerts retained for at least 12 months or as required by law

### 6.2 Regular Reviews

- Annual policy review and update, or sooner after material incident/regulatory change
- Quarterly review of access, asset inventory, and incident records
- Annual external or MSP audit against policy requirements

**Deliverable:**  
Policy review report to management/ASL; remedial action plan

---

## 7. TRAINING AND AWARENESS

### 7.1 Mandatory Training

**All staff must complete:**
- Cybersecurity awareness (annually, 2h minimum)
- Phishing and social engineering simulation (annually)

**Training topics:**
- Recognition/reporting of threats (phishing, suspicious behaviour)
- Data protection and GDPR duties
- Secure use of hospital devices and data

### 7.2 Acknowledgment

- Staff sign training completion logs each year
- Participation records stored by HR and available on audit

---

## 8. INCIDENT RESPONSE

### 8.1 Reporting

**All users must immediately report:**
- Suspected malware or ransomware events
- Loss/theft of devices containing patient/administrative data
- Suspected data breach (including health data or minors)

**Reporting channels:**
- Primary: IT helpdesk (phone/email/ticket)
- Escalation: Executive, DPO, regional health info-security contacts

### 8.2 Response Actions

1. IT/MSP verifies, contains, and analyses events
2. Escalation to management, regulators, or law enforcement as required
3. Documentation of investigation, actions, and communications
4. Recovery and lessons learned phase post-incident

---

## 9. COMPLIANCE AND AUDIT

### 9.1 Regulatory Compliance

This policy supports compliance with:
- **GDPR (EU Regulation 2016/679):** Art. 24–32, 33–34
- **D.Lgs. 196/2003 (Codice Privacy, as amended):** Ch. II–IV, VII
- **NIS2 Directive (2022/2555):** Art. 20–23 (essential entities)
- **AGID Linee Guida e Misure Minime:** Technical/organisation controls in PA
- **ISO/IEC 27001:2022:** Controls cited above
- **NIST CSF 2.0:** Identify, Protect, Detect, Respond, Recover

### 9.2 Policy Review

- Policy reviewed annually or with major regulatory/incident trigger
- Updates approved by Executive Leadership

### 9.3 Audit Rights

- Internal IT/MSP: Quarterly checks on compliance points
- ASL or external: Audit per regulatory/contractual schedule
- Audit remediation within 60 days

---

## 10. ENFORCEMENT

### 10.1 Policy Violations

Violations may result in:
- Written warning
- Temporary suspension of access
- Disciplinary action under employment or contract terms, up to dismissal or contract termination
- Regulatory notification and possible fines for legal breaches

**Examples:**
- Minor: Failure to complete training, accidental access to unauthorised data
- Moderate: Negligent handling of devices, failure to report incidents
- Severe: Intentional data disclosure, sabotage, failure to follow incident response

### 10.2 Documentation

- All violations and corrective actions are logged and retained by HR/IT

---

## 11. EXCEPTIONS

### 11.1 Exception Process

- Requests submitted in writing to Executive Leadership via IT function
- Approval by Hospital Director (or delegate), with DPO involvement for data/privacy exceptions
- Compensating controls documented
- Maximum validity: 12 months, with annual review

### 11.2 Emergency Access

- “Break-glass” accounts enabled only for time-limited, patient safety events, with access logged and reviewed after use

---

## APPENDICES

### Appendix A: Definitions

**AGID:** Agency for Digital Italy, responsible for public sector IT standards.  
**ASL:** Local Health Agency (Azienda Sanitaria Locale), regional public health body.  
**DPO:** Data Protection Officer, designated under GDPR.  
**EHR:** Electronic Health Record.  
**PIA/DPIA:** (Data) Privacy Impact Assessment.  
**NIS2:** EU Network and Information Security Directive (essential sector).  
**MSP:** Managed Service Provider.

### Appendix B: Forms and Templates

- Access request and removal form  
- Incident reporting template  
- Employee training acknowledgment form

### Appendix C: Contact Information

- IT Helpdesk: [Contact details]  
- Executive office: [Contact details]  
- DPO: [Contact details]  
- MSP escalation: [Contact details]  

### Appendix D: Technical Controls (if applicable)

- Default endpoint AV settings  
- Backup encryption configuration  
- UTM firewall sample rules (segmentation between clinical/admin/PACS VLAN)

---

## DOCUMENT CONTROL

### Version History Table
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Insert date] | Chief Admin Officer | Initial issue |

---

### Approval Block

**Policy Approved By:**
  
[Executive Role]: _______________ Date: _______________

[IT/Technical Delegate]: _______________ Date: _______________

[Compliance/DPO]: _______________ Date: _______________

---

## REFERENCES AND SOURCES

This policy was developed based on the following frameworks/regulations/standards:

**GDPR (Regulation EU 2016/679):**  
- Articles 5, 24–34 (principles, security, breach notification)

**D.Lgs. 196/2003 as amended by D.Lgs. 101/2018 (“Codice Privacy”):**  
- Technical and organizational security measures

**NIS2 Directive (Directive EU 2022/2555):**  
- Articles 20–23 (cybersecurity of essential health sector entities)

**AGID “Misure minime” and “Linee guida sulla sicurezza informatica”:**  
- Public sector IT minimum security controls 

**ISO/IEC 27001:2022:**  
- Controls cited by identifier (A.5.x, A.8.x, etc.) 

**NIST Cybersecurity Framework 2.0:**  
- Identify, Protect, Detect, Respond, Recover functions 

**Official rulings and guidelines from the Garante Privacy**  
- Regarding health data, data breaches, and security in healthcare

**Regional/Local Regulations:**  
- FSE (Fascicolo Sanitario Elettronico) and other regional mandates

*Where no precise standard is listed, controls reflect practical adaptations of widely recommended sectoral best practices and the hospital’s own operational constraints.*

</policy>
