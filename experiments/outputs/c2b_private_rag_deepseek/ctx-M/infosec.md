---
config: C2b
context_id: ctx-M
policy_id: P5
policy_name: General Cybersecurity Policy
policy_short: infosec
metadata:
  config: C2b
  model: deepseek-ai/DeepSeek-V3.2
  input_tokens: 25898
  output_tokens: 2402
  total_tokens: 28300
  latency_s: 47.802
  tool_calls:
  - rag_retrieval
  raw_provider_id: b56ad615-6d29-400f-b1ab-5513c91cdd3a
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
answer_chars: 10535
generated_at_unix: 1778504037
---

<policy title="NATO Allied Command Operations Detachment Cybersecurity Policy">

| Field | Value |
|-------|-------|
| **Document ID** | ACO-DET-POL-CYB-001 |
| **Version** | 1.0 |
| **Status** | Final Draft |
| **Classification** | NATO UNCLASSIFIED (Releasable to NATO, PfP, MD, ICI, Australia, Japan, New Zealand) |
| **Owner** | Detachment Information Systems Security Manager (ISSM) |
| **Approved by** | Detachment Commander |
| **Approval Date** | [Date of Approval] |
| **Next Review Date** | One year from approval |
| **Review Cycle** | Annual, or upon significant change in mission, structure, or threat landscape. |

---

## 1. Purpose

This Cybersecurity Policy establishes the minimum mandatory security requirements for the protection of NATO Allied Command Operations (ACO) Detachment information, information systems, and networks. It ensures the confidentiality, integrity, and availability of information across all classification levels (NU, NR, NS) in accordance with NATO Security Policy, host-nation (Romanian) law, and applicable national frameworks of contributing nations. This policy provides the framework for implementing the NATO Information Security Policy (C-M(2002)49 and successors), the NATO Cyber Defence Pledge, and supports compliance with Allied Joint Doctrine for Cyberspace Operations (AJP-3.20).

## 2. Scope

This policy applies to all personnel (military, civilian, and contractor) assigned to or supporting the Detachment, and to all information systems, networks, and data under the Detachment's operational control, including:
- NATO Classified Information Systems (NATO SECRET, NATO RESTRICTED, NATO UNCLASSIFIED).
- Mission-specific coalition networks (e.g., MISSION SECRET).
- All workstations (1200 classified, 800 unclassified), servers, and network infrastructure.
- All personnel (2000 total: 1500 military, 200 civilian staff, 300 cleared contractors).

## 3. Roles and Responsibilities

### 3.1 Detachment Commander
- Holds ultimate responsibility for the security of Detachment information and systems.
- Approves this policy and any major exceptions.
- Ensures adequate resources are allocated for cybersecurity.

### 3.2 Information Systems Security Manager (ISSM)
- Owns and maintains this policy.
- Oversees the implementation of all cybersecurity controls.
- Serves as the primary liaison with the NATO Communications and Information Agency (NCIA) and host-nation (Romanian) Computer Security Incident Response Team (RO-CSIRT).
- Reports to the Detachment Commander on security posture.

### 3.3 Information Systems Security Officer (ISSO)
- Implements and enforces this policy on a day-to-day basis.
- Manages the 25-person security staff.
- Conducts security audits and vulnerability assessments.

### 3.4 All Personnel
- Complete mandatory annual cybersecurity and classification handling training (40 hours/year minimum).
- Report all security incidents or policy violations immediately.
- Adhere to the principle of least privilege and need-to-know.

## 4. Policy Principles

1.  **Defense in Depth:** Security is implemented in multiple, overlapping layers (physical, network, host, application, data).
2.  **Need-to-Know & Least Privilege:** Access to information and systems is granted based on mission-essential requirements and the principle of least privilege.
3.  **Strict Domain Separation:** Information of different classification levels (NU, NR, NS, MISSION) shall be processed on separate, accredited systems. Cross-domain data transfers require approved, accredited Cross-Domain Solutions (CDS).
4.  **Continuous Monitoring:** 24/7 Security Operations Center (SOC) monitoring and regular red-team exercises (2/year) are mandated to ensure proactive threat detection.
5.  **Compliance with NATO Directives:** All security controls must comply with the NATO Security Policy and its implementing directives (e.g., AC/35-D/1015, AC/322-D(2017)0009).

## 5. Policy Requirements & Controls

### 5.1. Asset Management & Classification
*   **Control:** All assets (1,200 classified, 800 unclassified workstations, servers, network devices) must be entered into a Configuration Management Database (CMDB) with a designated asset owner.
*   **Control:** All information and systems must be classified and marked in accordance with NATO and national classification guides (NATO SECRET, NATO RESTRICTED, NATO UNCLASSIFIED, MISSION-SPECIFIC).
*   **Source:** NATO Security Policy (C-M(2002)49), NATO Security Indoctrination.

### 5.2. Access Control & Identity Management
*   **Control:** Access to all systems is controlled via NATO PKI smart cards (CAC-equivalent). Multi-Factor Authentication (MFA) is mandatory for all privileged and remote access.
*   **Control:** Access rights are reviewed quarterly by the ISSM and system owners, based on current mission role and need-to-know.
*   **Control:** Strict separation of duties is enforced between network administration, system administration, and security auditing functions.
*   **Source:** NATO AC/35-D/1029 (Personnel Security), NIST SP 800-53 (IA-2, AC-2, AC-6).

### 5.3. Network Security & Segmentation
*   **Control:** Network domains (NU, NR, NS, MISSION) must be physically or logically separated. Traffic between domains is only permitted via accredited Cross-Domain Solutions (CDS) with explicit data flow approval.
*   **Control:** All network traffic is logged and subject to 24/7 monitoring by the SOC. Intrusion Detection/Prevention Systems (IDS/IPS) are mandatory at all domain boundaries.
*   **Source:** NATO AC/322-D(2017)0009, NIST CSF PR.AC-5, PR.AC-6.

### 5.4. Physical & COMSEC Security
*   **Control:** TEMPEST-zoned SCIFs are mandatory for processing NS and above. Access requires appropriate clearance, need-to-know, and two-person integrity for high-grade COMSEC material.
*   **Control:** COMSEC keying material and cryptographic equipment are managed in accordance with NATO and national COMSEC instructions. Chain of custody for all COMSEC material is logged and audited.
*   **Source:** NATO COMSEC Directives, Host Nation SOFA and Romanian Law 58/2019.

### 5.5. Vulnerability & Patch Management
*   **Control:** All systems must be patched within the SLAs defined in the Vulnerability and Patch Management Policy (e.g., Critical/High CVSS patches within 48-72 hours of validated NATO Security Technical Implementation Guide (STIG) release).
*   **Control:** Vulnerability scans are conducted weekly for external and monthly for internal systems. Red Team exercises are conducted twice annually.
*   **Source:** NIST SP 800-53 (RA-5, SI-2, RA-5), NATO Security Directives.

### 5.6. Incident Response
*   **Control:** All personnel must report any suspected security incident immediately to the 24/7 SOC. The documented IR plan, aligned with NATO CIRC (NCIRC) and host-nation (Romanian) CERT procedures, must be followed.
*   **Control:** All incidents are reported to the NATO Communications and Information Systems Group (NCISG) and the host nation CERT (CERT-RO) as required by SOFA and host-nation law (Romanian Law 362/2018).
*   **Source:** NATO Cyber Incident Response SOPs, Romanian Cybersecurity Law 362/2018.

### 5.7. Supply Chain & Contractor Security
*   **Control:** All contractors and vendors must be vetted and on the NATO-approved vendor list. Supply chain risk assessments are mandatory for all COMSEC and CIS equipment.
*   **Control:** Contractor personnel with system access require the same level of security clearance and training as military personnel.
*   **Source:** NATO Security Principles (AC/35-D/1015), Host Nation Security Agreement.

## 6. Exceptions

Any exception to this policy requires a formal, written risk acceptance from the Detachment Commander, based on a risk assessment by the ISSM. Exceptions are time-bound and subject to compensating controls.

## 7. Monitoring and Review

*   The ISSM will conduct a quarterly review of policy compliance.
*   This policy will be reviewed annually by the ISSM and updated to reflect changes in NATO policy, host-nation law, or the threat landscape.
*   Effectiveness will be measured via audit reports, red team exercise results, and incident response metrics.

## 8. Enforcement

Violations of this policy may result in disciplinary action under the applicable national or NATO disciplinary codes, up to and including loss of security clearance, termination of network access, and legal action under the NATO Status of Forces Agreement (SOFA) or host-nation law.

## 9. References & Compliance Framework

This policy ensures compliance with, and draws authority from:
- NATO Security Policy (C-M(2002)49 and successors)
- NATO Cyber Defence Pledge (2016, 2021)
- NATO Security Indoctrination (AC/35-D/1015)
- NATO Security within NATO (AC/35-D/1015)
- NATO Personnel Security (AC/35-D/1029)
- NATO Technical Security & Implementation Directive (AC/322-D(2017)0009)
- Romanian Cybersecurity Law 362/2018 (and NIS2 transposition)
- NATO SOFA and Host Nation Support Agreement with Romania
- NIST Cybersecurity Framework 2.0
- ISO/IEC 27001:2022

---
**Policy Approved:**

**Detachment Commander Signature:** _________________________
**Date:** _________________________

**Information Systems Security Manager (ISSM):** _________________________
**Date:** _________________________

---
**Document Control**
| Version | Date | Author | Changes |
| :--- | :--- | :--- | :--- |
| 1.0 | [Date] | [Name, ISSM] | Initial Release for ACO Detachment |

</policy>

**Sources Consulted & References:**
*   **RELEVANT DOCUMENTS (Provided Context):** The provided context documents, particularly the NATO and national policy references (e.g., AC/35-D/1015, AC/322-D/2017/0009) and the Romanian legal framework, were used to establish the regulatory foundation and specific control requirements.
*   **NIST Cybersecurity Framework 2.0 & NIST SP 800-53:** Provided the control families (Identify, Protect, Detect, Respond, Recover) and specific control identifiers (e.g., AC-2, RA-5) used to structure the policy's technical and administrative controls.
*   **NATO & Host-Nation Directives:** The policy is explicitly built upon the cited NATO security policies (C-M(2002)49, AC/35-D/1015, etc.) and acknowledges compliance with host-nation (Romanian) law, as per the provided organizational profile.
*   **ISO/IEC 27001:2022:** The policy structure and principles of continuous improvement, risk management, and asset management align with the ISO 27001 framework, as referenced in the organizational profile.
