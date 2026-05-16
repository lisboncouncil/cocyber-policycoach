---
config: C0
context_id: ctx-M
policy_id: P1
policy_name: Password Policy
policy_short: password
metadata:
  config: C0
  model: gpt-4.1-2025-04-14
  input_tokens: 1364
  output_tokens: 2446
  total_tokens: 3810
  latency_s: 58.284
  tool_calls: []
  raw_provider_id: chatcmpl-DcZb3EWu8wal14d5xJmjQsPBPd8eN
sources_count: 0
sources: []
prompt_chars: 6027
answer_chars: 9452
generated_at_unix: 1778085727
---

---
**Organisation:** NATO Multinational Military Detachment (Romania)  
**Policy Title:** Password Policy  
**Effective Date:** 2024-07-01  
**Policy Owner:** Information Systems Security Manager (ISSM), J6 Chain  
**Review Cycle:** Annual or upon regulatory/operational change  
---

## 1. Purpose

This policy establishes mandatory requirements for password selection, use, management, and protection across all NATO, coalition, and host-nation information systems operated by the detachment. It aims to ensure compliance with NATO, host-nation, and international security standards, mitigate cyber threats, and enforce strict separation between classification domains in line with operational and legal obligations.

---

## 2. Scope

This policy applies to all personnel (military, NATO civilian, and cleared contractors) who access, administer, or manage CIS assets, applications, and networks at all classification levels (NU, NR, NS, MISSION SECRET) under the detachment’s operational control. It covers:

- User and administrative accounts
- End-user devices and workstations
- Network infrastructure components
- Cross-domain solutions and COMSEC equipment with password controls
- Any system that authenticates via password or passphrase  
Excluded: Systems using only hardware tokens with no password fallback, or cryptographic systems secured by other controls (e.g., dual-key with no password element).

---

## 3. Roles and Responsibilities

| Role                            | Responsibilities                                                                                                 |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------|
| ISSM (Information Systems Security Manager) | Policy ownership, periodic review, compliance oversight, exceptions approval, audit coordination             |
| CIS/IT Administrators            | Implementation of controls, password system configuration, local enforcement, privileged account management     |
| Security Staff (25 FTE)          | Monitoring, auditing, incident response, user awareness training, policy enforcement                            |
| All Users                        | Adherence to all password requirements, prompt reporting of suspected compromise or policy violation            |
| Contractors (Vetted)             | Compliance as per SOFA, GDPR, and host-nation requirements                                                      |
| Host-Nation Liaison Officer      | Coordination of cross-jurisdictional compliance (GDPR, Romanian CSL), escalation of legal issues                |

---

## 4. Principles

- **Defence-in-Depth:** Passwords are one component of layered access control, enforced alongside PKI, smartcards, and need-to-know restrictions.  
  *(Ref: AC/322-D(2017)0009, NIST CSF PR.AC-1)*

- **Classification Domain Separation:** Password management and storage must not allow spillage or cross-domain compromise.  
  *(Ref: C-M(2002)49, AJP-3.20, NATO INFOSEC)*

- **Risk-Based Controls:** Password strength and lifecycle controls are proportional to system sensitivity and threat environment.  
  *(Ref: NIST SP 800-53 Rev 5, ISO/IEC 27001:2022 A.5.17, A.8.2.3)*

- **Privacy by Design:** User credential data must be protected in accordance with GDPR and host-nation law.  
  *(Ref: GDPR Art. 25, Romanian CSL)*

---

## 5. Requirements and Controls

### 5.1. Password Composition and Complexity

- **Minimum Length:**  
  - All user passwords: ≥14 characters  
    *(Ref: NIST SP 800-63B §5.1.1.2, ISO/IEC 27002:2022 8.3.3, AC/322-D(2017)0009 §20)*
  - Administrative/privileged accounts: ≥20 characters (passphrase recommended)  
    *(Ref: NIST SP 800-53 IA-5, NATO INFOSEC)*

- **Character Set:**  
  No mandatory complexity (upper/lower/digit/symbol) if minimum length met, but users are encouraged to use a mix. For systems not supporting long passwords, enforce at least three character classes.  
  *(Ref: NIST SP 800-63B §5.1.1.2, ISO/IEC 27002:2022 8.3.3)*

- **Prohibited Passwords:**  
  - Disallow passwords from a list of the top 10,000 known breached passwords (updated quarterly).  
    *(Ref: NIST SP 800-63B §5.1.1.2, ISO/IEC 27002:2022 8.3.4)*
  - Screen against obvious, context-specific words (e.g., “NATO”, “Romania”, system names, user name, rank, or detachment identifiers).  
    *(Ref: ISO/IEC 27002:2022 8.3.4)*

### 5.2. Password Lifecycle

- **Expiration:**  
  - No periodic (time-based) expiry for user accounts unless compromise is suspected or system risk assessment dictates.  
    *(Ref: NIST SP 800-63B §5.1.1.2, ISO/IEC 27002:2022 8.3.4)*  
  - Administrative/privileged accounts: 180-day maximum validity, or upon change of assignee.  
    *(Ref: NIST SP 800-53 IA-5, NATO INFOSEC)*

- **Change on Compromise:**  
  Immediate reset required upon evidence or strong suspicion of compromise, spillage, or loss of control.  
  *(Ref: NIST CSF DE.CM-7, NATO IRP/NCIRC SOP)*

- **Reuse Restrictions:**  
  - Minimum password history: 10 previous passwords disallowed.  
    *(Ref: ISO/IEC 27002:2022 8.3.4)*
  - No reuse of passwords across different classification domains or systems.  
    *(Ref: NATO INFOSEC, C-M(2002)49)*

### 5.3. Password Storage and Transmission

- **Storage:**  
  - All passwords must be stored using salted, strong, cryptographic hashing (e.g., bcrypt, PBKDF2, Argon2).  
    *(Ref: NIST SP 800-63B §5.1.1.2, ISO/IEC 27002:2022 8.3.2)*
  - Never store passwords in plaintext or reversible encryption.

- **Transmission:**  
  - Passwords must not be transmitted in cleartext; enforce encrypted protocols (TLS 1.2+).  
    *(Ref: ISO/IEC 27002:2022 8.3.2, NIST SP 800-53 SC-8/SC-13)*

### 5.4. Password Sharing and Disclosure

- **Prohibition:**  
  - Password sharing is strictly prohibited except for emergency break-glass accounts (with auditable two-person integrity).  
    *(Ref: NATO INFOSEC, AC/35-D/1029, ISO/IEC 27002:2022 8.3.5)*
  - All emergency disclosures must be logged and reported to ISSM.

### 5.5. Authentication Methods

- **Multi-Factor Authentication (MFA):**  
  - MFA (smartcard + PIN/password) is mandatory for all NS, MISSION SECRET, and privileged accounts.  
    *(Ref: AC/322-D(2017)0009 §21, NIST CSF PR.AC-7, ISO/IEC 27002:2022 8.4.2)*
  - Single-factor authentication is only permitted for systems with explicit risk acceptance and ISSM approval.

### 5.6. Password Entry and Lockout

- **Failed Attempts:**  
  - User accounts: Lock after 5 unsuccessful attempts; unlock via helpdesk or automated process with identity verification.  
    *(Ref: ISO/IEC 27002:2022 8.3.5, NIST SP 800-53 AC-7)*
  - Admin/privileged accounts: Lock after 3 failed attempts; unlock only via ISSM or delegated authority.

- **Obscured Entry:**  
  - Passwords must not be displayed in cleartext during entry.  
    *(Ref: ISO/IEC 27002:2022 8.3.2)*

### 5.7. Password Reset Procedures

- **User-Initiated Reset:**  
  - Must verify identity via second factor (smartcard, PKI, biometric) or direct supervisor validation.  
    *(Ref: NIST SP 800-63B §5.1.1.2, ISO/IEC 27002:2022 8.3.5)*

- **Admin Reset:**  
  - Temporary passwords must be unique, expire within 24 hours, and require immediate change on first use.

### 5.8. System/Service Accounts

- **Random, High-Entropy Passwords:**  
  - Generated and stored securely; not to be known or used by any individual unless operationally required and logged.  
    *(Ref: ISO/IEC 27002:2022 8.3.4, NIST SP 800-53 IA-5)*

- **Rotation:**  
  - Rotate immediately on personnel change or suspected compromise.

---

## 6. Exceptions

- Exceptions may only be granted in writing by the ISSM, following risk assessment, and must be time-bound with compensating controls.  
  *(Ref: ISO/IEC 27001:2022 A.6.5)*

- All exceptions must be logged, periodically reviewed, and reported through the J6 chain to higher NATO authority if required.

---

## 7. Monitoring and Review

- **Monitoring:**  
  - The SOC and security staff will audit password-related events (creation, reset, failed login, lockout, and suspected compromise) in accordance with NATO CIRC and NCIRC guidance.  
    *(Ref: NIST CSF DE.CM-7, ISO/IEC 27002:2022 8.16.1)*

- **Review:**  
  - Policy effectiveness will be reviewed annually and after every red-team engagement, major incident, or regulatory change.  
    *(Ref: ISO/IEC 27001:2022 A.10.1, NATO INFOSEC)*
  - Training and awareness outcomes will be assessed as part of the annual training cycle (minimum 40 hours/staff/year).

---

## 8. References

- **NATO:**  
  - NATO Information Security Policy (C-M(2002)49)  
  - AC/322-D(2017)0009 – NATO INFOSEC Technical and Implementation Directive  
  - Allied Joint Doctrine for Cyberspace Operations (AJP-3.20)  
  - AC/35-D/1015, AC/35-D/1029

- **Host Nation and EU:**  
  - Romanian Cybersecurity Law (Law 58/2019; NIS/NIS2)  
  - GDPR (EU 2016/679)  
  - NATO SOFA

- **International Standards:**  
  - NIST SP 800-63B Digital Identity Guidelines  
  - NIST SP 800-53 Revision 5  
  - NIST CSF 2.0  
  - ISO/IEC 27001:2022, ISO/IEC 27002:2022

- **Other:**  
  - NATO Cyber Defence Pledge 2016  
  - Bilateral/multilateral information sharing agreements

---

**Document Control:**  
Approved by: ISSM, NATO Detachment J6  
Distribution: All personnel, security staff, contractors  
Classification: UNCLASSIFIED (for policy distribution only)  
---
