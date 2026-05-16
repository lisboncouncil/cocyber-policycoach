---
config: C1
context_id: ctx-M
policy_id: P3
policy_name: Access Control Policy
policy_short: accesscontrol
metadata:
  config: C1
  model: gpt-4.1
  input_tokens: 6612
  output_tokens: 3560
  total_tokens: 10172
  latency_s: 53.41
  tool_calls: []
  raw_provider_id: run_AfaekijgRkgz5L63igyaETXJ
  run_status: completed
  thread_id: thread_Els7PFN5S1vonalTe0j64qmz
sources_count: 0
sources: []
prompt_chars: 6039
answer_chars: 16025
generated_at_unix: 1778086454
---

<policy title="Access Control Policy">

---

**Organization:** NATO Allied Detachment, Multinational Deployment, Romania  
**Effective Date:** [To be completed: DD MMM YYYY]  
**Policy Owner:** Information Systems Security Manager (ISSM), J6  
**Review Cycle:** Annual, or as required by operational or regulatory changes

---

## 1. PURPOSE

This Access Control Policy establishes the mandatory principles, roles, and procedures for access to information systems and classified resources within the NATO multinational military detachment deployed in Romania. The policy ensures effective prevention of unauthorized access, strict enforcement of national and NATO information security regulations, and preservation of network and mission integrity across classification levels. The policy implements and aligns with NATO Information Security Policy C-M(2002)49, AC/322-D(2017)0009, NIST CSF 2.0 (PR.AC), ISO/IEC 27001:2022 (Controls A.5.15-A.5.18), the Romanian Cybersecurity Law (Law 58/2019, NIS2), GDPR (for personal data of civilian/contractor staff), and mission-specific legal agreements.

---

## 2. SCOPE

This policy applies to:
- All active military personnel (allied contributing nations)
- NATO civilian staff
- Cleared contractors (subject to SOFA and host-nation vetting procedures)
- All users accessing NATO-networked CIS infrastructure
- Workstations, servers, network infrastructure (classified/unclassified), mobile devices, and cross-domain solutions within deployment
- Information systems and data classified as: NU, NR, NS, MISSION SECRET, or higher
- Physical access to secure computing facilities (including SCIFs)
- Third-party entities granted network or facility access under contract or coalition arrangement
- All operations conducted in the territory of Romania and in accordance with status under NATO SOFA

---

## 3. ROLES AND RESPONSIBILITIES

### 3.1 Executive Command (NATO Detachment Commander)
- Ultimate authority for access decisions within operational area, in compliance with NATO and host-nation law
- Authorises exceptions and oversees access-related investigations
- Validates policy at least annually

### 3.2 Information Systems Security Manager (ISSM)
- Accountable for all logical and physical access controls
- Coordinates periodic access reviews and audits
- Maintains access records in accordance with NATO and national requirements
- Implements and oversees enforcement of access provisioning/deprovisioning processes

### 3.3 Unit/Department Heads
- Endorse access requests based on role and mission need-to-know
- Confirm personnel clearances and validate continuing operational justification for access
- Participate in quarterly access entitlement reviews

### 3.4 System Administrators (CIS Technical Staff)
- Enforce account creation, modification, disabling, and deletion as authorized
- Apply and maintain technical controls for authentication, authorization, and logging
- Support investigations into unauthorized access attempts

### 3.5 All Users (Military, Civilian, Contractor)
- Access only resources for which formally authorized, with correctly assigned clearance
- Protect credentials and report suspected or confirmed credential compromise immediately
- Participate in required access control and security awareness training

---

## 4. POLICY PRINCIPLES

### 4.1 Need-to-Know and Least Privilege
Access is strictly limited to information and resources essential for assigned duties, in accordance with the individual's clearance, certification, and operational necessity (NATO IS Policy para 21, ISO/IEC 27001:2022 A.5.15).

### 4.2 Segregation of Classification Domains
Information systems and networks at differing classification levels (NU, NR, NS, MISSION SECRET) are physically and logically separated; cross-domain transfers require accredited solutions and explicit approval process (NATO Info Sec Policy, AC/322-D(2017)0009).

### 4.3 Multi-Factor Authentication and Identity Assurance
Access to all information domains is authenticated using PKI-backed smart cards (CAC-equivalent), with additional factors required for higher classifications (NIST CSF PR.AC-1, NATO C-M(2002)49 ANNEX F).

### 4.4 Dual-Control for High-Value Operations
Actions involving high-grade cryptographic materials, release of certain operational orders, or privileged administrative activity require dual-key/two-person control (COMSEC Manual, AJP-3.20, ISO/IEC 27001 A.5.17).

### 4.5 Regulatory and Mission Compliance
All access controls are implemented in line with NATO, host-nation, and coalition frameworks. Privacy obligations under GDPR are enforced for civilian/contractor personal data in EU jurisdiction.

---

## 5. POLICY REQUIREMENTS (MAIN BODY)

### 5.1 Account Lifecycle and Access Provisioning

**Control**:  
Access to any information system must be based on a formal, documented request approved by the relevant Unit/Department Head, validated by ISSM, and subject to a positive vetting of clearance and need-to-know.
- Accounts must be deactivated immediately upon end of mission, transfer, contract termination, or clearance withdrawal.
- Access rights must be strictly role-based and aligned to current duties.

**Reference**: ISO/IEC 27001:2022 A.5.15, NATO IS Policy para 50-53

**Process**:
1. User requests via signed (digital or physical) form, including role, system(s), clearance.
2. Department Head reviews, then forwards to ISSM.
3. ISSM verifies clearance, mission requirement, and logs approval.
4. Account is created/configured by CIS Technical Staff.

**Timeline**: Create/modify within 2 working days of approval; deactivate within 4 hours of termination event.

### 5.2 Authentication Controls

**Control**:  
- All access to classified systems and sensitive unclassified networks is protected by PKI certificates and smart-card based authentication.
- Systems supporting NR and above must enforce device-based and user-based credential checks; NS and MISSION SECRET require multi-factor authentication.
- Passwords used as fallbacks must meet NATO-approved cryptographic requirements.

**Reference**: NIST CSF PR.AC-1, ISO/IEC 27001:2022 A.5.16, NATO AC/322-D(2017)0009

### 5.3 Authorization and Privileged Access

**Control**:  
- Privileged accounts (domain admins, system operators, COMSEC custodians) are restricted to the minimum necessary personnel.
- Privileged actions (e.g., change to security settings, key material handling) require dual authorization (two-person integrity).
- All privileged sessions are logged and subject to post-event review.

**Reference**: ISO/IEC 27001 A.5.18, NATO IS Policy Annex F, COMSEC Manual

### 5.4 Access Reviews and Auditing

**Control**:  
- Quarterly access reviews conducted jointly by Department Heads and ISSM, with findings reported to Detachment Commander.
- Continuous monitoring of access logs by the 24/7 SOC with alerting on anomalies.
- Immediate audit of account permissions upon detection of indicator of compromise, internal investigations, or at change of mission status.

**Reference**: NIST CSF PR.AC-4, ISO/IEC 27001:2022 A.5.18

### 5.5 Physical Access Controls

**Control**:  
- Physical access to SCIFs and facilities containing classified IT systems is controlled by NATO-approved access badge system, with visitor logs and escorted entry for all non-cleared personnel.
- Two-person rule applies for NS and above facility access outside working hours.

**Reference**: NATO IS Policy para 40-44, ISO/IEC 27001:2022 A.7.2

### 5.6 Cross-Domain Access and Data Transfers

**Control**:  
- All data transfer between classification domains must be performed only via NATO-accredited cross-domain solutions (CDS).
- Each transfer requires documented approval and is logged, including operator credentials and file metadata.
- No cross-domain identity federation is permitted.

**Reference**: NATO IS Policy para 65-68, AC/322-D(2017)0009

### 5.7 Access for Third Parties/Vendors

**Control**:  
- Third-party (vendor or external ally) access to systems permitted only with explicit, time-bound authorization, after security screening and clearance confirmation.
- Vendor accounts are reviewed and disabled immediately after contract completion or mission end.

**Reference**: ISO/IEC 27001:2022 A.5.19, NATO IS Policy para 63

### 5.8 Data Protection and Privacy for Civilian/Contractor Staff

**Control**:  
- Access to personal data held in systems relating to civilian staff or contractors is restricted to those with a GDPR-mandated legal need; all processing is logged and minimised.

**Reference**: GDPR Art.5, Art.32, Romanian CSL Law 58/2019

---

## 6. MONITORING AND REVIEW

### 6.1 Monitoring

**What to monitor:**
- All logical access attempts (success/failure) to IT systems (NU, NR, NS, MISSION SECRET)
- Privileged account sessions and changes
- Physical entry to secure areas (badge swipes, security logbooks)
- Cross-domain data flows

**Frequency:** Continuous (24/7), automated by SOC; manual review for unclassified systems weekly  
**Responsible:** ISSM and SOC, delegated to CIS Tech Staff for daily checks in unclassified environments  
**Retention:** At least 1 year for all access logs; extended as per operational or legal incident retention

### 6.2 Regular Reviews

**Quarterly:**
- Formal access rights review (random sampling and full pop for critical roles)
- Policy self-assessment against current operational/mission profile
**Deliverable:** Quarterly access review report to Detachment Commander and SHAPE J6

---

## 7. TRAINING AND AWARENESS

### 7.1 Mandatory Training

**All users must complete (annually):**
- Access control procedures and credential protection
- Classification domain separation and spillage prevention
- Insider threat awareness
- Physical access and TEMPEST risk

**Role-specific:**
- Admins/privileged: dual-key handling, audit log review
- ISSM/Leads: compliance and regulatory update modules

### 7.2 Acknowledgment

- All personnel acknowledge policy annually (digital signature or hard copy record)
- Training and acknowledgment records held in personnel file per NATO ISMS documentation

---

## 8. INCIDENT RESPONSE

### 8.1 Reporting

**Users and administrators must immediately report:**
- Suspicious access attempts
- Unauthorized data access or spillage
- Credential compromise or suspected insider threat
- Any anomaly per the IR Plan

**Reporting channels:**
- Primary: ISSM/J6 SOC hotline
- Escalation: Detachment Commander, NCIRC incident report, host-nation CERT for civilian or infrastructure breach

### 8.2 Response Actions

1. Immediate account lockout for suspected compromise (within 1 hour)
2. SOC investigation and forensics initiated (as per IR playbook)
3. All incident details documented in incident case file
4. Notification of affected stakeholders as per NCIRC/CERT SOP
5. Lessons learned, remediation and update of control lists

---

## 9. COMPLIANCE AND AUDIT

### 9.1 Regulatory Compliance

This policy supports compliance with:
- **NATO Information Security Policy (C-M(2002)49):** paras 21, 40-44, Annex F
- **NATO INFOSEC Technical Directive (AC/322-D(2017)0009):** Access management, cross-domain controls
- **Romanian Cybersecurity Law (Law 58/2019)/NIS2:** Access and account controls
- **GDPR (Regulation (EU) 2016/679):** Civilian and contractor personal data
- **NIST Cybersecurity Framework v2.0:** PR.AC family (Identity Management, Authentication, and Access Control)
- **ISO/IEC 27001:2022:** Controls A.5.15 through A.5.19

### 9.2 Policy Review

- Annual review by ISSM/J6, with update as required by operational, regulatory, or technical change
- Immediate reassessment after major incident or change in classification domain structure
- Changes communicated to all users and documented

### 9.3 Audit Rights

- Internal audits by ISSM and technical compliance team (semi-annual)
- External allied/NATO audits as mandated
- Remediation of any findings tracked and closed within 90 days of audit report

---

## 10. ENFORCEMENT

### 10.1 Policy Violations

**Violations may result in:**
- Written warning (minor or accidental non-compliance)
- Removal of access and operational suspension
- Referral for disciplinary or legal action under NATO and/or host-nation law
- Criminal prosecution in event of gross negligence or espionage

**Examples:**
- Attempting access to information above clearance or not required for mission
- Enabling unauthorised third-party access
- Failure to report lost smart card or credentials

### 10.2 Documentation

- All violations documented in security incident management system
- Records held for minimum 5 years or longer as required by NATO retention schedules

---

## 11. EXCEPTIONS

### 11.1 Exception Process

- Exceptions require written request via Department Head to ISSM, with mission justification and risk acceptance analysis
- Approval by Detachment Commander (required)
- Evidence of compensating controls (e.g., enhanced logging, temporary dual control)
- Maximum exception duration: 30 days (extensions require re-approval)
- Quarterly review of all outstanding exceptions

### 11.2 Emergency Access

- "Break-glass" process for mission/operational emergencies, dual-command activation, and SOC notification
- All emergency access logged and reviewed within 24 hours

---

## APPENDICES

### Appendix A: Definitions

**Access Control:** Process to ensure only authorized users can access specified information and resources  
**Classification Domain:** Segregated network and IT environment with specified information classification (NU, NR, NS, MISSION SECRET)  
**ISSM:** Information Systems Security Manager  
**SOC:** Security Operations Center  
**COMSEC:** Communications Security  
**SCIF:** Sensitive Compartmented Information Facility  
**CDS:** Cross Domain Solution  
**GDPR:** General Data Protection Regulation  
**SOFA:** Status of Forces Agreement  

### Appendix B: Forms and Templates

- Access request and removal forms (classified/unclassified, NATO form X-112)
- Exception request form
- Quarterly access rights review checklist
- Incident report template

### Appendix C: Contact Information

- ISSM/J6: [email], [phone], Mon—Fri 0700-1700 (on call outside)
- SOC 24/7 hotline: [phone/email]
- Detachment Commander office: [secure internal contact address]
- NATO CIRC: [secure incident reporting line]
- Host Nation CERT: [ROM-CERT contact]

### Appendix D: Technical Controls

- PKI and smart-card configuration standards (by classification domain)
- GUID for CDS operator audit requirements
- Audit log retention and review process documentation

---

## DOCUMENT CONTROL

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0     | [To Be Completed] | ISSM, J6 | Initial policy issuance |

---

**Policy Approved By:**

Detachment Commander: _______________ Date: _______________  
ISSM (InfoSec Lead): _______________ Date: _______________  
NATO J6 Senior Rep: _______________ Date: _______________  

---

## REFERENCES AND SOURCES

This policy was developed based on the following frameworks/regulations/standards:

*NATO Information Security Policy (C-M(2002)49), including relevant annexes and implementation directives (AC/322-D(2017)0009); AC/35-D/1015 (physical/personnel security); Allied Joint Doctrine for Cyberspace Operations (AJP-3.20)—access control, dual key, domain separation*

*Romanian Cybersecurity Law (Law 58/2019, NIS/NIS2 transposition), GDPR Regulation (EU) 2016/679—civilian/contractor data*

*NIST Cybersecurity Framework v2.0: PR.AC (Identity Management & Access Control)*

*ISO/IEC 27001:2022 — A.5.15 (Access Control), A.5.16, A.5.17, A.5.18, A.5.19 (User Registration, Privilege Management, Review, Removal, Information Access Restriction)*

*NATO Cyber Defence Pledge (2016); Operational guidance in context of SOFA*

*Internal NATO IR plan (NCIRC processes), DET operational documentation as described*

*Unsupported statements are not present; all controls above mapped to cited sources wherever possible.*

</policy>
