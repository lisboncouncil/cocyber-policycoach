---
config: C0+web
context_id: ctx-H
policy_id: P2
policy_name: Incident Response Policy
policy_short: ir
metadata:
  config: C0+web
  model: gpt-4.1-2025-04-14
  input_tokens: 1186
  output_tokens: 1889
  total_tokens: 3075
  latency_s: 23.315
  tool_calls: []
  raw_provider_id: resp_053505772d89e2430069fb693a3238819791413a56ab894ff8
sources_count: 0
sources: []
prompt_chars: 4105
answer_chars: 8009
generated_at_unix: 1778084176
---

---

**Incident Response Policy**

**Organisation:** Ospedale Pubblico di [Regione], ASL [NN]  
**Effective Date:** [DD/MM/YYYY]  
**Policy Owner:** Responsabile IT / Direttore Sanitario  
**Review Cycle:** Annual (or upon relevant regulatory or operational change)

---

### 1. Purpose

This policy establishes the principles and requirements for detecting, reporting, responding to, and recovering from information security incidents affecting Ospedale Pubblico di [Regione], in compliance with the applicable regulatory and contractual obligations. The aim is to safeguard patient safety, ensure business continuity of clinical and administrative services, protect the confidentiality, integrity, and availability of health and personal data, and meet legal and sector-specific requirements.

---

### 2. Scope

This policy applies to all staff (clinical, administrative, technical), contractors, and third parties (including MSPs and vendors) who access or manage the hospital’s information systems, data, and devices. It covers all ICT assets within the hospital, including workstations, mobile devices, on-premises and federated systems, medical devices connected to the network, and cloud or managed services.

---

### 3. Roles and Responsibilities

| Role                             | Responsibilities                                                                                                                     |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| **Responsabile IT (IT Manager)**  | Overall policy owner; coordinates incident response; liaison with Direzione Sanitaria, MSP, and external authorities as required.    |
| **Direzione Sanitaria**           | Ensures clinical continuity and patient safety during incidents; participates in major incident assessment and communication.         |
| **Internal IT Staff**             | First-line technical response; initial triage, containment, and escalation to MSP as needed.                                         |
| **MSP (Managed Service Provider)**| Executes technical incident response under contract; supports investigation, containment, eradication, and recovery.                 |
| **All Staff**                     | Must report suspected or confirmed incidents immediately via defined channels.                                                       |
| **DPO (Data Protection Officer)** | Notified for incidents involving personal data; oversees GDPR compliance, reporting to Garante Privacy as required.                  |
| **Facility/Physical Security**    | Supports physical incident containment (e.g., theft of devices).                                                                    |

---

### 4. Principles

- **Patient Safety Priority:** Incident response must not compromise critical patient care or emergency clinical workflows. (AGID PA Guidelines, NIST CSF ID.BE-5)
- **Business Continuity:** Ensure restoration of essential clinical systems (EHR, ADT/PS) within RTO targets. (NIS2 Art. 21, ISO/IEC 27001:2022 A.5.30)
- **Regulatory Compliance:** Align with GDPR, D.Lgs. 196/2003, NIS2, AGID, and relevant regional/national health data provisions.
- **Confidentiality, Integrity, Availability:** Incidents must be managed with appropriate protection of sensitive health and personal data. (GDPR Art. 32, ISO/IEC 27001:2022 A.5.13)
- **Proportionality:** Controls and responses must be feasible within resource, staffing, and budget constraints.

---

### 5. Requirements / Controls

#### 5.1. Incident Identification and Reporting

a) **Definition of Incident:**  
An incident is any event that compromises, or threatens to compromise, the confidentiality, integrity, or availability of hospital information systems or data, including but not limited to: malware/ransomware, data breach, loss/theft of device, unauthorised access, supply-chain compromise.  
(Cited: NIS2 Art. 2, NIST CSF DE.DP-4, ISO/IEC 27001:2022 A.5.24)

b) **Obligation to Report:**  
All staff must immediately report suspected or confirmed incidents using the internal ticketing system or direct contact with IT.  
(Cited: Linee Guida AGID, NIST CSF DE.DP-5)

c) **Awareness:**  
Annual training (minimum 2h/year per staff) must include incident reporting procedures and examples.  
(Cited: Misure Minime AGID 14.2, NIST CSF PR.AT-1)

#### 5.2. Incident Triage and Initial Response

a) **Initial Assessment:**  
Internal IT staff perform rapid triage (within 30 minutes of report during business hours; as soon as feasible otherwise) to determine scope and severity.  
(Cited: ISO/IEC 27001:2022 A.5.24)

b) **Escalation:**  
Incidents beyond internal IT capacity or affecting critical systems are escalated to the MSP within 1h.  
(Cited: NIST CSF RS.CO-2, AGID PA Guidelines)

#### 5.3. Containment, Eradication, and Recovery

a) **Containment:**  
Actions are prioritised to limit impact (e.g., network isolation, account disablement), always considering patient safety and clinical continuity.  
(Cited: NIS2 Art. 21, NIST CSF RS.CO-3)

b) **Recovery:**  
Systems are restored based on clinical priority:  
- ADT/PS: RTO 1h  
- EHR/FSE, PACS/RIS: RTO 4h  
(Cited: NIS2 Art. 21, ISO/IEC 27001:2022 A.5.30)

c) **Use of Backups:**  
Recovery actions leverage available backups; backup integrity is regularly tested (at least quarterly).  
(Cited: Misure Minime AGID 9.1, ISO/IEC 27001:2022 A.8.13)

#### 5.4. Communication and Notification

a) **Internal Communication:**  
Relevant internal stakeholders (Direzione Sanitaria, DPO, relevant clinical leads) are notified as soon as a significant incident is confirmed.  
(Cited: NIST CSF RS.CO-2)

b) **External Notification:**  
If the incident involves personal data, the DPO assesses the need for notification to Garante Privacy within 72 hours per GDPR Art. 33.  
For incidents of significant impact, regional/national authorities are notified in line with NIS2 and AGID guidelines.  
(Cited: GDPR Art. 33–34, NIS2 Art. 23)

#### 5.5. Evidence Preservation

a) **Preservation Measures:**  
Where feasible, logs and relevant evidence are preserved for investigation, respecting privacy and clinical needs.  
(Cited: ISO/IEC 27001:2022 A.5.25, NIS2 Art. 28)

#### 5.6. Post-Incident Review and Improvement

a) **Lessons Learned:**  
A post-incident review is performed for all major incidents to identify root causes and improvement actions.  
(Cited: ISO/IEC 27001:2022 A.10.1, NIST CSF RS.IM-1)

b) **Update Procedures:**  
Incident response procedures are updated based on lessons learned and changes in threat landscape/regulation.  
(Cited: NIST CSF RS.IM-2)

---

### 6. Exceptions

Exceptions to this policy (e.g., where a control is not feasible due to patient safety or critical clinical need) must be approved by the IT Manager in consultation with Direzione Sanitaria. All exceptions are documented, justified, and reviewed annually.

---

### 7. Monitoring and Review

- Compliance with this policy is monitored by the IT Manager through periodic review of incident logs, MSP reports, and post-incident reviews.
- The policy is reviewed at least annually, or upon significant incident or regulatory change, involving the DPO and Direzione Sanitaria.
- Metrics for monitoring include incident response times, incident volumes/trends, and training completion rates.

---

### 8. References

- **GDPR (Regulation EU 2016/679), esp. Art. 32, 33, 34**
- **D.Lgs. 196/2003 as amended by D.Lgs. 101/2018**
- **NIS2 Directive (EU 2022/2555), esp. Arts. 2, 21, 23, 28**
- **Provvedimenti Garante Privacy in sanità**
- **Linee Guida AGID per la sicurezza informatica nella PA**
- **Misure minime AGID per la PA, esp. 9.1, 14.2**
- **ISO/IEC 27001:2022, esp. A.5.13, A.5.24, A.5.25, A.5.30, A.8.13, A.10.1**
- **NIST Cybersecurity Framework 2.0, esp. DE.DP-4, DE.DP-5, PR.AT-1, ID.BE-5, RS.CO-2, RS.CO-3, RS.IM-1, RS.IM-2**

---

**End of Policy**
