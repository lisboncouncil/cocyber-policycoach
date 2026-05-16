---
config: C0+web
context_id: ctx-M
policy_id: P4
policy_name: Incident Response Policy
policy_short: ir
metadata:
  config: C0+web
  model: gpt-4.1-2025-04-14
  input_tokens: 1660
  output_tokens: 1907
  total_tokens: 3567
  latency_s: 19.039
  tool_calls: []
  raw_provider_id: resp_0121136ff619ce4d0069fb70fb1d688193bc0a92dbf1e45b0e
sources_count: 0
sources: []
prompt_chars: 6045
answer_chars: 8148
generated_at_unix: 1778086157
---

---

# NATO Multinational Military Detachment  
**Incident Response Policy**  
**Effective Date:** 2024-07-01  
**Policy Owner:** Information Systems Security Manager (ISSM), J6 Chain  
**Review Cycle:** Annual (every 12 months) or upon major regulatory/mission change  
**Classification:** NATO UNCLASSIFIED (NU)  

---

## 1. Purpose

This policy defines the principles, roles, responsibilities, and requirements for incident response (IR) across all NATO, coalition, and host-nation information systems operated, managed, or used by the NATO Multinational Military Detachment in Romania. It ensures alignment with NATO, host-nation, and coalition regulatory frameworks, and implements best practices from NIST CSF 2.0 and ISO/IEC 27001:2022.

---

## 2. Scope

This policy applies to:
- All personnel (military, NATO civilian, contractors) with access to NATO, coalition, or host-nation networks and information assets under the detachment’s operational control.
- All information systems and networks (NU, NR, NS, MISSION SECRET domains) managed, operated, or accessed by the detachment.
- All incidents impacting the confidentiality, integrity, or availability of information or services, including classified, restricted, and unclassified systems.

---

## 3. Roles and Responsibilities

| Role                  | Responsibilities                                                                                          |
|-----------------------|----------------------------------------------------------------------------------------------------------|
| ISSM (Policy Owner)   | Oversight of IR planning, execution, compliance, and reporting. Maintains policy and delegates as needed.|
| Security Operations Center (SOC) | 24/7 monitoring, initial triage, escalation, and coordination with IR team and NCIRC.         |
| Incident Response Team (IRT)     | Executes IR plan, containment, eradication, recovery, evidence preservation, and reporting.   |
| J6 Chain of Command             | Operational decision-making, communications, and coordination with command and legal authorities.|
| COMSEC Custodian                | Manages cryptographic incidents and coordinates with national COMSEC authority.                |
| Personnel, Contractors, Users   | Immediate reporting of suspected incidents, cooperation with IR and SOC.                       |
| Host-Nation Liaison             | Coordinates with host-nation CERT and legal authorities, ensuring GDPR and SOFA compliance.   |

---

## 4. Principles

- **Defence-in-depth:** Incident response is integrated as part of a layered security posture (NIST CSF 2.0, ID.GV-1).
- **Timeliness:** Incidents are detected, reported, and responded to without undue delay (NATO C-M(2002)49, GDPR Art. 33).
- **Confidentiality:** All IR activities and reports are classified and protected according to the highest relevant classification domain (NATO C-M(2002)49).
- **Need-to-know:** Incident details are shared only with authorised personnel (NATO classification framework, ORCON).
- **Legal/regulatory alignment:** IR activities comply with NATO, host-nation (Romania, EU), and coalition requirements.
- **Continuous improvement:** Lessons identified from incidents are used to enhance procedures, controls, and training (ISO/IEC 27001:2022, 10.1).

---

## 5. Requirements and Controls

### 5.1. Preparation

- **IR Plan:** Maintain a documented IR Plan aligned with NATO CIRC (NCIRC) and host-nation CERT requirements. [NATO AC/322-D(2017)0009, NIST CSF RS.IM-1]
- **Training:** All staff complete at least 40 hours of security and IR training annually. [NATO Cyber Defence Pledge, ISO/IEC 27001:2022, 6.3]
- **Exercise:** Conduct six IR exercises per year, including at least two red-team engagements. [NIST CSF DE.DP-1, NATO AJP-3.20]
- **Asset Inventory:** Maintain up-to-date inventory of critical assets, prioritised by classification and mission impact. [NIST CSF ID.AM-1]

### 5.2. Detection and Reporting

- **Continuous Monitoring:** All domain boundaries and critical assets are monitored 24/7 by SOC sensors. [NIST CSF DE.CM-1, ISO/IEC 27001 A.8.16]
- **Incident Categories:** Incidents are categorised per NATO CIRC taxonomy (e.g., unauthorised access, spillage, COMSEC, supply-chain compromise). [NCIRC Process, NIST CSF RS.AN-1]
- **Mandatory Reporting:** All personnel must report suspected or confirmed incidents immediately to the SOC. [NATO C-M(2002)49, GDPR Art. 33]
- **Insider Threat:** Special focus is placed on reporting anomalous behaviour by cleared personnel and contractors. [ISO/IEC 27001 A.6.1, AC/35-D/1029]

### 5.3. Response

- **Triage and Containment:** SOC conducts initial triage; IRT leads containment and eradication, prioritising mission continuity. [NIST CSF RS.CO-2, ISO/IEC 27001 A.5.25]
- **Forensics and Preservation:** Evidence is preserved following chain-of-custody standards, especially for classified/COSMIC material and COMSEC. [NATO AC/35-D/1015, ISO/IEC 27001 A.8.18]
- **Spillage:** Immediate isolation of affected systems in case of cross-domain data spillages; notify originator and enforce ORCON. [NATO INFOSEC, AC/322-D(2017)0009]
- **COMSEC Incidents:** All cryptographic incidents are reported to national COMSEC authority; two-person integrity enforced. [NATO COMSEC Policy, dual-key procedures]
- **Host-Nation Engagement:** Notify host-nation CERT and NCSC within legally required timeframes; observe SOFA and GDPR constraints (report within 72 hours for personal data breaches). [GDPR Art. 33, Romanian Law 58/2019]

### 5.4. Recovery

- **Restoration:** Systems are restored using validated, secure backups, preserving forensic evidence where necessary. [NIST CSF RC.RP-1]
- **Remediation:** Root cause analysis is performed for all major incidents, with lessons learned documented. [ISO/IEC 27001 A.10.1]
- **Communications:** Inform stakeholders, including NATO, framework nations, and host-nation authorities, per incident communication plan. [NATO AJP-3.20, ORCON]

### 5.5. Post-Incident Activities

- **Reporting:** Formal incident reports are completed and archived per NATO and host-nation record-keeping requirements. [NATO CIRC, ISO/IEC 27001 A.8.17]
- **Lessons Learned:** All significant incidents undergo post-mortem analysis; findings drive updates to controls, training, and IR plan. [NIST CSF RS.IM-2]
- **Audit:** IR activities are subject to regular audit and review (minimum annually). [ISO/IEC 27001 A.10, NIST CSF ID.GV-3]

---

## 6. Exceptions

- Any exceptions to this policy must be approved in writing by the ISSM and authorised by the J6 chain of command.
- Exception requests must document the operational justification, risk assessment, and compensating controls.
- No exceptions shall be granted that violate applicable NATO, EU, or host-nation law.

---

## 7. Monitoring and Review

- The ISSM will ensure annual review of this policy and IR procedures, or more frequently if required by changes in mission, regulatory environment, or following major incidents.
- Effectiveness will be measured by exercise outcomes, audit findings, and incident statistics.
- Compliance is monitored through regular SOC reports, IR exercise after-action reviews, and external audits as required by NATO and host-nation authorities.

---

## 8. References

- **NATO C-M(2002)49:** NATO Information Security Policy
- **NATO AC/322-D(2017)0009:** NATO INFOSEC Technical Directive
- **NATO AC/35-D/1015:** Security within NATO
- **NATO AC/35-D/1029:** Personnel Security
- **NATO Cyber Defence Pledge (2016)**
- **NATO AJP-3.20:** Allied Joint Doctrine for Cyberspace Operations
- **NIST CSF 2.0:** National Institute of Standards and Technology Cybersecurity Framework
- **ISO/IEC 27001:2022:** Information Security Management
- **GDPR:** General Data Protection Regulation (EU 2016/679)
- **Romanian Cybersecurity Law 58/2019**
- **NCIRC:** NATO Computer Incident Response Capability Processes
- **NATO SOFA:** Status of Forces Agreement

---

**Approved by:**  
[Signature block for J6/ISSM]

**Distribution:**  
All NATO Detachment Personnel, Security Staff, Contractors, and Relevant Host-Nation Liaisons

---
