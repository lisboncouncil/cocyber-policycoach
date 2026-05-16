---
config: C2b
context_id: ctx-H
policy_id: P5
policy_name: General Cybersecurity Policy
policy_short: infosec
metadata:
  config: C2b
  model: deepseek-ai/DeepSeek-V3.2
  input_tokens: 25627
  output_tokens: 2189
  total_tokens: 27816
  latency_s: 66.655
  tool_calls:
  - rag_retrieval
  raw_provider_id: fa615e2a-64e7-4164-aaea-07cd6b5963a2
  chunks_retrieved: 5
  server_version: 1.3.4
sources_count: 4
sources:
- type: kb_source
  source: ./datadir-plus-templates/cybersecurity_policy_BASIC.docx
  title: ./datadir-plus-templates/cybersecurity_policy_BASIC.docx
- type: kb_source
  source: ./datadir-plus-templates/asset_management.docx
  title: ./datadir-plus-templates/asset_management.docx
- type: kb_source
  source: ./datadir-plus-templates/9.json
  title: 'The Sector CSIRT Framework: Developing Sector-Based Incident Response Capabilities'
- type: kb_source
  source: ./datadir-plus-templates/1.json
  title: Best Practices for Cyber Crisis Management
prompt_chars: 4683
answer_chars: 8929
generated_at_unix: 1778503798
---

<policy title="Cybersecurity Policy for Ospedale Civile di [Province Name]">

| Field | Value |
|-------|-------|
| **Document ID** | POL-001 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Internal |
| **Owner** | [To be assigned to Head of IT or designated CISO function] |
| **Approved by** | [To be signed by Hospital Director] |
| **Approval Date** | [DD/MM/YYYY] |
| **Next Review Date** | [DD/MM/YYYY] |
| **Review Cycle** | Annual |

---

## 1. Purpose

This Cybersecurity Policy establishes the framework for protecting the information assets of Ospedale Civile di [Province Name] (hereinafter "the Hospital"). It defines the minimum security requirements to protect the confidentiality, integrity, and availability of information and information systems, in compliance with the Italian and European regulatory framework, including GDPR (EU 2016/679), the Italian Privacy Code (D.Lgs. 196/2003 as amended), the NIS2 Directive (EU 2022/2555), and AGID guidelines. This policy is aligned with the principles of ISO/IEC 27001:2022 and the NIST Cybersecurity Framework 2.0, adapted to the operational and resource constraints of a public healthcare provider.

## 2. Scope

This policy applies to:
*   All employees, contractors, consultants, and third-party personnel with access to Hospital information systems.
*   All information assets owned, managed, or processed by the Hospital, including but not limited to the Cartella Clinica Elettronica (FSE), PACS/RIS, LIS, ADT, and pharmacy management systems.
*   All Hospital-owned or managed devices, networks, and data, whether on-premises or accessed remotely.
*   Clinical, administrative, and technical departments across all wards and units.

## 3. Roles and Responsibilities

*   **Hospital Director:** Ultimately accountable for cybersecurity governance and resource allocation.
*   **Information Security Officer (ISO) / CISO (to be designated):** Owns this policy, oversees its implementation, and reports to the Hospital Director. Acts as the Data Protection Officer (DPO) liaison.
*   **IT Manager / MSP (Managed Service Provider):** Responsible for the technical implementation, monitoring, and day-to-day operation of security controls.
*   **Department Heads:** Responsible for policy enforcement and staff compliance within their units.
*   **All Personnel:** Responsible for adhering to this policy, reporting incidents, and completing required training.

## 4. Core Cybersecurity Principles

1.  **Risk-Based Approach:** Security measures shall be proportionate to the value and sensitivity of the information and the associated risks, as mandated by GDPR (Art. 32) and AGID guidelines.
2.  **Defense in Depth:** Security is implemented in multiple, overlapping layers (network, endpoint, data, user).
3.  **Least Privilege:** Access to information and systems is granted on a strict need-to-know and need-to-use basis.
4.  **Shared Responsibility:** Cybersecurity is the responsibility of every individual with access to Hospital systems.
5.  **Resilience & Continuity:** Security measures must support, not hinder, 24/7 clinical operations. Recovery Time Objectives (RTOs) for critical systems (EHR: 4h, ADT/PS: 1h) must be met.

## 5. Policy Requirements & Controls

### 5.1. Asset & Data Management
*   **Control 1.1:** An asset inventory of all hardware, software, and critical data (especially sensitive patient data) shall be maintained and updated quarterly. *[Source: ISO/IEC 27001:2022 A.5.9, AGID Linee Guida]*
*   **Control 1.2:** All sensitive data, particularly Special Category Data under GDPR (health records), must be classified and encrypted at rest and in transit. *[Source: GDPR Art. 9, Codice Privacy Art. 2-ter]*

### 5.2. Access Control & Identity Management
*   **Control 2.1:** Access to all systems, especially the Cartella Clinica Elettronica, PACS, and ADT, shall be controlled via the on-premise Active Directory, federated where possible with regional SPID/CIE systems. *[Source: NIST CSF PR.AC-1]*
*   **Control 2.2:** The principle of least privilege shall be enforced. Shared accounts are prohibited for clinical systems. *[Source: ISO/IEC 27001:2022 A.5.15, NIST CSF PR.AC-4]*
*   **Control 2.3:** Multi-Factor Authentication (MFA) is mandatory for all remote access (VPN, clinical portals) and for all administrative/privileged accounts. *[Source: NIST SP 800-63B, AGID Misure Minime]*

### 5.3. Network Security
*   **Control 3.1:** The existing segmentation (clinical VLAN, admin VLAN, PACS) shall be maintained and enhanced to isolate critical systems (e.g., PACS island). Micro-segmentation for clinical IoT devices shall be planned. *[Source: NIST CSF PR.AC-5, IEC 62443 for IACS]*
*   **Control 3.2:** All traffic, especially to/from legacy systems (Windows kiosks), shall be filtered by the UTM. Outbound connections shall be monitored for data exfiltration attempts.

### 5.4. Vulnerability & Patch Management
*   **Control 4.1:** A formal, risk-based patch management process shall be established. Critical and High-severity patches for systems like the 35 legacy Windows kiosks shall be applied within 30 days of release, following testing. *[Source: NIST CSF DE.CM-8, AGID Misure Minime]*
*   **Control 4.2:** An annual vulnerability scan, supplemented by the MSP, shall be performed. The MSP is responsible for monthly vulnerability scanning of internet-facing assets. *[Source: ISO/IEC 27001:2022 A.8.8]*

### 5.5. Data Protection & Backup
*   **Control 5.1:** The existing nightly backup to NAS and weekly off-site tape rotation shall continue. A full Disaster Recovery test, incorporating the RTOs for EHR (4h) and ADT (1h), shall be conducted at least every 18 months. The 18-month gap since the last test is a non-conformity and must be addressed. *[Source: ISO 22301, Business Continuity]*
*   **Control 5.2:** All backups shall be encrypted, and their integrity verified quarterly.

### 5.6. Incident Response & Training
*   **Control 6.1:** A formal, documented incident response plan shall be created, moving beyond the current ad-hoc process. The plan must define roles for the 1.5 FTE IT staff and the MSP during a ransomware or data breach event. *[Source: NIST CSF RS.RP-1, NIS2 Directive Art. 21.1]*
*   **Control 6.2:** All staff shall receive 2 hours of mandatory cybersecurity awareness training annually, with a specific focus on phishing and the secure handling of patient data. Clinical staff receive additional onboarding training. *[Source: GDPR Art. 39, AGID guidelines]*

### 5.7. Third-Party Risk
*   **Control 7.1:** Contracts with the MSP and other key suppliers (e.g., medical device vendors) must include specific security and data protection clauses aligned with this policy and NIS2 requirements for essential entities. *[Source: NIS2 Directive (EU) 2022/2555]*

## 6. Exceptions & Enforcement

Requests for exceptions to this policy must be submitted in writing to the IT Manager and the designated CISO/DPO, with a full risk assessment and proposed compensating controls. Violations of this policy may result in disciplinary action, up to and including termination and legal action, in accordance with Italian law (D.Lgs. 196/2003).

## 7. Monitoring & Review
The IT Manager, in conjunction with the MSP, will provide a quarterly security status report to the Hospital Director. This policy shall be reviewed and updated at least annually, or following any significant security incident or regulatory change.

## 8. References & Source Mapping
This policy is informed by the following frameworks and regulations, which are incorporated by reference:
*   **GDPR (EU 2016/679) & Italian Privacy Code (D.Lgs. 196/2003):** Articles 5, 25, 32, 39. Mandate data protection by design, security of processing, and breach notification.
*   **NIS2 Directive (EU 2022/2555):** Art. 21.1 requires "appropriate and proportionate technical and organisational measures" for essential entities like hospitals.
*   **AGID Linee Guida per la Sicurezza ICT nelle PA:** Provides the baseline technical controls for public administration in Italy.
*   **NIST Cybersecurity Framework 2.0:** Provides the core structure (Govern, Identify, Protect, Detect, Respond, Recover) and is referenced for controls (e.g., PR.AC-1, DE.CM-8).
*   **ISO/IEC 27001:2022:** Provides the structure for the ISMS and specific Annex A controls (e.g., A.5.9, A.5.15, A.8.8).
*   **NIST SP 800-63B:** Informs the requirements for strong authentication (Control 2.3).

---
**Approval:**

Hospital Director: ________________________ Date: ___/___/______

Designated CISO/Security Officer: ________________________ Date: ___/___/______

</policy>

**Sources Consulted:**
*   *[1] Cybersecurity Policy (Basic) Template*
*   *[2] Asset Management Policy Template*
*   *[3] The Sector CSIRT Framework (for incident response structure)*
*   *[4] Best Practices for Cyber Crisis Management (NIS2 Art. 21.1)*
