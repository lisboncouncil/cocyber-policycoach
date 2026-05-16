---
config: C2b
context_id: ctx-H
policy_id: P1
policy_name: Password Policy
policy_short: password
metadata:
  config: C2b
  model: Qwen/Qwen3-235B-A22B-Instruct-2507
  input_tokens: 26308
  output_tokens: 3445
  total_tokens: 29753
  latency_s: 40.803
  tool_calls:
  - rag_retrieval
  raw_provider_id: 6b399cc7-3aa6-4965-ab5b-c71d3c330f96
  chunks_retrieved: 5
  server_version: 1.3.4
sources_count: 3
sources:
- type: kb_source
  source: ./datadir-plus-templates/password_policy.docx
  title: ./datadir-plus-templates/password_policy.docx
- type: kb_source
  source: ./datadir-plus-templates/cybersecurity_policy_BASIC.docx
  title: ./datadir-plus-templates/cybersecurity_policy_BASIC.docx
- type: kb_source
  source: ./datadir-plus-templates/asset_management.docx
  title: ./datadir-plus-templates/asset_management.docx
prompt_chars: 4657
answer_chars: 14295
generated_at_unix: 1778174714
---

<policy title="Password Policy">
# Password Policy

| Field | Value |
|---|---|
| **Document ID** | POL-006 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Internal — Restricted |
| **Owner** | IT Manager (in coordination with Regional ASL Security Officer) |
| **Approved by** | Director General, Azienda Sanitaria Locale (ASL) |
| **Approval date** | [DD/MM/YYYY] |
| **Next review date** | [DD/MM/YYYY] |
| **Review cycle** | Annual |

---

## 1. Purpose

This Password Policy establishes the requirements for the creation, management, protection, and use of passwords used to authenticate access to information systems and data at the [Hospital Name], a provincial public hospital operating under the Italian Servizio Sanitario Nazionale (SSN). The policy ensures that password practices support the confidentiality, integrity, and availability of sensitive health data and critical clinical systems, in compliance with **GDPR (EU) 2016/679**, **D.Lgs. 196/2003 as amended**, **NIS2 Directive (EU) 2022/2555**, and **AGID Linee Guida per la sicurezza informatica nella PA**.

Given the high risk of ransomware, phishing, and insider threats in the healthcare sector, and the limited internal IT resources (1.5 FTE), this policy prioritises practical, enforceable controls that align with modern security principles—emphasising password length, multi-factor authentication (MFA), and integration with existing identity infrastructure (SPID/CIE, Active Directory). It supports the organisation’s ongoing efforts toward ISO/IEC 27001:2022 and NIST CSF 2.0 alignment.

---

## 2. Scope

This policy applies to:

- All user accounts accessing [Hospital Name]’s information systems, including:
  - Cartella Clinica Elettronica (FSE)
  - PACS / RIS (Radiology)
  - LIS (Laboratory)
  - ADT (Admission/Discharge/Transfer)
  - Pharmacy Management System
  - Active Directory, email, and administrative systems
- All personnel: clinical staff (doctors, nurses, technicians), administrative staff, facility/technical staff, contractors, and temporary personnel
- All devices: desktop workstations (including legacy Windows systems), mobile point-of-care devices, and remote access clients
- All authentication methods involving passwords, including local accounts, domain accounts, and federated identities where password is a factor

This policy does **not** apply to:
- Service accounts used exclusively for machine-to-machine communication and not accessible via interactive login (covered under Vulnerability and Patch Management and Access Control policies)
- Systems physically isolated from the network and protected by strong physical access controls (e.g., standalone diagnostic devices), provided such exceptions are formally documented and approved

---

## 3. Roles and Responsibilities

### 3.1 IT Manager (Policy Owner)
- Own and maintain this policy
- Configure and enforce password policies across Active Directory and applicable systems
- Coordinate with the external Managed Service Provider (MSP) to ensure compliance
- Audit password policy enforcement at least annually
- Report compliance status to the Regional ASL Security Officer

### 3.2 Regional ASL Security Officer
- Provide oversight and approval for security policies within the regional healthcare network
- Ensure alignment with regional FSE regulations and SSN-wide security directives
- Approve exceptions involving cross-system or regional identity implications

### 3.3 Department Heads (Clinical and Administrative)
- Ensure staff under their supervision comply with password requirements
- Report staff departures or role changes to IT within 24 hours to trigger access revocation
- Reinforce secure password practices during team briefings

### 3.4 All Users
- Create and use passwords in accordance with this policy
- Never share passwords, write them down in unsecured locations, or include them in emails/messages
- Immediately report suspected password compromise to IT
- Use only organisation-approved methods for password storage (e.g., no personal password managers)
- Complete mandatory security awareness training, including password hygiene

---

## 4. Policy Principles

### 4.1 Length Over Complexity
Prioritise long passwords or passphrases over complex but short ones. Modern guidance (NIST SP 800-63B) indicates that length significantly increases entropy and usability, reducing helpdesk burden and password fatigue. *Supported by: NIST SP 800-63B, Section 5.1.1.2; ISO/IEC 27001:2022, A.8.2 Authentication information*

### 4.2 Multi-Factor Authentication (MFA) as Primary Defence
Where technically feasible, MFA must be enforced, especially for remote access, privileged accounts, and systems containing health data. Given the high phishing risk and limited detection capabilities, MFA is a critical compensating control. *Supported by: NIS2 Article 21(4); GDPR Article 32; AGID Misure Minime, Section 3.2.1*

### 4.3 Risk-Based Enforcement
Password requirements are tailored to system criticality and user role. Legacy systems with technical limitations are subject to compensating controls (e.g., network isolation, MFA on access gateway). *Supported by: ISO/IEC 27001:2022, A.5.7 Threat intelligence; NIST CSF PR.AC-1*

### 4.4 Usability and Clinical Workflow
Controls must not impede emergency clinical operations. Authentication mechanisms must support rapid access in critical situations (e.g., break-glass accounts with audit logging). *Supported by: AGID Linee Guida, Section 4.3 – Continuity of Service*

---

## 5. Password Requirements

### 5.1 Minimum Password Strength

| Account Type | Minimum Length | Complexity Requirements |
|--------------|----------------|--------------------------|
| Standard User (clinical, admin) | **12 characters** | At least three of: uppercase, lowercase, digits, special characters (`!@#$%^&*`) |
| Privileged Accounts (domain admin, system admin) | **16 characters** | Same as above; must not contain username or personal identifiers |
| Service Accounts (interactive use) | **20 characters** | Auto-generated, stored in secure vault; complexity enforced by system |

> **Note**: Systems must reject passwords found in known breach databases where technically feasible (e.g., via integration with deny lists). *Supported by: NIST SP 800-63B, Section 5.1.1.2*

### 5.2 Password Change Policy

| Scenario | Requirement |
|--------|-------------|
| Default/vendor passwords | Changed immediately upon first use |
| Temporary passwords (set by IT) | Must be changed at first login |
| Suspected or confirmed compromise | Changed immediately across all affected systems |
| Periodic change (non-privileged accounts) | Every **12 months**, provided password is at least 12 characters long |
| Periodic change (privileged accounts) | Every **6 months** |
| Service accounts | Changed every **90 days** or upon personnel change with knowledge of credential |

> **Rationale**: NIST SP 800-63B and AGID guidance discourage arbitrary frequent changes for long passwords, as they increase user burden and may lead to weaker patterns. However, due to high staff turnover and phishing risk, a 12-month cycle is retained for standard accounts. *Supported by: NIST SP 800-63B, Section 5.1.1.2; AGID Misure Minime, Section 3.2.1*

### 5.3 Password Reuse and History
- Systems must prevent reuse of the last **5 passwords**.
- Shared passwords (e.g., for kiosk logins) must be changed immediately upon departure of any staff member who knew the password.

### 5.4 Brute Force Protection
All systems accessible from the internet or clinical VLANs must implement one of the following:
- **Account lockout**: Lock account for **30 minutes** after **5 failed attempts**
- **IP-based rate limiting**: Block source IP for **1 hour** after **10 failed attempts**
- **Progressive delay**: Increase delay between login attempts (e.g., 1s → 2s → 4s)

> *Supported by: ISO/IEC 27001:2022, A.8.2; AGID Misure Minime, Section 3.2.1*

---

## 6. Password Handling and Protection

- **No sharing**: Passwords must never be shared, even among team members. Shared accounts must be avoided; if technically unavoidable (e.g., clinical kiosk), access must be logged and reviewed monthly.
- **No transmission in clear text**: Passwords must not be sent via email, chat, or phone. If temporary credentials must be issued, they must be delivered via secure channel (e.g., in person, encrypted message) and expire after **7 days**.
- **Storage**: 
  - Passwords must not be stored in plain text, spreadsheets, or browser "remember password" functions.
  - Use of personal password managers is **prohibited**.
  - Organisation-approved password vault (managed by MSP) must be used for privileged and service accounts.
- **Physical storage**: If a break-glass password must be written (e.g., emergency access), it must be stored in a sealed envelope in a locked safe, with access logs. *Supported by: AGID Linee Guida, Section 4.4 – Emergency Access*

---

## 7. Multi-Factor Authentication (MFA)

MFA must be enforced for:
- All remote access via VPN
- Privileged accounts (domain admin, system admin)
- Access to FSE, PACS, LIS, and Pharmacy systems from outside clinical VLANs
- Any account with access to health data of minors

MFA methods must include at least one of:
- SPID or CIE (Carta d’Identità Elettronica) via regional federation
- Authenticator app (TOTP)
- Hardware token

SMS-based OTP is **not permitted** for initial login due to SIM-swapping risks. *Supported by: NIS2 Article 21(4); AGID Misure Minime, Section 3.2.1; ENISA Recommendations on MFA*

---

## 8. Exceptions

Exceptions to this policy may be granted only under the following conditions:
- **Justification**: Technical incompatibility (e.g., legacy Windows kiosk), operational necessity (e.g., emergency device), or procurement delay
- **Approval**: Written approval from IT Manager and Regional ASL Security Officer
- **Compensating controls**: Must include at least two of:
  - Network isolation (e.g., VLAN segmentation, firewall rules)
  - MFA on access gateway
  - Enhanced logging and monitoring
  - Physical access controls
- **Duration**: Maximum **6 months**, subject to review
- **Documentation**: Recorded in the ISMS exception register

> *Supported by: ISO/IEC 27001:2022, A.5.1 Policy for information security; NIS2 Article 21(5)*

---

## 9. Monitoring and Review

- **Compliance checks**: IT Manager, in coordination with MSP, will verify password policy enforcement on Active Directory and critical systems **quarterly**.
- **Incident review**: All password-related incidents (compromise, policy violation) will be logged and reviewed monthly.
- **Policy review**: This policy will be reviewed **annually** or after any significant incident, in coordination with the Regional ASL Security Officer.
- **Training integration**: Password hygiene will be included in the mandatory **2 hours/year** security awareness training, with focus on phishing and secure handling.

---

## 10. Enforcement

- **Minor violations** (e.g., weak password, temporary sharing): Verbal warning and mandatory retraining
- **Moderate violations** (e.g., repeated non-compliance, unauthorised password storage): Formal written warning, access suspension
- **Severe violations** (e.g., deliberate sharing of privileged credentials, failure to report compromise): Disciplinary action up to termination; potential reporting to Garante Privacy if health data is involved

All violations will be documented in the ISMS incident register.

---

## 11. Related Documents

| Document ID | Title |
|---|---|
| POL-001 | Cybersecurity Policy |
| POL-002 | Access Control Policy |
| POL-004 | Backup and Recovery Policy |
| POL-008 | Cyber Incident Response Plan |
| POL-007 | Vulnerability and Patch Management Policy |

---

## 12. Definitions

| Term | Definition |
|------|-----------|
| **MFA** | Multi-Factor Authentication — verification using two or more factors (e.g., password + token) |
| **SPID/CIE** | Italian digital identity systems used for secure authentication |
| **Break-glass account** | Emergency access account used only in life-threatening situations, with full audit logging |
| **Service account** | Non-human account used by applications or systems |
| **Legacy system** | Outdated system with limited security capabilities (e.g., Windows 7/8 on clinical kiosks) |
| **ISMS** | Information Security Management System — framework for managing security risks |

---

## 13. Compliance and Regulatory References

This policy supports compliance with:

- **GDPR (EU) 2016/679** — Article 32 (security of processing)
- **D.Lgs. 196/2003 as amended by D.Lgs. 101/2018** — Articles 33–35 (security measures for health data)
- **NIS2 Directive (EU) 2022/2555** — Articles 21, 22 (security and incident reporting obligations for essential entities)
- **AGID Linee Guida per la sicurezza informatica nella PA** — Sections 3.2, 4.3, 4.4
- **AGID Misure Minime di Sicurezza per le PA** — Section 3.2.1 (authentication)
- **NIST SP 800-63B** — Digital Identity Guidelines: Authentication and Lifecycle Management
- **ISO/IEC 27001:2022** — Controls A.5.1, A.5.7, A.8.2, A.8.11
- **NIST Cybersecurity Framework (CSF) 2.0** — PR.AC-1, PR.AC-7

---

## 14. Revision History

| Version | Date | Author | Description of Change |
|--------|------|--------|------------------------|
| 1.0 | [DD/MM/YYYY] | IT Manager, [Hospital Name] | Initial release |

---

## 15. Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Policy Owner (IT Manager) | | | |
| Regional ASL Security Officer | | | |
| Approved by (Director General, ASL) | | | |
| Compliance Review (Privacy Officer) | | | |

</policy>

*Sources consulted:*
- *[1] ./datadir-plus-templates/password_policy.docx — Provided baseline structure and technical controls for password policies.*
- *[2] ./datadir-plus-templates/cybersecurity_policy_BASIC.docx — Informed alignment with GDPR, AGID, and NIS2 requirements in public sector context.*
- *[3] ./datadir-plus-templates/asset_management.docx — Indirectly informed risk-based approach to system classification and access control.*
- *NIST SP 800-63B, ISO/IEC 27001:2022, AGID Linee Guida and Misure Minime — Cited directly in policy text for auditability.*
