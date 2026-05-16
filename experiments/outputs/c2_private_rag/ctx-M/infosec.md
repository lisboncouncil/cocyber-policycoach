---
config: C2
context_id: ctx-M
policy_id: P5
policy_name: General Cybersecurity Policy
policy_short: infosec
metadata:
  config: C2
  model: moonshotai/Kimi-K2.5
  input_tokens: 25607
  output_tokens: 8192
  total_tokens: 33799
  latency_s: 39.258
  tool_calls:
  - rag_retrieval
  raw_provider_id: e83c80d1-30c1-4858-b3b4-fbdaea98d5aa
  chunks_retrieved: 5
  server_version: 1.3.4
sources_count: 5
sources:
- type: kb_source
  source: ./datadir-plus-templates/5.json
  title: Cyber Rapid Response Teams​
- type: kb_source
  source: ./datadir-plus-templates/cybersecurity_policy_BASIC.docx
  title: ./datadir-plus-templates/cybersecurity_policy_BASIC.docx
- type: kb_source
  source: ./datadir-plus-templates/9.json
  title: 'The Sector CSIRT Framework: Developing Sector-Based Incident Response Capabilities'
- type: kb_source
  source: ./datadir-plus-templates/15.json
  title: 'National CERT/CSIRT: Mandate and Organisation paper'
- type: kb_source
  source: ./datadir-plus-templates/asset_management.docx
  title: ./datadir-plus-templates/asset_management.docx
prompt_chars: 6053
answer_chars: 13229
generated_at_unix: 1778086915
---

 <policy title="General Cybersecurity Policy">

| Field | Value |
|---|---|
| **Document ID** | POL-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | NATO RESTRICTED |
| **Owner** | Information Systems Security Manager (ISSM) |
| **Approved by** | Commander, [Multinational Military Detachment] |
| **Approval date** | [DD/MM/YYYY] |
| **Next review date** | [DD/MM/YYYY] |
| **Review cycle** | Annual |

---

## 1. Purpose

This General Cybersecurity Policy establishes the minimum security requirements for the protection of NATO Communications and Information Systems (CIS), classified information, and personnel within the [Multinational Military Detachment] operating under Allied Command Operations (SHAPE) in Romania. It ensures the confidentiality, integrity, and availability of information assets across all classification domains (NU, NR, NS, and MISSION SECRET) while supporting multinational interoperability, Signals Intelligence (SIGINT) operations, and cyber defence missions. This policy aligns with NATO Information Security Policy [C-M(2002)49], Allied Joint Doctrine for Cyberspace Operations [AJP-3.20], and applicable Romanian cybersecurity legislation, providing the governance framework for the ISMS continual improvement cycle [ISO/IEC 27001:2022, Clause 5.1].

---

## 2. Scope

This policy applies to:

- **All personnel**: 1,500 military active duty, 200 civilian NATO staff, and 300 cleared contractors assigned to or operating within the detachment [Organisational Profile].
- **All information systems**: 1,200 classified workstations and 800 unclassified workstations across four distinct classification domains:
  - **NU (NATO UNCLASSIFIED)**: Administrative, logistic, and coalition coordination systems.
  - **NR (NATO RESTRICTED)**: Operational planning at restricted level.
  - **NS (NATO SECRET)**: Operational planning, intelligence, and command and control.
  - **MISSION SECRET**: National/coalition mission-specific operational systems.
- **All network infrastructure**: Including Cross-Domain Solutions (CDS), COMSEC equipment, and boundary sensors monitored by the 24/7 Security Operations Centre (SOC).
- **Physical locations**: All TEMPEST-zoned SCIFs, server rooms, and operational facilities within the Romanian host-nation footprint, subject to NATO Status of Forces Agreement (SOFA) limitations.

---

## 3. Roles and Responsibilities

### 3.1 Commander, [Multinational Military Detachment]
- Provides strategic direction and resources for cybersecurity in accordance with NATO Cyber Defence Pledge 2016 commitments.
- Accepts residual risk for operations and approves high-risk exceptions to this policy.
- Serves as ultimate authority for dual-key procedures and high-grade COMSEC release decisions [AC/35-D/1015].

### 3.2 Information Systems Security Manager (ISSM)
- Owns and maintains this policy and subordinate security documentation.
- Reports ISMS performance and security posture to the Commander and SHAPE J6.
- Chairs the Cyber Incident Response Team (CIRT) and approves security exceptions [ISO/IEC 27001:2022, Clause 5.37].

### 3.3 J6 (CIS Director) and IT Operations
- Implements technical controls across NU, NR, NS, and MISSION SECRET domains.
- Maintains up-to-date asset inventory of all 2,000 workstations and network infrastructure [CIS Controls v8, Control 1].
- Operates the 24/7 SOC and manages PKI/smart-card infrastructure.

### 3.4 Security Officer (J2/J39)
- Conducts personnel security screening and counterintelligence activities in accordance with [AC/35-D/1029].
- Manages insider threat detection programmes and HUMINT awareness briefings.

### 3.5 Asset Owners (Mission System Owners)
- Define recovery objectives (RTO/RPO) for critical operational systems.
- Ensure need-to-know access controls are enforced for their respective classification domains [AC/322-D(2017)0009].

### 3.6 All Personnel (Military, Civilian, and Contractors)
- Comply with this policy, the 10 Golden Rules for Cybersecurity (where applicable), and classification handling procedures.
- Complete mandatory 40 hours of security training annually [Resource Envelope].
- Report suspected security incidents, spillage, or insider threats immediately to the SOC or ISSM.

---

## 4. Policy Principles

### 4.1 Defence in Depth and Layered Security
Security controls are implemented in multiple layers (physical, network, endpoint, application) to prevent single points of failure [AJP-3.20, Chapter 3].

### 4.2 Need-to-Know and Least Privilege
Access to information and systems is granted on a default-deny basis, limited to the minimum necessary for mission role and clearance level [AC/322-D(2017)0009, Annex A].

### 4.3 Separation of Classification Domains
Strict logical and physical separation between NU, NR, NS, and MISSION SECRET domains is maintained. Data transfer between domains occurs only through accredited Cross-Domain Solutions (CDS) [AC/322-D(2017)0009].

### 4.4 COMSEC Integrity and Two-Person Control
Cryptographic key material and high-grade COMSEC operations require two-person integrity (TPI) and auditable chain-of-custody procedures [AC/35-D/1015, para. 42].

### 4.5 Zero Trust for Cross-Domain Access
All cross-domain data transfers require explicit validation, inspection, and accreditation, regardless of source authentication [NIST CSF 2.0, Function PR.DS-5].

### 4.6 Continuous Monitoring and Proactive Defence
The 24/7 SOC maintains persistent monitoring of domain boundaries and critical assets to detect state-sponsored APT activity and insider threats [NIST CSF 2.0, Function DE.AE].

---

## 5. Security Requirements and Controls

### 5.1 Governance and Risk Management
- An **annual information security risk assessment** shall identify threats (including state-sponsored APTs, insider threats, and supply-chain compromises) and evaluate risks to mission objectives [ISO/IEC 27001:2022, Clause 6.1; NIST CSF 2.0, Function GV.RM].
- Risk treatment plans shall address kinetic-cyber convergence scenarios specific to the regional threat environment.
- The ISMS shall undergo **annual management review** by the Commander and ISSM to ensure continual improvement [ISO/IEC 27001:2022, Clause 9.3].

### 5.2 Asset Management and Classification
- A complete inventory of all 2,000 classified and 800 unclassified workstations, network devices, and COMSEC equipment shall be maintained and reviewed every **six months** [CIS Controls v8, Control 1; ISO/IEC 27001:2022, Control A.5.9].
- All assets shall be marked and handled according to NATO classification levels (NU, NR, NS, MISSION SECRET) with **Originator Control (ORCON)** markings applied to shared intelligence products [C-M(2002)49, Annex III].
- **Unsupported software** shall be removed from all systems; exceptions require ISSM approval with documented compensating controls [ISO/IEC 27001:2022, Control A.8.8].

### 5.3 Identity and Access Management
- **PKI and Smart-Card Authentication**: All users shall authenticate via NATO PKI-compliant smart cards (CAC-equivalent) unique to each classification domain. No cross-domain identity federation is permitted [AC/322-D(2017)0009].
- **Multi-Factor Authentication (MFA)**: MFA shall be enforced for all remote access (VPN), privileged accounts, and cloud services where technically feasible [ISO/IEC 27001:2022, Control A.5.18; NIST CSF 2.0, PR.AA-01].
- **Access Reviews**: User access rights shall be reviewed **quarterly** by Asset Owners and J6 to ensure continued need-to-know and proper clearance alignment [ISO/IEC 27001:2022, Control A.5.16].
- **Default-Deny**: All access requests require formal approval via the Account Creation and Modification Form (ACMF) with N+1 (or NATO equivalent) authorisation [ISO/IEC 27001:2022, Control A.5.15].

### 5.4 Cryptographic and COMSEC Controls
- **Equipment Standards**: Only NATO-approved COMSEC equipment listed on the NATO Information Security Equipment Catalogue (NISEC) shall be deployed [AC/35-D/1015].
- **Two-Person Integrity (TPI)**: All handling of high-grade keying material (TOP SECRET/COSMIC) requires TPI and dual-key procedures for operational release [AC/35-D/1015].
- **Key Management**: Cryptographic keys shall be managed under the authority of the national COMSEC custodian with end-to-end auditable chain-of-custody [AC/35-D/1015].
- **Encryption**: Data at RESTRICTED and above shall be encrypted at rest using NATO-approved algorithms; data in transit shall use IPSec or equivalent for inter-domain communication [ISO/IEC 27001:2022, Control A.8.24].

### 5.5 Cross-Domain Solutions and Data Transfer
- **Accredited CDS Only**: Data transfer between NU, NR, NS, or MISSION SECRET domains shall occur exclusively through NATO-accredited Cross-Domain Solutions with unidirectional or bidirectional certification appropriate to the transfer direction [AC/322-D(2017)0009].
- **Spillage Prevention**: All transfers shall be scanned for malware and classification violations. Accidental spillage shall trigger immediate incident response procedures [AJP-3.20, Annex B].
- **Removable Media**: Use of removable media across classification boundaries is prohibited unless via accredited CDS with sanitisation verification.

### 5.6 Vulnerability and Patch Management
- **Scanning Frequency**: Vulnerability scans shall be conducted **monthly** for NS and MISSION SECRET systems, and **quarterly** for NR/NU systems [CIS Controls v8, Control 7; ISO/IEC 27001:2022, Control A.8.8].
- **Patch SLAs**:
  - **Critical** (CVSS 9.0-10.0): Within 48 hours.
  - **High** (CVSS 7.0-8.9): Within 7 days.
  - **Medium/Low**: Within 30 days or next maintenance window [NIST CSF 2.0, PR.IP-12].
- **Red Team Exercises**: Two red-team engagements shall be conducted annually to test defences against APT tactics [Resource Envelope].

### 5.7 Incident Response and Reporting
- **Alignment with NCIRC**: All cyber incidents shall be managed in accordance with NATO Cyber Incident Response Centre (NCIRC) procedures and the Cyber Incident Response Plan (POL-008) [AJP-3.20].
- **Reporting Chain**: Incidents shall be reported simultaneously to:
  - The 24/7 SOC (immediate).
  - NATO NCSC (within 1 hour for Critical/High severity).
  - Romanian National CERT (CERT-RO) for incidents affecting host-nation networks or civilian data, per Romanian Cybersecurity Law 58/2019 [Romanian Law 58/2019, Art. 12].
- **Evidence Preservation**: All logs and forensic evidence shall be preserved with chain-of-custody documentation for potential legal or counterintelligence proceedings [ISO/IEC 27001:2022, Control A.5.26].

### 5.8 Physical and Environmental Security
- **TEMPEST and SCIF**: NS and MISSION SECRET processing shall occur only within accredited SCIFs with TEMPEST zoning and electromagnetic shielding [AC/35-D/1015].
- **Physical Access**: Network equipment rooms and COMSEC storage require two-factor physical access control (smart card + PIN/biometric) and 24/7 guard or alarmed monitoring [ISO/IEC 27001:2022, Control A.7.1].
- **Workstation Security**: Classified workstations shall be configured with automatic screen locks after 15 minutes of inactivity and visible "Classified" markings [AC/322-D(2017)0009].

### 5.9 Insider Threat and Personnel Security
- **Screening**: All personnel (military, civilian, contractors) shall undergo personnel security screening per [AC/35-D/1029] prior to access to NR and above.
- **Continuous Monitoring**: Cleared personnel shall be subject to continuous evaluation for financial distress, foreign contacts, or behavioural anomalies indicative of HUMINT recruitment risk [unsupported: organisational counterintelligence requirement].
- **Supply Chain Vetting**: Host-nation contractors and vendors shall undergo security screening and use only NATO-approved equipment lists to prevent supply-chain compromise [NIST CSF 2.0, PR.SC-1; AC/35-D/1029].

### 5.10 Data Protection and Privacy
- **GDPR Compliance**: Processing of civilian NATO staff and contractor personal data shall comply with GDPR (EU) 2016/679 Article 32 (technical and organisational measures), with the ISSM designated as data security contact for Romanian supervisory authority interactions [GDPR Art. 32].
- **SOFA Limitations**: Enforcement of host-nation cybersecurity laws against military personnel and systems is limited by NATO SOFA Article VII; civilian data breaches shall be reported to Romanian authorities per Law 58/2019 [NATO SOFA, Art. VII; Romanian Law 58/2019, Art. 13].
- **Classification of Personal Data**: Personal data of military personnel at SECRET level (e.g., Special Forces identities) shall be handled as NATO SECRET with ORCON markings.

### 5.11 Training and Awareness
- **Mandatory Training**: All personnel shall complete **40 hours** of cybersecurity and information assurance training annually, including classification handling, phishing recognition, and insider threat indicators [Resource Envelope; NATO Cyber Defence Pledge 2016].
- **Exercises**: Six multinational interoperability exercises shall be conducted annually to test cyber defence and CIS operational readiness [Resource Envelope].
- **Role-Based Training**: ISSM and SOC staff shall maintain current certifications (e.g., NATO INFO
