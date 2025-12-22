---
id: ac-uuid-184596
tags:
  - unrestricted-file-upload
  - command-injection
  - rce
  - dod
  - navy
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
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-Exposed-File-Upload-Endpoint]]'
  - '[[procedures/Upload-Malicious-Script-File]]'
  - '[[procedures/Trigger-Command-Injection-via-Uploaded-File]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T05:32:13.366Z'
description: >-
  Exploits an internet-exposed file upload tool in a U.S. Navy system lacking
  validation, allowing arbitrary file uploads that enable command injection and
  remote code execution.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
  - '[[Windows Command Shell]]'
---
# Unrestricted File Upload Leading to Command Injection and RCE in Navy Web System

Multi-stage attack chain demonstrating exploitation of an unrestricted file upload vulnerability in an internet-accessible U.S. Navy web system, leading to remote code execution.

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
    A[Access Upload Endpoint] --> B[Upload Malicious File]
    B --> C[Trigger Execution and Injection]
    C --> D[RCE Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser or [[commands/curl-upload-file]]

### Target Environment

- Web platform with exposed file upload functionality
- No authentication required for upload
- Internet-accessible Navy system endpoint

### Initial Access Requirements

- Direct internet access to the target URL
- No credentials needed due to unrestricted access
- Basic knowledge of HTTP requests

## Detailed Attack Procedures

### Step 1: Access Exposed File Upload Endpoint
procedure: [[procedures/Access-Exposed-File-Upload-Endpoint]]

**Objective**: Locate and verify the unrestricted file upload tool accessible from the internet.

**Instructions**: Identify the target system's upload endpoint via reconnaissance or direct knowledge of the URL. Use [[commands/curl-probe-endpoint]] to confirm accessibility and lack of restrictions:

```bash
curl -X GET https://target-navy-system.com/upload
```

If the endpoint responds without authentication prompts, proceed to upload testing.

**Expected Output**: HTTP response indicating an upload form or API endpoint, such as a 200 OK with upload instructions.

**Success Indicators**:
- Endpoint is reachable without credentials
- No file type or size restrictions mentioned in response

### Step 2: Upload Malicious Script File
procedure: [[procedures/Upload-Malicious-Script-File]]

**Objective**: Upload an arbitrary malicious file, such as a script, to the server without validation.

**Instructions**: Prepare a simple malicious script file (e.g., a shell script named malicious.sh containing `whoami > /tmp/output.txt`). Use [[commands/curl-upload-file]] to submit it to the endpoint:

```bash
curl -X POST -F "file=@malicious.sh" https://target-navy-system.com/upload
```

Monitor the response for successful upload confirmation.

**Expected Output**: Server acknowledgment of file upload, possibly with a file path or ID, without error for script file types.

**Success Indicators**:
- File upload succeeds without rejection
- Uploaded file is stored on the server (verifiable if path returned)

### Step 3: Trigger Command Injection via Uploaded File
procedure: [[procedures/Trigger-Command-Injection-via-Uploaded-File]]

**Objective**: Execute the uploaded file to inject and run arbitrary commands on the server.

**Instructions**: Interact with the system to process or execute the uploaded file, exploiting improper handling. Use [[commands/curl-trigger-execution]] to request execution, assuming the system runs uploaded files (e.g., via a preview or process feature):

```bash
curl -X POST https://target-navy-system.com/process?file=malicious.sh
```

This may trigger command injection if the file is executed without sanitization.

**Expected Output**: Server response showing command execution, such as output from `whoami` or errors indicating RCE.

**Success Indicators**:
- Arbitrary command output visible in response
- File system changes or server compromise confirmed

## Attack Chain Summary

### Key Achievements

1. Gained initial access to a critical DoD system via unrestricted upload
2. Uploaded and executed malicious code leading to command injection
3. Achieved remote code execution on a high-impact Navy server

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
