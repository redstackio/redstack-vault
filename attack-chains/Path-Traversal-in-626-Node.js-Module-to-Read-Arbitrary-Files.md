---
tags:
  - path-traversal
  - node-js
  - arbitrary-file-read
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/npm]]'
  - '[[tools/node-js]]'
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
  - Node.js
  - Linux
submitted: true
complexity: medium
created_at: '2024-01-01T00:00:00Z'
procedures:
  - '[[procedures/Install-Vulnerable-626-Module]]'
  - '[[procedures/Start-626-HTTP-Server]]'
  - '[[procedures/Exploit-Path-Traversal-with-Curl]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:12.218Z'
description: >-
  A multi-stage attack exploiting a path traversal vulnerability in the 626
  Node.js module to install the vulnerable package, start its HTTP server, and
  read arbitrary sensitive files like /etc/passwd from the remote server.
skill_level: intermediate
impact_level: high
id: 3c6039e3-2cc4-4bdf-aac7-9e2ec3c32102
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
---
# Path Traversal in 626 Node.js Module to Read Arbitrary Files

Multi-stage attack chain demonstrating exploitation of a path traversal vulnerability in the 626 Node.js module, allowing arbitrary file reads on the server.

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
    A[Install Vulnerable Module] --> B[Start HTTP Server]
    B --> C[Exploit Path Traversal]
    C --> D[Read Arbitrary Files]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/npm]]
- [[tools/node-js]]
- [[tools/curl]]

### Target Environment

- Node.js runtime (v8.9.3 or compatible)
- Linux-based server (for /etc/passwd access)
- Network access to localhost:8080

### Initial Access Requirements

- Local machine with npm and Node.js installed
- No prior credentials needed; exploits public-facing HTTP server

## Detailed Attack Procedures

### Step 1: Install Vulnerable Module

procedure: [[procedures/Install-Vulnerable-626-Module]]

**Objective**: Set up the vulnerable environment by installing the 626 Node.js module version 1.1.1.

**Instructions**: Use [[commands/npm-install-626]] to install the package:

```bash
npm install 626
```

**Expected Output**: Installation logs confirming the package is added to node_modules/626.

**Success Indicators**:
- Package directory created in node_modules
- No installation errors

### Step 2: Start HTTP Server

procedure: [[procedures/Start-626-HTTP-Server]]

**Objective**: Launch the vulnerable HTTP server exposed on port 8080.

**Instructions**: Execute [[commands/start-626-server]] to run the index.js script:

```bash
./node_modules/626/index.js
```

**Expected Output**: Server startup message indicating 'Listening on 8080'.

**Success Indicators**:
- Server process running
- Port 8080 listening (verify with netstat or similar)

### Step 3: Exploit Path Traversal

procedure: [[procedures/Exploit-Path-Traversal-with-Curl]]

**Objective**: Craft an HTTP request to traverse directories and read sensitive files like /etc/passwd.

**Instructions**: Send a GET request using [[commands/curl-path-traversal-exploit]] with traversal sequences:

```bash
curl -v --path-as-is http://127.0.0.1:8080/../../../../etc/passwd
```

Adjust '../' count based on directory depth. The --path-as-is flag prevents normalization.

**Expected Output**: HTTP 200 response containing /etc/passwd contents, such as user entries starting with 'root:x:0:0'.

**Success Indicators**:
- File contents retrieved
- No 404 or access denied errors

## Attack Chain Summary

### Key Achievements

1. Installed and ran the vulnerable 626 module server
2. Exploited path traversal to bypass directory restrictions
3. Read arbitrary system files, enabling information disclosure

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]

---

*Last updated: 2024-01-01T00:00:00Z*
