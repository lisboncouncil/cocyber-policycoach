---
config: C1
context_id: ctx-H
policy_id: P4
policy_name: Incident Response Policy
policy_short: ir
metadata:
  config: C1
  model: gpt-4.1
  input_tokens: 6392
  output_tokens: 3609
  total_tokens: 10001
  latency_s: 41.548
  tool_calls: []
  raw_provider_id: run_4eDU9pHGz1PjGP1EyqhIQgLj
  run_status: completed
  thread_id: thread_stVk0kdYIyA65i0eqfsHEoos
sources_count: 0
sources: []
prompt_chars: 4675
answer_chars: 15820
generated_at_unix: 1778087083
---

<policy title="Incident Response Policy">

---

## POLICY HEADER BLOCK

**Organization:** [Unnamed Small Public Hospital], Azienda Sanitaria Locale (ASL), Italy  
**Effective Date:** [Insert: 2024-06-11]  
**Policy Owner:** Director, IT & Digital Health / Interim Security Officer  
**Review Cycle:** Annual, or after any significant incident or change in regulatory environment

---

## 1. PURPOSE

This Incident Response Policy establishes the framework for detecting, reporting, managing, and recovering from cybersecurity incidents affecting the hospital’s information systems, data, and digital assets. The policy is designed to support patient safety, service continuity, and regulatory compliance—including GDPR (Reg. EU 2016/679), NIS2 (Directive EU 2022/2555), AGID security measures for public administration, and other applicable regulations—while being proportionate to the hospital’s size, threat profile, and operational constraints.  
*Citations: ISO/IEC 27001:2022 §A.5.24, NIST CSF ID.RA, AGID "Linee Guida", NIS2 Art. 21.*

---

## 2. SCOPE

This policy applies to:
- All staff (clinical, administrative, technical/facility), volunteers, interns
- Hospital IT systems (EHR/FSE, PACS, LIS, ADT, Pharmacy, workstations, mobile devices)
- Third parties (managed service providers, clinical software vendors)
- Data categories (health and personal data, including minors and employees)
- Physical premises and all digital infrastructure
- All incidents (suspected or confirmed) impacting confidentiality, integrity, availability or legal compliance  
*Citations: ISO/IEC 27001:2022 §A.5.24, NIS2 Art. 21, GDPR Art. 33.*

---

## 3. ROLES AND RESPONSIBILITIES

### 3.1 Executive Management / Hospital Director
- Accountable for overall incident response governance and resource allocation
- Approves policy and major incident escalations
- Ensures timely regulatory reporting (e.g., Garante Privacy, CSIRT Italia)

### 3.2 IT Coordinator / Interim Security Officer
- Maintains the incident response process and policy
- Leads or coordinates incident investigation and communication with external MSP
- Ensures alignment with regional ASL and Servizio Sanitario Nazionale guidance
- Documents incidents and follow-up actions

### 3.3 External Managed Service Provider (MSP)
- Implements technical containment, eradication, and recovery actions as authorized
- Provides Tier 2/3 technical investigation and forensics (per contract)
- Notifies IT Coordinator of incidents and actions taken

### 3.4 Department Heads (Clinical & Administrative)
- Facilitates staff cooperation in incident response
- Ensures unit-level incident detection (e.g., reporting of compromised accounts or device theft)
- Supports business continuity actions

### 3.5 All Staff and Users
- Promptly report suspected or real security incidents or data breaches
- Comply with containment and follow-up instructions
- Participate in relevant incident awareness training

*Citations: ISO/IEC 27001:2022 §A.5.24, AGID Linee Guida, NIS2 Art. 21.*

---

## 4. POLICY PRINCIPLES

### 4.1 Patient Safety First
Incident response shall minimize disruption to clinical care, emergency workflows, and patient safety at all times.

### 4.2 Timely Detection and Response
All incidents must be detected and addressed rapidly to minimize impact, with clear procedures for escalation, communication, and recovery.

### 4.3 Compliance With Regulations and Reporting
Regulatory notification obligations (e.g., Garante Privacy, CSIRT Italia, AGID) must be met within statutory deadlines.

### 4.4 Least Privilege and Containment
Only necessary systems/accounts shall be affected by control actions; containment methods should avoid collateral impact.

### 4.5 Documentation and Continuous Improvement
All incidents—including near misses—are to be documented and reviewed to strengthen future response capabilities.

*Citations: ISO/IEC 27001:2022 §A.5.24, NIST CSF RS, NIS2 Art. 23, GDPR Art. 33.*

---

## 5. POLICY REQUIREMENTS

### 5.1 Incident Identification and Reporting

**Requirements:**
- All users must report suspected or confirmed incidents immediately via designated channels (telephone/email to IT Coordinator; after hours via on-call MSP contact or escalation tree).
- Incident types include, but are not limited to: ransomware/infection, data leakage/exfiltration, account compromise, unauthorized physical access, system unavailability (including EHR and ADT), theft/loss of devices .

**Process:**
1. User detects or suspects an incident → contacts IT Coordinator or (after hours) MSP hotline.
2. IT logs incident in incident response register/log (with time, nature, and initial assessment).

**Timeline:** Within 15 minutes of detection, 1 hour for MSP/high-severity escalation.

**Controls:**
- Awareness materials centrally circulated quarterly.
- Internal incident log maintained and regularly reviewed.

*Citations: ISO/IEC 27001:2022 §A.5.24, A.5.25, AGID Linee Guida §Incident Handling.*

---

### 5.2 Incident Classification and Severity Assessment

**Requirements:**
- Incidents are scored for criticality (Critical, High, Medium, Low), considering impact to patient care, clinical workflows, data confidentiality, and legal obligations.

**Process:**
1. IT Coordinator assigns initial severity based on guidance/procedure.
2. Critical/high incidents escalate to Executive Management and, if data breach, DPO/Garante Privacy.

**Timeline:** Severity classification within 30 minutes of initial report.

**Controls:**
- Predefined severity matrix linked to business continuity priorities (e.g., EHR/ADT loss = Critical).

*Citations: ISO/IEC 27001:2022 §A.5.24, NIST CSF RS.AN.*

---

### 5.3 Incident Containment and Mitigation

**Requirements:**
- Containment actions (e.g., isolating infected device, disabling compromised accounts) must be rapid but must not endanger patient safety or emergency clinical operations.
- MSP executes advanced technical containment (perimeter blocking, forensic image for ransomware).

**Process:**
1. IT Coordinator authorizes basic containment; escalates to MSP for advanced technical response.
2. End users cooperate, following instructions for isolating endpoints.

**Timeline:** Initial containment within 1 hour for Critical incidents.

**Controls:**
- Playbooks for top threats (e.g., ransomware, device theft) maintained and circulated.
- Regular tabletop exercises conducted for IT and clinical leads.

*Citations: ISO/IEC 27001:2022 §A.5.24, A.5.25, NIS2 Art. 23.*

---

### 5.4 Notification and Regulatory Reporting

**Requirements:**
- Data breaches reportable under GDPR or sector regulations must be notified to Garante Privacy within 72 hours; NIS2 incidents to CSIRT Italia per Art. 23 timelines.
- Notifications to patients/data subjects are coordinated with ASL DPO as required.

**Process:**
1. IT Coordinator and Executive Management confirm need for regulatory notification.
2. Draft and send report per statutory template, with external legal assistance if needed.

**Timeline:** GDPR: 72h max; NIS2/CSIRT Italia: as per Art. 23 table (4h for alerts, 24h for notification).

**Controls:**
- Pre-drafted notification templates maintained.
- Incident register tracks notifications made and deadlines.

*Citations: GDPR Art. 33, NIS2 Art. 23, AGID Linee Guida, Provvedimenti Garante Privacy in sanità.*

---

### 5.5 System Recovery and Restoration

**Requirements:**
- Restoration of clinical-critical systems (EHR, ADT/PS) within RTO targets: 1h (ADT/PS), 4h (EHR) where feasible.
- Recovery steps prioritize safety and data integrity; systems verified clean before reintroduction.

**Process:**
1. MSP restores affected systems from backups, following chain-of-custody/logging.
2. Business units verify that restored services support safe clinical operation.

**Timeline:** RTO targets per BIA—must be reviewed after each incident.

**Controls:**
- Backup restoration procedures tested at least annually.
- Chain-of-custody forms for forensic images.

*Citations: ISO/IEC 27001:2022 §A.5.30, NIST CSF RS.RP, BCP/DRP sector best practice.*

---

### 5.6 Post-Incident Review and Lessons Learned

**Requirements:**
- Every incident rated Medium or higher must have a documented review within 10 working days.
- Action items tracked and reported to Executive Management.

**Process:**
1. Convene response review involving IT, MSP, management, affected business units.
2. Update procedures, training, and controls as relevant.

**Timeline:** Post-incident review within 10 business days.

**Controls:**
- Corrective/preventive action tracker.
- Policy revision if systemic gaps are identified.

*Citations: ISO/IEC 27001:2022 §A.5.24, NIST CSF RC.IM, AGID Linee Guida.*

---

## 6. MONITORING AND REVIEW

### 6.1 Monitoring

**What to monitor:**
- Incident log, detection feeds (AV console), MSP incident tickets, backup/recovery logs

**Frequency:** Continuous monitoring by MSP for technical alerts; monthly by IT for log completeness

**Responsible:** IT Coordinator with MSP

**Retention:** Incident logs retained for 5 years (or per legal minimums)

### 6.2 Regular Reviews

- Quarterly review of incident logs and lessons learned reports
- Annual full review of policy, process effectiveness, and RTO compliance
- Immediate review after any major incident

**Deliverable:** Incident response review report, documented improvement actions

*Citations: ISO/IEC 27001:2022 §A.5.32, A.5.25, AGID Linee Guida.*

---

## 7. TRAINING AND AWARENESS

### 7.1 Mandatory Training

All staff must complete:
- Initial cybersecurity incident awareness training during onboarding (first 30 days)
- Annual refresher training (2 hours/year)

**Training topics:**
- Recognizing common attack types (phishing, ransomware)
- Prompt incident reporting
- Safe use and loss/reporting of mobile devices

### 7.2 Acknowledgment

- Staff must confirm training completion via HR attendance record
- Training and policy access via internal portal

*Citations: ISO/IEC 27001:2022 §A.6.3, NIST CSF PR.AT, AGID mandatory awareness guidance.*

---

## 8. INCIDENT RESPONSE

### 8.1 Reporting

Staff must immediately report:
- Suspicious emails or system behavior
- Loss/theft of any hospital or personal device containing hospital data
- Suspected unauthorized access or data breach

**Reporting channels:**
- IT Coordinator (business hours): [Insert contact]
- MSP on-call (after hours): [Insert contact]
- Escalation: Hospital Director for Critical incidents

### 8.2 Response Actions

Upon incident report:
1. Logging incident and performing initial triage (within 15 min)
2. Informing MSP and/or relevant management/DPO as required
3. Executing authorized containment measures
4. Documenting technical and business context, including affected assets and impact
5. Conducting root cause and follow-up analysis
6. Communicating resolution and documenting closure in the register

*Citations: ISO/IEC 27001:2022 §A.5.24, A.5.25, NIS2 Art. 23, AGID Linee Guida.*

---

## 9. COMPLIANCE AND AUDIT

### 9.1 Regulatory Compliance

This policy supports compliance with:
- **GDPR (EU 2016/679):** Art. 33/34 (breach notification)
- **NIS2 (EU 2022/2555):** Art. 21, 23 (incident handling and reporting)
- **AGID Guidelines:** Incident handling, minimum security measures
- **Provvedimenti Garante Privacy in sanità**
- **ISO/IEC 27001:2022:** §A.5.24, A.5.25, A.5.32 (Information Security Incident Management)

### 9.2 Policy Review

- Reviewed annually, and after major changes in regulatory requirements or following serious incidents.
- Owner: IT Coordinator with Executive Management sign-off.
- Revised policy to be communicated to all staff within 30 days of changes.

### 9.3 Audit Rights

- Subject to internal audit (annual) by hospital management or parent ASL
- Ad-hoc external audit as part of regional or government oversight

*Citations: As above.*

---

## 10. ENFORCEMENT

### 10.1 Policy Violations

Violations may result in:
- Reminder/training requirement (first minor lapse)
- Formal written warning (repeated failures)
- Disciplinary action (serious or intentional violation)
- Referral to law enforcement for criminal violations

**Examples:**
- Minor: Delay in reporting incident
- Moderate: Unauthorized communication of incident details
- Severe: Knowingly suppressing an incident, illegal data disclosure

### 10.2 Documentation

- All violations and responses tracked in HR/IT incident register

*Citations: ISO/IEC 27001:2022 §A.5.24, AGID Linee Guida.*

---

## 11. EXCEPTIONS

### 11.1 Exception Process

- Staff may request written exceptions to incident response protocols (e.g., during clinical emergency) via department head to IT Coordinator
- Approval required from Executive Management
- Compensating controls must be documented
- Maximum validity: 30 days unless renewed/justified
- All exceptions logged and reviewed quarterly

### 11.2 Emergency Access

- In emergency (patient/life-safety), clinical operations may override IT containment with immediate post-event documentation.
- All such actions retrospectively reviewed within 2 business days.

*Citations: ISO/IEC 27001:2022 §A.5.24, NIS2 Art. 23, AGID Linee Guida.*

---

## APPENDICES

### Appendix A: Definitions

**Incident:** Any event with potential adverse effect on confidentiality, integrity, or availability of hospital’s information assets or compliance.  
**Critical system:** EHR/FSE, ADT/PS, PACS/RIS, LIS, pharmacy management.  
**Data Breach:** Unauthorized access, disclosure, loss, or destruction of personal data.  
**MSP:** Managed Service Provider with contractual responsibility for IT operations and response.  
**RTO:** Recovery Time Objective. Maximum allowed downtime.

### Appendix B: Forms and Templates

- Incident reporting form (staff use)
- Forensic evidence chain-of-custody
- Regulatory notification template (Garante, CSIRT Italia)
- Incident log template

### Appendix C: Contact Information

- IT Coordinator: [Insert name/email/phone]
- MSP 24/7 incident hotline: [Insert contact]
- Executive escalation: [Insert contact]
- Regional ASL/DPO: [Insert contact]

### Appendix D: Technical Controls

- AV console alert triggers
- Endpoint isolation script (preconfigured by MSP)
- Backup/restore procedure documentation

---

## DOCUMENT CONTROL

### Version History Table

| Version | Date       | Author              | Changes                                   |
|---------|------------|---------------------|-------------------------------------------|
| 1.0     | 2024-06-11 | IT Coordinator      | Initial release                           |

---

### Approval Block

**Policy Approved By:**

Hospital Director: _______________ Date: _______________

IT Coordinator / Interim Security: _______________ Date: _______________

Regional ASL DPO: _______________ Date: _______________

---

## REFERENCES AND SOURCES

This policy was developed based on the following frameworks, sector guidance, and regulations:

- **ISO/IEC 27001:2022:** A.5.24 (Information Security Incident Management), A.5.25 (Response to Information Security Incidents), A.5.32 (Monitoring, Review, and Evaluation)
- **NIST Cybersecurity Framework 2.0:** Respond (RS) and Recover (RC)
- **GDPR (EU 2016/679):** Arts. 33–34 (Data breach notification)
- **NIS2 (Directive EU 2022/2555):** Arts. 21, 23 (Essential Entities—Incident Handling and Reporting)
- **AGID Linee Guida per la sicurezza informatica nella PA** (2022): Requirements for PA incident management and reporting
- **Provvedimenti Garante Privacy in sanità**: Sector-specific breach notification
- **Regional regulations on FSE operations**
- [Sector cyber threat intelligence and Italian health sector incident statistics]

*Unsupported statements are operational best practices informed by sector context and limitations.*

---

</policy>
