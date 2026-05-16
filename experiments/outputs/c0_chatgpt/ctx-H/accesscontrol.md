---
config: C0
context_id: ctx-H
policy_id: P3
policy_name: Access Control Policy
policy_short: accesscontrol
metadata:
  config: C0
  model: gpt-4.1-2025-04-14
  input_tokens: 1146
  output_tokens: 2221
  total_tokens: 3367
  latency_s: 18.999
  tool_calls: []
  raw_provider_id: chatcmpl-DcZa2CvTycj4RBxkDBzT8KFhs5W20
sources_count: 0
sources: []
prompt_chars: 4669
answer_chars: 8743
generated_at_unix: 1778085624
---

---

**Access Control Policy**

**Organisation:** [Redacted] Provincial General Hospital, ASL [Redacted], Italy  
**Effective Date:** 2024-07-01  
**Policy Owner:** Direttore Amministrativo (Administrative Director)  
**Review Cycle:** Annual (every 12 months), or upon significant change in regulatory or threat environment  

---

### 1. Purpose

This Access Control Policy establishes the principles and requirements for the management of access to information systems, applications, and data within [Redacted] Provincial General Hospital. The purpose is to ensure that access to information and systems is granted only to authorised individuals, in accordance with legal, regulatory, and clinical requirements, while supporting patient safety and business continuity. This policy aligns with the General Data Protection Regulation (GDPR), NIS2 Directive, AGID Guidelines, and international standards (ISO/IEC 27001:2022, NIST CSF 2.0).

---

### 2. Scope

This policy applies to all staff (clinical, administrative, technical), contractors, external service providers (including Managed Service Providers), and any third parties who access the hospital’s information systems, networks, or data, whether on-site or remotely. It covers all IT assets (workstations, mobile devices, servers, network equipment), applications (including EHR, PACS/RIS, LIS, ADT, Pharmacy), and data (including special category health data and personal data of minors) under the hospital’s control.

---

### 3. Roles and Responsibilities

**Administrative Director (Policy Owner):**
- Ensures the policy is implemented and reviewed.
- Reports to the hospital board and regional ASL.

**IT Manager (internal IT staff lead):**
- Administers user accounts and access permissions.
- Coordinates with the Managed Service Provider (MSP) for technical enforcement.
- Maintains records of access rights.

**Managed Service Provider (MSP):**
- Implements technical controls as per contract.
- Provides reports on access management.
- Notifies hospital of access-related incidents.

**Department Heads:**
- Approve access requests for their team members.
- Ensure prompt notification of staff role changes or departures.

**All Users:**
- Use only their assigned credentials.
- Report any suspected unauthorised access or security incidents.

---

### 4. Principles

#### 4.1. Least Privilege  
Access rights are granted based on the minimum necessary privileges required to perform job functions.  
**References:** ISO/IEC 27001:2022 A.5.18; NIST CSF PR.AC-6; GDPR Art. 32(1)(b); AGID "Misure minime" 8.1

#### 4.2. Need-to-Know  
Access to special category data (health records, minors' data) is restricted to personnel with a legitimate clinical or administrative need.  
**References:** GDPR Art. 5(1)(c); ISO/IEC 27001:2022 A.5.13

#### 4.3. Segregation of Duties  
Responsibilities are distributed to reduce risk of unauthorised or fraudulent activity.  
**References:** ISO/IEC 27001:2022 A.5.17; NIS2 Annex I, 2(c)

#### 4.4. Accountability  
All access to systems and data is attributable to a unique, identifiable individual or service account.  
**References:** GDPR Art. 5(1)(f); AGID Linee Guida 5.2.2; ISO/IEC 27001:2022 A.5.15

#### 4.5. Regulatory Compliance  
Controls reflect the requirements of GDPR, NIS2, AGID, and Garante Privacy provisions for the health sector.  
**References:** See Section 8

---

### 5. Access Control Requirements

#### 5.1. User Identification and Authentication

- **Unique User IDs:** Each user is assigned a unique identifier; shared credentials are prohibited.  
  *References:* ISO/IEC 27001:2022 A.5.15; AGID "Misure minime" 8.2.1; NIS2 Art. 21(2)(a)

- **Authentication:**  
   - Internal users authenticate via on-premises Active Directory.  
   - Access to regional platforms (FSE, SPID/CIE) uses regional federation mechanisms.  
   - Multi-factor authentication (MFA) is required for remote/VPN access; for local clinical access, MFA is strongly recommended where workflow allows.  
   *References:* AGID "Misure minime" 8.2.2; NIST CSF PR.AC-7; ISO/IEC 27001:2022 A.5.16

- **Password Management:**  
   - Passwords must meet complexity requirements (minimum 10 characters, mix of types); changed at least every 12 months or immediately upon suspected compromise.  
   - Default passwords must be changed upon first use.  
   *References:* AGID "Misure minime" 8.2.3; ISO/IEC 27001:2022 A.5.16

#### 5.2. Authorisation and Access Provisioning

- **Role-Based Access Control (RBAC):**  
   - Access rights are assigned based on defined roles (clinical, administrative, technical), in line with job functions and the principle of least privilege.  
   *References:* ISO/IEC 27001:2022 A.5.18; NIST CSF PR.AC-4

- **Access Requests:**  
   - All access requests must be approved by the relevant Department Head and logged by IT.  
   - Temporary access (e.g., for agency staff) is time-limited and reviewed weekly.  
   *References:* ISO/IEC 27001:2022 A.5.18

- **Access Reviews:**  
   - User access rights are reviewed at least every six months, and upon role changes or termination.  
   - Orphaned accounts are disabled within 24 hours of user departure.  
   *References:* ISO/IEC 27001:2022 A.5.18; AGID "Misure minime" 8.2.4

#### 5.3. Privileged Access Management

- **Administrative Privileges:**  
   - Privileged accounts (e.g., domain admins, local administrators) are strictly limited, documented, and monitored.  
   - Use of privileged accounts for non-administrative tasks is prohibited.  
   *References:* ISO/IEC 27001:2022 A.5.18; NIS2 Art. 21(2)(c)

- **Third-Party Access:**  
   - MSP and vendor access is controlled, time-limited, and monitored; remote sessions are logged and, where possible, supervised.  
   *References:* NIS2 Art. 21(2)(f); AGID "Misure minime" 8.2.5

#### 5.4. Physical and Device Access

- **Workstations:**  
   - Clinical kiosks and point-of-care devices automatically lock after 5 minutes of inactivity.  
   - Legacy systems are isolated on clinical VLANs; access is restricted and usage logs are retained.  
   *References:* ISO/IEC 27001:2022 A.7.2; AGID "Misure minime" 8.3

- **Mobile Devices:**  
   - All mobile devices must implement device encryption, PIN/biometric lock, and remote wipe capability.  
   - Loss or theft must be reported immediately to IT.  
   *References:* GDPR Art. 32(2); ISO/IEC 27001:2022 A.8.1

#### 5.5. Logging and Monitoring

- **Access Logging:**  
   - All access to EHR, PACS, and other critical systems is logged, with logs retained for at least 12 months.  
   - Regular (at least quarterly) review of access logs for anomalies or unauthorised access.  
   *References:* GDPR Art. 32(1)(d); NIS2 Art. 21(2)(g); AGID "Misure minime" 8.6

#### 5.6. Remote Access

- **VPN Access:**  
   - Remote access is permitted only via hospital-approved VPN with MFA and is restricted by role.  
   - Remote desktop access to clinical systems is not permitted except for documented exceptions.  
   *References:* AGID "Misure minime" 8.4; NIST CSF PR.AC-3

---

### 6. Exceptions

Requests for exceptions to this policy must be submitted in writing to the Administrative Director with justification, risk assessment, and proposed compensating controls. Exceptions are granted only for essential clinical or operational needs, documented, and reviewed at least annually. Controls affecting patient safety and emergency care may be adapted in consultation with clinical leadership, provided that regulatory minimums are maintained.

---

### 7. Monitoring and Review

- Compliance with this policy will be monitored by the IT Manager and the MSP through regular access reviews, log analysis, and incident reporting.
- The policy will be reviewed annually, or following significant changes in regulatory requirements, business processes, or threat landscape.
- Breaches of this policy will be managed as security incidents and may result in disciplinary or contractual action.

---

### 8. References

- **EU Regulation 2016/679 (GDPR)**: Art. 5, Art. 32
- **D.Lgs. 196/2003 as amended by D.Lgs. 101/2018**: Art. 33, 34
- **Directive (EU) 2022/2555 (NIS2)**: Art. 21, Annex I
- **AGID "Misure minime di sicurezza ICT per la PA"**: Sections 8, 9
- **AGID Linee Guida sulla sicurezza informatica nella PA**: Sections 5.2, 5.3
- **Provvedimenti Garante Privacy in sanità**: [Specific measures for EHR and health record access]
- **ISO/IEC 27001:2022**: Controls A.5.13–A.5.19, A.7.2, A.8.1
- **NIST Cybersecurity Framework v2.0**: PR.AC (Access Control), DE.CM (Security Continuous Monitoring)
- **Regional FSE Regulations**: [As applicable]

---

**Document History:**  
- Version 1.0 – 2024-07-01 – Initial publication

---

**End of Policy**
