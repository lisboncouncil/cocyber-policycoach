---
config: C2
context_id: ctx-M
policy_id: P2
policy_name: Data Protection Policy
policy_short: dataprot
metadata:
  config: C2
  model: moonshotai/Kimi-K2.5
  input_tokens: 25613
  output_tokens: 6782
  total_tokens: 32395
  latency_s: 40.294
  tool_calls:
  - rag_retrieval
  raw_provider_id: 54dbc54b-1a23-49f3-ac70-ebe399d94e94
  chunks_retrieved: 5
  server_version: 1.3.4
sources_count: 4
sources:
- type: kb_source
  source: ./datadir-plus-templates/asset_management.docx
  title: ./datadir-plus-templates/asset_management.docx
- type: kb_source
  source: ./datadir-plus-templates/5.json
  title: Cyber Rapid Response Teams​
- type: kb_source
  source: ./datadir-plus-templates/cybersecurity_policy_BASIC.docx
  title: ./datadir-plus-templates/cybersecurity_policy_BASIC.docx
- type: kb_source
  source: ./datadir-plus-templates/18.json
  title: International Cybersecurity Information Sharing Agreements​
prompt_chars: 6041
answer_chars: 18679
generated_at_unix: 1778086803
---

 <policy title="Data Protection Policy">

| Field | Value |
|---|---|
| **Document ID** | POL-DP-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | NATO RESTRICTED |
| **Owner** | Information Systems Security Manager (ISSM) |
| **Approved by** | Commander, [Organisation] |
| **Approval date** | [DD/MM/YYYY] |
| **Next review date** | [DD/MM/YYYY] |
| **Review cycle** | Annual (and following any significant spillage or cross-domain incident) |

---

## 1. Purpose

This Data Protection Policy establishes the mandatory framework for safeguarding all information assets processed by [Organisation], including NATO classified information (NU, NR, NS, MISSION SECRET) and personal data of civilian staff and contractors. It ensures that data is protected according to its classification level, applicable NATO security directives, host-nation legal requirements (Romanian Law 58/2019, GDPR), and coalition information-sharing agreements. The policy supports the prevention of unauthorised spillage between classification domains, state-sponsored APT exfiltration, and insider threats, while enabling multinational interoperability.

---

## 2. Scope

This policy applies to:

- **All data classifications**: NATO UNCLASSIFIED (NU), NATO RESTRICTED (NR), NATO SECRET (NS), and MISSION SECRET (national/coalition SECRET) processed by [Organisation]
- **All personnel**: 1,500 military active duty, 200 civilian NATO staff, and 300 cleared contractors
- **All systems**: 1,200 classified workstations and 800 unclassified workstations across the four network domains
- **All environments**: On-premises SCIFs (Sensitive Compartmented Information Facilities), deployed tactical systems, and accredited Cross-Domain Solutions (CDS)
- **All data states**: Data at rest, in transit (including via NATO COMSEC equipment), and in processing
- **Third-party processing**: Host-nation contractors and vetted supply chain vendors with access to [Organisation] data

---

## 3. Roles and Responsibilities

### 3.1 Information Systems Security Manager (ISSM)
- Own and maintain this policy per NATO AC/322-D(2017)0009 requirements.
- Approve all exceptions and risk acceptances for data protection controls.
- Report data spillages and breaches to NATO NCSC and host-nation CERT within regulatory timeframes.
- Oversee the 24/7 SOC monitoring of data exfiltration attempts.

### 3.2 Data Owners (Mission Commanders / System Owners)
- Classify data assets according to NATO C-M(2002)49 and assign need-to-know access lists.
- Define data retention periods and disposal authorisation for their respective mission sets.
- Accept residual risk for mission-critical data processing where technical constraints exist.

### 3.3 COMSEC Custodian
- Manage NATO-approved cryptographic keying material with two-person integrity controls.
- Ensure encryption keys for NS and MISSION SECRET data are generated, distributed, and destroyed per national COMSEC authority directives.
- Maintain auditable chain-of-custody records for all keying material.

### 3.4 GDPR Compliance Officer (Designated for Civilian/Contractor Data)
- Ensure processing of personal data for 200 civilian staff and 300 contractors complies with GDPR (EU) 2016/679 and Romanian Law 58/2019.
- Maintain Records of Processing Activities (ROPA) for civilian personnel data.
- Liaise with Romanian National Supervisory Authority regarding data subject rights and breach notifications.

### 3.5 All Personnel (Military, Civilian, Contractors)
- Handle data per the 10 Golden Rules for Cybersecurity and classification-specific handling requirements.
- Report suspected data spillages, unauthorised disclosures, or TEMPEST anomalies immediately to the SOC.
- Comply with dual-key procedures for high-grade COMSEC and operational order releases.

---

## 4. Policy Principles

### 4.1 Classification-Based Protection
Data protection controls are commensurate with the NATO classification level (NU, NR, NS, MISSION SECRET) and the assessed threat from state-sponsored APT and insider actors (*NATO C-M(2002)49, Annex 1*).

### 4.2 Need-to-Know and Least Privilege
Access to data is granted strictly on a need-to-know basis verified by clearance level and mission role, enforced through PKI smart-card authentication without cross-domain identity federation (*ISO/IEC 27001:2022 A.5.15*).

### 4.3 Domain Separation
Strict logical and physical separation between NU, NR, NS, and MISSION SECRET domains is maintained. Data transfer between domains occurs only through accredited Cross-Domain Solutions (CDS) with unidirectional/bidirectional validation (*NATO AC/322-D(2017)0009, Section 4*).

### 4.4 Privacy by Design (Civilian Data)
Personal data processing for civilian staff and contractors incorporates data protection principles by design and by default, ensuring technical and organisational measures comply with GDPR Article 25 (*GDPR (EU) 2016/679, Art. 25*).

### 4.5 Defence in Depth
Layered controls (TEMPEST zoning, COMSEC encryption, access controls, monitoring) protect against kinetic-cyber convergence and physical access threats (*NIST CSF 2.0, PR.DS-1*).

---

## 5. Data Protection Requirements

### 5.1 Data Classification and Inventory

**5.1.1 Classification Levels**
All data must be classified and marked according to NATO standards:
- **NU (NATO UNCLASSIFIED)**: Administrative, logistic, coalition coordination data.
- **NR (NATO RESTRICTED)**: Operational planning at restricted level.
- **NS (NATO SECRET)**: Operational planning, intelligence, command and control.
- **MISSION SECRET**: National/coalition SECRET mission-specific data.

**5.1.2 Inventory**
An up-to-date inventory of all data assets (primary and secondary) must be maintained per the Asset Management Policy (POL-003), reviewed every six months (*ISO/IEC 27001:2022 A.5.9*). The inventory must indicate:
- Classification level and caveats (e.g., ORCON)
- Data Owner and mission system affiliation
- Personal data indicators (for GDPR applicability)
- Physical location (including TEMPEST zone requirements for NS/SECRET)

### 5.2 Handling and Marking

**5.2.1 Physical and Electronic Marking**
All data must bear the appropriate NATO classification marking (NU, NR, NS) or national equivalent (MISSION SECRET) in header/footer metadata. Removable media must be physically labelled with classification and handling caveats (*NATO AC/35-D/1015*).

**5.2.2 TEMPEST Controls**
NS and MISSION SECRET data may only be processed in accredited SCIF rooms with appropriate TEMPEST zoning and electromagnetic shielding. Mobile devices with wireless capabilities are prohibited in SCIFs unless specifically TEMPEST-approved and disabled (*unsupported: specific TEMPEST accreditation standards*).

**5.2.3 Need-to-Know Enforcement**
Access to NR, NS, and MISSION SECRET data requires:
- Valid NATO/Personal Security Clearance at or above the data classification level
- Formal access authorisation by the Data Owner
- PKI smart-card authentication (CAC-equivalent) per classification domain

### 5.3 Encryption and Cryptographic Controls

**5.3.1 Encryption Standards**
Data must be encrypted using NATO-approved algorithms and key lengths per AC/322-D(2017)0009:

| Classification | Data at Rest | Data in Transit | Key Management |
|---|---|---|---|
| **NU** | AES-256 or NATO equivalent | TLS 1.3 or IPsec VPN | PKI per domain |
| **NR** | AES-256 with hardware security module (HSM) | IPsec with NATO-approved crypto | PKI + COMSEC keying material |
| **NS / MISSION SECRET** | NATO-approved Type 1 encryption | NATO COMSEC equipment (encrypted links only) | Two-person integrity for high-grade keys |

**5.3.2 COMSEC Key Management**
- High-grade keying material for NS/SECRET networks is managed under national COMSEC authority with two-person integrity (dual control) for generation, distribution, and destruction (*unsupported: specific national COMSEC regulations*).
- Key rotation occurs per NATO cryptographic period standards or upon suspected compromise.
- Compromised keys must be reported immediately to the COMSEC Custodian and NCSC.

**5.3.3 End-to-End Encryption**
For coalition data sharing, end-to-end encryption must align with bilateral/multilateral information-sharing agreements, ensuring no decryption at intermediate nodes (*NIST CSF 2.0, PR.DS-2*).

### 5.4 Cross-Domain Data Transfers

**5.4.1 Approved Transfer Mechanisms**
Data transfer between classification domains (e.g., NU to NR, or NR to NS) is permitted only through:
- Accredited NATO Cross-Domain Solutions (CDS) with unidirectional/bidirectional guards
- Manual transfer via approved removable media with verified antivirus scanning and data-type validation

**5.4.2 Spillage Prevention**
- Automated content inspection filters must scan for classification marking violations at all CDS boundaries.
- Human review by cleared personnel is required for transfers involving MISSION SECRET or ORCON-marked data.
- All cross-domain transfers are logged and audited monthly for anomalous patterns indicative of adversarial spillage attempts (*ISO/IEC 27001:2022 A.8.5*).

### 5.5 Personal Data Protection (GDPR and NIS2)

**5.5.1 Applicability**
GDPR (EU) 2016/679 and Romanian Law 58/2019 (transposing NIS2) apply to the processing of personal data of 200 civilian NATO staff and 300 contractors resident in Romania. Military personnel data falls under NATO SOFA and national military regulations.

**5.5.2 Lawful Basis and Minimisation**
Processing of civilian personal data requires:
- Documented lawful basis (typically Article 6(1)(e) for public interest or Article 6(1)(b) for contract)
- Data minimisation: collection limited to what is necessary for personnel security vetting, payroll, and operational support (*GDPR Art. 5(1)(c)*)

**5.5.3 Technical and Organisational Measures**
- Encryption of personal data at rest and in transit (per §5.3.1).
- Pseudonymisation where possible for analytical processing.
- Access logging and annual reviews of access rights for civilian HR systems (*GDPR Art. 32*).

**5.5.4 Data Subject Rights**
Civilian staff and contractors may exercise GDPR rights (access, rectification, erasure) through the GDPR Compliance Officer, subject to NATO SOFA limitations regarding operational necessity and security vetting records (*unsupported: specific SOFA Article limitations*).

**5.5.5 Breach Notification**
Personal data breaches affecting civilian/contractor data must be reported to the Romanian National Supervisory Authority within 72 hours of discovery, and to affected data subjects where high risk (*GDPR Art. 33-34*).

### 5.6 Data Retention and Disposal

**5.6.1 Retention Schedules**
Data retention periods are defined by Data Owners based on:
- NATO archival requirements (typically 5-10 years for operational records)
- Romanian legal requirements for financial/personnel records (civilian data)
- Mission-specific coalition agreements

**5.6.2 Secure Disposal**
Obsolete or non-repairable assets containing data must be disposed of per DIN 66399 (destruction level 3 or higher) or NATO equivalent standards:
- **NU/NR**: Cryptographic erasure or physical destruction
- **NS/MISSION SECRET**: Physical destruction (shredding, degaussing, or incineration) with two-person witnessing and certificate of destruction (*ISO/IEC 27001:2022 A.5.11*)

**5.6.3 Domain-Specific Sanitisation**
Prior to reclassification or release to host-nation authorities, storage media must undergo verified sanitisation appropriate to the highest classification level ever stored on the device.

### 5.7 Backup and Recovery

**5.7.1 Backup Requirements**
Critical data (operational plans, intelligence products, civilian personnel records) must be backed up in accordance with the Backup and Recovery Policy (POL-004):
- **RPO**: 4 hours for NS/MISSION SECRET operational data; 24 hours for NR; 7 days for NU
- **Encryption**: All backups encrypted at the classification level of the source data
- **Segregation**: Backup media for NS/SECRET stored in physically separate TEMPEST-accredited facilities (*NIST CSF 2.0, PR.DS-9*)

**5.7.2 Recovery Testing**
Restoration of classified data from backup must be tested annually for NS/MISSION SECRET systems and semi-annually for critical coalition interoperability systems.

### 5.8 Supply Chain Data Protection

Vendors providing data processing services (cloud storage, analytics) must:
- Be vetted against NATO-approved equipment lists and security screening requirements
- Contractually agree to data protection clauses mirroring this policy
- Allow audit rights for the ISSM to verify data handling at subcontractor facilities (*ISO/IEC 27001:2022 A.5.20*)

---

## 6. Monitoring and Review

**6.1 Continuous Monitoring**
The 24/7 SOC monitors for:
- Unauthorized data exfiltration attempts (DLP alerts at domain boundaries)
- Anomalous access patterns indicating insider threat or compromised credentials
- CDS bypass attempts or unauthorized removable media usage

**6.2 Compliance Audits**
- Annual internal audits verify compliance with this policy, NATO C-M(2002)49, and GDPR (*ISO/IEC 27001:2022 A.5.36*).
- Red-team engagements (2 per year) specifically test data exfiltration paths and cross-domain spillage controls.

**6.3 Policy Review**
This policy is reviewed annually and following:
- Any significant data spillage incident
- Changes to NATO INFOSEC directives (AC/322 series)
- Updates to Romanian Law 58/2019 or NIS2 implementation decrees
- New coalition information-sharing agreements

---

## 7. Exceptions

Exceptions to data protection requirements (e.g., temporary waiver of encryption for legacy tactical systems) require:
1. Written request from the Data Owner documenting operational necessity and compensating controls (e.g., physical security, air-gapping).
2. Risk assessment by the ISSM against state-sponsored APT and insider threat vectors.
3. Approval by the Commander for exceptions affecting NS/MISSION SECRET data; ISSM approval for NU/NR.
4. Time-limitation (maximum 6 months) and entry in the ISMS Exception Register.
5. Quarterly review of exception validity (*unsupported: NATO exception management procedures*).

---

## 8. Incident Response and Reporting

**8.1 Data Spillage Response**
Suspected or confirmed spillage between classification domains (e.g., SECRET data on NU network) constitutes a Critical incident requiring:
- Immediate isolation of affected systems
- Notification to NCSC and host-nation CERT within 1 hour
- Forensic preservation per the Cyber Incident Response Plan (POL-008)
- Post-incident review within 5 business days

**8.2 Personal Data Breach Response**
Breaches affecting civilian/contractor personal data follow the GDPR 72-hour notification timeline to the Romanian supervisory authority and documented internal records (*GDPR Art. 33*).

---

## 9. Enforcement

Non-compliance with data protection requirements, including:
- Unauthorized removal of data from secure domains
- Failure to apply classification markings
- Intentional circumvention of CDS or COMSEC controls
- Unauthorized disclosure to uncleared personnel

will result in disciplinary action per NATO personnel security regulations (AC/35-D/1029), revocation of security clearance, and potential referral to host-nation law enforcement or national military justice systems for criminal prosecution under espionage or unauthorized disclosure statutes.

---

## 10. Related Documents

| Document ID | Title |
|---|---|
| POL-001 | Cybersecurity Policy |
| POL-002 | Access Control Policy |
| POL-003 | Asset Management Policy |
| POL-004 | Backup and Recovery Policy |
| POL-006 | Password Policy |
| POL-007 | Vulnerability and Patch Management Policy |
| POL-008 | Cyber Incident Response Plan |
| POL-009 | 10 Golden Rules for Cybersecurity |

---

## 11. Definitions

| Term | Definition |
|---|---|
| **CDS** | Cross-Domain Solution — accredited hardware/software enabling controlled data transfer between different security domains. |
| **COMSEC** | Communications Security — measures and controls to protect information derived from telecommunications and cryptology. |
| **Mission Secret** | National or coalition SECRET classification level for mission-specific operational data. |
| **NCSC** | NATO Cyber Security Centre — the central authority for cyber incidents affecting NATO networks. |
| **Need-to-Know** | Principle restricting access to information to those whose official duties require such access. |
| **NS** | NATO SECRET — classification level for information whose unauthorized disclosure would cause serious damage to NATO. |
| **NU** | NATO UNCLASSIFIED — publicly releasable information subject to standard handling precautions. |
| **NR** | NATO RESTRICTED — classification for information requiring protection against unauthorized disclosure. |
| **ORCON** | Originator Control — caveat restricting further dissemination without originator approval. |
| **SCIF** | Sensitive Compartmented Information Facility — accredited room for processing SECRET information with TEMPEST and physical protections. |
| **SOFA** | Status of Forces Agreement — treaty defining legal status of NATO forces in host nation (Romania). |
| **TEMPEST** | Investigation and study of compromising emanations from electronic equipment. |
| **Two-Person Integrity** | Security measure requiring two authorized persons to jointly perform sensitive actions (e.g., COMSEC key handling). |

---

## 12. Compliance and Regulatory References

- **NATO C-M(2002)49** — NATO Information Security Policy (and successor directives)
- **NATO AC/322-D(2017)0009** — INFOSEC Technical and Implementation Directive
- **NATO AC/35-D/1015** — Security within NATO
- **NATO AC/35-D/1029** — Personnel Security
- **NATO Allied Joint Doctrine for Cyberspace Operations (AJP-3.20)**
- **GDPR (EU) 2016/679** — Articles 5, 25, 32, 33, 34 (data protection principles, security, breach notification)
- **Romanian Law 58/2019** — Cybersecurity Law (transposing NIS Directive and NIS2)
- **ISO/IEC 27001:2022** — Controls A.5.9, A.5.10, A.5.11, A.5.12, A.5.15, A.5.20, A.5.36, A.8.5
- **NIST CSF 2.0** — Functions PR.DS (Data Security), PR.AC (Access Control)
- **DIN 66399** — Information Technology — Destruction of Data Carriers (for sanitisation standards)

---

## 13. Revision History

| Version | Date | Author | Description of Change |
|---|---|---|---|
| 1.0 | [DD/MM/YYYY] | ISSM / J6 | Initial release for multinational detachment deployment |

---

## 14. Approval

| Role | Name | Signature | Date |
|---|---|---|---|
| Policy Owner (ISSM) | | | |
| Approved by (Commander) | | | |
| Legal/Compliance Review (GDPR Officer) | | | |

</policy>
