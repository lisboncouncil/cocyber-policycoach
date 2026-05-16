---
config: C0
context_id: ctx-M
policy_id: P2
policy_name: Incident Response Policy
policy_short: ir
metadata:
  config: C0
  model: gpt-4.1-2025-04-14
  input_tokens: 1015
  output_tokens: 2449
  total_tokens: 3464
  latency_s: 23.482
  tool_calls: []
  raw_provider_id: chatcmpl-DcZAbooTNtc6I3PU6dNByjCs62qQY
sources_count: 0
sources: []
prompt_chars: 4953
answer_chars: 10002
generated_at_unix: 1778084052
---

---

# NATO Allied Command Operations (ACO) — Multinational Military Detachment, Romania  
**Incident Response Policy**  

**Document Reference:** ACO-MMD-IRP-001  
**Effective Date:** 2024-07-01  
**Policy Owner:** Information Systems Security Manager (ISSM), J6  
**Review Cycle:** Annual, or upon significant change in threat or operational environment  
**Approved By:** Commander, Multinational Military Detachment  
**Classification:** NATO UNCLASSIFIED (when detached from annexes and operational runbooks)

---

## 1. Purpose

This policy establishes the mandatory requirements and processes for incident response (IR) within the Multinational Military Detachment (MMD) under NATO Allied Command Operations (ACO) in Romania. It is designed to ensure the rapid detection, accurate reporting, containment, eradication, and recovery from cybersecurity incidents in line with NATO policy and operational doctrine, host-nation law, and relevant international standards. The policy ensures protection of classified information, operational continuity, and compliance with applicable legal and regulatory obligations.

---

## 2. Scope

This policy applies to:
- All personnel (military, NATO civilian, and cleared contractors) assigned to or supporting the MMD,  
- All information and communication systems (CIS) operated by or on behalf of the unit, across all classification domains (NU, NR, NS, MISSION SECRET),
- All physical, logical, and cross-domain environments, including COMSEC equipment and keying material,
- All incidents impacting, or with potential to impact, the confidentiality, integrity, or availability of MMD information assets.

---

## 3. Roles and Responsibilities

| Role | Responsibility | Reference |
|------|---------------|-----------|
| **Commander** | Approves IR policy; ensures resourcing and command support. | [C-M(2002)49 Rev], ISO 27001:2022 Clause 5.1 |
| **ISSM (J6)** | Owns IR policy/process; oversees IR capability; ensures alignment with NATO/host-nation frameworks. | ISO 27001:2022 Clause 5.3, 6.1.2 |
| **ISSO(s)** | Maintain IR procedures; coordinate with SOC, NCIRC, NCSC, and host-nation CERT; support incident handling and reporting. | ISO 27001:2022 A.5.24, A.5.25 |
| **Cyber Operations Team** | Operate detection, containment, and eradication tools; triage incidents; execute IR playbooks. | NIST CSF DE.DP, RS.RP |
| **SOC (24/7 Theatre-level)** | Provide continuous monitoring; raise alerts; escalate to MMD ISSM/ISSO per runbook. | NIST CSF DE.CM |
| **COMSEC Custodians** | Manage incidents involving COMSEC equipment/material; apply two-person integrity in response; report to national COMSEC authority as required. | AC/35-D/1015, AC/35-D/1029 |
| **All Personnel** | Immediately report suspected or confirmed incidents via established channels; support investigations as directed. | AC/35-D/1015, ISO 27001:2022 A.5.25 |

---

## 4. Principles

- **NATO Policy Alignment:** All IR activities must comply with NATO Information Security Policy (C-M(2002)49), technical directives (AC/322-D(2017)0009), and Allied Joint Doctrine for Cyberspace Operations (AJP-3.20).
- **Host-Nation Law:** IR for systems containing personal data must comply with Romanian Cybersecurity Law (Law 58/2019), NIS2, and GDPR within SOFA limitations.  
- **Classified Domain Separation:** Incidents must be contained and investigated within their classification domain; no cross-domain transfer of data or evidence without documented approval and accredited cross-domain solutions ([AC/322-D(2017)0009]).
- **Need-to-Know and Originator Control:** Information related to incidents is shared strictly on a need-to-know and ORCON basis, especially for incidents involving shared intelligence or sensitive operational data ([C-M(2002)49], NATO classification policy).
- **Timely Reporting:** All incidents must be reported promptly to enable rapid containment and escalation ([NIST CSF RS.AN, ISO 27001:2022 A.5.25]).
- **Continuous Improvement:** Lessons learned from incidents are incorporated into training, processes, and technical controls ([NIST CSF IM, ISO 27001:2022 A.5.27]).

---

## 5. Requirements and Controls

### 5.1 Incident Identification and Reporting

- **5.1.1** All personnel must immediately report suspected or actual security incidents via designated secure reporting channels (phone, in-person, or classified email as appropriate to domain) ([ISO 27001:2022 A.5.25], [NIST CSF DE.DP], [AC/35-D/1015]).
- **5.1.2** Security Operations Centre (SOC) must provide 24/7 monitoring of MMD CIS, including all classification domains; alerts must be triaged and escalated per documented runbooks ([NIST CSF DE.CM], [AC/322-D(2017)0009]).
- **5.1.3** All incidents involving suspected COMSEC compromise must be reported immediately to the ISSM and COMSEC Custodian, and (where required) to the national COMSEC authority; two-person integrity must be maintained throughout ([AC/35-D/1015]).

### 5.2 Incident Categorisation and Prioritisation

- **5.2.1** All incidents must be classified by impact (information classification, operational effect, potential compromise) and assigned a priority per NATO/NCIRC scheme ([AJP-3.20 Section 3.6], [ISO 27001:2022 A.5.24]).
- **5.2.2** Incidents involving possible state-sponsored APT, insider threat, supply-chain compromise, cross-domain spillage, or COMSEC equipment must be categorised as major incidents and trigger immediate escalation.

### 5.3 Containment, Eradication, and Recovery

- **5.3.1** Containment strategies must respect the strict separation between classification domains; evidence and logs must not be transferred between domains except via accredited and documented cross-domain solutions and with ISSM approval ([AC/322-D(2017)0009]).
- **5.3.2** For COMSEC-related incidents, dual-key and two-person integrity measures must be maintained throughout the response process ([AC/35-D/1015]).
- **5.3.3** Recovery of affected systems must be coordinated with the ISSM and, where appropriate, the SOC and national/international CERTs; restoration of classified systems must follow NATO accreditation and sanitisation procedures ([C-M(2002)49], [ISO 27001:2022 A.5.26]).

### 5.4 Communication and Escalation

- **5.4.1** Incident communication must be conducted within the appropriate classification domain and limited to personnel with need-to-know and relevant clearance ([C-M(2002)49], [NATO classification policy]).
- **5.4.2** Incidents must be escalated to:
  - NCIRC (NATO Computer Incident Response Capability) for all significant cyber incidents ([AJP-3.20 Section 4.5]),
  - NCSC (NATO Security Coordination Centre) for incidents impacting NATO policy or security,
  - Host-nation CERT for incidents with host-nation legal impact (e.g., GDPR-relevant data), within SOFA limitations ([Law 58/2019], [GDPR Articles 33/34]),
  - National COMSEC authority for COMSEC compromise ([AC/35-D/1015]).
- **5.4.3** For incidents involving personal data, notification to data subjects and host-nation authorities must be managed by the ISSM in coordination with NATO DPO and legal counsel, in compliance with GDPR and SOFA ([GDPR Arts. 33/34], [ISO 27001:2022 A.5.25]).

### 5.5 Evidence Handling and Forensics

- **5.5.1** All evidence collection and handling must preserve chain of custody, particularly for classified or COMSEC-related material; two-person integrity applies at all times for high-grade material ([AC/35-D/1015]).
- **5.5.2** Evidence must remain in the originating classification domain unless cross-domain transfer is essential, and only via accredited means and ISSM authorisation ([AC/322-D(2017)0009]).
- **5.5.3** Forensic activity must use NATO-approved tools and methodologies; all actions must be logged and auditable ([ISO 27001:2022 A.5.26], [NIST CSF RS.CO]).

### 5.6 Post-Incident Review and Lessons Learned

- **5.6.1** After each major incident, a formal post-incident review must be conducted within 30 days, identifying root cause, remediation, and lessons learned ([ISO 27001:2022 A.5.27], [NIST CSF IM]).
- **5.6.2** Action items resulting from post-incident reviews must be tracked and remediated, with status reported to the ISSM and Commander ([ISO 27001:2022 A.5.27]).
- **5.6.3** Training and technical controls must be updated in light of lessons learned, including integration into regular exercises ([ISO 27001:2022 A.6.3], [NIST CSF IM]).

---

## 6. Exceptions

- **6.1** Exceptions to this policy may only be granted by the ISSM, in consultation with the Commander, and must be formally documented with compensating controls and a defined review period.
- **6.2** No exception may be granted that violates NATO policy, host-nation law, or the principle of domain separation for classified information ([Unsupported if otherwise]).

---

## 7. Monitoring and Review

- **7.1** Compliance with this policy will be monitored through:
  - Regular audits by the ISSM/ISSO team ([ISO 27001:2022 A.5.36]),
  - Red-team exercises (minimum twice per year) and after-action reviews,
  - Review of incident logs and escalation records,
  - Annual policy review, or as directed following significant incident or change in threat/mission.
- **7.2** Policy effectiveness is reported annually to the Commander, with recommendations for improvement.

---

## 8. References

- **NATO Information Security Policy (C-M(2002)49 & successors)**
- **AC/35-D/1015** — Security Within NATO
- **AC/35-D/1029** — Personnel Security
- **AC/322-D(2017)0009** — NATO INFOSEC Technical and Implementation Directive
- **NATO Cyber Defence Pledge (2016)**
- **AJP-3.20** — Allied Joint Doctrine for Cyberspace Operations
- **Romanian Cybersecurity Law (Law 58/2019, NIS/NIS2 Transposition)**
- **GDPR (EU 2016/679)**
- **NIST Cybersecurity Framework (CSF) 2.0**
- **ISO/IEC 27001:2022, 27002:2022**

---

**Document Control:**  
This policy is maintained by the ISSM (J6) and is reviewed annually or upon significant change in mission, threat, or regulatory environment.

---
