---
config: C2
context_id: ctx-H
policy_id: P1
policy_name: Password Policy
policy_short: password
metadata:
  config: C2
  model: moonshotai/Kimi-K2.5
  input_tokens: 25338
  output_tokens: 3744
  total_tokens: 29082
  latency_s: 20.141
  tool_calls:
  - rag_retrieval
  raw_provider_id: 75fb5db1-88fe-4b96-8608-79e9530e0060
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
answer_chars: 13260
generated_at_unix: 1778086576
---

 <policy title="Password Policy">
| Field | Value |
|---|---|
| **Document ID** | POL-006-ASL |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Internal — Restricted |
| **Owner** | Responsabile del Servizio Informatico / IT Manager |
| **Approved by** | Direttore Generale (CEO equivalent) |
| **Approval date** | [DD/MM/YYYY] |
| **Next review date** | [DD/MM/YYYY] |
| **Review cycle** | Annual |

---

## 1. Purpose

This policy establishes the minimum requirements for password creation, management, and protection across all information systems of [Azienda Ospedaliera Provinciale — insert hospital name] (hereinafter "[Organisation]"). It ensures that authentication mechanisms adequately protect the confidentiality, integrity, and availability of patient health data (dati sanitari), personal data, and critical clinical systems, in compliance with the NIS2 Directive (EU) 2022/2555 (essential entity obligations), GDPR (EU) 2016/679, D.Lgs. 196/2003 as amended by D.Lgs. 101/2018, and AGID Linee Guida per la sicurezza informatica nella PA.

Given the 24/7 clinical operations and resource constraints (1.5 FTE internal IT staff with MSP support), this policy balances security rigour with clinical workflow usability, prioritising Multi-Factor Authentication (MFA) and password length over arbitrary complexity, while maintaining defensible controls for legacy clinical systems.

---

## 2. Scope

This policy applies to:

- All user accounts accessing [Organisation]'s information systems, including the Cartella Clinica Elettronica (FSE), PACS/RIS, LIS, ADT, Pharmacy management, and administrative systems
- All employees (clinical, administrative, technical), contractors, MSP personnel, and third-party vendors with system access
- All devices: workstations (including 35 legacy Windows clinical kiosks), mobile point-of-care devices (60 units), and remote access endpoints
- All authentication methods: local Active Directory, regional SPID/CIE federation, and application-specific logins
- Service accounts and emergency access (break-glass) credentials

---

## 3. Roles and Responsibilities

### 3.1 Responsabile del Servizio Informatico (IT Manager)
- Own and maintain this policy, ensuring alignment with AGID and regional ASL requirements
- Configure and enforce password settings via Active Directory Group Policy and IAM systems
- Approve exceptions and emergency access procedures
- Liaise with the MSP to ensure password policy compliance in outsourced systems

### 3.2 MSP (Managed Service Provider)
- Implement technical controls per this policy on managed infrastructure
- Monitor failed authentication attempts and report anomalies to [Organisation]
- Ensure MSP personnel use unique, non-shared credentials for [Organisation] access (ref: ISO 27001:2022 5.17)

### 3.3 Department Managers (Unità Operative)
- Ensure clinical and administrative staff complete mandatory password awareness training (within the allocated 2 hours/year)
- Immediately notify IT of staff departures to trigger password resets for shared accounts
- Enforce physical security of mobile devices (point-of-care tablets/smartphones)

### 3.4 All Users (Clinical, Administrative, Technical)
- Create, protect, and manage passwords in accordance with this policy
- Report suspected credential compromise immediately to IT/MSP helpdesk
- Use only [Organisation]-approved authentication methods; prohibit credential sharing

---

## 4. Policy Requirements

### 4.1 Password Strength Requirements

All passwords must meet the following minimum standards:

| Account Type | Minimum Length | Complexity | Maximum Age |
|---|---|---|---|
| Standard users (clinical/admin) | 12 characters | 3 of 4 categories* | 12 months |
| Privileged accounts (IT/MSP) | 16 characters | 3 of 4 categories* | 6 months |
| Service accounts | 20 characters | 3 of 4 categories* | 12 months** |
| Emergency break-glass | 16 characters | 3 of 4 categories* | 3 months |

\* Categories: Uppercase (A-Z), Lowercase (a-z), Digits (0-9), Special characters (!@#$%^&*)

**Service accounts used for automated processes only (no interactive login) may use longer passwords (20+ characters) without expiry if protected by compensating controls (network isolation, certificate-based authentication).

**Rationale:** Aligns with NIST SP 800-63B (memorized secret verifiers) and AGID recommendations for Public Administration. Length prioritised over arbitrary complexity to support clinical usability given high staff turnover and limited training time (2 hours/year).

### 4.2 Multi-Factor Authentication (MFA)

MFA is **mandatory** for:
- All remote access (VPN client-to-site) — ref: NIS2 Art. 21(2)(c)
- All privileged/administrative access to Active Directory, PACS, LIS, and network infrastructure
- Access to the Cartella Clinica Elettronica (FSE) from non-clinical workstations
- All MSP administrative access to [Organisation] systems

MFA should use:
- SPID/CIE for regional federation access (compliant with Italian eIDAS framework)
- TOTP (Time-based One-Time Password) or hardware tokens for local systems
- SMS-based OTP only as fallback for clinical emergency access, subject to risk acceptance

*Unsupported: NIST SP 800-63B discourages SMS-based 2FA, but permitted temporarily for legacy clinical kiosks unable to support authenticator apps, pending hardware refresh (see Exceptions).

### 4.3 Password Change Policy

**Mandatory changes required:**
- Default/vendor-supplied passwords must be changed immediately upon first login (ref: ISO 27001:2022 8.5)
- Temporary passwords set by IT/MSP must be changed at first login
- Suspected or confirmed compromise requires immediate password reset
- Shared passwords known to departing staff must be changed within 24 hours of departure notification (ref: ISO 27001:2022 5.17)

**Prohibited practices:**
- Password reuse: Systems must deny the last 5 passwords (configured in Active Directory)
- Passwords must not contain the username, ward name, or "Ospedale" variants
- Common passwords (top 1000 breached passwords) must be blocked via Active Directory Password Protection or equivalent

### 4.4 Brute Force Protection

All systems must implement account lockout:
- Lockout threshold: 5 failed attempts
- Lockout duration: 30 minutes
- Reset counter: 30 minutes

Critical systems (PACS, LIS, ADT) must alert the MSP/IT immediately upon lockout events to detect potential ransomware brute-force attempts (ref: NIST CSF 2.0 PR.AC-7).

### 4.5 Password Protection and Handling

- **No sharing:** Passwords are personal and non-transferable. Shared accounts (e.g., ward kiosk logins) are prohibited except where technically unavoidable (see §4.6).
- **No storage:** Passwords must not be stored in plain text, spreadsheets, browser auto-fill (unless enterprise-managed), or written on paper affixed to devices.
- **Approved managers:** Only [Organisation]-approved password managers (if deployed) or secure credential vaults managed by the MSP may be used for service accounts.
- **Transmission:** Passwords must never be sent via email, WhatsApp, or SMS. Temporary passwords may be communicated via secure voice (phone) or split-channel (SMS username, email password, or vice versa).

### 4.6 Shared and Service Accounts

Given the 35 legacy Windows clinical kiosks and high clinical turnover:

- **Generic ward accounts** (e.g., "MedicinaInterna01") are permitted **only** on legacy kiosks unable to support individual authentication, provided:
  - The account has minimal privileges (web access only, no local admin)
  - Password is changed every 30 days or upon any staff rotation in that ward
  - Screen locks after 5 minutes of inactivity requiring re-authentication
  - Physical access to the kiosk is controlled (ward-specific, non-public)
  - Documented in the ISMS exception register with target remediation date (individual accounts)

- **MSP service accounts** must:
  - Be identifiable with prefix (e.g., "MSP_")
  - Use unique credentials per technician (no shared "admin" accounts)
  - Be disabled when not in use (time-bound access)
  - Log all activities via privileged access management (PAM) if available, or at minimum via dedicated jump server with session recording

### 4.7 Emergency Access (Break-Glass)

For 24/7 clinical operations where patient safety is at risk:
- Emergency administrative accounts ("break-glass") must exist for critical systems (PACS, ADT, LIS)
- Credentials must be stored in a sealed envelope in the Direttore di Guardia (on-call manager) safe, with tamper-evident seals
- Use triggers immediate alert to IT Manager and MSP SOC
- Password must be changed immediately after use
- Usage logged in the incident register (ref: ISO 27001:2022 8.15)

---

## 5. Monitoring and Review

- **Compliance checks:** IT Manager/MSP verifies password policy configuration on all systems quarterly
- **Audit logs:** Failed login attempts and password changes on critical systems (FSE, PACS) retained for 12 months (ref: GDPR Art. 5(1)(f) accountability principle)
- **Metrics:** 
  - Percentage of accounts with MFA enabled (target: 100% for privileged, 80% for standard by end of year 1)
  - Number of shared accounts remaining (target: 0 by end of year 2, except break-glass)
  - Password policy violations reported

---

## 6. Exceptions

Exceptions to this policy require:
1. Written request to IT Manager documenting technical constraint (e.g., legacy medical device OS limitations)
2. Compensating controls (network isolation, enhanced monitoring, physical security)
3. Risk acceptance by Direttore Generale for high-risk exceptions
4. Entry in the ISMS exception register with review date (maximum 12 months)
5. Annual review of all exceptions with plan for remediation or upgrade

*Current known exceptions:* 35 legacy Windows clinical kiosks (target: replacement/upgrade within 24 months).

---

## 7. Enforcement

Non-compliance constitutes a breach of professional obligations under the Contratto Collettivo Nazionale (CCNL) for healthcare workers and may trigger disciplinary procedures:

| Severity | Examples | Consequence |
|---|---|---|
| Minor | Writing password on sticky note (first occurrence) | Verbal warning, mandatory refresher training |
| Moderate | Sharing credentials with colleague, failure to report suspected compromise | Written warning, suspension of remote access privileges |
| Severe | Deliberate circumvention of MFA, using generic accounts for unauthorized data access | Formal disciplinary action, potential suspension |
| Critical | Selling patient data credentials, ransomware infection via weak password | Immediate suspension, legal referral to Garante Privacy and law enforcement (Art. 616-bis CP for accesso abusivo) |

---

## 8. Related Documents

| Document ID | Title |
|---|---|
| POL-001 | Cybersecurity Policy |
| POL-002 | Access Control Policy |
| POL-004 | Backup and Recovery Policy |
| POL-008 | Cyber Incident Response Plan |
| Regional FSE Guidelines | Fascicolo Sanitario Elettronico — Security Requirements |

---

## 9. Definitions

| Term | Definition |
|---|---|
| **MFA** | Multi-Factor Authentication — two or more verification factors (knowledge, possession, inherence) |
| **Break-glass** | Emergency account for critical system access when standard authentication fails |
| **MSP** | Managed Service Provider — external IT support contractor |
| **SPID/CIE** | Sistema Pubblico di Identità Digitale / Carta di Identità Elettronica — Italian digital identity frameworks |
| **FSE** | Fascicolo Sanitario Elettronico — Electronic Health Record |
| **PACS** | Picture Archiving and Communication System (radiology) |
| **LIS** | Laboratory Information System |

---

## 10. Compliance and Regulatory References

- **NIS2 Directive (EU) 2022/2555** — Art. 21(2)(c) (multi-factor authentication for essential entities)
- **GDPR (EU) 2016/679** — Art. 32 (technical and organisational measures), Art. 5(1)(f) (integrity and confidentiality)
- **D.Lgs. 196/2003** (Codice Privacy) as amended by D.Lgs. 101/2018 — Art. 31 (security measures)
- **ISO/IEC 27001:2022** — Controls 5.17 (Authentication information), 8.2 (Privileged access rights), 8.5 (Secure authentication)
- **NIST SP 800-63B** — Digital Identity Guidelines: Authentication and Lifecycle Management (memorized secrets)
- **AGID Linee Guida per la sicurezza informatica nella PA** — Misure minime (password length, MFA for remote access)
- **Garante Privacy** — Provvedimenti specifici per il settore sanitario (health data protection)

---

## 11. Revision History

| Version | Date | Author | Description of Change |
|---|---|---|---|
| 1.0 | [DD/MM/YYYY] | [Responsabile del Servizio Informatico] | Initial release for NIS2 compliance and AGID alignment |

---

## 12. Approval

| Role | Name | Signature | Date |
|---|---|---|---|
| Policy Owner (Responsabile del Servizio Informatico) | | | |
| Approved by (Direttore Generale) | | | |
| Compliance Review (Privacy Officer/DPO) | | | |

---

*Sources consulted: ISO/IEC 27001:2022 Controls 5.17, 8.2, 8.5; NIST SP 800-63B; NIS2 Directive Art. 21; GDPR Art. 32; AGID Linee Guida per la sicurezza informatica nella PA; D.Lgs. 196/2003; CIS Controls v8 (Control 5 — Account Management).*
</policy>
