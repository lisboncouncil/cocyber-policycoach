---
config: C0
context_id: ctx-H
policy_id: P4
policy_name: Access Control Policy
policy_short: accesscontrol
metadata:
  config: C0
  model: gpt-4.1-2025-04-14
  input_tokens: 892
  output_tokens: 2515
  total_tokens: 3407
  latency_s: 52.225
  tool_calls: []
  raw_provider_id: chatcmpl-DcZ9KVxLqtkRS622WDYnBB68vLvrc
sources_count: 0
sources: []
prompt_chars: 4102
answer_chars: 9665
generated_at_unix: 1778084002
---

---

**Organisation:** [Hospital Name], ASL [Region]  
**Policy Title:** Access Control Policy  
**Effective Date:** [DD/MM/YYYY]  
**Policy Owner:** ICT Manager / Responsabile della Protezione dei Dati (DPO)  
**Review Cycle:** Annual, or upon significant change in regulations or systems; minimum review every 12 months  
**Version:** 1.0

---

# 1. Purpose

The purpose of this Access Control Policy is to define the rules and principles for managing, granting, reviewing, and revoking access to information systems and data at [Hospital Name], in compliance with applicable Italian and EU regulations (GDPR, D.Lgs. 196/2003, NIS2, AGID guidelines), sector-specific requirements for healthcare, and in alignment with international standards (ISO/IEC 27001:2022, NIST CSF 2.0). The policy aims to protect patient safety and the confidentiality, integrity, and availability of health data, while supporting the hospital’s clinical, administrative, and technical operations.

---

# 2. Scope

This policy applies to all hospital staff (clinical, administrative, technical/facility), external consultants, service providers (including MSP personnel), trainees, and contractors who access hospital information systems, networks, or data, regardless of location or device used.  
It covers all electronic systems including, but not limited to:  
- Cartella Clinica Elettronica (EHR, FSE)  
- PACS/RIS, LIS, ADT, Pharmacy  
- Active Directory, SPID/CIE federated services  
- Workstations, legacy clinical kiosks, and mobile devices  
- Physical and remote access to information assets

---

# 3. Roles and Responsibilities

- **ICT Manager (Responsabile ICT):**  
  - Policy owner; ensures implementation, maintenance, and review of access controls  
  - Approves user provisioning and de-provisioning processes  
  - Coordinates with MSP and Regional IT for federated identity  
  - Reports to Direzione Sanitaria and DPO

- **DPO (Responsabile della Protezione dei Dati):**  
  - Advises on GDPR, privacy, and data minimization aspects  
  - Reviews access rights to special categories of data (GDPR Art. 9)

- **System Administrators (Internal ICT and MSP):**  
  - Implement technical controls for user access  
  - Maintain access logs and support periodic access reviews

- **Department Heads (Clinical/Administrative):**  
  - Authorize access requests based on job requirements  
  - Notify ICT of changes in staff roles or departures (ISO/IEC 27001 A.9.2.2)

- **All Users:**  
  - Use only credentials assigned to them  
  - Refrain from sharing credentials  
  - Report suspected unauthorised access promptly (ISO/IEC 27001 A.9.3.1)

---

# 4. Principles

- **Least Privilege:** Access is granted only to the minimum information and resources required for legitimate work purposes. *(ISO/IEC 27001 A.9.1.2; NIST CSF PR.AC-6)*
- **Need to Know:** Special category data (e.g., health data, minors’ data) is accessible only to those whose roles require it. *(GDPR Art. 32, Art. 9; D.Lgs. 196/2003 Art. 2-sexies)*
- **Segregation of Duties:** No user shall have conflicting roles or excessive privileges that could permit abuse. *(ISO/IEC 27001 A.6.1.2; NIS2 Art. 21)*
- **Accountability:** All access to systems and data is attributable to a single, identifiable individual. *(GDPR Art. 5(1)(f); AGID Linee Guida 1/2017)*

---

# 5. Access Control Requirements and Controls

*Controls are mapped to primary sources; additional references provided where relevant.*

## 5.1. User Registration and De-registration

- All access rights must be provisioned through a formal, documented request and approval process, involving Department Head and ICT. *(ISO/IEC 27001 A.9.2.1; AGID "Misure Minime" 7.1)*
- User accounts must be deactivated or revoked immediately upon termination, role change, or contract expiration. *(ISO/IEC 27001 A.9.2.6; NIS2 Art. 21(2)(e); GDPR Art. 32)*

## 5.2. User Access Provisioning

- Access rights are assigned based on pre-defined role profiles (clinical, administrative, technical), limiting access to only necessary applications and data. *(ISO/IEC 27001 A.9.1.2; AGID "Misure Minime" 7.1.1)*
- Access to special category data (health data, minors' data) is logged and periodically reviewed. *(GDPR Art. 32; Provvedimento Garante Privacy 19/12/2019)*

## 5.3. Authentication

- All users authenticate via unique credentials (username/password) managed in Active Directory or via SPID/CIE federation for regional applications. *(AGID Linee Guida 1/2017; NIS2 Art. 21(2)(e))*
- Passwords must comply with complexity and renewal requirements as per AGID "Misure Minime" (minimum 8 characters, changed at least every 180 days). *(AGID "Misure Minime" 7.2.1)*
- Where supported by systems, two-factor authentication (2FA) is enabled for remote access to critical systems (e.g., EHR, PACS over VPN). *(ISO/IEC 27001 A.9.4.2; AGID "Misure Minime" 7.2.2; NIS2 Art. 21(2)(e))*
- Clinical kiosks/legacy devices: Where technical limitations prevent 2FA, compensating controls (e.g., session timeouts, physical security) must be implemented. *(Unsupported by ISO/IEC 27001, justified due to technical debt and resource constraints)*

## 5.4. Privileged Access

- Administrator or super-user rights are granted only to ICT staff and MSP personnel, with approval from ICT Manager. *(ISO/IEC 27001 A.9.2.3)*
- Privileged accounts are not to be used for routine operations; separate accounts for administrative and standard use are required. *(ISO/IEC 27001 A.9.2.3; NIST CSF PR.AC-4)*
- All privileged access must be logged; logs must be retained for a minimum of 6 months. *(AGID "Misure Minime" 13.2; Provv. Garante Privacy 27/11/2008)*

## 5.5. Review and Audit of Access Rights

- Access rights for all users (including MSP) must be reviewed at least annually and upon major role changes. *(ISO/IEC 27001 A.9.2.5; AGID "Misure Minime" 7.1.3)*
- Department Heads are responsible for confirming staff roles and access needs during review cycles.

## 5.6. Session Management and Timeout

- Workstations and mobile devices must be configured to automatically lock after a maximum of 15 minutes of inactivity. *(AGID "Misure Minime" 12.1; ISO/IEC 27001 A.11.2.9)*
- In point-of-care and emergency areas, session timeout can be adjusted to balance patient safety and security, with justification documented by ICT Manager. *(Unsupported by standards, justified by patient safety priority)*

## 5.7. Remote Access

- Remote access (including from home or external sites) to hospital systems is permitted only via secure, encrypted VPN managed by ICT/MSP, and subject to 2FA where feasible. *(ISO/IEC 27001 A.13.1.1; NIS2 Art. 21(2)(e); AGID "Misure Minime" 10.1)*

## 5.8. Physical Access

- Access to server rooms and network equipment is restricted to authorised technical staff. *(ISO/IEC 27001 A.11.1.1; AGID "Misure Minime" 8.1)*
- Portable/mobile devices containing personal data must be stored securely when not in use. *(GDPR Art. 32; AGID "Misure Minime" 9.1)*

## 5.9. Use of Shared or Generic Accounts

- Use of shared or generic accounts is strictly prohibited except where technical limitations (e.g., legacy kiosks) make it unavoidable. In such cases, ICT Manager must document compensating controls and review usage logs. *(ISO/IEC 27001 A.9.4.1; AGID "Misure Minime" 7.1.2)*

## 5.10. Third-Party Access (MSP, Vendors)

- All third-party access must be governed by formal contracts (MEPA/CONSIP) specifying confidentiality, minimum security measures, and audit rights. *(ISO/IEC 27001 A.15.1.1; NIS2 Art. 21(2)(d); AGID "Misure Minime" 15.1)*
- Third-party accounts must be time-limited and disabled when not required.

---

# 6. Exceptions

- Any exceptions to this policy must be formally documented, approved by the ICT Manager in consultation with the DPO, and reviewed annually.
- Exceptions must include justification, compensating controls, and a defined timeline for remediation if applicable.
- Where patient safety requires deviation (e.g., in life-critical emergency care), this must be documented and reported post-event to ICT and DPO.

---

# 7. Monitoring and Review

- ICT Manager and MSP will monitor access logs and user activity for signs of unauthorised access or policy violation, using available AV management and log tools. *(AGID "Misure Minime" 13.1; ISO/IEC 27001 A.12.4.1)*
- All suspected or confirmed access control incidents must be reported immediately to the ICT Manager, who will activate the incident response procedure.
- This policy and its effectiveness will be reviewed at least annually, and whenever there are significant changes in technology, regulations, or operations.
- Outcomes of audits and reviews will be reported to senior management and DPO, and corrective actions tracked.

---

# 8. References

- **EU General Data Protection Regulation (GDPR) (Regulation EU 2016/679)**
- **D.Lgs. 196/2003 as amended by D.Lgs. 101/2018** (“Codice in materia di protezione dei dati personali”)
- **NIS2 Directive (EU 2022/2555), Art. 21**
- **AGID Linee Guida per la Sicurezza Informatica nella PA**
- **AGID Misure Minime di Sicurezza ICT per la PA (2017)**
- **Provvedimenti del Garante Privacy in materia sanitaria (e.g., 19/12/2019, 27/11/2008)**
- **ISO/IEC 27001:2022** (not certified, target framework; controls A.9, A.13, A.15, etc.)
- **NIST Cybersecurity Framework (CSF) 2.0** (functions PR.AC, DE.CM)
- **Regional regulations on Fascicolo Sanitario Elettronico (FSE)**
- **Hospital Information Security Procedures** (internal)

---

**Approval:**  
[Name], ICT Manager  
[Name], DPO  
[Signature, Date]

---

**Document History:**  
- Version 1.0 | [Effective Date] | Initial issue

---
