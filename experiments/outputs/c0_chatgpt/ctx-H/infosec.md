---
config: C0
context_id: ctx-H
policy_id: P5
policy_name: General Cybersecurity Policy
policy_short: infosec
metadata:
  config: C0
  model: gpt-4.1-2025-04-14
  input_tokens: 1148
  output_tokens: 2660
  total_tokens: 3808
  latency_s: 24.648
  tool_calls: []
  raw_provider_id: chatcmpl-DcZaf6N0aoMWAGTetkVj7dCgdU1qn
sources_count: 0
sources: []
prompt_chars: 4683
answer_chars: 9331
generated_at_unix: 1778085669
---

---
**General Cybersecurity Policy**

**Organisation:** [Redacted] Provincial General Hospital  
**Governance:** ASL [Region], Servizio Sanitario Nazionale, Italy  
**Effective Date:** 2024-07-01  
**Policy Owner:** Hospital Director (delegated ICT Security Lead)  
**Review Cycle:** Annual (every 12 months) or as mandated by regulatory updates  
**Working Language:** Italian (policy in English for reference)

---

### 1. Purpose

This policy establishes the general principles and minimum requirements for cybersecurity at [Redacted] Provincial General Hospital, in compliance with relevant Italian and EU legislation, sector-specific regulations, and best practices (NIST CSF 2.0, ISO/IEC 27001:2022). The policy aims to protect the confidentiality, integrity, and availability of health and personal data, ensure continuity of clinical operations, and safeguard against cyber threats, including ransomware, data leaks, and supply-chain attacks.  
**References:**  
- GDPR, Art. 32  
- D.Lgs. 196/2003, as amended  
- NIS2 (Directive EU 2022/2555)  
- AGID Linee Guida per la sicurezza informatica nella PA  
- ISO/IEC 27001:2022, cl. 5, 6, 8  
- NIST CSF 2.0, Identify/Protect/Detect/Respond/Recover

---

### 2. Scope

This policy applies to all staff (clinical, administrative, technical/facility), contractors, external service providers (including MSPs), and any third parties with access to the hospital’s information systems, networks, or physical assets. It covers all IT systems, medical devices connected to the network, mobile and workstation endpoints, and all forms of data (digital and paper) processed or stored by the Hospital.

---

### 3. Roles and Responsibilities

**3.1 Hospital Director**  
- Ultimate accountability for cybersecurity and data protection  
**(ISO/IEC 27001:2022 cl. 5.3; GDPR Art. 24, 32)**

**3.2 ICT Security Lead (delegated; internal IT manager or external MSP as per contract)**  
- Day-to-day coordination of cybersecurity controls  
- Liaison with regional ASL/SSN DPO, Data Protection Authority, and external security providers  
**(ISO/IEC 27001:2022 cl. 5.3; NIS2 Art. 21)**

**3.3 All Staff**  
- Adhere to this policy and related procedures  
- Complete mandatory cybersecurity training  
- Promptly report incidents or suspicious activities  
**(GDPR Art. 32; AGID Linee Guida; NIST CSF 2.0 PR.AT)**

**3.4 External Service Providers (MSP, vendors)**  
- Comply with hospital security requirements  
- Report incidents and cooperate in investigations  
**(NIS2 Art. 21; ISO/IEC 27001:2022 cl. 5.1, 8.1.4)**

---

### 4. Principles

4.1 **Patient Safety and Service Continuity**  
Controls must not impede urgent clinical workflows or patient care.  
**(Unsupported, sector-specific prioritisation)**

4.2 **Legal Compliance**  
All processing of health and personal data must comply with GDPR, Italian law, and sector regulations.  
**(GDPR Art. 5, 32; D.Lgs. 196/2003; AGID Linee Guida)**

4.3 **Risk-based Approach**  
Security controls will be proportionate to the risks identified, with special focus on ransomware, data leaks, supply chain compromise, and physical theft.  
**(ISO/IEC 27001:2022 cl. 6.1; NIST CSF 2.0 ID.RA)**

4.4 **Least Privilege and Need-to-Know**  
Access to information and systems is restricted to the minimum required for role-based duties.  
**(ISO/IEC 27001:2022 A.9.1.2; GDPR Art. 32)**

4.5 **Continuous Improvement**  
The hospital will seek to improve its cybersecurity posture over time, aiming for alignment with ISO/IEC 27001:2022 and NIST CSF 2.0.  
**(ISO/IEC 27001:2022 cl. 10.2; NIST CSF 2.0 ID.IM)**

---

### 5. Policy Requirements and Controls

#### 5.1 Governance and Documentation

- Maintain and update a central register of ICT assets and data flows.  
  **(ISO/IEC 27001:2022 A.5.9, A.8.1; NIST CSF 2.0 ID.AM)**
- Ensure all policies and procedures are documented, version-controlled, and accessible to relevant staff.  
  **(ISO/IEC 27001:2022 cl. 7.5)**

#### 5.2 Human Resources and Awareness

- All staff must complete a minimum of 2 hours/year of cybersecurity awareness training, with onboarding for new hires within 1 month.  
  **(NIS2 Art. 21(2); ISO/IEC 27001:2022 A.6.3; AGID Linee Guida)**
- Training to include phishing, password management, and reporting procedures.  
  **(NIST CSF 2.0 PR.AT; AGID Linee Guida)**
- Disciplinary action for violations as per HR policy.  
  **(ISO/IEC 27001:2022 A.6.2.2)**

#### 5.3 Identity and Access Management

- All user accounts must be unique, with strong authentication (including SPID/CIE federation where available).  
  **(GDPR Art. 32; ISO/IEC 27001:2022 A.5.16, A.8.2.2)**
- Role-based access controls enforced for all clinical and administrative systems.  
  **(ISO/IEC 27001:2022 A.8.2.3)**
- Privileged access (e.g. domain admin, PACS admin) restricted and monitored; periodic access reviews at least annually.  
  **(ISO/IEC 27001:2022 A.8.2.4, A.8.2.5; NIST CSF 2.0 PR.AC)**

#### 5.4 System and Network Security

- Segregate networks for clinical, administrative, and medical imaging systems; maintain VLAN separation.  
  **(ISO/IEC 27001:2022 A.8.20; NIST CSF 2.0 PR.AC-5; AGID Linee Guida)**
- All endpoints (servers, workstations, mobile devices) must have up-to-date antivirus/anti-malware protection.  
  **(ISO/IEC 27001:2022 A.8.7.2)**
- Patching of supported systems within 30 days of vendor release; legacy systems (e.g., Windows kiosks) mitigated by network isolation and compensating controls.  
  **(ISO/IEC 27001:2022 A.8.8; AGID Misure Minime)**
- Remote access (VPN) restricted to authorised staff, with strong authentication and logging.  
  **(ISO/IEC 27001:2022 A.8.23, A.8.21)**

#### 5.5 Data Protection and Privacy

- All health and special category data processed in accordance with GDPR Art. 9, with encryption in transit and at rest where technically feasible.  
  **(GDPR Art. 32; ISO/IEC 27001:2022 A.8.24, A.8.25)**
- Regular review of data retention and deletion in line with legal/regulatory mandates.  
  **(GDPR Art. 5(e); D.Lgs. 196/2003 Art. 11)**
- Data sharing with third parties only under written agreement and with DPO approval where required.  
  **(GDPR Art. 28; NIS2 Art. 21)**

#### 5.6 Backup and Recovery

- Daily backups to on-site NAS; weekly off-site tape backup; retention and restoration procedures documented.  
  **(ISO/IEC 27001:2022 A.8.13; AGID Linee Guida)**
- Disaster Recovery (DR) tests at least every 18 months (move to annual as target).  
  **(ISO/IEC 27001:2022 A.5.30; NIST CSF 2.0 RC.IM)**
- RTO targets: 4 hours for EHR, 1 hour for ADT/PS.  
  **(Unsupported; set per organisational requirements)**

#### 5.7 Threat Detection and Response

- Maintain central AV console monitoring; ensure alerts reviewed by internal IT or MSP at least daily.  
  **(ISO/IEC 27001:2022 A.8.7.2; AGID Linee Guida)**
- All security incidents must be reported to IT lead and escalated to MSP per incident response procedure.  
  **(NIS2 Art. 23; ISO/IEC 27001:2022 A.5.24)**
- Document and periodically test (at least annually) incident response runbook; coordinate with regional CERT and DPO as required.  
  **(ISO/IEC 27001:2022 A.5.24, A.5.25; NIST CSF 2.0 RS.RP)**

#### 5.8 Supply Chain Security

- Contracts with MSP and vendors must include cybersecurity requirements and incident reporting obligations.  
  **(NIS2 Art. 21; ISO/IEC 27001:2022 A.5.19, A.5.20)**
- Risk assessment of critical suppliers at least every 2 years, focusing on medical device vendors and MSP.  
  **(NIS2 Art. 21(2); ISO/IEC 27001:2022 A.5.19)**

#### 5.9 Physical and Mobile Security

- Secure physical access to server rooms and sensitive areas; restrict access to authorised personnel only.  
  **(ISO/IEC 27001:2022 A.7.2, A.7.3)**
- Mobile devices (e.g. tablets, laptops) must be encrypted; staff must report loss/theft immediately.  
  **(GDPR Art. 32; ISO/IEC 27001:2022 A.8.25)**
- Regular awareness reminders on mobile device security at point-of-care.  
  **(NIST CSF 2.0 PR.AT)**

---

### 6. Exceptions

Requests for exception to this policy (e.g. due to clinical urgency, legacy system constraints) must be submitted in writing to the ICT Security Lead, who will assess the risk and, where appropriate, seek Director or DPO approval. Exceptions must be documented, time-limited, and reviewed at least annually.  
**(ISO/IEC 27001:2022 cl. 6.1.3)**

---

### 7. Monitoring and Review

- This policy will be reviewed at least annually, or upon significant change in legal, regulatory, or threat environment.  
  **(ISO/IEC 27001:2022 cl. 9.2, 10.1)**
- Compliance will be monitored via periodic audits (internal or external), with corrective actions tracked and reported to hospital management.  
  **(NIS2 Art. 21(3); ISO/IEC 27001:2022 cl. 9.2, 10.1)**
- Key performance indicators (e.g. training completion, backup success, incident response times) will be reported quarterly.  
  **(Unsupported; recommended operational best practice)**

---

### 8. References

- **GDPR (Regulation EU 2016/679)**
- **D.Lgs. 196/2003** (Codice Privacy, as amended)
- **NIS2 Directive (EU 2022/2555)**
- **AGID Linee Guida per la sicurezza informatica nella PA**
- **Provvedimenti Garante Privacy in sanità**
- **Misure minime AGID per la PA**
- **ISO/IEC 27001:2022**
- **NIST Cybersecurity Framework 2.0**

---

*End of Policy*
