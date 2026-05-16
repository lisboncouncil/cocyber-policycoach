---
config: C2b
context_id: ctx-H
policy_id: P1
policy_name: Password Policy
policy_short: password
metadata:
  config: C2b
  model: deepseek-ai/DeepSeek-V3.2
  input_tokens: 25625
  output_tokens: 1407
  total_tokens: 27032
  latency_s: 37.875
  tool_calls:
  - rag_retrieval
  raw_provider_id: b4a96012-72f2-4223-b4b7-c97e81bd6170
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
answer_chars: 6301
generated_at_unix: 1778503463
---

<policy title="Password Policy">

| Field | Value |
|-------|-------|
| **Document ID** | POL-006 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Internal |
| **Owner** | IT Manager / CISO (to be designated) |
| **Approved by** | Chief Executive Officer (CEO) |
| **Approval date** | [DD/MM/YYYY] |
| **Next review date** | [DD/MM/YYYY] |
| **Review cycle** | Annual |

---

## 1. Purpose

This Password Policy establishes the requirements for creating, managing, and protecting passwords used to access the information systems of [Hospital Name], a public hospital operating under the Italian National Health Service (SSN). This policy is designed to protect the confidentiality, integrity, and availability of sensitive patient and operational data, in compliance with GDPR (EU 2016/679), the Italian Privacy Code (D.Lgs. 196/2003 as amended), and the AGID Minimum Security Measures for Public Administration. It aligns with the principles of ISO/IEC 27001:2022 and the NIST Cybersecurity Framework 2.0.

## 2. Scope

This policy applies to all employees, contractors, consultants, and third-party personnel who have access to the hospital’s information systems, including but not limited to:
- All clinical and administrative staff.
- IT and technical personnel.
- Third-party vendors with system access.
- All systems, including the Electronic Health Record (FSE), PACS/RIS, LIS, ADT, and pharmacy management systems.

## 3. Roles and Responsibilities

### 3.1 IT Manager / Designated Security Officer
- Responsible for the implementation and technical enforcement of this policy.
- Configures systems to enforce password standards.
- Reviews and audits compliance with this policy.

### 3.2 Department Heads
- Ensure staff within their department are aware of and comply with this policy.
- Report any suspected password or account compromises to IT immediately.

### 3.3 All Users
- Create and manage passwords in accordance with this policy.
- Never share credentials.
- Report any suspected security incidents or policy violations.

## 4. Policy Requirements

### 4.1 Password Creation and Strength
All passwords for [Hospital Name] systems must adhere to the following:
- **Minimum Length:** 12 characters for standard user accounts.
- **Complexity:** Must include characters from at least three of the following categories:
    - Uppercase letters (A-Z)
    - Lowercase letters (a-z)
    - Numbers (0-9)
    - Non-alphanumeric characters (e.g., !, @, #, $)
- **Prohibited:** Do not use easily guessable information (e.g., usernames, hospital/ward names, simple patterns).
- **Password Managers:** The use of the organization-approved password manager is **mandatory** for storing and generating strong, unique passwords for work-related accounts.

### 4.2 Password Change and History
- **Standard Users:** Passwords must be changed every 90 days.
- **Privileged Accounts (Admin, IT Staff):** Passwords must be changed every 60 days.
- **Password Reuse:** The system must prevent the reuse of the last 5 passwords.
- **First Login:** All temporary or initial passwords must be changed on first use.

### 4.3 Multi-Factor Authentication (MFA)
- **Requirement:** MFA is **mandatory** for all remote access (VPN, webmail, cloud applications) and for all privileged accounts (e.g., domain administrators, system administrators).
- **Clinical Systems:** MFA is required for all access to the Electronic Health Record (FSE) and PACS/RIS systems for users accessing from outside the hospital's secure network.

### 4.4 Password Protection and Handling
- **No Sharing:** Passwords must never be shared. This includes not writing them down on paper or in unsecured digital files.
- **No Defaults:** Default vendor passwords on any system or device must be changed immediately upon installation.
- **No Reuse:** Passwords used for [Hospital Name] systems must be unique and not used for any personal accounts.

### 4.5 Account Lockout and Monitoring
- **Account Lockout:** User accounts will be locked for 30 minutes after 5 consecutive failed login attempts within 15 minutes.
- **Inactivity:** User accounts will be automatically disabled after 90 days of inactivity.
- **Logging:** All authentication attempts (success and failure) for critical systems (FSE, PACS, ADT) must be logged and retained for 12 months.

## 5. Exceptions

Exceptions to this policy may be granted only with documented approval from the IT Manager and the designated Data Protection Officer (DPO). Exceptions are granted for a limited time and require a documented risk assessment and compensating controls (e.g., a system that cannot support 12-character passwords may require additional network segmentation).

## 6. Enforcement and Review

Violations of this policy may result in disciplinary action, up to and including termination of employment or contract, and may be reported to the relevant authorities in case of a data breach. This policy will be reviewed annually or following a significant security incident.

## 7. Compliance and Regulatory References

This policy is designed to ensure compliance with:
- **GDPR (EU 2016/679) - Art. 5, 25, 32:** Mandates appropriate technical and organizational measures to ensure data security, including the confidentiality and integrity of processing systems.
- **AGID Minimum Security Measures for Public Administration:** Adherence to technical rules for the security of digital data processing.
- **NIST Cybersecurity Framework (CSF) 2.0:** PR.AC-1 (Identities and credentials are managed for authorized users and devices), PR.AC-7 (Users, devices, and other assets are authenticated).
- **ISO/IEC 27001:2022 Annex A.9.4 (System and application access control):** Requirements for secure log-on procedures and password management.

## 8. Revision History

| Version | Date | Author | Description of Change |
|---|---|---|---|
| 1.0 | [DD/MM/YYYY] | IT Manager | Initial Release |

## 9. Approval

This policy has been reviewed and approved by:

**Policy Owner:** [Name, Title]
**Date:** [DD/MM/YYYY]

**Approved by:** [Name, Title]
**Date:** [DD/MM/YYYY]

---

*This policy is a component of [Hospital Name]'s Information Security Management System (ISMS). All personnel are responsible for understanding and complying with this policy.*

</policy>
