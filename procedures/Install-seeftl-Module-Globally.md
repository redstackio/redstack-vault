---
tags:
  - xss
  - node.js
  - installation
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/npm-install-seeftl-global]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:09.696Z'
sub_techniques: []
id: 38e56b48-9ef4-4ae4-ba8d-55e040792b21
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Install-seeftl-Module-Globally

## Summary

This procedure installs the vulnerable seeftl Node.js module globally using npm, enabling the static file server that exposes the stored XSS vulnerability in directory listings.

## Description

The seeftl module (version 0.1.1) is a simple static file server for Node.js. Installing it globally makes the 'seeftl' command available system-wide, allowing it to serve files from any directory. This sets up the environment for exploiting the lack of filename sanitization, where malicious JavaScript in filenames is rendered directly into HTML without encoding, leading to stored XSS when users view directory listings.

## Requirements

1. Node.js and npm installed on the system
2. Internet access to the npm registry
3. Administrative privileges for global installation (or configure npm for user-level install)

## Defense

Defensive measures and detection strategies:

- Use package vulnerability scanners like npm audit before installation
- Avoid global installs of untrusted modules; prefer local or Docker isolation
- Monitor for anomalous npm installs in logs

## Objectives

1. Prepare the attack environment by installing the affected module
2. Enable the seeftl command for server startup
3. Set the stage for XSS payload injection and execution

## Instructions

### Step 1: Install seeftl Globally

**Context**: This step fetches and installs the seeftl package from the npm registry, making it executable.

**Command** ([[commands/npm-install-seeftl-global]]):
```bash
npm install seeftl -g
```

> This command downloads version 0.1.1 (vulnerable) and installs it globally. Expected output includes progress bars, dependency resolutions, and a final success message like "+ seeftl@0.1.1".

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/npm-install-seeftl-global]]

## Tools Used

- [[tools/npm]]

## Tags

- xss
- node.js
