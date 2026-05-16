---
config: C0+web
context_id: ctx-M
policy_id: P5
policy_name: General Cybersecurity Policy
policy_short: infosec
metadata:
  config: C0+web
  model: gpt-4.1-2025-04-14
  input_tokens: 1662
  output_tokens: 2485
  total_tokens: 4147
  latency_s: 25.19
  tool_calls: []
  raw_provider_id: resp_06693230d90ffecc0069fb710e1e88819f81528654a8e9ca94
sources_count: 0
sources: []
prompt_chars: 6053
answer_chars: 8911
generated_at_unix: 1778086183
---

---

# GENERAL CYBERSECURITY POLICY

**Organisation:** NATO Multinational Military Detachment (Romania, SHAPE Operational Control)  
**Effective Date:** 2024-07-01  
**Policy Owner:** Information Systems Security Manager (ISSM), J6  
**Review Cycle:** Annual or upon significant change in NATO/host-nation regulatory framework

---

## 1. Purpose

This policy defines the minimum cybersecurity requirements for the NATO Multinational Military Detachment (hereafter "the Detachment") under the operational control of SHAPE, located in Romania. The policy aims to ensure the confidentiality, integrity, and availability of all NATO, coalition, and national information processed, stored, or transmitted on Detachment-managed systems. It aligns with applicable NATO, host-nation, and international standards, and supports the mission set of cyber defence, CIS operations, signals intelligence, and multinational interoperability.

---

## 2. Scope

This policy applies to:
- All Detachment personnel (military, civilian, contractor) with access to Detachment-managed information systems.
- All IT and communications systems under Detachment control, including NATO, coalition, and national networks (NU, NR, NS, MISSION SECRET domains).
- All physical and logical assets processing, storing, or transmitting classified or sensitive information.
- All activities, processes, and third-party engagements related to information security.

---

## 3. Roles and Responsibilities

| Role | Responsibilities |
|------|------------------|
| **ISSM (J6)** | Policy owner, compliance oversight, technical implementation, liaison with NCIRC/NCSC, approval of exceptions. [C-M(2002)49, AJP-3.20, NIST CSF ID.GV-1] |
| **Security Staff (25 FTE)** | Day-to-day security operations, incident response, training delivery, monitoring, auditing. [AC/322-D(2017)0009] |
| **Command Authority (SHAPE)** | Strategic direction, operational oversight, enforcement of NATO cyber defence directives. [AJP-3.20] |
| **Unit Commanders** | Implementation within subordinate units, dissemination of policy, assurance of compliance. [AC/35-D/1015] |
| **All Personnel** | Adherence to policy, prompt incident reporting, participation in training. [NATO Security Handbook, Art. 25] |
| **Host Nation Liaison** | Coordination on legal/regulatory matters (GDPR, Romanian CSL), interface with host-nation CERT/NCSC. [SOFA, GDPR Art. 4] |

---

## 4. Principles

1. **Defence-in-Depth**: Layered controls across physical, technical, and administrative domains.  
   *[NIST CSF PR.AC, ISO/IEC 27002:2022 sec. 8]*  
2. **Classification and Need-to-Know**: Enforcement of strict separation between classification domains, with access granted strictly by mission role and clearance.  
   *[C-M(2002)49, AC/35-D/1015, ISO/IEC 27001:2022 A.5.10]*  
3. **Default Deny**: Access to all systems, data, and facilities is denied by default unless explicitly authorised.  
   *[NIST CSF PR.AC-4, ISO/IEC 27002:2022 sec. 9.1.2]*  
4. **Accountability and Auditability**: All actions on classified systems must be attributable and auditable.  
   *[NATO INFOSEC, ISO/IEC 27001:2022 A.8.15, NIST CSF PR.PT-1]*  
5. **Legal Compliance**: Adherence to all applicable NATO, host-nation, and EU legal and regulatory requirements, including GDPR for personal data.  
   *[GDPR Art. 5, Law 58/2019, SOFA]*  
6. **Continuous Improvement**: Regular review, training, exercise, and red-teaming to ensure currency and effectiveness.  
   *[NIST CSF ID.RA-7, ISO/IEC 27001:2022 A.7.2]*  

---

## 5. Requirements and Controls

### 5.1 Access Control

- **Separation of domains:** No unauthorised data, user, or network flow across NU, NR, NS, and MISSION SECRET domains. Cross-domain transfers only via accredited NATO CDS.  
  *[C-M(2002)49, AC/322-D(2017)0009 s.3.2, NIST CSF PR.AC-5, ISO/IEC 27002:2022 8.3.2]*
- **Authentication:** PKI-based smart-card (CAC-equivalent) authentication for all users per domain; no cross-domain federation.  
  *[AC/322-D(2017)0009, NIST CSF PR.AC-1, ISO/IEC 27001:2022 A.9.4.2]*
- **Least Privilege & Need-to-Know:** Access granted strictly as required by mission role and clearance; periodic review by ISSM.  
  *[C-M(2002)49, ISO/IEC 27001:2022 A.5.11, NIST CSF PR.AC-6]*
- **Account Management:** Joiners, movers, leavers process enforced; accounts disabled within 1 hour of separation.  
  *[ISO/IEC 27001:2022 A.8.2.3, NIST CSF PR.AC-1]*

### 5.2 Asset and Configuration Management

- **Asset Register:** Maintain inventory of all IT, COMSEC, and CIS assets, mapped to classification domain and owner.  
  *[NIST CSF ID.AM, ISO/IEC 27001:2022 A.5.9]*
- **Configuration Baselines:** All systems built and maintained to NATO-approved secure configurations.  
  *[AC/322-D(2017)0009, NIST CSF PR.IP-1, ISO/IEC 27002:2022 sec. 8.9]*

### 5.3 Physical and Environmental Security

- **TEMPEST Zoning:** All NS and above processing in SCIF or NATO-approved shielded environments.  
  *[AC/35-D/1015, NATO TEMPEST Policy, ISO/IEC 27001:2022 A.7.4]*
- **Access Controls:** Two-person integrity for high-grade COMSEC and keying material; auditable logs for all secure area access.  
  *[C-M(2002)49, ISO/IEC 27001:2022 A.8.15]*

### 5.4 Communications Security (COMSEC)

- **NATO-Approved Equipment:** Only NATO-listed or host-nation-vetted equipment permitted; supply chain managed per NATO and host-nation requirements.  
  *[AC/322-D(2017)0009, NIST CSF ID.SC, ISO/IEC 27001:2022 A.5.19]*
- **Cryptographic Key Management:** Dual-key procedures for high-grade material; chain of custody and audit logs enforced.  
  *[AC/322-D(2017)0009, ISO/IEC 27001:2022 A.8.25]*

### 5.5 Monitoring, Detection, and Response

- **SOC Operations:** 24/7 monitoring at theatre level; all domain boundaries instrumented with NATO-approved sensors.  
  *[NIST CSF DE.CM, ISO/IEC 27001:2022 A.8.16]*
- **Incident Response:** IR plan aligned with NCIRC, with reporting to NCSC and host-nation CERT as required; tests and exercises conducted at least 2x per year.  
  *[NIST CSF RS, AC/35-D/1015, ISO/IEC 27001:2022 A.8.23]*

### 5.6 Supply Chain Security

- **Vendor Vetting:** Only NATO-approved vendors; host-nation contractors subject to security screening.  
  *[NIST CSF ID.SC-1, ISO/IEC 27001:2022 A.5.19]*
- **Supply Chain Audit:** Annual review of supplier compliance and incident history.  
  *[ISO/IEC 27001:2022 A.5.19]*

### 5.7 Data Protection and Privacy

- **GDPR Compliance:** All civilian/contractor personal data processed per GDPR and Romanian CSL; Data Protection Impact Assessments (DPIA) for new systems.  
  *[GDPR Art. 5, Art. 32, Law 58/2019]*
- **Classification Handling:** All information marked and handled IAW NATO and originator classification; spillage procedures enforced.  
  *[C-M(2002)49, ISO/IEC 27001:2022 A.5.10]*

### 5.8 Personnel Security

- **Clearance & Vetting:** Access to classified domains only for cleared personnel; vetting per AC/35-D/1029.  
  *[AC/35-D/1029, ISO/IEC 27001:2022 A.6.1]*
- **Insider Threat Programme:** Continuous monitoring and awareness, focused on counterintelligence risk.  
  *[NIST CSF PR.AT, ISO/IEC 27001:2022 A.6.3]*

### 5.9 Training and Awareness

- **Annual Training:** Minimum 40 hours/year per staff; includes classification handling, incident response, insider threat, and GDPR.  
  *[NIST CSF PR.AT, ISO/IEC 27001:2022 A.6.3]*
- **Exercise and Red Teaming:** Minimum 6 cyber exercises and 2 red-team engagements per year.  
  *[NIST CSF PR.IP-10, ISO/IEC 27001:2022 A.8.23]*

---

## 6. Exceptions

- All exceptions to this policy must be risk-assessed, documented, and approved in writing by the ISSM and Command Authority.  
  *[ISO/IEC 27001:2022 A.5.30]*
- Temporary operational waivers may be granted for urgent mission needs, but must be reviewed within 72 hours and reported to NCIRC if they affect classified domains.  
  *[Unsupported: operational best practice]*

---

## 7. Monitoring and Review

- Policy compliance will be assessed through:
  - Quarterly internal audits by the security staff.
  - Annual independent audit (by NCIRC or NATO Audit).
  - After-action review following all major incidents, exercises, or significant regulatory/legal updates.
- The ISSM will maintain a policy exceptions log and report quarterly to Command Authority and SHAPE J6.

---

## 8. References

1. NATO Information Security Policy (C-M(2002)49)  
2. AC/35-D/1015 Security within NATO  
3. AC/35-D/1029 Personnel security  
4. AC/322-D(2017)0009 NATO INFOSEC Technical Directive  
5. Allied Joint Doctrine for Cyberspace Operations (AJP-3.20)  
6. NATO Cyber Defence Pledge (2016)  
7. Romanian Cybersecurity Law 58/2019  
8. GDPR (Regulation EU 2016/679)  
9. NIST Cybersecurity Framework 2.0  
10. ISO/IEC 27001:2022, ISO/IEC 27002:2022  
11. NATO SOFA  
12. Classified NATO and coalition bilateral/multilateral information-sharing agreements

---

*End of Policy Document*
