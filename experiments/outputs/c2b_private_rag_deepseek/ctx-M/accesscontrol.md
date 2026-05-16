---
config: C2b
context_id: ctx-M
policy_id: P3
policy_name: Access Control Policy
policy_short: accesscontrol
metadata:
  config: C2b
  model: deepseek-ai/DeepSeek-V3.2
  input_tokens: 25891
  output_tokens: 2116
  total_tokens: 28007
  latency_s: 53.096
  tool_calls:
  - rag_retrieval
  raw_provider_id: 4527f00b-1d51-472e-bd51-898d3cb84e60
  chunks_retrieved: 5
  server_version: 1.3.4
sources_count: 3
sources:
- type: kb_source
  source: ./datadir-plus-templates/access_control_policy.docx
  title: ./datadir-plus-templates/access_control_policy.docx
- type: kb_source
  source: ./datadir-plus-templates/asset_management.docx
  title: ./datadir-plus-templates/asset_management.docx
- type: kb_source
  source: ./datadir-plus-templates/5.json
  title: Cyber Rapid Response Teams​
prompt_chars: 6039
answer_chars: 9329
generated_at_unix: 1778503947
---

<policy title="NATO Detachment Access Control Policy">

| Field | Value |
|-------|-------|
| **Document ID** | POL-AC-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | NATO RESTRICTED (NR) |
| **Owner** | Information Systems Security Manager (ISSM) |
| **Approved by** | Detachment Commander |
| **Approval Date** | 2023-10-27 |
| **Next Review Date** | 2024-10-27 |
| **Review Cycle** | Annual (or upon significant change in accreditation) |

---

## 1. Purpose

This Access Control Policy establishes the mandatory requirements for controlling and monitoring access to the information systems, networks, and data of the NATO Detachment (the "Detachment"). The policy enforces the principles of "need-to-know" and "least privilege" across all classification domains (NU, NR, NS, MISSION SECRET). It ensures that only authorized, authenticated, and vetted personnel and systems can access information assets, in strict compliance with NATO security policies, host-nation regulations, and the principle of data sovereignty. This policy supports the operational security (OPSEC) and mission assurance of the Detachment.

## 2. Scope

This policy applies to:
- All personnel assigned to or supporting the Detachment, including military, civilian, and contractor personnel.
- All information systems, networks, and data repositories owned, operated by, or in the custody of the Detachment.
- All classification domains (NU, NR, NS, MISSION SECRET) and cross-domain solutions.
- All physical and logical access points to Detachment facilities, networks, and information.

## 3. Roles and Responsibilities

### 3.1. Detachment Commander
- Holds ultimate responsibility for the security of Detachment information assets.
- Approves exceptions to this policy in writing, in consultation with the ISSM and Legal Advisor.

### 3.2. Information Systems Security Manager (ISSM)
- Owns, maintains, and enforces this policy.
- Oversees the implementation of access controls and periodic access reviews.
- Investigates and reports on access control violations.

### 3.3. Information Systems Security Officer (ISSO)
- Implements and manages technical access controls.
- Manages user account lifecycle (provisioning, modification, revocation).
- Conducts regular access reviews and audits.

### 3.4. System/Network Administrators
- Implement and maintain technical controls as directed by the ISSM/ISSO.
- Enforce access control rules on systems and network devices.

### 3.5. All Personnel
- Comply with all access control procedures.
- Report any suspected violations or anomalies immediately.

## 4. Policy Principles & Requirements

### 4.1. Foundational Principles
- **Need-to-Know:** Access is granted solely based on operational necessity for mission performance.
- **Least Privilege:** Users and systems are granted the minimum level of access necessary to perform their duties.
- **Defense in Depth:** Access controls are applied at multiple layers (physical, network, host, application).
- **Separation of Duties:** Critical functions (e.g., access approval and implementation) are separated.
- **Non-Repudiation:** All access events, especially for privileged actions, must be attributable to a unique, authenticated identity.

### 4.2. Access Control Requirements

#### 4.2.1. Identification & Authentication (I&A)
1.  **Multi-Factor Authentication (MFA) is mandatory** for all access to NR, NS, and MISSION SECRET domains. This shall be a combination of:
    - Something you have (e.g., NATO-approved smart card/CAC).
    - Something you know (e.g., a strong PIN/passphrase).
    - Biometric verification (where supported and for specific high-assurance use cases).
    *Reference: NATO AC/35-D/1029 (Security within NATO), NIST SP 800-63B, ISO/IEC 27001:2022 A.9.4.2*

2.  **Smart Card (PKI) Authentication** is the primary method for logical access. All personnel must use their NATO-issued smart card for authentication to any classified network or system.

3.  **Session Management:** User sessions shall automatically lock after 15 minutes of inactivity and require re-authentication. Sessions shall be terminated after a maximum of 12 hours.

#### 4.2.2. Authorization & Access Control Models
1.  **Role-Based Access Control (RBAC):** Access to information is based on the user's role within the Detachment (e.g., Intelligence Analyst, Logistics Officer, System Administrator). Roles are defined by the ISSM in accordance with NATO Standardization Agreements (STANAGs).
2.  **Mandatory Access Control (MAC):** The primary model for classified information. Access decisions are based on the classification of the information (NU, NR, NS, MISSION SECRET) and the clearance/need-to-know of the user. The system (not the user or data owner) is the ultimate authority.
3.  **Rule-Based Access Control:** Applied at network and application layers (e.g., firewall rules, cross-domain guard policies).

#### 4.2.3. Physical Access Control
1.  **Facility Access:** Access to Sensitive Compartmented Information Facilities (SCIFs) and server rooms requires a valid NATO ID, PIN, and biometric verification (e.g., fingerprint). Access logs are retained for 90 days.
2.  **Two-Person Integrity (TPI):** Mandatory for all COMSEC key material handling, as per NATO AC/35-D/1015. Access to high-grade COMSEC requires two authorized, cleared individuals present.
3.  **Escort Policy:** Visitors and uncleared personnel must be escorted by a vetted, cleared, and authorized escort at all times within controlled areas.

#### 4.2.4. Network & System Access
1.  **Network Segmentation:** Strict network segmentation (NU, NR, NS, MISSION SECRET) enforced by firewalls and cross-domain solutions (CDS). Data transfer between domains only via accredited cross-domain solutions (CDS).
2.  **Privileged Access:** Privileged accounts (e.g., Domain Admin, root) are strictly controlled. Use is logged, monitored, and requires justification for each session. Privileged sessions are recorded.
3.  **Remote Access:** Remote access to any Detachment system from a non-Detachment network (e.g., from a NATO HQ) requires a VPN connection with MFA and is only permitted from authorized, NATO-managed devices.

#### 4.2.5. Account Management
1.  **Lifecycle Management:** User accounts are created, modified, and disabled in accordance with personnel status (onboarding, transfer, termination). Account creation requires a signed request from the unit commander or designated approving authority.
2.  **Timely Revocation:** Access must be revoked within 24 hours of a user's transfer, mission end, or termination.
3.  **Service Accounts:** Non-personal accounts (e.g., for applications) must have a designated owner, and their use must be logged and reviewed quarterly.

### 4.3. Access Reviews & Auditing
1.  **Quarterly Access Reviews:** The ISSO will conduct and document a quarterly review of all user accounts and access rights, especially for privileged accounts and personnel with access to NS and MISSION SECRET information.
2.  **Audit Logging:** All authentication events (success/failure), privilege use, and policy changes must be logged. Logs are to be stored centrally, protected from tampering, and retained for a minimum of 365 days for analysis and incident response.
3.  **Cross-Domain Access:** Any data transfer between classification levels (e.g., NR to NS) must be performed via an accredited cross-domain solution (CDS) and logged. All such transfers require dual authorization.

## 5. Exceptions

Any exception to this policy requires a formal, written waiver from the Detachment Commander, based on a risk assessment by the ISSM. The waiver must include a specific expiration date and a plan for compensating controls. All waivers are reviewed at least annually.

## 6. Monitoring & Review

The ISSM/ISSO will:
- Conduct monthly reviews of access logs for anomalies.
- Perform a quarterly audit of user access rights against personnel rosters and clearance levels.
- Conduct an annual review of this policy and its effectiveness, updating it to reflect changes in NATO policy, host-nation law (Romanian Law 58/2019, NIS2), and the threat landscape.

## 7. Compliance & Enforcement

Violations of this policy may result in disciplinary action, revocation of access, administrative action, or legal proceedings in accordance with NATO regulations and host-nation agreements (NATO SOFA). Deliberate or negligent violations will be reported to the chain of command and the appropriate security office.

## 8. References & Compliance

This policy is designed to comply with:
- **NATO:** AC/35-D/1015 (Security within NATO), AC/35-D/1029 (Personnel Security), AJP-3.20 (Cyberspace Operations).
- **NATO Cyber Defence Pledge (2016).**
- **Romanian Legislation:** Law 58/2019 (Cybersecurity) and GDPR (for personal data of EU personnel).
- **International Standards:** ISO/IEC 27001:2022, NIST Cybersecurity Framework v1.1, NIST SP 800-53 (Security Controls).
- **NATO STANAGs** for communications and information security.

## 9. Revision History

| Version | Date | Author | Changes |
| :--- | :--- | :--- | :--- |
| 1.0 | 2023-10-27 | ISSM | Initial Policy Release |

---
*This document is the property of the NATO Detachment. Unauthorized distribution is prohibited. Classification: NATO RESTRICTED.*

</policy>
