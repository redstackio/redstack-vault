---
id: proc-start-mitm-brave-001
name: Start-MITM-Server-for-Brave-DnD-Attack
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:32.798Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Encrypted Channel]]'
tags:
  - mitm
  - node-js
commands:
  - '[[commands/start-mitm-server]]'
platforms:
  - macOS
tools:
  - '[[tools/Node.js]]'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Encrypted Channel]]'
---

# Start-MITM-Server-for-Brave-DnD-Attack

## Summary

This procedure launches a Node.js-based MITM server to intercept HTTPS traffic (e.g., to maps.googleapis.com) and inject malicious HTML payloads when Brave navigates to chrome://brave URLs via DnD, enabling the loading of exploit code in the privileged Muon context.

## Description

The attack targets Brave's handling of chrome://brave origins, which are vulnerable to MITM despite HTTPS Everywhere. The Node.js server (server.js) acts as a proxy, modifying responses to serve HTML that exploits the context for file reads and RCE. This is run with sudo for port binding; prerequisites include the prepared environment from prior steps. Expected outcomes: Server ready to inject payloads, leading to UXSS and IPC access upon DnD trigger.

## Requirements

1. Node.js 7.9.0 installed
2. server.js script prepared with MITM logic for domains like maps.googleapis.com
3. Sudo privileges for low-port binding

## Defense

Defensive measures and detection strategies:

- Enable HSTS and certificate pinning in browsers to prevent MITM
- Monitor for anomalous Node.js processes with sudo via endpoint detection (e.g., CrowdStrike)
- Log network traffic for localhost redirections and unexpected proxies

## Objectives

1. Intercept browser requests to inject malicious content
2. Facilitate payload delivery during DnD navigation
3. Enable privileged context exploitation for RCE

## Instructions

### Step 1: Execute MITM Server

**Context**: Run the Node.js script to start the proxy server, binding to necessary ports for interception.

**Command** ([[commands/start-mitm-server]]):
```bash
sudo node server.js
```

> This starts the server with elevated privileges, handling MITM for specified domains. Expected output: Logs like "Server listening on port 443" and readiness messages.

### Step 2: Verify Server Operation

**Context**: Test the MITM setup by sending a request to the redirected domain.

**Command** (Test Ping/Curl):
```bash
curl https://maps.googleapis.com
```

> Should return modified response from local server. Expected output: Injected content or proxy confirmation in server logs.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Encrypted Channel]] Encrypted Code Execution (MITM injection)

### Sub-Techniques


## Commands Used

- [[commands/start-mitm-server]]

## Tools Used

- [[tools/Node.js]]

## Tags

- mitm
- node-js
