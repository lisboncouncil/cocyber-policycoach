---
config: C2b
context_id: ctx-M
policy_id: P1
policy_name: Password Policy
policy_short: password
metadata:
  config: C2b
  model: deepseek-ai/DeepSeek-V3.2
  input_tokens: 25842
  output_tokens: 1854
  total_tokens: 27696
  latency_s: 57.221
  tool_calls:
  - rag_retrieval
  raw_provider_id: 5ce7ed54-027e-4682-8bc5-72fefaeae35d
  chunks_retrieved: 5
  server_version: 1.3.4
sources_count: 2
sources:
- type: kb_source
  source: ./datadir-plus-templates/password_policy.docx
  title: ./datadir-plus-templates/password_policy.docx
- type: kb_source
  source: ./datadir-plus-templates/cybersecurity_policy_BASIC.docx
  title: ./datadir-plus-templates/cybersecurity_policy_BASIC.docx
prompt_chars: 6027
answer_chars: 8352
generated_at_unix: 1778503855
---

<policy title="NATO Multinational Detachment Password Policy">

| Field | Value |
|-------|-------|
| **Document ID** | POL-006 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | NATO RESTRICTED (NR) |
| **Owner** | Information Systems Security Manager (ISSM) |
| **Approved by** | Detachment Commander |
| **Approval Date** | [Date of Approval] |
| **Next Review Date** | [Date of Next Review] |
| **Review Cycle** | Annual (or upon significant change in NATO/National policy) |
| **Distribution** | NATO RESTRICTED (NR) |

---

## 1. Purpose

This Password Policy establishes the minimum requirements for the creation, management, and protection of passwords and other authentication secrets for all personnel (military, civilian, and contractor) assigned to or supporting the Multinational Detachment. This policy is designed to protect NATO and national information systems and data, from Unclassified to NATO SECRET, against unauthorized access. It enforces the principle of least privilege and supports compliance with NATO Security Policy (AC/35-D/1015), NATO INFOSEC directives, and host-nation (Romanian) cybersecurity law.

## 2. Scope

This policy applies to all personnel, including military, civilian, and contractor personnel, who require access to the Detachment’s information systems, including:
- NATO Unclassified (NU), NATO Restricted (NR), and NATO Secret (NS) systems.
- Coalition and National systems operated by the Detachment.
- All workstations, servers, network devices, and communication systems.
- All personnel must adhere to this policy regardless of classification domain (NU, NR, NS).

## 3. Roles and Responsibilities

| Role | Responsibilities |
| :--- | :--- |
| **Detachment Commander** | Ultimate accountability for policy enforcement and resource allocation. |
| **Information Systems Security Manager (ISSM)** | Policy implementation, compliance monitoring, and incident reporting. |
| **System/Network Administrators** | Enforce technical controls, manage password systems, and conduct audits. |
| **All Personnel** | Comply with policy, report suspected compromises, and complete mandatory training. |
| **Security Officer (SECO)** | Ensures physical and procedural security of COMSEC and authentication devices. |

## 4. Password and Authentication Policy Requirements

### 4.1. Password Creation and Strength
1.  **Length and Complexity**: All passwords must be a minimum of 15 characters. They must include at least three of the following four character sets: uppercase, lowercase, numbers, and special characters (e.g., `! @ # $ % & *`).
2.  **Prohibited Patterns**: Passwords must not contain dictionary words, common phrases, or predictable sequences (e.g., `Password123!`, `Qwerty!234`). Default and vendor-supplied passwords must be changed immediately upon system setup.
3.  **Password Managers**: The use of a NATO-approved password manager is mandatory for storing and generating strong, unique passwords for all systems. Master passwords for password managers must adhere to the strength requirements above.

### 4.2. Multi-Factor Authentication (MFA)
1.  **Mandatory MFA**: MFA is mandatory for all access to NATO SECRET (NS) and NATO RESTRICTED (NR) systems, and for all privileged/administrative accounts on any system.
2.  **MFA Methods**: The primary MFA method is the use of NATO-approved Common Access Card (CAC) or derived credentials on a PKI-enabled smart card (CAC/PIV). Hardware tokens (e.g., YubiKey) are required where smart cards are not feasible.
3.  **Backup Codes**: For contingency access, one-time-use backup codes must be generated, stored in a sealed envelope, and secured in the unit safe. Their use must be logged and reported to the ISSM.

### 4.3. Password Management
1.  **Password Changes**: Passwords for user accounts must be changed every 60 days for SECRET systems and every 90 days for UNCLASSIFIED/RESTRICTED systems. Service account passwords must be changed at least annually or upon any personnel change.
2.  **Password Reuse**: The system must prevent the reuse of the last 10 passwords.
3.  **Account Lockout**: Accounts will be locked for 30 minutes after 5 consecutive failed login attempts. Unlock requires administrator intervention.
4.  **Shared Accounts**: Shared accounts (e.g., service accounts) are prohibited. Where technically unavoidable (e.g., system-level service accounts), they require ISSM approval, a designated owner, and strict logging of use.
5.  **Password Storage**: Passwords must never be stored in plain text. Systems must store only salted, iterated, and cryptographically strong hashes (e.g., bcrypt, Argon2).

### 4.4. Classification-Specific Handling
1.  **NU/NR Systems**: Password length and complexity as per Section 4.1. MFA is strongly encouraged.
2.  **NS Systems**: In addition to the above, passwords for NS systems must be at least 20 characters and changed every 30 days. Physical token-based MFA is mandatory.
3.  **COMSEC/CRYPTO**: Password requirements for cryptographic systems are defined in separate COMSEC Local Operating Procedures (LOPs) and take precedence.

### 4.5. Physical and Procedural Security
1.  **No Plaintext Storage**: Passwords must not be written down. If a password must be temporarily recorded (e.g., for break-glass procedures), it must be stored in a sealed envelope in a GSA-approved safe.
2.  **No Sharing**: Passwords must never be shared, even with supervisors or IT staff. IT will never ask for your password.
3.  **Incident Reporting**: Any suspected password compromise (e.g., suspected shoulder surfing, lost token) must be reported to the ISSM and the Security Officer immediately.

## 5. Exceptions

1.  **Exception Process**: Any requirement of this policy may be waived only via a formal, time-limited exception granted by the ISSM. The request must include a risk assessment and compensating controls.
2.  **Legacy Systems**: Legacy or coalition partner systems that cannot technically comply with this policy require a formal risk acceptance memo from the Detachment Commander, reviewed annually.

## 6. Monitoring and Enforcement

1.  **Audit Logs**: All authentication attempts (success/failure) and password change events must be logged and retained for 365 days. Logs are reviewed weekly by the ISSM.
2.  **Compliance Audits**: The ISSM or designated auditor will conduct quarterly password policy audits using automated tools and log analysis.
3.  **Consequences for Non-Compliance**: Violations of this policy may result in disciplinary action, revocation of system access, and/or administrative or legal action in accordance with NATO and national regulations.

## 7. Training and Awareness

1.  All personnel will complete annual password and security awareness training.
2.  All new personnel will receive this training as part of their in-processing.

## 8. Related Documents and References

*   NATO Security Policy (C-M(2002)49 and successors)
*   AC/35-D/1015 (Security within NATO)
*   NATO INFOSEC Technical and Implementation Directives
*   AJP-3.20, Allied Joint Doctrine for Cyberspace Operations
*   Host Nation (Romanian) Cybersecurity Law 58/2019
*   NIST SP 800-63B (Digital Identity Guidelines)
*   This policy supersedes all previous password or authentication directives for this Detachment.

## 9. Revision History

| Version | Date | Author | Description of Change |
| :--- | :--- | :--- | :--- |
| 1.0 | [Draft Date] | ISSM | Initial Draft for Detachment Review |

---
**Approved by:**

**Detachment Commander** (Name, Rank, Date)

**Concurrence, Information Systems Security Manager (ISSM):** _________________________

**Concurrence, J6 Communications and Information Systems Officer:** _________________________

</policy>

**Sources Consulted (from provided context):**
*   *Password Policy (Basic) Template*: Provided the foundational structure and core password policy concepts (password length, change frequency, MFA encouragement).
*   *Cybersecurity Policy (Basic) Template*: Provided the high-level policy structure, roles and responsibilities, and the framework for integrating with other security documents (like the Access Control and Incident Response plans).
*   NATO and regulatory references are derived from the organizational profile provided (NATO Security Policy, AC/35-D documents, AJP-3.20, host-nation law).
