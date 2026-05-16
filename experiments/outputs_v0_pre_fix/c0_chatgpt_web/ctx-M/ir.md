---
config: C0+web
context_id: ctx-M
policy_id: P2
policy_name: Incident Response Policy
policy_short: ir
metadata:
  config: C0+web
  model: gpt-4.1-2025-04-14
  input_tokens: 1309
  output_tokens: 2259
  total_tokens: 3568
  latency_s: 25.439
  tool_calls: []
  raw_provider_id: resp_0ee958141945ce430069fb69a07c8481a192027e4989b79b73
sources_count: 0
sources: []
prompt_chars: 4953
answer_chars: 8695
generated_at_unix: 1778084281
---

---

**[NATO Allied Command Operations – Multinational Military Detachment, Romania]**  
**Incident Response Policy**

**Effective Date:** 2024-07-01  
**Policy Owner:** Information Systems Security Manager (ISSM), J6  
**Review Cycle:** Annual, or upon change of mission set/regulatory regime  
**Classification:** NATO UNCLASSIFIED (when detached from annexes/attachments)

---

### 1. Purpose

This Incident Response Policy establishes the framework, principles, and requirements for timely, coordinated, and effective response to cybersecurity incidents affecting NATO, national, and mission networks, information, or systems within the Multinational Military Detachment, Romania, under NATO Allied Command Operations (SHAPE). The policy supports compliance with NATO and host-nation cyber regulations, ensures mission continuity, and protects classified and sensitive information.

---

### 2. Scope

This policy applies to all personnel (military, NATO civilians, and cleared contractors), systems, and network domains (NU, NR, NS, MISSION SECRET) operated or managed by the detachment. It covers detection, analysis, response, and reporting of incidents affecting CIS, COMSEC, and related information assets. This policy is binding on all detachment elements and personnel, irrespective of nationality or duty status.

---

### 3. Roles and Responsibilities

- **ISSM (J6):**  
  - Policy owner; ensures policy alignment with NATO, host-nation, and contributing nation requirements.  
  - Approves incident response plans and ensures resource allocation.  
  - Liaises with NCIRC, NCSC, host-nation CERT, and SHAPE as needed.  
  - [Ref: C-M(2002)49, AC/322-D(2017)0009, ISO/IEC 27001:2022 A.5.3]

- **Cyber Operations Team (incl. ISSO/ISSM support, 24/7 SOC):**  
  - Monitors, detects, triages, and investigates security incidents.  
  - Maintains incident records and escalates per documented procedures.  
  - [Ref: NIST CSF 2.0 ID.RA, DE.DP, RS.AN; AC/322-D(2017)0009]

- **COMSEC Custodians:**  
  - Respond to incidents affecting COMSEC material; ensure two-person integrity and chain of custody.  
  - Notify national COMSEC authority per national and NATO protocols.  
  - [Ref: AC/322-D(2017)0009, COMSEC policy, AC/35-D/1015]

- **All Users (Military, Civilians, Contractors):**  
  - Promptly report suspected or confirmed incidents via chain of command or direct to SOC.  
  - Cooperate with investigations; preserve evidence where instructed.  
  - [Ref: C-M(2002)49, AC/35-D/1015, ISO/IEC 27001:2022 A.6.1.2]

---

### 4. Principles

- **Mission Continuity:** Incident response must prioritise operational effectiveness and continuity of NATO missions.  
  - [Ref: Allied Joint Doctrine for Cyberspace Operations (AJP-3.20) 1.6, ISO/IEC 27001:2022 6.1.3]

- **Confidentiality and Integrity:** All incident response activities must enforce NATO classification, need-to-know, and originator control (ORCON) requirements.  
  - [Ref: C-M(2002)49, AC/35-D/1015, ISO/IEC 27001:2022 A.5.13]

- **Timely Detection and Escalation:** Incidents must be detected and escalated without undue delay, with 24/7 monitoring and clear escalation thresholds.  
  - [Ref: NIST CSF 2.0 DE.DP, RS.CO; AC/322-D(2017)0009]

- **Legal and Regulatory Compliance:** All incident handling must comply with NATO, host-nation, and applicable EU law (NIS2, GDPR within SOFA limits).  
  - [Ref: Romanian Cybersecurity Law 58/2019, NIS/NIS2, GDPR, NATO SOFA]

- **Non-Repudiation and Auditability:** All incident response actions must be logged and be auditable; chain of custody is mandatory for classified and COMSEC incidents.  
  - [Ref: ISO/IEC 27001:2022 A.8.12, AC/322-D(2017)0009]

---

### 5. Requirements / Controls

#### 5.1 Incident Detection and Reporting

- **Continuous Monitoring:** All network domains must be monitored 24/7 by the theatre-level SOC for indicators of compromise, per NATO technical directives.  
  - [Ref: AC/322-D(2017)0009, NIST CSF 2.0 DE.CM]

- **Mandatory Reporting:** All personnel must report suspected or actual security incidents immediately via the established reporting channels.  
  - [Ref: ISO/IEC 27001:2022 A.6.1.2, AC/35-D/1015]

- **Initial Triage:** The SOC must triage and categorise incidents within 30 minutes of detection, using NATO incident taxonomy.  
  - [Ref: AC/322-D(2017)0009, NIST CSF 2.0 DE.DP]

#### 5.2 Incident Analysis and Containment

- **Classification-Respecting Response:** Incident response must not compromise separation of classification domains or need-to-know. No cross-domain artefacts or logs may be moved without explicit authorisation.  
  - [Ref: C-M(2002)49, AC/322-D(2017)0009]

- **Containment:** Upon confirmation, containment measures must be initiated immediately to limit incident propagation, including network segmentation, account suspension, and device isolation as appropriate.  
  - [Ref: NIST CSF 2.0 RS.CO, ISO/IEC 27001:2022 A.5.15]

- **Evidence Preservation:** Evidence must be preserved in line with chain of custody and NATO/host-nation legal requirements. Dual-key or two-person procedures apply for high-grade COMSEC or mission secrets.  
  - [Ref: AC/322-D(2017)0009, AC/35-D/1015]

#### 5.3 Incident Notification and Escalation

- **Escalation Pathways:** Significant incidents (as defined in the incident response plan) must be immediately escalated to NCIRC, NCSC, and host-nation CERT per alliance/host-nation protocols.  
  - [Ref: AC/322-D(2017)0009, Romanian Law 58/2019, NIS2]

- **COMSEC Incident Reporting:** All suspected or actual COMSEC incidents must be reported via national COMSEC authority and NATO COMSEC channels, per national and NATO directives.  
  - [Ref: AC/35-D/1015, AC/322-D(2017)0009]

- **Data Protection Notification:** Incidents involving personal data of NATO civilians/contractors must be notified to the Data Protection Officer and, where required, to host-nation authorities per GDPR/NIS2 within SOFA constraints.  
  - [Ref: GDPR Art. 33, Romanian Law 58/2019]

#### 5.4 Recovery and Post-Incident Activities

- **Service Restoration:** Restoration of CIS and COMSEC services must follow documented recovery plans, prioritising mission-essential functions and classified assets.  
  - [Ref: ISO/IEC 27001:2022 A.5.30, NIST CSF 2.0 RC.IM]

- **Root Cause Analysis:** Every major incident must be subject to documented root cause analysis and lessons-learned review within 10 working days of closure.  
  - [Ref: NIST CSF 2.0 RC.RP, ISO/IEC 27001:2022 A.10.1]

- **Reporting and Documentation:** All incident records must be maintained in accordance with NATO and host-nation retention requirements.  
  - [Ref: AC/322-D(2017)0009, ISO/IEC 27001:2022 A.8.12]

#### 5.5 Training and Exercising

- **Annual Training:** All personnel must receive annual incident response awareness training; cyber operations staff require a minimum of 40 hours/year of advanced training, including participation in at least 2 red-team exercises per year.  
  - [Ref: NATO Cyber Defence Pledge 2016, NIST CSF 2.0 PR.AT]

- **Exercise and Testing:** The incident response plan must be tested in at least 2 multinational exercises per year, with findings documented and remediated.  
  - [Ref: ISO/IEC 27001:2022 A.5.31]

---

### 6. Exceptions

Any exception to this policy (including emergency deviation during incident handling) must be approved by the ISSM and documented with rationale, scope, and duration. Exceptions are subject to review by NATO and national security authorities and may not override legal or classification requirements.  
- [Ref: ISO/IEC 27001:2022 A.5.36]

---

### 7. Monitoring and Review

- **Continuous Audit:** Incident response processes and controls are subject to continuous monitoring and regular internal/external audit (including NATO, NCIRC, and host-nation reviews).  
  - [Ref: AC/322-D(2017)0009, ISO/IEC 27001:2022 A.8.16]

- **Annual Review:** This policy and the underlying incident response plan shall be reviewed at least annually, or upon significant change in threat, mission, or regulatory regime.  
  - [Ref: ISO/IEC 27001:2022 A.5.35]

---

### 8. References

- NATO Information Security Policy (C-M(2002)49 and successor)
- AC/35-D/1015 Security within NATO
- AC/35-D/1029 Personnel security  
- AC/322-D(2017)0009 NATO INFOSEC technical and implementation directive
- Allied Joint Doctrine for Cyberspace Operations (AJP-3.20)
- NATO Cyber Defence Pledge 2016
- Romanian Cybersecurity Law 58/2019 (NIS/NIS2 transposition)
- General Data Protection Regulation (GDPR), EU 2016/679
- NATO SOFA (Status of Forces Agreement)
- NIST Cybersecurity Framework (CSF) 2.0
- ISO/IEC 27001:2022 and ISO/IEC 27002:2022

---

**End of Document**
