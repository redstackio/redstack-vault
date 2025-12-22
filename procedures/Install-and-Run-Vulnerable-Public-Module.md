---
id: proc-001
tags:
  - xss
  - node-js
  - installation
type: procedure
tools:
  - '[[tools/npm]]'
  - '[[tools/public-module]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/npm-i-public]]'
  - '[[commands/public-bin-start-server]]'
verified: false
platforms:
  - Node.js
  - macOS
submitted: true
created_at: '2024-01-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:02.762Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Install-and-Run-Vulnerable-Public-Module

## Summary

This procedure installs the vulnerable 'public' Node.js module (v0.1.3) using npm and starts its static file server with directory indexing, setting up the environment for stored XSS exploitation via unsanitized filenames.

## Description

The 'public' module is a simple static file hosting server that enables directory indexing without sanitizing filenames in the generated HTML. By installing and running it, an attacker prepares a local server where malicious files can be placed to inject XSS payloads into directory listings viewed by victims. This is typically used in scenarios where the server is exposed publicly or shared, leading to browser-based code execution. Prerequisites include Node.js and npm installed on a Unix-like system.

## Requirements

1. Node.js and npm installed (version compatible with module 0.1.3)
2. Port 6060 available and not firewalled
3. Local directory to serve (current working directory)
4. Unix-like OS (e.g., macOS) for command execution

## Defense

Defensive measures and detection strategies:

- Update to a patched version or avoid using unmaintained modules like 'public'
- Implement filename sanitization and HTML escaping in custom servers
- Monitor for unusual npm installations and server startups in logs
- Use Content Security Policy (CSP) in browsers to mitigate XSS

## Objectives

1. Install the vulnerable module without errors
2. Start the server serving the target directory
3. Verify server accessibility for subsequent exploitation

## Instructions

### Step 1: Install the Module

**Context**: Download and install the 'public' module from the npm registry to access its binary.

**Command** ([[commands/npm-i-public]]):
```bash
npm i public
```

> This command installs the module locally, creating a node_modules/public directory. Expected output includes progress logs and confirmation like "added 1 package".

### Step 2: Start the Server

**Context**: Launch the server to host static files with directory indexing on the specified port.

**Command** ([[commands/public-bin-start-server]]):
```bash
./node_modules/public/bin/public ./ 6060
```

> This executes the module's binary, serving the current directory (./) on port 6060. Expected output is a message like "Server running at http://0.0.0.0:6060".

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/npm-i-public]]
- [[commands/public-bin-start-server]]

## Tools Used

- [[tools/npm]]
- [[tools/public-module]]

## Tags

- xss
- node-js
- setup
