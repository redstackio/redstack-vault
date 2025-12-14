---
tags:
  - rce
  - pentaho
  - default-credentials
  - prpt
  - bsh
  - javascript
  - java
type: attack_chain
tools:
  - '[[tools/Pentaho-Report-Designer]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Java
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-Pentaho-BI-Server-with-Default-Admin-Credentials]]'
  - '[[procedures/Craft-Malicious-PRPT-Report-with-Embedded-Scripts]]'
  - '[[procedures/Upload-and-Execute-Malicious-PRPT-Report-for-RCE]]'
step_count: 3
techniques:
  - '[[Valid Accounts]]'
  - '[[Default Accounts]]'
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:23:54.339Z'
description: >-
  Multi-stage attack exploiting default credentials in Pentaho BI Server to gain
  unauthorized access and upload a malicious PRPT report embedding scripts for
  remote code execution.
skill_level: intermediate
impact_level: high
id: 866b5534-6803-43e9-a21d-342bddb87289
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Default Accounts]]'
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Remote Code Execution via Malicious PRPT Upload in Pentaho BI Server Using Default Credentials

Multi-stage attack chain demonstrating a complete attack workflow exploiting a publicly exposed Pentaho BI Server with default credentials to achieve remote code execution through malicious report uploads.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via Default Credentials] --> B[Create Malicious Report]
    B --> C[Upload and Execute for RCE]
    C --> D[Server Compromise]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Pentaho-Report-Designer]]

### Target Environment

- Web-based Pentaho BI Server exposed on port 8888
- Java runtime environment
- Services: Pentaho BI Server
- Tech stack: Java, BeanShell, JavaScript

### Initial Access Requirements

- Network access to https://target:8888/pentaho
- No prior credentials needed; defaults (admin/password) assumed unchanged
- Public exposure of the server

## Detailed Attack Procedures

### Step 1: Initial Access
procedure: [[procedures/Access-Pentaho-BI-Server-with-Default-Admin-Credentials]]

**Objective**: Gain unauthorized administrative access to the Pentaho BI Server using default credentials.

**Instructions**: Navigate to the login endpoint at https://sm.mtn.ci:8888/pentaho and enter the default username 'admin' and password 'password' to authenticate. This bypasses authentication due to unchanged defaults.

**Expected Output**: Successful login to the Pentaho dashboard with administrative privileges.

**Success Indicators**:
- Access to server interface without errors
- Ability to view and manage reports

### Step 2: Create Malicious Report
procedure: [[procedures/Craft-Malicious-PRPT-Report-with-Embedded-Scripts]]

**Objective**: Design a PRPT report file embedding malicious scripts in BeanShell, JavaScript, or Java to enable code execution upon report rendering.

**Instructions**: Use Pentaho Report Designer to create a new report. Embed scripts such as BeanShell code for system command execution or JavaScript for client-side exploitation. Save the file as a .prpt archive containing the malicious elements.

**Expected Output**: A .prpt file ready for upload, containing verifiable embedded scripts.

**Success Indicators**:
- Report file generates without errors in designer
- Embedded scripts parse correctly in preview

### Step 3: Upload and Execute
procedure: [[procedures/Upload-and-Execute-Malicious-PRPT-Report-for-RCE]]

**Objective**: Upload the malicious PRPT report to the server and execute it to trigger remote code execution, potentially compromising the entire system.

**Instructions**: In the Pentaho interface, navigate to the report upload section, select the crafted .prpt file, and upload it. Then, schedule or run the report to invoke the embedded scripts, leading to arbitrary code execution on the server.

**Expected Output**: Report executes with evidence of code running, such as command output or malware deployment.

**Success Indicators**:
- Upload succeeds without validation errors
- Execution triggers server-side effects like file creation or network activity

## Attack Chain Summary

### Key Achievements

1. Unauthorized access to administrative functions via default credentials
2. Successful creation and upload of a malicious report embedding exploitable scripts
3. Achievement of remote code execution, enabling full server compromise or malware deployment

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Default Accounts]] Default Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

---
*Last updated: 2023-10-01T00:00:00Z*
