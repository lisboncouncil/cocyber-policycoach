---
config: C2b
context_id: ctx-M
policy_id: P2
policy_name: Data Protection Policy
policy_short: dataprot
metadata:
  config: C2b
  model: deepseek-ai/DeepSeek-V3.2
  input_tokens: 25920
  output_tokens: 2029
  total_tokens: 27949
  latency_s: 38.836
  tool_calls:
  - rag_retrieval
  raw_provider_id: 48265f46-cb81-4ea9-ab53-f32bb6ea9cee
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
answer_chars: 8664
generated_at_unix: 1778503894
---

<policy title="Data Protection Policy">

| Field | Value |
|-------|-------|
| **Document ID** | POL-DP-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | NATO RESTRICTED (Releasable to NATO and PfP Nations) |
| **Owner** | Information Systems Security Manager (ISSM) |
| **Approved by** | Detachment Commander |
| **Approval Date** | [DD/MM/YYYY] |
| **Next Review Date** | [DD/MM/YYYY] (One year from approval) |
| **Review Cycle** | Annual (or upon significant change in NATO regulations or mission) |

---

## 1. Purpose

This Data Protection Policy establishes the framework for the protection of all information assets, with a particular focus on NATO and national classified information, personal data, and mission-critical operational data within the [NATO Detachment]. It defines the minimum requirements for data classification, handling, storage, transmission, and destruction in accordance with NATO Security Policy (C-M(2002)49), the NATO Information Security Policy, and applicable host-nation regulations, including the EU General Data Protection Regulation (GDPR) for personal data of EU/EEA personnel. This policy ensures the confidentiality, integrity, and availability of information in alignment with NATO Allied Joint Doctrine for Cyberspace Operations (AJP-3.20) and the NIST Cybersecurity Framework.

## 2. Scope

This policy applies to:
*   All personnel assigned to the detachment, including military, civilian, and contractor personnel.
*   All information systems, networks, and data repositories under the detachment's operational control, including NATO SECRET (NS), NATO RESTRICTED (NR), and NATO UNCLASSIFIED (NU) domains.
*   All data, structured and unstructured, in transit, at rest, and in use, including:
    *   NATO and national classified information.
    *   Personal data of military, civilian, and contractor personnel.
    *   Mission-critical operational data (e.g., CIS logs, operational plans, intelligence).
    *   Data processed by cross-domain solutions (CDS) and on coalition networks.

## 3. Roles and Responsibilities

### 3.1. Detachment Commander
*   Holds ultimate accountability for information security and data protection within the detachment.
*   Approves significant deviations from this policy.

### 3.2. Information Systems Security Manager (ISSM)
*   The primary owner and approving authority for this policy.
*   Oversees implementation, ensures compliance with NATO and host-nation regulations, and reports to the Commander.
*   Chairs the detachment's Security Working Group.

### 3.3. Information Systems Security Officer (ISSO)
*   Implements and enforces this policy.
*   Conducts regular audits and risk assessments.
*   Manages the data classification and handling program.
*   Reports security incidents to the ISSM and relevant authorities (NCIRC, host-nation CERT).

### 3.4. All Personnel
*   Complete mandatory annual data protection and security awareness training.
*   Adhere to the principle of "need-to-know" and "least privilege."
*   Report suspected data breaches or policy violations immediately.

### 3.5. System/Data Owner (e.g., J2, J3, J6)
*   Classify information assets under their purview.
*   Authorize access based on mission need and personnel clearance.
*   Define retention and destruction schedules for their data.

## 4. Policy Principles & Core Requirements

### 4.1. Data Classification & Handling
All information must be classified and handled according to the highest classification of any data it contains.

| Classification | Label | Storage & Transmission | Destruction |
| :--- | :--- | :--- | :--- |
| **NATO SECRET (NS)** | Physical: NATO SECRET containers, SCIFs. Digital: NS-domain, encrypted per NATO crypto. | Secure voice/data links (CRYPTO). NATO SECRET cover sheets. | Incineration or cross-cut shredding. COMSEC material as per AC/35-D1. |
| **NATO RESTRICTED (NR)** | Physical: Locked containers, NR-registered mail. Digital: NR-domain, encrypted email. | NATO RESTRICTED cover sheets. | Cross-cut shredding. |
| **NATO UNCLASSIFIED (NU)** | Physical: Controlled access. Digital: NU-domain. | Standard mail/email with basic encryption. | Standard shredding. |
| **Personal Data (GDPR)** | Encrypted at rest and in transit. | Anonymized/pseudonymized where possible. | Secure erasure after legal retention period. |

### 4.2. Access Control & Need-to-Know
*   Access to information is granted based on **need-to-know** and **security clearance** equal to or exceeding the data's classification.
*   The principle of **least privilege** is enforced. Access is role-based (RBAC) and reviewed quarterly.
*   Multi-Factor Authentication (MFA) is mandatory for all remote and privileged access to NS/NR domains.
*   **Dual-Key Procedures** are mandatory for the release of COMSEC keys and certain operational orders.

### 4.3. Data in Transit & Cross-Domain
*   Data transfer between different classification levels **must** use accredited NATO Cross-Domain Solutions (CDS).
*   Data in transit between sites or to higher HQs must be encrypted using NATO-approved cryptographic products (e.g., TACLANE, SINA).
*   Wireless transmission of NS/NSa data is prohibited unless on a TEMPEST-approved, TEMPEST-suppressed system.

### 4.4. Data at Rest & Storage
*   **NS Data:** Stored only on accredited, air-gapped systems within SCIFs. Full-disk encryption (FIPS 140-3 validated) is mandatory for mobile computing devices.
*   **Personal/Operational Data:** Encrypted at rest using AES-256. Keys managed by the detachment COMSEC custodian.
*   **Media Sanitization:** Decommissioned media (HDDs, SSDs, USBs) storing NS/NSa data must be physically destroyed (degaussed and shredded) in accordance with NATO SDIP-27.

### 4.5. Data Retention & Disposal
*   Retention schedules are defined by the data owner (J-codes) and must comply with NATO and host-nation laws.
*   GDPR data is retained only as long as necessary for the stated purpose (GDPR Art. 5(1)(e)).
*   Destruction must be irreversible. Paper is cross-cut shredded; digital media is cryptographically erased (DoD 5220.22-M standard) or physically destroyed.

### 4.6. Incident Response & Breach Notification
*   All suspected data breaches (spillage, unauthorized access, loss of media) must be reported to the ISSO **immediately**.
*   The ISSO will activate the NATO Computer Incident Response Capability (NCIRC) reporting process.
*   Personal data breaches with risk to individuals will be reported to the host-nation Data Protection Authority (if applicable under GDPR) within 72 hours, coordinated through legal/public affairs.

## 5. NATO & Regulatory Compliance
This policy enforces compliance with:
*   **NATO:** C-M(2002)49 (Security within NATO), AC/35-D/1015, AC/322(2021) on Cyber Defence.
*   **Host Nation (Romania):** Law 190/2018 (Cybersecurity Law), GDPR (Regulation 2016/679).
*   **NATO Cyber Defence Pledge (2016)** and **Allied Joint Doctrine for Cyberspace Operations (AJP-3.20)**.
*   **NIST Cybersecurity Framework (CSF) 2.0** is used as the primary control framework for technical and procedural controls.

## 6. Exceptions
Requests for exceptions to this policy must be submitted in writing to the ISSM. Temporary exceptions may be granted for operational necessity, requiring a written risk acceptance from the Detachment Commander and compensating controls.

## 7. Policy Review & Monitoring
*   The ISSO will conduct quarterly audits of access logs and data handling procedures.
*   This policy will be reviewed annually by the ISSM, or following any significant security incident or change in NATO/National regulation.
*   All personnel will complete annual Data Protection and Security Awareness training.

## 8. Enforcement
Violations of this policy may result in disciplinary action under the NATO SOFA/SOFA and applicable national military/disciplinary codes, up to and including termination of access, administrative action, or legal proceedings.

---
**Approval**

**Detachment Commander:** ____________________ Date: _________

**Information Systems Security Manager (ISSM):** ____________________ Date: _________

---
**References & Sources:**
*   NATO Security Policy (C-M(2002)49)
*   NATO Cyber Defence Pledge (2016)
*   NATO AJP-3.20, Allied Joint Doctrine for Cyberspace Operations
*   EU General Data Protection Regulation (GDPR) 2016/679
*   NIST Cybersecurity Framework 2.0 (NIST CSF 2.0)
*   AC/35-D/1015, AC/35-D/1029
*   Romanian Cybersecurity Law 58/2019 (transposing NIS2)

**Revision History**
| Version | Date | Author | Changes |
| :--- | :--- | :--- | :--- |
| 1.0 | [Date] | ISSM | Initial Policy Draft |

</policy>
