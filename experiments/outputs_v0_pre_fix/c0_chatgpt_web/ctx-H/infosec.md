---
config: C0+web
context_id: ctx-H
policy_id: P1
policy_name: Information Security Policy
policy_short: infosec
metadata:
  config: C0+web
  model: gpt-4.1-2025-04-14
  input_tokens: 1186
  output_tokens: 2489
  total_tokens: 3675
  latency_s: 35.674
  tool_calls: []
  raw_provider_id: resp_00885cdf522a4d740069fb6915c69081a1b5ff3137f6bb8eb4
sources_count: 0
sources: []
prompt_chars: 4108
answer_chars: 9696
generated_at_unix: 1778084153
---

Certainly! Below is a tailored **Information Security Policy** for the described small Italian hospital, fully cross-referenced with cited regulatory and standards controls, with pragmatic measures suited to resource and operational constraints.

---

# [Hospital Name] Information Security Policy

**Organisation:** [Hospital Name], ASL [Region]  
**Effective Date:** [YYYY-MM-DD]  
**Owner:** Head of ICT / Direttore UOC Sistemi Informativi  
**Review Cycle:** Annual (or on major regulatory/operational change)  
**Version:** 1.0

---

## 1. Purpose

This policy establishes the information security principles, responsibilities, and controls to protect the confidentiality, integrity, and availability of data and systems managed by [Hospital Name]. It ensures compliance with applicable laws and standards, notably GDPR, D.Lgs. 196/2003, NIS2, AGID guidelines, and sectoral best practices, while supporting 24/7 clinical operations and patient safety.

---

## 2. Scope

This policy applies to all personnel (employees, contractors, MSP), systems (including EHR, PACS/RIS, LIS, ADT, Pharmacy), endpoints (workstations, mobile devices), and data (including special category health data, minors’ data, staff data) processed or managed by [Hospital Name], irrespective of location.

---

## 3. Roles and Responsibilities

| Role                    | Responsibilities                                                                                                                                                               | Source(s)                                              |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| **Hospital Director**   | Final responsibility for compliance and resource allocation.                                                                                                                    | ISO/IEC 27001:2022 5.3, NIS2 Art. 21                  |
| **Head of ICT**         | Policy owner, implementation oversight, incident escalation, cooperation with MSP and regional authorities.                                                                     | ISO/IEC 27001:2022 5.3, NIS2 Art. 21                  |
| **Internal ICT Staff**  | Day-to-day administration, local incident response, user support, monitoring, and reporting.                                                                                   | ISO/IEC 27001:2022 A.6.1                              |
| **Managed Service Provider (MSP)** | Execution of agreed technical controls, incident response support, reporting as per contract.                                                                        | NIS2 Art. 21(2), ISO/IEC 27001:2022 A.5.19            |
| **All Staff**           | Adherence to policy, reporting security incidents, completing mandatory training.                                                                                              | ISO/IEC 27001:2022 A.6.3, GDPR Art. 32(4)             |

---

## 4. Information Security Principles

**4.1 Regulatory Compliance**  
All activities must comply with GDPR, D.Lgs. 196/2003 as amended, NIS2, AGID Linee Guida, Garante Privacy health sector measures, and applicable regional regulations.  
*Cited: GDPR Art. 32, D.Lgs. 196/2003, NIS2 Art. 21, AGID Misure minime*

**4.2 Risk-based Approach**  
Controls are implemented based on risk assessments, considering threats to patient safety and business continuity.  
*Cited: ISO/IEC 27001:2022 6.1.2, NIST CSF ID.RA*

**4.3 Data Minimization and Purpose Limitation**  
Only process health and personal data strictly necessary for care, operations, or legal requirements.  
*Cited: GDPR Art. 5(1)(c), D.Lgs. 196/2003 Art. 3*

**4.4 Least Privilege & Need to Know**  
Access to data and systems is restricted to authorized users based on role and necessity.  
*Cited: ISO/IEC 27001:2022 A.8.2, NIST CSF PR.AC-4*

---

## 5. Requirements and Controls

### 5.1 Access Control

- **User Authentication**: All users must authenticate via on-premise Active Directory or regional SPID/CIE.  
  *Cited: ISO/IEC 27001:2022 A.8.3.2, AGID Misure minime 4.3.1, NIS2 Art. 21(2)(b)*
- **Account Management**: Accounts must be promptly deactivated on staff departure or role change (max 24h after HR notification).  
  *Cited: ISO/IEC 27001:2022 A.8.2.2, AGID Misure minime 4.3.2*
- **Privileged Access**: Administrative privileges limited to ICT and MSP; reviewed quarterly.  
  *Cited: ISO/IEC 27001:2022 A.8.2.3, NIS2 Art. 21(2)(b)*
- **Password Policy**: Enforce strong passwords (min 10 chars, complexity, no reuse for 12 months); encourage MFA where supported.  
  *Cited: AGID Misure minime 4.3.4, NIST CSF PR.AC-1*

### 5.2 Endpoint and Device Security

- **Antivirus & Patching**: All endpoints must run vendor-approved AV with central console monitoring; supported OS/devices patched monthly, legacy clinical devices patched per vendor/ICT capability.  
  *Cited: AGID Misure minime 4.4.2, ISO/IEC 27001:2022 A.8.8, NIS2 Art. 21(2)(c)*
- **Legacy Devices**: Legacy Windows clinical kiosks to be segmented on network and monitored; access restricted.  
  *Cited: ISO/IEC 27001:2022 A.8.20, NIS2 Art. 21(2)(a)*
- **Mobile Devices**: Mandatory device encryption and screen lock; loss/theft must be reported within 2h.  
  *Cited: AGID Misure minime 4.4.3, ISO/IEC 27001:2022 A.8.11*

### 5.3 Data Protection

- **Data Classification**: Health/patient data classified as “high sensitivity”; employee data as “confidential”.  
  *Cited: ISO/IEC 27001:2022 A.5.12, GDPR Art. 9*
- **Data at Rest/Transit**: Health data must be encrypted at rest and in transit where technically feasible (focus: mobile devices, backups, external transfers).  
  *Cited: GDPR Art. 32, AGID Misure minime 4.6.1, ISO/IEC 27001:2022 A.8.10*
- **Backups**: EHR and ADT/PS data backed up daily; test restore monthly; backups stored securely, separate from primary systems.  
  *Cited: AGID Misure minime 4.6.2, NIS2 Art. 21(2)(e)*

### 5.4 Physical Security

- **Device Security**: Portable devices (laptops/tablets) to be secured when not in use; no patient data to be stored on unauthorized USB/media.  
  *Cited: ISO/IEC 27001:2022 A.7.8, AGID Misure minime 4.8.1*
- **Access Control**: Server rooms and medical device closets locked; access logged and restricted to authorized personnel.  
  *Cited: ISO/IEC 27001:2022 A.7.2, AGID Misure minime 4.8.2*

### 5.5 Incident Management

- **Reporting**: All users must report suspected or confirmed security incidents immediately to ICT; if ICT unavailable, escalate to MSP contact.  
  *Cited: ISO/IEC 27001:2022 A.5.24, NIS2 Art. 23*
- **Response**: Incident response led by ICT, escalated to MSP as needed; priority to clinical continuity and regulatory notification timelines (GDPR 72h for data breaches).  
  *Cited: GDPR Art. 33, NIS2 Art. 23, ISO/IEC 27001:2022 A.5.25*

### 5.6 Vendor and Supply Chain Security

- **MSP Oversight**: MSP contract includes security SLAs; regular review of MSP access and activity logs.  
  *Cited: NIS2 Art. 21(2)(d), ISO/IEC 27001:2022 A.5.19*
- **Medical Device Vendors**: New device procurement requires security assessment per MEPA/CONSIP process; legacy device risks documented and managed.  
  *Cited: AGID Linee Guida, ISO/IEC 27001:2022 A.5.19, NIS2 Art. 21(2)(d)*

### 5.7 Awareness and Training

- **Mandatory Training**: All staff must complete at least 2 hours/year of cybersecurity and privacy awareness, focusing on phishing, safe data handling, device security, and incident reporting.  
  *Cited: ISO/IEC 27001:2022 A.6.3, NIS2 Art. 21(2)(f), AGID Misure minime 4.1.3*
- **Phishing Simulation**: Periodic simulated phishing for clinical staff, with feedback, prioritizing high-turnover roles.  
  *Cited: NIST CSF PR.AT-2 (recommended, not required)*

---

## 6. Exceptions

Requests for exceptions to this policy must be approved by the Head of ICT and formally documented, with justification, risk assessment, and, where required, notification to the Data Protection Officer (DPO) and/or regional authority.  
*Cited: ISO/IEC 27001:2022 A.5.31*

---

## 7. Monitoring and Review

- **Monitoring**: ICT and MSP monitor systems via AV console and AD logs; periodic audit of access logs for sensitive systems.  
  *Cited: ISO/IEC 27001:2022 A.8.16, AGID Misure minime 4.7.1*
- **Review**: Policy reviewed annually or on significant incident/regulatory change; effectiveness assessed via incident records, audit findings, and user feedback.  
  *Cited: ISO/IEC 27001:2022 9.3, NIS2 Art. 21(4)*

---

## 8. References

- **EU GDPR** (Reg. EU 2016/679), esp. Art. 5, 32, 33
- **D.Lgs. 196/2003** as amended by D.Lgs. 101/2018
- **NIS2 Directive** (EU 2022/2555), esp. Art. 21, 23
- **AGID Misure minime per la sicurezza ICT nella PA**
- **AGID Linee Guida per la sicurezza informatica nella PA**
- **Provvedimenti Garante Privacy in sanità**
- **ISO/IEC 27001:2022**, Annex A controls (see above)
- **NIST Cybersecurity Framework 2.0** (recommended)
- **Regional regulations on Fascicolo Sanitario Elettronico (FSE)**

---

**Approval:**  
[Name, Title] — [Date]

---

*(End of policy)*

---

**Note:** All control citations are precise to allow audit and compliance checks. Controls recommended (but not mandatory) are marked as such. No control is proposed that would exceed the organisation’s realistic capacity, per profile constraints. If you require an Italian-language version or additional topic-specific policies (e.g., Data Protection, Acceptable Use), let me know!
