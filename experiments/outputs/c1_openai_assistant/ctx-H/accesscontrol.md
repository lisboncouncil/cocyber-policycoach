---
config: C1
context_id: ctx-H
policy_id: P3
policy_name: Access Control Policy
policy_short: accesscontrol
metadata:
  config: C1
  model: gpt-4.1
  input_tokens: 6392
  output_tokens: 3290
  total_tokens: 9682
  latency_s: 33.646
  tool_calls: []
  raw_provider_id: run_2YgRi7DJUc1kOhF8FvKCsrhb
  run_status: completed
  thread_id: thread_E4PxHTNnvxn2raQ6VMbARI8c
sources_count: 0
sources: []
prompt_chars: 4669
answer_chars: 13825
generated_at_unix: 1778086267
---

<policy title="Access Control Policy">

---

**Organization:** Azienda Sanitaria Locale [Province-level Small Public Hospital], Italy  
**Effective Date:** [Insert Effective Date: e.g., 2024-06-19]  
**Policy Owner:** Director of IT/ICT (or delegated Data Protection Officer)  
**Review Cycle:** Annual (or upon regulatory/operational change)

---

## 1. PURPOSE

This Access Control Policy establishes the framework and operational requirements for access to information systems and data managed by the [Hospital Name], ensuring confidentiality, integrity, and availability of all sensitive health and personal information in compliance with GDPR (Regulation EU 2016/679), NIS2 Directive (EU 2022/2555), Italian data protection law (D.Lgs. 196/2003, as amended), AGID cybersecurity requirements for Italian public administration, and referencing ISO/IEC 27001:2022 and NIST CSF 2.0 best practices.

---

## 2. SCOPE

This policy applies to:
- All hospital staff (clinical, administrative, technical/facility)
- Managed Service Provider (MSP) and contracted external personnel
- Volunteers, interns, and temporary staff
- All physical and virtual systems: workstations (legacy and current), mobile point-of-care devices, on-premises and federated accounts (Active Directory, SPID/CIE)
- Core clinical applications: EHR/FSE, PACS/RIS, LIS, ADT, Pharmacy
- All data classified as personal or health data, including minors' data and employee records
- The entire hospital facility and remote (VPN) access

---

## 3. ROLES AND RESPONSIBILITIES

### 3.1 Executive Administrative Director / Data Protection Officer (DPO)
- Accountable for ensuring compliance with this policy and regulatory frameworks.
- Approves major access exceptions and high-impact privilege assignments.
- Ensures policy review and communicates updates to all staff.

### 3.2 IT/ICT Manager (Internal/Outsourced)
- Implements access controls per this policy, including user lifecycle management.
- Maintains access logs and ensures provisioning/de-provisioning activities.
- Conducts/coordinates periodic access reviews (minimum annually).
- Escalates and responds to access-related incidents.

### 3.3 Department Heads (Wards/Units)
- Approve access requests for their department staff.
- Ensure onboarding/offboarding/mobility processes are triggered for access change.

### 3.4 All Users (Staff, Temporary, Contractors)
- Use only assigned credentials and never share passwords.
- Report suspicious or unauthorized access immediately.
- Complete mandatory training on access control and privacy.

---

## 4. POLICY PRINCIPLES

### 4.1 Least Privilege

Access rights are allocated to grant the minimum necessary permissions for users to perform assigned duties, reducing the risk of accidental or intentional data breach (ISO 27001:2022, A.9.1.2; NIST CSF ID.AM-3).

### 4.2 Need-to-Know

Access to patient and sensitive data is strictly controlled, limited to staff with an identifiable, documented clinical or operational need (GDPR Art. 32(1)(b); AGID Linee Guida §4.2).

### 4.3 Segregation of Duties

Critical operations (such as those involving sensitive health data or systems administration) require role separation to prevent error and fraud (ISO 27001:2022, A.6.2.2).

### 4.4 Accountability and Traceability

All access must be attributable to a unique user. Actions are logged for audit purposes to ensure traceability (NIS2 Recital 79; GDPR Art. 5(1)(f); ISO 27001 A.12.4.1).

---

## 5. POLICY REQUIREMENTS

### 5.1 User Identification and Authentication

**Control:**  
- Each user is assigned an individual, non-transferable account for all hospital information systems.
- Authentication is required for all access to digital systems, using passwords that meet minimum complexity requirements or strong authentication via federation (SPID/CIE).

**Process:**  
1. Assign unique accounts via Active Directory or federation for all new staff before system access.
2. Enforce password strength: minimum 10 characters, mix of letters, numbers, and symbols; prohibit reuse for 12 months.
3. Require second-factor authentication (2FA) for all remote access and privileged accounts where technically feasible.

**Timeline:**  
- At onboarding; password changes prompted every 180 days or upon suspected compromise.

**Controls:**  
- Technical: Password policy in AD, federation integration, MFA.
- Administrative: Staff training, documented onboarding/offboarding.
- Reference: ISO 27001 A.5.17, A.8.2.2; AGID "Misure minime", §4.1; GDPR Art. 32(1)(b).

---

### 5.2 Authorization and Role Assignment

**Control:**  
- Access is provisioned based on pre-defined roles (clinical, admin, technical) and department/unit.
- Department Heads must approve all access requests to applications with health data.

**Process:**  
1. Document role-based access matrices for major applications (EHR, PACS, etc.).
2. Secure written approval (electronic or paper) from Department Head.
3. IT/ICT to provision access accordingly.
4. Limit administrative privileges to minimum required MSP and internal IT staff.

**Timeline:**  
- At onboarding/change of job function; revoke immediately upon termination or leave.

**Controls:**  
- Technical: Role profiles in AD and main clinical systems.
- Administrative: Access request forms, supervisor approvals.
- Reference: ISO 27001 A.5.18, A.8.2.3; AGID Linee Guida §4.2; NIS2 Art. 21.

---

### 5.3 Access Reviews and Recertification

**Control:**  
- Conduct formal access reviews at least annually, and upon significant organizational change.

**Process:**  
1. Department Heads and IT jointly review active accounts and privileges to ensure alignment with current duties.
2. Revoke or adjust access as required.
3. Document and archive review results.

**Timeline:**  
- At least annually; immediately post-role change.

**Controls:**  
- Technical: Audit tools built into systems, export account lists.
- Administrative: Review forms/checklists, sign-off logs.
- Reference: ISO 27001 A.8.2.4; GDPR Art. 32; NIST CSF PR.AC-4.

---

### 5.4 Privileged Access Management

**Control:**  
- Elevated (administrator/root) privileges are restricted to MSP and authorized IT staff.
- Usage of privileged accounts is logged, and privileged actions are subject to monitoring.

**Process:**  
1. Designate short-term privileged access for specific admin tasks.
2. Require secondary, individual admin credentials (not shared) wherever possible.
3. Periodically review admin accounts for necessity and usage.

**Timeline:**  
- On privilege grant/review; logs retained for minimum 12 months.

**Controls:**  
- Technical: Separate privilege accounts; enforced log monitoring.
- Administrative: Admin access approval workflow.
- Reference: AGID "Misure minime" §4.2.3; ISO 27001 A.8.2.1, A.12.4.1.

---

### 5.5 Remote and Mobile Access

**Control:**  
- VPN access is enforced for all remote connections; device authentication and compliance checks are required.
- Lost/stolen mobile devices are to be reported and remotely locked/erased.

**Process:**  
1. Enable VPN client-to-site for external staff with two-factor authentication.
2. Register mobile devices in hospital asset inventory; enable device encryption and remote wipe.
3. Staff to report lost devices within 1 hour; IT disables associated accounts and wipes device where possible.

**Timeline:**  
- VPN: Each connection; mobile: upon loss/theft.

**Controls:**  
- Technical: VPN, device encryption, MDM (if available).
- Administrative: User awareness, inventory logs.
- Reference: ISO 27001 A.6.2.1, A.6.2.2; NIS2 Art. 21; AGID Linee Guida §5.

---

### 5.6 Legacy Systems

**Control:**  
- Restrict access to legacy clinical kiosks (legacy Windows) to essential staff, minimize data footprint, and monitor anomalous activity.

**Process:**  
1. Maintain a documented list of authorized kiosk users.
2. Apply compensating controls: restrict software install, deploy AV, regular monitoring.
3. Plan for phased replacement as per procurement constraints.

**Timeline:**  
- Immediate; review quarterly.

**Controls:**  
- Technical: Local restrictions/AV.
- Administrative: Kiosk user roster.
- Reference: AGID Linee Guida, "Misure minime" §4.3.1.

---

## 6. MONITORING AND REVIEW

### 6.1 Access Logging and Auditing

- Log user logon/logoff and privileged activity for all systems handling health or personal data.
- Logs reviewed by IT in collaboration with MSP monthly; suspicious access patterns escalated to DPO.
- Retain access logs for minimum 12 months, or as required by law/regulation.

### 6.2 Regular Reviews

- Annual policy review by IT Manager and DPO.
- Trigger reviews: changes to clinical system providers, significant incidents, regulatory updates.

**Deliverable:**  
Policy review report, access review records.

---

## 7. TRAINING AND AWARENESS

### 7.1 Mandatory Training

All staff must attend annual training (minimum 2 hours/year) covering:
- Secure password practices
- Risks of credential sharing/social engineering
- Reporting procedures for lost/stolen devices or suspected compromise

### 7.2 Acknowledgment

- Users are required to sign policy receipt and training attendance.
- Records maintained in HR files.

---

## 8. INCIDENT RESPONSE

### 8.1 Reporting

All users must immediately report:
- Suspected unauthorized access, credential compromise, or phishing
- Lost/stolen access device

Reporting channels:
- First: internal IT helpdesk
- Escalation: MSP contact or hospital DPO

### 8.2 Response Actions

Upon report:
1. IT disables affected accounts within 1 hour.
2. MSP/IT investigates and logs incident.
3. DPO notifies authorities/data subjects as required by GDPR/NIS2 if breach is confirmed.
4. Lessons learned shared in post-incident review.

**Reference:** ISO 27001 A.5.26; GDPR Art. 33–34; NIS2 Art. 23.

---

## 9. COMPLIANCE AND AUDIT

### 9.1 Regulatory Compliance

This policy supports compliance with:
- **GDPR (Regulation EU 2016/679):** Art. 5, 25, 32, 33–34
- **D.Lgs. 196/2003 as amended, D.Lgs. 101/2018**
- **NIS2 Directive (EU 2022/2555):** Essential entity obligations, Art. 21–23
- **AGID Linee Guida / Misure Minime:** §§4–5
- **ISO/IEC 27001:2022:** Controls A.5.17–A.5.18, A.6.2.1–A.6.2.2, A.8.2.x, A.12.4.1
- **Regional healthcare data regulations**

### 9.2 Policy Review

- Annual review by IT Manager/DPO or upon significant operational/regulatory change.
- Policy and access procedures updated and communicated promptly.

### 9.3 Audit Rights

- Internal audit: annually, documented by IT/Administration.
- External audit: following regional/national authorities' requirements or as requested by supervisory authorities.

---

## 10. ENFORCEMENT

### 10.1 Policy Violations

Violations may result in:
- User retraining (minor, e.g., infrequent password mishandling)
- Formal reprimand or limitation of account (moderate, e.g., unauthorized data access)
- Disciplinary action up to termination or legal action (severe, e.g., unauthorized disclosure, credential sharing, intentional breach)
- Deduction or criminal procedures for matters involving patient data per GDPR/NIS2

### 10.2 Documentation

- All violations and actions taken are documented by HR and IT.

---

## 11. EXCEPTIONS

### 11.1 Exception Process

- Exception requests must be submitted in writing to the IT Manager and DPO, detailing reasons and compensating controls.
- Approvals are documented and time-limited (maximum 6 months).
- All exceptions are reviewed at policy review or upon operational change.

### 11.2 Emergency Access

- “Break-glass” accounts (generic/override credentials) are restricted; usage logged and justified in medical emergencies only.
- Every such use is subject to immediate review by DPO and Department Head.

---

## APPENDICES

### Appendix A: Definitions

- **Active Directory (AD):** Microsoft’s directory service for user authentication and access control.
- **SPID/CIE Federation:** Italian digital identity systems for public sector authentication.
- **EHR/FSE:** Electronic Health Record / Fascicolo Sanitario Elettronico.
- **MSP:** Managed Services Provider.
- **2FA (Two-factor Authentication):** Security process requiring two forms of identification.
- **MDM:** Mobile Device Management, technology for managing mobile devices remotely.

### Appendix B: Forms and Templates

- User Access Request Form
- Department Approval Form
- Access Review Checklist

### Appendix C: Contact Information

- IT Helpdesk: [Insert email/telephone]
- DPO: [Insert contact]
- MSP Service Desk: [Insert contact]

---

## DOCUMENT CONTROL

| Version | Date       | Author          | Changes                       |
|---------|------------|-----------------|-------------------------------|
| 1.0     | 2024-06-19 | [Policy Owner]  | Initial release               |


### Approval Block

Policy Approved By:

Executive Director: _______________ Date: _______________

IT/ICT Manager: _______________ Date: _______________

Data Protection Officer: _______________ Date: _______________

---

## REFERENCES AND SOURCES

This policy has been developed based on the following frameworks, regulations, and standards:

*GDPR (Regulation EU 2016/679)* — especially Art. 5, 25, 32, 33–34  
*D.Lgs. 196/2003 as amended by D.Lgs. 101/2018* (Italian Personal Data Code)  
*NIS2 Directive (EU 2022/2555):* Arts. 21–23  
*AGID Linee Guida per la sicurezza informatica nella PA*  
*AGID Misure minime per la PA* §§4–5  
*Regional regulations on FSE (Fascicolo Sanitario Elettronico)*  
*Provvedimenti Garante Privacy in sanità*  
*ISO/IEC 27001:2022: A.5.17, A.5.18, A.6.2.1, A.6.2.2, A.8.2.1–A.8.2.4, A.12.4.1*  
*NIST Cybersecurity Framework 2.0: ID.AM, PR.AC, DE.CM*  
*Operational threat and asset details drawn from sectoral incident reports, Italian PA and regional guidance (2023–2025)*

</policy>
