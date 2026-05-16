---
config: C0
context_id: ctx-H
policy_id: P2
policy_name: Incident Response Policy
policy_short: ir
metadata:
  config: C0
  model: gpt-4.1-2025-04-14
  input_tokens: 892
  output_tokens: 2421
  total_tokens: 3313
  latency_s: 47.794
  tool_calls: []
  raw_provider_id: chatcmpl-DcZ7crg3RCC8ioGre94vBCB0i6YyR
sources_count: 0
sources: []
prompt_chars: 4105
answer_chars: 9709
generated_at_unix: 1778083891
---

---

**Incident Response Policy**  
**Organisation:** [Hospital Name], Public Hospital — [Region], Servizio Sanitario Nazionale  
**Effective Date:** [DD/MM/YYYY]  
**Policy Owner:** Responsabile della Protezione dei Dati (DPO) & IT Manager  
**Review Cycle:** Annual (or after major incident/regulatory change)  
**Approved By:** Hospital Director  
**Version:** 1.0

---

### 1. Purpose

This Incident Response Policy defines the principles, roles, responsibilities, and controls for detecting, reporting, managing, and learning from cybersecurity incidents affecting [Hospital Name]. The policy ensures alignment with applicable legal and regulatory requirements, supports the continuity and safety of clinical care, and protects the confidentiality, integrity, and availability of personal and health data processed by the hospital.  
**References:**  
- GDPR Art. 32–34  
- D.Lgs. 196/2003 (as amended by D.Lgs. 101/2018)  
- NIS2 Directive (EU 2022/2555), Art. 21, 23  
- AGID “Linee Guida per la sicurezza informatica nella PA”  
- ISO/IEC 27001:2022 A.5.24, A.5.25  
- NIST CSF 2.0 (RS — Respond, RC — Recover)

---

### 2. Scope

This policy applies to:  
- All employees, consultants, contractors, and third parties with access to the hospital’s information systems, networks, and data.  
- All information systems and data assets managed by the hospital, including on-premises infrastructure, cloud services, and systems managed by third parties (e.g., MSP, clinical system vendors).  
- All data categories, with special focus on health data, minors’ data, and employee personal data.

---

### 3. Roles and Responsibilities

| Role                          | Responsibility                                                                                  |
|-------------------------------|-----------------------------------------------------------------------------------------------|
| **Hospital Director**         | Approves policy; ensures resources for implementation.                                         |
| **IT Manager (Internal)**     | Coordinates incident response; primary contact for internal/external escalation.               |
| **DPO**                       | Involved in all incidents involving personal data; leads regulatory notifications.             |
| **MSP (Managed Service Provider)** | Provides technical support; assists in detection, containment, eradication, and recovery.       |
| **Clinical/Administrative Staff** | Promptly report suspected incidents as per reporting procedure.                                 |
| **Medical Device Vendors**    | Cooperate in incident management if their systems/devices are affected.                        |
| **Regional/Federated Identity Provider** | Notify of credential compromise incidents as per federation agreements.                        |

**References:**  
- ISO/IEC 27001:2022 A.5.24, A.5.25  
- NIS2 Art. 23  
- AGID “Misure minime di sicurezza ICT per la PA” §5.2.2  
- GDPR Art. 33, 34

---

### 4. Principles

1. **Patient Safety First:** Incident response must prioritise uninterrupted delivery of critical clinical services and patient safety at all times.  
   _Reference: NIS2 Recital 18; AGID Linee Guida §4.2_
2. **Regulatory Compliance:** All actions must comply with GDPR, Italian privacy law, NIS2, and AGID guidance.  
3. **Timely Detection and Escalation:** Rapid identification and escalation of incidents is essential to minimise impact.  
   _Reference: NIST CSF 2.0 RS.ID, RS.AN, RS.CO_
4. **Minimum Service Disruption:** Response actions should minimise disruption to clinical and administrative workflows.  
   _Reference: ISO/IEC 27001:2022 A.5.25_
5. **Documentation and Learning:** All incidents are logged, reviewed, and lessons learned are integrated into procedures.  
   _Reference: NIST CSF 2.0 RC.IM; ISO/IEC 27001:2022 A.5.25.8_
6. **Third-Party Coordination:** Incidents involving MSPs or vendors are managed collaboratively, per contractual terms.  
   _Reference: NIS2 Art. 21(2)(c); AGID §5.3.4_

---

### 5. Requirements and Controls

#### 5.1. Incident Definition and Classification

- **Control:** All events that compromise, or could compromise, the confidentiality, integrity, or availability of information systems, data, or services, are considered security incidents.
    - _Reference: ISO/IEC 27001:2022 A.5.24.1; NIST CSF RS.ID_

- **Control:** Incidents must be classified by severity (Critical, High, Medium, Low) based on impact on patient safety, service continuity, and legal/regulatory exposure.
    - _Reference: AGID Linee Guida §5.2.2; NIS2 Art. 23(1)_

#### 5.2. Detection and Reporting

- **Control:** All staff must promptly report suspected or actual security incidents to the IT helpdesk (via internal ticket, phone, or designated email). “Incident reporting” is included in annual staff cyber awareness training.
    - _Reference: ISO/IEC 27001:2022 A.6.2.2; AGID Misure minime §10.5_

- **Control:** The IT Manager and/or MSP will monitor available detection tools (AV console, system logs, MSP alerts) for signs of security incidents. Automated detection is limited to existing tools.
    - _Reference: NIST CSF 2.0 DE.DP, DE.CM; AGID Misure minime §10.5_

#### 5.3. Initial Assessment and Containment

- **Control:** Upon report, the IT Manager (with MSP) will assess the incident within 2 hours (during business hours) or ASAP after hours.
    - _Reference: NIS2 Art. 23(2); AGID Linee Guida §5.2.2_

- **Control:** For incidents affecting clinical services (e.g., EHR, ADT), containment actions (e.g., network segmentation, account disablement, endpoint isolation) must be balanced against patient safety and business continuity (RTO: 1h for ADT/PS, 4h for EHR).
    - _Reference: NIS2 Art. 21; Hospital BC Plan_

- **Control:** When containment may disrupt critical care, the IT Manager must consult the relevant clinical lead before action.
    - _Unsupported (best practice for safety-critical healthcare)_

#### 5.4. Notification and Escalation

- **Control:** The DPO must be informed of all incidents involving personal data, in order to assess notification obligations to the Garante Privacy and data subjects (GDPR Art. 33–34).
    - _Reference: GDPR Art. 33, 34; D.Lgs. 196/2003 Art. 2-septies_

- **Control:** For “significant” incidents as defined by NIS2 and regional regulation (e.g., major service outage, significant data breach), the hospital will notify the CSIRT or regional authority within 24 hours.
    - _Reference: NIS2 Art. 23(2)_

- **Control:** Incidents impacting third-party services (e.g., MSP, medical device vendor) must be escalated to the relevant provider immediately per contractual SLAs.
    - _Reference: NIS2 Art. 21(2)(c); AGID §5.3.4_

#### 5.5. Eradication and Recovery

- **Control:** The IT Manager and MSP will coordinate eradication of threats (e.g., malware removal, credential reset) and restore systems from backups as soon as safely possible, prioritising ADT and EHR systems in line with RTOs.
    - _Reference: ISO/IEC 27001:2022 A.5.25.5, A.5.25.7_

- **Control:** Where possible, incident recovery must preserve evidence (e.g., logs, disk images) for root cause analysis and potential legal proceedings.
    - _Reference: NIST CSF 2.0 RS.IM; ISO/IEC 27001:2022 A.5.25.6_

#### 5.6. Post-Incident Review and Lessons Learned

- **Control:** For all “High” and “Critical” incidents, a formal post-incident review will be held within 10 working days, involving IT, DPO, MSP, and clinical/administrative leads as appropriate.
    - _Reference: ISO/IEC 27001:2022 A.5.25.8; NIST CSF RC.IM_

- **Control:** The review must document cause, response actions, impact, and recommendations, and feed into updates to procedures and training.
    - _Reference: ISO/IEC 27001:2022 A.5.25.8_

#### 5.7. Documentation

- **Control:** All incidents are recorded in the hospital’s Incident Register, including time, nature, actions taken, and resolution.
    - _Reference: ISO/IEC 27001:2022 A.5.25.8_

#### 5.8. Awareness and Training

- **Control:** Incident response awareness (how to recognise and report incidents) is included in the mandatory annual 2-hour cybersecurity training for all staff.
    - _Reference: AGID Misure minime §10.5; ISO/IEC 27001:2022 A.6.2.2_

---

### 6. Exceptions

- Any deviation from this policy must be approved by the Hospital Director and DPO, documented, and justified (e.g., urgent need to preserve patient safety).
- Where resource or technical constraints prevent full implementation, a risk assessment must be performed and compensating measures identified.
    - _Reference: ISO/IEC 27001:2022 A.5.31_

---

### 7. Monitoring and Review

- The IT Manager and DPO will jointly review incident trends, root causes, and the effectiveness of this policy at least annually, or after any “Critical” incident or regulatory update.
    - _Reference: ISO/IEC 27001:2022 A.10.1_

- The policy will be updated to reflect lessons learned, changes in threat landscape, or regulatory changes.

---

### 8. References

- **GDPR (Regulation EU 2016/679), Art. 32–34**
- **D.Lgs. 196/2003 as amended (Codice Privacy)**
- **NIS2 Directive (EU 2022/2555), Art. 21, 23**
- **AGID Linee Guida per la sicurezza informatica nella PA, Misure minime di sicurezza ICT**
- **Provvedimenti Garante Privacy in sanità**
- **ISO/IEC 27001:2022, especially A.5.24, A.5.25, A.6.2.2, A.5.31, A.10.1**
- **NIST Cybersecurity Framework 2.0 (Identify, Protect, Detect, Respond, Recover)**
- **Regional regulations on FSE (Fascicolo Sanitario Elettronico)**
- **[Hospital Name] Business Continuity Plan**

---

**Document History:**  
Version 1.0 — [DD/MM/YYYY]: Initial release

---

**End of Policy**
