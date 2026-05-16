---
config: C0
context_id: ctx-H
policy_id: P1
policy_name: Password Policy
policy_short: password
metadata:
  config: C0
  model: gpt-4.1-2025-04-14
  input_tokens: 1144
  output_tokens: 2184
  total_tokens: 3328
  latency_s: 21.672
  tool_calls: []
  raw_provider_id: chatcmpl-DcZZFjOYspDqHZzCmJiEieGnpkcxl
sources_count: 0
sources: []
prompt_chars: 4657
answer_chars: 8609
generated_at_unix: 1778085578
---

---

# Password Policy

**Organisation**: [REDACTED] Provincial Public Hospital, Italy  
**Effective Date**: 2024-07-01  
**Policy Owner**: Head of IT (Responsabile dei Sistemi Informativi), with external MSP support  
**Review Cycle**: Annual, or upon major regulatory/technical change  
**Approved by**: Hospital Director (Direttore Sanitario)  
**Version**: 1.0

---

## 1. Purpose

This Password Policy defines the requirements for the creation, use, management, and protection of passwords for all systems and services operated or managed by [REDACTED] Provincial Public Hospital (“the Hospital”). The purpose is to reduce the risk of unauthorised access to critical systems and sensitive data, ensure compliance with Italian and EU regulations (GDPR, NIS2, Codice Privacy, AGID), and align with recognised international standards (ISO/IEC 27001:2022, NIST CSF 2.0) in a hospital environment with 24/7 clinical operations.

---

## 2. Scope

This policy applies to:  
- All Hospital staff (clinical, administrative, technical, and contract/outsourced staff)  
- All accounts (user and system) on Hospital IT systems, including but not limited to:  
  - On-premises and cloud-based systems  
  - Regional identity federation (SPID/CIE)  
  - Electronic Health Record (EHR), PACS/RIS, LIS, ADT, Pharmacy  
  - Workstations, mobile devices, and clinical kiosks  
  - Systems managed by the MSP under contract  
- Any other system processing hospital data within the Hospital’s responsibility

---

## 3. Roles and Responsibilities

| Role                              | Responsibilities                                                                                              |
|------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Hospital Director                  | Approves the policy and ensures organisational compliance                                                    |
| Head of IT (Int. + MSP)            | Implements and enforces the policy, manages exceptions, monitors compliance                                  |
| Outsourced MSP                     | Implements technical controls, supports compliance monitoring, supports incident response                    |
| All Employees and Contractors      | Comply with password practices, participate in training, report suspected compromise                         |
| HR/Onboarding (with IT)            | Ensures new users receive password guidance at induction, disables accounts on exit or role change           |

---

## 4. Principles

- **Data Protection**: Passwords are a primary safeguard for personal and health data, supporting GDPR Art. 32 and Codice Privacy (D.Lgs. 196/2003, Art. 31-34).
- **Risk-Based**: Controls are proportional to the criticality of systems and data (ISO/IEC 27001:2022, A.9.2.1, NIST CSF PR.AC-1).
- **Usability**: Controls are designed to balance security with clinical workflow and emergency access needs (Linee Guida AGID, NIS2).
- **Minimum Privilege**: Accounts and passwords grant only necessary access (ISO/IEC 27001:2022, A.9.1.2).
- **Continuous Improvement**: Controls are reviewed in light of evolving threats and regulatory requirements.

---

## 5. Requirements and Controls

**5.1 Password Creation**

- **Length & Complexity**
  - Minimum length: 12 characters for all accounts, except where technical or vendor limitations apply (NIST SP 800-63B §5.1.1, ISO/IEC 27001:2022 A.9.3.1).
  - No mandatory complexity (special characters, upper/lowercase) required if length is met (NIST SP 800-63B §5.1.1.2), but users are encouraged to use passphrases.
  - For legacy clinical kiosks (Windows systems unable to support 12+ characters): minimum length 8 characters; complexity enabled if supported. (Exception noted; see §7.)

- **Prohibited Passwords**
  - Common, easily guessed, and breached passwords (e.g. “Password123”, local hospital name) are blocked via technical means where supported (NIST SP 800-63B §5.1.1.2, AGID Misure minime 7.2).
  - Passwords must not contain user’s name, username, or easily associated personal data.

**5.2 Password Change and Expiry**

- **Change on Compromise**: Immediate password reset required if compromise is suspected/reported (NIST CSF DE.CM-7, ISO/IEC 27001:2022 A.5.17).
- **Periodic Expiry**:
  - General users: No forced periodic expiry unless evidence of compromise (NIST SP 800-63B §5.1.1.2, AGID Misure minime 7.2; supported).
  - Privileged/admin accounts: Change at least every 180 days, and after any role/personnel change (ISO/IEC 27001:2022 A.9.4.3).
- **Initial Passwords and Resets**: Must be changed at first login. Temporary passwords to be delivered securely, expire after 24 hours (ISO/IEC 27001:2022 A.9.2.4).

**5.3 Password Storage and Handling**

- **User Responsibility**: Passwords must never be shared, written down in accessible locations, or stored in plaintext (ISO/IEC 27001:2022 A.9.3.2).
- **Technical Storage**: All passwords stored in IT systems must be hashed and salted using industry-standard algorithms (ISO/IEC 27001:2022 A.10.1.1, AGID Misure minime 7.2).
- **Password Managers**: Use of centrally approved password managers is permitted/recommended for privileged accounts; guidance to be provided by IT. (Unsupported in ISO/IEC 27001:2022; recommended by NIST.)

**5.4 Authentication Mechanisms**

- **Multi-Factor Authentication (MFA)**:
  - Required for remote/VPN access and privileged accounts wherever feasible (NIS2 Art. 21, NIST CSF PR.AC-7, AGID Misure minime 7.3).
  - MFA for EHR/FSE, PACS, and ADT to be implemented as supported by vendor/regional platform (GDPR Art. 32; NIS2).
  - Where MFA is technically not possible, strengthen monitoring and logging.

**5.5 Account Lockout and Recovery**

- **Lockout**: After 10 failed attempts, account is locked for at least 15 minutes or until reset by IT/MSP (NIST SP 800-63B §5.2.2, AGID Misure minime 7.2).
- **Self-Service Recovery**: Password reset functionality must include identity verification (e.g., SPID/CIE, in-person, or secure contact with IT). (ISO/IEC 27001:2022 A.9.2.4)

**5.6 Training and Awareness**

- Mandatory password hygiene training for all staff at induction and annually (minimum 1 hour/year; ISO/IEC 27001:2022 A.6.3, AGID Misure minime 13.1).
- Training content must be tailored to clinical and administrative contexts, covering phishing, social engineering, and reporting compromised credentials.

**5.7 Privileged and Service Accounts**

- Privileged accounts (administrators, MSP staff, system operators) must have unique, strong passwords and, where possible, be restricted from daily use (ISO/IEC 27001:2022 A.9.2.3).
- Service/application accounts: Passwords must meet technical minimums and be changed annually, or upon staff/vendor change.

---

## 6. Exceptions

- **Legacy Systems**: Where vendor or system constraints prevent compliance (e.g., legacy Windows kiosks), document the limitation, apply compensating controls (network segmentation, monitoring), and seek upgrade or replacement as part of IT planning (ISO/IEC 27001:2022 A.8.1.3).
- **Clinical Emergency**: In clinical emergencies, patient safety takes precedence. Emergency access (“break glass”) mechanisms must be logged and reviewed by IT post-incident, in accordance with Garante Privacy guidance (Provvedimento 2015/331).

All exceptions must be authorised by the Head of IT in writing, with periodic review.

---

## 7. Monitoring and Review

- Compliance is monitored by the IT team and MSP via periodic account audits and password policy enforcement checks (ISO/IEC 27001:2022 A.12.7.1).
- Incidents and suspected breaches are handled per the Incident Response Policy; password-related incidents must be reviewed for policy effectiveness (NIS2, AGID, ISO/IEC 27001:2022 A.16.1.1).
- The policy is reviewed at least annually, and after major incidents or regulatory changes.

---

## 8. References

- **EU Regulation 2016/679 (GDPR)**, Art. 32
- **D.Lgs. 196/2003 (Codice Privacy)**, as amended by D.Lgs. 101/2018
- **Directive EU 2022/2555 (NIS2)**, Art. 21, Annex II
- **AGID Misure Minime per la Sicurezza ICT nella PA** (2017), §7.2, §7.3, §13.1
- **Linee Guida AGID per la sicurezza informatica nella PA**
- **Provvedimenti Garante Privacy in Sanità** (e.g. Provv. 2015/331)
- **ISO/IEC 27001:2022** (esp. A.5.17, A.6.3, A.8.1.3, A.9.2.1–A.9.4.3, A.10.1.1, A.12.7.1, A.16.1.1)
- **NIST Cybersecurity Framework (CSF) 2.0** (PR.AC-1, PR.AC-7, DE.CM-7)
- **NIST SP 800-63B** (Digital Identity Guidelines) §5.1.1, §5.2.2

---

**End of Policy**
