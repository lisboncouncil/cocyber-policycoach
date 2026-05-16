---
config: C2
context_id: ctx-H
policy_id: P3
policy_name: Access Control Policy
policy_short: accesscontrol
metadata:
  config: C2
  model: moonshotai/Kimi-K2.5
  input_tokens: 25367
  output_tokens: 4780
  total_tokens: 30147
  latency_s: 23.365
  tool_calls:
  - rag_retrieval
  raw_provider_id: 5fe940c5-a8e7-4f25-aed1-a6082933c7b7
  chunks_retrieved: 5
  server_version: 1.3.4
sources_count: 2
sources:
- type: kb_source
  source: ./datadir-plus-templates/access_control_policy.docx
  title: ./datadir-plus-templates/access_control_policy.docx
- type: kb_source
  source: ./datadir-plus-templates/asset_management.docx
  title: ./datadir-plus-templates/asset_management.docx
prompt_chars: 4669
answer_chars: 15935
generated_at_unix: 1778086634
---

 <policy title="Access Control Policy">

| Field | Value |
|---|---|
| **Document ID** | POL-002 |
| **Version** | 1.0 |
| **Status** | Draft |
| **Classification** | Internal — Restricted |
| **Owner** | Responsabile IT / Direttore Sanitario (acting) |
| **Approved by** | Direttore Generale (CEO equivalent) |
| **Approval date** | [DD/MM/YYYY] |
| **Next review date** | [DD/MM/YYYY] |
| **Review cycle** | Annual (or upon significant organisational change) |

---

## 1. Purpose

This policy establishes the framework for managing access to Ospedale Provinciale [Name]'s information systems, electronic health records (FSE), clinical applications (PACS, LIS, ADT), and administrative data. It ensures that access is granted solely on the basis of legitimate business need and clinical duty, using the principle of least privilege, and that all access is authenticated, authorised, and periodically reviewed. 

This policy supports compliance with NIS2 Directive (EU) 2022/2555 — under which the Hospital qualifies as an Essential Entity in the health sector — GDPR (EU) 2016/679, D.Lgs. 196/2003 as amended (Codice Privacy), AGID Linee Guida per la Sicurezza Informatica nella PA, and ISO/IEC 27001:2022 controls 5.16, 5.17, 5.18 and 8.2. *Source: ISO/IEC 27001:2022; NIS2 Directive Article 21; AGID Misure Minime per la PA.*

---

## 2. Scope

This policy applies to:

- All information systems, clinical applications (Cartella Clinica Elettronica/FSE, PACS/RIS, LIS, ADT, Pharmacy management), and administrative systems owned or managed by the Hospital
- All user accounts: employees (clinical and administrative), contractors, Managed Service Provider (MSP) personnel, medical device vendors, and regional ASL users accessing via SPID/CIE federation
- All access methods: on-premises (including 35 legacy Windows clinical kiosks), remote VPN, regional federation (SPID/CIE), and emergency break-glass access
- All devices used to access Hospital systems: 220 workstations, 60 mobile point-of-care devices, and personal devices (BYOD prohibited for clinical systems)
- All physical locations: internal medicine, general surgery, paediatrics, long-term care, emergency first aid (PS), and administrative offices

---

## 3. Roles and Responsibilities

### 3.1 Direttore Generale (CEO equivalent)
- Ultimate accountability for access control governance as required by NIS2 Article 21 for essential entities
- Approval of policy exceptions exceeding 30 days
- Resource allocation for MFA and identity management tools

### 3.2 Direttore Sanitario (Medical Director) — Policy Co-Owner
- Clinical governance of access rights to patient data and medical systems
- Approval of access requests for clinical staff and medical students
- Authorisation of emergency break-glass access protocols
- Annual review of clinical access rights (privileged medical accounts)

### 3.3 Responsabile IT (IT Manager — 1.5 FTE)
- Operational ownership of this policy
- Implementation of technical controls via MSP coordination
- Maintenance of Active Directory and VPN access lists
- Monthly review of access logs for anomalies
- Coordination with regional ASL for FSE/SPID identity federation

### 3.4 Managed Service Provider (MSP) — [Contractor Name]
- Provisioning and de-provisioning of accounts within 24 hours of HR notification
- Technical enforcement of MFA on VPN and email systems
- Maintenance of network access controls (UTM firewall rules)
- Quarterly access certification reports

### 3.5 HR Department (Ufficio Personale)
- Notification to IT/MSP of all new starters, leavers, and role changes within 4 hours
- Maintenance of authoritative personnel registry linked to ASL employment status
- Collection of signed confidentiality agreements (NDA) before access provisioning

### 3.6 Unit Managers (Capo Sala / Responsabile di Unità)
- Validation of access requests for personnel within their ward/unit
- Immediate notification to HR/IT of unexpected departures or suspensions
- Ward-level enforcement of screen lock and device security policies

### 3.7 All Users (Clinical and Administrative)
- Use only assigned accounts; no credential sharing even during shift changes
- Immediate reporting of suspected compromise to IT Help Desk (internal 2xxx)
- Compliance with MFA requirements and password policy

---

## 4. Policy Requirements

### 4.1 Principle of Least Privilege and Clinical Need
Every user — internal, external, or regional — is granted the minimum access required to perform their specific clinical or administrative function. Access to patient data (special category data under GDPR Article 9) is restricted to direct care teams and authorised administrative personnel only. *Source: GDPR Article 32(1)(b); ISO 27001:2022 Control 5.16.*

### 4.2 Authentication and MFA

#### 4.2.1 Multi-Factor Authentication (MFA)
- **Mandatory** for: VPN remote access, email (PEC and standard), FSE access via web portal, and all privileged administrative accounts
- **Implementation**: Via MSP-managed UTM and Microsoft Authenticator (or SMS fallback for legacy compatibility)
- **Exemption**: Legacy Windows clinical kiosks (35 units) pending hardware refresh; compensating controls via network segmentation and physical security required *Source: NIST CSF 2.0 PR.AA-01; AGID Linee Guida.*

#### 4.2.2 Regional Federation (SPID/CIE)
Access to regional FSE systems utilises the national SPID/CIE federation. Hospital-managed accounts must align with regional identity assertions; manual provisioning of local FSE accounts only where federation is technically unavailable.

### 4.3 User Account Management

#### 4.3.1 Standard Clinical and Administrative Accounts
- **Uniqueness**: One person, one account; shared accounts prohibited except for emergency break-glass (see §4.6)
- **Naming Convention**: `name.surname` for standard users; `name.surname.admin` for privileged IT accounts
- **Lifecycle**: 
  - Provisioning: Within 24 hours of HR notification and manager approval
  - Modification: Within 4 hours of role change notification
  - De-provisioning: Immediate upon contract termination or suspension; accounts disabled within 2 hours, deleted within 30 days
- **High Turnover Management**: Automated workflow via HR-MSP ticketing system to accommodate frequent clinical staff rotations *Source: ISO 27001:2022 Control 5.17.*

#### 4.3.2 Privileged Accounts
- **Scope**: Domain administrators, PACS administrators, LIS super-users, ADT system managers
- **Restrictions**: Maximum 3 persons; no use for routine tasks; separate privileged and standard accounts required
- **MFA**: Hardware token or authenticator app mandatory
- **Review**: Quarterly access certification by Direttore Sanitario and Responsabile IT

#### 4.3.3 Third-Party and MSP Accounts
- **Identification**: Prefix `EXT-` or `MSP-` in account names
- **Expiry**: Automatic expiration every 90 days unless renewed by contract holder
- **VPN Access**: Time-restricted (business hours only) unless emergency on-call
- **Termination**: Immediate upon contract end or incident suspicion

#### 4.3.4 Service Accounts
- Non-interactive use only where technically feasible
- Passwords rotated every 180 days or upon personnel change
- Documentation in secure password manager (MSP-maintained)

### 4.4 Authorisation Process

| Access Type | Requestor | Approver | Provisioner | Timeline |
|---|---|---|---|---|
| Standard Clinical | HR | Unit Manager (Capo Sala) | MSP | 24 hours |
| Standard Administrative | HR | Department Head | MSP | 24 hours |
| Privileged/Admin | N+1 | Direttore Sanitario + Responsabile IT | Responsabile IT | 48 hours |
| Emergency Temporary | Unit Manager | Direttore Sanitario (verbal, documented after) | MSP | 2 hours |
| Third-Party/MSP | Contract Owner | Direttore Generale | Responsabile IT | 48 hours |

**Forms**: Account Creation and Modification Form (ACMF — Annex A) for standard requests; Emergency Access Log (Annex B) for break-glass.

### 4.5 Remote Access
- **VPN Only**: All remote access via client-to-site VPN (UTM-managed); direct RDP/SSH exposure prohibited
- **Device Requirements**: Hospital-managed devices only; personal devices prohibited for clinical data access
- **Session Timeout**: 30 minutes idle timeout; maximum 8-hour session duration
- **Geofencing**: Alerts for connections from outside Italy (unless pre-approved travel) *Source: NIS2 Article 21(2)(c); ISO 27001:2022 Control 8.2.*

### 4.6 Emergency Break-Glass Access
Given 24/7 clinical operations and patient safety imperatives:
- **Definition**: Emergency access to bypass normal controls when systems fail or delay would endanger patient safety
- **Authorisation**: Verbal approval by Direttore Sanitario or Unit Manager; documented within 1 hour post-event
- **Accounts**: Two shared emergency accounts per critical system (ADT, PACS) with passwords sealed in physical safe (break-glass envelope)
- **Logging**: All break-glass usage triggers immediate alert to Responsabile IT and post-event review within 24 hours
- **Compensating Controls**: Enhanced logging, immediate password change after use, mandatory incident report *Source: NIST CSF 2.0 PR.AC-1; AGID Raccomandazioni per accesso emergenziale.*

### 4.7 Legacy System Constraints
- **Windows Clinical Kiosks (35 units)**: Unsupported OS versions; compensating controls include:
  - Network isolation (dedicated VLAN, no internet access, restricted to PACS/RIS only)
  - Physical security (kiosk mode, locked enclosures)
  - Quarterly review for replacement planning
  - No local administrative access for clinical staff

### 4.8 Access Reviews
- **Quarterly**: Privileged accounts and MSP access
- **Semi-annually**: All clinical staff access to FSE and PACS
- **Annually**: Administrative access and role alignment
- **Process**: Automated report from AD/MSP → Unit Manager validation → Responsabile IT revocation of obsolete rights within 5 business days *Source: ISO 27001:2022 Control 5.18.*

---

## 5. Monitoring and Logging

- **Scope**: All authentication events (success/failure) on ADT, PACS, LIS, FSE portal, and VPN gateway
- **Retention**: 12 months minimum (GDPR and NIS2 requirement)
- **Review**: Weekly automated report review by Responsabile IT; monthly anomaly analysis
- **Alerts**: Immediate notification for:
  - Break-glass account usage
  - Failed login attempts >5 within 5 minutes (brute force)
  - After-hours access to patient databases by administrative accounts
  - VPN access from non-Italian IPs without prior approval *Source: GDPR Article 32(1)(d); NIS2 Article 21(2)(d).*

---

## 6. Exceptions

Exceptions to this policy require:
1. Written business justification (clinical or operational necessity)
2. Risk assessment documenting compensating controls
3. Approval by Direttore Sanitario and Responsabile IT (operational exceptions) or Direttore Generale (strategic exceptions)
4. Maximum validity: 6 months (renewable once)
5. Registration in ISMS Exception Register maintained by Responsabile IT

**Standing Exceptions**:
- Legacy clinical kiosks (until replacement Q[XX] 20XX)
- Emergency break-glass procedures (permanent, governed by §4.6)

---

## 7. Enforcement

Non-compliance will be handled under the Hospital's disciplinary procedures (CCNL Sanità — Contratto Collettivo Nazionale):

| Severity | Examples | Consequence |
|---|---|---|
| Minor | Failure to lock screen, delayed password change | Verbal warning, mandatory retraining |
| Moderate | Sharing credentials, unauthorised access attempt | Written warning, HR notification |
| Severe | Bypassing MFA, unauthorised access to patient records not in care team | Suspension of access, formal disciplinary action |
| Critical | Data exfiltration, ransomware facilitation | Immediate suspension, termination, Garante Privacy notification, potential criminal referral under D.Lgs. 196/2003 |

---

## 8. Related Documents

| Document ID | Title |
|---|---|
| POL-001 | Cybersecurity Policy |
| POL-003 | Asset Management Policy (Medical Devices) |
| POL-004 | Backup and Recovery Policy (RTO 4h/1h) |
| POL-006 | Password Policy |
| POL-008 | Cyber Incident Response Plan (MSP escalation) |
| Regional | Regolamento FSE [Region Name] |
| Annex A | Account Creation and Modification Form (ACMF) |
| Annex B | Emergency Access Log |

---

## 9. Definitions

| Term | Definition |
|---|---|
| **ASL** | Azienda Sanitaria Locale — Local Health Authority |
| **FSE** | Fascicolo Sanitario Elettronico — Electronic Health Record |
| **PACS** | Picture Archiving and Communication System (Radiology) |
| **LIS** | Laboratory Information System |
| **ADT** | Admission, Discharge, Transfer system |
| **SPID/CIE** | Sistema Pubblico di Identità Digitale / Carta di Identità Elettronica |
| **Break-glass** | Emergency access procedure bypassing normal controls for patient safety |
| **MSP** | Managed Service Provider — external IT service provider |
| **NIS2** | Directive (EU) 2022/2555 on measures for high common level of cybersecurity |

---

## 10. Compliance and Regulatory References

- **NIS2 Directive (EU) 2022/2555** — Article 21 (cybersecurity risk-management measures for essential entities), Article 23 (reporting obligations)
- **GDPR (EU) 2016/679** — Article 9 (processing of special categories of personal data), Article 32 (security of processing)
- **D.Lgs. 196/2003** (Codice in materia di protezione dei dati personali) as amended by D.Lgs. 101/2018
- **ISO/IEC 27001:2022** — Controls 5.16 (Identity management), 5.17 (Authentication information), 5.18 (Access rights), 8.2 (Privileged access rights)
- **NIST Cybersecurity Framework 2.0** — Function PR.AA (Access Control), PR.AC (Identity Management and Authentication)
- **AGID Linee Guida** — Misure minime di sicurezza ICT per le Pubbliche Amministrazioni
- **Garante Privacy** — Provvedimenti specifici per il settore sanitario

---

## 11. Revision History

| Version | Date | Author | Description of Change |
|---|---|---|---|
| 1.0 | [DD/MM/YYYY] | Responsabile IT | Initial release — aligned with NIS2 essential entity requirements and regional ASL integration |

---

## 12. Approval

| Role | Name | Signature | Date |
|---|---|---|---|
| Policy Owner (Responsabile IT) | | | |
| Clinical Co-Owner (Direttore Sanitario) | | | |
| Approved by (Direttore Generale) | | | |
| Compliance Review (Privacy Officer) | | | |

---

## Annex A — Account Creation and Modification Form (ACMF)

**Classification: INTERNAL**

| Field | Details |
|---|---|
| **Request type** | New account / Modification / Temporary |
| **User full name** | |
| **Codice Fiscale** | |
| **Department/Unit** | Internal Medicine / Surgery / Paediatrics / LTC / Emergency / Admin |
| **Role** | Doctor / Nurse / Admin / Technician / Student / Contractor |
| **Systems required** | FSE / PACS / LIS / ADT / Pharmacy / Email / VPN |
| **Access level** | Standard / Read-only / Admin / Emergency |
| **Start date** | |
| **End date** (if temporary) | |
| **Requested by** | |
| **Unit Manager approval** | |
| **HR verification** | |
| **IT/MSP action** | |
| **Date completed** | |

---

## Annex B — Emergency Access Log (Break-Glass)

**Classification: RESTRICTED**

| Field | Details |
|---|---|
| **Date/Time of access** | |
| **System accessed** | ADT / PACS / LIS / Other |
| **Emergency account used** | |
| **Authorising clinician** | |
| **Reason for emergency** | System outage / Patient safety / Other |
| **Patient ID(s) accessed** | |
| **Actions performed** | |
| **Time normal access restored** | |
| **Post-event review date** | |
| **Responsabile IT sign-off** | |

</policy>

*Sources consulted: ISO/IEC 27001:2022 Controls 5.16, 5.17, 5.18, 8.2; NIS2 Directive (EU) 2022/2555 Articles 21 and 23; GDPR (EU) 2016/679 Articles 9 and 32; AGID Linee Guida per la Sicurezza Informatica nella Pubblica Amministrazione; NIST Cybersecurity Framework 2.0 (PR.AA, PR.AC); Regional FSE regulations; D.Lgs. 196/2003 (Codice Privacy).*
