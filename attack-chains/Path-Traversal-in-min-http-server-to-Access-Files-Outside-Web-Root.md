---
id: ac-uuid-1234
tags:
  - path-traversal
  - node-js
  - web-server
  - file-access
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/npm]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Install-min-http-server-Module]]'
  - '[[procedures/Start-min-http-server]]'
  - '[[procedures/Exploit-Path-Traversal-with-Burp-Suite]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:17.348Z'
description: >-
  Demonstrates exploiting a path traversal vulnerability in the min-http-server
  Node.js module to access and list sensitive files outside the intended
  directory.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
---
# Path Traversal in min-http-server to Access Files Outside Web Root

Multi-stage attack chain demonstrating exploitation of a path traversal vulnerability in the min-http-server Node.js module, allowing unauthorized access to files outside the web root.

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
    B --> C[Exploit Traversal]
    C --> D[Access Sensitive Files]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/npm]]
- [[tools/Burp-Suite]]

### Target Environment

- Node.js runtime installed
- Local machine with npm access
- No specific ports required beyond default 8000

### Initial Access Requirements

- Local system access to install and run Node.js modules
- No network credentials needed; targets local server

## Detailed Attack Procedures

### Step 1: Install min-http-server Module
procedure: [[procedures/Install-min-http-server-Module]]

**Objective**: Set up the vulnerable min-http-server module on the system.

**Instructions**: Use [[commands/npm-install-min-http-server]] to install globally:

```bash
npm install min-http-server -g
```

**Expected Output**: Installation logs confirming successful global install of the module.

**Success Indicators**:
- Module installed without errors
- Command `min-http-server` available in PATH

### Step 2: Start min-http-server
procedure: [[procedures/Start-min-http-server]]

**Objective**: Launch the vulnerable HTTP server to expose the path traversal flaw.

**Instructions**: Execute [[commands/min-http-server-start]] to start the server:

```bash
min-http-server
```

**Expected Output**: Server startup message indicating it's listening on port 8000.

**Success Indicators**:
- Server running and accessible at http://localhost:8000
- No errors in console output

### Step 3: Exploit Path Traversal with Burp Suite
procedure: [[procedures/Exploit-Path-Traversal-with-Burp-Suite]]

**Objective**: Craft and send requests with '../' sequences to bypass path restrictions and access files outside the web root.

**Instructions**: Configure [[tools/Burp-Suite]] in proxy mode, intercept a request to the server, and modify the URL path to include traversal sequences, such as http://localhost:8000/../etc/passwd. Send the modified request.

**Expected Output**: Server response containing contents of the targeted file, like /etc/passwd.

**Success Indicators**:
- Unauthorized file contents returned in response
- Ability to list or read files from parent directories

## Attack Chain Summary

### Key Achievements

1. Successful installation and startup of the vulnerable server
2. Bypassing URL normalization to exploit path traversal
3. Accessing sensitive system files, enabling potential data exposure or further attacks

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
