---
tags:
  - rce
  - file-upload
  - null-byte
  - asp
  - iis
  - dod
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Windows
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Fuzz-for-Hidden-Repository-Endpoints]]'
  - '[[procedures/Upload-Malicious-ASP-File-with-Null-Byte]]'
  - '[[procedures/Execute-Commands-via-Uploaded-ASPShell]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T05:32:13.324Z'
description: >-
  A multi-stage attack exploiting a file upload vulnerability in a U.S.
  Department of Defense web application to achieve remote code execution through
  null byte injection.
skill_level: intermediate
impact_level: high
id: f65f9969-dfd7-4b59-be31-78b19d697af6
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
  - '[[Windows Command Shell]]'
---
# RCE via Null Byte File Upload Bypass in DoD Repository Endpoint

Multi-stage attack chain demonstrating exploitation of a file upload vulnerability in a U.S. Department of Defense web application, allowing remote code execution (RCE) via null byte (%00) injection to bypass extension validation and upload malicious ASP scripts.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Fuzz for Endpoints] --> B[Upload Malicious File]
    B --> C[Execute Commands]
    C --> D[RCE Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web application on Windows with IIS and Classic ASP
- Exposed repository endpoints (e.g., /repo/)
- No authentication required for upload endpoint

### Initial Access Requirements

- Direct network access to the target web application
- No prior credentials needed
- Ability to intercept and modify HTTP requests

## Detailed Attack Procedures

### Step 1: Identify Vulnerable Repository Endpoints
procedure: [[procedures/Fuzz-for-Hidden-Repository-Endpoints]]

**Objective**: Discover hidden repository endpoints through fuzzing to identify potential upload points.

**Instructions**: Use fuzzing techniques to probe for endpoints containing 'repos', such as https://target/repo/, https://target/c█████████/, and https://target/███████/. This step uncovers the vulnerable /repo/orbital/repo.asp endpoint.

**Expected Output**: List of discovered endpoints responsive to fuzzing inputs.

**Success Indicators**:
- Endpoints like /repo/ return 200 OK or upload forms
- Confirmation of file upload functionality

### Step 2: Upload Malicious File Using Null Byte Bypass
procedure: [[procedures/Upload-Malicious-ASP-File-with-Null-Byte]]

**Objective**: Bypass file extension validation by appending a null byte (%00) to upload a malicious ASP script disguised as a PNG file.

**Instructions**: Intercept the upload request with [[tools/Burp-Suite]] and modify the filename to 'poc.asp%00.png'. Send a POST request to /repo/orbital/repo.asp?fileToUpload=pizza.asp with multipart/form-data containing ASP shell code that enables command execution.

**Expected Output**: Successful upload response (e.g., 200 OK) and file saved as poc.asp in /savefiles/ directory.

**Success Indicators**:
- File upload succeeds without validation errors
- Uploaded file accessible at https://target/savefiles/poc.asp

### Step 3: Access Uploaded Shell and Execute Commands
procedure: [[procedures/Execute-Commands-via-Uploaded-ASPShell]]

**Objective**: Interact with the uploaded ASP shell to execute arbitrary commands, demonstrating RCE.

**Instructions**: Visit https://target/savefiles/poc.asp?cmd=dir to execute the [[commands/windows-dir]] command. The ASP script processes the 'cmd' parameter using [[commands/windows-cmd-c]] to run system commands and return output.

**Expected Output**: Output from the 'dir' command listing the directory contents.

**Success Indicators**:
- Command output displayed in the HTTP response
- Ability to run further commands confirming server control

## Attack Chain Summary

### Key Achievements

1. Discovery of hidden repository endpoints via fuzzing
2. Successful upload of malicious ASP script bypassing null byte validation
3. Achievement of RCE with arbitrary command execution on the Windows server

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Remote File Copy]]
- [[Windows Command Shell]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
