---
config: C0
context_id: ctx-H
policy_id: P3
policy_name: Data Protection Policy
policy_short: dataprot
metadata:
  config: C0
  model: gpt-4.1-2025-04-14
  input_tokens: 892
  output_tokens: 2809
  total_tokens: 3701
  latency_s: 57.93
  tool_calls: []
  raw_provider_id: chatcmpl-DcZ8OqnZaQWcboajbXMjhsRqRP0g2
sources_count: 0
sources: []
prompt_chars: 4103
answer_chars: 10658
generated_at_unix: 1778083949
---

---

**[ORGANISATION NAME]: Data Protection Policy**

**Effective date:** 2024-07-01  
**Owner:** Director of ICT & Data Protection Officer (DPO)  
**Review cycle:** Annual (or upon significant regulatory/operational changes)  
**Applicability:** All staff, contractors, and third parties accessing or processing organisational data

---

### 1. Purpose

This policy establishes the principles and minimum requirements for the protection of personal data, including special categories such as health data, processed by [Organisation Name], a public hospital operating under the Servizio Sanitario Nazionale (SSN) and the regional Azienda Sanitaria Locale (ASL). The policy aims to ensure compliance with all applicable laws and regulations, including the **General Data Protection Regulation (GDPR) (Regulation EU 2016/679)**, **D.Lgs. 196/2003 as amended by D.Lgs. 101/2018**, **NIS2 Directive (EU 2022/2555)**, **AGID Linee Guida per la sicurezza informatica nella PA**, **Provvedimenti Garante Privacy in sanità**, **Misure minime AGID per la PA**, and regional regulations on the **Fascicolo Sanitario Elettronico (FSE)**. The policy also draws on best practices from **NIST Cybersecurity Framework (CSF) 2.0** and **ISO/IEC 27001:2022**.

---

### 2. Scope

This policy applies to:

- All personal data processed by the organisation, including health data, minors' data, and employee data;
- All employees (clinical, administrative, technical), contractors, and third parties (e.g., Managed Service Providers, vendors) with access to such data;
- All information systems and devices used to process personal data, including but not limited to EHR (FSE), PACS/RIS, LIS, ADT, Pharmacy systems, workstations, and mobile devices;
- All processing activities, whether digital or paper-based, performed in the execution of the organisation’s mission.

---

### 3. Roles and Responsibilities

| Role                  | Responsibilities                                                                                             |
|-----------------------|-------------------------------------------------------------------------------------------------------------|
| **Data Controller**   | The legal entity (hospital) responsible for determining the means and purposes of data processing [GDPR Art. 4(7)]. |
| **Data Protection Officer (DPO)** | Monitors compliance, advises on data protection obligations, acts as point of contact for data subjects and authorities [GDPR Art. 39]. |
| **Director of ICT**   | Ensures technical and organisational measures are implemented, manages IT operations, and reports incidents. |
| **System Administrators / MSP** | Implement and maintain technical controls, manage user access, support incident response [ISO 27001:2022 A.7.2.2]. |
| **Staff (All)**       | Process personal data only as required for their duties, follow procedures, report incidents [GDPR Art. 32(4)]. |
| **Third Parties (incl. MSP, vendors)** | Process data only as per contract, follow organisation’s security requirements [GDPR Art. 28, AGID Linee Guida]. |

---

### 4. Principles

Data processing at [Organisation Name] shall be governed by the following principles ([GDPR Art. 5]; ISO 27001:2022 A.8.1.1):

1. **Lawfulness, Fairness, and Transparency:** Data processed lawfully, fairly, and in a transparent manner.
2. **Purpose Limitation:** Data collected for explicit, legitimate purposes and not further processed incompatibly.
3. **Data Minimisation:** Only data necessary for the intended purpose are processed.
4. **Accuracy:** Data is kept accurate and up to date.
5. **Storage Limitation:** Data kept in a form which permits identification no longer than necessary.
6. **Integrity and Confidentiality:** Data processed securely to ensure protection against unauthorised or unlawful processing and against accidental loss, destruction, or damage.
7. **Accountability:** The organisation is responsible for, and can demonstrate, compliance with these principles.

---

### 5. Requirements / Controls

**5.1. Lawful Processing & Information to Data Subjects**  
- All processing of personal data must have a valid legal basis (e.g., provision of healthcare under law) [GDPR Arts. 6, 9].  
- Data subjects (patients, staff) must be informed of processing via concise privacy notices [GDPR Art. 13–14; Provvedimenti Garante Privacy in sanità].  
**Reference:** GDPR Art. 6, 9, 13, 14; D.Lgs. 196/2003; Provv. Garante Privacy (2015, 2018)

**5.2. Data Subject Rights**  
- Procedures must be in place to permit the exercise of rights (access, rectification, erasure, restriction, objection, data portability) within legal timeframes [GDPR Art. 12–23].  
**Reference:** GDPR Art. 12–23

**5.3. Data Minimisation & Access Control**  
- Access to personal data is restricted to staff whose duties require it, using least privilege and role-based access wherever technically feasible [ISO 27001:2022 A.8.2.2; NIST CSF PR.AC-4].
- Regular reviews of user access (minimum annually) for critical systems (EHR, PACS, ADT) [AGID Linee Guida; Misure minime AGID].
- Multi-factor authentication is required for remote access and privileged accounts, as supported by existing systems [AGID Linee Guida; NIS2 Art. 21].
**References:** ISO 27001:2022 A.8.2.2, A.5.18; NIST CSF PR.AC-1,-4; AGID Linee Guida; NIS2

**5.4. Data Security – Technical and Organisational Measures**  
- Antivirus/anti-malware protection must be installed and regularly updated on all endpoints [Misure minime AGID 5.2.1].
- Security patches must be applied in a timely manner following vendor/AGID guidelines, with documented exceptions for legacy systems (which must be isolated and monitored) [AGID Misure minime 6.2; NIST CSF PR.IP-12].
- Encryption is mandatory for all mobile devices that store or process personal data [Misure minime AGID 5.3.2; NIST CSF PR.DS-1].
- Physical security controls (e.g., locked storage, device tethering) for endpoints in public or patient-accessible areas [ISO 27001:2022 A.7.1.2; AGID Misure minime].
- Data must not be stored unencrypted on removable media unless justified and logged [AGID Misure minime 5.3.2].
**References:** Misure minime AGID; ISO 27001:2022 A.8.12, A.8.13; NIST CSF PR.DS-1,-2

**5.5. Supply Chain Security**  
- Third parties (MSP, vendors) with access to personal data must be engaged via contracts that include data protection clauses [GDPR Art. 28; NIS2 Art. 21(2); AGID Linee Guida].
- Access and activities of external parties must be logged and monitored [NIST CSF PR.PT-3].
**References:** GDPR Art. 28; NIS2 Art. 21; AGID Linee Guida

**5.6. Data Breach Management**  
- All staff must promptly report suspected or actual personal data breaches to the DPO and ICT Director [GDPR Art. 33].
- The DPO must assess, document, and, where required, notify the Garante and affected subjects within legal timeframes [GDPR Art. 33–34; Provvedimenti Garante].
- Incident response plans must be maintained and tested at least annually, with roles defined (including MSP involvement) [NIST CSF RS; AGID Linee Guida].
**References:** GDPR Art. 33–34; NIST CSF RS; AGID Linee Guida

**5.7. Data Retention and Disposal**  
- Personal data must be retained only as long as required by law or operational necessity, according to the hospital’s data retention schedule [GDPR Art. 5(1)(e); AGID Linee Guida].
- Secure deletion or physical destruction must be ensured for data at end-of-life [ISO 27001:2022 A.8.10; NIST CSF PR.DS-3].
**References:** GDPR Art. 5(1)(e); ISO 27001:2022 A.8.10; NIST CSF PR.DS-3

**5.8. Training and Awareness**  
- All staff must complete at least **2 hours/year** of data protection and cybersecurity training, with records maintained [NIS2 Art. 21(2); AGID Linee Guida].
- Induction training is mandatory for new hires and those changing roles [ISO 27001:2022 A.6.3].
- Training includes simulated phishing exercises, focusing on common sector threats [NIS2 Recital 88].
**References:** NIS2 Art. 21, Recital 88; AGID Linee Guida; ISO 27001:2022 A.6.3

**5.9. Special Category and Minors’ Data**  
- Processing of health data and minors’ data is subject to heightened protection, including minimisation of access, logging of access, and explicit consent procedures where required [GDPR Art. 9, 8; Provvedimenti Garante 2015, 2018].
- Access to minors’ data is limited to authorised personnel and parents/guardians as per law [GDPR Art. 8; Provv. Garante Privacy].
**References:** GDPR Art. 8, 9; Provvedimenti Garante Privacy in sanità

**5.10. Business Continuity & Patient Safety**  
- Data protection controls must be implemented in a manner that does not impede emergency clinical workflows [NIS2 Art. 21(1); AGID Linee Guida].
- Business continuity plans must address data availability for critical clinical systems (EHR RTO 4h, ADT/PS RTO 1h), with regular backup and restoration testing [ISO 27001:2022 A.17.1; AGID Linee Guida].
**References:** ISO 27001:2022 A.17.1; AGID Linee Guida; NIS2 Art. 21

---

### 6. Exceptions

Requests for exceptions to this policy (e.g., legacy system constraints, clinical workflow impacts) must be submitted in writing to the Director of ICT and DPO, with justification and compensating controls proposed. Exceptions are granted only after documented risk assessment and, where required, notification to the Data Controller and Garante Privacy [GDPR Art. 32(1)(d); AGID Linee Guida].

---

### 7. Monitoring and Review

- Compliance with this policy will be monitored by the DPO and ICT Director via periodic audits, access reviews, and incident analysis [ISO 27001:2022 A.9.2.1; AGID Linee Guida].
- The policy will be reviewed at least annually, or upon significant changes in law, technology, or risk landscape, with updates approved by the Data Controller.
- Records of reviews, incidents, and exceptions will be maintained for audit purposes [GDPR Art. 30; ISO 27001:2022 A.7.5.3].

---

### 8. References

1. **GDPR (Regulation EU 2016/679)** – esp. Arts. 5, 6, 8, 9, 12–23, 28, 32–34  
2. **D.Lgs. 196/2003** as amended by **D.Lgs. 101/2018**  
3. **NIS2 Directive (EU 2022/2555)** – esp. Art. 21, Recital 88  
4. **Linee Guida AGID per la sicurezza informatica nella PA**  
5. **Misure minime AGID per la PA**  
6. **Provvedimenti Garante Privacy in sanità** (2015, 2018)  
7. **Regional FSE regulations**  
8. **ISO/IEC 27001:2022** – esp. A.5.18, A.6.3, A.7.1.2, A.7.2.2, A.8.1.1, A.8.2.2, A.8.10, A.8.12, A.8.13, A.17.1  
9. **NIST Cybersecurity Framework (CSF) 2.0** – esp. PR.AC, PR.DS, PR.IP, PR.PT, RS  
10. **Other applicable national and regional regulations**

---

**Document History:**  
- v1.0 – Initial issue (2024-07-01)

---
