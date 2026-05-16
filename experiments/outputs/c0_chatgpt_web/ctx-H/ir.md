---
config: C0+web
context_id: ctx-H
policy_id: P4
policy_name: Incident Response Policy
policy_short: ir
metadata:
  config: C0+web
  model: gpt-4.1-2025-04-14
  input_tokens: 1440
  output_tokens: 2189
  total_tokens: 3629
  latency_s: 34.146
  tool_calls: []
  raw_provider_id: resp_044c6c05cbeb5a900069fb7068ad18819586d4cb9dc10fa6e1
sources_count: 0
sources: []
prompt_chars: 4675
answer_chars: 8835
generated_at_unix: 1778086026
---

---

**INCIDENT RESPONSE POLICY**

**Organisation:** Ospedale Provinciale Generale, ASL [REDACTED], Italy  
**Effective Date:** [Insert Date: YYYY-MM-DD]  
**Policy Owner:** IT Manager (on behalf of Direzione Sanitaria e Amministrativa)  
**Review Cycle:** Annual, or following any material incident or regulatory change  
**Working Language:** Italian (policy text in English for auditability)  
**Version:** 1.0

---

## 1. Purpose

This policy establishes the requirements and procedures for responding to information security incidents within Ospedale Provinciale Generale, in alignment with applicable Italian and EU legal frameworks, sectoral regulations, and international best practices (NIS2, GDPR, AGID, NIST CSF 2.0, ISO/IEC 27001:2022). The aim is to ensure rapid, effective, and coordinated response to incidents that may affect patient care, confidentiality, integrity, or availability of personal and health data, or disrupt hospital operations.

---

## 2. Scope

This policy applies to all staff (clinical, administrative, technical), contractors, and external service providers (including the Managed Service Provider, MSP) who access, manage, or support the hospital’s information systems, medical devices, data, and networks. It covers all information assets, including on-premise and mobile devices, and all data categories processed by the hospital (special category health data, minors’ data, employee data).

---

## 3. Roles and Responsibilities

| Role                       | Responsibilities                                                                                                       |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------|
| IT Manager (Policy Owner)  | Oversees incident response process, ensures policy implementation, primary point of contact for escalation.            |
| Internal IT Staff          | First-line detection and response, initial triage, communication with MSP, documentation of incidents.                 |
| MSP (Managed Service Provider) | Supports incident containment, eradication, and recovery under contract and SLA. Provides escalation to specialist resources as needed. |
| Direzione Sanitaria/Amministrativa | Ensures patient safety and operational continuity decisions; authorises major escalations and communications (e.g., to Garante Privacy, regional ASL).|
| DPO (Data Protection Officer, regional) | Advises on GDPR/data breach notification, liaises with Garante Privacy, oversees personal data-related incidents. |
| All Staff                  | Promptly report suspected or actual security incidents; comply with response instructions.                            |

---

## 4. Principles

- **Patient Safety First:** Incident response actions must not compromise urgent/emergency clinical care (NIS2 Art. 21, ISO/IEC 27001:2022 A.5.7).
- **Legal and Regulatory Compliance:** All actions must comply with GDPR, NIS2, D.Lgs. 196/2003, AGID guidelines, and regional regulations (GDPR Art. 33-34; NIS2 Art. 23; AGID "Misure minime" 5.8).
- **Timely Response:** Incidents affecting EHR/ADT must be responded to immediately; RTOs apply as specified in the business continuity plan (NIS2 Art. 21.2, ISO/IEC 27001:2022 A.5.30).
- **Proportionality:** Responses should be proportionate to the risk, scale, and impact of the incident (ISO/IEC 27001:2022 A.5.30, NIST CSF RS).
- **Continuous Improvement:** Lessons learned from incidents must inform policy, training, and controls (ISO/IEC 27001:2022 A.10.1).

---

## 5. Requirements and Controls

### 5.1. Incident Definition and Classification

- **Definition:** An information security incident is any event that has compromised or may compromise the confidentiality, integrity, or availability of hospital information systems, data, or services (ISO/IEC 27001:2022 A.5.30; NIS2 Art. 3.7).
- **Classification:** Incidents must be classified by impact (High/Medium/Low), based on patient safety, data confidentiality, and operational continuity (NIST CSF RS.AN-1, ISO/IEC 27001:2022 A.5.30).

### 5.2. Reporting

- **Mandatory Reporting:** All staff and contractors must immediately report suspected or actual information security incidents via designated channels (telephone, email to IT, or incident form) (ISO/IEC 27001:2022 A.5.30; AGID Misure Minime 5.8).
- **External Notification:** Where required, the hospital must notify the regional ASL, Garante Privacy, and/or CERT-PA of notifiable incidents within statutory timeframes (GDPR Art. 33: 72h; NIS2 Art. 23: "without undue delay").

### 5.3. Initial Response and Triage

- **First Response:** Internal IT staff perform initial assessment and containment, with support from MSP as per contract (ISO/IEC 27001:2022 A.5.30; NIST CSF RS.CO-1).
- **Escalation:** High-impact incidents (e.g., ransomware, major data breach) must be escalated immediately to the IT Manager, Direzione Sanitaria, and MSP (NIST CSF RS.CO-2; ISO/IEC 27001:2022 A.5.30).
- **Documentation:** All incidents must be logged using the incident register, including date/time, reporter, description, actions taken, and outcome (ISO/IEC 27001:2022 A.5.30).

### 5.4. Containment, Eradication, and Recovery

- **Containment:** Priority is to isolate affected systems (e.g., disconnect from network, lock user accounts) while minimising clinical disruption (NIST CSF RS.CO-3; ISO/IEC 27001:2022 A.5.30).
- **Eradication:** MSP/in-house IT removes malicious artefacts, restores from backups as applicable (ISO/IEC 27001:2022 A.5.30).
- **Recovery:** Restore affected services and data in line with documented RTOs (EHR: 4h; ADT/PS: 1h) (ISO/IEC 27001:2022 A.17.1; NIST CSF RC.RP-1).
- **Forensic Preservation:** In case of major incidents (e.g., criminal activity), evidence must be preserved for investigation, coordinated with law enforcement as necessary (GDPR Art. 33-34; NIS2 Art. 23).

### 5.5. Communication and Notification

- **Internal Communication:** The IT Manager ensures timely updates to relevant internal stakeholders (clinical leads, administration, regional ASL) (NIST CSF RS.CO-2).
- **External Communication:** The DPO manages regulatory notifications (Garante Privacy, regional ASL, CERT-PA) (GDPR Art. 33-34; NIS2 Art. 23).
- **Patient/Third-Party Notification:** Required if data breach poses high risk to rights/freedoms of individuals (GDPR Art. 34).

### 5.6. Post-Incident Review and Lessons Learned

- **Debrief:** For all high/medium impact incidents, a debrief must be held within 10 working days, involving IT, MSP, DPO, and clinical/administrative leads as appropriate (ISO/IEC 27001:2022 A.10.1).
- **Reporting:** A summary of the incident and lessons learned must be shared with hospital management and used to update training, procedures, and controls (ISO/IEC 27001:2022 A.10.1).

### 5.7. Training and Awareness

- **Annual Training:** All staff must complete at least 2 hours/year of security awareness training, including incident recognition and reporting (AGID Misure Minime 5.6; NIST CSF PR.AT-1).
- **Induction:** New staff must receive incident response training as part of onboarding (ISO/IEC 27001:2022 A.6.3).

### 5.8. Testing and Continuous Improvement

- **Tabletop Exercise:** At least annually, conduct a tabletop incident response exercise involving IT, MSP, DPO, and selected clinical/administrative staff (ISO/IEC 27001:2022 A.5.30; NIST CSF RS.IM-1).
- **Disaster Recovery Test:** Disaster recovery plan must be tested at least every 18 months (ISO/IEC 27001:2022 A.17.1).

---

## 6. Exceptions

Any exceptions to this policy must be documented and approved by the Direzione Sanitaria/Amministrativa and IT Manager, with risk accepted and reviewed at least annually. Exceptions must not violate legal or regulatory obligations.

---

## 7. Monitoring and Review

- **Monitoring:** Incident logs, response times, and post-incident reviews will be regularly monitored by the IT Manager and reported to hospital management.
- **Review:** This policy will be reviewed annually, or following a significant incident or regulatory update, to ensure ongoing compliance and effectiveness (ISO/IEC 27001:2022 A.5.9).

---

## 8. References

- Regulation (EU) 2016/679 (GDPR), esp. Art. 33-34
- D.Lgs. 196/2003 as amended by D.Lgs. 101/2018
- Directive (EU) 2022/2555 (NIS2), esp. Art. 21, 23
- AGID "Misure minime di sicurezza ICT per le PA", 2017, Sections 5.6, 5.8
- Linee Guida AGID per la sicurezza informatica nella PA
- Provvedimenti Garante Privacy in sanità
- ISO/IEC 27001:2022, esp. A.5.7, A.5.9, A.5.30, A.6.3, A.10.1, A.17.1
- NIST Cybersecurity Framework (CSF) 2.0, esp. Identify (ID.RA), Protect (PR.AT), Respond (RS), Recover (RC)
- Regional regulations on FSE (Fascicolo Sanitario Elettronico)

---

**End of Document**
