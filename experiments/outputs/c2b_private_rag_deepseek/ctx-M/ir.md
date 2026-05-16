---
config: C2b
context_id: ctx-M
policy_id: P4
policy_name: Incident Response Policy
policy_short: ir
metadata:
  config: C2b
  model: deepseek-ai/DeepSeek-V3.2
  input_tokens: 26034
  output_tokens: 2014
  total_tokens: 28048
  latency_s: 42.377
  tool_calls:
  - rag_retrieval
  raw_provider_id: be82209d-1f33-4bfd-a6da-56129aace0a6
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
answer_chars: 8406
generated_at_unix: 1778503989
---

<policy title="Cyber Incident Response Policy for NATO Allied Command Operations Unit">

| Field | Value |
|-------|-------|
| **Document ID** | IRP-001 |
| **Version** | 1.0 |
| **Status** | Draft for Approval |
| **Classification** | NATO RESTRICTED (Releasable to NATO and PfP Nations) |
| **Policy Owner** | Information Systems Security Manager (ISSM) |
| **Approving Authority** | Detachment Commander |
| **Approval Date** | [Date of Approval] |
| **Next Review Date** | One year from approval date |
| **Review Cycle** | Annual, or following a major incident or significant change in threat landscape. |

---

## 1. Purpose

This Cyber Incident Response Plan (CIRP) establishes the framework and procedures for the NATO Allied Command Operations (ACO) unit to effectively detect, respond to, contain, and recover from cyber security incidents. This plan ensures a rapid, coordinated, and effective response to cyber threats, minimizing operational impact and safeguarding NATO classified and mission-critical information. It is aligned with NATO Allied Joint Doctrine for Cyberspace Operations (AJP-3.20), the NATO Information Security Policy, and host-nation (Romanian) cybersecurity law.

## 2. Scope

This policy applies to all personnel, including military, civilian, and contractor staff, with access to NATO information systems, networks, and data within the unit. It covers all classification levels (NU, NR, NS, CTS) and all information systems, including CIS, COMSEC, and mission-specific coalition systems.

## 3. Roles and Responsibilities

### 3.1. Incident Response Team (IRT) Lead (ISSM)
- **Primary:** Information Systems Security Manager (ISSM)
- **Alternate:** Deputy ISSM or Senior CIS Officer
- **Responsibilities:** Declares an incident, chairs the IRT, coordinates with external entities (NCIRC, NCSC, host-nation CERT), and has final authority on containment and remediation actions.

### 3.2. Technical Lead (CIS Security Officer)
- **Primary:** Senior CIS NCO/Warrant Officer
- **Responsibilities:** Leads technical analysis, digital forensics, and containment actions. Manages the technical IRT members.

### 3.3. Legal & Compliance Officer (LNO)
- **Primary:** Staff Judge Advocate (SJA) or designated legal advisor.
- **Responsibilities:** Ensures response actions comply with NATO SOFAs, host-nation law (Romanian Law 58/2019), GDPR for civilian staff data, and NATO information sharing agreements.

### 3.4. Public Affairs Officer (PAO)
- **Primary:** Public Affairs Officer (PAO) or designated spokesperson.
- **Responsibilities:** Manages all external and internal communications regarding the incident, in coordination with SHAPE PAO.

### 3.5. Watch Officer / 24/7 Operations Centre
- **Primary:** J6 Operations Watch
- **Responsibilities:** Initial detection, logging, and immediate notification of the ISSM/IRT.

## 4. Incident Classification and Severity Levels

Incidents are classified based on impact to mission, data sensitivity, and system criticality.

| Severity | Impact Level | Description | Example | Response SLA |
| :--- | :--- | :--- | :--- | :--- |
| **SEV-1 (Critical)** | Catastrophic | Active, ongoing attack on mission-critical CIS (e.g., C2 system). Data exfiltration of NS/CTS. | 15 min | Immediate, 24/7 |
| **SEV-2 (High)** | Severe | Significant compromise of NR/NS system. Denial of service to critical service. Insider threat with data loss. | 1 hour | 1 hour |
| **SEV-3 (Medium)** | Moderate | Malware on NU/NR system. Unauthorized access attempt to NS system. | 4 hours | 4 hours |
| **SEV-4 (Low)** | Low | Policy violation, non-malicious malware on NU system. | 8 hours | 8 hours |

## 5. Incident Response Process (NATO AJP-3.20 Aligned)

### Phase 1: Preparation
- **Training:** All personnel receive annual IR training. IRT conducts quarterly tabletop exercises (TTX) and annual full-scale exercise with SHAPE J6/Cyber.
- **Tools:** Network sensors (at domain boundaries), SIEM, EDR on all endpoints, COMSEC key management system.
- **Agreements:** Pre-established communication channels with:
    - NATO Computer Incident Response Capability (NCIRC)
    - Host Nation CERT-RO (Romanian National CSIRT)
    - Contributing Nation Cyber Commands (via SHAPE)
    - NATO Communications and Information Agency (NCI Agency)

### Phase 2: Detection & Analysis
1.  **Detection:** Via SOC sensors, EDR alerts, user reports, or NCIRC notification.
2.  **Triage:** Watch Officer performs initial classification using the matrix above.
3.  **Declaration:** ISSM, as IRT Lead, declares an incident and activates the IRT.

### Phase 3: Containment, Eradication & Recovery
1.  **Containment (Short-Term):** Isolate affected systems from network (logical/physical). For COMSEC incidents, follow two-person integrity procedures for key material.
2.  **Forensic Analysis:** Technical team images memory, logs, and takes forensic snapshots. Chain of custody is maintained for potential legal/disciplinary action.
3.  **Eradication:** Remove malware, close vulnerabilities, reset compromised credentials. For supply-chain compromises, quarantine and replace affected hardware/software.
4.  **Recovery:** Restore systems from trusted, clean backups (following the 3-2-1 backup strategy). Systems are not returned to the operational network until validated clean by the Technical Lead.

### Phase 4: Post-Incident Activity
1.  **Post-Incident Review:** Conducted within 5 business days for SEV-1/2 incidents. Led by ISSM with JAG, PAO, and CIS.
2.  **Lessons Learned:** Report generated, identifying root cause, timeline, and corrective actions. Updates made to this plan, configurations, or training.
3.  **Reporting:**
    - **Internal:** To Detachment Commander and SHAPE J6 within 1 hour of SEV-1/2 declaration.
    - **External (Mandatory):**
        - **NATO:** NCIRC and SHAPE J6, per AC/35 and AC/322 directives.
        - **Host Nation:** CERT-RO, per Romanian Law 58/2019 (NIS2).
        - **Affected Nations:** If data of contributing nation(s) is involved, per bilateral agreements.
    - **Regulatory:** Personal Data Breaches under GDPR reported to Romanian DPA within 72 hours if EU/EEA data subjects are affected.

## 6. Classification & Information Sharing
- All incident details are classified at minimum NATO RESTRICTED. Sharing with external entities (NCIRC, host-nation CERT) follows NATO and NATO/EU classified information exchange guidelines.
- Information sharing with non-NATO entities requires SHAPE J2/J6 and legal approval.

## 7. Communication Plan
- **Internal:** ISSM → Commander → SHAPE J6. PAO manages all external messaging.
- **External (Public):** All external and public communications are managed exclusively by the PAO in coordination with SHAPE Public Affairs.
- **Regulatory:** Legal Officer manages notifications to host-nation authorities (CERT-RO, Data Protection Authority).

## 8. Training and Exercises
- All personnel: Annual Cyber Awareness Training (phishing, reporting).
- IRT Members: Quarterly TTX, Annual Red/Blue Team Exercise with NCIRC/NCSC.
- CIS Operators: Annual "Break-Glass" procedures for COMSEC and cross-domain incidents.

## 9. Policy Review and Compliance
This policy is reviewed annually by the ISSM and Legal Officer. It is mandated by:
- NATO Security Policy (C-M(2002)49, AC/35-D/1015)
- NATO Cyber Defence Pledge (2016)
- AJP-3.20, Allied Joint Doctrine for Cyberspace Operations
- Romanian Law 58/2019 (NIS2 implementation)

## 10. Exceptions
Any deviation from this plan requires written authorization from the ISSM and Legal Officer, documenting the operational necessity and risk accepted.

## 11. Appendices
- Appendix A: Contact Roster (NCIRC, CERT-RO, SHAPE J6, Legal, PAO)
- Appendix B: Incident Reporting Form (NATO and National)
- Appendix C: COMSEC Emergency Zeroization & Key Management Procedures

---
**Approved By:**

[Signature Block for Detachment Commander]

**Date of Approval:** [Date]

**Next Review Date:** [One year from approval]

---
**Sources Consulted & Compliance References:**
- NATO Security Policy (C-M(2002)49)
- NATO AJP-3.20, Allied Joint Doctrine for Cyberspace Operations
- NATO Cyber Defence Pledge (2016)
- Romanian Law 58/2019 on Cybersecurity (NIS2 transposition)
- GDPR (Regulation (EU) 2016/679)
- NIST SP 800-61 Rev. 2 (Computer Security Incident Handling Guide)
- ISO/IEC 27035:2023 (Information Security Incident Management)

</policy>
