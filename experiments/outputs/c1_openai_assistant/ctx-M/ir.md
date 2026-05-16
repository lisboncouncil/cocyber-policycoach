---
config: C1
context_id: ctx-M
policy_id: P4
policy_name: Incident Response Policy
policy_short: ir
metadata:
  config: C1
  model: gpt-4.1
  input_tokens: 6612
  output_tokens: 3523
  total_tokens: 10135
  latency_s: 35.044
  tool_calls: []
  raw_provider_id: run_gtrXv48s1jCKju9gqCpeFuW7
  run_status: completed
  thread_id: thread_AaeDcdzytzsNvwIf1WIcWGW2
sources_count: 0
sources: []
prompt_chars: 6045
answer_chars: 16056
generated_at_unix: 1778086490
---

<policy title="Incident Response Policy">

---

## POLICY HEADER BLOCK

**Organization:** NATO Multinational Military Detachment, Romania  
**Effective Date:** [Insert Effective Date]  
**Policy Owner:** Information Systems Security Manager (ISSM), J6  
**Review Cycle:** Annual (or mission/operational event-driven update)

---

## 1. PURPOSE

This Incident Response Policy establishes the framework for structured detection, management, containment, and resolution of cybersecurity incidents affecting the NATO Multinational Military Detachment in Romania. The policy ensures effective incident handling to protect classified/unclassified CIS and information assets, maintain operational integrity, and comply with NATO Information Security Policy (C-M(2002)49), Romanian Cybersecurity Law (Law 58/2019/NIS2), GDPR (for civilian/contractor data), Allied Joint Doctrine for Cyberspace Operations (AJP-3.20), NIST CSF 2.0, and ISO/IEC 27001:2022 controls.

---

## 2. SCOPE

This policy applies to:
- All NATO and framework-nation military personnel assigned to the detachment
- NATO civilian staff and cleared contractors on-site or remote
- Contractors/vendors with access to CIS infrastructure
- All information systems, networks, and assets across NU/NR/NS/MISSION SECRET domains
- Implemented Cross Domain Solutions (CDS), SCIFs, and COMSEC equipment
- Information/data within the NATO, host-nation, bilateral/multilateral, or coalition regulatory regimes
- Physical and cyber-physical environments within compound control or boundary
- Any incident impacting mission command, network, or information security at the detachment

---

## 3. ROLES AND RESPONSIBILITIES

### 3.1 ISSM (Information Systems Security Manager)
- Overall responsibility and incident authority per J6 chain and NATO SOPs
- Maintains and updates IR procedures; reports to detachment command and NCIRC
- Approves IR plans; coordinates after-action reviews

### 3.2 Security Operations Center (SOC) Staff
- 24/7 first-line monitoring, triage, containment, and escalation of detected incidents
- Documents all alerts and response actions in accordance with NATO and host-nation processes
- Coordinates with ISSM, NCSC (host nation), and NCIRC

### 3.3 Command Leadership (Detachment / J6)
- Provides operational authority for incident containment decisions (incl. network segmentation, isolation)
- Marshals resources for major incident response
- Ensures operational continuity in case of severe incident impact

### 3.4 Information Owners/System Administrators
- Ensure IR procedures are implemented within assigned CIS and assets
- Participate in reviews, data collection for post-incident analysis
- Immediately isolate/report affected systems when notified

### 3.5 All Users (Military, Civilian, Contractor)
- Promptly report any suspected or confirmed security incidents through designated channels
- Follow guidance provided during ongoing incidents
- Complete required incident response training and acknowledge responsibilities

---

## 4. POLICY PRINCIPLES

### 4.1 Rapid Detection and Containment
All incidents must be identified, analyzed, and contained as rapidly as possible to minimize mission impact and information compromise (ref. ISO 27001 A.5.25, NATO AJP-3.20).

### 4.2 Defence in Depth
Responses utilize technological, administrative, and physical controls across all network domains to address layered threats, including state-sponsored and insider threats.

### 4.3 Classification Integrity
Incident handling rigorously maintains separation and non-spillage between NU/NR/NS/SECRET domains, enforcing need-to-know and ORCON principles at all response stages.

### 4.4 Legal and Regulatory Compliance
All activities comply with NATO policy, host-nation law, bilateral/multilateral agreements, and GDPR where applicable to data subject rights (ref. GDPR Articles 33/34, Law 58/2019).

### 4.5 Documentation and Auditability
Every incident response action must be logged, time-stamped, and retained to ensure traceability, legal defensibility, and process improvement.

---

## 5. POLICY REQUIREMENTS

### 5.1 Detection and Reporting

**Requirement:**  
- All users, upon detecting or suspecting a potential incident, must immediately report via secured channels (SOC hotline, incident report form, or classified means per domain).

**Process:**  
1. User reports incident to SOC or direct supervisor.
2. SOC logs and acknowledges report within 10 minutes.
3. ISSM is alerted for any incident exceeding minor severity or involving classified domains.

**Controls:**  
- Automated monitoring on all domain perimeters (SIEM, IDS/IPS)
- Mandatory reporting forms
- Secure communications for classified reporting

**Reference:** ISO 27001 A.5.24, NIST CSF DE.AE-1, C-M(2002)49, AJP-3.20

### 5.2 Incident Classification and Triage

**Requirement:**  
- SOC/classified IR team classifies each incident by confidentiality, integrity, and availability impact; applies NATO/host-nation severity scales.

**Process:**  
1. Initial assessment by SOC within 30 minutes.
2. Major/critical or cross-domain incidents immediately escalated to ISSM, NCIRC, NCSC.
3. Documentation of all steps and classification decision.

**Controls:**  
- Incident classification guidance (NATO/host-nation)
- Centralized incident tracker
- Pre-defined escalation matrix

**Reference:** ISO 27001 A.5.25, NIST CSF RS.AN-1, Romanian Law 58/2019 Art 18-19

### 5.3 Containment, Eradication, and Recovery

**Requirement:**  
- Rapid containment of compromised assets with minimal mission disruption while preserving evidentiary integrity.

**Process:**  
1. Isolate affected systems/networks (disconnect, segment, or power down as required).
2. Forensic snapshot capture before clean-up where possible.
3. Execute coordinated eradication and restoration steps per classification domain SOP.

**Controls:**  
- Use of accredited CDS for cross-domain incident mitigation
- Two-person integrity for systems at NR/NS/MISSION SECRET levels
- Chain-of-custody logs for forensic evidence

**Reference:** C-M(2002)49, ISO 27001 A.5.26, NIST CSF RS.CO-2, AJP-3.20

### 5.4 Communication and Notification

**Requirement:**  
- Incidents must be reported up the NATO/NCSC/NCIRC chain and, for applicable data breaches, to host-nation authorities and affected individuals in compliance with GDPR.

**Process:**  
1. Classified incident reporting is routed per NATO and SOFA procedures.
2. Civilian/contractor PII breach notifications per GDPR Arts. 33/34 (within 72 hours of knowledge of breach).
3. Internal communications coordinated through ISSM and command.

**Controls:**  
- Notification checklists integrated with IR tracker
- Checklist for reporting contents (data affected, scope, mitigation steps, contact details)

**Reference:** GDPR, Law 58/2019, ISO 27001 A.5.24

### 5.5 Recovery and Lessons Learned

**Requirement:**  
- Restoration of services to mission standard. Post-incident reviews for every major (or above) incident.

**Process:**  
1. Validate asset and data restoration to known-good state.
2. Conduct after-action review within 5 working days.
3. Update risk register, IR procedures, and related controls based on lessons learned.

**Controls:**  
- Standardized after-action review template
- Updates tracked in policy/configuration management system

**Reference:** ISO 27001 A.5.36, NIST CSF RS.IM-1, AJP-3.20

### 5.6 Forensics and Evidence Handling

**Requirement:**  
- All evidence must be preserved per NATO and host-nation legal/evidentiary standards, ensuring integrity and admissibility.

**Process:**  
1. Use two-person integrity for chain of custody.
2. Store evidence in secure containers/locations per classification.
3. Document every transfer or analysis step, using standard forms.

**Controls:**  
- Forensics SOPs and chain-of-custody forms
- Secure evidence storage with access logs

**Reference:** AC/35-D/1015, ISO 27001 A.5.26

### 5.7 Insider Threat and Counterintelligence

**Requirement:**  
- Insider incidents (espionage, unauthorized disclosure) require parallel counterintelligence response with all NATO/host-nation security entities engaged.

**Process:**  
1. Immediate SOC/ISSM notification.
2. Secure affected accounts, badge access, physical locations.
3. CI team initiates parallel investigation and reporting.

**Controls:**  
- Insider-threat indicators monitored by SOC
- Access suspension workflows
- Secure compartments for investigation

**Reference:** AC/35-D/1029, NATO C-M(2002)49 Annex C

---

## 6. MONITORING AND REVIEW

### 6.1 Monitoring

**What to monitor:**
- SIEM alert volume, incident response time, and containment time
- Quality/completeness of incident documentation
- Cross-domain transfer logs during incidents

**Frequency:** Continuous; weekly reporting to ISSM; quarterly high-level review  
**Responsible:** SOC, ISSM  
**Retention:** Audit logs retained 3 years minimum or per NATO guidance

### 6.2 Regular Reviews

- Annual tabletop exercises (minimum 6/year for mission-set validation)
- Post-incident review after every major incident.
- Policy and procedure updates upon review, major incidents, or regulatory changes

**Deliverable:** After-action review reports, annual compliance statement to detachment command

---

## 7. TRAINING AND AWARENESS

### 7.1 Mandatory Training

**All personnel (military, civilian, contractor) must complete:**
- Initial incident response training (onboarding)
- Annual refresher (minimum 4 hours focused on incident reporting, role responsibilities)
- Targeted exercises as part of the 40-hour per year training curriculum

**Training topics:**
- Security incident types and reporting
- Classification-specific incident protocols
- Forensic evidence handling
- Lessons learned from recent incidents

### 7.2 Acknowledgment

- All personnel sign annual acknowledgment of IR responsibilities
- Documentation maintained by ISSM (J6)

---

## 8. INCIDENT RESPONSE (PRACTICAL PROCESS SUMMARY)

### 8.1 Reporting

**Personnel must immediately report:**
- Actual or suspected security breach (network, physical, classified/unclassified spillage)
- Suspicious insider behavior or loss of credentials
- Suspected supply chain/CIS equipment security event

**Reporting channels:**
- Secure SOC hotline/email (classified/unclassified as required)
- Immediate supervisor or chain of command if technical means unavailable

### 8.2 Response Actions

Upon incident report:
1. Contain compromised assets (with authority proportional to domain/classification).
2. Asset owner/system admin collects relevant data/logs for initial triage.
3. ISSM/SOC initiates formal incident documentation and analysis.
4. Notify relevant external/coalition authorities if impact is cross-command or multi-domain.
5. Conduct after-action review and implement follow-up mitigations.

---

## 9. COMPLIANCE AND AUDIT

### 9.1 Regulatory Compliance

This policy supports compliance with:
- **NATO Information Security Policy (C-M(2002)49):** Security incident reporting, containment, lessons learned
- **AJP-3.20:** Allied joint doctrine for cyber operations (incident management lifecycle)
- **AC/35-D/1015 & AC/35-D/1029:** Security within NATO and personnel security for incident-related investigations
- **NIST CSF 2.0:** Identification, Protection, Detection, Response, Recovery functions
- **ISO/IEC 27001:2022:** A.5.24–A.5.34 (incident management)
- **Romanian Law 58/2019/NIS2:** National incident reporting and response, PII breach notification
- **GDPR:** Breach reporting and notification for personal data of EU civilian/contractor staff

### 9.2 Policy Review

- This policy and supporting playbooks are reviewed annually and after major incidents by the ISSM with command oversight.
- Updates occur upon regulatory, mission, or threat changes
- All changes are communicated to staff via command communications

### 9.3 Audit Rights

- Regular internal/external audits per NATO, ISSM, and host-nation authority direction
- Audit findings are tracked, with remediation deadlines and owner assignment

---

## 10. ENFORCEMENT

### 10.1 Policy Violations

**Violations may result in:**
- Verbal/written warnings (minor reporting failures)
- Removal from sensitive duties
- Suspension or termination of access/privileges
- Subject to military/UCMJ, NATO, or host-nation legal action

**Examples:**
- Failure to report a security incident: moderate
- Intentional destruction or alteration of incident evidence: severe
- Unauthorized cross-domain communication/disclosure: severe

### 10.2 Documentation

- All violations and response actions are documented and retained in a centralized repository with restricted access per classification

---

## 11. EXCEPTIONS

### 11.1 Exception Process

- Exception requests must be submitted in writing to the ISSM, with rationale and compensating controls identified
- Approval is by ISSM and detachment command
- Maximum validity is 90 days unless extended by review
- All exceptions reviewed quarterly

### 11.2 Emergency Access

- "Break-glass" incidents (critical mission or life-threatening) must be documented and reviewed within 24 hours post-facto
- SOC logs all emergency actions for audit review

---

## APPENDICES

### Appendix A: Definitions

**Incident:** An event or suspected event posing a threat to confidentiality, integrity, or availability of CIS or information assets  
**SOC:** Security Operations Center  
**ISSM:** Information Systems Security Manager  
**CDS:** Cross-Domain Solution  
**SCIF:** Sensitive Compartmented Information Facility  
**NCIRC:** NATO Computer Incident Response Capability  
**NCSC:** National Cyber Security Centre (host nation)  
**PII:** Personally Identifiable Information  
**CI:** Counterintelligence

### Appendix B: Forms and Templates

- Incident report form (classified/unclassified variants)  
- Chain-of-custody form  
- After-action review checklist  
- Exception request template

### Appendix C: Contact Information

- ISSM (J6): [contact, secured line/email]
- SOC Hotline: [classified/unclassified numbers]
- NCIRC Liaison: [contact]
- NCSC (host nation): [contact, notification protocol]

### Appendix D: Technical Controls

- SIEM/IDS/IPS configuration requirements  
- CDS incident isolation settings  
- Forensics toolkits authorized for each domain/classification

---

## DOCUMENT CONTROL

### Version History Table

| Version | Date         | Author    | Changes                         |
|---------|--------------|-----------|---------------------------------|
| 1.0     | [Insert Date]| ISSM/J6   | Initial issue                   |

---

### Approval Block

**Policy Approved By:**

Detachment Commander (Operational Authority): _______________ Date: _______________

ISSM (Policy Owner): _______________ Date: _______________

Host-Nation Cyber Liaison: _______________ Date: _______________

---

## REFERENCES AND SOURCES

This policy was developed based on the following frameworks, regulations, and standards:

*NATO Information Security Policy (C-M(2002)49):*  
- Security incident management, logging, reporting, containment, and lessons learned

*Allied Joint Doctrine for Cyberspace Operations (AJP-3.20):*  
- End-to-end incident management, cross-command/coalition integration

*AC/35-D/1015, AC/35-D/1029:*  
- Physical/personnel security and investigative requirements

*NATO Cyber Defence Pledge (2016):*  
- Minimum requirements for allied cyber defence posture

*NIST Cybersecurity Framework (CSF) 2.0:*  
- Functions/respond category, detection, and recovery controls

*ISO/IEC 27001:2022:*  
- A.5.24–A.5.36 (information security incident management requirements)

*Romanian Law 58/2019:*  
- Cyber incident notification, NIS2 directives

*GDPR, Arts. 33/34:*  
- Breach notification to authorities and data subjects

*Host-nation SOFA, bilateral/multilateral agreements:*  
- Legal authority and data sharing constraints

*Additional resources:*  
- NATO NCIRC and NCSC operational guidelines  
- Vendor secure SOC/SIEM/forensics documentation

---

</policy>
