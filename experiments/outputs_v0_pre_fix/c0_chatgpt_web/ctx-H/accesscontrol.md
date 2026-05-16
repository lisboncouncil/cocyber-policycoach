---
config: C0+web
context_id: ctx-H
policy_id: P4
policy_name: Access Control Policy
policy_short: accesscontrol
metadata:
  config: C0+web
  model: gpt-4.1-2025-04-14
  input_tokens: 1186
  output_tokens: 1895
  total_tokens: 3081
  latency_s: 22.09
  tool_calls: []
  raw_provider_id: resp_0224f437e7c665a70069fb69679758819fbfc61c8325057aeb
sources_count: 0
sources: []
prompt_chars: 4102
answer_chars: 6903
generated_at_unix: 1778084221
---

---

**Access Control Policy**  
**Organisation:** [Hospital Name], ASL [Region], Servizio Sanitario Nazionale  
**Effective Date:** [Insert Date]  
**Policy Owner:** Director of ICT / IT Operations Lead  
**Review Cycle:** Annual (or upon significant regulatory/operational change)

---

### 1. **Purpose**

This Access Control Policy establishes rules for managing access to information systems and data at [Hospital Name], in compliance with GDPR, Codice Privacy, NIS2, AGID Linee Guida, and sectoral best practices (NIST CSF 2.0, ISO/IEC 27001:2022). The policy aims to ensure that access to patient, employee, and organisational data is granted only to authorised users, supports patient safety, and maintains operational continuity.

---

### 2. **Scope**

This policy applies to all staff (clinical, administrative, technical), contractors, and third-party service providers (e.g., MSP, medical device vendors) who access the hospital’s information systems, electronic health records (EHR), medical devices, and networked resources. It covers workstations, clinical kiosks, mobile devices, and remote access.

---

### 3. **Roles and Responsibilities**

| Role | Responsibilities |
|------|------------------|
| **IT Operations Lead** | Policy maintenance, access approval, control implementation, periodic review |
| **Managed Service Provider (MSP)** | Technical enforcement of access controls, logging, reporting incidents, supporting audits |
| **Department Heads** | Authorisation of clinical/administrative staff access, notification of staff changes |
| **All Users** | Use only assigned credentials, report anomalies or suspected breaches |
| **Data Protection Officer (DPO)** | Oversight for GDPR/data protection compliance, breach notification |

---

### 4. **Principles**

- **Need-to-Know & Least Privilege:** Access is granted strictly as required for job functions. *(ISO 27001:2022, A.9.1.2; NIST CSF PR.AC-6)*
- **Role-Based Access Control (RBAC):** Assignment of permissions is role-driven, mapped to clinical/administrative functions. *(ISO 27001:2022, A.9.2.1; AGID Linee Guida 2.1.1)*
- **Segregation of Duties:** Wherever possible, critical tasks are divided to prevent conflict of interest and reduce error/fraud risk. *(ISO 27001:2022, A.6.1.2)*
- **Regulatory Compliance:** Access management aligns with GDPR (Art. 32), Codice Privacy, NIS2, and AGID’s Misure Minime. 

---

### 5. **Access Control Requirements**

#### 5.1 **User Access Management**

- **Account Provisioning:**  
  - All user accounts must be formally requested and approved by Department Heads, documented by IT. *(ISO 27001:2022, A.9.2.2; AGID Misure Minime 2.3.1)*
  - Accounts for clinical systems (EHR, PACS, LIS, ADT, Pharmacy) must be unique and tied to individual identities. *(GDPR Art. 32; NIS2 Art. 21(2)(e))*
- **Authentication Mechanisms:**  
  - Hospital staff authenticate via on-prem Active Directory; external access uses SPID/CIE federation. *(AGID Linee Guida 2.1.1/2.2.1)*
  - Shared or generic accounts are prohibited except for clinical kiosks/devices where traceability is maintained via device logs. *(ISO 27001:2022, A.9.2.3)*
  - Passwords must meet complexity and expiry standards: at least 10 characters, changed annually or upon suspected compromise. *(AGID Misure Minime 2.2.1; ISO 27001:2022, A.9.4.3)*
- **Account Review & Removal:**  
  - Access rights are reviewed semi-annually and upon staff role change or termination. *(ISO 27001:2022, A.9.2.5; AGID Misure Minime 2.3.1)*
  - Departed staff accounts must be disabled within 24 hours of contract end. *(NIS2 Art. 21(2)(e); GDPR Art. 32)*

#### 5.2 **Access to Special Category Data (Health/Minors/Employees)**

- **Minimum Necessary Access:**  
  - Clinical records, minors’ data, and employee data are only accessible to staff with a direct care or administrative relationship. *(GDPR Art. 5(1)(c); Provvedimenti Garante Privacy in sanità)*
- **Audit Trails:**  
  - All access to EHR and sensitive systems is logged and reviewed at least annually. *(GDPR Art. 30; ISO 27001:2022, A.12.4.1)*

#### 5.3 **Physical Access Controls**

- **Device Security:**  
  - Workstations and mobile devices in clinical areas must be locked when unattended. *(AGID Misure Minime 2.4.3)*
  - Mobile devices must be encrypted and, where possible, use PIN/biometric locks. *(NIS2 Art. 21(2)(d); ISO 27001:2022, A.11.2.6)*
  - Report loss or theft of devices immediately to IT. *(ISO 27001:2022, A.11.2.9)*

#### 5.4 **Remote and Third-Party Access**

- **Remote Access:**  
  - Remote access (e.g., MSP, telemedicine providers) is restricted to essential tasks, using VPN with MFA where technically feasible. *(NIS2 Art. 21(2)(e); ISO 27001:2022, A.13.1.1)*
  - Each third-party session must be authorised by IT, with logs maintained for accountability. *(AGID Linee Guida 2.2.1; ISO 27001:2022, A.9.4.1)*
- **Vendor Access Review:**  
  - Access by external vendors is reviewed quarterly and revoked immediately after contract/service end. *(ISO 27001:2022, A.15.1.2)*

#### 5.5 **Legacy Systems and Clinical Kiosks**

- **Compensating Controls:**  
  - Where clinical kiosks/legacy systems cannot support modern authentication, access is restricted by physical controls and network segmentation. *(AGID Misure Minime 2.4.2/2.4.4; ISO 27001:2022, A.13.1.3)*

---

### 6. **Exceptions**

- Any exceptions to this policy must be justified in writing, approved by the IT Operations Lead and DPO, and documented for audit.
- Exception requests will consider patient safety, clinical workflow, and regulatory risk.

---

### 7. **Monitoring and Review**

- **Monitoring:**  
  - Access logs are periodically reviewed by IT and the MSP for anomalies or unauthorised access. *(ISO 27001:2022, A.12.4.1; NIS2 Art. 21(2)(d))*
  - Incidents or breaches are escalated per the hospital’s incident response procedure.
- **Review:**  
  - This policy is reviewed at least annually, or after significant changes to regulations, IT systems, or clinical workflow.
  - Audit outcomes and lessons learned from incidents inform updates.

---

### 8. **References**

- **Regulatory:**
  - GDPR (Regulation EU 2016/679), especially Art. 5, 32, 30
  - Codice Privacy (D.Lgs. 196/2003 as amended)
  - NIS2 Directive (EU 2022/2555), Art. 21
  - AGID Linee Guida per la sicurezza informatica nella PA (esp. 2.1.1, 2.2.1, 2.3.1, 2.4.x)
  - Provvedimenti Garante Privacy in sanità
  - Misure minime AGID per la PA
- **Standards:**
  - ISO/IEC 27001:2022 (esp. A.6, A.9, A.11, A.12, A.13, A.15)
  - NIST CSF 2.0 (PR.AC-1 to PR.AC-6)
- **Other:**
  - Regional regulations on Fascicolo Sanitario Elettronico (FSE)
  - Vendor documentation (for technical controls)
  
---

**Document History**  
| Version | Date | Author | Comments |
|---------|------|--------|----------|
| 1.0 | [Insert Date] | IT Operations Lead | Initial issue |

---

**End of Policy**

---
