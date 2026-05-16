---
config: C0
context_id: ctx-M
policy_id: P4
policy_name: Incident Response Policy
policy_short: ir
metadata:
  config: C0
  model: gpt-4.1-2025-04-14
  input_tokens: 1366
  output_tokens: 2174
  total_tokens: 3540
  latency_s: 34.268
  tool_calls: []
  raw_provider_id: chatcmpl-DcZdMvHGozbb1rfHsLXWK4XNc9F8F
sources_count: 0
sources: []
prompt_chars: 6045
answer_chars: 8719
generated_at_unix: 1778085846
---

---

**NATO Multinational Military Detachment — Incident Response Policy**

**Document ID:** NMD-SEC-IRP-001  
**Effective Date:** 2024-07-01  
**Owner:** Information Systems Security Manager (ISSM), J6  
**Review Cycle:** Annual (or upon major regulatory/mission change)  
**Classification:** NATO RESTRICTED  
**Language:** English

---

### 1. Purpose

This policy establishes the principles, roles, and mandatory controls for incident response (IR) across all information systems, networks, and personnel assigned to, or supporting, the NATO Multinational Military Detachment deployed in Romania. It ensures compliance with NATO, host-nation, coalition, and international cybersecurity requirements, enabling timely, coordinated, and effective response to cyber and information security incidents.

---

### 2. Scope

This policy applies to:  
- All military, civilian, and contractor personnel (hereafter “staff”) assigned or attached to the Detachment;  
- All information systems, networks, and devices managed or operated by the Detachment, including NATO, coalition, and mission-specific systems (NU, NR, NS, MISSION SECRET domains);  
- All classified and unclassified workstations, CIS, and COMSEC assets under Detachment operational control.

The policy encompasses the full IR lifecycle: preparation, detection, analysis, containment, eradication, recovery, post-incident activities, and reporting.

---

### 3. Roles and Responsibilities

#### 3.1 Information Systems Security Manager (ISSM), J6
- Policy owner; ensures alignment with NATO and host-nation frameworks (C-M(2002)49, AC/35-D/1015, Law 58/2019, NIST CSF 2.0).
- Maintains the Incident Response Plan (IRP) and supporting procedures.
- Liaises with NATO CIRC (NCIRC), NCSC, host-nation CERT, and coalition partners.

#### 3.2 Security Operations Center (SOC)
- Provides 24/7 monitoring, detection, initial triage, and escalation.
- Maintains sensor coverage at all classification domain boundaries.
- Coordinates with ISSM and IR Team during incidents.

#### 3.3 Incident Response Team (IRT)
- Cross-domain team of security, technical, and legal/CI representatives.
- Executes IRP per assigned incident category and domain.
- Maintains evidence handling and chain of custody.

#### 3.4 Chain of Command (COC)
- Ensures operational continuity and mission impact assessment.
- Approves major response actions affecting mission systems or classified networks.

#### 3.5 All Staff
- Must immediately report suspected incidents, spillage, or compromise via established channels (ref. AC/35-D/1015, NIST CSF ID.RA-5).
- Participate in IR training and exercises.

#### 3.6 Contractors and Vendors
- Subject to all incident reporting and cooperation requirements as per contract and security clearance terms (AC/322-D(2017)0009, Law 58/2019).

---

### 4. Principles

- **Mission Assurance:** IR procedures prioritise operational continuity and protection of classified information (AJP-3.20, C-M(2002)49).
- **Classified Domain Separation:** Incidents are contained within their domain; cross-domain spillages invoke mandatory separation and reporting (AC/322-D(2017)0009 9.5.3).
- **Regulatory Alignment:** All IR activities comply with NATO, host-nation law (including GDPR for personal data), and coalition agreements.
- **Need-to-Know and Originator Control:** Incident information is disseminated only as required for response and mandated reporting (C-M(2002)49, ORCON).
- **Chain of Custody:** Forensic and COMSEC evidence is handled under auditable, two-person integrity processes (NATO COMSEC policy, AC/35-D/1015 §29).
- **Continuous Improvement:** Post-incident review and lessons learned are mandatory (NIST CSF RS.IM-1, ISO/IEC 27001:2022 A.5.25).

---

### 5. Requirements / Controls

#### 5.1 Preparation

- Maintain a documented Incident Response Plan (IRP) aligned with NCIRC and host-nation CERT requirements.  
  _[Ref: NIST CSF RS.RP-1, AC/322-D(2017)0009 9.3.1]_

- Conduct annual IR exercises (minimum 6 per year), including cross-domain, red team, and major incident scenarios.  
  _[C-M(2002)49, NIST CSF RS.IM-1]_

- Ensure all staff receive at least 4 hours/year of IR training as part of the 40-hour security curriculum.  
  _[ISO/IEC 27001:2022 A.6.3, NIST CSF PR.AT-3]_

#### 5.2 Detection and Reporting

- All security events and potential incidents must be reported immediately to the SOC via secure channels.  
  _[AC/35-D/1015 §19, NIST CSF DE.CM-1]_

- SOC must monitor all network and cross-domain boundaries 24/7 and maintain detection coverage for classified and unclassified domains.  
  _[AC/322-D(2017)0009 9.5.2, NIST CSF DE.CM-7]_

- Spillage between classification domains is a critical incident and triggers mandatory containment and escalation procedures.  
  _[AC/322-D(2017)0009 9.5.3]_

#### 5.3 Analysis and Categorisation

- Incidents are categorised by impact, classification, and regulatory exposure (e.g., personal data, COMSEC, coalition assets).  
  _[ISO/IEC 27001:2022 A.5.25, NIST CSF RS.AN-1]_

- Forensic analysis is conducted using tools and methods approved for the relevant classification domain; evidence is preserved with chain of custody.  
  _[NATO COMSEC policy, NIST CSF RS.AN-2]_

#### 5.4 Containment, Eradication, and Recovery

- Containment actions must prioritise preventing lateral movement across classification domains and preserving mission continuity.  
  _[AJP-3.20, NIST CSF RS.CO-2]_

- Only authorised IR Team personnel may execute containment or restoration actions on classified systems; dual-key/dual-control procedures are enforced for NS and above.  
  _[AC/322-D(2017)0009 9.3.4, NATO COMSEC policy]_

- Compromised COMSEC material is quarantined and reported per national and NATO COMSEC directives; destruction follows two-person integrity.  
  _[NATO COMSEC policy, AC/35-D/1015 §29]_

#### 5.5 Communication and Reporting

- All incidents are reported to the NCIRC per established timelines and procedures, with parallel notification to host-nation NCSC and, if involving personal data, the DPO for GDPR compliance.  
  _[C-M(2002)49, Law 58/2019, GDPR Art. 33, NIST CSF RS.CO-5]_

- Information sharing with coalition partners follows originator control and information-sharing agreements; dissemination outside NATO channels requires prior authorisation.  
  _[C-M(2002)49, ORCON, AC/35-D/1015 §12]_

#### 5.6 Post-Incident Activities

- Every major incident requires a formal post-incident review within 10 business days, including root cause analysis, lessons learned, and remediation plan.  
  _[NIST CSF RS.IM-1, ISO/IEC 27001:2022 A.5.25]_

- IRP and related procedures are updated promptly to integrate lessons learned from exercises and real-world incidents.  
  _[NIST CSF RS.IM-2, ISO/IEC 27001:2022 A.10.1]_

#### 5.7 Special Considerations

- Insider threats and suspected HUMINT activity are escalated to Counterintelligence (CI) and handled under additional confidentiality controls.  
  _[NATO CI Policy, unsupported (no open citation)]_

- Supply chain incidents involving vendors/contractors are jointly managed with the Procurement Office and reported per contractual and security requirements.  
  _[ISO/IEC 27001:2022 A.15.1, NIST CSF ID.SC-4]_

---

### 6. Exceptions

- Any deviation from this policy requires advance written approval from the ISSM and, where required, SHAPE legal/security authorities.
- Emergency actions taken to protect life or mission must be documented and reported for post-incident review and retroactive authorisation.

---

### 7. Monitoring and Review

- The ISSM will monitor policy effectiveness through regular incident metrics, exercise outcomes, and post-incident reviews.
- The policy will be reviewed annually, or in response to major changes in NATO or host-nation regulatory frameworks, Detachment mission, or threat landscape.
- Auditability is ensured through documented logs, incident reports, and change records for all IR actions (ISO/IEC 27001:2022 A.10.1, NIST CSF RS.IM-3).

---

### 8. References

1. NATO Information Security Policy C-M(2002)49  
2. AC/35-D/1015 Security within NATO  
3. AC/35-D/1029 Personnel Security  
4. AC/322-D(2017)0009 NATO INFOSEC Technical and Implementation Directive  
5. Allied Joint Doctrine for Cyberspace Operations (AJP-3.20)  
6. NATO Cyber Defence Pledge (2016)  
7. Romanian Law 58/2019 (NIS, NIS2 transposition)  
8. GDPR (EU Regulation 2016/679)  
9. NIST Cybersecurity Framework (CSF) v2.0  
10. ISO/IEC 27001:2022, ISO/IEC 27002:2022  
11. NATO Status of Forces Agreement (SOFA)  
12. NATO COMSEC Policy  
13. Bilateral/multilateral information-sharing agreements  
14. Detachment IR Plan and Standard Operating Procedures

---

**End of Policy**
