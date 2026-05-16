---
config: C0
context_id: ctx-H
policy_id: P1
policy_name: Information Security Policy
policy_short: infosec
metadata:
  config: C0
  model: gpt-4.1-2025-04-14
  input_tokens: 892
  output_tokens: 2490
  total_tokens: 3382
  latency_s: 56.869
  tool_calls: []
  raw_provider_id: chatcmpl-DcZ6iPYyrIsMbNGeDns0jDKa1NNYs
sources_count: 0
sources: []
prompt_chars: 4108
answer_chars: 9402
generated_at_unix: 1778083844
---

---

**INFORMATION SECURITY POLICY**

**Organisation:** [Hospital Name], [Region], Italy  
**Effective Date:** [DD/MM/YYYY, e.g., 01/07/2024]  
**Policy Owner:** ICT Manager  
**Review Cycle:** Annual (or as required by regulatory change, incident, or audit)  

---

### 1. PURPOSE

This Information Security Policy establishes the principles, responsibilities, and requirements for the protection of information assets at [Hospital Name], a public healthcare organisation operating under the Servizio Sanitario Nazionale (SSN). The policy ensures compliance with applicable Italian and EU legislation (GDPR, D.Lgs. 196/2003 as amended, NIS2, AGID guidelines, Provvedimenti Garante Privacy), and aligns with international standards (NIST CSF 2.0, ISO/IEC 27001:2022) within the operational realities and resource constraints of the organisation.

---

### 2. SCOPE

This policy applies to:

- All staff (clinical, administrative, technical), contractors, and third parties (including Managed Service Providers) with access to [Hospital Name]'s information assets.
- All information systems, physical and electronic records, networked medical devices, and endpoints (workstations and mobile devices) managed by [Hospital Name].
- All data categories processed, including special category data (health data), minors’ data, and employee personal data.

---

### 3. ROLES AND RESPONSIBILITIES

| Role | Responsibilities |
|------|------------------|
| **ICT Manager (Policy Owner)** | Maintains policy, oversees implementation, coordinates with MSP and Data Protection Officer (DPO). |
| **Data Protection Officer (DPO)** | Ensures GDPR and data privacy compliance; advises on privacy impact assessments. |
| **Internal IT Staff** | Day-to-day security operations, endpoint management, incident response, user support. |
| **Managed Service Provider (MSP)** | Provides contracted IT services, including security operations as per SLA, supports incident response and patching. |
| **All Staff** | Comply with this policy and attend mandatory security awareness training. Report security incidents promptly. |
| **Hospital Management** | Allocates resources; supports enforcement and disciplinary action as necessary. |

**References:**  
- GDPR Art. 24, 32  
- D.Lgs. 196/2003, Art. 31, 33  
- NIS2 Art. 21, 23  
- ISO/IEC 27001:2022, Clause 5.3, A.5.1  
- NIST CSF 2.0: ID.GV-1, ID.AM-1  

---

### 4. PRINCIPLES

1. **Patient Safety:** Controls must not impede urgent clinical workflows. (AGID Linee Guida, Rec. 8.2.2)
2. **Data Protection by Design and Default:** Data processing must comply with GDPR and privacy-by-design. (GDPR Art. 25)
3. **Proportionality:** Security measures are risk-based and tailored to the hospital’s size, resources, and threat landscape. (NIS2 Art. 21, ISO/IEC 27001:2022 A.5.31)
4. **Continuous Improvement:** Security is reviewed regularly for effectiveness and updated as threats and regulations evolve. (NIST CSF 2.0: ID.IM-1)
5. **Staff Awareness:** All staff are responsible for safeguarding information, supported by regular training. (ISO/IEC 27001:2022 A.6.3.2)

---

### 5. REQUIREMENTS AND CONTROLS

#### 5.1. Asset Management

- Maintain an up-to-date inventory of information systems, endpoints, mobile devices, and medical devices.  
  **References:** ISO/IEC 27001:2022 A.5.9; NIST CSF 2.0: ID.AM-1; AGID Misure minime 1.1

- Assign asset ownership and ensure asset usage is traceable.  
  **References:** ISO/IEC 27001:2022 A.5.12

#### 5.2. Access Control

- All user accounts must be uniquely assigned. Clinical, administrative, and technical users must use individual credentials.  
  **References:** ISO/IEC 27001:2022 A.5.15; GDPR Art. 32; AGID Misure minime 2.1

- Use strong password policies for all systems (minimum 10 characters, complexity enforced; avoid password reuse).  
  **References:** AGID Misure minime 2.2; ISO/IEC 27001:2022 A.5.17

- Leverage regional SPID/CIE federation where available. For legacy systems, document compensatory controls.  
  **References:** AGID Linee Guida identità digitale; unsupported for legacy exceptions

- Enforce least-privilege and role-based access for all health information systems (EHR/FSE, PACS, LIS, ADT, Pharmacy).  
  **References:** GDPR Art. 32; ISO/IEC 27001:2022 A.5.18

- Remove or disable accounts promptly upon staff exit or role change.  
  **References:** AGID Misure minime 2.3; ISO/IEC 27001:2022 A.5.16

#### 5.3. Physical and Environmental Security

- Restrict access to server rooms and networking areas to authorised personnel only.  
  **References:** ISO/IEC 27001:2022 A.5.19; AGID Misure minime 3.1

- Mobile devices used at the point-of-care must be physically secured when not in use; thefts must be reported immediately.  
  **References:** ISO/IEC 27001:2022 A.5.22

- Devices handling personal or health data must have full-disk encryption enabled unless technically unfeasible (document exceptions).  
  **References:** AGID Misure minime 4.2; ISO/IEC 27001:2022 A.5.22

#### 5.4. Operations Security

- All supported endpoints must run up-to-date antivirus/endpoint protection, centrally monitored via AV console.  
  **References:** AGID Misure minime 5.2; ISO/IEC 27001:2022 A.5.26; NIST CSF 2.0: PR.IP-1

- Critical security patches must be applied to servers and workstations within 30 days of release; legacy or unsupported systems must be isolated and risks documented.  
  **References:** AGID Misure minime 5.1; ISO/IEC 27001:2022 A.5.27

- Back up critical systems (EHR/FSE, ADT, PACS, LIS, pharmacy) at least daily. Test restore procedures quarterly.  
  **References:** ISO/IEC 27001:2022 A.5.30; NIST CSF 2.0: PR.IP-4

- Where feasible, monitor for unusual activity via AV vendor console and logs (no SIEM in place).  
  **References:** AGID Misure minime 5.2; unsupported for SIEM/SOC

#### 5.5. Third-Party and Supply Chain Security

- All contracts with MSPs and vendors must require compliance with GDPR, NIS2, and AGID security measures.  
  **References:** NIS2 Art. 21, 44; ISO/IEC 27001:2022 A.5.29

- Access by third parties (e.g., MSP, device vendors) must be logged and monitored.  
  **References:** ISO/IEC 27001:2022 A.5.20

#### 5.6. Information Transfer and Data Protection

- Transmit health and personal data over secure, encrypted channels (e.g., TLS 1.2+).  
  **References:** GDPR Art. 32; AGID Misure minime 4.4

- Prohibit the use of unauthorised portable media (e.g., USB drives) for patient data transfer.  
  **References:** ISO/IEC 27001:2022 A.5.10; AGID Misure minime 6.3

- Ensure disposal of devices/media containing personal data is performed securely and documented.  
  **References:** GDPR Art. 32; ISO/IEC 27001:2022 A.5.11

#### 5.7. Security Awareness and Training

- All staff must complete at least 2 hours/year of security awareness training, including phishing and data protection topics.  
  **References:** ISO/IEC 27001:2022 A.6.3.2; AGID Misure minime 8.1

- Training records will be maintained by HR/ICT.  
  **References:** Unsupported (local administrative practice)

#### 5.8. Incident Management and Business Continuity

- All suspected or confirmed security incidents must be reported promptly to ICT and escalated to the MSP as required.  
  **References:** ISO/IEC 27001:2022 A.5.29; AGID Misure minime 7.1

- ICT maintains an incident log and coordinates with the DPO for data breaches (as per GDPR Art. 33).  
  **References:** GDPR Art. 33; ISO/IEC 27001:2022 A.5.29

- Business continuity plans must ensure:  
  - EHR/FSE: Recovery Time Objective (RTO) 4h  
  - ADT/PS: RTO 1h  
  **References:** AGID Linee Guida Continuità Operativa; NIS2 Art. 21; ISO/IEC 27001:2022 A.5.30

- Regularly test backup restores and critical system failover (minimum quarterly).  
  **References:** ISO/IEC 27001:2022 A.5.30

#### 5.9. Policy Exceptions

- Exceptions to this policy may be granted only by the ICT Manager, in consultation with the DPO and hospital management, based on documented risk assessment and business need.
- All exceptions must be recorded and reviewed at each policy review cycle.

---

### 6. MONITORING AND REVIEW

- The ICT Manager will review this policy at least annually, and after significant incidents or regulatory changes.
- Compliance will be monitored via periodic audits, endpoint checks, and review of incident logs.
- Policy effectiveness will be evaluated using incident trends, audit results, and staff feedback.
- Findings and recommendations will be reported to hospital management, with action items tracked to closure.

---

### 7. REFERENCES

**Legal and Regulatory:**  
- Regulation (EU) 2016/679 (GDPR)  
- D.Lgs. 196/2003 as amended by D.Lgs. 101/2018  
- Directive (EU) 2022/2555 (NIS2)  
- Linee Guida AGID per la sicurezza informatica nella PA  
- Provvedimenti Garante Privacy in sanità  
- Misure minime di sicurezza ICT per la PA (AGID, 2017)  
- Regional regulations on FSE

**Standards and Frameworks:**  
- ISO/IEC 27001:2022  
- NIST Cybersecurity Framework (CSF) 2.0

**Other:**  
- [Local hospital procedures and contracts]  
- [Vendor documentation for clinical systems]

---

**Approved by:**  
[Name], [Hospital Director]  
[Date]

**Next Review Due:**  
[Month/Year]

---

**Document History:**  
| Version | Date | Changes | Approved by |
|---------|------|---------|-------------|
| 1.0 | [Effective Date] | Initial policy | [Hospital Director] |

---
