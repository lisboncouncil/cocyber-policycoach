---
config: C1
context_id: ctx-M
policy_id: P2
policy_name: Data Protection Policy
policy_short: dataprot
metadata:
  config: C1
  model: gpt-4.1
  input_tokens: 6612
  output_tokens: 3749
  total_tokens: 10361
  latency_s: 45.678
  tool_calls: []
  raw_provider_id: run_D3bt0F8xvILbmo88CpNZp9Wn
  run_status: completed
  thread_id: thread_EeQw0awG40DdChhMnnBdDjRr
sources_count: 0
sources: []
prompt_chars: 6041
answer_chars: 15551
generated_at_unix: 1778086400
---

<policy title="Data Protection Policy for NATO Multinational Military Detachment (Romania)">

---
## POLICY HEADER BLOCK

**Organization:** NATO Multinational Military Detachment, Romania (medium, rotational framework, under SHAPE OPCON)  
**Effective Date:** [Insert Date]  
**Policy Owner:** Information Systems Security Manager (ISSM, J6)  
**Review Cycle:** Annual or following significant operational, regulatory, or technical changes

---

## 1. PURPOSE

This Data Protection Policy establishes the principles and controls for safeguarding all data, including NATO-classified, operational, technical, and personal information, processed, stored, or transmitted by the detachment. The policy ensures data is protected against accidental or unauthorized access, disclosure, alteration, loss, or destruction in compliance with NATO security policy (C-M(2002)49, successors), host-nation and coalition laws, the Romanian Cybersecurity Law (Law 58/2019, NIS/NIS2), GDPR, and international standards (ISO/IEC 27001:2022, NIST CSF 2.0).

---

## 2. SCOPE

This policy applies to:
- All military, civilian, and contractor personnel assigned to or supporting the detachment
- All NATO, coalition, and host-nation CIS systems and devices (including cross-domain solutions and COMSEC equipment) at the deployment
- All data classifications: NATO UNCLASSIFIED, NATO RESTRICTED, NATO SECRET, MISSION SECRET, and personal data of EU-based civilian staff/contractors
- All operational locations (including cross-domain, SCIF zones, and off-site operations)
- All third-party service providers, vendors, and supply-chain partners subject to NATO or host-nation vetting

---

## 3. ROLES AND RESPONSIBILITIES

### 3.1 Executive Command (OPCON/Detachment Commander)
- Accountable for detachment-wide data protection and resourcing
- Approves policy exceptions and significant data handling deviations
- Receives and acts upon serious data breach reports

### 3.2 Information Systems Security Manager (ISSM, J6)
- Maintains and enforces data protection policy and technical controls
- Coordinates with host-nation and NATO authorities (NCIRC, NCSC, CERT)
- Supervises data protection training and incident response
- Maintains data asset registry and risk assessments

### 3.3 Security Operations Centre (SOC) Staff & Security FTE
- Monitor, detect, and respond to data incidents 24/7
- Conduct data breach investigations and reporting in line with NCIRC and host-nation channels
- Advise on technical and procedural controls (e.g., cross-domain, TEMPEST)

### 3.4 System/Network Administrators
- Implement and maintain technical data protection measures for each classification domain
- Enforce least privilege and need-to-know on CIS systems

### 3.5 All Personnel (Military, Civilian, Contractor)
- Adhere to this policy and data handling rules for all classifications
- Immediately report data spills, lost devices, and suspected breaches
- Complete mandated data protection and classification training annually

---

## 4. POLICY PRINCIPLES

### 4.1 Principle of Classification and Segregation
All data shall be classified and segregated according to NATO and host-nation frameworks. Segregation is enforced at every level: physical, logical, and personnel access (ISO/IEC 27001: A.8.2.1–A.8.2.3; C-M(2002)49).

### 4.2 Principle of Need-to-Know/Default Deny
Data access is restricted by default and based strictly on mission role and current clearance; “default deny” applies unless explicitly authorized (NIST CSF PR.AC-4; ORCON; NATO C-M(2002)49).

### 4.3 Principle of Data Minimization & Retention
Only the minimum necessary data required for mission/operation is processed. Retention periods comply with NATO, host-nation, and GDPR (if applicable), and unnecessary data is securely destroyed (GDPR Art.5(1)(c,e); ISO/IEC 27001:2022 A.7.4).

### 4.4 Principle of Accountability & Auditability
All accesses, transfers, and handling of data, particularly classified and personal, must be logged and auditable (NATO INFOSEC AC/322-D(2017)0009; ISO/IEC 27001:2022 A.8.9).

---

## 5. POLICY REQUIREMENTS

### 5.1 Data Classification & Handling

**Control:** All data shall be classified as NU, NR, NS, MISSION SECRET, or NATO CTS, and marked accordingly at creation.  
**Process:**  
1. Information originators classify per C-M(2002)49 and mark accordingly.  
2. All users check markings before transmission or sharing.  
3. No downgrade or cross-domain transfer without ISSM and CDS approval.

**Timeline:** At data creation or import  
**Reference:** NATO C-M(2002)49, AC/35-D/1015, ISO/IEC 27001: A.8.2

---

### 5.2 Access Control & Identity Management

**Control:** Access is strictly enforced through smart-card PKI authentication per domain, with no cross-domain federation.  
**Process:**  
1. Accounts provisioned by admin on request, based on clearance/role.  
2. Periodic access review by ISSM and domain owner (quarterly).  
3. Immediate revocation on departure or loss of clearance.

**Timeline:** Ongoing, with quarterly review  
**Reference:** ISO/IEC 27001:2022 A.5.18, NIST CSF PR.AC-1-4; NATO INFOSEC AC/322-D(2017)0009

---

### 5.3 Data Encryption & Network Protection

**Control:**  
- Data at rest and in transit in NR and above domains is protected using NATO-approved encryption.  
- COMSEC equipment used exclusively for SECRET and above, with key material managed per national and NATO COMSEC policy.

**Process:**  
1. Enforce device and media encryption for mobile storage and laptops.  
2. Strict perimeter security, with TEMPEST compliance for NS and above.  
3. Cross-domain transfers use NATO CDS, approved and logged.

**Timeline:** Continuous  
**Reference:** ISO/IEC 27001:2022 A.8.24, A.8.25; NATO C-M(2002)49; Host-nation Law 58/2019

---

### 5.4 Data Retention & Disposal

**Control:**  
- Retain mission, operational, and personnel data only as long as required for mission or legal purposes.
- Secure disposal/destruction (per classification) of IT media, with audit trail.

**Process:**  
1. ISSM maintains retention schedules meeting NATO, host-nation, and GDPR (for covered personal data) obligations.  
2. Destruction by approved methodology—degaussing, shredding for SECRET+.  
3. Log destruction and verify dual-person integrity for SECRET+.

**Timeline:** Annual review or upon system decommission  
**Reference:** ISO/IEC 27001:2022 A.8.10, A.7.4; NATO C-M(2002)49; GDPR Art. 5(1)(e)

---

### 5.5 Data Transfer & Cross-Domain Controls

**Control:**   
- No data shall cross classification boundaries except through accredited NATO Cross-Domain Solutions (CDS), per CDS approval and monitoring regimes.
- All data transfers logged and subject to two-person integrity for SECRET/CTS.

**Process:**  
1. All transfers approved and overseen by designated CDS Officer and ISSM.  
2. Cross-domain logs maintained for 12 months minimum.  
3. Review quarterly for irregularities.

**Timeline:** As needed  
**Reference:** NATO INFOSEC AC/322-D(2017)0009; ISO/IEC 27001: A.8.14

---

### 5.6 Personal Data & GDPR/Host-Nation Compliance

**Control:**  
- All EU-personal data processed in line with GDPR (Art. 5–32).
- Lawful basis for processing (Art. 6), with explicit records (Art. 30).
- Data subject rights honoured except where mission or NATO SOFA restricts.

**Process:**  
1. Civilian/contractor data reviewed with DPO/ISSM.  
2. Data privacy notices provided and records maintained.  
3. Breach notification per GDPR Art. 33/34 and NATO/NCIRC guidance.

**Timeline:** Ongoing  
**Reference:** GDPR; Romanian Law 58/2019; ISO/IEC 27001:2022 A.8.1

---

### 5.7 Supply Chain & Vendor Controls

**Control:**  
- Only NATO-approved, host-nation-cleared vendors and supply channels used for all CIS and COMSEC equipment.

**Process:**  
1. Vendor vetting aligned with NATO Security and host-nation standards.  
2. Contracts include explicit data protection and incident notification clauses.  
3. Annual re-certification review.

**Timeline:** Annually or upon contract initiation/change  
**Reference:** ISO/IEC 27001:2022 A.5.19, A.8.28; NATO AC/322-D(2017)0009

---

### 5.8 Incident Detection & Response

**Control:**  
- 24/7 SOC monitoring for data leaks, spills, and unauthorized access.
- Incidents reported in accordance with NATO CIRC and national CERT procedures.

**Process:**  
1. Immediate triage of incidents.  
2. Mandatory reporting chain: NCIRC, NCSC Romania, and DPO (for GDPR-impacted incidents).  
3. Lessons learned and corrective action within 30 days post-incident.

**Timeline:** Continuous  
**Reference:** ISO/IEC 27001:2022 A.5.23; NATO INFOSEC AC/322-D(2017)0009; GDPR Art. 33/34

---

## 6. MONITORING AND REVIEW

### 6.1 Monitoring
- Access, data transfers, and classified information handling shall be logged per domain
- Logs shall be reviewed monthly by ISSM and SOC
- Retention of logs: minimum 12 months

### 6.2 Regular Reviews
- Annual data protection audit by ISSM, with results to OPCON and framework nation
- Quarterly review of cross-domain logs and incident records
- Data breach drills and red-team exercises (at least biannually)

**Deliverable:** Annual compliance and effectiveness report

**References:** ISO/IEC 27001:2022 A.5.15, A.5.20

---

## 7. TRAINING AND AWARENESS

### 7.1 Mandatory Training
All personnel (military, civilian, contractor) must complete:
- Data protection and classification handling (annual, 40 hours/year for security staff)
- Secure handling for new system/supply chain introductions

**Training topics:**
- NATO security frameworks and classification
- GDPR basics and personnel data handling (for covered roles)
- Incident/breach identification and reporting

### 7.2 Acknowledgment
- Personnel must sign written acknowledgment of training and policy receipt
- Training records maintained by ISSM/J6

---

## 8. INCIDENT RESPONSE

### 8.1 Reporting
**All personnel must immediately report:**
- Data loss, spillage, or leak (any classification)
- Suspected or known unauthorized access

**Reporting channels:**
- SOC 24/7 hotline
- ISSM/J6 security team
- Upward reporting to NCIRC, NCSC, Framework Nation

### 8.2 Response Actions
1. Immediate containment by SOC/ISSM (within 1 hour)
2. Incident documentation and initial notification (within 4 hours)
3. Full technical and process root-cause analysis
4. Remediation and system hardening before return to service
5. Lessons-learned review (within 30 days); update of playbooks and policies as appropriate

---

## 9. COMPLIANCE AND AUDIT

### 9.1 Regulatory Compliance
This policy supports compliance with:
- **NATO C-M(2002)49 and successors; AC/35-D/1015; AC/322-D(2017)0009**
- **Romanian Cybersecurity Law (Law 58/2019, NIS/NIS2)**
- **GDPR (where applicable, primarily to civilian/contractor data)**
- **ISO/IEC 27001:2022** (referenced clauses A.5–A.8 and others as cited)
- **NIST CSF 2.0** (functions: Identify, Protect, Detect, Respond referenced)

### 9.2 Policy Review
- Annual review by ISSM and command authority
- Triggered update upon: major regulatory change; operational changes; significant incident; change of framework/host nation

### 9.3 Audit Rights
- Internal audits: annually and after major incidents
- External: by OPCON, framework nation, NCIRC, or host-nation regulators as applicable
- Remediation plan within 30 days of audit findings

---

## 10. ENFORCEMENT

### 10.1 Policy Violations

Violations may result in:
- Oral or written warning (minor, e.g. mishandling unclassified)
- Restriction of access, formal disciplinary proceedings (moderate, e.g. improper handling of classified)
- Removal from post, criminal prosecution (severe, e.g. intentional data breach, espionage, unauthorized transfer to higher classification domain)
- Notification to host-nation or framework nation authorities as appropriate

**Examples:**
- Minor: Unintentional data spillage below RESTRICTED, promptly reported
- Severe: Willful bypass of CDS or transfer of SECRET outside channels

### 10.2 Documentation
- All violations documented by ISSM and security staff
- Repeat offenses tracked and escalated

---

## 11. EXCEPTIONS

### 11.1 Exception Process
- Exception requests via ISSM/J6 to Command
- Must state operational need, duration, and compensating controls
- Approval granted only at Commander level or by OPCON authority
- Time-limited (maximum 90 days unless reapproved)
- Quarterly review of issued exceptions

### 11.2 Emergency Access
- Break-glass procedures for life/safety or critical mission continuity only
- Event logged and post-event review required

---

## APPENDICES

### Appendix A: Definitions

- **ISSM:** Information Systems Security Manager; responsible for all INFOSEC matters.
- **CDS:** Cross-Domain Solution, an approved means to transfer data between classification domains.
- **COMSEC:** Communications Security—systems, equipment, and procedures to secure NATO communications.
- **OPCON:** Operational Control; command authority as vested by SHAPE/NATO.
- **NU/NR/NS/CTS:** NATO marking for Unclassified, Restricted, Secret, Cosmic Top Secret.
- **SOC:** Security Operations Centre, organization responsible for 24/7 monitoring/response.
- **NCSC:** National Cyber Security Centre (Romania).
- **NCIRC:** NATO Computer Incident Response Capability.

### Appendix B: Forms and Templates

- Data access request/approval form
- Exception request form
- Breach/incident reporting template
- Data destruction/custody log

### Appendix C: Contact Information

- ISSM/J6 (Detachment): [phone/email]
- SOC 24/7: [phone/email]
- OPCON Command Desk: [phone/email]
- DPO (for personal data): [phone/email, if applicable]

### Appendix D: Technical Controls

- PKI/smartcard provisioning workflow
- CDS configuration guidance
- Encryption algorithm and key management references (link to NATO COMSEC guidance)

---

## DOCUMENT CONTROL

| Version | Date       | Author                    | Changes                |
|---------|------------|--------------------------|------------------------|
| 1.0     | [Insert]   | ISSM/J6                  | Initial release        |

---

**Policy Approved By:**  
[Commander, NATO Multinational Detachment]: _______________ Date: _______________  
[ISSM, J6]: _______________ Date: _______________  
[Framework Nation Security Representative]: _______________ Date: _______________  

---

## REFERENCES AND SOURCES

This policy was developed with reference to the following standards, frameworks, and internal guidance:

- **NATO C-M(2002)49 and successors**: NATO Information Security Policy (policy framework, data governance, authority).
- **NATO AC/35-D/1015 & AC/35-D/1029**: Security within NATO, personnel and physical security requirements.
- **NATO AC/322-D(2017)0009**: INFOSEC technical controls and implementation directives.
- **NATO Cyber Defence Pledge (2016)**: High-level guidance on allied cyber posture.
- **Allied Joint Doctrine for Cyberspace Ops (AJP-3.20)**: Operational integration, data in mission context.
- **Romanian Cybersecurity Law (Law 58/2019)**: Host-nation requirements, NIS/NIS2 transposition.
- **GDPR (Regulation (EU) 2016/679)**: Only for EU/EEA civilian and contractor personal data.
- **NIST CSF 2.0**: Best practice reference for identify, protect, detect, respond, recover (technical requirement mapping).
- **ISO/IEC 27001:2022 & 27002**: Structure, technical/administrative controls; see specific clause references in sections.
- **Command/OPCON guidance**: Policy harmonization with Framework Nation, Host Nation, and NATO operational command.

---

</policy>
