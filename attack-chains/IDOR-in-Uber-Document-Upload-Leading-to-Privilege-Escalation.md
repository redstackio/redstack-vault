---
tags:
  - idor
  - access-control
  - privilege-escalation
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
procedures:
  - '[[procedures/Identify-IDOR-in-Document-Upload-Endpoint]]'
  - '[[procedures/Exploit-IDOR-to-Overwrite-Admin-Documents]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation for Privilege Escalation]]'
description: >-
  Multi-stage attack exploiting Insecure Direct Object Reference (IDOR) and
  access control flaws in the /p3/drivers/uploadDocument endpoint on
  partners.uber.com, allowing a driver to overwrite administrator documents and
  achieve privilege escalation.
skill_level: intermediate
impact_level: high
id: b1528f7c-7b23-499c-b6ca-0083d5ca5095
created_at: '2025-12-14T17:25:29.569Z'
updated_at: '2025-12-14T17:25:29.569Z'
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation for Privilege Escalation]]'
---
# IDOR in Uber Document Upload Leading to Privilege Escalation

Multi-stage attack chain demonstrating exploitation of IDOR and access control issues in Uber's partners portal, enabling a driver account to overwrite critical documents belonging to other drivers or the account administrator, resulting in potential privilege escalation.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify IDOR Vulnerability] --> B[Exploit to Overwrite Documents]
    B --> C[Privilege Escalation Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools or proxy like Burp Suite for request manipulation

### Target Environment

- Web platform
- Access to Uber partners.uber.com with a valid driver account
- Multi-driver account structure

### Initial Access Requirements

- Authenticated session as a driver user
- Knowledge of other driver IDs or admin identifiers (e.g., via enumeration or prior recon)
- Network access to partners.uber.com

## Detailed Attack Procedures

### Step 1: Identify IDOR Vulnerability
procedure: [[procedures/Identify-IDOR-in-Document-Upload-Endpoint]]

**Objective**: Test the /p3/drivers/uploadDocument endpoint for IDOR by attempting to upload or access documents using identifiers of other users without proper authorization checks.

**Instructions**: Authenticate as a driver and capture a legitimate upload request using browser tools. Modify the request to target another driver's document ID. Use [[commands/curl-test-idor-upload]] to simulate the test:

```bash
curl -X POST 'https://partners.uber.com/p3/drivers/uploadDocument' \
  -H 'Authorization: Bearer YOUR_DRIVER_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"driver_id": "TARGET_DRIVER_ID", "document_type": "license", "file": "malicious_file.pdf"}'
```

Then, check the response for successful upload without errors indicating permission denial.

**Expected Output**: HTTP 200 or success response confirming document upload/overwrite for the target driver ID.

**Success Indicators**:
- No authorization error returned
- Document listed under the target driver's profile upon verification

### Step 2: Exploit to Overwrite Admin Documents
procedure: [[procedures/Exploit-IDOR-to-Overwrite-Admin-Documents]]

**Objective**: Leverage the identified IDOR to overwrite critical administrator documents, potentially allowing impersonation or escalation to admin privileges.

**Instructions**: With the confirmed IDOR, craft a request to target the admin's document ID (e.g., obtained via account enumeration). Use [[commands/curl-exploit-admin-overwrite]] to upload a malicious or forged document:

```bash
curl -X POST 'https://partners.uber.com/p3/drivers/uploadDocument' \
  -H 'Authorization: Bearer YOUR_DRIVER_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"driver_id": "ADMIN_ID", "document_type": "admin_verification", "file": "forged_admin_doc.pdf"}'
```

Verify the overwrite by accessing the admin's document section or monitoring account changes.

**Expected Output**: Success response indicating the admin document has been replaced.

**Success Indicators**:
- Admin document updated with driver-uploaded content
- Potential access to escalated features or admin dashboard

## Attack Chain Summary

### Key Achievements

1. Identified IDOR allowing cross-user document manipulation
2. Overwrote admin documents without proper checks
3. Achieved potential privilege escalation from driver to admin role

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Exploitation for Privilege Escalation]]

### MITRE ATT&CK Tactics

- [[Privilege Escalation]]

---
*Last updated: 2023-10-01*
