---
config: C0+web
context_id: ctx-H
policy_id: P3
policy_name: Access Control Policy
policy_short: accesscontrol
metadata:
  config: C0+web
  model: gpt-4.1-2025-04-14
  input_tokens: 1440
  output_tokens: 2140
  total_tokens: 3580
  latency_s: 36.679
  tool_calls: []
  raw_provider_id: resp_08262bf093d8d7860069fb7043f718819fa50f80ed7b10b867
sources_count: 0
sources: []
prompt_chars: 4669
answer_chars: 8344
generated_at_unix: 1778085992
---

---

# Access Control Policy

**Organisation:** [Redacted] Provincial Hospital (Servizio Sanitario Nazionale, ASL)  
**Country:** Italy  
**Policy Title:** Access Control Policy  
**Effective Date:** [Insert Date]  
**Owner:** IT Manager (with oversight by Hospital Director, delegated to external MSP)  
**Review Cycle:** Annual, or upon significant change in systems, regulation, or threat landscape  
**Approved by:** [Hospital Director/ASL delegate]  
**Version:** 1.0

---

## 1. Purpose

This Access Control Policy establishes requirements for managing user access to information systems and data at [Redacted] Provincial Hospital. The policy aims to ensure the confidentiality, integrity, and availability of special category health data and personal data, in compliance with applicable Italian, EU, and international regulations and standards. Controls are designed to be proportionate to the hospital's resource envelope and clinical context, prioritising patient safety and service continuity.

---

## 2. Scope

This policy applies to:
- All staff (clinical, administrative, technical), contractors, and third parties (including the external MSP) with access to hospital IT resources.
- All hospital-managed IT systems, including on-premises, regional, and cloud-hosted platforms (e.g. EHR/FSE, PACS/RIS, LIS, ADT, pharmacy, workstations, mobile devices).
- All data classified as personal or special category data under GDPR and national law.
- Physical and logical access to hospital information assets.

---

## 3. Roles and Responsibilities

| Role                  | Responsibility                                              |
|-----------------------|------------------------------------------------------------|
| IT Manager (internal) | Day-to-day access management; policy enforcement.           |
| MSP                   | Implements technical controls, supports identity lifecycle. |
| Data Protection Officer (DPO) | Oversight on GDPR/data protection compliance.  |
| Hospital Director / ASL | Ultimate accountability for policy.                      |
| Department Heads      | Authorisation for access requests in line with job roles.   |
| All Users             | Adhere to this policy; report suspected breaches.           |

---

## 4. Principles

- **Least Privilege**: Access is granted only to the minimum resources necessary for role performance.  
  *Source: ISO/IEC 27001:2022 A.9.1.2; NIST CSF PR.AC-4; GDPR Art. 25(2)*
- **Role-Based Access Control (RBAC)**: Access rights are assigned based on defined roles, not individuals, to ensure consistency and scalability.  
  *Source: ISO/IEC 27001:2022 A.9.2.2; NIST CSF PR.AC-4*
- **Need-to-Know**: Special category health data are accessible only to authorised personnel directly involved in patient care or administrative processes.
  *Source: GDPR Art. 32(1), Art. 5(1)(c); Codice Privacy D.Lgs. 196/2003, Art. 2-ter*
- **Segregation of Duties**: Conflicting duties are separated to reduce risk of unauthorised or fraudulent activity.
  *Source: ISO/IEC 27001:2022 A.6.1.2; NIST CSF PR.AC-5*
- **User Accountability**: All users are uniquely identified and accountable for actions performed under their credentials.
  *Source: ISO/IEC 27001:2022 A.9.2.1; NIS2 Art. 21(2)(d)*

---

## 5. Access Control Requirements

### 5.1 User Registration and De-registration

- All users must be registered in the appropriate identity management system (on-prem AD, regional SPID/CIE) with unique identifiers.  
  *Source: ISO/IEC 27001:2022 A.9.2.1; AGID Linee Guida 4.2*
- Access requests require approval by the relevant Department Head and validation by IT.  
  *Source: ISO/IEC 27001:2022 A.9.2.2*
- Access rights must be promptly revoked upon termination or role change (within 24h of notification).  
  *Source: NIST CSF PR.AC-1; NIS2 Art. 21(2)(d); AGID Misure Minime 14.2*

### 5.2 User Access Management

- Role profiles are maintained for each major job function; access privileges mapped to these profiles.  
  *Source: ISO/IEC 27001:2022 A.9.1.1; AGID Misure Minime 13.1*
- Periodic access reviews (at least annually, or upon staff transfer) are conducted by IT/HR to validate appropriateness of access.  
  *Source: ISO/IEC 27001:2022 A.9.2.5; AGID Linee Guida 4.5*
- Temporary/guest access is limited in time and scope, with mandatory expiry.  
  *Source: ISO/IEC 27001:2022 A.9.2.6*

### 5.3 Authentication

- Multi-factor authentication (MFA) is required for remote access (VPN, remote desktop, cloud systems), and for privileged accounts.  
  *Source: AGID Misure Minime 14.4; NIS2 Art. 21(2)(d); NIST CSF PR.AC-7*
- Passwords must comply with current security best practices (minimum 12 characters, complexity, regular rotation for privileged accounts, no reuse).  
  *Source: ISO/IEC 27001:2022 A.9.3.1; AGID Misure Minime 14.3.2*
- SPID/CIE federation is used for systems integrated with regional identity, leveraging strong authentication.  
  *Source: AGID Linee Guida, regional FSE regulations*

### 5.4 Privileged Access

- Privileged accounts (e.g., system admins, MSP technicians) are strictly limited and monitored; use of shared accounts is prohibited except where technically unavoidable (documented and justified).  
  *Source: ISO/IEC 27001:2022 A.9.2.3; NIST CSF PR.AC-4*
- Administrative actions on critical systems (EHR, ADT, PACS) are logged and logs are retained for at least 12 months.  
  *Source: Provvedimenti Garante Privacy 2015/2018; AGID Misure Minime 15.2*

### 5.5 Network and Device Access

- Network segmentation is maintained between clinical, administrative, and diagnostic systems; direct access between VLANs is restricted and monitored.  
  *Source: AGID Misure Minime 17.1; NIST CSF PR.AC-5*
- Legacy devices (e.g. Windows kiosks) are restricted to essential functions, placed on dedicated VLANs, and subject to enhanced monitoring.  
  *Source: AGID Misure Minime 10.1; unsupported (segmentation best practice)*
- Mobile devices are enrolled in Mobile Device Management (MDM) controls, require screen lock, and full-disk encryption where technically feasible.  
  *Source: ISO/IEC 27001:2022 A.6.2.1; AGID Misure Minime 12.3; NIS2 Art. 21(2)(d)*

### 5.6 Physical Access

- Access to IT rooms and critical infrastructure is restricted to authorised personnel; access logs are maintained.  
  *Source: ISO/IEC 27001:2022 A.11.1.1; AGID Misure Minime 9.1*

### 5.7 Third-Party and MSP Access

- MSP and vendor access is governed by contract, with access limited to the minimum necessary and subject to monitoring.  
  *Source: ISO/IEC 27001:2022 A.15.1.1; NIS2 Art. 21(2)(f); AGID Misure Minime 16.3*
- Remote access by third-parties requires explicit approval, is time-limited, and must be logged.  
  *Source: ISO/IEC 27001:2022 A.15.2.1*

---

## 6. Exceptions

- Any exceptions to this policy must be documented, justified (e.g., legacy system constraints, patient safety override), and approved by the IT Manager and DPO, with notification to Hospital Director/ASL.
- Exceptions must include compensating controls and time limits; they are subject to review at least annually.

---

## 7. Monitoring and Review

- Access control events (e.g. failed logins, privilege escalations) are logged and reviewed at least monthly by IT/MSP.  
  *Source: AGID Misure Minime 15.1; NIST CSF DE.CM-7*
- Annual policy reviews are conducted by the IT Manager in consultation with the DPO and MSP, and upon significant incidents or regulatory changes.
- Results of access reviews, monitoring, and incident investigations are reported to the Hospital Director/ASL and documented for audit purposes.

---

## 8. References

- **Regulatory**:
    - GDPR (Regulation EU 2016/679)
    - Codice Privacy D.Lgs. 196/2003, as amended
    - NIS2 Directive EU 2022/2555
    - AGID Linee Guida per la sicurezza informatica nella PA
    - AGID Misure Minime per la PA
    - Provvedimenti Garante Privacy in sanità
    - Regional FSE regulations

- **Standards**:
    - ISO/IEC 27001:2022 (esp. A.6, A.9, A.11, A.15)
    - NIST Cybersecurity Framework 2.0 (PR.AC, DE.CM)
    - Hospital internal security architecture and relevant MSP contracts

---

*This policy is to be communicated to all staff and made available on the hospital intranet. Training and awareness sessions will be conducted in line with the annual training schedule.*

---
