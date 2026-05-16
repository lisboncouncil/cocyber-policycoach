---
config: C0
context_id: ctx-M
policy_id: P3
policy_name: Access Control Policy
policy_short: accesscontrol
metadata:
  config: C0
  model: gpt-4.1-2025-04-14
  input_tokens: 1366
  output_tokens: 2320
  total_tokens: 3686
  latency_s: 33.898
  tool_calls: []
  raw_provider_id: chatcmpl-DcZcolknSCGrZAJXGIppLAJzsjjTU
sources_count: 0
sources: []
prompt_chars: 6039
answer_chars: 9705
generated_at_unix: 1778085811
---

---
**Access Control Policy**

**Organisation:** NATO Multinational Military Detachment, Romania  
**Effective Date:** [YYYY-MM-DD]  
**Policy Owner:** Information Systems Security Manager (ISSM), J6  
**Review Cycle:** Annual, or as required by changes in NATO or host-nation regulations

---

### 1. Purpose

This Access Control Policy establishes requirements and responsibilities for controlling access to NATO, coalition, and national information systems and networks operated by the Detachment in Romania. The policy is designed to ensure protection of classified and sensitive information, support NATO operational effectiveness, and comply with NATO, host-nation, and coalition legal and regulatory obligations. The policy aligns with NATO Information Security Policy (C-M(2002)49), AC/322-D(2017)0009, the Romanian Cybersecurity Law (Law 58/2019), GDPR, NIST CSF 2.0, and ISO/IEC 27001:2022.

---

### 2. Scope

This policy applies to all Detachment personnel (military, civilian, contractor), all information systems (classified and unclassified), network domains (NU, NR, NS, MISSION SECRET), and all physical and logical access to information and information systems, including cross-domain solutions, mobile devices, and COMSEC assets.

---

### 3. Roles and Responsibilities

| Role                      | Responsibility                                                                                                                    |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| ISSM (J6)                 | Policy owner; ensures implementation, compliance, and review of access controls.                                                  |
| Security Staff (25 FTE)   | Administers access controls, monitors compliance, supports audits and investigations.                                             |
| System Owners             | Define access requirements for systems, ensure configuration aligns with policy and mission needs.                                 |
| Line Managers/Supervisors | Validate and authorise access requests based on role and need-to-know.                                                            |
| All Users                 | Comply with access controls, report violations or suspicious activity.                                                            |
| COMSEC Custodians         | Enforce access to COMSEC materials, maintain auditable records, apply dual-key/two-person controls as required.                   |
| Human Resources           | Ensure personnel screening, onboarding, and offboarding processes support access control objectives.                              |
| Host-Nation Liaison       | Coordinate access control compliance for contractors and civilians subject to host-nation law (GDPR, CSL).                        |

---

### 4. Principles

- **Need-to-Know / Least Privilege:** Access is granted only to the minimum information and resources necessary for assigned duties. [C-M(2002)49, AC/35-D/1015, ISO/IEC 27001:2022 cl. 5.10, NIST CSF PR.AC-6]
- **Role-Based Access Control (RBAC):** Access rights are based on formal roles, clearance, and mission requirements. [AC/322-D(2017)0009, NIST CSF PR.AC-4]
- **Separation of Duties:** No single individual may perform critical functions unilaterally where dual-key or two-person integrity is mandated (e.g., high-grade COMSEC, operational orders). [NIST CSF PR.AC-5, ISO/IEC 27001:2022 cl. 5.13]
- **Default Deny:** Access is denied by default; explicit authorisation is required. [AC/322-D(2017)0009, NIST CSF PR.AC-1]
- **Originator Control (ORCON):** Originators retain control over dissemination of classified products. [NATO policy, cited in AJP-3.20]
- **Auditability:** All access must be logged and subject to regular review and audit. [ISO/IEC 27001:2022 cl. 8.15, NIST CSF DE.CM-7]
- **Compliance:** Controls must comply with NATO, host-nation, coalition, and EU law, including GDPR for personal data. [GDPR Art. 32, Law 58/2019, C-M(2002)49]

---

### 5. Access Control Requirements

#### 5.1. User Identification and Authentication

- All access to information systems requires unique user identification (UID) and strong authentication.
- Smart-card (CAC-equivalent) PKI credentials are mandatory for all classified domains (NR, NS, MISSION SECRET). [AC/322-D(2017)0009, ISO/IEC 27001:2022 cl. 5.14, NIST CSF PR.AC-1, PR.AC-7]
- Passwords (where used) must comply with NATO and NIST SP 800-63B recommendations (minimum length, complexity, periodic change). [unsupported: NATO does not specify password complexity, but NIST and ISO/IEC 27001:2022 cl. 5.15 do]
- Multi-factor authentication (MFA) is required for remote and privileged access. [ISO/IEC 27001:2022 cl. 5.14, NIST CSF PR.AC-7]

#### 5.2. Access Provisioning and Deprovisioning

- Access is granted based on validated mission need, clearance level, and documented authorisation by line management. [AC/322-D(2017)0009, ISO/IEC 27001:2022 cl. 5.18, NIST CSF PR.AC-4]
- Access rights are reviewed quarterly and upon change of role, clearance, or employment status. [ISO/IEC 27001:2022 cl. 5.18, NIST CSF PR.AC-4]
- Access is immediately revoked upon termination, suspension, or change of duties incompatible with previous rights. [ISO/IEC 27001:2022 cl. 5.18, GDPR Art. 32]

#### 5.3. Segregation by Classification Domain

- Strict technical and procedural controls prevent unauthorised access or transfer of data between classification domains (NU, NR, NS, MISSION SECRET).
- Cross-domain transfers are only permitted via accredited NATO Cross-Domain Solutions (CDS) and are subject to formal release procedures and logs. [AC/322-D(2017)0009, NIST CSF PR.AC-5, ISO/IEC 27001:2022 cl. 5.13]
- Spillage incidents must be reported immediately and handled per the documented Incident Response Plan. [AC/322-D(2017)0009, NIST CSF RS.CO-2]

#### 5.4. Physical Access Controls

- Physical access to systems at NS and above is restricted to cleared personnel with need-to-know and is enforced via access control systems (badges, guards).
- TEMPEST-zoned areas (e.g., SCIFs) require additional access controls, physical logging, and two-person entry for certain operations. [ISO/IEC 27001:2022 cl. 7.2, NATO TEMPEST Policy]
- Visitors and contractors are escorted and access is logged. [ISO/IEC 27001:2022 cl. 7.2]

#### 5.5. Privileged Access

- Privileged accounts (administrators, SOC operators) are assigned only with senior management approval, based on operational necessity and clearance.
- Privileged access is logged, monitored, and subject to enhanced audit. [ISO/IEC 27001:2022 cl. 5.17, NIST CSF PR.AC-4]
- Privileged sessions on classified systems are monitored in real time where technically feasible. [ISO/IEC 27001:2022 cl. 8.15, NIST CSF DE.CM-7]

#### 5.6. COMSEC and Dual-Key Controls

- Access to COMSEC equipment and keying material is restricted to authorised, cleared personnel under two-person integrity where specified. [NATO COMSEC Policy, ISO/IEC 27001:2022 cl. 5.13]
- All COMSEC access and custodial actions are logged and auditable. [NATO COMSEC Policy]

#### 5.7. Supply Chain and Contractor Access

- Contractors and vendors must be security-screened per NATO and host-nation requirements before being granted access. [AC/35-D/1029, Law 58/2019]
- Contractor access is role- and time-limited, and subject to ongoing monitoring. [ISO/IEC 27001:2022 cl. 5.18]

#### 5.8. Personal Data and GDPR

- Access to personal data (civilian, contractor) is strictly limited to personnel with a legitimate role-based need. [GDPR Art. 32]
- Access logs for systems processing personal data are retained per GDPR and host-nation law. [GDPR Art. 5, Law 58/2019]

#### 5.9. Monitoring, Logging, and Review

- All access events (logical and physical) are logged in accordance with NATO technical directives and ISO/IEC 27001:2022 cl. 8.15.
- Logs are reviewed for anomalies by the Security Operations Centre (SOC) on a continual basis.
- Periodic audits are conducted (at least annually) to verify compliance. [ISO/IEC 27001:2022 cl. 8.16]

---

### 6. Exceptions

- Temporary exceptions to this policy may be granted only by the ISSM in writing, on the basis of documented operational necessity and risk assessment.
- All exceptions are time-bound, logged, and subject to review. [ISO/IEC 27001:2022 cl. 5.32]
- Permanent exceptions are not permitted without documented change approval through the Detachment’s Change Advisory Board and, where applicable, NATO or host-nation authority.

---

### 7. Monitoring and Review

- This policy and its implementation will be reviewed annually and following any significant changes in operational requirements, regulatory frameworks, or after major incidents.
- Compliance will be monitored via automated tools, regular audits, and red-team exercises.
- Policy effectiveness will be evaluated through incident statistics, audit findings, and feedback from operational units.

---

### 8. References

- NATO Information Security Policy (C-M(2002)49; as amended)
- AC/35-D/1015 (Security within NATO)
- AC/35-D/1029 (Personnel Security)
- AC/322-D(2017)0009 (NATO INFOSEC technical and implementation directive)
- NATO Cyber Defence Pledge 2016
- Allied Joint Doctrine for Cyberspace Operations (AJP-3.20)
- Romanian Cybersecurity Law (Law 58/2019)
- GDPR (Regulation EU 2016/679)
- NIST Cybersecurity Framework v2.0
- ISO/IEC 27001:2022, 27002:2022
- NATO TEMPEST Policy (current version)
- NATO COMSEC Policy (current version)

---

**Approved by:**  
[Name, Rank]  
Information Systems Security Manager (ISSM), J6  
Date: [YYYY-MM-DD]

---
