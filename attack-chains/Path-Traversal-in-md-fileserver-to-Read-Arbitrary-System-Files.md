---
tags:
  - path-traversal
  - node-js
  - arbitrary-file-read
  - local-server
type: attack_chain
tools:
  - '[[tools/npm]]'
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
commands:
  - '[[commands/npm-install-md-fileserver]]'
  - '[[commands/mdstart-server]]'
  - '[[commands/curl-path-traversal-exploit]]'
platforms:
  - Web
  - Node.js
  - Linux
complexity: medium
procedures:
  - '[[procedures/Install-md-fileserver-Module]]'
  - '[[procedures/Start-md-fileserver-Server]]'
  - '[[procedures/Exploit-Path-Traversal-with-Curl]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
description: >-
  A multi-step attack exploiting path traversal in the md-fileserver Node.js
  module to install the vulnerable server, start it locally, and read sensitive
  files like /etc/passwd.
skill_level: intermediate
impact_level: high
id: de26092e-000c-45a7-8b31-7330c3bd5cc4
created_at: '2025-12-14T17:26:05.915Z'
updated_at: '2025-12-14T17:26:05.916Z'
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
# Path Traversal in md-fileserver to Read Arbitrary System Files

Multi-stage attack chain demonstrating exploitation of a path traversal vulnerability in the md-fileserver Node.js module (v1.3.2) to access files outside the intended directory, such as sensitive system files on a Linux server.

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
    A[Install Vulnerable Module] --> B[Start Local Server]
    B --> C[Exploit Path Traversal]
    C --> D[Read Sensitive Files]

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

- Node.js runtime installed
- Linux OS for testing sensitive files like /etc/passwd
- Local network access to port 8080

### Initial Access Requirements

- Local machine with npm and curl
- No remote credentials needed; exploits local server misconfiguration
- Administrative privileges not required for installation and execution

## Detailed Attack Procedures

### Step 1: Install Vulnerable Module
procedure: [[procedures/Install-md-fileserver-Module]]

**Objective**: Set up the vulnerable md-fileserver module globally to enable server startup.

**Instructions**: Use [[commands/npm-install-md-fileserver]] to install the module from the npm registry:

```bash
npm install -g md-fileserver
```

**Expected Output**: Installation logs confirming the package is downloaded and installed globally, making the mdstart command available.

**Success Indicators**:
- No errors in npm output
- mdstart command is executable in the terminal

### Step 2: Start Local Server
procedure: [[procedures/Start-md-fileserver-Server]]

**Objective**: Launch the vulnerable server on localhost:8080 to expose the path traversal endpoint.

**Instructions**: Execute [[commands/mdstart-server]] to start the server:

```bash
mdstart
```

**Expected Output**: Server startup message indicating it's listening on http://127.0.0.1:8080.

**Success Indicators**:
- Server logs show successful binding to port 8080
- No port conflicts or startup errors

### Step 3: Exploit Path Traversal
procedure: [[procedures/Exploit-Path-Traversal-with-Curl]]

**Objective**: Traverse outside the root directory to read arbitrary files, such as /etc/passwd, leading to potential data exposure.

**Instructions**: With the server running, use [[commands/curl-path-traversal-exploit]] to request a sensitive file:

```bash
curl -v --path-as-is http://127.0.0.1:8080/etc/passwd
```

**Expected Output**: Verbose HTTP response containing the contents of /etc/passwd, including user account details.

**Success Indicators**:
- HTTP 200 response with file contents
- No path normalization errors; file data is returned unescaped

## Attack Chain Summary

### Key Achievements

1. Successful installation of the vulnerable md-fileserver module
2. Launch of a local server without path validation
3. Arbitrary file read demonstrating severe impact on server confidentiality

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]

---

*Last updated: 2023-10-01T00:00:00Z*
