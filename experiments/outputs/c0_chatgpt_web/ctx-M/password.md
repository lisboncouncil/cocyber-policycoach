---
config: C0+web
context_id: ctx-M
policy_id: P1
policy_name: Password Policy
policy_short: password
metadata:
  config: C0+web
  model: gpt-4.1-2025-04-14
  input_tokens: 1658
  output_tokens: 2445
  total_tokens: 4103
  latency_s: 28.872
  tool_calls: []
  raw_provider_id: resp_0267e74359a048100069fb70ae7a78819387555a8075b6f057
sources_count: 0
sources: []
prompt_chars: 6027
answer_chars: 9130
generated_at_unix: 1778086091
---

---

# NATO Multinational Military Detachment  
**Password Policy**  
**Document Reference:** NMD-SEC-POL-003  
**Effective Date:** 2024-07-01  
**Policy Owner:** Information Systems Security Manager (ISSM, J6 chain)  
**Review Cycle:** Annual (every 12 months) or upon significant regulatory/operational change  
**Classification:** NATO UNCLASSIFIED (NU)  
**Language:** English  

---

## 1. Purpose

This policy establishes mandatory requirements and best practices for password management within the NATO Multinational Military Detachment (NMD) operating in Romania. The aim is to reduce the risk of unauthorised access to NATO and coalition CIS resources, mitigate insider and external threats, and ensure compliance with NATO, host-nation, and international security frameworks.

---

## 2. Scope

This policy applies to all NMD personnel (military, civilian, contractors), accounts, and information systems within the operational control of the detachment—covering all classification domains (NU, NR, NS, MISSION SECRET). It governs authentication to all CIS, including but not limited to: workstations, servers, cross-domain solutions (CDS), network devices, applications, and COMSEC management systems.

---

## 3. Roles and Responsibilities

- **ISSM (Policy Owner):** Maintains and enforces this policy; reviews and updates as per cycle.
- **Security Staff (J6):** Implements controls, monitors compliance, and investigates incidents.
- **System Administrators:** Enforce technical controls, respond to password-related incidents, and support user onboarding/offboarding.
- **All Users:** Adhere to password requirements and report suspected compromise or policy violations.
- **Contractor Managers:** Ensure contract staff comply with all controls and receive appropriate training.

---

## 4. Policy Principles

- **Defence in Depth:** Password controls are part of a layered authentication strategy, including PKI, smart card, and multifactor authentication (MFA) as mandated by domain/classification.
- **Least Privilege and Need-to-Know:** Passwords grant access solely to resources required by the user’s role and clearance.
- **Compliance:** Align with NATO, host-nation, and international frameworks (see references).
- **Auditable Enforcement:** All controls must be technically and procedurally auditable.
- **Operational Realism:** Requirements reflect the detachment’s operational tempo and multinational staffing.

---

## 5. Requirements and Controls

### 5.1. General

- **Password use is mandatory** for all authentication where PKI/smart card is not enforced by system design.  
  **Sources:** [NATO C-M(2002)49, AC/322-D(2017)0009, NIST CSF PR.AC-1, ISO/IEC 27001:2022 A.5.15]

### 5.2. Password Complexity and Length

- **Minimum password length:**  
  - All domains: **15 characters** (NATO SECRET and above), **12 characters** (NU/NR).  
    *[NIST SP 800-63B §5.1.1.2, ISO/IEC 27001:2022 A.5.15, NATO INFOSEC]*
- **Composition:**  
  - Passwords must not require arbitrary complexity (e.g., mix of upper/lowercase, digits, symbols), but must not allow commonly used, dictionary, or context-specific words (e.g., “NATO2024!”, “Romania123”).  
    *[NIST SP 800-63B §5.1.1.2, ISO/IEC 27001:2022 A.5.15]*
- **Prohibited passwords:**  
  - Passwords must be screened against a dynamic deny-list of known compromised, dictionary, and context-specific weak passwords.  
    *[NIST SP 800-63B §5.1.1.2]*

### 5.3. Password Change and Reuse

- **Change on suspicion or compromise:**  
  - Immediate password change is required upon suspected or confirmed compromise.  
    *[NIST CSF PR.AC-7, NATO C-M(2002)49]*
- **No forced periodic change:**  
  - Routine periodic password changes (e.g., every 90 days) are NOT required unless mandated by higher authority, except for accounts where technical constraints preclude other mitigations.  
    *[NIST SP 800-63B §5.1.1.2, ISO/IEC 27001:2022 A.5.15]*
- **Reuse prohibition:**  
  - Users may not reuse their last 10 passwords.  
    *[ISO/IEC 27001:2022 A.5.15]*
- **Initial/temporary passwords:**  
  - Must be single-use, set to expire upon first use, and delivered securely (not via email).  
    *[NATO INFOSEC, NIST CSF PR.AC-1]*

### 5.4. Multifactor Authentication (MFA)

- **Mandatory for all NR, NS, and MISSION SECRET domains:**  
  - Passwords must always be combined with smart-card or equivalent PKI token.  
    *[NATO AC/322-D(2017)0009, NIST CSF PR.AC-7]*
- **NU domain:**  
  - MFA required for privileged access, remote access, and where technically feasible for all users.  
    *[NIST CSF PR.AC-7, ISO/IEC 27001:2022 A.5.15]*

### 5.5. Storage and Protection

- **Hashing and salting:**  
  - All stored passwords must be protected with industry-standard cryptographic hashing and unique salt per credential.  
    *[ISO/IEC 27001:2022 A.8.12, NIST SP 800-63B §5.1.1.2]*
- **No plaintext storage:**  
  - Passwords must never be stored or transmitted in plaintext.  
    *[ISO/IEC 27001:2022 A.8.12]*

### 5.6. Account Lockout and Throttling

- **Lockout after 10 failed attempts:**  
  - Accounts are locked for a minimum of 15 minutes or until administrative reset after 10 failed login attempts.  
    *[NIST SP 800-63B §5.2.2, ISO/IEC 27001:2022 A.5.16]*
- **Progressive delays:**  
  - For non-critical systems, implement progressive delay (throttling) after each failed attempt to discourage brute-force attacks.  
    *[NIST SP 800-63B §5.2.2]*

### 5.7. Password Sharing and Delegation

- **No password sharing:**  
  - Passwords are individual credentials; sharing is strictly forbidden.  
    *[ISO/IEC 27001:2022 A.5.15, NATO C-M(2002)49]*
- **Delegated access:**  
  - Where delegation is required, use technical delegation (e.g., privilege separation) not credential sharing.  
    *[ISO/IEC 27001:2022 A.5.15]*

### 5.8. Administrative and Privileged Accounts

- **Privileged account passwords:**  
  - Must be generated randomly (minimum 20 characters), rotated after each use where possible, and protected by MFA at all times.  
    *[ISO/IEC 27001:2022 A.8.2, NIST CSF PR.AC-4]*

### 5.9. End-User Support

- **Self-service reset:**  
  - Provide secure self-service password reset mechanisms, requiring identity verification (e.g., smart card, in-person, or secure secondary channel).  
    *[ISO/IEC 27001:2022 A.5.15, NIST SP 800-63B §5.1.1.2]*
- **Assisted reset:**  
  - For users unable to use self-service, identity must be verified by security-cleared personnel before reset.  
    *[ISO/IEC 27001:2022 A.5.15]*

### 5.10. Training and Awareness

- **Annual training:**  
  - All users must complete annual cyber hygiene training, including secure password practices, as part of the NMD cybersecurity training requirement (minimum 40 hours/year).  
    *[NATO Cyber Defence Pledge 2016, ISO/IEC 27001:2022 A.6.3]*

### 5.11. Compliance with Host-Nation and GDPR

- **Personal data protection:**  
  - Where user passwords or reset data are considered personal data under GDPR, ensure compliance with data minimisation, storage limitation, and access control principles.  
    *[GDPR Art. 5, Art. 32]*

---

## 6. Exceptions

- **Authorisation:**  
  - Exceptions to this policy require documented risk assessment and explicit approval from the ISSM and the detachment commander (or delegate), with notification to the NATO CIS Security Accreditation Authority.
- **Legacy Systems:**  
  - Where technical constraints preclude compliance, compensating controls (e.g., increased monitoring, air-gapping) must be implemented and documented.
- **National Caveats:**  
  - Where a framework nation or coalition partner imposes stricter controls, the higher standard will apply for affected systems and users.

---

## 7. Monitoring and Review

- **Monitoring:**  
  - The Security Operations Centre (SOC) shall continuously monitor for password-related security events (e.g., brute force, account lockout, credential stuffing), and issue alerts per the Incident Response Plan (NCIRC alignment).  
    *[NIST CSF DE.CM-7, NATO C-M(2002)49]*
- **Audit:**  
  - Quarterly audits of password policy compliance will be conducted by the J6 security staff, with results reported to the ISSM and detachment leadership.
- **Review:**  
  - This policy will be reviewed at least annually or upon significant regulatory or operational change.

---

## 8. References

- **NATO Policies:**  
  - C-M(2002)49: NATO Information Security Policy  
  - AC/322-D(2017)0009: NATO INFOSEC Technical and Implementation Directive  
  - AC/35-D/1015, AC/35-D/1029: NATO Personnel and Physical Security  
  - Allied Joint Doctrine for Cyberspace Operations (AJP-3.20)
- **Host-Nation/Legal:**  
  - Romanian Cybersecurity Law 58/2019 (NIS/NIS2)  
  - GDPR (Regulation (EU) 2016/679), esp. Articles 5, 32  
  - NATO SOFA
- **International Standards:**  
  - NIST CSF 2.0 (esp. PR.AC-1, PR.AC-7, PR.AC-4, DE.CM-7)  
  - NIST SP 800-63B Digital Identity Guidelines  
  - ISO/IEC 27001:2022 (esp. A.5.15, A.5.16, A.8.2, A.8.12, A.6.3)
- **Other:**  
  - NATO Cyber Defence Pledge 2016

---

**Approved:**  
ISSM (NMD, J6)  
Date: 2024-07-01

---
