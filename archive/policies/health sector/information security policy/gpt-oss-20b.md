**Access‑Control Policy** 

---

## 1. Purpose
To protect patient records, staff personal information, and appointment schedules by defining who may access the hospital’s information assets (PCs, central server, peripherals) and under what conditions.

## 2. Scope
Applies to all hospital staff (doctors, nurses, administrative personnel) who use the LAN‑connected PCs and to any device that accesses the central server. External internet access is not permitted.

## 3. Policy Statements

| Control | Policy |
|---------|--------|
| **AC‑1 – Access Control Policy and Procedures** | • The hospital maintains an access‑control policy that: <br>• Addresses purpose, scope, roles, responsibilities, management commitment, coordination among entities, and compliance. <br>• Is consistent with applicable laws (e.g., HIPAA, GDPR) and NIST SP 800‑53 rev. 5. |
| **AC‑2 – Account Management** | • All user accounts are created, modified, and revoked by the IT administrator in accordance with role‑based access (RBAC). <br>• Account creation requires a signed request from the department head. <br>• Accounts are disabled after 30 days of inactivity. |
| **AC‑3 – Access Enforcement** | • Only authorized users may log into the PCs or the central server. <br>• Access is granted on a least‑privilege basis: <br> • Doctors and nurses receive read/write access to clinical data; <br> • Administrative staff receive read-only access to patient records and full access to scheduling data. |
| **AC‑4 – Information Flow Enforcement** | • All data movement between PCs and the central server is logged. <br>• No patient or staff data may leave the LAN without explicit approval from the IT security officer. |
| **AC‑17 – Remote Access** | • Remote access is not allowed (no internet connectivity). <br>• If future remote needs arise, they will be implemented via VPN with TLS encryption (SC‑8) and managed access points (SC‑7). |
| **AU‑2 – Audit Events** | • The central server logs all user logons, data access, and modification events. <br>• Logs are retained for 90 days and reviewed monthly by the security officer. |
| **AU‑6 – Audit Review, Analysis, and Reporting** | • Monthly audit reviews identify anomalous access patterns; findings are reported to the hospital board. |
| **SC‑7 – Boundary Protection** | • Network segmentation isolates the central server from non‑clinical PCs. <br>• Firewalls and intrusion detection systems monitor traffic at the LAN perimeter. |
| **SC‑13 – Cryptographic Protection** | • All data at rest on the central server is encrypted using AES‑256. <br>• Encryption keys are stored in a hardware security module (HSM). |

## 4. Roles and Responsibilities

| Role | Responsibility |
|------|----------------|
| **IT Security Officer** | • Approves access requests. <br>• Conducts monthly audit reviews. |
| **Department Heads** | • Verify that staff access aligns with clinical duties. |
| **All Users** | • Follow the least‑privilege principle. <br>• Report suspicious activity immediately. |

## 5. Enforcement
Violations of this policy may result in disciplinary action, up to termination, and potential legal penalties under HIPAA or GDPR.

## 6. Review Cycle
The policy is reviewed annually or when significant changes occur (e.g., new systems, regulatory updates).

---

### References

- *NIST SP 800‑53 rev. 5 – Security and Privacy Controls for Information Systems and Organizations* (AC, AU, SC families)  
- *USC 3502 – Information Resources Definition* (definition of information assets)  
- *USC 11101 – Information Technology Definition* (scope of IT resources)

Please review the draft and let me know if any adjustments are needed.