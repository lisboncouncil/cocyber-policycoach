---
config: C0
context_id: ctx-M
policy_id: P3
policy_name: Data Protection Policy
policy_short: dataprot
metadata:
  config: C0
  model: gpt-4.1-2025-04-14
  input_tokens: 1015
  output_tokens: 2605
  total_tokens: 3620
  latency_s: 28.378
  tool_calls: []
  raw_provider_id: chatcmpl-DcZAyT6O8QI9UhF2ImGbIwSwKfnKK
sources_count: 0
sources: []
prompt_chars: 4951
answer_chars: 10182
generated_at_unix: 1778084080
---

---

**NATO ALLIED COMMAND OPERATIONS (ACO) — MULTINATIONAL MILITARY DETACHMENT, ROMANIA**

**DATA PROTECTION POLICY**

| Policy Title        | Data Protection Policy                           |
|---------------------|-------------------------------------------------|
| Organisation        | NATO ACO Multinational Military Detachment, Romania |
| Effective Date      | 1 July 2024                                     |
| Policy Owner        | Information Systems Security Manager (ISSM), J6  |
| Review Cycle        | Annual; or on significant organisational, legal, or threat change |
| Classification      | NATO UNCLASSIFIED (NU)                          |

---

## 1. PURPOSE

This policy establishes the principles and controls for the protection of data—including NATO classified information, mission data, and personal data—processed, stored, or transmitted by the NATO ACO Multinational Military Detachment in Romania. The policy ensures compliance with NATO regulations, relevant host-nation (Romanian/EU) law within SOFA limitations, and applicable international security best practices, supporting the detachment’s operational integrity, mission assurance, and legal obligations.

---

## 2. SCOPE

This policy applies to:
- All personnel (military, NATO civilian staff, and cleared contractors) assigned to or supporting the detachment.
- All information systems and network domains operated by the detachment (NU, NR, NS, MISSION SECRET).
- All forms of data (digital, paper, voice, COMSEC material) processed, stored, or transmitted within the detachment’s area of responsibility.
- All data processed on behalf of, or shared with, NATO, framework nation, or contributing nations, within applicable information sharing agreements.

---

## 3. ROLES AND RESPONSIBILITIES

- **Information Systems Security Manager (ISSM), J6:** Policy owner; oversees implementation, compliance, and review; reports to Detachment Commander and ACO J6.
- **Information Systems Security Officers (ISSOs):** Support implementation in assigned domains; conduct technical and administrative controls.
- **COMSEC Custodian:** Implements and audits controls for cryptographic material and COMSEC equipment, ensuring dual-key and two-person integrity as required.
- **Cyber Operations Team:** Operates, monitors, and defends network domains; escalates incidents per NCIRC and host-nation procedures.
- **Detachment Commander:** Accountable for overall compliance; ensures resources and command emphasis.
- **Data Owners and System Owners:** Ensure data is classified, handled, and protected according to originator control and need-to-know.
- **All Personnel:** Adhere to this policy and report suspected or actual breaches.

*References: NATO C-M(2002)49, AC/35-D/1015, AC/322-D(2017)0009; ISO/IEC 27001:2022 cl. 5.3, 5.7; NIST CSF 2.0 ID.GV-1, ID.GV-2.*

---

## 4. PRINCIPLES

1. **Defence-in-Depth:** Data is protected through layered, mutually reinforcing technical and administrative controls. *(NATO C-M(2002)49; NIST CSF PR.DS-1)*
2. **Separation of Domains:** Strict separation between classification domains is enforced; cross-domain flows are only permitted via accredited NATO Cross-Domain Solutions. *(AC/322-D(2017)0009 s.4; ISO 27001 cl. 8.1)*
3. **Need-to-Know & Originator Control:** Access to data is granted only as required for mission duties, with originator control enforced on shared information. *(NATO C-M(2002)49 s.12, AC/35-D/1015 s.6)*
4. **Compliance by Design:** All data processing complies with applicable NATO, host-nation, and EU legal and regulatory requirements, including GDPR for civilian/contractor data. *(GDPR Art. 5-6; Law 58/2019; NIST CSF ID.GV-3)*
5. **Accountability & Auditability:** Data handling is logged, monitored, and auditable; chain of custody is maintained for high-grade and COMSEC material. *(AC/35-D/1015 s.10; ISO 27001 cl. 9.1)*
6. **Minimum Data Principle:** Only the minimum necessary data is processed or retained for mission or legal purposes. *(GDPR Art. 5(1)(c); ISO 27001 cl. 5.7)*
7. **Personnel Vetting:** All personnel are security cleared and subject to ongoing vetting appropriate to their access level. *(AC/35-D/1029)*

---

## 5. REQUIREMENTS AND CONTROLS

### 5.1. **Data Classification and Labelling**
- All data is classified and labelled per NATO and detachment schema: NU, NR, NS, MISSION SECRET, COSMIC TOP SECRET (CTS), and marked for Need-to-Know and ORCON as required.
    - *Reference: AC/35-D/1015 s.5, s.6; ISO 27001 cl. 8.2; NIST CSF PR.DS-1.*

### 5.2. **Access Control**
- Access to data is strictly enforced via:
    - PKI-enabled smart-card authentication per domain (no cross-domain single sign-on).
    - Role-based access control (RBAC) mapped to Need-to-Know.
    - Physical access controls and two-person integrity for high-grade and COMSEC material.
    - Privileged access is logged and periodically reviewed by ISSM/ISSO.
    - *Reference: AC/322-D(2017)0009 s.4.2; ISO 27001 cl. 8.1, 8.2, 8.3; NIST CSF PR.AC-1, PR.AC-4.*

### 5.3. **Separation of Domains and Cross-Domain Data Flows**
- Data transfer between classification domains is only permitted through accredited NATO Cross-Domain Solutions; all flows are logged, monitored, and subject to approval.
- No manual or unmediated data movement (“air gap crossing”) is permitted without explicit written authorisation and audit trail.
    - *Reference: AC/322-D(2017)0009 s.4.3; NATO C-M(2002)49 s.12; ISO 27001 cl. 8.1.*

### 5.4. **Data Handling and Storage**
- Data is stored only on NATO-approved, accredited hardware.
- Portable media use is minimised and strictly controlled; all portable media must be encrypted to NATO standards and tracked.
- Retention of data is minimised and data is securely destroyed when no longer required.
    - *Reference: AC/322-D(2017)0009 s.6.1-6.4; ISO 27001 cl. 8.3, 8.10; NIST CSF PR.DS-3, PR.DS-6.*

### 5.5. **Data Transmission and Encryption**
- All classified or sensitive data is encrypted in transit and at rest using NATO-approved cryptographic standards.
- Transmission of data outside NATO networks requires explicit ISSM approval and must be logged.
    - *Reference: NATO C-M(2002)49 s.17; AC/322-D(2017)0009 s.5; NIST CSF PR.DS-2, PR.DS-5.*

### 5.6. **COMSEC Material and Key Management**
- All COMSEC material is managed under NATO-approved processes, with dual-key/two-person integrity for high-grade material.
- Chain of custody for COMSEC is auditable and reviewed quarterly.
    - *Reference: AC/322-D(2017)0009 s.7; ISO 27001 cl. 8.3; NATO COMSEC Policy.*

### 5.7. **Supply Chain Data Protection**
- Only vetted vendors and NATO-approved equipment lists may be used.
- All host-nation contractors must pass security screening per AC/35-D/1029.
    - *Reference: AC/322-D(2017)0009 s.8; ISO 27001 cl. 15.1; NIST CSF ID.SC-1.*

### 5.8. **Personal Data Protection (GDPR & Host-Nation Law)**
- Processing of personal data (for NATO civilians and contractors) is in accordance with GDPR and Romanian Law 58/2019, within SOFA limitations.
    - Lawful basis for processing must be documented.
    - Data subjects are informed of their rights.
    - Data subject access requests are handled per procedure unless restricted by operational or security necessity.
    - Data breaches involving personal data are reported to the ISSM and, where required, to NCSC/NCIRC and host-nation CERT within statutory deadlines.
    - *Reference: GDPR Art. 5-34; Law 58/2019; ISO 27001 cl. 5.7, 8.9.*

### 5.9. **Incident Detection and Response**
- Continuous monitoring by the theatre-level SOC.
- All data protection incidents (including spillage, unauthorised access, or breach) are managed per NCIRC processes, with escalation to NCSC and host-nation CERT as required.
- Incidents are documented and reviewed for lessons learned.
    - *Reference: AC/322-D(2017)0009 s.9; NIST CSF DE.CM-1, RS.RP-1; ISO 27001 cl. 6.1.*

### 5.10. **Training and Awareness**
- All personnel must complete a minimum of 40 hours of cybersecurity and data protection training annually, including refresher modules on classification, handling, and GDPR basics.
    - *Reference: AC/322-D(2017)0009 s.10; ISO 27001 cl. 7.2; NIST CSF PR.AT-1.*

### 5.11. **Audit and Accountability**
- Access to data, domain separation controls, and COMSEC handling are subject to quarterly audit by ISSM or delegated authority.
- Non-compliance or deficiencies are documented, reported to the Detachment Commander, and remediated in a timely manner.
    - *Reference: AC/35-D/1015 s.10; ISO 27001 cl. 9.2; NIST CSF ID.GV-4.*

---

## 6. EXCEPTIONS

- Exceptions to this policy may only be granted by the ISSM, in writing, based on documented operational necessity and with appropriate risk mitigation. Permanent exceptions must be approved by the Detachment Commander and reported to ACO J6.
- All exceptions must be logged and subject to periodic review.

*Reference: ISO 27001 cl. 5.7.2.*

---

## 7. MONITORING AND REVIEW

- The ISSM will ensure continuous monitoring and annual review of this policy, incorporating developments in threat intelligence, changes in NATO/host-nation legal frameworks, and lessons learned from incidents or exercises.
- The policy is updated at least annually, or earlier if there is a significant change in mission, regulatory environment, or threat landscape.

*Reference: ISO 27001 cl. 10.1, 10.2; NIST CSF ID.GV-5.*

---

## 8. REFERENCES

**NATO:**
- NATO Information Security Policy (C-M(2002)49, latest version)
- AC/35-D/1015, Security within NATO
- AC/35-D/1029, Personnel Security
- AC/322-D(2017)0009, NATO INFOSEC Technical and Implementation Directive
- NATO Cyber Defence Pledge (2016)
- Allied Joint Doctrine for Cyberspace Operations (AJP-3.20)
- NATO COMSEC Policy

**Host-Nation (Romania/EU):**
- Romanian Cybersecurity Law 58/2019 (transposing NIS/NIS2)
- General Data Protection Regulation (GDPR) (EU) 2016/679
- NATO Status of Forces Agreement (SOFA)

**International Standards:**
- NIST Cybersecurity Framework (CSF) v2.0
- ISO/IEC 27001:2022, Information Security Management Systems
- ISO/IEC 27002:2022, Code of Practice for Information Security Controls

---

**End of Policy**
