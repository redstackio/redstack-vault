---
id: ac-fastify-open-redirect-001
tags:
  - open-redirect
  - fastify
  - node.js
  - phishing
  - ssrf-bypass
type: attack_chain
tools:
  - '[[tools/Firefox-Browser-for-Redirect-Testing]]'
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
  - '[[procedures/Download-Fastify-Static-PoC-Archive]]'
  - '[[procedures/Run-Fastify-Static-Vulnerable-Server]]'
  - '[[procedures/Trigger-Open-Redirect-with-Crafted-URL]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Phishing]]'
updated_at: '2025-12-14T17:24:23.275Z'
description: >-
  Multi-stage chain exploiting an open redirect vulnerability in the
  fastify-static plugin for Fastify, allowing redirection to arbitrary external
  sites via mishandled double-slash paths, enabling phishing and SSRF bypass.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Phishing]]'
---
# Fastify-Static Open Redirect via Double Slash Path Manipulation

Multi-stage attack chain demonstrating exploitation of an open redirect in the fastify-static plugin for Fastify, triggered by paths starting with double forward slashes (//), leading to arbitrary redirects primarily effective in Firefox.

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
    A[Download PoC] --> B[Run Vulnerable Server]
    B --> C[Trigger Redirect]
    C --> D[Arbitrary Site Redirect]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Firefox-Browser-for-Redirect-Testing]]

### Target Environment

- Node.js runtime
- Fastify framework with fastify-static plugin
- Port 3000 open locally

### Initial Access Requirements

- Local machine with bash shell
- Internet access for downloading PoC
- No prior credentials needed; local reproduction

## Detailed Attack Procedures

### Step 1: Download PoC Archive
procedure: [[procedures/Download-Fastify-Static-PoC-Archive]]

**Objective**: Obtain the proof-of-concept files to set up the vulnerable Fastify server.

**Instructions**: Download the fastify-static-poc.zip archive containing the vulnerable configuration and scripts.

**Expected Output**: ZIP file downloaded to local directory.

**Success Indicators**:
- PoC archive successfully downloaded and extracted
- Files including run.sh present

### Step 2: Run Vulnerable Server
procedure: [[procedures/Run-Fastify-Static-Vulnerable-Server]]

**Objective**: Start a local Fastify server with fastify-static mounted at root and redirect option enabled to reproduce the vulnerability.

**Instructions**: Extract the PoC and execute the provided script using [[commands/run-fastify-static-poc]]:

```bash
bash run.sh
```

**Expected Output**: Server starts and listens on http://localhost:3000.

**Success Indicators**:
- Server output confirms binding to port 3000
- No errors in startup logs

### Step 3: Trigger Redirect
procedure: [[procedures/Trigger-Open-Redirect-with-Crafted-URL]]

**Objective**: Send a crafted request to exploit the open redirect, bypassing domain restrictions and redirecting to an external site.

**Instructions**: Open Firefox and navigate to the malicious path http://localhost:3000//google.com/%2e%2e. This triggers a 301 redirect to //google.com/%2e%2e/, which Firefox resolves to https://www.google.com/.

**Expected Output**: Browser redirects to the arbitrary external site (e.g., Google).

**Success Indicators**:
- 301 response received with Location: //google.com/%2e%2e/
- Successful navigation to external domain

## Attack Chain Summary

### Key Achievements

1. Reproduced open redirect in fastify-static via double-slash path handling flaw
2. Demonstrated phishing potential by redirecting to arbitrary sites
3. Highlighted browser-specific behavior, effective in Firefox for SSRF bypass and OAuth token theft

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Phishing]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---

*Last updated: 2023-10-01T00:00:00Z*
