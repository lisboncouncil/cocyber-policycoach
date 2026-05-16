---
config: C0+web
context_id: ctx-H
policy_id: P5
policy_name: General Cybersecurity Policy
policy_short: infosec
metadata:
  config: C0+web
  model: gpt-4.1-2025-04-14
  input_tokens: 1442
  output_tokens: 1947
  total_tokens: 3389
  latency_s: 35.687
  tool_calls: []
  raw_provider_id: resp_0f0db530ac3359c60069fb708acd4481938bda3298c490b267
sources_count: 0
sources: []
prompt_chars: 4683
answer_chars: 7456
generated_at_unix: 1778086062
---

---

# General Cybersecurity Policy

**Organisation**: [Redacted] Provincial Public Hospital  
**Governance**: ASL [Redacted], Servizio Sanitario Nazionale, Italy  
**Effective date**: 2024-07-01  
**Policy owner**: Hospital Director (delegated to IT/Privacy Officer)  
**Review cycle**: Annual, or upon material change in risk/regulatory environment

---

## 1. Purpose

This policy establishes the principles and requirements for ensuring the security and integrity of information systems, networks, and data at [Redacted] Provincial Public Hospital. It aims to protect the confidentiality, integrity, and availability of personal and health data, ensure patient safety, and maintain compliance with applicable Italian and European regulations, including GDPR, NIS2, and sectoral guidance.

**References**:  
- GDPR (Regulation EU 2016/679)  
- D.Lgs. 196/2003 as amended by D.Lgs. 101/2018  
- NIS2 (Directive EU 2022/2555)  
- AGID Linee Guida per la sicurezza informatica nella PA  
- ISO/IEC 27001:2022, NIST CSF 2.0

---

## 2. Scope

This policy applies to:
- All employees, external contractors, and service providers accessing or managing hospital ICT resources.
- All information systems, networks, applications, and data, including clinical, administrative, and technical domains.
- All devices (fixed and mobile), regardless of ownership, connected to hospital networks.

---

## 3. Roles and Responsibilities

| Role                          | Responsibilities                                                    | Reference |
|-------------------------------|---------------------------------------------------------------------|-----------|
| **Hospital Director**         | Policy approval, resource allocation, overall accountability        | ISO/IEC 27001: A.5.2 |
| **IT/Privacy Officer**        | Policy implementation, incident escalation, regulatory liaison      | GDPR Art. 37–39; ISO/IEC 27001: A.5.3 |
| **IT Staff (internal + MSP)** | Operations, technical controls, user support, backup, reporting     | ISO/IEC 27001: A.5.7, A.8.2 |
| **All Staff**                 | Follow policy, report incidents/phishing, attend training           | ISO/IEC 27001: A.6.1.1, A.7.2.2 |
| **External Service Providers**| Comply with contract terms and policy, support incident response    | NIS2 Art. 21(2)(h), ISO/IEC 27001: A.5.19 |

---

## 4. Principles

- **Patient Safety**: Cybersecurity controls must not impede emergency clinical care (NIS2 Art. 21, Recital 60).
- **Data Protection by Design and Default**: Data minimisation and security integrated in workflows (GDPR Art. 25).
- **Risk-Based Approach**: Controls proportionate to threats and resources (NIST CSF 2.0: Identify).
- **Least Privilege and Segregation of Duties**: Only necessary access granted (ISO/IEC 27001: A.8.2.3).
- **Continuous Improvement**: Policies adapt to new threats/regulations (ISO/IEC 27001: A.10.1).

---

## 5. Requirements and Controls

### 5.1 Governance and Risk Management

- Maintain an up-to-date ICT asset inventory (ISO/IEC 27001: A.5.9, AGID min. measures).
- Conduct annual risk assessment, covering clinical and admin systems (ISO/IEC 27001: A.6.1.2, NIS2 Art. 21).
- Assign clear responsibility for cybersecurity and privacy compliance (GDPR Art. 37, ISO/IEC 27001: A.5.3).

### 5.2 Access Control and Identity Management

- Enforce unique user accounts; no sharing of credentials (ISO/IEC 27001: A.8.2.1).
- Integrate regional SPID/CIE federation for external identity validation (AGID PA guidelines).
- Apply least privilege access to EHR, PACS, ADT, and other critical systems (ISO/IEC 27001: A.8.2.3).
- Review user privileges quarterly, especially on legacy kiosks (unsupported: specific frequency, but ISO/IEC 27001: A.8.2.2).

### 5.3 Network and System Security

- Maintain VLAN separation between clinical and admin networks; PACS as isolated segment (AGID min. measures, ISO/IEC 27001: A.8.20).
- Implement UTM-managed firewall and VPN for remote access; limit to authorised users (ISO/IEC 27001: A.8.21).
- Legacy Windows kiosks must have restricted internet access and regular patching where possible (unsupported: specific patching cadence for legacy).
- Prohibit unapproved devices on the hospital network (ISO/IEC 27001: A.8.1.3).

### 5.4 Data Protection and Privacy

- Encrypt all mobile devices and laptops with access to patient data (GDPR Art. 32, AGID min. measures).
- Store backups encrypted; retain weekly off-site tapes for minimum 3 months (ISO/IEC 27001: A.8.12; unsupported: specific retention period).
- Strictly control export of health data and restrict use of removable media (GDPR Art. 32, ISO/IEC 27001: A.8.10).

### 5.5 Business Continuity and Incident Response

- Nightly backups to NAS; weekly off-site tape backups (ISO/IEC 27001: A.8.13; AGID min. measures).
- Disaster Recovery test to be performed at least annually (ISO/IEC 27001: A.17.1; AGID min. measures).
- Maintain and update incident response contacts; all staff must report suspected incidents immediately (NIS2 Art. 21(2)(d); ISO/IEC 27001: A.5.24).
- Escalate serious incidents to MSP and regional authorities as per escalation plan (NIS2 Art. 23).

### 5.6 Phishing and End-User Awareness

- Mandatory cybersecurity training: minimum 2 hours/year for all staff, including simulated phishing (AGID min. measures; ISO/IEC 27001: A.6.3).
- Onboarding training within two weeks of start date (unsupported: specific timeframe, but ISO/IEC 27001: A.7.2.2).

### 5.7 Physical and Device Security

- Secure all point-of-care mobile devices with cable locks or secure storage when not in use (ISO/IEC 27001: A.7.4).
- Promptly report loss/theft of any device containing health data (GDPR Art. 33; ISO/IEC 27001: A.5.25).

### 5.8 Supply Chain Security

- All contracts with MSPs and medical device vendors must include data protection and cybersecurity clauses (NIS2 Art. 21(2)(h); ISO/IEC 27001: A.5.19).
- Require third-party suppliers to notify the hospital of any security incident affecting hospital data or systems (GDPR Art. 28; ISO/IEC 27001: A.5.19).

---

## 6. Exceptions

Requests for exceptions to this policy must be submitted in writing to the IT/Privacy Officer. Exceptions will be granted only after documented risk assessment and, where relevant, consultation with clinical leadership and the regional ASL.

---

## 7. Monitoring and Review

- The IT/Privacy Officer will monitor compliance through periodic reviews, log analysis, and audits (NIS2 Art. 21, ISO/IEC 27001: A.10.1).
- The policy will be reviewed annually or in response to major incidents, regulatory changes, or introduction of new systems.
- Non-compliance may result in disciplinary measures as per hospital HR policy.

---

## 8. References

- **GDPR (Regulation EU 2016/679)** — https://eur-lex.europa.eu/eli/reg/2016/679/oj  
- **D.Lgs. 196/2003 e s.m.i.** — https://www.garanteprivacy.it/web/guest/home/docweb/-/docweb-display/docweb/1311248  
- **NIS2 (Directive EU 2022/2555)** — https://eur-lex.europa.eu/eli/dir/2022/2555/oj  
- **Linee Guida AGID** — https://www.agid.gov.it/it/sicurezza  
- **ISO/IEC 27001:2022** — https://www.iso.org/isoiec-27001-information-security.html  
- **NIST CSF 2.0** — https://www.nist.gov/cyberframework  
- **Provvedimenti Garante Privacy** — https://www.garanteprivacy.it/web/guest/home/docweb/-/docweb-display/docweb/3134436  
- **Regional FSE Regulations** — [Regional ASL/SSR documentation]

---

**End of Policy**
