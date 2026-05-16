---
config: C2
context_id: ctx-M
policy_id: P4
policy_name: Incident Response Policy
policy_short: ir
metadata:
  config: C2
  model: moonshotai/Kimi-K2.5
  input_tokens: 25725
  output_tokens: 5988
  total_tokens: 31713
  latency_s: 32.267
  tool_calls:
  - rag_retrieval
  raw_provider_id: 64eeba1b-58c2-462a-9e2f-751b5b32a114
  chunks_retrieved: 5
  server_version: 1.3.4
sources_count: 4
sources:
- type: kb_source
  source: ./datadir-plus-templates/15.json
  title: 'National CERT/CSIRT: Mandate and Organisation paper'
- type: kb_source
  source: ./datadir-plus-templates/9.json
  title: 'The Sector CSIRT Framework: Developing Sector-Based Incident Response Capabilities'
- type: kb_source
  source: ./datadir-plus-templates/cyber_incident_response_plan.docx
  title: ./datadir-plus-templates/cyber_incident_response_plan.docx
- type: kb_source
  source: ./datadir-plus-templates/5.json
  title: Cyber Rapid Response Teams​
prompt_chars: 6045
answer_chars: 17660
generated_at_unix: 1778086876
---

 <policy title="Cyber Incident Response Policy">

| Field | Value |
|---|---|
| **Document ID** | J6-POL-008 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | NATO RESTRICTED |
| **Owner** | Information Systems Security Manager (ISSM) |
| **Approved by** | Commander, [Unit Designation], SHAPE Operational Control |
| **Approval date** | [DD/MM/YYYY] |
| **Next review date** | [DD/MM/YYYY] |
| **Review cycle** | Annual (and after any significant incident or exercise) |

---

## 1. Purpose and Objectives

This Cyber Incident Response Policy (CIRP) establishes the framework for detecting, reporting, assessing, and responding to cyber incidents affecting the Communications and Information Systems (CIS) and classified information of [Unit Designation], operating under NATO Allied Command Operations (SHAPE). The policy ensures rapid restoration of mission-critical capabilities, protection of NATO classified information (NU/NR/NS/MISSION SECRET), and compliance with NATO Information Security Policy, host-nation cybersecurity obligations, and applicable coalition agreements.

### 1.1 Objectives

- Provide structured procedures for incident response across all classification domains (NU, NR, NS, MISSION SECRET) in accordance with NATO CIRC (NCIRC) processes.
- Define roles, responsibilities, and command authority for incident response within a multinational military detachment of 2,000 personnel.
- Ensure compliance with NATO Information Security Policy (C-M(2002)49), AC/322-D(2017)0009 (NATO INFOSEC Technical Directive), Romanian Cybersecurity Law 58/2019 (NIS2 transposition), and GDPR (EU) 2016/679 for civilian/contractor data.
- Establish reporting channels to NCIRC, host-nation CERT (CERT-RO), and national authorities per bilateral agreements and NATO Status of Forces Agreement (SOFA).
- Maintain operational readiness through mandatory annual testing aligned with 6 yearly exercises and 2 red-team engagements.

*Sources: NATO C-M(2002)49; AC/322-D(2017)0009; AJP-3.20 (Allied Joint Doctrine for Cyberspace Operations); ISO/IEC 27001:2022 A.5.24-A.5.28*

---

## 2. Scope

This policy applies to:

- All cyber incidents affecting information systems, networks, and data across the four classification domains: NATO UNCLASSIFIED (NU), NATO RESTRICTED (NR), NATO SECRET (NS), and MISSION SECRET.
- All personnel: 1,500 military active duty, 200 civilian NATO staff, and 300 cleared contractors.
- All CIS assets including 1,200 classified workstations, 800 unclassified workstations, COMSEC equipment, cross-domain solutions (CDS), and TEMPEST-rated SCIF infrastructure.
- All network boundaries, including connections to NATO Mission Networks, coalition partner networks, and the 24/7 Theatre SOC.
- Third-party and supply-chain incidents affecting NATO-approved equipment lists or COMSEC key management.

*Source: AC/35-D/1015 (Security within NATO); AC/322-D(2017)0009*

---

## 3. Standards and Frameworks

This policy aligns with:

- **NATO Policy:** C-M(2002)49 (Information Security Policy), AC/322-D(2017)0009 (INFOSEC Technical Directive), AJP-3.20 (Allied Joint Doctrine for Cyberspace Operations), NATO Cyber Defence Pledge 2016.
- **Host-Nation Law:** Romanian Cybersecurity Law 58/2019 (transposing NIS Directive and NIS2), GDPR (EU) 2016/679.
- **International Standards:** ISO/IEC 27001:2022 (Information Security Incident Management), NIST Cybersecurity Framework 2.0 (Functions: IR, RS).
- **Coalition Frameworks:** Bilateral/multilateral information-sharing agreements and ORCON (Originator Control) restrictions.

---

## 4. Definitions and Terminology

| Term | Definition |
|---|---|
| **CIRT** | Cyber Incident Response Team — the operational team managing incidents within the detachment. |
| **NCIRC** | NATO Computer Incident Response Centre — the central NATO authority for cyber incident coordination. |
| **COMSEC** | Communications Security — measures protecting classified communications (cryptographic keys, equipment). |
| **Spillage** | Unauthorized transfer of classified information to lower classification domains or unclassified systems. |
| **TEMPEST** | Investigation and study of compromising emanations from electronic equipment (unintended signal leakage). |
| **CDS** | Cross-Domain Solution — accredited systems allowing controlled data transfer between classification domains. |
| **ORCON** | Originator Control — restriction on further dissemination of shared intelligence products. |
| **APT** | Advanced Persistent Threat — sophisticated, state-sponsored adversary with long-term presence. |
| **ISSM** | Information Systems Security Manager — full-time security lead under J6 chain of command. |
| **SCIF** | Sensitive Compartmented Information Facility — TEMPEST-rated secure area for NS and above. |

---

## 5. Threat Vectors and Incident Types

### 5.1 Priority Threat Vectors
Based on the operational threat profile:
- **State-sponsored APT:** Russia-aligned and China-aligned actors targeting NATO operational planning.
- **Insider Threat:** Cleared personnel or contractors with access to NS/MISSION SECRET systems (counterintelligence priority).
- **Supply Chain:** Compromise of NATO-approved COMSEC or CIS equipment during procurement or maintenance.
- **TEMPEST:** Exploitation of electromagnetic emanations from SCIF or high-grade equipment.
- **HUMINT Recruitment:** Targeting of cleared personnel by hostile intelligence services.
- **Spillage:** Accidental or adversarial crossing of classification boundaries (e.g., via CDS misuse).
- **Kinetic-Cyber Convergence:** Cyber attacks supporting or accompanying physical threats in regional contingency.

### 5.2 Incident Classification Matrix

| Severity | Criteria | Examples | Response SLA |
|---|---|---|---|
| **Critical** | Active compromise of NS/CTS; APT presence; COMSEC compromise; kinetic-cyber attack | Unauthorized access to NS network; confirmed key compromise; TEMPEST penetration | Immediate (< 1 hour) |
| **High** | NR compromise; insider threat indicators; successful phishing with data exfiltration; spillage to NU | Malware on NR workstation; unauthorized data transfer attempt; suspected insider activity | < 4 hours |
| **Medium** | NU breach; malware without data loss; policy violations affecting availability | Ransomware on administrative network; DDoS affecting logistics systems | < 24 hours |
| **Low** | Attempted attacks; minor policy violations; blocked malware | Port scans; failed phishing attempts | < 72 hours |

*Source: NATO CIRC Classification Guidelines; NIST CSF 2.0 IR.4*

---

## 6. Incident Response Process

### Phase 1 — Preparation
- The ISSM maintains this CIRP, contact rosters (including NCIRC and CERT-RO), and forensic toolkits.
- All 25 FTE security staff maintain 40 hours annual training including incident response, forensics, and NATO CIRC procedures.
- The 24/7 Theatre SOC maintains sensors at every domain boundary (NU/NR/NS/MISSION SECRET) with automated alerting to the CIRT.
- **Annual Testing:** Tabletop exercises (6/year) and red-team engagements (2/year) validate response capabilities per NATO exercise schedules.

*Source: ISO/IEC 27001:2022 A.5.24; AC/322-D(2017)0009*

### Phase 2 — Detection and Reporting
- **Detection:** Automated (SOC sensors, IDS/IPS at domain boundaries, COMSEC tamper alarms, TEMPEST monitoring) or manual (user reports, intelligence tips).
- **Immediate Actions:** Isolate affected systems using domain-specific isolation procedures (do not disconnect NS systems from NU without CDS protocol).
- **Reporting Chain:**
  1. **Immediate:** Notify ISSM and J6 (CIS Operations).
  2. **Within 1 hour:** Report to NCIRC for all Critical/High incidents (per NATO CIRC requirements).
  3. **Within 4 hours:** Notify host-nation CERT (CERT-RO) for incidents involving civilian personal data under Romanian Law 58/2019.
  4. **Within 72 hours (GDPR):** If personal data of EU civilians/contractors is breached, notify the Romanian Data Protection Authority (ANSPDCP) per GDPR Article 33, unless SOFA limitations apply (coordinate with Legal Advisor).

*Source: NATO CIRC Operating Procedures; Romanian Law 58/2019 Art. 25; GDPR Art. 33*

### Phase 3 — Classification and Triage
- The ISSM classifies incidents using the matrix in Section 5.2.
- **Counterintelligence Involvement:** All suspected insider threats, HUMINT, or TEMPEST incidents require immediate notification to the Security Officer (counterintelligence) and potential involvement of national security services under bilateral agreements.
- **Legal Review:** Legal Advisor assesses SOFA implications, GDPR notification requirements, and coalition agreement restrictions before external sharing.

### Phase 4 — Containment
- **Short-term:** Isolate affected classification domains (e.g., disconnect compromised NR segment from NS CDS). Preserve COMSEC material under two-person integrity.
- **Long-term:** Implement domain-specific network segmentation, revoke compromised PKI certificates (smart cards), and activate backup communication paths.
- **Spillage Response:** Immediately halt CDS transfers; conduct damage assessment for classified data exposure; initiate formal spillage reporting to NATO security authorities (AC/35-D/1015).

*Source: AC/322-D(2017)0009 (Containment Procedures)*

### Phase 5 — Eradication
- Remove root cause: Reimage compromised workstations using gold images; replace compromised COMSEC keys under national COMSEC authority; remove unauthorized accounts.
- **APT Specific:** Full forensic imaging of affected systems before eradication for attribution analysis (coordinate with NCIRC).

### Phase 6 — Recovery
- Restore from verified clean backups per Backup and Recovery Policy (RTO/RPO defined per classification level).
- **COMSEC Recovery:** Re-key all affected circuits using NATO-approved key management procedures; verify TEMPEST compliance before returning SCIF to operational status.
- Validate system integrity before reconnecting to NATO Mission Networks.

### Phase 7 — Post-Incident Review
- Conduct review within **5 business days** for Critical/High incidents; **15 business days** for Medium/Low.
- Document: timeline, root cause (including supply chain analysis if applicable), effectiveness of response, lessons learned.
- **Reporting:** Submit final report to NCIRC, contributing nations (if multinational assets involved), and SHAPE J6.
- **Improvement:** Update controls based on red-team findings; incorporate lessons into the 40-hour annual training curriculum.

*Source: ISO/IEC 27001:2022 A.5.27; NIST CSF 2.0 IR.6*

---

## 7. Roles and Responsibilities

### 7.1 Cyber Incident Response Team (CIRT)

| Role | Responsibility | Authority |
|---|---|---|
| **CIRT Lead (ISSM)** | Overall incident coordination; NCIRC liaison; policy enforcement; external reporting decisions | Authority to isolate classification domains; approve exception requests |
| **J6 (CIS Operations)** | Technical containment, eradication, recovery; system restoration; network isolation execution | Authority to disconnect network segments; manage COMSEC re-keying |
| **Security Officer** | Counterintelligence aspects; insider threat investigation; HUMINT/TEMPEST incidents; law enforcement liaison | Authority to suspend clearances; initiate security investigations |
| **Legal Advisor** | SOFA interpretation; GDPR/NIS2 compliance; coalition agreement restrictions; evidence handling for legal proceedings | Authority to approve external notifications; invoke legal privilege |
| **Contractor Security Officer** | Incident response for contractor-managed systems; personnel security for 300 cleared contractors | Authority to revoke contractor access |

### 7.2 External Coordination
- **NCIRC:** Central coordination for NATO-wide threats; technical analysis support; dissemination of indicators of compromise (IOCs).
- **CERT-RO:** Host-nation coordination for incidents affecting Romanian infrastructure or civilian data.
- **National CSIRTs:** Contributing nations' CSIRTs for incidents affecting their national networks or personnel.

---

## 8. Communications

### 8.1 Principles
- **Need-to-Know:** Information shared only with personnel holding appropriate clearance and mission need.
- **ORCON:** Respect originator control markings on shared intelligence products; seek approval before further dissemination.
- **Secure Channels:** Use NATO SECRET or higher communication systems for incident details involving NS/MISSION SECRET; avoid unencrypted commercial channels.

### 8.2 Stakeholder Matrix

| Stakeholder | Channel | Trigger |
|---|---|---|
| NCIRC | Secure NATO network (NSANet) or classified fax | All Critical/High incidents; APT activity |
| SHAPE J6 / ACO | Operational reporting chain | Mission-impacting incidents |
| Host-Nation (Romania) | CERT-RO secure portal; diplomatic channels | Incidents affecting civilian data or national infrastructure |
| Contributing Nations | Bilateral secure channels | Incidents involving national assets or personnel |
| Affected Personnel | Secure briefing (SCIF for NS/SECRET) | Confirmed compromise of personal data or clearance status |

*Source: NATO CIRC Communication Protocols; GDPR Art. 34 (data subject notification)*

---

## 9. Evidence Preservation and Forensics

- **Chain of Custody:** Maintain tamper-evident logs for all forensic evidence; use NATO-approved forensic tools; document all access to evidence.
- **Classification:** Forensic images of NS systems retain NS classification; store in accredited SCIF.
- **Legal Admissibility:** Follow Romanian criminal procedure code (where applicable under SOFA) and NATO administrative procedures for evidence handling.
- **Retention:** Retain incident logs and forensic data for minimum **12 months** (Critical incidents: **7 years** or as required by national authorities).

*Source: AC/35-D/1015 (Security Investigations); ISO/IEC 27001:2022 A.5.28*

---

## 10. Testing and Exercises

- **Frequency:** Minimum 6 exercises per year (as per resource envelope), including at least 1 full-scale exercise involving NCIRC and host-nation CERT.
- **Red Team:** 2 annual red-team engagements authorized by Commander; scope includes APT simulation, insider threat scenarios, and TEMPEST testing.
- **Validation:** Verify 24/7 SOC contact procedures, COMSEC emergency re-keying, and CDS failover capabilities.
- **After-Action Reviews:** Document gaps; update CIRP within 30 days of significant exercise findings.

*Source: AJP-3.20 (Training Requirements); NIST CSF 2.0 IR.9*

---

## 11. Exceptions

Exceptions to response timelines or containment procedures (e.g., operational necessity to maintain connectivity during active incident) require:

1. Written justification by J6 with mission impact assessment.
2. Compensating controls (e.g., enhanced monitoring, manual logging).
3. Approval by ISSM and Commander.
4. Notification to NCIRC of delayed containment actions.
5. Maximum validity: **72 hours** (renewable with SHAPE approval for operational exigencies).

*Source: NATO CIRC Exception Procedures; ISO/IEC 27001:2022 A.5.24*

---

## 12. Enforcement

Violations of this policy, including failure to report incidents, deliberate destruction of evidence, or unauthorized disclosure of incident details (ORCON violations), may result in:

- **Military Personnel:** Disciplinary action under national military justice codes and NATO administrative procedures.
- **Civilian Staff:** Administrative sanctions per NATO International Civilian Staff Regulations.
- **Contractors:** Immediate termination of contract; revocation of security clearance; financial penalties; referral to host-nation authorities under SOFA Article VII.

*Source: AC/35-D/1029 (Personnel Security)*

---

## 13. Related Documents

| Document ID | Title |
|---|---|
| C-M(2002)49 | NATO Information Security Policy |
| AC/322-D(2017)0009 | NATO INFOSEC Technical and Implementation Directive |
| AC/35-D/1015 | Security within NATO |
| AC/35-D/1029 | Personnel Security |
| AJP-3.20 | Allied Joint Doctrine for Cyberspace Operations |
| Law 58/2019 | Romanian Cybersecurity Law (NIS2 Transposition) |
| GDPR (EU) 2016/679 | General Data Protection Regulation |
| J6-POL-002 | Access Control Policy (Classification Domains) |
| J6-POL-003 | Asset Management Policy (COMSEC and CIS) |
| J6-POL-004 | Backup and Recovery Policy |
| J6-POL-005 | Network Security Policy (Domain Segregation) |

---

## 14. Compliance and Regulatory References

- **NATO C-M(2002)49** — Information Security Policy (Incident Response Coordination)
- **AC/322-D(2017)0009** — Technical Directive (Incident Handling Procedures)
- **ISO/IEC 27001:2022** — A.5.24 (Information Security Incident Management Planning and Preparation), A.5.25 (Assessment and Decision), A.5.26 (Response to Information Security Incidents), A.5.27 (Learning from Information Security Incidents), A.5.28 (Collection of Evidence)
- **NIST CSF 2.0** — Function IR (Incident Response), RS (Response Sharing)
- **Romanian Law 58/2019** — Article 25 (Incident Reporting to CERT-RO)
- **NIS2 Directive (EU) 2022/2555** — Article 23 (Incident Reporting)
- **GDPR (EU) 2016/679** — Article 33 (Notification of Personal Data Breaches), Article 34 (Communication to Data Subjects)

---

## 15. Revision History

| Version | Date | Author | Description of Change |
|---|---|---|---|
| 1.0 | [DD/MM/YYYY] | ISSM / J6 | Initial release for multinational detachment |

---

## 16. Approval

| Role | Name | Signature | Date |
|---|---|---|---|
| Policy Owner (ISSM) | | | |
| Approved by (Commander) | | | |
| Legal Review (SOFA/GDPR) | | | |
| Security Officer (CI) | | | |

</policy>
