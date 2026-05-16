---
config: C0+web
context_id: ctx-H
policy_id: P1
policy_name: Password Policy
policy_short: password
metadata:
  config: C0+web
  model: gpt-4.1-2025-04-14
  input_tokens: 1438
  output_tokens: 1900
  total_tokens: 3338
  latency_s: 33.26
  tool_calls: []
  raw_provider_id: resp_0f8ed767f9ba0e620069fb6ffd602881a29f9b438533c1fb75
sources_count: 0
sources: []
prompt_chars: 4657
answer_chars: 7233
generated_at_unix: 1778085917
---

---

# Password Policy

**Organisation:** Azienda Sanitaria Locale (ASL) — Small Public Hospital, Italy  
**Effective Date:** 2024-07-01  
**Policy Owner:** IT Manager (with delegated responsibility for cybersecurity)  
**Review Cycle:** Annual (or upon major regulatory/operational change)  

---

## 1. Purpose

This Password Policy establishes mandatory requirements for the creation, use, management, and protection of passwords within the hospital’s information systems. Its purpose is to safeguard sensitive health data, ensure compliance with applicable regulations (GDPR, NIS2, AGID, etc.), and mitigate sector-specific cyber threats (e.g., ransomware, phishing, data leaks) under the hospital’s operational and resource constraints.

---

## 2. Scope

This policy applies to all hospital employees, contractors, consultants, temporary staff, volunteers, and third-party users (including MSP personnel) who access hospital IT resources, including on-premises and remotely, via workstations, mobile devices, or systems containing or processing personal or health data.

---

## 3. Roles and Responsibilities

- **IT Manager:**  
  - Policy owner and coordinator of implementation, monitoring, and review.  
  - Delegates technical enforcement to MSP and provides guidance to staff.
- **Managed Service Provider (MSP):**  
  - Implements and enforces technical controls per this policy, reports breaches/incidents.
- **Department Heads:**  
  - Ensure all staff comply with this policy and complete required training.
- **All Users:**  
  - Adhere to password creation, usage, and protection requirements; report suspected compromise immediately.

---

## 4. Principles

- **Data Protection:** Passwords are a primary safeguard for special category (health) data; controls are risk-based and aligned to regulatory and international best practice.
- **Usability:** Controls must not hinder clinical or emergency workflows.
- **Least Privilege:** Access is granted only as necessary for professional duties.
- **Proportionality:** Technical and procedural controls reflect the hospital’s size, staffing, and budgetary limits.

---

## 5. Requirements and Controls

### 5.1 Password Creation & Complexity

- **Minimum Length:**  
  - 12 characters for all user accounts accessing personal or health data (GDPR Art. 32; AGID Linee guida; NIST SP 800-63B §5.1.1.2).
- **Complexity Requirements:**  
  - No mandatory character classes, but passwords must not be easily guessable (NIST SP 800-63B §5.1.1.2; ISO/IEC 27001:2022 A.5.17).
  - Passwords must not contain the user's name, username, or hospital name.
  - Passwords must not be found in commonly used password lists or compromised credentials (NIST SP 800-63B §5.1.1.2; AGID Misure Minime).
- **System Accounts (Privileged):**  
  - Minimum 16 characters, as above (ISO/IEC 27001:2022 A.5.17; NIS2 Annex I, 2(d)).

### 5.2 Password Management

- **Change on First Use:**  
  - All initial passwords (and resets) must be changed on first login (ISO/IEC 27001:2022 A.5.17; AGID Misure Minime 6.2.2).
- **Password Expiry:**  
  - No mandatory periodic expiration unless compromise is suspected or confirmed (NIST SP 800-63B §5.1.1.2; AGID Misure Minime).
- **Password Reset:**  
  - Identity of user must be verified prior to password reset (GDPR Art. 32; NIST SP 800-63B §5.1.2).
- **Password History:**  
  - Prevent reuse of the last 5 passwords (ISO/IEC 27001:2022 A.5.17; AGID Misure Minime).

### 5.3 Protection of Passwords

- **Storage:**  
  - Passwords must be stored and transmitted only in encrypted form (ISO/IEC 27001:2022 A.8.12; GDPR Art. 32; AGID Misure Minime 6.2.3).
- **Disclosure:**  
  - Passwords must not be shared, written down, or disclosed to anyone (including IT or MSP staff), except as required for emergency support, which must be logged and reset immediately after use (ISO/IEC 27001:2022 A.5.17).
- **Default Credentials:**  
  - All default passwords must be changed before deployment (NIS2 Annex I, 2(d); AGID Misure Minime 6.2.2).

### 5.4 Multi-Factor Authentication (MFA)

- **Administrative & Remote Access:**  
  - MFA is required for all administrative accounts and for remote access to hospital systems, where technically feasible and without impeding patient safety or emergency care (NIS2 Annex I, 2(d); AGID Linee guida; ISO/IEC 27001:2022 A.5.18).
- **Federated Accounts (SPID/CIE):**  
  - Where federated authentication is used, rely on the assurance level provided by the federating authority.

### 5.5 Account Lockout

- **Lockout Threshold:**  
  - Accounts must be locked after 10 consecutive failed login attempts. Lockout duration: 15 minutes or until reset by IT (ISO/IEC 27001:2022 A.5.17; AGID Misure Minime 6.2.2).

### 5.6 Training & Awareness

- **Annual User Training:**  
  - Staff must complete at least 2 hours/year in security awareness, including secure password practices and phishing recognition (GDPR Art. 32; NIS2 Art. 21(2); AGID Linee guida).

---

## 6. Exceptions

- **Clinical Emergency:**  
  - In situations where password controls impede patient safety or emergency care, clinical leads may authorise temporary bypass, with subsequent incident reporting to IT for review and remediation (unsupported, sector-specific adaptation).
- **Legacy Systems:**  
  - Where technical limitations prevent compliance (e.g., legacy kiosk workstations), compensating controls (e.g., physical access restriction, monitoring) must be documented and approved by IT and MSP (ISO/IEC 27001:2022 A.8.15).

---

## 7. Monitoring and Review

- **Audit:**  
  - Periodic review (at least annually) of password controls, compliance, and effectiveness by IT in coordination with MSP (ISO/IEC 27001:2022 A.10.1; NIS2 Art. 21).
- **Incident Reporting:**  
  - All suspected password compromises or policy violations must be reported immediately to IT and escalated to MSP per incident response procedures.
- **Review Cycle:**  
  - Policy reviewed annually, or upon significant changes in regulatory requirements, threat landscape, or hospital operations.

---

## 8. References

- **Regulatory/Legal:**  
  - [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) (Art. 32, 33)  
  - [NIS2 Directive](https://eur-lex.europa.eu/eli/dir/2022/2555/oj) (Art. 21, Annex I)  
  - [Codice Privacy](https://www.garanteprivacy.it/web/guest/home/docweb/-/docweb-display/docweb/9058976) (D.Lgs. 196/2003, D.Lgs. 101/2018)  
  - [AGID Linee Guida sulla sicurezza](https://www.agid.gov.it/it/sicurezza/minime)  
  - [Misure minime di sicurezza ICT per la PA](https://www.agid.gov.it/sites/default/files/repository_files/misure_minime_sicurezza_pa.pdf)  
  - [Provvedimenti Garante Privacy in sanità](https://www.garanteprivacy.it/home/provvedimenti-normativa/provvedimenti-nel-settore-sanitario)
- **International Standards:**  
  - [NIST SP 800-63B Digital Identity Guidelines](https://pages.nist.gov/800-63-3/sp800-63b.html)  
  - [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework) (ID.AM-3, PR.AC-1, PR.AC-6)  
  - [ISO/IEC 27001:2022](https://www.iso.org/standard/27001) (A.5.17, A.5.18, A.8.12, A.8.15, A.10.1)

---

**Policy Owner:** IT Manager  
**Approval:** Hospital Director  
**Next Review:** 2025-07-01

---
