---
config: C0+web
context_id: ctx-M
policy_id: P1
policy_name: Information Security Policy
policy_short: infosec
metadata:
  config: C0+web
  model: gpt-4.1-2025-04-14
  input_tokens: 1309
  output_tokens: 2092
  total_tokens: 3401
  latency_s: 34.771
  tool_calls: []
  raw_provider_id: resp_03381b41043dfd870069fb697db30c819e9d75cc89d93b90c6
sources_count: 0
sources: []
prompt_chars: 4956
answer_chars: 7721
generated_at_unix: 1778084256
---

---

**INFORMATION SECURITY POLICY**  
**NATO Multinational Military Detachment, Romania**  
**Effective Date:** 2024-07-01  
**Policy Owner:** ISSM, J6 Chain  
**Review Cycle:** Annual or upon significant regulatory/mission change

---

### 1. PURPOSE

This policy establishes the framework for protecting the confidentiality, integrity, and availability of information and communications systems supporting the NATO Multinational Military Detachment in Romania. It ensures compliance with NATO and host-nation legal and regulatory requirements, and supports the mission’s operational effectiveness in a contested, multinational environment.

---

### 2. SCOPE

This policy applies to all personnel (military, NATO civilians, and contractors) assigned to or supporting the Detachment, all systems and data handled within the Detachment’s four classified network domains (NATO UNCLASSIFIED (NU), NATO RESTRICTED (NR), NATO SECRET (NS), MISSION SECRET), and all supporting facilities, information, and technology resources under the Detachment’s operational control.

---

### 3. ROLES AND RESPONSIBILITIES

**3.1 Information Systems Security Manager (ISSM):**  
- Overall owner of the policy and accountable for compliance (NATO: AC/322-D(2017)0009; ISO/IEC 27001:2022, A.5.3).
- Leads the cyber security team, reporting to the J6.

**3.2 Information Systems Security Officers (ISSOs):**  
- Support the ISSM in implementing controls, incident response, and user awareness (NATO: AC/322-D(2017)0009 3.3.2).

**3.3 COMSEC Custodian:**  
- Responsible for COMSEC key management and two-person integrity procedures (NATO: AC/322-D(2017)0009, Section 10; AC/35-D/1015).

**3.4 Security Operations Center (SOC):**  
- 24/7 monitoring, detection, and escalation per NCIRC process (NATO: AC/322-D(2017)0009, 8.1.3).

**3.5 All Users:**  
- Comply with all security procedures, report incidents, and complete required training (NATO: AC/322-D(2017)0009, 3.3.3; ISO 27001:2022 A.6.3).

---

### 4. PRINCIPLES

- **Defence in Depth:** Layered security for all classified domains and mission systems (NATO: C-M(2002)49; NIST CSF 2.0).
- **Need-to-Know:** Access to information is strictly limited and enforced by technical and procedural controls (NATO: AC/35-D/1015, 2.3).
- **Separation of Domains:** Physical and logical separation between NU, NR, NS, and MISSION SECRET networks, enforced by accredited Cross-Domain Solutions (NATO: AC/322-D(2017)0009, 6.2.2).
- **Originator Control (ORCON):** Classified products subject to release controls by originating authority (NATO: AC/35-D/1015).
- **Compliance:** Adherence to NATO, host-nation, and international law and standards (see Section 8).

---

### 5. REQUIREMENTS AND CONTROLS

#### 5.1 Access Control

- **Identity & Authentication:**  
  All user and privileged access must use PKI-based smart card authentication aligned to the relevant classification domain. No cross-domain identity federation permitted (NATO: AC/322-D(2017)0009, 7.4; ISO/IEC 27001:2022, A.5.18).
- **Need-to-Know:**  
  Default-deny posture on all classified networks; access granted only on documented mission justification (NATO: AC/35-D/1015, 2.3; NIST CSF ID.AM-3).
- **Account Reviews:**  
  Quarterly review of user access rights by ISSO (NATO: AC/322-D(2017)0009, 7.7; ISO 27001 A.5.18).

#### 5.2 Domain Separation

- **Network Segmentation:**  
  NU, NR, NS, and MISSION SECRET domains physically and logically separated; only accredited NATO Cross-Domain Solutions may bridge domains (NATO: AC/322-D(2017)0009, 6.2.2).
- **Data Transfer Controls:**  
  All cross-domain transfers subject to content filtering and release approval (NATO: AC/322-D(2017)0009, 6.2.3).

#### 5.3 COMSEC and Cryptographic Controls

- **Key Management:**  
  All cryptographic keying material handled under national COMSEC authority and two-person integrity for high-grade material (NATO: AC/322-D(2017)0009, 10.3; AC/35-D/1015).
- **Chain of Custody:**  
  Auditable two-person chain of custody for all classified COMSEC material (NATO: AC/35-D/1015, 4.5).

#### 5.4 Personnel Security

- **Screening:**  
  All personnel (including host-nation contractors) must be security cleared to level commensurate with their access (NATO: AC/35-D/1029).
- **Insider Threat Mitigation:**  
  User activity monitoring on all classified networks; mandatory annual counterintelligence briefings (NATO: AC/322-D(2017)0009, 8.3; NIST CSF DE.AE-1).

#### 5.5 Supply Chain Security

- **Vendor Vetting:**  
  Only NATO-vetted vendors and NATO-approved equipment may be procured for CIS/COMSEC (NATO: AC/322-D(2017)0009, 9.2).
- **Contractor Oversight:**  
  Host-nation contractors subject to security screening and need-to-know restrictions (NATO: AC/35-D/1029; ISO/IEC 27001:2022, A.5.19).

#### 5.6 Physical and TEMPEST Controls

- **Facility Security:**  
  Physical access controls, guard force, and intrusion detection for all sensitive areas (NATO: AC/35-D/1015, 5.3).
- **TEMPEST:**  
  Sensitive sites assessed and protected against electromagnetic eavesdropping per NATO and host-nation standards (NATO: AC/322-D(2017)0009, 11.2).

#### 5.7 Monitoring, Detection, and Incident Response

- **SOC Operations:**  
  24/7 monitoring with escalation routes to NCIRC, NCSC, and host-nation CERT as documented (NATO: AC/322-D(2017)0009, 8.1.3).
- **Incident Handling:**  
  All suspected or confirmed incidents handled per NCIRC SOP; major incidents escalated to appropriate authorities (NATO: AC/322-D(2017)0009, 8.2).

#### 5.8 Training and Awareness

- **Mandatory Training:**  
  All personnel must complete a minimum of 40 hours of security training annually, including cyber incident response and counterintelligence topics (NATO: AC/322-D(2017)0009, 3.3.3; ISO/IEC 27001:2022, A.6.3).
- **Exercises:**  
  The Detachment conducts at least 6 security exercises and 2 red team engagements per year to validate controls (NATO Cyber Defence Pledge 2016).

#### 5.9 Data Protection and Privacy

- **GDPR Compliance:**  
  Processing of personal data for civilians/contractors within EU jurisdiction must comply with GDPR and Romanian Cybersecurity Law, within SOFA limitations (GDPR Art. 32; Romanian Law 58/2019).
- **Data Minimization:**  
  Only essential personal data collected and retained, subject to access controls and audit (GDPR Art. 5).

---

### 6. EXCEPTIONS

Exception requests must be submitted to the ISSM in writing, with mission justification and risk assessment. Exceptions to NATO or national security regulations require approval from the relevant authority (NATO: AC/322-D(2017)0009, 2.4). All exceptions must be documented and regularly reviewed.

---

### 7. MONITORING AND REVIEW

- **Continuous Monitoring:**  
  The SOC continuously monitors for threats and policy violations (NATO: AC/322-D(2017)0009, 8.1.3; NIST CSF DE.CM-1).
- **Annual Review:**  
  This policy is reviewed annually or upon significant changes in mission, threat, or regulatory requirements (ISO/IEC 27001:2022, A.5.1).
- **Audit:**  
  Compliance is subject to periodic internal and external audit, including by NATO, contributing nation, and host-nation authorities as appropriate (NATO: AC/322-D(2017)0009, 3.4).

---

### 8. REFERENCES

- NATO Information Security Policy (C-M(2002)49 and successor)
- NATO Security Regulations (AC/35-D/1015; AC/35-D/1029)
- NATO INFOSEC Technical and Implementation Directive (AC/322-D(2017)0009)
- NATO Cyber Defence Pledge 2016
- Allied Joint Doctrine for Cyberspace Operations (AJP-3.20)
- Romanian Cybersecurity Law (Law 58/2019, NIS)
- GDPR (EU Regulation 2016/679)
- NIST Cybersecurity Framework (CSF) 2.0
- ISO/IEC 27001:2022; ISO/IEC 27002:2022

---

**End of Policy Document**
