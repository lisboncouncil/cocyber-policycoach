---
config: C1
context_id: ctx-M
policy_id: P1
policy_name: Password Policy
policy_short: password
metadata:
  config: C1
  model: gpt-4.1
  input_tokens: 6610
  output_tokens: 3157
  total_tokens: 9767
  latency_s: 38.549
  tool_calls: []
  raw_provider_id: run_5u4mDfl099uOgFmHbP1yxCcz
  run_status: completed
  thread_id: thread_aGWAa88lls9z6hXV8TEqmgrg
sources_count: 0
sources: []
prompt_chars: 6027
answer_chars: 13262
generated_at_unix: 1778086354
---

<policy title="Password Policy">

---

## POLICY HEADER BLOCK

**Organization:** NATO Multinational Military Detachment (deployed, Romania)  
**Effective Date:** [To be assigned – YYYY-MM-DD]  
**Policy Owner:** Information Systems Security Manager (ISSM, J6)  
**Review Cycle:** Annual or on change in regulatory framework/command

---

## 1. PURPOSE

This Password Policy establishes requirements for the creation, use, management, and protection of authentication secrets—including passwords and PINs—across all classification domains of the NATO military detachment deployed in Romania. The policy ensures robust access control in compliance with NATO Information Security Policy (C-M(2002)49 and successors), relevant host-nation and EU law (Romanian Cybersecurity Law, NIS2, GDPR), and technical best practices from NIST CSF 2.0, ISO/IEC 27001:2022, and AC/322-D(2017)0009. The objective is to mitigate unauthorized access, insider threat, and credential compromise, while supporting coalition interoperability and national caveat obligations.

---

## 2. SCOPE

This policy applies to:
- All military, NATO civilian, and cleared contractor personnel assigned to or supporting the Detachment
- All information systems, networks, and CIS equipment (NU, NR, NS, MISSION SECRET domains)
- All accounts, including system, service, privileged, and user accounts
- All authentication systems: PKI/smart card, local/enterprise passwords, PINs, fallback secrets
- Cross-domain transfer mechanisms and mission partner environments (MPEs)
- NATO-provided, framework nation, host-nation, and coalition equipment/infrastructures

---

## 3. ROLES AND RESPONSIBILITIES

### 3.1 Detachment Commander
- Holds final accountability for the enforcement of this policy
- Approves exceptions and emergency access under operational exigency
- Ensures resources for secure authentication management

### 3.2 Information Systems Security Manager (ISSM, J6)
- Oversees policy implementation and updates
- Ensures alignment with NATO, host-nation, and EU directives
- Coordinates compliance monitoring and incident response

### 3.3 Section Chiefs / Mission Leads
- Ensure subordinate personnel comply with policy
- Enforce privileged account restrictions within domain
- Support audit and training processes

### 3.4 SOC & Security Operations Staff
- Monitor for password compromise, brute-force attempts, or anomalous logins
- Enforce controls on password change and recovery mechanisms
- Escalate detected non-compliance per IR plan

### 3.5 All Users (Military, Civilian, Contractor)
- Comply with password controls for assigned accounts and systems
- Promptly report suspected compromise or policy violations
- Complete annual authentication security training

---

## 4. POLICY PRINCIPLES

### 4.1 Defense in Depth for Authentication
Passwords are enforced as part of a layered authentication strategy that prioritizes PKI/smart card where feasible and ensures passwords function as a resilient fallback. Controls scale with classification domain, risk, and threat actor profile.
*(NATO C-M(2002)49, AC/322-D(2017)0009, NIST CSF PR.AC-1)*

### 4.2 Principle of Least Privilege
Authentication secrets are unique per user, mapped to explicit mission/role-based access, following default-deny. Service and admin accounts are tightly controlled, minimizing attack surface.
*(ISO 27001:2022 A.5.15, NIST CSF PR.AC-4)*

### 4.3 Separation of Classification Domains
No password reuse or sharing is permitted across different security classification levels (e.g., NS, NR, NU, MISSION SECRET). Controls and complexity requirements are scaled accordingly.
*(NATO AC/322-D(2017)0009, C-M(2002)49, Romanian CSL 2019)*

### 4.4 Continuous Improvement Based on Threat Intel
Password controls are updated in response to threat intelligence, vulnerability reporting (NCSC/NCIRC), and red-team findings.
*(NIST CSF ID.RA-1, NATO CIRC IR processes)*

---

## 5. POLICY REQUIREMENTS

### 5.1 General Authentication Requirements

**Control:** Passwords are mandatory for all accounts not using certificate-based authentication; fallback or backup secrets must meet equivalent security standards.  
**Reference:** AC/322-D(2017)0009 Sect. 6.3, NIST CSF PR.AC-7, ISO 27001 A.5.15

---

### 5.2 Password Complexity

- Minimum length: 
  - NU: 12 characters (enforced system-side)
  - NR/NS/MISSION SECRET: 15 characters
- Blacklist: Prohibit common dictionary words, previously compromised credentials, service-related terms, names, and known NATO terms
- Required character set: enforce minimum three of four types (uppercase, lowercase, number, symbol)
- Support long passphrases (encourage >20-character phrases)
- Complexity rules reviewed at least annually or per threat intelligence

**Reference:** NIST SP 800-63B §5.1.1, ISO 27001 A.5.15, NATO AC/322-D(2017)0009, Romanian CSL Art. 23

---

### 5.3 Password Lifetime and Rotation

- Maximum password validity: 365 days (NU), 180 days (NR/NS/SECRET)
- Immediate reset required upon role change, revocation, or compromise
- Prohibit forced rotation except for compromise/privilege elevation; align with NIST guidance to prevent unnecessary user fatigue
- Prevent reuse of previous 10 passwords per account

**Reference:** NIST SP 800-63B §5.1.1.2, NATO AC/322-D(2017)0009, ISO 27001 A.5.15

---

### 5.4 Privileged Account Controls

- Local admin/service accounts: passwords changed every 90 days or upon personnel change
- No shared or group accounts unless authorized by ISSM; use role-based objects wherever feasible
- Enable multi-factor authentication (MFA) for admin access—mandatory if technically possible in domain
- High-privilege actions require re-authentication

**Reference:** ISO 27001 A.5.18, NIST CSF PR.AC-1, NATO AC/322-D(2017)0009

---

### 5.5 Password Transmission and Storage

- Never transmit unencrypted passwords (all domains)
- Store passwords only in hashed/salted/encrypted format per NATO crypto/TEMPEST requirements
- Password storage systems must be accredited for the relevant classification level
- Audit storage software and cryptography per NATO, NCSC/NCIRC mandates

**Reference:** ISO 27001 A.8.2.3, NIST CSF PR.DS-1, NATO C-M(2002)49

---

### 5.6 Password Entry, Handling, and Compromise

- Limit failed login attempts: maximum 5 consecutive failures before account lock (review thresholds per domain SOP)
- Prevent password hints
- User-initiated resets: only via approved, logged processes with identity proof (in-person or MFA method)
- Mandatory reporting of suspected/unintentional exposure; immediate account security review and reset

**Reference:** NIST SP 800-63B §5.2.2, ISO 27001 A.5.15, AC/322-D(2017)0009

---

### 5.7 Contractor and Third-Party Access

- Password issuance and use subject to same requirements as NATO personnel
- Accounts must be immediately disabled upon contract/assignment termination
- All third-party password use must be logged and reviewed per operational security (OPSEC) procedures

**Reference:** ISO 27001 A.5.19, NATO AC/35-D/1029, Host-nation CSL (Law 58/2019)

---

### 5.8 Cross-Domain and Coalition Operations

- No passwords reused across coalition, mission partner, or classification boundaries
- Where federation is technically necessary, employ federation protocols that do not replicate or share password hashes/secrets
- CDS (cross-domain solution) admin passwords controlled under two-person integrity in SECRET operations

**Reference:** NATO AC/322-D(2017)0009, Originator Control (ORCON), AJP-3.20

---

## 6. MONITORING AND REVIEW

- SOC monitors for brute-force, credential stuffing, and anomalous password-related behavior 24/7 across all domains (feeding NCIRC and NCSC warning/alerting)
- Quarterly password audit: check for reuse, idle/abandoned accounts, privilege creep
- Red-team and security exercise injects will test password control efficacy at least annually
- All password policy changes tabled at annual review or after relevant incident/threat report

**Reference:** NIST CSF DE.CM-7, NATO CIRC IR Plan, ISO 27001 A.10.1

---

## 7. TRAINING AND AWARENESS

- All users require annual cybersecurity and authentication training (minimum 40h/year incl. password and phishing modules)
- Privileged users: additional semiannual briefings on advanced credential abuse, current threats, and secure management
- Attendance and test completion tracked and auditable

**Reference:** NATO Cyber Defence Pledge, ISO 27001 A.6.3, NIST CSF PR.AT-1

---

## 8. INCIDENT RESPONSE

- Any suspected or confirmed password compromise must be reported immediately to ISSM/J6 and the Theatre SOC
- IR actions follow established NCIRC procedures:
  - Immediate account lock/pw reset
  - Forensic investigation and logging
  - Notification per relevant chain (NCIRC, NCSC, Host-nation authorities if personal data at risk)
  - Corrective and preventative action documentation

**Reference:** NATO NCIRC IR Process, ISO 27001 A.5.25, NIST CSF RS.RP-1

---

## 9. COMPLIANCE AND AUDIT

- Supports and enforces: 
  - NATO C-M(2002)49 (Policy), AC/322-D(2017)0009 (Technical/Implementation), AC/35-D/1015/1029 (Personnel security)
  - Romanian CSL Law 58/2019 (NIS/NIS2), GDPR for relevant data
  - Bilateral/multilateral sharing agreements and coalition caveats
  - ISO/IEC 27001:2022 A.5.15, A.5.18, A.8.2.3, A.5.25, NIST CSF (PR, DE, RS domains)
- Internal audit: annually by ISSM with J6 technical staff
- External/coalition/NATO audit: per SHAPE schedules, coalition verification, or operational requirement
- Remediation of findings within 30 days unless otherwise mandated

---

## 10. ENFORCEMENT

- Any policy violation is subject to investigation per NATO, host-nation, and home-nation/coalition legal and disciplinary regimes
- Consequences may include account suspension, operational privilege revocation, removal from detachment, administrative/legal sanction, or notification to national authorities
- All violations and actions logged and retained per classification and privacy requirements

---

## 11. EXCEPTIONS

- Exception requests must be submitted in writing to the ISSM for review and Detachment Commander approval; all exceptions must state operational justification and compensating controls
- Emergency exceptions (e.g., tactical ops/cyber defense exigency) may be granted by Commander with immediate notification to ISSM and followed by a documented risk review within 48 hours
- All exceptions logged and reviewed during the annual policy review

---

## APPENDICES

### APPENDIX A: DEFINITIONS

- **NU/NR/NS/MISSION SECRET:** NATO security classification domains (see Section 3)
- **ISSM:** Information Systems Security Manager — lead security officer at detachment, J6 branch
- **SOC:** Security Operations Center
- **PKI:** Public Key Infrastructure – certificate-based authentication system
- **TEMPEST:** NATO technical standard for shielding against electromagnetic eavesdropping
- **CDS:** Cross-domain solution – system for transferring data securely across classification boundaries
- **NCIRC:** NATO Computer Incident Response Capability
- **NCSC:** Romanian National Cyber Security Directorate/Center
- **COSMIC TOP SECRET (CTS):** Highest NATO classification
- **Two-person integrity:** Procedure requiring two cleared individuals for critical security operations (e.g., COMSEC)

---

### APPENDIX B: FORMS AND TEMPLATES

- Password exception request template (available from J6/ISSM)
- Account request and privilege change forms
- Incident report template for credential compromise

---

### APPENDIX C: CONTACT INFORMATION

- ISSM/J6: [contact details]
- SOC (24/7 Incident Desk): [contact details]
- NCIRC Reporting Chain: [reference in IR Plan]
- Host-nation/NCSC interface officer: [contact details]

---

### APPENDIX D: TECHNICAL CONTROLS

- System-enforced complexity per classification
- Integration points for PKI/multi-factor
- Cross-domain password transfer prohibitions
- Automated audit scripts for reuse and privilege audit

---

## DOCUMENT CONTROL

| Version | Date       | Author         | Changes                           |
|---------|------------|---------------|-----------------------------------|
| 1.0     | [YYYY-MM-DD]| ISSM (J6), NATO Multinational Detachment | Initial issue                     |

---

### Approval Block

Detachment Commander: _______________  Date: _______________

ISSM (J6): _______________  Date: _______________

NATO CIS Security Authority (as delegated): _______________  Date: _______________

---

## REFERENCES AND SOURCES

This policy was developed based on the following frameworks, regulations, and standards:
- *NATO Information Security Policy (C-M(2002)49 and successor), AC/322-D(2017)0009, AC/35-D/1015, AC/35-D/1029*
- *NATO Cyber Defence Pledge 2016, Allied Joint Doctrine for Cyberspace Operations (AJP-3.20)*
- *Romanian Cybersecurity Law (Law 58/2019/NIS/NIS2 transposition), GDPR (Regulation EU 2016/679)*
- *ISO/IEC 27001:2022 (Controls A.5.15, A.5.18, A.8.2.3, A.5.25, A.6.3, A.10.1, A.5.19)*
- *NIST Cybersecurity Framework v2.0 (PR, DE, RS domains), NIST SP 800-63B (Digital Identity Guidelines)*
- *NATO NCIRC IR processes, SHAPE/NCSC/NCIRC bulletins*
- *Internal operational procedures and red-team/blue-team exercise findings*

</policy>
