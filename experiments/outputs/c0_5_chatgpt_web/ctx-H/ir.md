---
config: C0_5+web
context_id: ctx-H
policy_id: P4
policy_name: Incident Response Policy
policy_short: ir
metadata:
  config: C0_5+web
  model: gpt-5.5-2026-04-23
  input_tokens: 69881
  output_tokens: 12206
  total_tokens: 82087
  latency_s: 245.721
  tool_calls:
  - web_search_call
  - web_search_call
  - web_search_call
  - web_search_call
  - web_search_call
  - web_search_call
  - web_search_call
  - web_search_call
  - web_search_call
  - web_search_call
  - web_search_call
  raw_provider_id: resp_0061191480729ad80069fc81ddf8d8819686ec1707fb87d07e
sources_count: 18
sources:
- type: url_citation
  url: https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf
  title: The NIST Cybersecurity Framework (CSF) 2.0
  start_index: 2114
  end_index: 2191
- type: url_citation
  url: https://www.garanteprivacy.it/data-breach
  title: Data Breach - Violazioni di dati personali - Garante Privacy
  start_index: 4704
  end_index: 4768
- type: url_citation
  url: https://eur-lex.europa.eu/legal-content/EN-SV/TXT/?uri=CELEX%3A32022L2555&utm_source=openai
  title: Directive - 2022/2555 - BG - EUR-Lex
  start_index: 5293
  end_index: 5407
- type: url_citation
  url: https://csrc.nist.gov/pubs/sp/800/61/r3/final
  title: 'SP 800-61 Rev. 3, Incident Response Recommendations and Considerations for
    Cybersecurity Risk Management: A CSF 2.0 Community Profile | CSRC'
  start_index: 5654
  end_index: 5718
- type: url_citation
  url: https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf
  title: The NIST Cybersecurity Framework (CSF) 2.0
  start_index: 9092
  end_index: 9169
- type: url_citation
  url: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf
  title: 'Incident Response Recommendations and Considerations for Cybersecurity Risk
    Management: A CSF 2.0 Community Profile'
  start_index: 12443
  end_index: 12539
- type: url_citation
  url: https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf
  title: The NIST Cybersecurity Framework (CSF) 2.0
  start_index: 14394
  end_index: 14471
- type: url_citation
  url: https://eur-lex.europa.eu/legal-content/EN-SV/TXT/?uri=CELEX%3A32022L2555&utm_source=openai
  title: Directive - 2022/2555 - BG - EUR-Lex
  start_index: 18154
  end_index: 18268
- type: url_citation
  url: https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf
  title: The NIST Cybersecurity Framework (CSF) 2.0
  start_index: 22699
  end_index: 22776
- type: url_citation
  url: https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf
  title: The NIST Cybersecurity Framework (CSF) 2.0
  start_index: 24563
  end_index: 24640
- type: url_citation
  url: https://www.garanteprivacy.it/data-breach
  title: Data Breach - Violazioni di dati personali - Garante Privacy
  start_index: 27356
  end_index: 27420
- type: url_citation
  url: https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf
  title: The NIST Cybersecurity Framework (CSF) 2.0
  start_index: 29658
  end_index: 29735
- type: url_citation
  url: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf
  title: 'Incident Response Recommendations and Considerations for Cybersecurity Risk
    Management: A CSF 2.0 Community Profile'
  start_index: 31485
  end_index: 31581
- type: url_citation
  url: https://www.garanteprivacy.it/data-breach
  title: Data Breach - Violazioni di dati personali - Garante Privacy
  start_index: 39396
  end_index: 39460
- type: url_citation
  url: https://eur-lex.europa.eu/legal-content/EN-SV/TXT/?uri=CELEX%3A32022L2555&utm_source=openai
  title: Directive - 2022/2555 - BG - EUR-Lex
  start_index: 39688
  end_index: 39802
- type: url_citation
  url: https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf
  title: The NIST Cybersecurity Framework (CSF) 2.0
  start_index: 40069
  end_index: 40146
- type: url_citation
  url: https://csrc.nist.gov/pubs/sp/800/61/r3/final
  title: 'SP 800-61 Rev. 3, Incident Response Recommendations and Considerations for
    Cybersecurity Risk Management: A CSF 2.0 Community Profile | CSRC'
  start_index: 40295
  end_index: 40359
- type: url_citation
  url: https://www.agid.gov.it/it/sicurezza/misure-minime-sicurezza-ict?utm_source=openai
  title: Misure minime di sicurezza ICT per le pubbliche amministrazioni|Agenzia per
    l'Italia digitale
  start_index: 40818
  end_index: 40917
prompt_chars: 4675
answer_chars: 41042
generated_at_unix: 1778156243
---

# Incident Response Policy

## 1. Document Control

| Field | Value |
|---|---|
| **Organisation** | Province-level public general hospital, Italy — regional ASL / Servizio Sanitario Nazionale |
| **Policy title** | Incident Response Policy |
| **Effective date** | 7 May 2026 |
| **Policy owner** | Hospital Director, delegated operational ownership to the IT Service Responsible / Incident Response Coordinator |
| **Approver** | Hospital Director, in consultation with Medical Director, DPO, Administrative Director, and regional ASL ICT/security function |
| **Review cycle** | At least annually; also after any Severity 1 or Severity 2 incident, material regulatory change, major system change, or MSP contract renewal |
| **Version** | 1.0 |
| **Classification** | Internal use; controlled copy. Incident-specific records may be Restricted / Confidential depending on patient data, evidence, or legal sensitivity |

---

## 2. Purpose

This policy establishes how the hospital shall prepare for, detect, report, assess, contain, eradicate, recover from, and learn from cybersecurity incidents affecting clinical, administrative, technical, and outsourced ICT services.

The policy is tailored to a small 24/7 public hospital with limited internal IT capacity, outsourced managed services, sensitive health data, paediatric data, regional clinical platforms, legacy clinical kiosks, point-of-care mobile devices, and strict patient-safety continuity requirements. Incident response must prioritise patient safety, continuity of emergency and clinical care, legal notification duties, and preservation of evidence.

This policy aligns with the NIST Cybersecurity Framework 2.0 Respond and Recover functions, including Incident Management, Incident Analysis, Incident Response Reporting and Communication, Incident Mitigation, Incident Recovery Plan Execution, and Incident Recovery Communication. NIST CSF 2.0 defines these categories and outcomes for managing responses, conducting analysis, communicating with stakeholders, containing and eradicating incidents, and restoring affected assets and operations. ([nvlpubs.nist.gov](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf))

---

## 3. Scope

This policy applies to:

1. **People**: all clinical, administrative, technical/facility staff, temporary staff, trainees, contractors, consultants, volunteers, MSP personnel, and third-party support personnel with access to hospital systems or data.
2. **Systems and services**:
   - On-premises Active Directory, regional SPID/CIE federation integrations, VPN, UTM, endpoint protection, servers, NAS and tape backups.
   - Clinical systems including Cartella Clinica Elettronica / regional FSE access, PACS/RIS, LIS, ADT, pharmacy management, clinical kiosks, and point-of-care mobile devices.
   - Administrative systems, email, file shares, HR, procurement, finance, and document management systems.
   - Network infrastructure, clinical and administrative VLANs, PACS island, wireless, remote access, and any MSP-managed infrastructure.
3. **Data**:
   - Special-category health data.
   - Personal data of minors.
   - Employee personal data.
   - Operational, security, audit, and clinical workflow data.
4. **Incident types**:
   - Ransomware, malware, destructive attacks, unauthorised access, credential compromise, phishing, business email compromise, data leakage, loss or theft of devices, denial of service, supply-chain compromise, medical-device/vendor compromise, backup compromise, unauthorised clinical-record access, and significant ICT service disruption.

This policy applies during normal operations, downtime procedures, emergency clinical operations, maintenance windows, and outsourced support activity.

---

## 4. Regulatory and Framework Basis

The hospital operates in Italy as a public healthcare organisation and processes special-category health data. Incident response must therefore support compliance with GDPR, the Italian Privacy Code as amended, Garante Privacy requirements, NIS2 as transposed in Italy, AGID public-administration security measures, regional FSE rules, and the hospital’s ASL governance obligations.

For personal data breaches, the Italian Garante states that the controller must notify the Garante without undue delay and, where possible, within 72 hours after becoming aware of the breach unless the breach is unlikely to result in a risk to individuals’ rights and freedoms; late notifications must include reasons for delay. The Garante also states that high-risk breaches must be communicated to affected individuals unless mitigating conditions apply, and that all personal data breaches must be documented in a breach register. ([garanteprivacy.it](https://www.garanteprivacy.it/data-breach))

For NIS2, Directive (EU) 2022/2555 requires appropriate and proportionate technical, operational, and organisational cybersecurity risk-management measures, including incident handling, business continuity, backup management, disaster recovery, crisis management, and supply-chain security. NIS2 incident reporting includes early warning within 24 hours, incident notification within 72 hours, and a final report not later than one month after the incident notification, with progress reporting if the incident is ongoing. ([eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/EN-SV/TXT/?uri=CELEX%3A32022L2555&utm_source=openai))

NIST SP 800-61 Rev. 3 describes incident response as part of cybersecurity risk management and is intended to help organisations prepare for incident response, reduce incident impact, and improve detection, response, and recovery effectiveness. ([csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/61/r3/final)) ISO/IEC 27001:2022 Annex A controls used by this policy include A.5.24, A.5.25, A.5.26, A.5.27, A.5.28, A.5.29, A.5.30, A.5.19, A.5.20, A.5.22, A.8.15, and A.8.16.

---

## 5. Definitions

| Term | Definition |
|---|---|
| **Event** | An observable occurrence in an information system, clinical system, network, device, physical environment, or process. |
| **Cybersecurity incident** | An event or set of events that has compromised or may compromise confidentiality, integrity, availability, authenticity, accountability, or resilience of hospital systems, services, or data. |
| **Personal data breach** | A breach of security leading to accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to personal data. |
| **Significant incident** | An incident that may cause serious operational disruption, affect clinical-service delivery, cause data compromise, involve a critical supplier/MSP, or meet NIS2 / national notification criteria. |
| **Incident Response Coordinator** | The designated internal person coordinating incident handling. In this hospital, this role is assigned to the IT Service Responsible unless formally delegated. |
| **MSP** | The contracted managed service provider responsible for outsourced ICT support and agreed security-response activities. |
| **Downtime procedure** | Predefined manual or alternative clinical workflow used when electronic systems are unavailable or unsafe to use. |
| **Severity 1 / Critical** | Incident causing or likely to cause patient-safety impact, major clinical-system outage, ransomware, significant personal-data breach, or NIS2-significant disruption. |

---

## 6. Incident Response Principles

1. **Patient safety first**: Cybersecurity actions must not unnecessarily impede emergency treatment, triage, paediatrics, medication dispensing, surgery, or life-critical workflows.
2. **Contain rapidly, recover safely**: Containment may precede full forensic certainty where ransomware, active compromise, or patient-safety risk is suspected.
3. **Minimum necessary disruption**: Network isolation, account disabling, device quarantine, or service shutdown must be proportionate and coordinated with clinical leadership.
4. **Legal-clock discipline**: The hospital shall treat the time of awareness of a suspected personal data breach or significant NIS incident as a controlled timestamp for notification assessment.
5. **Evidence preservation**: Logs, alerts, device images where feasible, administrative actions, communications, and decisions must be preserved with integrity.
6. **Clear command structure**: During incidents, the Incident Response Coordinator coordinates technical response, while the Hospital Director or delegate retains executive authority for clinical and public-impact decisions.
7. **Supplier accountability**: Outsourcing does not transfer the hospital’s accountability for public-service continuity, patient data, or regulatory notification.
8. **Continuous improvement**: Lessons learned shall be converted into corrective actions, training updates, supplier actions, and budget-prioritised risk treatment.

These principles are based on NIST CSF 2.0 governance, response, recovery, communication, and improvement outcomes, and on NIST SP 800-61 Rev. 3’s treatment of incident response as an integrated cybersecurity risk-management activity. ([nvlpubs.nist.gov](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf))

---

## 7. Roles and Responsibilities

| Role | Responsibilities | Reference basis |
|---|---|---|
| **Hospital Director** | Accountable executive for incident response, patient-service continuity, major external communication approval, and risk acceptance during incidents. Approves Severity 1 declarations and extraordinary expenditure within delegated authority. | NIST CSF GV.RR-01, GV.RR-02; NIS2 management accountability principles; ISO/IEC 27001:2022 clauses 5.1, 5.3 |
| **Medical Director / Clinical Operations Lead** | Advises on patient-safety impacts, activates clinical downtime procedures, prioritises clinical service restoration, approves clinical-risk trade-offs. | NIST CSF GV.OC-04, RS.MA-04, RC.RP-04 |
| **Incident Response Coordinator — IT Service Responsible** | Maintains this policy, incident register, call tree, severity matrix, runbooks, technical coordination with MSP, evidence log, and after-action reports. | NIST CSF RS.MA-01 to RS.MA-05; ISO/IEC 27001:2022 A.5.24–A.5.28 |
| **MSP Incident Lead** | Provides 24/7 technical triage for Severity 1–2 incidents under contract, preserves logs, supports containment, eradication, backup restoration, endpoint isolation, and evidence collection. Must notify hospital contacts within defined SLA. | NIST CSF GV.SC-02, GV.SC-05, RS.MA-01; ISO/IEC 27001:2022 A.5.19, A.5.20, A.5.22 |
| **DPO / Privacy Officer** | Determines whether an incident is a personal data breach, assesses risk to individuals, prepares/validates Garante notification and data-subject communication, maintains data-breach register. | GDPR Articles 33–34; Garante data-breach guidance; ISO/IEC 27001:2022 A.5.34 |
| **Administrative Director / Legal Contact** | Supports regulatory notifications, procurement emergency actions, contractual enforcement against suppliers, insurance, and law-enforcement coordination. | NIST CSF RS.CO-02, RS.CO-03; ISO/IEC 27001:2022 A.5.31 |
| **Communications Lead** | Prepares internal staff notices, patient-facing messages, website/telephone scripts, press holding statements, and coordinates with ASL/regional communications. | NIST CSF RS.CO, RC.CO |
| **System Owners — ADT, EHR/FSE access, PACS/RIS, LIS, Pharmacy, Admin systems** | Provide system criticality, downtime procedures, user validation, data-integrity checks, and recovery acceptance. | NIST CSF ID.AM, RS.AN-08, RC.RP-05 |
| **Ward / Unit Managers** | Report suspected incidents, activate local downtime procedures, cascade staff instructions, collect clinical impact information. | NIST CSF RS.CO-02, RS.MA-02 |
| **All workforce members** | Immediately report suspected phishing, lost devices, unusual system behaviour, unauthorised access, ransomware messages, or data exposure. Follow downtime and communication instructions. | NIST CSF PR.AT, DE.AE-06, RS.MA-02 |
| **Regional ASL / Regional ICT or FSE contacts** | Provide escalation path for regional systems, FSE, SPID/CIE federation, inter-hospital dependencies, and regional incident coordination. | NIST CSF GV.OC-02, RS.CO-03, RC.CO-03 |

Role-based training shall include incident responsibilities for staff who have response duties, consistent with NIST SP 800-61 Rev. 3’s recommendation that role-based training include incident-related responsibilities. ([nvlpubs.nist.gov](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf))

---

## 8. Severity Classification

| Severity | Criteria | Examples | Required response |
|---|---|---|---|
| **S1 — Critical** | Actual or imminent patient-safety impact; loss of ADT/emergency-first-aid availability; ransomware or destructive malware; widespread clinical-system outage; confirmed or likely large-scale health-data breach; compromise of MSP privileged access; backup compromise. | Ransomware on EHR/PACS; ADT unavailable; domain admin compromise; PACS inaccessible during emergency care; confirmed exfiltration of patient records. | Immediate call tree activation; Hospital Director and Medical Director notified; MSP engaged urgently; DPO notified; NIS/GDPR assessment started; downtime procedures activated as needed. |
| **S2 — High** | Significant service disruption, confirmed unauthorised access to clinical/admin systems, compromised privileged account, malware affecting multiple endpoints, lost unencrypted mobile device with patient data. | Phishing leading to mailbox compromise; multiple clinical kiosks infected; stolen point-of-care device. | Response within 1 hour; Incident Response Coordinator leads; DPO and MSP involved; containment same shift. |
| **S3 — Medium** | Localised compromise or policy violation with limited operational impact or uncertain data exposure. | Single endpoint malware blocked; suspicious VPN login; unauthorised access attempt. | Triage within 4 business hours or same day for clinical assets. |
| **S4 — Low** | Security event with no confirmed compromise and no clinical impact. | Spam/phishing reported but not clicked; failed login noise; minor misconfiguration. | Record, monitor, close or escalate if new evidence appears. |

Incident reports must be triaged, validated, categorised, prioritised, and escalated where needed, consistent with NIST CSF RS.MA-02, RS.MA-03, and RS.MA-04. ([nvlpubs.nist.gov](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf))

---

## 9. Mandatory Incident Response Requirements and Controls

### 9.1 Preparation

| Control | Requirement | Implementation for this hospital | Source / auditable reference |
|---|---|---|---|
| **IR-01 Incident response governance** | The hospital shall maintain an approved incident response policy, severity matrix, call tree, and minimum runbooks for ransomware, phishing/account compromise, lost device, clinical-system outage, data breach, and MSP/vendor compromise. | Use lightweight documents maintained by IT Service Responsible and stored both online and printed in Emergency First Aid, switchboard, server room, and administrative office. | NIST CSF GV.PO-01, GV.PO-02, RS.MA-01; ISO/IEC 27001:2022 A.5.24; NIST SP 800-61 Rev. 3 |
| **IR-02 24/7 escalation** | A 24/7 escalation path shall exist for Severity 1 and Severity 2 incidents. | MSP contract must include emergency phone number, named escalation manager, response SLAs, log access obligations, and after-hours support. Internal call tree must include Hospital Director, Medical Director, IT, DPO, switchboard, and ward leads. | NIST CSF GV.RR-02, GV.SC-02, GV.SC-05, RS.MA-04; ISO/IEC 27001:2022 A.5.20 |
| **IR-03 Clinical downtime readiness** | Each critical clinical system shall have a documented downtime procedure. | Minimum coverage: ADT/emergency first aid, EHR/FSE access, PACS/RIS, LIS, pharmacy. Paper forms and downtime packs must be available in clinical units. | NIST CSF PR.IR, RC.RP-04; NIS2 Article 21 business continuity and crisis management; ISO/IEC 27001:2022 A.5.29, A.5.30 |
| **IR-04 Backup and restoration readiness** | Backups shall support incident recovery and shall be protected from ransomware. | Continue nightly NAS and weekly off-site tape; add monthly sample restore test and annual full DR exercise for ADT/EHR access dependencies where feasible. NAS admin access must be restricted and monitored; tapes must remain offline. | NIST CSF RC.RP-03, RC.RP-05; NIS2 Article 21(c); GDPR Article 32 availability/resilience principle |
| **IR-05 Minimum logging** | The hospital shall collect and preserve logs sufficient for triage and legal assessment. | Prioritise UTM/VPN, AD domain controllers, AV console, EHR/FSE access logs available locally or regionally, PACS/RIS, LIS, ADT, pharmacy admin logs, backup logs, and MSP remote-access logs. Use low-cost syslog or MSP log export rather than full SIEM initially. | NIST CSF DE.CM, DE.AE, RS.AN-06, RS.AN-07; ISO/IEC 27001:2022 A.8.15, A.8.16 |
| **IR-06 Workforce reporting** | Staff shall know how to report incidents quickly. | Provide one reporting email, one phone extension, and a “report suspicious email/device loss/system ransom screen” card during onboarding. Include in annual 2-hour training. | NIST CSF PR.AT, RS.MA-02; ISO/IEC 27001:2022 A.6.3, A.5.24 |
| **IR-07 Supplier readiness** | Critical suppliers shall be required to notify the hospital promptly of security incidents affecting hospital systems or data. | MSP and clinical vendors must notify the hospital within 1 hour for suspected compromise of hospital systems, privileged access, patient data, or service availability. Include right to logs, cooperation, and post-incident report in contracts at renewal or MEPA/CONSIP procurement. | NIST CSF GV.SC-02, GV.SC-05; NIS2 Article 21(d); ISO/IEC 27001:2022 A.5.19, A.5.20, A.5.22 |

NIS2 expressly includes incident handling, business continuity, backup management, disaster recovery, crisis management, and supply-chain security among risk-management measures, and the Directive recognises proportionality and cost of implementation, which is relevant to this hospital’s limited staffing and budget. ([eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/EN-SV/TXT/?uri=CELEX%3A32022L2555&utm_source=openai))

---

### 9.2 Detection, Reporting, and Triage

| Control | Requirement | Implementation for this hospital | Source / auditable reference |
|---|---|---|---|
| **IR-08 Immediate reporting by staff** | Any workforce member who observes a suspected incident shall report it immediately and shall not attempt unauthorised investigation. | Report phishing clicks, ransom notes, locked files, missing devices, unusual login prompts, suspected patient-record snooping, or system unavailability to IT/MSP/switchboard. | NIST CSF DE.AE-06, RS.MA-02; ISO/IEC 27001:2022 A.5.25 |
| **IR-09 Initial triage** | The Incident Response Coordinator or MSP shall validate reports and assign severity. | Use the severity table in Section 8. If clinical impact is uncertain, classify at the higher severity until Medical Director input is obtained. | NIST CSF RS.MA-02, RS.MA-03; ISO/IEC 27001:2022 A.5.25 |
| **IR-10 Awareness timestamp** | For potential personal data breaches or NIS-significant incidents, the coordinator shall record the time and basis of organisational awareness. | Record who knew what and when, including first report, validation time, and decision time. This starts legal assessment workflows. | GDPR Article 33; Garante guidance; NIS2 Article 23 / Italian NIS notification model |
| **IR-11 Escalation triggers** | S1 and S2 incidents must be escalated without waiting for complete root-cause analysis. | Ransomware indicators, clinical outage, domain admin compromise, confirmed unauthorised access, stolen unencrypted mobile device, or suspected patient-data leak trigger escalation. | NIST CSF RS.MA-04; RS.AN-08; ISO/IEC 27001:2022 A.5.26 |

---

### 9.3 Containment and Clinical Continuity

| Control | Requirement | Implementation for this hospital | Source / auditable reference |
|---|---|---|---|
| **IR-12 Ransomware containment** | Suspected ransomware shall trigger immediate containment. | MSP/IT may isolate affected endpoints, disable suspected accounts, block VPN sessions, disconnect infected VLAN segments, and protect NAS backups. Clinical leadership must be informed before broad shutdown unless delay would worsen patient safety or spread. | NIST CSF RS.MI-01, RS.MI-02; ISO/IEC 27001:2022 A.5.26 |
| **IR-13 Legacy kiosk containment** | Legacy Windows clinical kiosks shall be treated as high-risk during incidents. | If one kiosk is compromised, isolate that kiosk and assess peer kiosks on the same clinical VLAN. Do not reconnect until AV scan, account review, and patch/compensating-control decision are completed. | NIST CSF ID.RA, RS.AN-08, RS.MI-01; ISO/IEC 27001:2022 A.8.8, A.8.9 |
| **IR-14 Account compromise** | Suspected credential compromise shall trigger account containment. | Disable or reset affected account, revoke sessions where possible, review VPN/AD logs, check mailbox forwarding rules, and assess access to patient data. Privileged accounts receive priority. | NIST CSF PR.AA, DE.CM, RS.MI-01; ISO/IEC 27001:2022 A.5.16, A.5.17, A.8.5 |
| **IR-15 Mobile-device loss/theft** | Lost or stolen mobile devices shall be reported immediately and remotely locked/wiped where technically possible. | Disable associated accounts/tokens, check device encryption/MDM status, document patient-data exposure, notify DPO. If no MDM exists, prioritise implementation for point-of-care devices within annual budget planning. | NIST CSF PR.DS, RS.MI-01; GDPR Articles 32–34; ISO/IEC 27001:2022 A.8.1 |
| **IR-16 Downtime activation** | Clinical downtime procedures shall be activated when electronic systems are unavailable, unsafe, or unreliable. | Medical Director or delegated on-call clinical lead activates downtime. IT/MSP must not restore clinical systems into use until integrity and safety checks are completed by system owner and clinical representative. | NIST CSF RC.RP-04, RC.RP-05; ISO/IEC 27001:2022 A.5.29, A.5.30 |
| **IR-17 Network isolation authority** | The Incident Response Coordinator and MSP may isolate systems during S1/S2 incidents. | For major segmentation actions affecting care, notify Medical Director immediately. Emergency isolation may occur first if ransomware propagation is active. | NIST CSF RS.MI-01; ISO/IEC 27001:2022 A.5.26 |

NIST CSF 2.0 states that incidents are contained and eradicated under Incident Mitigation, and that recovery actions should be selected, scoped, prioritised, verified, and documented under Incident Recovery Plan Execution. ([nvlpubs.nist.gov](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf))

---

### 9.4 Investigation, Evidence, and Documentation

| Control | Requirement | Implementation for this hospital | Source / auditable reference |
|---|---|---|---|
| **IR-18 Incident record** | Every S1–S3 incident shall have an incident ticket or record. | Minimum fields: timestamp, reporter, affected systems, severity, patient impact, suspected data impact, actions taken, decisions, evidence locations, notifications, recovery validation, closure approval. | NIST CSF RS.AN-06, RS.AN-07; ISO/IEC 27001:2022 A.5.28 |
| **IR-19 Evidence preservation** | Evidence shall be preserved proportionately and safely. | Export logs, preserve ransom notes, screenshots, email headers, AV alerts, UTM/VPN logs, AD sign-ins, and backup job logs. Full disk images are required only when feasible and clinically appropriate. | NIST CSF RS.AN-06, RS.AN-07; ISO/IEC 27001:2022 A.5.28 |
| **IR-20 Root-cause analysis** | S1 and S2 incidents require root-cause analysis or a documented best-effort explanation. | RCA may be performed by MSP or external consultant. For ransomware, include initial access vector, lateral movement, affected accounts, data-access assessment, and backup integrity. | NIST CSF RS.AN-03; ISO/IEC 27001:2022 A.5.27 |
| **IR-21 Investigation confidentiality** | Incident information shall be shared strictly on a need-to-know basis. | Avoid broad email threads containing patient data, indicators, or legal assessments. Use restricted folders and named recipients. | GDPR Article 32 confidentiality principle; NIST CSF RS.CO-03; ISO/IEC 27001:2022 A.5.10, A.5.15 |

NIST CSF 2.0 requires that investigation actions be recorded, that incident data and metadata be collected with integrity and provenance preserved, and that incident magnitude be estimated and validated. ([nvlpubs.nist.gov](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf))

---

### 9.5 Legal, Regulatory, and External Notification

| Control | Requirement | Implementation for this hospital | Source / auditable reference |
|---|---|---|---|
| **IR-22 GDPR breach assessment** | The DPO shall assess every suspected personal data breach. | Assess type of data, health/minor data, number of subjects, confidentiality/integrity/availability impact, likelihood and severity of harm, mitigating controls, and whether notification is required. | GDPR Articles 33–34; Garante guidance |
| **IR-23 Garante notification** | Notifiable personal data breaches shall be notified to the Garante without undue delay and, where feasible, within 72 hours of awareness. | Use the Garante telematic procedure. If notification is late, document reasons. Maintain breach register regardless of notification. | GDPR Article 33; Garante data-breach guidance |
| **IR-24 Communication to data subjects** | High-risk personal data breaches shall be communicated to affected individuals unless a GDPR exception applies. | Communications must be clear, plain language, coordinated by DPO, Legal, Communications, and ASL/regional contacts where relevant. | GDPR Article 34; Garante guidance |
| **IR-25 NIS2 / CSIRT Italia notification** | Significant incidents affecting service provision shall be assessed for NIS notification duties. | For NIS-significant incidents, prepare early warning within 24 hours, incident notification within 72 hours, and final report within one month, with progress report if ongoing. Coordinate with ASL/regional NIS contacts and CSIRT Italia procedures. | NIS2 Article 23; D.Lgs. 138/2024 Article 25; NIST CSF RS.CO-02 |
| **IR-26 Law enforcement** | Incidents suspected to involve criminal activity may be reported to competent law enforcement, coordinated by Legal/Administrative Director and Hospital Director. | Ransomware, extortion, data theft, fraud, or malicious insider activity should be considered for reporting. Preserve evidence before disruptive actions where feasible. | NIS2 recital and Article 23 reporting principles; ISO/IEC 27001:2022 A.5.31 |
| **IR-27 Public and media communication** | Staff shall not communicate incident details externally unless authorised. | All press, patient-facing, supplier-wide, or public statements require approval by Hospital Director or delegate, DPO where data is involved, and ASL/regional communications where applicable. | NIST CSF RS.CO, RC.CO; ISO/IEC 27001:2022 A.5.14 |

The Garante requires notification through its dedicated online procedure and states that controllers must document all personal data breaches, while NIS2 establishes the 24-hour, 72-hour, and one-month reporting sequence for significant incidents. ([garanteprivacy.it](https://www.garanteprivacy.it/data-breach))

---

### 9.6 Recovery and Return to Service

| Control | Requirement | Implementation for this hospital | Source / auditable reference |
|---|---|---|---|
| **IR-28 Recovery prioritisation** | Recovery shall follow clinical criticality. | Priority 1: ADT / emergency first aid, identity services, network core. Priority 2: EHR/FSE access, LIS, pharmacy. Priority 3: PACS/RIS unless emergency imaging need elevates priority. Priority 4: administrative systems. | NIST CSF RC.RP-02, RC.RP-04; hospital RTO objectives |
| **IR-29 RTO targets** | Incident recovery planning shall support target RTOs of 1 hour for ADT/emergency-first-aid workflows and 4 hours for EHR access, recognising that manual downtime may satisfy temporary clinical continuity. | If technical restoration cannot meet RTO, clinical downtime procedure must be confirmed active and communicated. | NIST CSF RC.RP-01, RC.RP-02, RC.CO-03; ISO/IEC 27001:2022 A.5.30 |
| **IR-30 Backup integrity before restore** | Backups and restoration media shall be checked before use. | Confirm backup date, malware risk, restore point, and integrity. Do not restore from suspected compromised NAS without MSP/IT validation. Prefer offline tape for ransomware recovery if NAS integrity is doubtful. | NIST CSF RC.RP-03; NIS2 Article 21(c) |
| **IR-31 Clinical validation** | Clinical system owners must validate restored systems before normal operations resume. | Validate patient identity matching, recent transactions, lab/radiology interfaces, medication records, ADT feeds, and downtime data reconciliation. | NIST CSF RC.RP-05; ISO/IEC 27001:2022 A.5.29 |
| **IR-32 Recovery closure** | Incident recovery may be declared complete only when defined closure criteria are met. | Criteria: containment complete, affected services restored or accepted workaround in place, patient-safety risk reviewed, legal notifications addressed, evidence secured, monitoring heightened, and documentation updated. | NIST CSF RC.RP-06; ISO/IEC 27001:2022 A.5.27 |

NIST CSF 2.0 specifically requires verification of backup and restoration-asset integrity before restoration, verification of restored assets, confirmation of normal operating status, and documented declaration of recovery closure. ([nvlpubs.nist.gov](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf))

---

### 9.7 Lessons Learned and Improvement

| Control | Requirement | Implementation for this hospital | Source / auditable reference |
|---|---|---|---|
| **IR-33 Post-incident review** | S1 and S2 incidents require a post-incident review within 10 working days after recovery closure. | Include IT, MSP, Medical Director or delegate, DPO if data involved, system owner, and affected unit manager. | NIST CSF ID.IM, RC.RP-06; ISO/IEC 27001:2022 A.5.27 |
| **IR-34 Corrective-action tracking** | Lessons learned shall become tracked corrective actions. | Actions must have owner, due date, risk rating, budget impact, and status. Prioritise low-cost, high-impact improvements due to limited budget. | NIST CSF GV.OV-03, ID.IM; ISO/IEC 27001:2022 clause 10 |
| **IR-35 Training update** | Incident lessons shall update staff awareness materials. | Use short Italian-language alerts, onboarding inserts, and annual 2-hour training. Prioritise phishing, mobile theft, ransomware recognition, and downtime behaviour. | NIST CSF PR.AT; NIST SP 800-61 Rev. 3 role-based training guidance; ISO/IEC 27001:2022 A.6.3 |
| **IR-36 Testing and exercises** | Incident response capability shall be tested at least annually. | Conduct one annual tabletop exercise rotating ransomware, ADT outage, data breach, or MSP compromise. Conduct at least one annual backup restore/DR test; perform smaller monthly sample restore checks where feasible. | NIST CSF GV.OV, RC.RP; ISO/IEC 27001:2022 A.5.24, A.5.30 |

NIST SP 800-61 Rev. 3 emphasises that lessons learned and root-cause analysis should improve cybersecurity risk management and help the organisation become better prepared to identify assets and risks and to detect, respond to, and recover from incidents. ([nvlpubs.nist.gov](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf))

---

## 10. Incident-Specific Minimum Runbooks

The Incident Response Coordinator shall maintain concise runbooks for the following scenarios. Each runbook must include detection signs, first actions, escalation, containment, evidence, clinical continuity, legal assessment, recovery, and closure checklist.

### 10.1 Ransomware on EHR / PACS / clinical network

Minimum actions:

1. Declare S1 unless proven otherwise.
2. Inform Hospital Director, Medical Director, DPO, MSP, and switchboard.
3. Activate relevant clinical downtime procedures.
4. Isolate affected endpoints/VLANs; disable suspected accounts; suspend risky VPN sessions.
5. Protect backups: stop suspicious backup jobs only if needed to prevent encryption propagation; preserve last known clean backups.
6. Preserve ransom note, filenames, affected hostnames, AV/UTM/AD logs.
7. Assess data exfiltration indicators.
8. Prepare GDPR and NIS2 notification assessment.
9. Restore only after backup integrity and restored-system validation.
10. Complete post-incident review and corrective actions.

References: NIST CSF RS.MA, RS.AN, RS.MI, RC.RP; ISO/IEC 27001:2022 A.5.24–A.5.28, A.5.30; NIS2 Articles 21 and 23; GDPR Articles 32–34.

### 10.2 Phishing / credential compromise

Minimum actions:

1. Triage as S2 if credentials entered, mailbox accessed, or clinical/admin account affected.
2. Reset password and revoke sessions.
3. Check mailbox rules, sent items, VPN logins, AD events, and patient-system access.
4. Search for similar emails and remove/quarantine if feasible.
5. Notify affected staff and ward manager where clinical workflow risk exists.
6. DPO assesses whether unauthorised personal-data access occurred.
7. Update awareness material with anonymised lesson.

References: NIST CSF PR.AT, PR.AA, DE.CM, RS.AN, RS.MI; ISO/IEC 27001:2022 A.5.16, A.5.17, A.6.3, A.8.15, A.8.16.

### 10.3 Lost or stolen point-of-care mobile device

Minimum actions:

1. Record time, user, device, last location, and patient-data access.
2. Lock/wipe device where possible.
3. Disable associated account/session/token.
4. Determine encryption and MDM status.
5. DPO assesses GDPR breach risk, especially if health or minor data may be exposed.
6. File internal security report; consider law-enforcement report for theft.
7. Replace device only after confirming secure configuration.

References: GDPR Articles 32–34; Garante data-breach guidance; NIST CSF PR.DS, RS.MA, RS.MI; ISO/IEC 27001:2022 A.8.1.

### 10.4 MSP or vendor compromise

Minimum actions:

1. Classify as S1 if privileged access, remote management, backups, identity, or clinical system support is affected.
2. Disable or restrict vendor remote access pending validation.
3. Require MSP/vendor incident statement, affected accounts, timelines, IOCs, and containment actions.
4. Review logs for remote access, privilege use, data access, and configuration changes.
5. Assess NIS2 supply-chain and notification impact.
6. Require post-incident supplier report and contractual remediation.

References: NIST CSF GV.SC-02, GV.SC-05, RS.CO-03; NIS2 Article 21(d); ISO/IEC 27001:2022 A.5.19, A.5.20, A.5.22.

### 10.5 Suspected unauthorised patient-record access

Minimum actions:

1. Preserve access logs from relevant systems.
2. Identify patient records, users, timestamps, purpose of access, and role legitimacy.
3. Involve DPO and HR/Legal if insider misuse is suspected.
4. Limit knowledge to need-to-know.
5. Determine GDPR notification and data-subject communication duties.
6. Apply disciplinary or access-control corrective actions where appropriate.

References: GDPR Articles 32–34; Garante data-breach guidance; NIST CSF RS.AN-06, RS.AN-07; ISO/IEC 27001:2022 A.5.15, A.5.18, A.5.28.

---

## 11. Communications Rules

1. **Internal incident channel**: S1/S2 communications shall use a dedicated incident bridge or telephone channel plus restricted written log. Avoid uncontrolled mass email.
2. **Clinical instructions**: Instructions affecting care delivery must be approved or validated by the Medical Director or delegated clinical lead.
3. **Staff notices**: Staff notices must be short, actionable, and in Italian where operationally necessary.
4. **External parties**: Communications to patients, public, media, regulators, suppliers, regional ASL, or law enforcement must be coordinated through authorised roles.
5. **No speculation**: Communications must distinguish confirmed facts from hypotheses.
6. **Sensitive details**: Indicators of compromise, vulnerabilities, patient data, credentials, and forensic details must not be shared publicly unless approved and necessary.

References: NIST CSF RS.CO-02, RS.CO-03, RC.CO-03, RC.CO-04; ISO/IEC 27001:2022 A.5.14.

---

## 12. Records and Retention

The hospital shall retain incident records, evidence logs, breach assessments, notification decisions, communications, post-incident reviews, and corrective-action records for at least **five years**, unless a longer period is required by law, litigation hold, ASL/regional instruction, contractual obligation, or medical-record governance rule.

Security logs required for investigation should be retained for a minimum of **180 days** where technically and contractually feasible, with higher-priority retention for AD, VPN, UTM, AV, privileged access, clinical-system audit logs, and backup logs. Where systems cannot meet this due to technical limits, the exception must be recorded and risk-treated.

References: GDPR accountability and breach-documentation requirements; Garante breach-register guidance; NIST CSF RS.AN-06, RS.AN-07; ISO/IEC 27001:2022 A.5.28, A.8.15.

---

## 13. Exceptions

1. Exceptions to this policy require written approval from the Hospital Director or delegated executive, with advice from the Incident Response Coordinator and DPO where personal data is involved.
2. Emergency clinical exceptions are permitted where strict compliance would endanger patient safety. Such exceptions must be documented within 24 hours after the emergency condition stabilises.
3. No exception may waive statutory notification obligations to the Garante, CSIRT Italia, competent authorities, or affected individuals where legally required.
4. Any recurring exception must be converted into a formal risk treatment plan.

References: NIST CSF GV.RM, GV.RR, GV.PO; ISO/IEC 27001:2022 clauses 6.1, 8.1, 9.3.

---

## 14. Monitoring, Metrics, and Review

The Incident Response Coordinator shall maintain the following metrics and report them at least quarterly to hospital management and annually to the ASL/regional ICT/security governance function where required:

1. Number of incidents by severity and type.
2. Time from report to triage.
3. Time from declaration to containment for S1/S2 incidents.
4. Clinical downtime activations and duration.
5. GDPR/NIS notification assessments and outcomes.
6. Backup restore test results.
7. Open corrective actions and overdue actions.
8. Phishing reports and repeat training needs.
9. Supplier incident or SLA failures.
10. Legacy kiosk incident trends and compensating controls.

This policy shall be reviewed annually and after any S1/S2 incident. Review must consider changes in threat profile, clinical operations, procurement, regional FSE requirements, NIS2/Italian implementing measures, Garante guidance, MSP contract terms, and hospital budget.

References: NIST CSF GV.OV-01 to GV.OV-03, ID.IM, RS.MA, RC.RP; ISO/IEC 27001:2022 clauses 9 and 10.

---

## 15. References

1. **Regulation (EU) 2016/679 — GDPR**, especially Articles 32, 33, and 34.
2. **Garante per la Protezione dei Dati Personali — Data Breach / Violazioni di dati personali guidance**, including 72-hour notification, online notification procedure, high-risk communication to data subjects, and breach documentation expectations. ([garanteprivacy.it](https://www.garanteprivacy.it/data-breach))
3. **D.Lgs. 196/2003**, as amended by **D.Lgs. 101/2018** — Italian Privacy Code.
4. **Directive (EU) 2022/2555 — NIS2**, especially Article 21 cybersecurity risk-management measures and Article 23 incident reporting timeline. ([eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/EN-SV/TXT/?uri=CELEX%3A32022L2555&utm_source=openai))
5. **D.Lgs. 4 September 2024, n. 138** — Italian transposition of NIS2, especially Article 25 incident notification to CSIRT Italia.
6. **NIST Cybersecurity Framework 2.0**, especially GV.RR, GV.PO, GV.SC, DE.CM, DE.AE, RS.MA, RS.AN, RS.CO, RS.MI, RC.RP, and RC.CO. ([nvlpubs.nist.gov](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf))
7. **NIST SP 800-61 Rev. 3 — Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile**. ([csrc.nist.gov](https://csrc.nist.gov/pubs/sp/800/61/r3/final))
8. **ISO/IEC 27001:2022**, including Annex A controls A.5.24, A.5.25, A.5.26, A.5.27, A.5.28, A.5.29, A.5.30, A.5.19, A.5.20, A.5.22, A.8.15, and A.8.16.
9. **AGID Misure minime di sicurezza ICT per le pubbliche amministrazioni** and applicable AGID public-administration cybersecurity guidance. AGID describes the minimum ICT security measures as a practical reference for public administrations to assess and improve security against common cyber threats. ([agid.gov.it](https://www.agid.gov.it/it/sicurezza/misure-minime-sicurezza-ict?utm_source=openai))
10. **Regional regulations and ASL instructions for FSE / Fascicolo Sanitario Elettronico and regional clinical platforms**.
