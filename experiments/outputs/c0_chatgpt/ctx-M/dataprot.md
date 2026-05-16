---
config: C0
context_id: ctx-M
policy_id: P2
policy_name: Data Protection Policy
policy_short: dataprot
metadata:
  config: C0
  model: gpt-4.1-2025-04-14
  input_tokens: 1366
  output_tokens: 2715
  total_tokens: 4081
  latency_s: 50.512
  tool_calls: []
  raw_provider_id: chatcmpl-DcZbzBRV0K5n8LByLfY788sONwYDh
sources_count: 0
sources: []
prompt_chars: 6041
answer_chars: 10547
generated_at_unix: 1778085777
---

---

# DATA PROTECTION POLICY

**Organisation:** [REDACTED] Multinational NATO Military Detachment, Romania  
**Effective Date:** 2024-07-01  
**Policy Owner:** Information Systems Security Manager (ISSM), J6  
**Review Cycle:** Annually, or upon significant regulatory/mission change  
**Classification:** NATO RESTRICTED when complete  

---

## 1. PURPOSE

This Data Protection Policy establishes mandatory principles and requirements for the protection of all data processed, stored, or transmitted by the [REDACTED] Multinational NATO Military Detachment (hereafter “the Detachment”). It ensures compliance with NATO, host-nation (Romanian/EU), coalition, and contributing nation regulations; enforces mission assurance; and mitigates adversarial threats to confidentiality, integrity, and availability of information assets, including personal data and classified material.

---

## 2. SCOPE

This policy applies to all personnel (military, civilian NATO staff, cleared contractors), network domains (NU, NR, NS, MISSION SECRET), all information classifications, and all Detachment-controlled information systems and data processing activities, inclusive of cross-domain and multinational information exchange, within the Detachment’s area of responsibility.

---

## 3. ROLES AND RESPONSIBILITIES

| Role | Responsibilities |
|------|------------------|
| **ISSM (Policy Owner)** | Policy maintenance, compliance oversight, incident reporting, audit coordination [NATO AC/322-D(2017)0009, NIST CSF ID.GV-1] |
| **Commander (CO)** | Overall accountability for data protection and policy enforcement [NATO C-M(2002)49, AJP-3.20] |
| **Security Staff (J6 Security/25 FTE)** | Implementation of technical and organisational controls, monitoring, and operational response [ISO/IEC 27001:2022 A.5.1, NIST CSF PR.PT-1] |
| **COMSEC Custodians** | Compliance with key management, chain of custody, and dual-key controls [AC/322-D(2017)0009, NATO COMSEC Policy] |
| **All Personnel** | Compliance with this Policy; reporting of data protection incidents or suspected breaches [NATO AC/35-D/1015, ISO/IEC 27001:2022 A.6.1.1] |
| **Host-Nation Liaison Officer** | Interface with host-nation authorities for GDPR/NIS compliance, notification, and cross-jurisdictional issues [GDPR Art. 27, Romanian Law 58/2019] |

---

## 4. PRINCIPLES

1. **Lawfulness, Fairness, and Transparency**  
   All data processing must be lawful, fair, and transparent to data subjects, consistent with NATO security policy, GDPR (for personal data), and national security exemptions [GDPR Art. 5; NATO C-M(2002)49].

2. **Purpose Limitation**  
   Data is collected and processed only for legitimate, explicitly stated NATO/Detachment purposes [GDPR Art. 5(1)(b); NATO C-M(2002)49].

3. **Data Minimisation**  
   Only data strictly required for mission, operational, or administrative purposes shall be processed [GDPR Art. 5(1)(c); ISO/IEC 27001:2022 A.8.1].

4. **Accuracy**  
   Data must be accurate and, where necessary, kept up to date. Inaccurate data must be rectified without delay [GDPR Art. 5(1)(d)].

5. **Storage Limitation**  
   Data shall be retained only as long as necessary for the purpose for which it was collected, subject to NATO and national retention schedules [GDPR Art. 5(1)(e); NATO C-M(2002)49].

6. **Integrity and Confidentiality**  
   Appropriate technical and organisational measures shall protect data from unauthorised access, alteration, loss, or disclosure [ISO/IEC 27001:2022 A.9, A.10; NIST CSF PR.DS-1 to PR.DS-5].

7. **Accountability**  
   Compliance with this Policy and all applicable frameworks must be demonstrable through audit trails, documentation, and review [GDPR Art. 5(2); ISO/IEC 27001:2022 A.5.1].

8. **Need-to-Know and Originator Control (ORCON)**  
   Access to classified or sensitive data is limited by clearance, mission role, and explicit need-to-know; originator retains control over further dissemination [NATO C-M(2002)49, AC/35-D/1015].

---

## 5. DATA PROTECTION REQUIREMENTS AND CONTROLS

### 5.1. Data Classification and Handling

- **All data** shall be classified per NATO and mission-specific regimes: NU, NR, NS, MISSION SECRET [NATO C-M(2002)49; AC/322-D(2017)0009].
- **Classified data** must be processed and stored only on accredited systems within the appropriate classification domain [ISO/IEC 27001:2022 A.5.12].
- **Spillage prevention:** Cross-domain data transfer is permitted only via accredited NATO Cross-Domain Solutions (CDS), with logging and dual authorisation [NATO AC/322-D(2017)0009, NIST CSF PR.DS-5].
- **ORCON:** All data with originator control markings must not be further disseminated without originator’s written consent [NATO C-M(2002)49].

### 5.2. Access Control

- **Access to data** is strictly role-based, enforced by least privilege and need-to-know, mapped to validated clearance and mission requirement [ISO/IEC 27001:2022 A.9.1.2; NATO AC/35-D/1015].
- **Authentication:** All users authenticate using NATO PKI smart cards (CAC-equivalent); passwords alone are prohibited on classified systems [NIST CSF PR.AC-1, ISO/IEC 27001:2022 A.9.4.2].
- **No cross-domain identity federation** is permitted; identities are managed per domain [Unsupported; based on operational constraint].

### 5.3. Protection of Personal Data (GDPR/Host-Nation Law)

- **Personal data** of civilian NATO staff and contractors is processed in accordance with GDPR and Romanian Law 58/2019, with data subjects’ rights respected where not incompatible with NATO security [GDPR Art. 6, 9, 13–15].
- **Data transfers** to non-EU/EEA nations or entities must be justified under NATO SOFA, with safeguards applied [GDPR Ch. V].
- **Data subject requests** (access, rectification, erasure, restriction) are managed via the Host-Nation Liaison Officer, subject to operational security limitations [GDPR Art. 12–18].

### 5.4. Data Security Measures

- **Encryption:** All classified and sensitive data at rest and in transit are protected with NATO-approved cryptography; high-grade keying material is managed with two-person integrity and auditable chain of custody [NATO COMSEC Policy; NIST CSF PR.DS-2].
- **Physical Controls:** SCIFs are used for NS and above; access is controlled and logged [ISO/IEC 27001:2022 A.11; NATO AC/35-D/1015].
- **TEMPEST Zoning:** All processing of NS and higher is within TEMPEST-validated zones [NATO AC/322-D(2017)0009].
- **Media Handling:** Removable media use is restricted to mission-justified cases, subject to logging, scanning, and authorisation [ISO/IEC 27001:2022 A.8.3; NATO C-M(2002)49].

### 5.5. Audit and Accountability

- **Logging:** All access to classified and sensitive data is logged, with regular review by security staff; logs are retained per NATO and national retention schedules [ISO/IEC 27001:2022 A.12.4; NIST CSF DE.AE-3].
- **Audit Trails:** All COMSEC material and cross-domain transfers are logged with dual-key/signature where required [NATO COMSEC Policy].
- **Separation of Duties:** No individual may approve, execute, and audit the same data transfer or COMSEC operation [ISO/IEC 27001:2022 A.6.1.2].

### 5.6. Data Retention and Disposal

- **Retention:** Data is retained only as long as mission, legal, or regulatory requirements demand, per NATO and national data retention schedules [GDPR Art. 5(1)(e); ISO/IEC 27001:2022 A.8.3.3].
- **Secure Disposal:** Data and media are destroyed using NATO-standard processes appropriate to their classification; disposal is logged and, for NS and above, requires dual-person verification [NATO C-M(2002)49; ISO/IEC 27001:2022 A.8.3.2].

### 5.7. Supply Chain and Third-Party Controls

- **Equipment and vendors** must be selected from NATO-approved lists; all contractors are subject to security screening [NATO AC/322-D(2017)0009, AC/35-D/1029].
- **Supply-chain risk** (including COMSEC/CIS) is assessed, with controls in place for acceptance and ongoing monitoring [NIST CSF ID.SC-1 to ID.SC-5].

### 5.8. Data Breach and Incident Response

- **Incidents** (including data breaches, suspected loss or compromise) are handled per the Detachment’s IR plan, aligned with NATO NCIRC and host-nation CERT notification requirements [NATO C-M(2002)49; ISO/IEC 27001:2022 A.16.1.1; GDPR Art. 33].
- **Notification**: Breaches affecting personal data are notified to host-nation authorities (as required by GDPR) and coalition partners, considering SOFA and operational security [GDPR Art. 33; Romanian Law 58/2019].

### 5.9. Training and Awareness

- **All staff** must complete at least 40 hours/year of information security and data protection training, including GDPR awareness for those handling personal data [ISO/IEC 27001:2022 A.6.3].
- **Exercises:** Data protection procedures are validated in at least six exercises per year and two red-team engagements [Unsupported; based on operational practice].

---

## 6. EXCEPTIONS

Any exception to this Policy must be formally documented, risk-assessed, and approved by the ISSM and Commander, with notification to the NATO chain as appropriate [ISO/IEC 27001:2022 A.5.1.2]. Exceptions pertaining to classified data or national caveats may require higher authority or originator consent.

---

## 7. MONITORING AND REVIEW

- **Continuous Monitoring:** The Security Operations Centre (SOC) monitors all domain boundaries and critical systems 24/7 [NIST CSF DE.CM-1].
- **Audits:** Internal and external audits are conducted at least annually, and after any significant incident or regulatory change [ISO/IEC 27001:2022 A.12.7].
- **Policy Review:** The ISSM leads annual policy reviews, or more frequently as needed; all updates are approved by the Commander [ISO/IEC 27001:2022 A.5.1.1].
- **Metrics and Reporting:** Compliance metrics are reported quarterly to NATO chain of command and host-nation authorities as applicable [NATO C-M(2002)49].

---

## 8. REFERENCES

- **NATO C-M(2002)49** (NATO Security Policy and successors)
- **NATO AC/35-D/1015** (Security within NATO)
- **NATO AC/35-D/1029** (Personnel Security)
- **NATO AC/322-D(2017)0009** (INFOSEC Technical Directive)
- **NATO Cyber Defence Pledge (2016)**
- **Allied Joint Doctrine for Cyberspace Operations (AJP-3.20)**
- **Romanian Law 58/2019** (transposing NIS Directive, as amended)
- **GDPR (Regulation (EU) 2016/679)**
- **NIST Cybersecurity Framework (CSF) v2.0**
- **ISO/IEC 27001:2022** and **ISO/IEC 27002:2022**
- **NATO SOFA (Agreement between the Parties to the North Atlantic Treaty regarding the Status of their Forces)**

---

**End of Policy**
