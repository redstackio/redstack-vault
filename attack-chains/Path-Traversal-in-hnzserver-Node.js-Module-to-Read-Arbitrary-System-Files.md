---
id: 36b7ffdd-6727-4bad-b433-0cedc707b957
name: Path Traversal in hnzserver Node.js Module to Read Arbitrary System Files
type: attack_chain
description: >-
  A multi-step attack exploiting a path traversal vulnerability in the hnzserver
  Node.js static file server (v2.0.6) to achieve arbitrary file reads on the
  host system, such as /etc/passwd, potentially leading to information
  disclosure and further exploitation.
verified: false
submitted: true
step_count: 3
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:06.474Z'
procedures:
  - '[[procedures/Install-Vulnerable-hnzserver-Module]]'
  - '[[procedures/Start-hnzserver-Static-Server]]'
  - '[[procedures/Exploit-Path-Traversal-with-Curl]]'
techniques:
  - '[[File and Directory Discovery]]'
  - '[[Exploit Public-Facing Application]]'
tactics:
  - '[[Discovery]]'
  - '[[Initial Access]]'
tags:
  - path-traversal
  - node-js
  - arbitrary-file-read
  - information-disclosure
platforms:
  - Linux
  - Node.js
  - Web
tools:
  - '[[tools/npm]]'
  - '[[tools/hnzserver]]'
  - '[[tools/curl]]'
complexity: medium
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
  - '[[Exploit Public-Facing Application]]'
---

# Path Traversal in hnzserver Node.js Module to Read Arbitrary System Files

Multi-stage attack chain demonstrating exploitation of a path traversal vulnerability in the hnzserver Node.js module (version 2.0.6), a static file server that does not sanitize input paths. Attackers can use '../' sequences to access files outside the web root, such as sensitive system files like /etc/passwd. This was discovered by locally installing and running the module, then crafting a curl request to exploit it. The impact includes arbitrary file reads, enabling information disclosure and potential escalation to remote code execution via accessed configurations or scripts.

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
    A[Install Vulnerable Module] --> B[Start Static Server]
    B --> C[Exploit Path Traversal]
    C --> D[Arbitrary File Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/npm]]
- [[tools/hnzserver]]
- [[tools/curl]]

### Target Environment

- Linux-based system with Node.js installed
- npm version 6.9 or compatible
- Local network access to port 8888

### Initial Access Requirements

- Local administrative access to install Node.js packages globally
- No remote credentials needed; assumes local reproduction of the vulnerability
- Node.js runtime environment

## Detailed Attack Procedures

### Step 1: Install Vulnerable Module
procedure: [[procedures/Install-Vulnerable-hnzserver-Module]]

**Objective**: Install the vulnerable hnzserver module (v2.0.6) globally using npm to prepare for server execution.

**Instructions**: Navigate to a working directory and execute the installation command using [[commands/npm-install-hnzserver]]:

```bash
npm install -g hnzserver
```

**Expected Output**: Installation logs confirming successful install of hnzserver version 2.0.6, with the command now available system-wide.

**Success Indicators**:
- hnzserver command is executable from the terminal
- No errors in npm output

### Step 2: Start Static Server
procedure: [[procedures/Start-hnzserver-Static-Server]]

**Objective**: Launch the hnzserver in a controlled directory (e.g., ~/Desktop) to start serving static files on port 8888, exposing the path traversal vulnerability.

**Instructions**: Change to the ~/Desktop directory and run the server using [[commands/hnzserver-start]]:

```bash
hnzserver
```

**Expected Output**: Console message indicating "server running is :http://localhost:8888".

**Success Indicators**:
- Server starts without errors
- Accessible via browser or curl at http://127.0.0.1:8888

### Step 3: Exploit Path Traversal
procedure: [[procedures/Exploit-Path-Traversal-with-Curl]]

**Objective**: Send a crafted HTTP request to traverse directories and read arbitrary files like /etc/passwd, demonstrating information disclosure.

**Instructions**: With the server running, execute the exploit using [[commands/curl-path-traversal-exploit]]:

```bash
curl --path-as-is --url 'http://127.0.0.1:8888/../../../../etc/passwd'
```

**Expected Output**: Contents of the /etc/passwd file displayed in the terminal, confirming successful arbitrary file read due to unsanitized path handling.

**Success Indicators**:
- File contents retrieved without access denial
- No path normalization by curl (thanks to --path-as-is)

## Attack Chain Summary

### Key Achievements

1. Successful installation and execution of the vulnerable hnzserver module
2. Exposure of the static file server on localhost:8888
3. Arbitrary read of system files via path traversal, bypassing web root restrictions

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[File and Directory Discovery]] File and Directory Discovery
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Discovery]] Discovery
- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
