---
config: C0
context_id: ctx-M
policy_id: P1
policy_name: Information Security Policy
policy_short: infosec
metadata:
  config: C0
  model: gpt-4.1-2025-04-14
  input_tokens: 1015
  output_tokens: 2497
  total_tokens: 3512
  latency_s: 26.983
  tool_calls: []
  raw_provider_id: chatcmpl-DcZAAm4yRopRho4zkDZL1hID1jtxh
sources_count: 0
sources: []
prompt_chars: 4956
answer_chars: 10098
generated_at_unix: 1778084029
---

---
**INFORMATION SECURITY POLICY**  
**NATO Allied Command Operations – Multinational Military Detachment, Romania**  
**Effective date:** 2024-07-01  
**Policy owner:** Information Systems Security Manager (ISSM), J6  
**Review cycle:** Annual (or upon significant change in mission, threat, or regulatory context)  
---

### 1. PURPOSE

This Information Security Policy establishes the principles, responsibilities, and controls for ensuring the confidentiality, integrity, and availability of NATO, national, and mission information assets managed by the NATO multinational military detachment in Romania. The policy is designed to support the detachment’s mission set—cyber defence, CIS operations, signals intelligence, and multinational interoperability—while ensuring compliance with all applicable NATO, host-nation, and international regulatory frameworks.

---

### 2. SCOPE

This policy applies to:

- All personnel assigned or attached to the detachment, including military, NATO civilians, and cleared contractors.
- All information assets, information systems, and networks under detachment operational control, across NATO UNCLASSIFIED (NU), NATO RESTRICTED (NR), NATO SECRET (NS), and MISSION SECRET domains.
- All activities involving the processing, storage, or transmission of information within the detachment’s remit, regardless of location or medium.
- All suppliers and third parties with access to detachment networks or classified information.

---

### 3. ROLES AND RESPONSIBILITIES

#### 3.1 Information Systems Security Manager (ISSM), J6  
- Accountable for the implementation and oversight of this policy.  
- Ensures alignment with applicable NATO directives (e.g., C-M(2002)49, AC/322-D(2017)0009), host-nation law, and international standards (NIST CSF 2.0, ISO/IEC 27001:2022).

#### 3.2 Information Systems Security Officers (ISSO) and Cyber Operations Team  
- Implement technical and procedural controls as assigned.  
- Conduct monitoring, incident response, and reporting per NCIRC and NCSC processes.

#### 3.3 Command Staff  
- Ensure compliance within their functional and national elements.  
- Support enforcement of need-to-know and dual-key procedures.

#### 3.4 All Users (Military, Civilian, Contractor)  
- Comply with this policy and all supporting standards/procedures.  
- Complete annual information security awareness and role-based training.

#### 3.5 COMSEC Custodians  
- Manage cryptographic material in accordance with NATO and national COMSEC regulations (e.g., AC/322-D(2017)0009; national COMSEC authority guidance).  
- Maintain two-person integrity and auditable chain of custody.

#### 3.6 Supply Chain/Vendor Managers  
- Ensure supply chain controls are applied to all procured CIS/COMSEC equipment and services, using NATO-approved vendor lists and host-nation screening processes.

---

### 4. INFORMATION SECURITY PRINCIPLES

#### 4.1 Compliance  
All activities must comply with NATO, host-nation, and applicable international information security requirements, including but not limited to:

- **NATO Information Security Policy** (C-M(2002)49 and successors)
- **NATO INFOSEC Technical Directive** (AC/322-D(2017)0009)
- **Romanian Cybersecurity Law** (Law 58/2019, NIS/NIS2)
- **GDPR** (for personal data of EU-based civilians/contractors, within SOFA limits)
- **NIST CSF 2.0** and **ISO/IEC 27001:2022** as technical reference frameworks

#### 4.2 Defence-in-Depth  
Layered administrative, technical, and physical controls will be applied across all classification domains, commensurate with risk and mission criticality.  
(*Ref: NIST CSF 2.0 ID.GV-1, NATO C-M(2002)49 Art. 8, ISO/IEC 27001:2022 A.5.7*)

#### 4.3 Domain Separation  
Strict separation between classification domains (NU, NR, NS, MISSION SECRET) must be enforced; cross-domain flows only via accredited NATO Cross-Domain Solutions.  
(*Ref: AC/322-D(2017)0009 Section 8.5, NATO INFOSEC Directive Annex B*)

#### 4.4 Need-to-Know and Originator Control  
Access to classified information is by need-to-know, with originator control (ORCON) on intelligence products.  
(*Ref: C-M(2002)49 Art. 10, AC/35-D/1015, ISO/IEC 27001:2022 A.5.11*)

#### 4.5 Personnel Security  
All personnel must have appropriate clearance and be subject to ongoing vetting, in accordance with NATO and host-nation regulations.  
(*Ref: AC/35-D/1029, ISO/IEC 27001:2022 A.6.1*)

---

### 5. INFORMATION SECURITY REQUIREMENTS AND CONTROLS

#### 5.1 Access Control  
- All users are authenticated via NATO PKI and smart card (CAC-equivalent) at each classification domain; no cross-domain identity federation is permitted.  
- Access to classified networks and systems is restricted by clearance, role, and need-to-know.  
- Administrative and privileged access is subject to technical controls and logging.  
(*Ref: AC/322-D(2017)0009 Sec. 7.1, ISO/IEC 27001:2022 A.8.2, NIST CSF PR.AC-1/3/4*)

#### 5.2 Domain Separation and Cross-Domain Security  
- Network domains (NU/NR/NS/MISSION SECRET) are physically and logically separated, with only NATO-accredited Cross-Domain Solutions permitted for information transfer.  
- Cross-domain transfers are logged, auditable, and subject to two-person integrity for high-grade material.  
(*Ref: AC/322-D(2017)0009 Sec. 8.5, NATO CDS Policy, ISO/IEC 27001:2022 A.8.10*)

#### 5.3 Cryptography and COMSEC  
- All classified communications are protected by NATO-approved cryptographic equipment and key management practices.  
- Dual-key/two-person control is mandatory for high-grade COMSEC and selected operational orders.  
- Keying material is handled in accordance with national COMSEC authority and NATO procedures, with auditable chain of custody.  
(*Ref: AC/322-D(2017)0009 Sec. 9, NATO COMSEC Policy, ISO/IEC 27001:2022 A.10.1*)

#### 5.4 Monitoring and Detection  
- All network and security events are monitored 24/7 by the theatre SOC; incident response is performed per NCIRC and NCSC processes, with escalation to the host-nation CERT as required.  
- Audit logs are retained and protected per NATO INFOSEC standards.  
(*Ref: AC/322-D(2017)0009 Sec. 11, ISO/IEC 27001:2022 A.8.15, NIST CSF DE.CM-1/7*)

#### 5.5 Personnel Security and Insider Threat  
- All personnel (including contractors) are subject to initial and recurring security vetting per NATO and host-nation requirements.  
- Insider threat detection and mitigation measures are implemented, including monitoring, awareness, and reporting channels.  
(*Ref: AC/35-D/1029, NIST CSF PR.AT-1, ISO/IEC 27001:2022 A.6.3*)

#### 5.6 Supply Chain Security  
- Only NATO-approved equipment and vetted vendors may be used for CIS and COMSEC procurement; host-nation contractors must pass security screening.  
- Supply chain risk assessments are conducted as part of procurement and onboarding.  
(*Ref: AC/322-D(2017)0009 Sec. 12, NIST CSF ID.SC-1/2, ISO/IEC 27001:2022 A.15.1*)

#### 5.7 Physical and Environmental Security  
- Access to critical infrastructure and classified areas is controlled, logged, and limited to authorized personnel.  
- TEMPEST controls are implemented per NATO and national standards for all high-grade processing.  
(*Ref: AC/322-D(2017)0009 Sec. 13, ISO/IEC 27001:2022 A.7.1, NATO TEMPEST Policy*)

#### 5.8 Data Protection and Privacy  
- Personal data of NATO civilian staff and contractors is processed in accordance with GDPR and Romanian Cybersecurity Law, within SOFA legal limitations.  
- Data subject rights and data breach notification processes are established as per GDPR.  
(*Ref: GDPR Art. 32, Law 58/2019, ISO/IEC 27001:2022 A.8.1*)

#### 5.9 Incident Response  
- All cybersecurity incidents are managed per documented incident response plans, aligned with NCIRC/NCSC/host-nation CERT requirements.  
- Major incidents are escalated and reported in accordance with NATO Information Security Policy timelines.  
(*Ref: AC/322-D(2017)0009 Sec. 14, NIST CSF RS.RP-1, ISO/IEC 27001:2022 A.5.26*)

#### 5.10 Training and Awareness  
- All personnel complete at least 40 hours/year of cybersecurity awareness and role-based technical training.  
- Training effectiveness is reviewed annually and updated as required.  
(*Ref: NIST CSF PR.AT-1, ISO/IEC 27001:2022 A.6.3*)

#### 5.11 Exercise and Testing  
- The detachment will conduct at least 6 security exercises and 2 red-team engagements per year, in line with NATO and host-nation requirements.  
- Lessons identified are reviewed and integrated into controls and procedures.  
(*Ref: NIST CSF PR.IP-10, NATO CD Pledge 2016*)

---

### 6. EXCEPTIONS

- Any exception to this policy must be formally requested in writing to the ISSM/J6, with justification and risk assessment.
- Exceptions will be granted only where operationally necessary, must be time-limited, and are subject to higher command and/or national authority approval as required.
- All exceptions are logged and periodically reviewed.

(*No direct reference; general governance best practice—unsupported*)

---

### 7. MONITORING, REVIEW, AND CONTINUOUS IMPROVEMENT

- The ISSM will review this policy at least annually, or upon significant change in threat, mission, or regulatory context.
- Compliance with this policy is monitored through audits, technical monitoring, and incident reporting.
- Non-compliance is reported to command, and corrective actions are tracked to closure.

(*Ref: ISO/IEC 27001:2022 A.5.36, NIST CSF ID.GV-4*)

---

### 8. REFERENCES

- NATO Information Security Policy (C-M(2002)49 and successor)
- Security within NATO (AC/35-D/1015)
- Personnel Security within NATO (AC/35-D/1029)
- NATO INFOSEC Technical and Implementation Directive (AC/322-D(2017)0009)
- NATO Cyber Defence Pledge (2016)
- Allied Joint Doctrine for Cyberspace Operations (AJP-3.20)
- Romanian Cybersecurity Law (Law 58/2019, NIS/NIS2)
- General Data Protection Regulation (GDPR) (EU 2016/679)
- NATO SOFA (Status of Forces Agreement)
- NIST Cybersecurity Framework v2.0
- ISO/IEC 27001:2022, ISO/IEC 27002:2022

---

**Approved by:**  
[Detachment Commander or Senior NATO Representative]  
**Date:** [TBD]
