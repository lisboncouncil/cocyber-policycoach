---
config: C2
context_id: ctx-H
policy_id: P4
policy_name: Incident Response Policy
policy_short: ir
metadata:
  config: C2
  model: moonshotai/Kimi-K2.5
  input_tokens: 25355
  output_tokens: 7106
  total_tokens: 32461
  latency_s: 33.821
  tool_calls:
  - rag_retrieval
  raw_provider_id: f88ac5ea-53f7-4342-b64d-89d02abc9ec7
  chunks_retrieved: 5
  server_version: 1.3.4
sources_count: 3
sources:
- type: kb_source
  source: ./datadir-plus-templates/cyber_incident_response_plan.docx
  title: ./datadir-plus-templates/cyber_incident_response_plan.docx
- type: kb_source
  source: ./datadir-plus-templates/1.json
  title: Best Practices for Cyber Crisis Management
- type: kb_source
  source: ./datadir-plus-templates/9.json
  title: 'The Sector CSIRT Framework: Developing Sector-Based Incident Response Capabilities'
prompt_chars: 4675
answer_chars: 17283
generated_at_unix: 1778086668
---

 <policy title="Cyber Incident Response Policy and Plan">
| Field | Value |
|---|---|
| **Document ID** | POL-008-IR |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Internal — Restricted |
| **Owner** | IT Manager (External MSP) / Direttore Sanitario (Medical Director) |
| **Approved by** | Direttore Generale (CEO) |
| **Approval date** | [DD/MM/YYYY] |
| **Next review date** | [DD/MM/YYYY] |
| **Review cycle** | Annual (and after any significant incident) |

---

## 1. Purpose and Objectives

This Cyber Incident Response Policy and Plan establishes the framework for detecting, reporting, assessing, and responding to cyber incidents at [Hospital Name] (hereinafter "the Hospital"), a provincial public hospital operating within the Servizio Sanitario Nazionale. 

**Purpose:** To ensure a rapid, coordinated, and legally compliant response to cyber incidents that minimizes impact on patient safety, protects the confidentiality, integrity, and availability of health data (including FSE, PACS, and clinical systems), and meets regulatory obligations under NIS2* and GDPR.*

**Objectives:**
- Provide clear, actionable procedures for the 24/7 clinical environment, respecting the constraint that **patient safety takes precedence over all technical response actions** (ISO 27001:2022 A.5.26, NIST CSF 2.0 RS.RC-01).
- Define roles and escalation paths given the Hospital's resource constraints (1.5 FTE internal IT, outsourced MSP).
- Ensure compliance with NIS2* mandatory reporting to CSIRT Italia within 24 hours (early warning) and 72 hours (initial assessment) for significant incidents affecting essential entities (health sector).
- Ensure compliance with GDPR Article 33* (72-hour notification to Garante Privacy for personal data breaches) and D.Lgs. 196/2003 as amended by D.Lgs. 101/2018.*
- Maintain business continuity aligned with RTO targets: 1 hour for ADT/Pronto Soccorso, 4 hours for EHR (FSE).

---

## 2. Scope

This policy applies to:
- All information systems processing health data (FSE, PACS, RIS, LIS, ADT, Pharmacy systems) and administrative systems.
- All personnel: 130 clinical staff, 50 administrative staff, 20 technical/facility staff, and contractors (including the Managed Service Provider).
- All cyber incidents: ransomware, data breaches (insider/external), phishing, supply-chain compromises (MSP/medical device vendors), and physical theft of mobile devices containing patient data.
- All locations: 80-bed facility, emergency department, radiology, laboratories, and administrative offices.

---

## 3. Standards and Regulatory Frameworks

This policy aligns with:
- **NIS2 Directive (EU) 2022/2555** — Articles 21 (risk management measures) and 23 (incident reporting) for essential entities (health sector).
- **GDPR (EU) 2016/679** — Articles 33 (breach notification) and 34 (communication to data subjects).
- **D.Lgs. 196/2003** (Codice Privacy) as amended by **D.Lgs. 101/2018** — Personal data breach notification obligations.
- **ISO/IEC 27001:2022** — Controls 5.24 (Planning), 5.25 (Assessment), 5.26 (Response), 5.27 (Learning), 5.28 (Evidence).
- **NIST CSF 2.0** — Respond Function (RS.RC, RS.AN, RS.MI, RS.IM).
- **AGID Linee Guida** — Misure minime di sicurezza per le pubbliche amministrazioni (Incident Response requirements).
- **Regional ASL** — Fascicolo Sanitario Elettronico (FSE) security protocols.

---

## 4. Definitions

| Term | Definition |
|---|---|
| **Significant Incident** (NIS2) | An incident causing severe operational disruption or financial loss, affecting service provision to recipients (Art. 23.2). For hospitals: ransomware on EHR, PACS outage >1h, data breach >500 patients. |
| **Personal Data Breach** (GDPR) | Breach of security leading to accidental/unlawful destruction, loss, alteration, unauthorised disclosure of personal data (Art. 4(12)). |
| **CIRT** | Cyber Incident Response Team — operational team managing the incident (Hospital staff + MSP). |
| **MT** | Management Team — strategic oversight (Direttore Generale, Direttore Sanitario, Administrative Director). |
| **MSP** | Managed Service Provider — external IT provider with 24/7 SOC capability (if available) or on-call support. |
| **Ransomware** | Malware encrypting systems/data demanding payment (primary threat vector for Italian hospitals). |
| **FSE** | Fascicolo Sanitario Elettronico — regional electronic health record. |

---

## 5. Common Threat Vectors and Incident Types

Based on the Hospital's threat profile (AGID Risk Assessment guidelines):

| Threat Vector | Examples | Initial Response |
|---|---|---|
| **Ransomware** | Encryption of EHR/PACS, Hive/LockBit variants targeting healthcare | Isolate affected VLANs immediately; do not power off PACS servers (preserve memory forensics); activate paper-based contingency procedures; notify CIRT within 15 minutes. |
| **Phishing** | Spear-phishing targeting clinical staff for FSE credentials | Reset compromised credentials; check FSE access logs for unauthorised access; awareness alert to all staff. |
| **Insider Data Leak** | Unauthorized export of patient lists, snooping on celebrity patients | Suspend user access; preserve audit logs; assess scope via FSE access logs. |
| **Supply Chain (MSP)** | Compromise of MSP tools affecting Hospital infrastructure | Invoke contractual incident clauses with MSP; isolate MSP management VLANs; activate internal emergency contacts. |
| **Physical Theft** | Theft of point-of-care tablet/laptop with patient data | Remote wipe if MDM enabled; revoke device certificates; assess data at risk per GDPR; report to Postal Police. |
| **Medical Device Compromise** | Unpatched radiology workstation used as pivot | Isolate device from network; continue clinical use if safe (air-gapped mode); notify vendor. |

---

## 6. Incident Response Process

### Phase 1 — Preparation
- **Offline Documentation:** Print and store offline copies of this plan, contact lists, and network diagrams (NIST CSF RS.RC-01). Store in Direttore Generale's safe and Nursing Director's office.
- **Asset Inventory:** Maintain updated inventory of critical systems (PACS, ADT) per Asset Management Policy (POL-003) — ISO 27001 A.5.9.
- **Training:** Annual 2-hour cybersecurity training for all staff (GDPR Art. 39), including phishing recognition and incident reporting channels.
- **Backup Verification:** Monthly verification that offline backups (weekly tape) are recoverable for EHR/PACS (NIS2 Art. 21.2(c)).

### Phase 2 — Detection and Reporting
**Detection Sources:**
- MSP Security Operations Centre (if contracted) or AV console alerts.
- Clinical staff reporting unusual system behaviour (slow EHR, encrypted files).
- Automatic alerts from UTM firewall (single-vendor).

**Reporting Channels (24/7):**
- **Primary:** MSP Helpdesk [Phone: XXX] / Email: [soc@msp.example]
- **Clinical Emergency:** Nursing Coordinator on-call [Phone: XXX]
- **Escalation:** Direttore Sanitario [Phone: XXX]

**Requirement:** All suspected incidents must be reported within **15 minutes** of detection to the MSP (NIS2 early warning preparation).

### Phase 3 — Classification and Triage

| Severity | Criteria | NIS2 Reporting | Response SLA |
|---|---|---|---|
| **Critical** | Ransomware on EHR/PACS; Active data exfiltration; ADT/PS outage >30min | Mandatory (24h early warning) | Immediate (< 30 min) |
| **High** | Confirmed PHI breach >50 patients; Clinical workstation compromise; LIS outage | Mandatory (72h assessment) | < 2 hours |
| **Medium** | Phishing with credentials compromised; Single system malware; Guest network breach | Voluntary | < 24 hours |
| **Low** | Spam; Unsuccessful port scans; Policy violations | No | < 72 hours |

*Classification must consider patient safety impact first (ISO 27001 A.5.26).*

### Phase 4 — Containment
**Clinical Safety Priority:** Before technical containment (e.g., isolating a VLAN), assess impact on life-support or emergency systems. Consult Direttore Sanitario if isolation affects Pronto Soccorso (Emergency Department).

- **Short-term:** Isolate affected systems at switch level (limited segmentation available); disable compromised AD accounts; block malicious IPs at UTM.
- **Long-term:** Apply emergency patches; rotate all administrative credentials (Password Policy POL-006).

### Phase 5 — Eradication
- Remove malware using MSP tools; reimage compromised Windows workstations (including 35 legacy clinical kiosks if infected).
- For ransomware: Do not pay ransom without written approval from Direttore Generale and legal counsel (AGID guidelines).
- Verify root cause elimination via log review (UTM logs, AD logs).

### Phase 6 — Recovery
- Restore EHR from NAS backups (RPO: 24h) within 4-hour RTO target.
- Restore ADT/PS within 1-hour RTO using high-availability contingency (paper forms + manual entry).
- Validate integrity of PACS images before returning to production (Backup Policy POL-004).

### Phase 7 — Post-Incident Review
- **Timing:** Within 5 business days for Critical/High incidents (ISO 27001 A.5.27).
- **Attendees:** IT Manager (MSP), Direttore Sanitario, Nursing Director, Administrative Director.
- **Outputs:** Lessons learned report; update to this policy; staff awareness briefing if phishing involved.
- **NIS2 Final Report:** Submit to CSIRT Italia within 1 month of incident closure (Art. 23.4).

---

## 7. Roles and Responsibilities

### 7.1 Cyber Incident Response Team (CIRT)

Given limited internal IT (1.5 FTE), the CIRT is a hybrid internal/external team:

| Role | Responsibility | Contact |
|---|---|---|
| **CIRT Lead** | IT Manager (MSP) — coordinates technical response, liaises with CSIRT Italia | [MSP 24/7 Number] |
| **Clinical Safety Lead** | Direttore Sanitario — assesses patient safety impact, approves clinical system isolation | [Mobile] |
| **Administrative Lead** | Administrative Director — manages regulatory reporting (Garante), insurance notifications | [Mobile] |
| **Internal IT Liaison** | Internal IT Technician (1.5 FTE) — provides local access, physical system checks | [Mobile] |
| **Legal/Compliance** | External Legal Counsel (15k EUR budget) — GDPR/NIS2 compliance assessment | [Phone] |

### 7.2 Management Team (MT)
Activated for Critical/High incidents:
- **Direttore Generale:** Authorizes public statements, ransom decisions (non-payment preferred), and regulatory notifications.
- **Direttore Sanitario:** Clinical continuity decisions.
- **Regional ASL Contact:** For FSE-related incidents (mandatory regional notification).

---

## 8. Reporting Contacts and Regulatory Notifications

### 8.1 Internal Reporting (24/7)
| Channel | Contact Details |
|---|---|
| MSP SOC (Primary) | [24/7 Phone], [Email] |
| Hospital Switchboard (Emergency) | [Number] — for out-of-hours escalation to Direttore Sanitario |
| Nursing Coordinator | [Mobile] — for clinical system alerts |

### 8.2 External Reporting Obligations (NIS2 & GDPR)

| Authority | Trigger | Deadline | Method |
|---|---|---|---|
| **CSIRT Italia** (NIS2) | Significant incident affecting essential entity services | 24h (early warning), 72h (initial assessment), 1 month (final report) | https://www.csirt.gov.it (secure portal) |
| **Garante Privacy** | Personal data breach likely to result in risk to rights | 72 hours from awareness | Online form on garanteprivacy.it |
| **Data Subjects** (Patients) | High-risk breach per GDPR Art. 34 | Without undue delay | Registered letter or secure email if contact available |
| **Postal Police** (Polizia Postale) | Criminal activity (ransomware, theft) | Without undue delay | 117 or local Commissariato |
| **Regional ASL** | FSE data breach or unavailability | Concurrent with CSIRT Italia | Regional secure channel |
| **Cyber Insurance** | If policy held (check procurement records) | Per policy terms (typically 24h) | [Policy number/contact] |

*Note: NIS2 reporting takes precedence; simultaneous notification to Garante required if personal data involved.*

---

## 9. Communications Management

### 9.1 Internal Communications
- **Staff:** Use analog methods (paper notices, PA system) if IT systems compromised. Avoid email during active ransomware.
- **Clinical Departments:** Direct phone calls from Nursing Coordinator to Ward Chiefs for Critical incidents.

### 9.2 External Communications
- **Media:** Only Direttore Generale or designated spokesperson (External Legal) may communicate with press (NIS2 Art. 21.3).
- **Patients:** Template letters for data breach notifications must be pre-approved by Garante Privacy guidelines (D.Lgs. 101/2018).
- **Regulators:** Use encrypted channels where available (PEC — Posta Elettronica Certificata for Italian authorities).

---

## 10. Evidence Preservation and Forensics

- **Chain of Custody:** Document all actions taken (screenshots, log exports) with timestamps (ISO 27001 A.5.28).
- **Log Retention:** UTM logs and AD authentication logs retained for 12 months (AGID Misure Minime).
- **Forensic Images:** For ransomware, preserve disk images of affected servers (PACS) before restoration for potential law enforcement investigation.
- **Legal Privilege:** Coordinate with External Legal Counsel to maintain privilege over forensic reports.

---

## 11. Testing and Exercises

Given resource constraints (70k EUR budget):
- **Annual Tabletop Exercise:** Simulate ransomware on PACS involving clinical and IT staff (NIST CSF RS.RC-02).
- **Quarterly Contact Verification:** Verify MSP 24/7 contact numbers and offline document accessibility.
- **Drill:** Test paper-based contingency procedures for ADT/PS annually (align with Business Continuity Plan).

---

## 12. Integration with Business Continuity

This policy aligns with the Hospital's Business Continuity Plan (BCP):
- **Clinical Contingency:** Paper-based patient records (Cartella Clinica Cartacea) activated when EHR unavailable >1 hour.
- **RTO Compliance:** Recovery procedures must meet 1h (ADT/PS) and 4h (EHR) targets (Section 6.6).

---

## 13. Exceptions

Given the 35 legacy Windows clinical kiosks (unpatchable):
- **Compensating Controls:** These systems must remain on isolated VLANs with no internet access and restricted to specific MAC addresses (Network Policy POL-005).
- **Exception Process:** Documented in ISMS Exception Register, reviewed every 6 months by CIRT Lead and Direttore Sanitario (ISO 27001 A.5.36).

---

## 14. Enforcement

Non-compliance with reporting obligations (e.g., failure to report ransomware within 15 minutes to MSP) may result in disciplinary action per CCNL (National Collective Bargaining Agreement) for public health workers. Deliberate concealment of incidents may trigger personal liability under D.Lgs. 196/2003.

---

## 15. Related Documents

| Document ID | Title | Relationship |
|---|---|---|
| POL-001 | Cybersecurity Policy | Parent policy |
| POL-002 | Access Control Policy | Credential revocation procedures |
| POL-003 | Asset Management Policy | Inventory of critical systems |
| POL-004 | Backup and Recovery Policy | RTO/RPO targets for clinical systems |
| POL-005 | Network Security Policy | VLAN isolation procedures |
| POL-006 | Password Policy | Emergency credential rotation |
| POL-007 | Vulnerability Management | Patch status for incident root cause |
| POL-009 | 10 Golden Rules | Staff awareness baseline |

---

## 16. Compliance and Regulatory References

- **NIS2 Directive (EU) 2022/2555** — Articles 21, 23 (incident handling and reporting for essential entities).
- **GDPR (EU) 2016/679** — Articles 33, 34 (breach notification).
- **D.Lgs. 196/2003** (Privacy Code) and **D.Lgs. 101/2018** (GDPR harmonization) — Security measures and breach notification.
- **ISO/IEC 27001:2022** — Controls 5.24, 5.25, 5.26, 5.27, 5.28 (incident management lifecycle).
- **NIST CSF 2.0** — Respond Function (RS.RC, RS.AN, RS.MI, RS.IM).
- **AGID Misure Minime** — Specifiche tecniche per la sicurezza informatica nella PA (Incident Response requirements).
- **CyberFundamentals Framework** (Centre for Cybersecurity Belgium) — Basic/Important/Essential levels adapted for Italian context.

---

## 17. Revision History

| Version | Date | Author | Description of Change |
|---|---|---|---|
| 1.0 | [DD/MM/YYYY] | IT Manager (MSP) / Direttore Sanitario | Initial release — tailored for 200-bed provincial hospital under NIS2 |

---

## 18. Approval

| Role | Name | Signature | Date |
|---|---|---|---|
| Policy Owner (IT Manager MSP) | | | |
| Co-Owner (Direttore Sanitario) | | | |
| Approved by (Direttore Generale) | | | |
| Compliance Review (External Legal) | | | |

---

## Annex A — Quick Reference Card for Clinical Staff

**IF YOU SEE RANSOMWARE (Locked screen, ransom note):**
1. **DO NOT TURN OFF** the computer (preserve evidence).
2. **UNPLUG NETWORK CABLE** or disable Wi-Fi immediately.
3. **CALL** MSP Emergency [Number] AND Nursing Coordinator [Number].
4. **CONTINUE PATIENT CARE** using paper forms (Contingency Mode).

**REPORTING IS MANDATORY:** Failure to report immediately may result in patient safety risks and disciplinary action.

*Sources: NIS2 Directive (EU) 2022/2555; GDPR (EU) 2016/679; ISO/IEC 27001:2022 Controls 5.24–5.28; AGID Linee Guida per la Sicurezza Informatica nella PA; D.Lgs. 196/2003 as amended by D.Lgs. 101/2018.*
</policy>
