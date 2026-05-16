---
config: C1
context_id: ctx-H
policy_id: P1
policy_name: Password Policy
policy_short: password
metadata:
  config: C1
  model: gpt-4.1
  input_tokens: 6390
  output_tokens: 3312
  total_tokens: 9702
  latency_s: 41.23
  tool_calls: []
  raw_provider_id: run_Qt2Kxlx8PWMVP6FSalnFQ4Nc
  run_status: completed
  thread_id: thread_rtMg66XiRiuGweBpY7v5KsiU
sources_count: 0
sources: []
prompt_chars: 4657
answer_chars: 14278
generated_at_unix: 1778086225
---

<policy title="Password Policy">

---

## POLICY HEADER BLOCK

**Organization:** Azienda Sanitaria Locale (Provincial General Public Hospital), Italy  
**Effective Date:** [Insert Date]  
**Policy Owner:** IT Manager (or delegated ICT security officer)  
**Review Cycle:** Annual

---

## 1. PURPOSE

This Password Policy establishes the mandatory requirements for the creation, management, protection, and renewal of passwords within [Hospital Name], with the primary objective of securing access to clinical, administrative, and technical information systems while safeguarding special-category health data. The policy ensures alignment with applicable legal and regulatory frameworks—including GDPR (EU 2016/679), NIS2 (EU 2022/2555), the Italian Data Protection Code, relevant AGID security guidelines, and best practices per ISO/IEC 27001:2022 and NIST CSF 2.0.

---

## 2. SCOPE

This policy applies to:
- All employees (clinical, administrative, technical/facility)
- Affiliated personnel, interns, and contractors
- Managed Service Provider (MSP) personnel with access to hospital systems
- External consultants and vendors with system access
- All hospital IT systems (on-premises and remote), including:
  - Active Directory/Windows workstations
  - Regional FSE (Electronic Health Record) and related clinical platforms (PACS, RIS, LIS, ADT, Pharmacy)
  - Mobile/point-of-care devices
  - Administrative and backup systems
- All systems and devices connected to the hospital network, regardless of ownership
- Accounts with access to patient or employee personal data

---

## 3. ROLES AND RESPONSIBILITIES

### 3.1 Executive Leadership (Hospital Director)
- Approves the Password Policy.
- Allocates sufficient resources for policy implementation and user training.
- Ensures compliance mandates are met.

### 3.2 IT Manager / Delegated Security Officer
- Implements password management controls and technical enforcement.
- Ensures password-related incidents are investigated and reported.
- Maintains documentation of password events and policy exceptions.
- Coordinates with the MSP for operational controls.

### 3.3 Managed Services Provider (MSP)
- Configures and maintains technical password enforcement controls as per this policy.
- Reports suspicious authentication activity.
- Supports incident response.

### 3.4 All Staff and Users
- Comply with password creation, management, and confidentiality requirements.
- Promptly report any suspected compromise or loss of credentials.
- Participate in required training.

---

## 4. POLICY PRINCIPLES

### 4.1 Least Privilege and Need-to-Know
Passwords must limit access strictly to data and systems pertinent to user roles, reducing the risk of unauthorized data exposure.  
*(Ref: ISO/IEC 27001:2022 A.5.15, NIST CSF ID.AM-3)*

### 4.2 Strong Authentication as Sector Standard
Password strength and management rules must reflect the high-risk nature of healthcare and the presence of special-category (health) data, addressing common threats (phishing, ransomware, supplier compromise).  
*(Ref: GDPR Art. 32; Provvedimenti Garante Privacy, NIS2 Art. 21; AGID Linee Guida)*

### 4.3 Usability and Non-Obstruction of Clinical Operations
Controls must not impede urgent clinical workflows, especially in emergency or acute care contexts. Usability will be regularly reviewed to minimize unintended workarounds.  
*(Ref: AGID PA Security Guidelines, NIS2 Art. 21, Recital 33)*

### 4.4 Continuous Improvement and Training
Password controls and staff awareness training must evolve alongside changes in threats, technology, and regulations.  
*(Ref: NIST CSF PR.AT-1, ISO/IEC 27001:2022 A.6.3)*

---

## 5. POLICY REQUIREMENTS (MAIN BODY)

### 5.1 Password Creation and Complexity

**Control:**  
- Minimum length: 12 characters for all user accounts; 16 for privileged/administrator accounts.
- Must avoid common/predictable passwords (e.g., hospital name, “password123”, seasons, years).
- Prohibited to use the last 10 passwords again.
- Complexity: must include at least three of the following four: uppercase, lowercase, digit, special character.
  - Exception: Clinical kiosk logons may have relaxed complexity but with strict session controls (see 5.5).

**Process:**  
1. Password controls shall be enforced through domain policy and/or application settings.  
2. Password generation tools or password managers may be provided at the discretion of IT.  
3. Password auto-generation (where supported) is permitted if it meets these standards.

**Reference:**  
- ISO/IEC 27001:2022 A.5.15
- NIST SP 800-63B Sec. 5.1.1
- AGID Misure minime – “Gestione delle credenziali”
- Provvedimenti Garante Privacy (Sanità Digitale)

---

### 5.2 Password Change and Expiry

**Control:**  
- Passwords must be changed:
  - At first logon
  - In the event of suspected or confirmed compromise
- Routine expiry is not mandated (<12 months), except for privileged accounts (maximum 180 days).
- Password reuse: previous 10 passwords cannot be reused.
- On staff change/role change/termination, relevant credentials must be promptly reset or disabled.

**Reference:**  
- NIST SP 800-63B Sec. 5.1.1.2 (No forced periodic changes for ordinary users)
- ISO/IEC 27001:2022 A.5.15, A.8.2
- AGID Misure minime

---

### 5.3 Account Lockout and Authentication Failure

**Control:**  
- Automated lockout after 5 consecutive failed login attempts (user accounts); 3 attempts for privileged/admin accounts.
- Locked accounts must be reviewed before reset.
- Lockout period: minimum 15 minutes or until IT/admin unlocks.

**Reference:**  
- ISO/IEC 27001:2022 A.5.15
- NIST CSF PR.AC-7, SP 800-53 IA-5
- AGID Linee Guida (cfr. controllo sugli accessi)

---

### 5.4 Password Confidentiality and Sharing

**Control:**  
- Users must never share their passwords, even with IT, MSP, or clinical supervisors.
- Passwords must not be written down or stored in plain text, except securely in encrypted password managers approved by IT.
- Temporary/administrator accounts and break-glass access must be uniquely assigned, logged, and only used with management approval.

**Reference:**  
- GDPR Art. 32; ISO/IEC 27001:2022 A.5.15; AGID Misure minime

---

### 5.5 Special Use Cases (Clinical Kiosks, Shared Workstations, Emergency Access)

**Control:**  
- Clinical kiosks in acute/emergency settings may use quick-auth mechanisms (badge, PIN of at least 6 digits) only if session lock and timeout are enforced (lock after 1 minute of inactivity).
- All logins must be uniquely attributable (no generic/shared accounts except where strictly necessary for patient safety, with case-by-case IT approval and compensating controls).
- “Break-glass” accounts must be auditable, monitored, and reset after each use; all uses must be logged and reported.

**Reference:**  
- AGID Sanità Digitale; Provvedimenti Garante Privacy in Sanità; NIS2 Art. 21(2)(d); ISO/IEC 27001:2022 A.5.15

---

### 5.6 Vendor, Outsourced, and System Accounts

**Control:**  
- All external/vendor and system/service (non-human) accounts must comply with strong password requirements as above, or use certificate/key-based authentication where possible.
- Default passwords must be changed prior to system deployment or connection.
- Access for MSP or vendor personnel must be limited to designated windows and specific systems; passwords must be reset after engagement.

**Reference:**  
- NIS2 Art. 21; ISO/IEC 27001:2022 A.5.17; AGID Linee Guida (identità e accessi terzi)

---

## 6. MONITORING AND REVIEW

### 6.1 Password-Related Event Logging

**What to monitor:**
- Authentication failures, lockouts, and break-glass account use.
- Password resets, unauthorized or unusual logins.

**Frequency:**  
- Continuous (automated where feasible); reviewed weekly; critical events escalated immediately to IT and MSP.

**Responsible:**  
- IT Manager with MSP support

**Retention:**  
- Minimum 12 months or as per health data log retention requirements.

---

### 6.2 Regular Reviews

**Review Type:** Annual  
- Policy and technical enforcement review.
- User and privileged account audit (at least annually, after major incidents, or upon significant IT/system change).

**Deliverable:**  
- Annual password compliance and event report to executive leadership.

---

## 7. TRAINING AND AWARENESS

### 7.1 Mandatory Training

All staff must complete:
- Cybersecurity and password management module (minimum 2 hours/year, as per organisational envelope).
- Targeted awareness sessions addressing phishing and credential safety, tailored for clinical staff turnover/onboarding.

**Training Topics:**
- Password creation and threat awareness
- Consequences of password sharing and credential compromise
- Use of password managers (where provided)

### 7.2 Acknowledgment

- All users must confirm (electronically or in writing) understanding and acceptance of the policy at onboarding and following major updates.
- Documentation stored by HR and IT.

---

## 8. INCIDENT RESPONSE

### 8.1 Reporting

Staff must immediately report:
- Suspected/confirmed credential exposure or compromise
- Suspicious password-related events

**Reporting channels:**
- IT Manager/incident contact (in hours)
- MSP helpdesk (24/7 for clinical operations)
- Escalation to hospital management for critical clinical system compromise

### 8.2 Response Actions

Upon report:
1. Account promptly locked or password reset
2. Incident log opened; facts documented
3. Event escalated to MSP for technical investigation
4. Incident remediation and forensic review (where appropriate)
5. Lessons learned review post-incident

---

## 9. COMPLIANCE AND AUDIT

### 9.1 Regulatory Compliance

This policy supports compliance with:
- **GDPR (EU 2016/679):** Art. 32 (“Security of Processing”), Recital 39, 83
- **Codice Privacy D.Lgs. 196/2003 (as amended):** Art. 33–35 (“Misure minime e idonee”)
- **NIS2 (EU 2022/2555):** Art. 21 (cybersecurity risk management requirements for essential entities)
- **AGID Misure minime per la sicurezza ICT e Linee Guida**
- **ISO/IEC 27001:2022:** Controls A.5.15, A.8.2
- **NIST CSF 2.0:** PR.AC-1, PR.AC-7

### 9.2 Policy Review

- Formal review annually, after major incidents, or after regulatory/technology changes.
- Responsibility: IT Manager, with executive review and input from the MSP.

### 9.3 Audit Rights

- Internal audit annually; externally as required by ASL/regional inspectors.
- Audit remediation within 90 days of findings.

---

## 10. ENFORCEMENT

### 10.1 Policy Violations

Violations may result in:
- Written or oral warning (minor)
- Temporary loss of system access (moderate)
- Disciplinary action per employment contract or regulatory provisions (serious/repeat offender)
- Escalation to relevant authorities for regulatory/criminal breaches

**Examples:**
- Minor: repeated reset requests due to poor password habits
- Serious: intentionally sharing credentials, ignoring lockout procedures

### 10.2 Documentation

All violations are logged in IT/security incident log and reviewed by management.

---

## 11. EXCEPTIONS

### 11.1 Exception Process

- Request: made via formal written request to IT Manager, stating reason and risk justification.
- Approval: IT Manager, with escalation to hospital executive for critical systems.
- Compensating controls: must be defined and documented.
- Maximum validity 6 months, with mandatory review.

### 11.2 Emergency Access (“Break-glass”)

- Authorised only for urgent patient care scenarios.
- Logged automatically; post-use review by IT Manager.
- Password or credentials immediately reset after use.

---

## APPENDICES

### Appendix A: Definitions

**Password Policy:** Rules and processes regulating the creation, management, and protection of authentication credentials.  
**Privileged Account:** Accounts with administrative or elevated rights beyond standard user access.  
**Break-glass Account:** Special-use login for emergency access, subject to enhanced monitoring.  
**MSP:** Managed Service Provider; external contractor providing ICT operational support.  
**AGID:** Agenzia per l’Italia Digitale; Italian public agency issuing security guidelines.  
**FSE:** Fascicolo Sanitario Elettronico; Regional/national digital health record.  
**ASL:** Azienda Sanitaria Locale; Local health authority within Italy’s public health system.

---

### Appendix B: Forms and Templates

- Password exception request form
- Password reset request (user-initiated)
- Incident reporting template (password-related events)
- Privileged account usage log template

---

### Appendix C: Contact Information

- IT Manager: [Name] – [Phone] – [Email] – Availability: core business hours
- MSP Helpdesk: [External Contact Info] – 24/7 for critical clinical
- Hospital Executive Contact: [Name/Email]  
- Security Incident Response escalation (if available): [Contact]  

---

### Appendix D: Technical Controls

- Active Directory domain password policies screenshot/configuration
- Example clinical kiosk authentication timeout setting
- List of approved password managers or tools

---

## DOCUMENT CONTROL

### Version History Table

| Version | Date         | Author              | Changes                              |
|---------|--------------|---------------------|--------------------------------------|
| 1.0     | [YYYY-MM-DD] | IT Manager / Policy Lead | Initial draft                       |

---

### Approval Block

**Policy Approved By:**  
Hospital Director: _______________ Date: _______________  
IT Manager: _______________ Date: _______________  
Data Protection Officer (DPO): _______________ Date: _______________  

---

## REFERENCES AND SOURCES

This policy was developed based on the following frameworks, regulations, and standards:

- *GDPR (Regulation EU 2016/679), Art. 32, Recitals 39, 83*
- *NIS2 (Directive EU 2022/2555), Art. 21*
- *Codice in materia di protezione dei dati personali (D.Lgs. 196/2003 e 101/2018)*
- *Linee Guida AGID per la sicurezza informatica nella PA*
- *AGID Misure minime per la sicurezza ICT, “Gestione delle credenziali”*
- *Provvedimenti Garante Privacy in Sanità Digitale*
- *ISO/IEC 27001:2022, controls A.5.15, A.8.2*
- *NIST CSF 2.0, PR.AC-1, PR.AC-7, PR.AT-1; NIST SP 800-63B*
- *Hospital interview profile, 2024*

</policy>
