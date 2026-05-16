---
config: C0
context_id: ctx-M
policy_id: P5
policy_name: General Cybersecurity Policy
policy_short: infosec
metadata:
  config: C0
  model: gpt-4.1-2025-04-14
  input_tokens: 1368
  output_tokens: 2512
  total_tokens: 3880
  latency_s: 38.285
  tool_calls: []
  raw_provider_id: chatcmpl-DcZducDCR6g7WXC9Z5fqfbGyKN96l
sources_count: 0
sources: []
prompt_chars: 6053
answer_chars: 10188
generated_at_unix: 1778085884
---

---
# General Cybersecurity Policy

**Organisation:** NATO SHAPE-Sponsored Multinational Military Detachment, Romania  
**Effective Date:** [Insert Date]  
**Policy Owner:** Information Systems Security Manager (ISSM), J6  
**Review Cycle:** Annual or on change of mission/regulatory framework  
**Classification:** NATO UNCLASSIFIED (for dissemination); individual controls may reference higher classification requirements as appropriate.

---

## 1. Purpose

This General Cybersecurity Policy defines the principles, responsibilities, and mandatory controls governing the protection of information, communications, and information systems (CIS) operated by the NATO SHAPE-sponsored multinational detachment in Romania. The policy ensures compliance with NATO, host-nation (Romanian/EU), coalition, and contributing nation requirements, and aligns with internationally recognised cybersecurity frameworks (NIST CSF 2.0, ISO/IEC 27001:2022, GDPR) as appropriate.

---

## 2. Scope

This policy applies to:

- All personnel assigned to or supporting the detachment (military, civilian NATO staff, cleared contractors).
- All CIS assets and information processed, stored, or transmitted within the detachment’s control, across all classification domains (NU, NR, NS, MISSION SECRET).
- All physical locations, including deployed and SCIF environments.
- All activities supporting the detachment’s mission set, including cyber defence, CIS operations, signals intelligence, and coalition exercises.

---

## 3. Roles and Responsibilities

| Role/Body                      | Responsibility                                                                                                 | References                                           |
|---------------------------------|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| **ISSM (J6)**                   | Policy owner; oversight of cybersecurity; reporting to command and external authorities; ensures compliance.    | AJP-3.20; AC/322-D(2017)0009; NIST CSF ID.GV-1      |
| **Security Staff (25 FTE)**     | Implement and monitor controls; perform incident response; conduct awareness training and exercises.            | NIST CSF PR.AT-1; ISO 27001:2022 cl. 5.3            |
| **SOC (24/7 Theatre-Level)**    | Monitor networks; detect, analyse, and escalate incidents; coordinate with NCIRC, NCSC, host-nation CERT.      | C-M(2002)49; NIST CSF DE.DP-1; ISO 27001 cl. 6.1.3  |
| **COMSEC Custodians**           | Manage COMSEC equipment and keying material; enforce two-person integrity and auditable chain-of-custody.       | AC/35-D/1015; NATO COMSEC Policy                    |
| **All Users**                   | Adhere to security controls; report incidents; complete annual cyber awareness training.                        | NIST CSF PR.AT-1; ISO 27001 cl. 7.2                 |
| **Contractor Managers**         | Ensure contractors are vetted, briefed, and comply with policy and host-nation legal requirements.              | AC/35-D/1029; GDPR                                  |
| **Host-Nation Liaison**         | Coordinate local compliance, especially for GDPR and Romanian Cybersecurity Law.                                | Law 58/2019; GDPR                                   |

---

## 4. Principles

1. **Mission Assurance:** CIS and information assets are protected to ensure uninterrupted operational capability.  
   *[AJP-3.20; NIST CSF ID.AM-5]*
2. **Defence-in-Depth:** Layered technical, procedural, and physical controls across classification domains.  
   *[NIST CSF PR.AC-1; ISO 27001 cl. 6.1.3]*
3. **Need-to-Know/Least Privilege:** Access to information and systems is strictly limited by role, clearance, and mission requirement.  
   *[C-M(2002)49; NIST CSF PR.AC-4]*
4. **Separation of Domains:** Cross-domain transfers are strictly controlled and auditable; no cross-domain identity federation is permitted.  
   *[AC/322-D(2017)0009; NIST CSF PR.DS-5]*
5. **Compliance:** All activities conform to NATO, host-nation (Romanian/EU), coalition, and contributing nation cybersecurity requirements.  
   *[C-M(2002)49; Law 58/2019; GDPR]*
6. **Continuous Improvement:** Controls, processes, and training are reviewed and improved based on threat intelligence, lessons learned, and exercise outcomes.  
   *[NIST CSF ID.IM-1; ISO 27001 cl. 10.2]*

---

## 5. Requirements and Controls

### 5.1 Governance and Risk Management

- **Policy Approval and Review:** This policy and all subordinate policies are reviewed annually or upon significant change in mission, threat, or regulatory regime.  
  *[ISO 27001 cl. 5.1; NIST CSF ID.GV-1]*
- **Risk Assessment:** The ISSM ensures that risk assessments are conducted annually and upon major system changes, considering state-sponsored APTs, insider threat, supply-chain, and kinetic-cyber convergence.  
  *[NIST CSF ID.RA-1; ISO 27001 cl. 6.1.2]*
- **Supply Chain Security:** Procurements are limited to NATO-approved equipment/vendors; host-nation contractors are security-screened.  
  *[AC/35-D/1015; NIST CSF ID.SC-1]*

### 5.2 Access Control

- **Role-Based Access:** Access to each domain and system is role-based and requires a valid clearance.  
  *[C-M(2002)49; NIST CSF PR.AC-4; ISO 27001 cl. 9.1]*
- **Authentication:** PKI-based smart card authentication is mandatory on all domains; no cross-domain identity federation.  
  *[AC/322-D(2017)0009; NIST CSF PR.AC-7]*
- **Need-to-Know Enforcement:** Default-deny is enforced at all classification levels; exceptions require documented justification and authorisation.  
  *[C-M(2002)49; NIST CSF PR.AC-6]*

### 5.3 Network and System Security

- **Network Segmentation:** Physical and logical separation of NU, NR, NS, and MISSION SECRET domains.  
  *[AC/322-D(2017)0009; NIST CSF PR.AC-5]*
- **Cross-Domain Solutions:** Only NATO-accredited CDS may be used for information transfers; all transfers logged and subject to regular audit.  
  *[AC/322-D(2017)0009; NIST CSF PR.DS-5]*
- **Endpoint Security:** All workstations are centrally managed, patched, and protected with NATO-approved endpoint protection.  
  *[NIST CSF PR.IP-12; ISO 27001 cl. 8.1]*
- **COMSEC:** Management of cryptographic material follows NATO and national policy; dual-key and two-person integrity enforced for high-grade material.  
  *[AC/35-D/1015; NATO COMSEC Policy]*

### 5.4 Detection and Monitoring

- **Continuous Monitoring:** 24/7 SOC at theatre level monitors all domain boundaries with NATO-standard sensors.  
  *[NIST CSF DE.CM-1; ISO 27001 cl. 9.1]*
- **Logging:** Full logging of privileged access, cross-domain transfers, and security events, retained per NATO and host-nation requirements.  
  *[AC/322-D(2017)0009; NIST CSF DE.AE-3]*
- **Red Team/Exercises:** Minimum of two red-team engagements and six multinational cyber exercises per year.  
  *[NATO Cyber Defence Pledge 2016]*

### 5.5 Incident Response

- **IR Plan:** Incident response procedures align with NATO CIRC/NCIRC processes; escalation to NCSC and host-nation CERT as required.  
  *[AJP-3.20; NIST CSF RS.RP-1; ISO 27001 cl. 6.1.3]*
- **Reporting:** All users must report suspected or confirmed incidents immediately via established channels.  
  *[NIST CSF RS.CO-2]*
- **Containment/Remediation:** The SOC and ISSM coordinate immediate isolation, analysis, and remediation of incidents.  
  *[NIST CSF RS.CO-3]*

### 5.6 Physical and Environmental Security

- **Site Access:** Physical access to IT areas and SCIFs is controlled, logged, and limited to cleared personnel as per need-to-know.  
  *[ISO 27001 cl. 11.1; NATO SCIF Policy]*
- **TEMPEST:** NS and above equipment located only in accredited SCIF zones; periodic TEMPEST inspections conducted.  
  *[NATO INFOSEC Directive; NIST SP 800-53 PE-19]*

### 5.7 Personnel Security

- **Screening:** All personnel (including contractors) are cleared to the appropriate level and briefed on their security obligations.  
  *[AC/35-D/1029; ISO 27001 cl. 7.1]*
- **Awareness Training:** Minimum 40 hours cyber and INFOSEC training per staff per year, including insider threat and counterintelligence awareness.  
  *[NIST CSF PR.AT-1]*

### 5.8 Data Protection and Privacy

- **GDPR Compliance:** Civilian and contractor personal data is processed in accordance with GDPR and Romanian law; SOFA limitations on host-nation access apply.  
  *[GDPR Art. 5, 32; Law 58/2019]*
- **Originator Control:** All shared classified products are marked for originator control (ORCON) where required.  
  *[NATO Classification Policy]*

---

## 6. Exceptions

- Exceptions to this policy require written justification, risk assessment, and approval by the ISSM, with notification to the NATO SHAPE J6 and, where applicable, the host-nation authority.
- Emergency deviations during operations must be documented and reported post-facto within 24 hours.  
  *[ISO 27001 cl. 6.1.3 (f)]*

---

## 7. Monitoring and Review

- This policy is reviewed annually by the ISSM and Security Staff, with input from command, contributing nations, and host-nation liaison.
- Compliance audits are conducted in line with the NATO INFOSEC Directive and contributing-nation requirements.
- Lessons from incidents, exercises, and red-team engagements inform policy updates and procedural improvements.
- Reports on compliance, exceptions, and incidents are submitted to operational command, NCIRC, and host-nation authorities as required.

---

## 8. References

- NATO Information Security Policy (C-M(2002)49)
- AC/35-D/1015 Security within NATO
- AC/35-D/1029 Personnel Security
- AC/322-D(2017)0009 NATO INFOSEC Technical and Implementation Directive
- NATO Cyber Defence Pledge 2016
- Allied Joint Doctrine for Cyberspace Operations (AJP-3.20)
- Romanian Cybersecurity Law (Law 58/2019)
- GDPR (Regulation (EU) 2016/679)
- NIST Cybersecurity Framework (CSF) 2.0
- ISO/IEC 27001:2022; ISO/IEC 27002:2022
- NATO Status of Forces Agreement (SOFA)
- NATO COMSEC Policy
- NCSC and host-nation CERT guidance

---

**Approval:**  
[Signature block of ISSM/J6 and Command Authority]  
[Date]

---
