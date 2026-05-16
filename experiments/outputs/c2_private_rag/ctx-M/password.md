---
config: C2
context_id: ctx-M
policy_id: P1
policy_name: Password Policy
policy_short: password
metadata:
  config: C2
  model: moonshotai/Kimi-K2.5
  input_tokens: 25532
  output_tokens: 6628
  total_tokens: 32160
  latency_s: 49.947
  tool_calls:
  - rag_retrieval
  raw_provider_id: f895afb1-6b26-4161-a972-34a981ca4614
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
answer_chars: 14980
generated_at_unix: 1778086763
---

 <policy title="Password Policy">

| Field | Value |
|---|---|
| **Document ID** | POL-006 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | NATO RESTRICTED |
| **Owner** | Information Systems Security Manager (ISSM) / J6 |
| **Approved by** | Commander |
| **Approval date** | [DD/MM/YYYY] |
| **Next review date** | [DD/MM/YYYY] |
| **Review cycle** | Annual (or upon significant change to NATO INFOSEC directives or threat landscape) |

---

## 1. Purpose

This policy establishes the minimum requirements for the creation, management, protection, and lifecycle of passwords used to authenticate access to [Organisation]'s information systems across all classification domains (NU, NR, NS, and MISSION SECRET). It ensures that authentication information is protected against compromise by state-sponsored advanced persistent threats (APT), insider threats, and human intelligence (HUMINT) recruitment risks, while maintaining interoperability with NATO Public Key Infrastructure (PKI) and host-nation legal obligations.

This policy supports compliance with:
- **NATO Information Security Policy** (C-M(2002)49 and successor directives) — *Article 5 (Access Control)*  
- **AC/322-D(2017)0009** — *NATO INFOSEC Technical and Implementation Directive, Section 4.2 (Authentication)*  
- **Romanian Cybersecurity Law (Law 58/2019)** — *transposing NIS2 Directive, Article 21(2)(c) (access control policies)*  
- **GDPR (EU) 2016/679** — *Article 32(1)(b) (security of processing)*  
- **NIST SP 800-63B** — *Digital Identity Guidelines: Authentication and Lifecycle Management*  
- **ISO/IEC 27001:2022** — *Controls A.5.17 (Authentication Information) and A.8.5 (Secure Authentication)*

---

## 2. Scope

This policy applies to:

- **All personnel**: Military (active duty), civilian NATO staff, and cleared contractors (total 2000 personnel).
- **All classification domains**: NATO UNCLASSIFIED (NU), NATO RESTRICTED (NR), NATO SECRET (NS), and MISSION SECRET coalition networks.
- **All systems**: 1200 classified workstations, 800 unclassified workstations, servers, network infrastructure, COMSEC equipment, and mobile devices (smartphones/tablets) used for official business.
- **All environments**: On-premises (including SCIF/TEMPEST zones), deployed tactical systems, and remote access via NATO-approved VPNs.

**Note**: Where NATO PKI smart-card authentication (CAC-equivalent) is implemented, the smart card serves as the primary authentication factor. Passwords in this context protect local device access (boot, screen lock) and cryptographic key stores, and serve as fallback authentication only where PKI is technically infeasible.

---

## 3. Roles and Responsibilities

### 3.1 Information Systems Security Manager (ISSM) / J6
- Own and maintain this policy, ensuring alignment with NATO AC/322-D(2017)0009 and Romanian NIS2 requirements.
- Approve all password management tools and exception requests.
- Conduct quarterly compliance reviews for NS/MISSION SECRET domains and annual reviews for NU/NR.

### 3.2 COMSEC Custodian
- Ensure passwords protecting COMSEC keying material and crypto-equipment meet this policy’s minimum strength requirements.
- Enforce **two-person integrity (TPI)** for all administrative passwords accessing high-grade COMSEC systems, per NATO COMSEC doctrine.

### 3.3 Commanders and Unit Leaders (N+1)
- Ensure personnel within their command complete mandatory password security training (40 hours/year includes authentication security).
- Report suspected password compromise or insider threat indicators immediately to the 24/7 SOC and ISSM.

### 3.4 System Administrators (J6/IT Operations)
- Configure technical controls (length, complexity, lockout) on all managed systems per §4.
- Maintain sealed, tamper-evident envelopes containing emergency break-glass credentials in the J6 safe, under dual-key control.
- Revoke and reset passwords immediately upon personnel departure, clearance suspension, or reported compromise.

### 3.5 All Users (Military, Civilian, Contractor)
- Create, protect, and change passwords in accordance with this policy and classification domain requirements.
- Report suspected compromise immediately via NATO incident reporting channels (NCIRC).
- Acknowledge that passwords are NATO-sensitive information subject to need-to-know and ORCON (Originator Control) restrictions where applicable.

---

## 4. Policy Requirements

### 4.1 Authentication Hierarchy and Principles
- **Primary Authentication**: NATO PKI smart-card authentication is mandatory for all interactive logins where technically feasible (NR, NS, and MISSION SECRET domains).  
- **Secondary/Local Authentication**: Passwords protect workstation boot, screen locks, and encrypted volumes.  
- **Principle of Least Privilege and Need-to-Know**: Access to passwords for privileged accounts is granted only to personnel with valid clearance and mission requirement, per **AC/35-D/1015** (Personnel Security).

### 4.2 Classification-Specific Password Strength

| Classification Domain | Minimum Length | Complexity | Maximum Validity* |
|---|---|---|---|
| **NU (Unclassified)** | 12 characters | 3 of 4 categories | 12 months |
| **NR (Restricted)** | 14 characters | 3 of 4 categories | 12 months |
| **NS (Secret)** | 16 characters | 3 of 4 categories | 12 months (or 18 months if ≥20 chars) |
| **MISSION SECRET** | 16 characters | 3 of 4 categories | 12 months (or 18 months if ≥20 chars) |
| **Privileged/Admin** | 20 characters | 3 of 4 categories | 6 months (or 12 months if ≥24 chars) |

\*Validity periods align with **NIST SP 800-63B** (risk-based authentication) and **ISO/IEC 27001:2022 A.5.17**, adapted for NATO threat environment. Maximum validity is reduced for high-threat environments (NS/MISSION SECRET).

**Complexity Rules** (per **NIST SP 800-63B**):
- Characters from three of: Uppercase (A–Z), Lowercase (a–z), Digits (0–9), Special characters (`! @ # $ % ^ & * ( )` etc.).
- Rejection of dictionary words, NATO codewords, and personal identifiers (name, service number, date of birth).
- Support for passphrases up to 256 characters.

### 4.3 Password Change Policy
- **First Login**: Passwords distributed by J6 (temporary) or default vendor credentials must be changed immediately upon first use.
- **Reuse Prevention**: Systems must deny reuse of the last **10** passwords (NU/NR) or **15** passwords (NS/MISSION SECRET).
- **Compromise**: Change immediately upon suspected compromise, phishing attempt, or after travel to high-risk zones.
- **Shared Passwords**: Must be changed immediately when any authorised user departs the unit or changes role (insider threat mitigation).

### 4.4 Brute Force Protection
All systems must implement account lockout or progressive delay:
- **Lockout**: Account suspended for **30 minutes** after **5** consecutive failed attempts.
- **Progressive Delay**: Incremental delays (0.5s, 1s, 2s, 4s, etc.) after each failure.
- **Alerting**: Failed authentication attempts on NS/MISSION SECRET systems generate immediate alerts to the 24/7 SOC (**ISO/IEC 27001:2022 A.8.5**).

### 4.5 Physical and Environmental Controls (TEMPEST/SCIF)
- Passwords for systems within SCIFs or TEMPEST zones must never be written on paper unless stored in a **GSA-approved safe** or NATO equivalent, with access logged under two-person integrity.
- Password entry must be shielded from optical surveillance (shoulder-surfing) in multinational workspaces.
- Mobile devices (smartphones/tablets) used in NS environments must use a **minimum 6-digit PIN** (as second factor to smart card) or passphrase meeting §4.2, per **AC/322-D(2017)0009**.

### 4.6 Password Protection and Handling
- **No Sharing**: Passwords are individual credentials. Sharing constitutes a security violation under **AC/35-D/1015**.
- **No Electronic Transmission**: Passwords must not be sent via unencrypted email, chat (MS Teams/Signal), or voice. If electronic distribution is unavoidable, use **NATO-approved encrypted email (S/MIME)** to the specific classification level.
- **Storage**: 
  - User passwords: Store only in **NATO-approved password managers** (Common Criteria EAL4+ or NATO INFOSEC-evaluated products).
  - Break-glass/Admin passwords: Stored in sealed, tamper-evident envelopes in the J6 safe, requiring **dual-key access** (Commander or Deputy + ISSM).
- **No Auto-save**: Disable "Remember password" features in browsers and applications on all classified workstations (NR and above).

### 4.7 Multi-Factor Authentication (MFA)
- **PKI as MFA**: Smart-card authentication satisfies MFA requirements per **NIST SP 800-63B** (AAL2/AAL3 equivalent).
- **Fallback MFA**: Where PKI is unavailable (tactical edge, degraded connectivity), use **hardware TOTP tokens** or NATO-approved soft tokens in addition to passwords.
- **COMSEC**: Passwords for crypto-equipment must be used in conjunction with physical tokens (key fills) under TPI.

### 4.8 Service and Emergency Accounts
- **Service Accounts**: Must use passwords of minimum **20 characters**, stored in the privileged access management (PAM) vault, and rotated every **90 days** or upon any personnel change with access to the vault.
- **Emergency Access (Break-Glass)**: Documented in the Cyber Incident Response Plan (POL-008). Use requires:
  1. Written authorisation by Commander or Deputy Commander (dual-key).
  2. Immediate notification to ISSM and SOC.
  3. Password reset and audit review within 24 hours of use.

---

## 5. Monitoring and Review

- **Quarterly (NS/MISSION SECRET)**: Automated scans for weak passwords, reuse, and shared accounts. Results reviewed by ISSM.
- **Annually (All Domains)**: Full policy compliance audit against **ISO/IEC 27001:2022 A.5.17** and **NATO AC/322-D(2017)0009**.
- **Red Team Validation**: Bi-annual red-team exercises (2 per year) include password cracking and credential harvesting to test enforcement.
- **Metrics**: Report to Commander on password policy violations, brute-force attempts, and emergency access usage at each ISMS management review.

---

## 6. Exceptions

Exceptions to minimum length or change frequency require:
1. **Written justification** citing operational necessity (e.g., legacy tactical systems unable to support 16 characters).
2. **Compensating controls**: Network isolation, enhanced monitoring, or physical TEMPEST shielding.
3. **Approval**: ISSM for NR; Commander for NS/MISSION SECRET.
4. **Time limit**: Maximum **6 months**, tracked in the ISMS exception register.
5. **Review**: Monthly review of exception validity.

**Permanent Exceptions**:
- **COMSEC Key Management**: Follows separate NATO COMSEC doctrine (AC/35-D/1020 series), though passwords used for key entry must meet minimum complexity.
- **Air-Gapped Legacy Systems**: In SCIFs with no network connectivity, passwords may be managed via TPI and physical access controls only, provided documented in the Asset Management Policy (POL-003).

---

## 7. Enforcement

Non-compliance is handled under the **NATO Status of Forces Agreement (SOFA)** and host-nation (Romanian) labour law for civilians:

| Severity | Examples | Consequence |
|---|---|---|
| **Minor** | Accidental password sharing, writing password on non-secure note | Mandatory retraining; written warning |
| **Moderate** | Repeated violations, failure to report suspected compromise | Suspension of network access; formal disciplinary action under national military code or NATO civilian staff regulations |
| **Severe** | Deliberate password sharing with uncleared personnel, circumvention of PKI | Revocation of security clearance; removal from NATO premises; termination |
| **Criminal** | Selling credentials to adversary intelligence (HUMINT) | Prosecution under Romanian Penal Code (Art. 360 on cybercrime) and applicable military justice codes; referral to national law enforcement |

All violations are logged in the ISMS incident register and reported to NCIRC per **POL-008 (Cyber Incident Response Plan)**.

---

## 8. Related Documents

| Document ID | Title | Classification |
|---|---|---|
| POL-001 | Cybersecurity Policy | NATO RESTRICTED |
| POL-002 | Access Control Policy | NATO RESTRICTED |
| POL-003 | Asset Management Policy | NATO RESTRICTED |
| POL-008 | Cyber Incident Response Plan | NATO SECRET |
| NATO C-M(2002)49 | NATO Information Security Policy | NATO UNCLASSIFIED |
| AC/322-D(2017)0009 | NATO INFOSEC Technical and Implementation Directive | NATO RESTRICTED |
| AC/35-D/1015 | Security within NATO | NATO RESTRICTED |
| AJP-3.20 | Allied Joint Doctrine for Cyberspace Operations | NATO RESTRICTED |

---

## 9. Definitions

| Term | Definition |
|---|---|
| **PKI** | Public Key Infrastructure — NATO-approved cryptographic system for authentication and encryption using smart cards. |
| **COMSEC** | Communications Security — measures to prevent unauthorized access to telecommunications, including cryptographic key management. |
| **Two-Person Integrity (TPI)** | Security measure requiring two authorized persons to jointly perform a critical action (e.g., accessing admin passwords or COMSEC keys). |
| **SCIF** | Sensitive Compartmented Information Facility — accredited area for handling SECRET and above information. |
| **TEMPEST** | Protection against compromising emanations (electronic eavesdropping) from IT equipment. |
| **NU/NR/NS** | NATO classification levels: UNCLASSIFIED, RESTRICTED, SECRET. |
| **Break-glass** | Emergency account used to bypass normal authentication during critical system failure or incident response. |
| **APT** | Advanced Persistent Threat — sophisticated, state-sponsored cyber adversary. |

---

## 10. Compliance and Regulatory References

- **NATO C-M(2002)49** — *Information Security Policy (Articles 5, 6, and Annexes)*
- **AC/322-D(2017)0009** — *NATO INFOSEC Technical and Implementation Directive (Sections 4.2, 5.1)*
- **AC/35-D/1015** — *Security within NATO (Personnel Security Standards)*
- **Romanian Law 58/2019** — *Cybersecurity Law (transposition of NIS2, Articles 20-21 on access control and incident reporting)*
- **GDPR (EU) 2016/679** — *Article 32 (Security of Processing), Article 39 (Awareness raising)*
- **NIST SP 800-63B** — *Digital Identity Guidelines: Authentication and Lifecycle Management (Section 5.1.1 on Memorized Secrets)*
- **ISO/IEC 27001:2022** — *Control A.5.17 (Authentication Information), Control A.8.5 (Secure Authentication)*
- **CIS Controls v8** — *Control 5 (Account Management), Control 6 (Access Control Management)*

---

## 11. Revision History

| Version | Date | Author | Description of Change |
|---|---|---|---|
| 1.0 | [DD/MM/YYYY] | ISSM / J6 | Initial release for multinational detachment under SHAPE operational control |

---

## 12. Approval

| Role | Name | Signature | Date |
|---|---|---|---|
| Policy Owner (ISSM / J6) | | | |
| Approved by (Commander) | | | |
| Legal / SOFA Advisor Review | | | |
| Host-Nation Security Liaison (Romania) | | | |

</policy>
