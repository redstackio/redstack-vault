---
tags:
  - open-redirect
  - phishing
  - node-js
  - vulnerability
type: attack_chain
tools:
  - '[[tools/npm]]'
  - '[[tools/touch]]'
  - '[[tools/hekto]]'
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - Node.js
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Install-Hekto-Module]]'
  - '[[procedures/Create-Trigger-HTML-File]]'
  - '[[procedures/Start-Hekto-Server]]'
  - '[[procedures/Test-Open-Redirect]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Phishing]]'
updated_at: '2025-12-14T17:24:27.124Z'
description: >-
  Demonstrates exploitation of an open redirect vulnerability in the hekto
  Node.js module to redirect users to arbitrary external domains, facilitating
  phishing attacks.
skill_level: intermediate
impact_level: high
id: caeaa419-47ab-4821-9aee-51ad1b388e9b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Phishing]]'
---
# Hekto Node.js Open Redirect Enabling Phishing Attacks

Multi-stage attack chain demonstrating the exploitation of an open redirect vulnerability in the hekto Node.js module version 0.2.3. The vulnerability occurs due to improper path handling in the redirection logic for extensionless HTML files. By creating a file named after a target domain (e.g., 'hackerone.com.html') and accessing the server with a double slash path (e.g., '//hackerone.com'), the server issues a 307 redirect to a protocol-relative URL like '//hackerone.com/', which can be controlled by an attacker to point to malicious sites. This enables phishing by tricking users into visiting attacker-controlled domains.

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
    A[Install Vulnerable Module] --> B[Create Trigger File]
    B --> C[Start Server]
    C --> D[Test Redirect for Phishing]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/npm]]
- [[tools/touch]]
- [[tools/hekto]]
- [[tools/curl]]

### Target Environment

- Node.js environment (version 9.6.1 or compatible)
- npm (version 5.6.0 or compatible)
- Local server setup on port 3000
- Unix-like system for touch and curl commands

### Initial Access Requirements

- Local machine with Node.js installed
- No network credentials needed; local reproduction
- Administrative access not required

## Detailed Attack Procedures

### Step 1: Install Vulnerable Module
procedure: [[procedures/Install-Hekto-Module]]

**Objective**: Install the vulnerable hekto module to set up the exploitation environment.

**Instructions**: Use [[commands/install-hekto-module]] to fetch and install the package via npm.

```bash
npm install hekto
```

**Expected Output**: Installation logs confirming the package is added to node_modules, including version 0.2.3.

**Success Indicators**:
- Package installed without errors
- node_modules/hekto directory created

### Step 2: Create Trigger File
procedure: [[procedures/Create-Trigger-HTML-File]]

**Objective**: Create an HTML file named after a domain to trigger the faulty redirection logic.

**Instructions**: Execute [[commands/create-trigger-html-file]] in the document root directory.

```bash
touch hackerone.com.html
```

**Expected Output**: No output; the empty file 'hackerone.com.html' is created.

**Success Indicators**:
- File exists in the current directory
- ls command shows 'hackerone.com.html'

### Step 3: Start Server
procedure: [[procedures/Start-Hekto-Server]]

**Objective**: Launch the hekto server to expose the directory and activate the vulnerable redirection.

**Instructions**: Run [[commands/start-hekto-server]] to start the HTTP server on port 3000.

```bash
./node_modules/hekto/bin/hekto.js serve
```

**Expected Output**: Server startup message indicating it's listening on http://127.0.0.1:3000.

**Success Indicators**:
- Server process running
- Accessible via browser or curl on localhost:3000

### Step 4: Test Redirect
procedure: [[procedures/Test-Open-Redirect]]

**Objective**: Trigger and verify the open redirect to confirm phishing potential.

**Instructions**: Use [[commands/test-open-redirect]] to send a request with the double slash path.

```bash
curl -i http://127.0.0.1:3000//hackerone.com
```

**Expected Output**: HTTP/1.1 307 Temporary Redirect with Location: //hackerone.com/ header.

**Success Indicators**:
- 307 status code received
- Redirect Location points to protocol-relative URL

## Attack Chain Summary

### Key Achievements

1. Successful installation and setup of the vulnerable hekto module
2. Creation of a trigger file that exploits path handling flaws
3. Launch of a server exhibiting the open redirect behavior
4. Demonstration of arbitrary domain redirection for phishing

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Phishing]] Phishing

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---

*Last updated: 2023-10-01T00:00:00Z*
