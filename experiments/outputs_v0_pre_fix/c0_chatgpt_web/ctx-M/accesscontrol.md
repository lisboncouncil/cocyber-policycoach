---
config: C0+web
context_id: ctx-M
policy_id: P4
policy_name: Access Control Policy
policy_short: accesscontrol
metadata:
  config: C0+web
  model: gpt-4.1-2025-04-14
  input_tokens: 1309
  output_tokens: 2469
  total_tokens: 3778
  latency_s: 16.006
  tool_calls: []
  raw_provider_id: resp_02ea5efeee4194d60069fb69cc787c819494ce9d37ed1c1cb8
sources_count: 0
sources: []
prompt_chars: 4950
answer_chars: 9184
generated_at_unix: 1778084316
---

---

# NATO Multinational Detachment Romania  
**Access Control Policy**  
**Document Reference:** NMD-ROU-ACPOL-2024  
**Effective Date:** 2024-07-01  
**Policy Owner:** Information Systems Security Manager (ISSM), J6  
**Review Cycle:** Annual or upon major organisational, regulatory, or threat landscape change

---

## 1. Purpose

This Access Control Policy establishes the principles, roles, and controls necessary to ensure that only authorised personnel can access NATO, mission, and supporting information and systems, consistent with the need-to-know principle and regulatory obligations. The policy mitigates threats from state-sponsored APTs, insider threats, supply chain compromise, and cross-domain spillage, in line with NATO and host-nation requirements.

---

## 2. Scope

This policy applies to:
- All NATO, national, and contractor personnel assigned to the NATO Multinational Detachment Romania (NMD-ROU), including military, NATO civilian staff, and cleared contractors.
- All information systems, networks, and data (NU, NR, NS, MISSION SECRET) under NMD-ROU operational control.
- All physical and logical access to facilities, IT systems, COMSEC material, and classified information, regardless of location or medium.
- All access control systems and tools, including PKI, cross-domain solutions, COMSEC controls, and physical barriers.

---

## 3. Roles and Responsibilities

**3.1 Information Systems Security Manager (ISSM, J6 Chain):**  
- Owns and maintains the policy.  
- Ensures alignment with NATO, host-nation, and international frameworks.  
- Approves exceptions and oversees access reviews.  
- Reports on compliance to the Commander and higher authorities.  
  *[C-M(2002)49; ISO/IEC 27001:2022 cl.5.3]*

**3.2 Information System Security Officers (ISSOs):**  
- Implement access controls per this policy.  
- Conduct periodic access reviews, report non-conformities.  
  *[ISO/IEC 27001:2022 cl.5.3, 9.2]*

**3.3 System Administrators:**  
- Enforce technical access controls.  
- Maintain auditable logs of access and changes.  
  *[NIST CSF PR.AC-1; ISO/IEC 27002:2022 cl.8.2]*

**3.4 Human Resources/Civilian Personnel Office:**  
- Ensure personnel security clearances, onboarding/offboarding processes.  
  *[AC/35-D/1029; ISO/IEC 27002 cl.5.7]*

**3.5 All Users:**  
- Comply with this policy and report suspected access violations.  
  *[NATO Security Policy, C-M(2002)49; ISO/IEC 27002 cl.5.1]*

---

## 4. Principles

**4.1 Need-to-Know & Least Privilege**  
Access is granted strictly on the basis of operational necessity, minimum sufficient rights, and valid clearance.  
*[C-M(2002)49; AJP-3.20; ISO/IEC 27001:2022 cl.5.2, 8.1; NIST CSF PR.AC-4]*

**4.2 Separation of Domains**  
Enforce strict technical and procedural separation between NU, NR, NS, and MISSION SECRET domains.  
*[AC/322-D(2017)0009; NIST CSF PR.AC-5]*

**4.3 Accountability and Auditability**  
All access must be attributable to a unique individual and auditable.  
*[ISO/IEC 27001:2022 cl.8.3, 10.1; NIST CSF DE.CM-7]*

**4.4 Compliance with Legal and Regulatory Requirements**  
All access arrangements comply with NATO, host-nation, and EU (GDPR) requirements, within SOFA limitations.  
*[GDPR Art.5, 32; Law 58/2019; NIS2; SOFA; C-M(2002)49]*

---

## 5. Access Control Requirements and Controls

### 5.1 User Registration, De-registration, and Lifecycle Management

- **Formal User Registration and De-registration:**  
  Access to any NMD-ROU system or facility must be formally requested, approved, and tracked through an auditable process. De-registration must occur immediately upon termination of assignment, contract, or clearance.  
  *[ISO/IEC 27001:2022 cl.8.2; NIST CSF PR.AC-1; AC/35-D/1015]*

- **Periodic Access Reviews:**  
  Access rights are reviewed at least quarterly by ISSO for each domain, and upon change of role, clearance, or operational assignment.  
  *[ISO/IEC 27001:2022 cl.8.2; NIST CSF PR.AC-4]*

- **Personnel Security Prerequisite:**  
  No access to classified systems or COMSEC unless valid NATO or national clearance is confirmed per AC/35-D/1029.  
  *[AC/35-D/1029]*

### 5.2 Authentication and Identification

- **PKI-based Authentication:**  
  All logical access to classified domains (NR, NS, MISSION SECRET) requires PKI-based smart card authentication (CAC-equivalent), with domain-specific certificates.  
  *[NIST CSF PR.AC-1; ISO/IEC 27002:2022 cl.8.3.2]*

- **No Cross-Domain Federation:**  
  No identity federation or reuse of credentials across classification domains.  
  *[AC/322-D(2017)0009]*

- **Two-Factor Authentication (2FA):**  
  2FA is mandatory for administrative access and remote access to any domain.  
  *[ISO/IEC 27002:2022 cl.8.3.3; NIST CSF PR.AC-7]*

### 5.3 Authorisation and Access Rights Management

- **Role-Based Access Control (RBAC):**  
  Access permissions are assigned according to formal roles, with rights minimised to operational need.  
  *[NIST CSF PR.AC-4; ISO/IEC 27002:2022 cl.8.1.2]*

- **Need-to-Know and ORCON:**  
  Access to intelligence or sensitive products is additionally governed by Originator Control (ORCON) and explicit need-to-know validation.  
  *[C-M(2002)49; AC/35-D/1015]*

- **Dual-Key and Two-Person Integrity (TPI):**  
  For high-grade COMSEC and selected operational orders, dual-key procedures and TPI are enforced; access or action requires two cleared individuals present, and actions are logged.  
  *[NATO COMSEC Policy; ISO/IEC 27001:2022 cl.8.3.3]*

### 5.4 Physical Access Controls

- **Controlled Site Perimeter & Access Points:**  
  Physical access to sites hosting classified or COMSEC material is controlled by badge readers, guard force, and sign-in/out log.  
  *[ISO/IEC 27002:2022 cl.7.1, 7.2]*

- **Visitor Management:**  
  Unescorted access is prohibited for uncleared personnel; all visits logged and subject to escort.  
  *[AC/35-D/1015]*

- **TEMPEST Controls:**  
  Sensitive areas are protected from emanations per NATO TEMPEST standards.  
  *[AC/322-D(2017)0009]*

### 5.5 Cross-Domain and Data Transfer Controls

- **Accredited Cross-Domain Solutions:**  
  All data transfer between domains must use NATO-accredited cross-domain solutions, with data flow logging and sanitisation.  
  *[AC/322-D(2017)0009]*

- **No Manual Transfer Without Authorisation:**  
  Any manual data movement between domains is strictly prohibited except through authorised, logged, and sanitised procedures.  
  *[AC/322-D(2017)0009]*

### 5.6 Privileged Access Management

- **Dedicated Privileged Accounts:**  
  Privileged/administrator accounts are separate from user accounts, with access limited to essential personnel.  
  *[ISO/IEC 27002:2022 cl.8.2.2]*

- **Privileged Session Monitoring:**  
  All privileged sessions are auditable and subject to real-time or retrospective review by the SOC.  
  *[NIST CSF DE.CM-7]*

### 5.7 Supply Chain and Contractor Access

- **Vetted Vendors Only:**  
  Only contractors and vendors cleared through NATO/host-nation processes are granted access, and only to the minimum necessary.  
  *[Law 58/2019; AC/35-D/1029]*

- **Contractor Offboarding:**  
  Contractor access removed immediately upon contract end, with logs retained for audit.  
  *[ISO/IEC 27001:2022 cl.8.2]*

### 5.8 Data Protection and Privacy

- **GDPR and Host Nation Law Compliance:**  
  Civilian and contractor personal data is accessed, processed, and retained only as required for operational purposes, in compliance with GDPR and Romanian cybersecurity law, within SOFA limits.  
  *[GDPR Art.5, 32; Law 58/2019]*

---

## 6. Exceptions

Exception requests to this policy must be submitted in writing to the ISSM, with justification, scope, period, and proposed controls. Approval is required from the ISSM and, where necessary, the Commander. Exceptions are logged and reviewed annually.  
*[ISO/IEC 27001:2022 cl.10.1]*

Unsupported: Any deviation from the above process is unsupported and must not proceed without documented approval.

---

## 7. Monitoring and Review

- **Continuous Monitoring:**  
  All access attempts (successful and unsuccessful) are logged, monitored by the 24/7 SOC, and retained per NATO requirements.  
  *[C-M(2002)49; ISO/IEC 27002:2022 cl.8.15]*

- **Incident Response:**  
  Detected access violations or suspected compromise are escalated per NCIRC processes, with notification to NCSC and host-nation CERT as required.  
  *[NATO Cyber Defence Pledge; AC/322-D(2017)0009]*

- **Annual Review:**  
  This policy is formally reviewed annually or after significant changes in mission, threat, or regulation.  
  *[ISO/IEC 27001:2022 cl.10.1]*

---

## 8. References

- NATO Information Security Policy (C-M(2002)49 and successors)
- AC/35-D/1015 Security within NATO
- AC/35-D/1029 Personnel Security
- AC/322-D(2017)0009 (NATO INFOSEC Technical and Implementation Directive)
- NATO Cyber Defence Pledge 2016
- Allied Joint Doctrine for Cyberspace Operations (AJP-3.20)
- Romanian Cybersecurity Law (Law 58/2019, NIS2 transposition)
- GDPR (Regulation (EU) 2016/679)
- NATO SOFA
- NIST Cybersecurity Framework v2.0
- ISO/IEC 27001:2022, ISO/IEC 27002:2022

---

*End of Document*
