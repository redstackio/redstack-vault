---
tags:
  - file-upload
  - null-byte
  - rce
  - asp
  - iis
  - command-injection
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
  - '[[procedures/Access-Repository-File-Upload-Endpoint]]'
  - '[[procedures/Upload-Malicious-ASP-Shell-with-Null-Byte-Bypass]]'
  - '[[procedures/Execute-Commands-via-Uploaded-ASP-Shell]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:23:41.485Z'
description: >-
  Multi-stage attack exploiting unrestricted file upload vulnerability using
  null byte truncation to upload and execute an ASP shell, leading to remote
  code execution on a Windows IIS server.
skill_level: intermediate
impact_level: high
id: 22a64d6f-bb37-4d67-9dc2-e671713b93fb
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
  - '[[Windows Command Shell]]'
---
# RCE via Null Byte File Upload Bypass in ASP Web Repository

The vulnerability in the web repository application allows attackers to bypass file extension validation by inserting a null byte (%00) in the filename, such as 'poc.asp%00.png'. This tricks the server into saving the file with an executable .asp extension while appearing as a safe image. The uploaded ASP shell contains code to execute arbitrary commands via a WScript.Shell object. Once uploaded, accessing the shell with a 'cmd' parameter enables remote code execution (RCE), potentially compromising the entire Windows IIS server. This attack was discovered through fuzzing hidden endpoints and requires access to the public-facing web application.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Upload Endpoint] --> B[Upload Malicious Shell]
    B --> C[Execute Commands for RCE]
    C --> D[Server Compromise]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web application on Windows with IIS
- ASP (Classic ASP) enabled
- Exposed repository endpoint (e.g., /repo/orbital/repo.asp)
- No authentication required for upload

### Initial Access Requirements

- Network access to the target web server
- No credentials needed; public-facing application
- Prior reconnaissance to identify hidden upload endpoints via fuzzing

## Detailed Attack Procedures

### Step 1: Access Repository Endpoint
procedure: [[procedures/Access-Repository-File-Upload-Endpoint]]

**Objective**: Locate and access the hidden file upload functionality in the repository application to prepare for exploitation.

**Instructions**: Navigate to the repository endpoint, such as 'https://target.com/repo/orbital/repo.asp?fileToUpload=pizza.asp', which exposes the upload form. Use browser developer tools or a proxy to inspect for hidden parameters.

**Expected Output**: Upload page loads, revealing multipart/form-data submission capability.

**Success Indicators**:
- Endpoint responds with 200 OK
- Form fields for file upload are present

### Step 2: Upload Malicious ASP Shell with Null Byte Bypass
procedure: [[procedures/Upload-Malicious-ASP-Shell-with-Null-Byte-Bypass]]

**Objective**: Bypass extension validation by using a null byte to upload an executable ASP shell disguised as an image, saving it to the server's /savefiles/ directory.

**Instructions**: Intercept the POST request using [[tools/Burp-Suite]]. Modify the filename to 'poc.asp%00.png' and include ASP shell code in the body that creates a WScript.Shell for command execution. Submit to '/repo/orbital/repo.asp?fileToUpload=pizza.asp'.

**Expected Output**: Server returns 500 error, but file is saved as 'poc.asp' in /savefiles/ due to null byte truncation.

**Success Indicators**:
- File appears in /savefiles/ directory
- No immediate execution, but shell is uploaded

### Step 3: Execute Commands via Uploaded ASP Shell
procedure: [[procedures/Execute-Commands-via-Uploaded-ASP-Shell]]

**Objective**: Access the uploaded shell and run arbitrary OS commands to achieve RCE, demonstrating server compromise.

**Instructions**: Visit 'https://target.com/savefiles/poc.asp?cmd=dir' to trigger the shell. The ASP script executes the 'cmd' parameter using 'cmd /c' and displays output, including directory listings.

**Expected Output**: Output shows directory contents, server variables like server_name, server_port, and LOCAL_ADDR.

**Success Indicators**:
- Command output rendered in browser
- Arbitrary commands executable, confirming RCE

## Attack Chain Summary

### Key Achievements

1. Bypassed file upload restrictions using null byte truncation
2. Uploaded and persisted an ASP webshell on IIS server
3. Achieved remote code execution with full command control

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
