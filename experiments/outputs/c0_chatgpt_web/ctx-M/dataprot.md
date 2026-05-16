---
config: C0+web
context_id: ctx-M
policy_id: P2
policy_name: Data Protection Policy
policy_short: dataprot
metadata:
  config: C0+web
  model: gpt-4.1-2025-04-14
  input_tokens: 1660
  output_tokens: 2383
  total_tokens: 4043
  latency_s: 23.343
  tool_calls: []
  raw_provider_id: resp_0ecf27a6ff24d0b90069fb70cb5d4c8192be817780e39682a7
sources_count: 0
sources: []
prompt_chars: 6041
answer_chars: 8591
generated_at_unix: 1778086114
---

---

# DATA PROTECTION POLICY

**Organisation:** NATO Multinational Military Detachment (Romania, under SHAPE operational control)  
**Effective Date:** 2024-07-01  
**Policy Owner:** Information Systems Security Manager (ISSM), J6  
**Review Cycle:** Annual (or upon regulatory/mission change)  
**Classification:** NATO UNCLASSIFIED (NU)  
**Language:** English

---

## 1. Purpose

This Data Protection Policy establishes mandatory principles and requirements for the secure handling, processing, and protection of all data—classified and unclassified—across the NATO Multinational Military Detachment in Romania. The policy aligns with NATO, host-nation, and coalition frameworks, as well as international standards (NIST CSF 2.0, ISO/IEC 27001:2022, GDPR where applicable), to ensure confidentiality, integrity, availability, and lawful processing of information.

---

## 2. Scope

This policy applies to:
- All personnel (military, NATO civilian, contractors) and third parties with access to detachment data and systems.
- All information assets (physical and digital), including but not limited to: NU, NR, NS, and MISSION SECRET domains, communications, and personal data falling under GDPR.
- All processing activities conducted at or on behalf of the detachment, regardless of location or medium.

---

## 3. Roles and Responsibilities

**Information Systems Security Manager (ISSM, J6)**
- Policy owner and authority for implementation, compliance monitoring, and exception approval.
- Alignment with NATO and national security directives.  
  *[Ref: AC/322-D(2017)0009, ISO/IEC 27001:2022 cl. 5.3]*

**Security Staff (FTE)**
- 24/7 operational security monitoring, incident response, and audit activities.  
  *[Ref: NATO CIRC, NIST CSF PR.IP-1, DE.CM-1]*

**Data Owners**
- Classification, handling, and originator control (ORCON) of data assets.  
  *[Ref: NATO C-M(2002)49, AC/35-D/1015]*

**All Users**
- Compliance with classification, handling, and reporting requirements.  
  *[Ref: ISO/IEC 27001:2022 cl. 5.1, 5.2, 9.1]*

**Host-Nation Liaison/Legal Advisor**
- Oversight of GDPR and host-nation legal compliance for civilian/contractor data.  
  *[Ref: GDPR Art. 39, Romanian CSL Art. 4]*

---

## 4. Data Protection Principles

All data must be processed in accordance with the following principles:

1. **Lawfulness, Fairness, and Transparency**  
   All processing of personal data must be lawful, fair, and transparent to the data subject.  
   *[GDPR Art. 5(1)(a)]*

2. **Purpose Limitation**  
   Data must only be collected for specified, explicit, and legitimate purposes aligned with NATO and operational requirements.  
   *[GDPR Art. 5(1)(b), NATO C-M(2002)49]*

3. **Data Minimization**  
   Only the minimum data necessary for mission, operational, and legal requirements shall be processed.  
   *[GDPR Art. 5(1)(c), ISO/IEC 27001:2022 cl. 8.1]*

4. **Accuracy**  
   Data must be accurate and, where necessary, kept up to date.  
   *[GDPR Art. 5(1)(d)]*

5. **Storage Limitation**  
   Data must not be retained longer than necessary.  
   *[GDPR Art. 5(1)(e), ISO/IEC 27001:2022 cl. 7.5]*

6. **Integrity, Confidentiality, and Availability**  
   Data must be protected against unauthorized access, disclosure, alteration, or destruction, and available as required for mission.  
   *[NIST CSF PR.AC-1, ISO/IEC 27001:2022 Annex A.8, NATO C-M(2002)49]*

7. **Need-to-Know and Originator Control (ORCON)**  
   Access to classified material is strictly on a need-to-know basis and subject to ORCON rules.  
   *[NATO C-M(2002)49, AC/35-D/1015]*

8. **Default-Deny Access**  
   Access to systems and data is denied by default unless explicitly authorized.  
   *[NIST CSF PR.AC-4, ISO/IEC 27001:2022 Annex A.9.1.2]*

---

## 5. Data Protection Requirements and Controls

### 5.1 Classification and Handling

- All data must be classified and marked in accordance with NATO and coalition classification regimes: NU, NR, NS, and MISSION SECRET.  
  *[NATO C-M(2002)49, AC/35-D/1015, ISO/IEC 27001:2022 Annex A.5.12]*

- Strict separation of classification domains must be enforced (physical, logical, and procedural controls).  
  *[NATO C-M(2002)49, NIST CSF PR.AC-5]*

### 5.2 Access Control

- Access to all systems and data requires valid clearance, role-based access, and need-to-know validation.  
  *[ISO/IEC 27001:2022 Annex A.9.2.1, NIST CSF PR.AC-1, -4]*

- PKI smart-card authentication (no cross-domain federation) is mandatory for all user logons.  
  *[ISO/IEC 27001:2022 Annex A.9.4.2]*

- Dual-key procedures apply for high-grade COMSEC and release of certain operational orders.  
  *[NATO COMSEC Policy, AC/322-D(2017)0009]*

### 5.3 Data Transfer and Spillage Prevention

- Cross-domain data transfer must use only accredited NATO CDS solutions.  
  *[NATO C-M(2002)49, AC/322-D(2017)0009]*

- Data spillage incidents (accidental or adversarial) must be reported and managed per incident response procedures.  
  *[NIST CSF RS.CO-2, NATO CIRC SOPs]*

### 5.4 Data at Rest and in Transit

- All classified data at rest must be encrypted using NATO-approved cryptographic mechanisms.  
  *[ISO/IEC 27001:2022 Annex A.10.1, NIST CSF PR.DS-1]*

- All sensitive or classified data in transit must use end-to-end encryption (COMSEC or equivalent).  
  *[NATO COMSEC Policy, AC/322-D(2017)0009]*

### 5.5 Physical and Environmental Security

- NS and above domains must be processed only in accredited SCIF rooms, protected by TEMPEST zoning.  
  *[NATO C-M(2002)49, ISO/IEC 27001:2022 Annex A.11]*

- Access to physical facilities is restricted and logged; two-person integrity for high-grade keying material.  
  *[NATO COMSEC Policy, ISO/IEC 27001:2022 Annex A.11.1.1]*

### 5.6 Supply Chain Security

- All equipment and software must be sourced from vetted vendors and appear on NATO-approved lists; host-nation contractors require security screening.  
  *[NIST CSF ID.SC-1, ISO/IEC 27001:2022 Annex A.15.1.1]*

### 5.7 Personal Data Processing (GDPR/Host-Nation Law)

- Personal data (civilian/contractor) must be processed in accordance with GDPR and Romanian cybersecurity law, including lawful basis, transparency, and subject rights.  
  *[GDPR Art. 6, 12–23, Romanian CSL Art. 4]*

- Data transfers outside the EU are subject to adequacy and safeguards as defined by GDPR.  
  *[GDPR Ch. V]*

- Data Protection Impact Assessments (DPIA) must be conducted for high-risk processing activities involving personal data.  
  *[GDPR Art. 35]*

### 5.8 Monitoring, Logging, and Incident Response

- All access to classified networks and data must be logged and monitored by the theatre 24/7 SOC; logs must be retained per NATO and host-nation requirements.  
  *[ISO/IEC 27001:2022 Annex A.12.4, NIST CSF DE.CM-1]*

- Incident response is governed by the NCIRC-aligned plan, with mandatory reporting to NCSC and host-nation CERT as required.  
  *[NATO CIRC SOPs, ISO/IEC 27001:2022 cl. 6.1.3, 16.1]*

### 5.9 Training and Awareness

- All personnel must complete a minimum of 40 hours cybersecurity/data protection training per year, including scenario-based exercises.  
  *[ISO/IEC 27001:2022 cl. 7.2, NATO Cyber Defence Pledge 2016]*

---

## 6. Exceptions

Exceptions to this policy may only be granted by the ISSM (J6), in consultation with the NATO Security Authority and the Host-Nation Legal Advisor, and must be documented with a clear risk assessment and compensating controls.  
*[ISO/IEC 27001:2022 cl. 10.1]*

---

## 7. Monitoring and Review

- Compliance is monitored continuously by the security team (25 FTE) and audited annually, or upon significant change to regulatory, operational, or threat environment.
- Policy effectiveness is reviewed annually by the ISSM, with findings reported to NATO SHAPE and host-nation authorities as required.
- Non-compliance or data breaches are subject to disciplinary action under NATO and host-nation law.

---

## 8. References

1. **NATO Information Security Policy** (C-M(2002)49, latest revision)
2. **AC/35-D/1015** (Security within NATO)
3. **AC/35-D/1029** (Personnel Security)
4. **AC/322-D(2017)0009** (NATO INFOSEC Technical/Implementation Directive)
5. **NATO Cyber Defence Pledge** (2016)
6. **AJP-3.20** (Allied Joint Doctrine for Cyberspace Operations)
7. **Romanian Cybersecurity Law** (Law 58/2019, NIS, NIS2 transposition)
8. **GDPR** (General Data Protection Regulation, EU 2016/679)
9. **NIST Cybersecurity Framework 2.0**
10. **ISO/IEC 27001:2022** and **27002:2022**
11. **NATO SOFA** (Status of Forces Agreement)
12. **NATO CIRC SOPs**

---

**End of Policy**
