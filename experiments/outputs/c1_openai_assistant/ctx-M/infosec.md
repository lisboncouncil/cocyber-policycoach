---
config: C1
context_id: ctx-M
policy_id: P5
policy_name: General Cybersecurity Policy
policy_short: infosec
metadata:
  config: C1
  model: gpt-4.1
  input_tokens: 6614
  output_tokens: 3887
  total_tokens: 10501
  latency_s: 64.665
  tool_calls: []
  raw_provider_id: run_kPeYVDsibBuKIEx1lKzdcBVe
  run_status: completed
  thread_id: thread_JJLWBUNHJxEbEYJeDxEzBJfj
sources_count: 0
sources: []
prompt_chars: 6053
answer_chars: 17222
generated_at_unix: 1778086555
---

<policy title="General Cybersecurity Policy for NATO Multinational Military Detachment (Romania)">
  
---
  
## POLICY HEADER BLOCK

**Organization:** NATO Multinational Military Detachment (Romania), under Allied Command Operations (SHAPE)  
**Effective Date:** [To be assigned—suggest current year]  
**Policy Owner:** Information Systems Security Manager (ISSM, J6)  
**Review Cycle:** Annual, or sooner upon significant mission or threat changes  
  
---
  
## 1. PURPOSE

This General Cybersecurity Policy establishes the governance framework, roles, principles, and specific requirements underpinning the protection of NATO and coalition mission information systems under the operational control of Allied Command Operations and deployed to Romania. It ensures assurance, confidentiality, integrity, and availability of mission-critical assets and data, and enforces compliance with NATO and host-nation security policy (including C-M(2002)49, AC/35-D/1015, AC/322-D(2017)0009, Romanian Law 58/2019 / NIS2, GDPR, and ISO/IEC 27001:2022), aligned with NIST CSF 2.0 and NATO Cyber Defence Pledge.

---
  
## 2. SCOPE

This policy applies to:
- All assigned and attached personnel: NATO military members, civilian staff, and cleared contractors.
- All systems, networks, and data handled within the Detachment, including:
  - NATO UNCLASSIFIED (NU), NATO RESTRICTED (NR), NATO SECRET (NS), and MISSION SECRET domains.
  - Communications and Information Systems (CIS), COMSEC devices, and supporting infrastructure.
  - Physical locations under Detachment operational control, including SCIFs, field nodes, and coalition-integrated sites.
  - All temporary or exercise deployments, and remote access to Detachment IT resources.
  - All vendors and third-party entities providing goods or services within mission scope.
- All data, including NATO classified information, personal data (including GDPR-covered), signals intelligence, operational orders, and system telemetry.
- All information processed, stored, or transmitted in support of mission set operations.

---
  
## 3. ROLES AND RESPONSIBILITIES

### 3.1 Detachment Command Authority / S6-J6
- Accountable for implementation and enforcement of cybersecurity policies.
- Approves resourcing, policy exceptions, and major incident escalation.
- Oversees compliance with NATO, host-nation, and coalition frameworks.

### 3.2 Information Systems Security Manager (ISSM, J6)
- Daily owner for all IS security program elements.
- Maintains policy artifacts, controls updates, and executes compliance reviews.
- Coordinates incident response per NCIRC and NCSC/CERT reporting standards.
- Ensures adequate staff training, asset inventory, and governance structure.
  
### 3.3 Information Security Staff (FTE Team)
- Operate technical controls, monitor SOC sensors, and administer PKI and access.
- Conduct threat analysis, vulnerability assessments, red-team/blue-team support.
- Ensure operational and technical compliance in all classification domains.
  
### 3.4 All Users (Military, Civilian Staff, Contractors)
- Comply with this and all supporting security policies at all times.
- Report suspected or confirmed incidents without delay.
- Complete mandatory training and exercise operational discipline.

### 3.5 COMSEC Custodian
- Administer NATO-approved key material handling; enforce two-person integrity.
- Maintain full auditable records per AC/322-D(2017)0009 and national authority.

### 3.6 Host Nation and Contractor Liaisons
- Ensure vendors and third parties comply with applicable host-nation (GDPR, CSL) and NATO security regimes.

---
  
## 4. POLICY PRINCIPLES

### 4.1 Defense in Depth (C-M(2002)49, NIST CSF ID.AM, ISO/IEC 27001:2022 6.1.3)
Layered technical, physical, and procedural controls will be deployed across all mission assets, enforcing security at each boundary—network, system, application, and data.

### 4.2 Need-to-Know and Originator Control (ORCON) (NATO classification policy, C-M(2002)49)
All access to classified or restricted systems and information must be role-based, strictly enforced per need-to-know and ORCON markings; unauthorized disclosure or over-provisioning is a major violation.

### 4.3 Zero Trust for Mission Domains (NIST CSF PR.AC, ISO/IEC 27001:2022 9.1-9.4)
Access and transactions are always authenticated, authorized, and logged, independent of network location or user clearance alone.

### 4.4 Multinational Interoperability by Secure Design
Controls and operational processes will be compatible with NATO tech directives, coalition frameworks, and national-origin security overlays; solutions will enable but not compromise interoperability.

### 4.5 Legal and Regulatory Conformance (AC/35-D/1015; Romanian Law 58/2019/NIS2; GDPR)
Controls will be mapped to—and must not fall below—legal and regulatory minimums in force for both NATO and host-nation authorities, including relevant limitations per Status of Forces Agreement.

---
  
## 5. POLICY REQUIREMENTS

### 5.1 Access Control and Authentication  
- All accounts will be uniquely identified and provisioned per user, leveraging PKI-based smart cards (CAC equivalent) for all access above NU.
  - Reference: ISO/IEC 27001:2022 9.2, NATO AC/322-D(2017)0009, NIST CSF PR.AC-1.
- Separation of domains (NU, NR, NS, MISSION SECRET) will be technically and administratively enforced; no automated cross-domain access is permitted except via NATO-accredited cross-domain solutions (CDS) with documented procedures.
  - Reference: C-M(2002)49, AC/322-D(2017)0009, NATO ACO SOPs.
- Default-deny on all access unless explicitly granted per operational role and clearance.
  - Reference: NIST CSF PR.AC-4.

### 5.2 Asset Management and Protection  
- Maintain and annually review a complete, classification-tagged inventory of all workstations, CIS devices, COMSEC equipment, data types, and media.
  - Reference: ISO/IEC 27001:2022 8.1, NIST CSF ID.AM-1.
- Physical asset controls include labeling, custody assignment, and tracking per NATO and host-nation guidelines.

### 5.3 Classification Handling and Information Lifecycle  
- Data and information must be labeled and handled per NATO and coalition classification policies.
  - Reference: C-M(2002)49, AC/35-D/1015.
- Transfers between domains must employ NATO-accredited CDS solutions, with manual review for any up-transfer; all data movement logged and auditable.
  - Reference: AC/322-D(2017)0009.
- Erasure and disposal processes for IT assets must conform to the highest classification held, including NIST-compliant sanitization for SECRET and above.
  - Reference: ISO/IEC 27001:2022 11.2.

### 5.4 COMSEC and Key Management  
- All COMSEC keying material is managed under national authority, with auditable two-person integrity for all SECRET and above levels.
  - Reference: AC/322-D(2017)0009, national COMSEC doctrine.
- Strict chain-of-custody procedures are enforced for the lifecycle of key material, including destruction.

### 5.5 Network Defence and Boundary Protection  
- 24/7 monitoring using deployment-level Security Operations Center (SOC), with sensors at all network boundaries (NU, NR, NS, MISSION SECRET).
  - Reference: NIST CSF DE.CM, ISO/IEC 27001:2022 6.1.2, C-M(2002)49.
- All remote/field deployments provisioned with NATO-approved encrypted communications.
- Regular vulnerability assessments, red-team exercises, and hardening according to theatre and NATO directives.
  - Reference: NIST CSF PR.IP-12, NATO Cyber Defence Pledge.

### 5.6 Incident Response  
- Incidents are detected, reported, contained, and remediated following the Detachment IR Plan, aligned to NCIRC, NCSC, and host-nation CERT guidance.
  - Reference: NIST CSF RS, C-M(2002)49, ISO/IEC 27001:2022 6.1/Annex A.16.
- All security events are logged, and major incidents are reported up the NATO command chain and to host nation authorities as required.

### 5.7 Personnel Security and Training  
- All personnel (military, civilian, contractor) must be screened for at least the level required by their access (per AC/35-D/1029).
- Annual minimum of 40 hours of cyber/information security training per staff member.
  - Reference: ISO/IEC 27001:2022 7.2, AC/322-D(2017)0009.
- Threat awareness, incident reporting, OPSEC, and cross-domain hygiene are mandatory curricular components.

### 5.8 Supply Chain and Vendor Controls  
- Only NATO-approved vendors and hardware permitted; all host-nation contractors/venders undergo security vetting per host CSL and NATO protocols.
  - Reference: NIST CSF ID.SC, AC/322-D(2017)0009.
- Contracts must mandate adherence to this policy and allow for audit by NATO or its agents.

### 5.9 Physical and TEMPEST Security  
- All NS and MISSION SECRET processing and storage must occur in approved SCIF zones; regular reviews of TEMPEST compliance are mandatory.
  - Reference: C-M(2002)49, NATO TEMPEST policy.

### 5.10 Data Privacy and Legal Compliance  
- Processing of personal data about civilian staff or contractors must comply with GDPR, with technical protections separating operational and HR/personnel domains.
  - Reference: GDPR Articles 5/32, ISO/IEC 27001:2022 A.18.
- SOFA provisions take precedence where NATO immunities or status apply.

---

## 6. MONITORING AND REVIEW

### 6.1 Security Monitoring
**What to monitor:**
- All domain boundary events, authentication attempts, cross-domain transfers, COMSEC key usage, removable media insertion, and SOC alerts.

**Frequency:** Continuous (24/7) for network/SOC; Daily log review; Quarterly compliance audit.  
**Responsible:** ISSM, security team, SOC analysts.  
**Retention:** At least 12 months for standard logs, 24 months for classified events.

### 6.2 Regular Reviews
- Annual policy review by ISSM with input from command and all technical authorities.
- Post-exercise and after-action reviews (AAR) to update requirements.
- Compliance check following major incidents or regulatory changes.
- Tenant command or coalition partner reviews as required.

---
  
## 7. TRAINING AND AWARENESS

### 7.1 Mandatory Training
All staff must complete:
- Initial onboarding cyber/INFOSEC certification.
- Annual refresher (minimum 40 hrs/year).
- Pre- and post-deployment briefings for field operations and exercises.

Training topics:
- Classification handling
- Cross-domain hygiene
- Insider threat awareness
- Incident reporting and escalation
- Data privacy and legal obligations (GDPR/SOFA overlays)
- OPSEC/COMSEC practices

### 7.2 Acknowledgment
- Written acknowledgment of policy receipt, tracked in the staff records system.
- Recording of compliance is mandatory prior to system access.

---
  
## 8. INCIDENT RESPONSE

### 8.1 Reporting
All users must **immediately report**:
- Suspected malware or network breach.
- Loss or compromise of classified assets or COMSEC material.
- Insider threat indicators.
- Physical security breaches, including TEMPEST incidents.

Reporting channels:
- Detachment SOC primary contact (24/7)
- ISSM/J6 reporting chain
- NATO NCIRC and host-nation CERT (as required for incident type and classification)
- Escalation to command for mission-impacting events.

### 8.2 Response Actions
Upon report:
1. Immediate containment and preliminary triage by security team (within 15 minutes).
2. NCIRC notification for qualified incidents.
3. Documentation and forensic evidence collection.
4. Full incident review and recovery; after-action reporting within 48 hours.
5. Lessons-learned integration into process updates.

---
  
## 9. COMPLIANCE AND AUDIT

### 9.1 Regulatory Compliance
This policy supports compliance with:
- **NATO policy and directives:** C-M(2002)49 and successors, AC/35-D/1015, AC/322-D(2017)0009, AJP-3.20.
- **Host-nation Romanian law:** Law 58/2019 (transposing NIS/NIS2), GDPR (for personal data).
- **Civilian/international best practice:** NIST CSF 2.0, ISO/IEC 27001:2022.
- **Coalition/partner agreements:** Information-sharing MOUs; SOFA; ORCON.

### 9.2 Policy Review
- Scheduled annual review by ISSM and J6.
- Triggered review following major regulatory, command, operational, or threat changes.
- Communication of all changes to staff and contractors within one week of approval.

### 9.3 Audit Rights
- Internal audit schedule: minimum biannual technical and compliance audit.
- NATO or framework nation external audit upon request; host-nation data audit for GDPR compliance.
- Remediation for any non-compliance is due within 30 days.

---
  
## 10. ENFORCEMENT

### 10.1 Policy Violations
Violations may result in:
- Formal warning or retraining for minor lapses.
- Removal of system access or suspension for moderate violations.
- Reporting to command, legal, and security authorities for severe/intentional breaches (may include military judicial action, contract termination, referral to host nation authorities).
- Possible criminal prosecution for willful unauthorized disclosure or compromise of classified/comsec material.

**Examples:**  
- Minor: Neglecting logoff procedures in NU.  
- Moderate: Attempted unapproved cross-domain data transfer.  
- Severe: Loss or disclosure of SECRET/COMSEC material.

### 10.2 Documentation
All violations are logged, investigated, and recorded in a secure register accessible to ISSM and command; significant cases escalate to NATO security and host-nation as required.

---

## 11. EXCEPTIONS

### 11.1 Exception Process
- Exception requests must be submitted to ISSM in writing, detailing risk, mitigation, and duration.
- Approval required from ISSM, J6, and command (plus national authorities for COMSEC/SECRET and above).
- Compensating controls documented and implemented.
- Validity limited to maximum 90 days; subject to review and renewal only with command/national authority.

### 11.2 Emergency Access
- Break-glass procedures for mission-critical situations with full event logging and post-incident review mandatory.
- All emergency access to be reported and subject to after-action audit by ISSM and command.

---

## APPENDICES

### Appendix A: Definitions
**COMSEC:** Communications Security; equipment and procedures to secure official NATO/classified communications.
**ISSM:** Information Systems Security Manager; responsible for cybersecurity policy/program for the Detachment.
**SOC:** Security Operations Center; 24/7 monitoring and incident response team.
**SCIF:** Sensitive Compartmented Information Facility; accredited physical facility for SECRET or above.
**Cross-domain solution (CDS):** Approved gateway to transfer information between classified networks with controls.

### Appendix B: Forms and Templates
- Exception request form (maintained by ISSM)
- Incident report template (per NCIRC/NCSC standard)
- Access request and authorization form
- Training acknowledgment receipt

### Appendix C: Contact Information
- ISSM (J6): [Position contact email/DSN/phone]
- SOC (Theatre level): [24/7 phone, JWICS email]
- Command Duty Officer: [Contact]
- NATO NCIRC: [Contact]
- Host-nation CERT: [Contact]

### Appendix D: Technical Controls  
- PKI/Smart-card authentication config per domain
- SOC sensor baseline/alerting criteria
- Cross-domain and boundary firewall rules (per ACO SOP)
- TEMPEST countermeasures

---

## DOCUMENT CONTROL

### Version History Table

| Version | Date       | Author                | Changes                                       |
|---------|------------|-----------------------|-----------------------------------------------|
| 1.0     | [YYYY-MM-DD] | ISSM (J6)            | Initial version; full NATO/Host adaptation     |
| ...     | ...        | ...                   | ...                                           |

---

### Approval Block

**Policy Approved By:**

J6/Detachment Command: ________________ Date: ________________

ISSM: ________________ Date: ________________

Legal/Compliance/National Authority: ________________ Date: ________________

---

## REFERENCES AND SOURCES

This policy was developed using the following frameworks, regulations, and standards:

*NATO Information Security Policy (C-M(2002)49):*
- *Framework for classification, access control, incident response, and asset protection across NATO missions.*

*NATO Security Directives (AC/35-D/1015, AC/322-D(2017)0009, AC/35-D/1029):*
- *Detailed technical, personnel, and communications security requirements and procedures.*

*NATO Cyber Defence Pledge (2016), AJP-3.20 Allied Joint Doctrine for Cyberspace Operations:*
- *Operational doctrine for cyberspace defence effectiveness and alliance interoperability.*

*Romanian Law 58/2019 (transposing NIS2), GDPR (for personal data):*
- *National law for critical infrastructure and personal data protections, reflecting EU requirements.*

*NIST Cybersecurity Framework 2.0, ISO/IEC 27001:2022:*
- *Widely-recognized technical controls and best practice for access, monitoring, response, and supply chain sec.*

*SOFA (Status of Forces Agreement), coalition and bilateral MOUs:*
- *Defines legal regime for personnel, host-nation authority, and multinational information exchange.*

*Internal Detachment Governance (IR Plan, Asset Inventories, Training Schedules):*
- *Existing local practices, process documents, and technical implementations.*

---
</policy>
