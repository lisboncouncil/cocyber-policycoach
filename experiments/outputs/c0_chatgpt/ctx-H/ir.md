---
config: C0
context_id: ctx-H
policy_id: P4
policy_name: Incident Response Policy
policy_short: ir
metadata:
  config: C0
  model: gpt-4.1-2025-04-14
  input_tokens: 1146
  output_tokens: 2147
  total_tokens: 3293
  latency_s: 19.604
  tool_calls: []
  raw_provider_id: chatcmpl-DcZaLlVBqiYfQFQ3fn3WW3GqZsJCS
sources_count: 0
sources: []
prompt_chars: 4675
answer_chars: 8608
generated_at_unix: 1778085644
---

---

**Incident Response Policy**

**Organisation:** [Small Provincial General Hospital, ASL, Italy]  
**Effective Date:** [DD/MM/YYYY]  
**Policy Owner:** IT/Information Security Officer (delegated to MSP, oversight by Hospital Director)  
**Review Cycle:** Annual (or upon major incident/regulatory update)  
**Working Language:** Italian (official translation to be issued; English version authoritative for audit purposes)

---

### 1. Purpose

This policy establishes the principles, responsibilities, and required controls for the detection, response, management, and reporting of cybersecurity incidents within the [Hospital Name], in compliance with applicable Italian, EU, and sectoral regulations (GDPR, D.Lgs. 196/2003 as amended, NIS2, AGID guidelines), and in alignment with international standards (NIST CSF 2.0, ISO/IEC 27001:2022). The intention is to safeguard patient safety, data confidentiality, integrity, and availability, while supporting continuous clinical operations.

---

### 2. Scope

This policy applies to:

- All hospital information systems (clinical, administrative, technical)
- All staff, including clinical, administrative, technical/facility personnel, and third parties (e.g., MSP, vendors) with access to hospital information assets
- All devices connected to the hospital network or handling patient/employee data (desktops, mobile devices, kiosks, servers)
- All data processed, including special categories (health data, minors’ data, employee data)

---

### 3. Roles and Responsibilities

| Role | Responsibilities |
|------|------------------|
| **Hospital Director** | Overall accountability for incident management; ensures resources and oversight |
| **IT/Information Security Officer** (delegated to MSP; internal oversight) | Coordinates incident response, ensures policy implementation, liaison with authorities |
| **MSP (Managed Services Provider)** | Primary incident detection, triage, technical response, escalation, and reporting per contract |
| **All Staff** | Prompt reporting of suspected incidents; participation in awareness training |
| **Data Protection Officer (DPO)** | Assesses data breach notification requirements (GDPR Art. 33-34), supports regulatory communications |
| **Clinical/Administrative Managers** | Ensures staff compliance, supports business continuity during incidents |
| **Regional/ASL Security Authority** | Notified of significant incidents as required by NIS2/regional regulations |

---

### 4. Principles

- **Patient Safety First:** Incident response actions must not impede emergency clinical workflows or jeopardize patient care. (AGID LG Sicurezza, NIS2 Art. 21(2))
- **Proportionality:** Response is commensurate to incident severity and business impact. (ISO/IEC 27001:2022, 6.1.2)
- **Timeliness:** Incidents are detected, reported, and managed promptly to minimize harm. (NIS2 Art. 23, NIST CSF DE.DP-4, RS.AN-1)
- **Compliance:** All actions must adhere to GDPR, Italian privacy law, NIS2, AGID guidance, and regional/FSE obligations.
- **Accountability and Traceability:** All incident actions are logged and attributable. (ISO/IEC 27001:2022, 8.1, 8.2)
- **Continuous Improvement:** Lessons learned feed into process and control enhancement. (NIST CSF RC.IM-1)

---

### 5. Incident Response Requirements & Controls

#### 5.1. Incident Definition and Classification

- **Definition:** An incident is any event that compromises, or threatens to compromise, the confidentiality, integrity, or availability of hospital information assets, or breaches legal/regulatory obligations. (ISO/IEC 27001:2022, 5.25; NIS2 Art. 3(12))
- **Classification:** Adopt a severity scale (Low, Medium, High, Critical) based on impact on clinical services, data confidentiality, and legal obligations. (NIST CSF RS.AN-1, ISO/IEC 27001:2022, A.5.25)

#### 5.2. Detection and Reporting

- **Detection:** MSP monitors security events (AV console, UTM logs); staff report suspected incidents to IT via established channels (telephone/email/portal). (NIST CSF DE.DP-4, ISO/IEC 27001:2022, A.5.28)
- **Awareness:** All staff must complete annual incident awareness training (2 hours/year; supported by external consulting for clinical staff). (Linee Guida AGID, NIST CSF PR.AT-1)
- **Reporting:** Suspected incidents must be reported immediately to IT; IT/MSP must triage within 2 working hours. Critical incidents (impacting EHR, ADT/PS, or large-scale data) require immediate escalation. (NIS2 Art. 23)

#### 5.3. Containment, Eradication, Recovery

- **Containment:** MSP, in consultation with IT, must act swiftly to contain active threats (e.g., isolate infected endpoints, disable compromised accounts), prioritizing critical systems (EHR, ADT, PACS). (NIST CSF RS.CO-2, ISO/IEC 27001:2022, A.5.26)
- **Eradication:** Remove root cause (malware, unauthorised access) upon containment. Legacy systems (e.g., clinical kiosks) must be prioritized if involved. (ISO/IEC 27001:2022, A.5.26)
- **Recovery:** Restore affected services from backups as per RTO targets (4h for EHR, 1h for ADT/PS). (NIST CSF RS.RP-1, ISO/IEC 27001:2022, A.5.29)
    - Backups: Ensure integrity before restore; verify backup health weekly. (AGID Misure Minime, NIST CSF PR.IP-9)

#### 5.4. Communication and Notification

- **Internal:** IT/Information Security Officer must inform Hospital Director, DPO, and relevant managers of significant incidents.
- **External:** 
    - Report notifiable incidents to ASL/regional Security Authority and Garante Privacy within legal deadlines (72h for GDPR, “immediately” for NIS2). (GDPR Art. 33/34; NIS2 Art. 23)
    - Communicate with patients or staff as required by data breach regulations (GDPR Art. 34).
    - Media/public statements only by Hospital Director or delegated spokesperson.

#### 5.5. Documentation and Evidence Preservation

- **Record Keeping:** All incident actions, decisions, and communications must be logged and preserved for at least 5 years or as required by law. (ISO/IEC 27001:2022, 7.5; GDPR Art. 5(2))
- **Forensics/Evidence:** Where possible, preserve forensic evidence (system logs, affected devices) in accordance with chain-of-custody principles, considering resource constraints. (NIST CSF RS.CO-3)

#### 5.6. Post-Incident Review and Continuous Improvement

- **Review:** For all High/Critical incidents, conduct a post-incident review (within 10 working days) to identify root causes, lessons learned, and required improvements. (NIST CSF RC.IM-1, ISO/IEC 27001:2022, A.10.1)
- **Update:** Policy, procedures, and technical controls must be updated as necessary following incidents. (ISO/IEC 27001:2022, 10.2)
- **Testing:** Disaster recovery tests must be performed at least annually; incident response process must be exercised at least once per year (tabletop or live test). (NIST CSF RS.IM-2, AGID Misure Minime)

#### 5.7. Supply Chain and Third-Party Incidents

- **MSP and Vendor Obligations:** All third parties (including MSP, medical device vendors) must promptly report incidents affecting hospital assets or data. (NIS2 Art. 21(2); ISO/IEC 27001:2022, A.5.19)
- **Escalation:** Any suspicion of supply chain compromise must be escalated to the Hospital Director and ASL Security Authority.

---

### 6. Exceptions

Any exceptions to this policy must be documented, justified, and formally approved by the Hospital Director and, where required, the DPO. Exceptions must be time-limited and periodically reviewed. (ISO/IEC 27001:2022, 5.1f)

---

### 7. Monitoring and Review

- **Monitoring:** Compliance with this policy is subject to periodic review by the Hospital Director, with support from IT and DPO, and may be audited by regional or national authorities.
- **Review:** The policy shall be reviewed annually or after any significant incident, regulatory change, or audit finding. (ISO/IEC 27001:2022, 10.1)

---

### 8. References

- [GDPR] Regulation (EU) 2016/679, esp. Articles 33, 34  
- [D.Lgs 196/2003] Codice in materia di protezione dei dati personali (as amended)  
- [NIS2] Directive (EU) 2022/2555, esp. Arts. 21, 23  
- [AGID] Linee Guida per la sicurezza informatica nella PA; Misure minime di sicurezza ICT per la PA  
- Provvedimenti Garante Privacy in sanità  
- Regional regulations on Fascicolo Sanitario Elettronico (FSE)  
- [NIST CSF 2.0] Identify, Detect, Respond, Recover functions; e.g., RS.AN-1, RS.CO-2, RS.RP-1, RC.IM-1  
- [ISO/IEC 27001:2022] esp. Clauses 5.25, 5.26, 7.5, 8.2, 10.1, 10.2  
- Hospital Information Security Policy (internal, future cross-reference)

---

**Approval:**  
[Name], Hospital Director  
[Date]

---
