---
config: C0+web
context_id: ctx-H
policy_id: P3
policy_name: Data Protection Policy
policy_short: dataprot
metadata:
  config: C0+web
  model: gpt-4.1-2025-04-14
  input_tokens: 1186
  output_tokens: 2082
  total_tokens: 3268
  latency_s: 22.906
  tool_calls: []
  raw_provider_id: resp_0f88eb6cf48c8a3c0069fb6950b11081a2ba8c351baadfd6e0
sources_count: 0
sources: []
prompt_chars: 4103
answer_chars: 7420
generated_at_unix: 1778084199
---

---

**Data Protection Policy**

**Organisation:** [Redacted] Public Hospital (ASL, Servizio Sanitario Nazionale)  
**Effective Date:** [Insert Date]  
**Policy Owner:** IT Manager / DPO (Data Protection Officer)  
**Review Cycle:** Annual (or following significant organisational or regulatory change)  

---

### 1. Purpose

This policy establishes principles and mandatory controls for the protection of personal and special category data processed by [Redacted] Public Hospital. It ensures compliance with EU and Italian data protection regulations, supports continuity of clinical services, and mitigates cybersecurity risks aligned to the hospital’s profile, capacity, and sectoral threats.

---

### 2. Scope

This policy applies to all staff (clinical, administrative, technical), contractors, and third parties (including the MSP) who access or process personal data on behalf of the Hospital, across all information systems, devices, and physical or digital records, including the regional FSE, PACS/RIS, LIS, ADT, and Pharmacy systems.

---

### 3. Roles and Responsibilities

| Role | Responsibility |
|------|---------------|
| **Data Controller** (Hospital Director) | Ultimate responsibility for data protection (GDPR Art. 4(7)). |
| **DPO** | Advise on compliance, monitor adherence, liaise with Garante Privacy (GDPR Arts. 37–39). |
| **IT Manager** | Implement security measures, manage incidents, maintain records (AGID, NIS2). |
| **MSP** | Operate ICT per contract, report incidents, apply controls (GDPR Art. 28, NIS2 Art. 21). |
| **Staff** | Process data lawfully, follow procedures, report incidents (GDPR Art. 29, ISO 27001:2022 5.3). |

---

### 4. Principles

- **Lawfulness, Fairness, Transparency** (GDPR Art. 5(1)(a))
- **Purpose Limitation** (GDPR Art. 5(1)(b))
- **Data Minimisation** (GDPR Art. 5(1)(c))
- **Accuracy** (GDPR Art. 5(1)(d))
- **Storage Limitation** (GDPR Art. 5(1)(e))
- **Integrity and Confidentiality** (GDPR Art. 5(1)(f); NIS2 Art. 21; ISO 27001:2022 6.1.3)
- **Accountability** (GDPR Art. 5(2))

---

### 5. Policy Requirements and Controls

#### 5.1. Data Inventory and Classification

- Maintain a record of processing activities (ROPA) per GDPR Art. 30.
- Classify data by sensitivity: special category (health), minors’ data, employee data (ISO 27001:2022 5.12, AGID Linee Guida).
- Review and update inventory annually or upon significant change.

**Reference:** GDPR Art. 30, ISO 27001:2022 5.12

---

#### 5.2. Lawful Processing and Data Subject Rights

- Process data only for defined, legitimate purposes (GDPR Art. 6, 9).
- Ensure mechanisms to support data subject rights: access, rectification, erasure, restriction, portability, objection (GDPR Arts. 12–23).
- Communicate privacy information in clear Italian (GDPR Art. 12).

**Reference:** GDPR Arts. 6, 9, 12–23

---

#### 5.3. Access Control and Identity Management

- Enforce least privilege and role-based access for all systems (ISO 27001:2022 A.9.1.2, AGID Misure minime 1.1.1).
- Use on-prem AD and regional SPID/CIE federation for authentication (AGID Linee Guida).
- Review user rights quarterly, with immediate revocation upon contract end or role change (GDPR Art. 32(4), NIST CSF PR.AC-1).

**Reference:** ISO 27001:2022 A.9, AGID Misure minime, GDPR Art. 32

---

#### 5.4. Endpoint and Mobile Device Security

- Maintain antivirus/endpoint protection on all workstations (AGID Misure minime 1.2.2).
- Apply security updates monthly, except for legacy clinical kiosks where vendor support is not possible (document exceptions).
- Encrypt mobile devices and enable remote wipe (AGID Misure minime 1.3.1; unsupported for legacy clinical kiosks, document risk).

**Reference:** AGID Misure minime 1.2.2, 1.3.1; ISO 27001:2022 A.10.1

---

#### 5.5. Data Handling and Storage

- Store special category data only on approved systems (regional FSE, PACS/RIS, LIS, ADT, Pharmacy) (GDPR Art. 5(1)(f)).
- Prohibit use of personal cloud/USB for health data (AGID Linee Guida, ISO 27001 A.8.3).
- Apply data retention schedules per legal and regional requirements; securely delete when no longer needed (GDPR Art. 5(1)(e), AGID Linee Guida).

**Reference:** GDPR Art. 5(1)(e)-(f), AGID Linee Guida

---

#### 5.6. Third Party and Supply Chain Management

- Ensure MSP, vendors, and contractors sign data processing agreements (GDPR Art. 28).
- Require MSP to notify data breaches/incidents within 4 hours of detection (NIS2 Art. 23; SLA).
- Assess suppliers for security posture at onboarding and contract renewal (NIS2 Art. 21(2)(d), ISO 27001:2022 A.15).

**Reference:** GDPR Art. 28, NIS2 Art. 21–23, ISO 27001:2022 A.15

---

#### 5.7. Training and Awareness

- Deliver at least 2 hours of data protection/cybersecurity training to all staff per year, with special focus on phishing and data handling (AGID Linee Guida, NIS2 Art. 20(2)).
- Document attendance and completion.

**Reference:** AGID Linee Guida, NIS2 Art. 20(2)

---

#### 5.8. Incident and Breach Management

- Escalate all suspected data breaches to DPO and MSP immediately (GDPR Art. 33; NIS2 Art. 23).
- Document and manage incidents per ad-hoc procedure, with reporting to Garante Privacy within 72 hours where required (GDPR Art. 33).
- Conduct post-incident review for lessons learned and improvement (ISO 27001:2022 A.16.1.6).

**Reference:** GDPR Art. 33, NIS2 Art. 23, ISO 27001:2022 A.16

---

#### 5.9. Physical Security

- Restrict access to IT rooms and data storage areas to authorised staff (AGID Misure minime 1.5.1).
- Encourage prompt reporting of lost/stolen devices; enable device tracking where feasible (AGID Misure minime 1.3.2).

**Reference:** AGID Misure minime 1.5.1, 1.3.2

---

#### 5.10. Business Continuity and Data Availability

- Ensure daily backup of critical clinical systems (EHR, ADT, PACS/RIS, LIS) with offsite/segregated storage (ISO 27001:2022 A.17.1.3).
- Test backups at least quarterly.
- Document RTO (EHR: 4h, ADT/PS: 1h) and prioritise recovery accordingly (ISO 27001:2022 A.17, AGID Linee Guida).

**Reference:** ISO 27001:2022 A.17, AGID Linee Guida, NIS2 Art. 21

---

### 6. Exceptions

Any exception to this policy (e.g., use of legacy clinical kiosks without full support for encryption or updates) must be documented, risk-assessed, and approved by the IT Manager and DPO. Compensating controls and mitigation measures must be implemented where feasible.

**Reference:** ISO 27001:2022 6.1.3, AGID Linee Guida

---

### 7. Monitoring and Review

- The IT Manager, under DPO oversight, will review policy implementation annually or upon major incident/regulatory change.
- Compliance checks will be performed at least annually (AGID Linee Guida).
- Breaches of this policy may result in disciplinary action and must be reported to the DPO.

**Reference:** ISO 27001:2022 9.2, AGID Linee Guida

---

### 8. References

- **GDPR** (Reg. EU 2016/679)  
- **Codice Privacy** (D.Lgs. 196/2003 as amended by D.Lgs. 101/2018)
- **NIS2 Directive** (EU 2022/2555)
- **AGID Linee Guida per la sicurezza informatica nella PA**  
- **AGID Misure minime per la sicurezza ICT nella PA**  
- **Provvedimenti Garante Privacy in sanità**
- **Regional regulations on FSE**
- **ISO/IEC 27001:2022**
- **NIST Cybersecurity Framework 2.0**

---

**Document History:**  
- Drafted: [Insert Date]  
- Approved: [Insert Date, by IT Manager/DPO]  
- Next Review: [Insert Date]

---

**End of Document**
