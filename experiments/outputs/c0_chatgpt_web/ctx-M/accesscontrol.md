---
config: C0+web
context_id: ctx-M
policy_id: P3
policy_name: Access Control Policy
policy_short: accesscontrol
metadata:
  config: C0+web
  model: gpt-4.1-2025-04-14
  input_tokens: 1660
  output_tokens: 2241
  total_tokens: 3901
  latency_s: 24.366
  tool_calls: []
  raw_provider_id: resp_07b704bc9e8a5e950069fb70e2b7a0819186f834441695e362
sources_count: 0
sources: []
prompt_chars: 6039
answer_chars: 8825
generated_at_unix: 1778086138
---

---

# NATO Multinational Military Detachment  
**Access Control Policy**

**Organisation:** NATO Multinational Military Detachment, Romania (under SHAPE operational control)  
**Policy Owner:** Information Systems Security Manager (ISSM), J6  
**Effective Date:** 2024-07-01  
**Review Cycle:** Annual (or upon major regulatory/command change)  
**Classification:** NATO RESTRICTED

---

## 1. Purpose

This Access Control Policy establishes the principles, responsibilities, and controls for managing access to information systems, networks, and classified information within the NATO Multinational Military Detachment in Romania. The policy ensures compliance with NATO, host-nation, and coalition regulatory requirements, and implements best practices for safeguarding sensitive assets against unauthorised access, consistent with the mission to defend NATO networks and support allied operations.

---

## 2. Scope

This policy applies to:
- All personnel assigned, attached, or contracted to the detachment (military, civilian, and contractors).
- All information systems, communication and information systems (CIS), and networks under the detachment’s operational control, across all classification domains (NU, NR, NS, MISSION SECRET).
- Physical and logical access to information, systems, and facilities, including SCIFs and COMSEC repositories.
- All forms of access (physical, logical, remote, and cross-domain).

---

## 3. Roles and Responsibilities

| Role                                      | Responsibility                                                                                                  |
|-------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| ISSM (Policy Owner)                       | Policy implementation, periodic review, compliance monitoring, and reporting to command and NCIRC.              |
| Security Team (25 FTE)                    | Day-to-day access administration, monitoring, audit, and incident response.                                      |
| System Owners                             | Enforce domain-specific access controls, maintain user access logs, and support audits.                         |
| COMSEC Custodian                          | Manage COMSEC material access, enforce dual-key and two-person integrity.                                       |
| All Personnel                             | Adhere to access control procedures, report violations, and complete mandatory training.                        |
| Host Nation Security Liaison              | Ensure compliance with host-nation law for civilian/contractor data; liaise on GDPR and local cybersecurity law.|

_Citations: [NATO C-M(2002)49]; [NIST CSF ID.GV-2]; [ISO/IEC 27001:2022, cl. 5.3]; [GDPR Art. 5, 32]_

---

## 4. Principles

- **Need-to-Know and Least Privilege:** Access is granted strictly on the basis of mission requirement, clearance, and role, with a default-deny posture.  
  _[NATO C-M(2002)49, sec. 6]; [ISO/IEC 27001 cl. 7.2, 9.4.1]; [NIST CSF PR.AC-4]_

- **Separation of Classification Domains:** Strict mandatory separation of network domains (NU/NR/NS/MISSION SECRET) enforced by technical and procedural means.
  _[NATO AC/322-D(2017)0009, sec. 3.2]; [NIST CSF PR.AC-5]_

- **Multi-factor Authentication (MFA):** All logical access requires MFA (smart card/PIN) appropriate to domain sensitivity.
  _[NATO INFOSEC Dir. 3.2.2]; [NIST CSF PR.AC-7]; [ISO 27001 cl. 9.4.2]_

- **Dual-Control for High-Sensitivity Assets:** Dual-key/two-person integrity required for high-grade COMSEC and release of certain operational orders.
  _[NATO AC/322-D(2017)0009, sec. 4.5]; [COMSEC Policy 70-1]_

- **Auditable Access:** All access events are logged and retained according to classification and regulatory requirements.
  _[ISO 27001 cl. 9.4.3]; [NATO C-M(2002)49, sec. 10.5]; [NIST CSF PR.PT-1]_

---

## 5. Policy Requirements and Controls

### 5.1 Access Authorization

- **Account Provisioning:** Grant access only following formal authorisation by the ISSM or delegated authority, based on verified clearance, need-to-know, and role.  
  _[NATO AC/35-D/1015, sec. 4.1]; [ISO 27001 cl. 9.2.2]; [NIST CSF PR.AC-1]_

- **Personnel Security Screening:** All users must have a valid NATO security clearance or host-nation equivalent at or above the data classification handled. Contractors must clear host-nation security vetting.  
  _[NATO AC/35-D/1029]; [Host Nation Law 58/2019]_

- **Contractor Access:** Contractor access is limited to permitted domains and functions, subject to additional oversight and periodic review.  
  _[NATO C-M(2002)49, sec. 7]; [GDPR Art. 28]_

### 5.2 Authentication and Identification

- **Strong Authentication:** All user access to classified domains (NR/NS/MISSION SECRET) requires PKI-based smart card authentication with unique user IDs.  
  _[NATO INFOSEC Dir. 3.2.2]; [ISO 27001 cl. 9.4.2]; [NIST CSF PR.AC-7]_

- **No Shared Accounts:** Shared, group, or anonymous accounts are prohibited except for explicitly justified service accounts, subject to ISSM approval and enhanced monitoring.  
  _[NATO C-M(2002)49, sec. 8.2]; [ISO 27001 cl. 9.2.3]_

### 5.3 Access Enforcement

- **Access Controls:** Implement Role-Based Access Control (RBAC) for all systems, mapped to organisational structure and mission roles.  
  _[NIST CSF PR.AC-4]; [ISO 27001 cl. 9.2.1]_

- **Cross-Domain Transfers:** All information transfers between classification domains must use accredited NATO Cross-Domain Solutions (CDS) and conform to originator control (ORCON) and need-to-know.  
  _[NATO AC/322-D(2017)0009, sec. 5.2]; [NIST CSF PR.DS-5]_

- **Physical Access:** Physical access to SCIFs and secure areas is enforced via badge access control and logged; dual-person entry for NS and above.  
  _[NATO AC/35-D/1015, sec. 6.1]; [ISO 27001 cl. 9.1.2]_

### 5.4 Access Review and Revocation

- **Periodic Review:** User access rights are reviewed at least quarterly, and immediately upon change of role, departure, or security incident.  
  _[ISO 27001 cl. 9.2.5]; [NIST CSF PR.AC-1]_

- **Immediate Revocation:** Access rights are revoked within 4 hours of termination, transfer, or loss of clearance for classified systems.  
  _[NATO C-M(2002)49, sec. 9.1]; [ISO 27001 cl. 9.2.6]_

### 5.5 Privileged Access and Sensitive Operations

- **Least Privilege:** Privileged accounts (admins, COMSEC custodians) are restricted to named personnel, with duties segregated to prevent single-person control of critical functions.  
  _[NIST CSF PR.AC-6]; [ISO 27001 cl. 5.7, 8.1.4]_

- **Session Controls:** Privileged sessions must be monitored and logged in real time; all admin actions are auditable.  
  _[NATO C-M(2002)49, sec. 10.5]; [ISO 27001 cl. 5.10]_

### 5.6 Access to Personal Data

- **GDPR Compliance:** Access to personal data (EU civilian/contractor) is limited to authorised processing on a need-to-know basis, with logging and data minimisation.  
  _[GDPR Art. 5, 25, 32]; [Host Nation Law 58/2019]_

- **Data Subject Rights:** Data subjects may request access review or rectification per GDPR and host-nation law, subject to operational and security constraints.  
  _[GDPR Art. 15-20]_

---

## 6. Exceptions

- Requests for exceptions must be documented, justified by mission necessity, and formally approved by the ISSM in consultation with the security team and, where needed, with SHAPE/NCIRC or host-nation authorities.
- Emergency access (break-glass) must be logged, justified, and subject to post-incident review within 48 hours.
- No exceptions to national security clearance requirements or dual-control for high-grade COMSEC.

---

## 7. Monitoring and Review

- **Continuous Monitoring:** 24/7 SOC monitors access events, with alerts for anomalous or unauthorised access.  
  _[NIST CSF DE.CM-7]; [ISO 27001 cl. 9.4.3]_

- **Audit:** Quarterly internal audits and external audits as required by NATO and host-nation authorities.
- **Policy Review:** The ISSM reviews this policy annually or upon change in regulatory, command, or mission requirements.
- **Incident Response:** All access violations are reported and investigated per the documented IR plan (aligned with NCIRC).

---

## 8. References

- NATO C-M(2002)49 (NATO Security Policy)
- NATO AC/35-D/1015 (Security within NATO)
- NATO AC/35-D/1029 (Personnel Security)
- NATO AC/322-D(2017)0009 (NATO INFOSEC Technical Directive)
- Allied Joint Doctrine for Cyberspace Operations (AJP-3.20)
- NIST Cybersecurity Framework (CSF) v2.0
- ISO/IEC 27001:2022, ISO/IEC 27002:2022
- Romanian Law 58/2019 (Cybersecurity), NIS2 Transposition
- GDPR (EU 2016/679)
- NATO COMSEC Policy 70-1

---

**Approved by:**  
[Signature block for ISSM/J6]  
**Date:** 2024-07-01

---
