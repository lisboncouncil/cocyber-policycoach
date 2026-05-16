---
config: C2
context_id: ctx-M
policy_id: P3
policy_name: Access Control Policy
policy_short: accesscontrol
metadata:
  config: C2
  model: moonshotai/Kimi-K2.5
  input_tokens: 25585
  output_tokens: 7706
  total_tokens: 33291
  latency_s: 40.661
  tool_calls:
  - rag_retrieval
  raw_provider_id: 5ccd7313-68c7-4b3d-a857-e08c5749859b
  chunks_retrieved: 5
  server_version: 1.3.4
sources_count: 3
sources:
- type: kb_source
  source: ./datadir-plus-templates/access_control_policy.docx
  title: ./datadir-plus-templates/access_control_policy.docx
- type: kb_source
  source: ./datadir-plus-templates/asset_management.docx
  title: ./datadir-plus-templates/asset_management.docx
- type: kb_source
  source: ./datadir-plus-templates/5.json
  title: Cyber Rapid Response Teams​
prompt_chars: 6039
answer_chars: 15400
generated_at_unix: 1778086844
---

 <policy title="Access Control Policy">

| Field | Value |
|---|---|
| **Document ID** | POL-002 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | NATO RESTRICTED |
| **Owner** | Information Systems Security Manager (ISSM) |
| **Approved by** | Commander, [Detachment Name] |
| **Approval date** | [DD/MM/YYYY] |
| **Next review date** | [DD/MM/YYYY] |
| **Review cycle** | Annual |

---

## 1. Purpose

This policy establishes the framework for managing access to [Organisation]'s information systems and data assets across all NATO classification domains — NATO UNCLASSIFIED (NU), NATO RESTRICTED (NR), NATO SECRET (NS), and MISSION SECRET. It enforces the principles of **need-to-know** and **least privilege** to ensure that access is granted solely on the basis of valid security clearance, mission requirement, and operational role. This policy supports compliance with the NATO Information Security Policy (C-M(2002)49), AC/322-D(2017)0009 (NATO INFOSEC Technical and Implementation Directive), Allied Joint Doctrine for Cyberspace Operations (AJP-3.20), and applicable host-nation legislation including Romanian Cybersecurity Law 58/2019 and GDPR (EU) 2016/679 for civilian personnel data.

---

## 2. Scope

This policy applies to:

- All information systems, applications, and data assets operating within the NU, NR, NS, and MISSION SECRET domains, including the 1,200 classified and 800 unclassified workstations.
- All personnel with access to [Organisation] systems: 1,500 military personnel, 200 civilian NATO staff, and 300 cleared contractors.
- All access methods: on-premises (including SCIF/TEMPEST zones), remote via VPN, and cross-domain via accredited NATO Cross-Domain Solutions (CDS).
- All hardware tokens, smart cards (CAC-equivalent), and cryptographic keys managed under NATO COMSEC procedures.

---

## 3. Roles and Responsibilities

### 3.1 Information Systems Security Manager (ISSM)
- Own and maintain this policy, ensuring alignment with NATO AC/322-D(2017)0009 and host-nation requirements.
- Oversee implementation of access controls across all classification domains.
- Approve exceptions and compensating controls for high-risk access scenarios.
- Report access control posture to the Commander and SHAPE J6.

### 3.2 Security Officer (SY) / Personnel Branch
- Verify NATO and national security clearances (to Secret level or higher) prior to account provisioning, per AC/35-D/1029 (Personnel Security).
- Maintain the personnel security clearance register and notify IT of clearance suspensions or revocations within 24 hours.
- Ensure host-nation security screening for locally employed contractors per Romanian Cybersecurity Law 58/2019.

### 3.3 Unit Commanders / National Contingent Commanders
- Validate **need-to-know** for all access requests within their area of responsibility.
- Confirm access rights remain appropriate during semi-annual reviews.
- Immediately notify the ISSM and J6 of any personnel under investigation (insider threat) or end-of-tour dates.

### 3.4 J6 (CIS) / System Administrators
- Provision, modify, and revoke accounts in accordance with approved requests and clearance levels.
- Configure PKI and smart card authentication per domain; ensure no cross-domain identity federation.
- Maintain audit logs of all access management actions for 12 months, per ISO/IEC 27001:2022 Control 8.2.
- Implement two-person integrity controls for COMSEC key management.

### 3.5 All Personnel (Military, Civilian, Contractors)
- Use only accounts and credentials assigned to them; never share smart cards, PINs, or passwords.
- Report suspected account compromise, lost tokens, or spillage incidents immediately to the 24/7 SOC.
- Comply with TEMPEST zoning and SCIF access procedures for NS and MISSION SECRET domains.

---

## 4. Policy Requirements

### 4.1 Principle of Least Privilege and Need-to-Know
Access is granted on a **default-deny** basis. Every user is granted the minimum access necessary to perform their specific function, limited by both security clearance level and operational need-to-know (NATO Information Security Policy C-M(2002)49, Annex X). Role-based access control (RBAC) must be implemented where technically feasible.

### 4.2 Security Clearance and Eligibility
- Access to NR systems requires a minimum of NATO RESTRICTED clearance; NS systems require NATO SECRET; MISSION SECRET requires national/coalition SECRET clearance validated by the framework nation.
- Clearance verification must be completed prior to account activation (AC/35-D/1029, para 4.2).
- Access to COMSEC keying material requires additional cryptographic access authorization and two-person integrity (TPI) for high-grade material.

### 4.3 User Account Management

#### 4.3.1 Standard User Accounts
- Accounts must be unique and personal; shared accounts are prohibited except for emergency break-glass procedures documented with the ISSM.
- All accounts must be linked to a valid PKI certificate issued by the domain-specific Certificate Authority (NU, NR, NS separate PKIs).
- Contractor accounts must be clearly identifiable (e.g., prefix "CTR-") and automatically expire upon contract end date unless renewed by the contracting officer.

#### 4.3.2 Privileged Accounts (Administrators, Root, COMSEC Custodians)
- Privileged accounts are restricted to the minimum number of personnel necessary (ISO/IEC 27001:2022 Control 5.16).
- Administrators must use separate non-privileged accounts for routine tasks; privileged accounts may not be used for internet browsing or email.
- Access to COMSEC management systems requires dual authorization (two-person integrity) and is logged with tamper-evident mechanisms.
- Privileged access to NS and MISSION SECRET systems from remote locations is prohibited except via accredited CDS with explicit Commander approval.

#### 4.3.3 Service Accounts
- Service accounts must be identifiable (e.g., prefix "SVC-") and prohibited from interactive logon.
- Passwords for service accounts must be minimum 20 characters and stored in the NATO-approved password vault with MFA protection.

### 4.4 Authentication

- **Primary Authentication:** NATO PKI smart cards (CAC-equivalent) are mandatory for all interactive logons to classified systems (NR and above). Biometric authentication (fingerprint/iris) is required for SCIF entry and high-security areas (TEMPEST zones).
- **Multi-Factor Authentication (MFA):** MFA via smart card + PIN is mandatory for all remote access (VPN) and all privileged accounts, per NIST CSF 2.0 PR.AA-01 and AC/322-D(2017)0009.
- **Brute Force Protection:** Accounts must lock for 30 minutes after 3 failed authentication attempts within 5 minutes (ISO/IEC 27001:2022 Control 5.17).
- **Session Timeout:** Sessions on classified workstations must lock automatically after 15 minutes of inactivity (Win+L / Cmd+Ctrl+Q enforced via GPO).

### 4.5 Cross-Domain Access and Spillage Prevention
- **Strict Domain Separation:** No dual-homed systems or simultaneous logon to multiple classification domains (NU/NR/NS) is permitted. No cross-domain identity federation exists between domains (per operational constraints).
- **Cross-Domain Solutions (CDS):** Data transfer between domains is permitted only via NATO-accredited CDS (unidirectional or bidirectional as accredited). All CDS transfers are logged and monitored by the 24/7 SOC.
- **Sanitization:** All media and data transfers from higher to lower classification require formal sanitization and approval via the Security Officer (AC/35-D/1015).

### 4.6 Remote Access
- Remote access to NR, NS, or MISSION SECRET systems is restricted to designated users with valid operational requirements.
- All remote access must traverse NATO-approved VPN gateways with MFA and full tunnel encryption (AES-256).
- Remote access from host-nation networks (Romanian ISPs) is subject to additional monitoring and must comply with SOFA limitations regarding host-nation legal jurisdiction over civilian contractor data (GDPR Article 32 technical measures apply).

### 4.7 Physical and TEMPEST Access Controls
- Access to SCIFs and TEMPEST zones requires dual-factor authentication (smart card + biometric) and escort procedures for non-cleared maintenance personnel.
- Two-person integrity (TPI) is mandatory for access to high-grade COMSEC material and cryptographic facilities.

### 4.8 Access Reviews and Recertification
- Access rights for all users must be reviewed every **6 months** by Unit Commanders and confirmed by the ISSM (ISO/IEC 27001:2022 Control 5.18).
- Security clearances must be revalidated annually; accounts associated with expired clearances must be suspended pending renewal.
- Upon end-of-tour, transfer, or contract termination, access must be revoked within **24 hours** (NATO CIRC best practice).

---

## 5. Monitoring and Logging

- All authentication events (successful and failed), privilege escalation, and cross-domain transfers must be logged by the 24/7 SOC (ISO/IEC 27001:2022 Control 8.2).
- Logs must be retained for a minimum of **12 months** and protected against tampering (write-once media or cryptographic hashing).
- Anomalies (e.g., after-hours access to NS systems, multiple failed logins, suspected insider threat activity) must trigger immediate alerts to the ISSM and investigation per the Cyber Incident Response Plan (aligned with NATO CIRC).

---

## 6. Exceptions

Exceptions to this policy (e.g., temporary bypass of MFA, emergency break-glass accounts, or cross-domain exceptions) require:
- Written justification and risk assessment by the requesting Unit Commander.
- Approval by the ISSM and concurrence by the Commander for NS/MISSION SECRET systems.
- Implementation of compensating controls (e.g., enhanced monitoring, physical escort).
- Time-limitation (maximum 30 days for security-critical controls) and entry in the ISMS Exception Register.

---

## 7. Enforcement

Non-compliance is subject to:
- **Military Personnel:** Disciplinary action under national military codes and NATO Status of Forces Agreement (SOFA) provisions.
- **Civilian Staff:** Administrative sanctions up to and including termination of employment.
- **Contractors:** Immediate revocation of access, contract termination, and debarment from future NATO contracts.
- **Criminal Activity:** Intentional circumvention of access controls, unauthorized data transfer (spillage), or insider threat actions will be referred to national law enforcement and counterintelligence authorities per Romanian Cybersecurity Law 58/2019 and NATO AC/35-D/1015.

---

## 8. Related Documents

| Document ID | Title |
|---|---|
| POL-001 | Cybersecurity Policy |
| POL-003 | Asset Management Policy |
| POL-004 | Backup and Recovery Policy |
| POL-006 | Password Policy |
| POL-007 | Vulnerability and Patch Management Policy |
| POL-008 | Cyber Incident Response Plan |
| Annex A | Account Creation and Modification Form (ACMF) |
| Annex B | Account Removal Form (ARF) |
| Annex C | Cross-Domain Transfer Request Form |

---

## 9. Definitions

| Term | Definition |
|---|---|
| **Need-to-Know** | A security principle restricting access to information to only those persons who require it to perform their official duties (NATO C-M(2002)49). |
| **Clearance** | Formal authorization granted to personnel allowing access to classified information up to a specified level (NU, NR, NS, COSMIC TOP SECRET). |
| **CDS** | Cross-Domain Solution — an accredited hardware/software system for controlled data transfer between security domains. |
| **COMSEC** | Communications Security — measures to prevent unauthorized access to telecommunications and cryptographic material. |
| **SCIF** | Sensitive Compartmented Information Facility — an accredited area for processing SECRET and above information with TEMPEST shielding. |
| **Two-Person Integrity (TPI)** | A security procedure requiring two authorized persons to be present and accountable for access to sensitive material. |
| **PKI** | Public Key Infrastructure — the system of digital certificates, CAs, and registration authorities used for smart card authentication. |
| **Spillage** | Unauthorized transfer of classified information to an unclassified or lower-classification system. |

---

## 10. Compliance and Regulatory References

- **NATO Information Security Policy** C-M(2002)49 and successor — Need-to-know, classification handling.
- **AC/322-D(2017)0009** — NATO INFOSEC Technical and Implementation Directive (authentication, access control).
- **AC/35-D/1015** — Security within NATO (personnel security, incident reporting).
- **AC/35-D/1029** — Personnel Security (clearance verification).
- **AJP-3.20** — Allied Joint Doctrine for Cyberspace Operations (domain separation, defensive cyber operations).
- **ISO/IEC 27001:2022** — Controls 5.15 (Access Control), 5.16 (Managing Access Rights), 5.17 (Authentication Information), 5.18 (Access Rights Reviews), 8.2 (Logging).
- **NIST Cybersecurity Framework 2.0** — PR.AA-01 (Identity Management), PR.AC-01 (Access Control).
- **Romanian Cybersecurity Law 58/2019** — Transposition of NIS Directive and NIS2 (access security for critical infrastructure).
- **GDPR (EU) 2016/679** — Article 32 (technical and organisational measures for civilian/contractor personal data).

---

## 11. Revision History

| Version | Date | Author | Description of Change |
|---|---|---|---|
| 1.0 | [DD/MM/YYYY] | [ISSM Name], ISSM | Initial release for multinational detachment |

---

## 12. Approval

| Role | Name | Signature | Date |
|---|---|---|---|
| Policy Owner (ISSM) | | | |
| Approved by (Commander) | | | |
| Legal/Compliance Review (Staff Judge Advocate) | | | |

---

## Annex A — Account Creation and Modification Form (ACMF)

**Classification: NATO RESTRICTED**

| Field | Details |
|---|---|
| **Request type** | New account / Modification / Privileged elevation |
| **User full name** | |
| **Personnel Category** | Military / Civilian / Contractor |
| **Nationality / Contributing Nation** | |
| **Security Clearance** | NU / NR / NS / MISSION SECRET (Expiry date: ___) |
| **Domain required** | NU / NR / NS / MISSION SECRET |
| **Unit / Section** | |
| **Role / Function** | |
| **Need-to-Know Justification** (Commander sign-off required for NS/MS) | |
| **Start date / End date** (Contractors mandatory) | |
| **Systems / Applications requiring access** | |
| **Access level / Role required** | Standard User / Administrator / COMSEC Custodian |
| **Remote access required?** | Yes / No (If yes, Commander approval required) |
| **Requested by (Unit Commander/N+1)** | |
| **Security Officer clearance verification** | |
| **Approved by (ISSM)** | |
| **IT action completed by** | |
| **Date completed** | |

---

## Annex B — Account Removal Form (ARF)

**Classification: NATO RESTRICTED**

| Field | Details |
|---|---|
| **User full name** | |
| **Personnel Category** | |
| **Last working day / End of tour** | |
| **Domain(s) to revoke** | NU / NR / NS / MISSION SECRET |
| **Reason for removal** | End of tour / Resignation / Termination / Security Incident / Clearance expiry |
| **Security Officer confirmation** | |
| **Requested by (Unit Commander)** | |
| **Approved by (ISSM)** | |
| **IT action completed by** | |
| **Date completed** | |
| **Confirmation: All access revoked, smart card returned, COMSEC material accounted for** | Yes / No |

</policy>
