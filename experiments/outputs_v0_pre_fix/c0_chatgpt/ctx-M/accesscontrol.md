---
config: C0
context_id: ctx-M
policy_id: P4
policy_name: Access Control Policy
policy_short: accesscontrol
metadata:
  config: C0
  model: gpt-4.1-2025-04-14
  input_tokens: 1015
  output_tokens: 2634
  total_tokens: 3649
  latency_s: 36.537
  tool_calls: []
  raw_provider_id: chatcmpl-DcZBRLFpMFCNYuXV3iTmmb9RxYcKT
sources_count: 0
sources: []
prompt_chars: 4950
answer_chars: 10422
generated_at_unix: 1778084117
---

---

**NATO Allied Command Operations (SHAPE) — Romania Deployment**  
**Access Control Policy**  
**Document Reference:** NACO-R-AC-01  
**Effective Date:** 2024-07-01  
**Policy Owner:** ISSM, J6 Branch  
**Review Cycle:** Annual, or upon significant organisational or regulatory change  
**Classification:** NATO RESTRICTED

---

### 1. Purpose

The purpose of this Access Control Policy is to establish and govern access to physical, logical, and information assets within the NATO Allied Command Operations (SHAPE) deployment in Romania, in alignment with NATO, host-nation, and international regulatory requirements. The policy aims to ensure enforceable, auditable, and risk-based access controls that reflect the multinational, classified, and operational context of the detachment, supporting mission assurance for cyber defence, CIS operations, signals intelligence, and interoperability exercises.

---

### 2. Scope

This policy applies to all personnel assigned or attached to the detachment, including military members, NATO civilian staff, and cleared contractors, as well as all information systems, network domains (NU, NR, NS, MISSION SECRET), physical facilities, and communication assets under the detachment’s operational control. The policy applies to all access modalities (physical, logical, and remote), all classification levels, and all COMSEC assets.

---

### 3. Roles and Responsibilities

| Role | Responsibility |
|------|---------------|
| **Information Systems Security Manager (ISSM)** | Policy owner; ensures policy alignment, implementation, and auditability (C-M(2002)49; AC/322-D(2017)0009). |
| **Information Systems Security Officers (ISSOs)** | Day-to-day enforcement and monitoring of access controls per domain. |
| **Commanding Officer (CO)** | Approves access for mission-critical exceptions; enforces disciplinary consequences. |
| **COMSEC Custodian** | Manages access to COMSEC assets, ensures two-person integrity and chain of custody (AC/35-D/1015). |
| **Network Administrators** | Implement and maintain technical controls, monitor for violations. |
| **Security Operations Center (SOC)** | Monitors access logs, escalates incidents per NCIRC and NCSC processes. |
| **Personnel Security Officer (PSO)** | Validates personnel clearances and need-to-know; coordinates with national vetting authorities (AC/35-D/1029). |
| **All Users** | Comply with policy; report suspected violations. |

---

### 4. Principles

1. **Need-to-Know & Least Privilege:** Access is granted strictly on a need-to-know and least privilege basis, default-deny unless explicitly authorised (C-M(2002)49; NIST CSF PR.AC-4; ISO/IEC 27001:2022 A.5.15).
2. **Separation of Classification Domains:** Absolute technical and procedural separation between NU, NR, NS, and MISSION SECRET domains; no cross-domain access except through accredited NATO Cross-Domain Solutions (ACDS) (AC/322-D(2017)0009; AJP-3.20).
3. **Strong Authentication:** PKI-based, smart-card (CAC-equivalent) authentication is mandatory for all logical access; no password-only authentication permitted (NIST CSF PR.AC-1; ISO/IEC 27001:2022 A.5.17).
4. **Originator Control (ORCON):** Access to shared intelligence and operational products is further restricted by originator control where required (AJP-3.20).
5. **Two-Person Integrity (TPI):** Dual presence is required for access to high-grade COMSEC material and specific operational orders (AC/35-D/1015; COMSEC Policy).
6. **Auditability:** All access events for classified systems and COMSEC assets must be logged and auditable (C-M(2002)49; NIST CSF DE.CM-7; ISO/IEC 27001:2022 A.8.15).
7. **Personnel Security:** All users must have a valid personnel security clearance matching the classification level and specific mission need (AC/35-D/1029; AJP-3.20).

---

### 5. Requirements / Controls

#### 5.1. Access Authorisation

- **5.1.1. User Access Provisioning:**  
  Access to all systems (physical and logical) requires formal authorisation by the relevant line manager and security authority, documented in the NATO-mandated access control register. (C-M(2002)49 Art. 24; ISO/IEC 27001:2022 A.5.18)
- **5.1.2. Clearance Verification:**  
  No user shall be granted access to classified resources unless their personnel security clearance is confirmed at or above the required level and validated by the PSO. (AC/35-D/1029; NIST CSF PR.AC-3)
- **5.1.3. Need-to-Know Enforcement:**  
  Access is limited to information and assets strictly necessary for assigned duties, enforced by system configuration and procedural checks. (C-M(2002)49 Art. 25; ISO/IEC 27001:2022 A.5.15)
- **5.1.4. Access Review:**  
  All access rights shall be reviewed at least quarterly and upon role change, detachment, or termination. (ISO/IEC 27001:2022 A.5.19; NIST CSF PR.AC-4)

#### 5.2. Authentication and Access Mechanisms

- **5.2.1. Strong Authentication:**  
  All logical access must use NATO-approved PKI and smart card authentication. Password-only authentication is not permitted on classified domains. (AC/322-D(2017)0009; NIST CSF PR.AC-1)
- **5.2.2. Segregated Identities:**  
  Separate identities and credentials shall be used for each classification domain; no cross-domain identity federation is permitted. (AC/322-D(2017)0009; NATO INFOSEC Technical Directive)
- **5.2.3. Access to Cross-Domain Solutions:**  
  Only specifically authorised personnel may access Cross-Domain Solutions, and only for permitted data transfer purposes. All transfers must be logged and subject to approval. (AJP-3.20; C-M(2002)49)
- **5.2.4. Session Management:**  
  Sessions shall automatically lock after 15 minutes of inactivity on classified systems. (ISO/IEC 27001:2022 A.5.17)

#### 5.3. Physical and Environmental Access

- **5.3.1. Physical Access Controls:**  
  Access to secure areas (server rooms, COMSEC vaults, network operation centres) is controlled by badge, guard, and/or biometric systems, with logs retained for at least 12 months. (C-M(2002)49 Art. 32; ISO/IEC 27001:2022 A.7.1)
- **5.3.2. Two-Person Integrity (TPI):**  
  Two cleared and authorised persons are required for physical access to high-grade COMSEC areas and when handling cryptographic material. (AC/35-D/1015; NIST CSF PR.AC-5)
- **5.3.3. Visitor Control:**  
  All visitors to controlled areas must be escorted at all times and logged, with records maintained per NATO and host nation requirements. (AC/35-D/1015; ISO/IEC 27001:2022 A.7.2)

#### 5.4. COMSEC and Sensitive Asset Access

- **5.4.1. Dual-Key Procedures:**  
  For high-grade COMSEC assets and select operational orders, dual authorisation (two-person rule) is enforced for access, change, or removal. (AC/35-D/1015)
- **5.4.2. Chain of Custody:**  
  All access and transfer of COMSEC assets must be documented in an auditable register, signed by both persons involved. (AC/35-D/1015)

#### 5.5. Contractor and Third-Party Access

- **5.5.1. Security Screening:**  
  All host-nation contractors and third parties must undergo security screening to NATO and host-nation standards before access is granted. (AC/35-D/1029; NIS2 Directive)
- **5.5.2. Restricted Access:**  
  Contractors are granted access only to the minimum systems and information required for their contractual duties, with technical controls to enforce such limitations. (NIST CSF PR.AC-3; ISO/IEC 27001:2022 A.5.15)
- **5.5.3. Data Protection:**  
  Civilian and contractor personal data are processed in compliance with GDPR and host nation cybersecurity law, subject to SOFA limitations. (GDPR Art. 32; Romanian CSL)

#### 5.6. Account Lifecycle Management

- **5.6.1. Account Creation:**  
  All accounts must be created based on validated requests, including clearance and need-to-know checks. (ISO/IEC 27001:2022 A.5.18)
- **5.6.2. Account Deactivation:**  
  All accounts must be deactivated within 24 hours of personnel departure, contract termination, or role change removing the need for access. (ISO/IEC 27001:2022 A.5.18)
- **5.6.3. Periodic Recertification:**  
  At least quarterly, access lists and user accounts are reconciled against current personnel rosters. (ISO/IEC 27001:2022 A.5.19)

#### 5.7. Privileged Access

- **5.7.1. Justification and Approval:**  
  Privileged (admin) access is restricted to essential personnel, with explicit written justification and approval by the ISSM. (C-M(2002)49; NIST CSF PR.AC-4)
- **5.7.2. Privileged Activity Monitoring:**  
  All privileged access events are logged and subject to enhanced review by the SOC. (NIST CSF DE.CM-7; ISO/IEC 27001:2022 A.8.15)
- **5.7.3. Segregation of Duties:**  
  Where feasible, duties and access for critical functions (e.g., system administration and security monitoring) are separated to minimise risk. (ISO/IEC 27001:2022 A.6.4)

---

### 6. Exceptions

Requests for exception to this policy must be formally submitted to the ISSM, justified on mission, operational, or technical grounds, and subject to risk assessment. Exceptions must be approved in writing by the ISSM and, where required, the Commanding Officer. All exceptions will be logged and reviewed during annual policy review. No exceptions will be granted that contravene NATO security policy (C-M(2002)49) or host nation law.

---

### 7. Monitoring and Review

- The ISSM and SOC will continuously monitor compliance with this policy via system logs, access reviews, and periodic audits.
- Violations will be escalated per NCIRC process, with notification to NCSC and host-nation CERT as required.
- This policy will be reviewed annually or upon significant change in mission, technology, or regulatory environment.
- Audit findings and incident lessons learned will inform future policy updates.

---

### 8. References

- NATO Information Security Policy (C-M(2002)49) and successor versions  
- AC/35-D/1015: Security within NATO (COMSEC)  
- AC/35-D/1029: Personnel Security  
- AC/322-D(2017)0009: NATO INFOSEC Technical and Implementation Directive  
- Allied Joint Doctrine for Cyberspace Operations (AJP-3.20)  
- NATO Cyber Defence Pledge (2016)  
- Romanian Cybersecurity Law (Law 58/2019, NIS/NIS2 transposition)  
- General Data Protection Regulation (GDPR)  
- NIST Cybersecurity Framework (CSF) 2.0  
- ISO/IEC 27001:2022 and ISO/IEC 27002:2022  
- NATO SOFA  
- NCSC / NCIRC Incident Response Processes  

---

**Approved by:**  
[Name, Rank], ISSM, J6 Branch  
Date: [to be completed]

---
