---
id: proc-uuid-1
tags:
  - xss
  - setup
  - node-js
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/npm-install-glance]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:46.976Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Install-Glance-Node-Module

## Summary

This procedure installs the vulnerable Glance Node.js module using npm, preparing the environment for exploiting the Stored XSS vulnerability in directory listings.

## Description

The Glance module is a simple HTTP server for static files that fails to sanitize file names, allowing XSS payloads. This step sets up the module locally or globally, enabling subsequent steps to create and serve malicious files. It targets Node.js environments and requires basic package management knowledge.

## Requirements

1. Node.js and npm installed on the system
2. Internet access for package download
3. Write permissions in the working directory

## Defense

Defensive measures and detection strategies:

- Monitor npm installations for suspicious packages like 'glance'
- Use package vulnerability scanners (e.g., npm audit) to detect known issues
- Restrict npm installs to trusted sources

## Objectives

1. Install the Glance module without errors
2. Prepare node_modules for server execution
3. Enable static file serving for exploitation

## Instructions

### Step 1: Install via npm

**Context**: This installs the Glance package, creating the necessary binaries for the server.

**Command** ([[commands/npm-install-glance]]):
```bash
npm install glance
```

> This command fetches and installs the glance package from the npm registry, outputting logs of dependencies and confirmation. Expected output includes "added X packages" and placement in ./node_modules.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/npm-install-glance]]

## Tools Used

- [[tools/npm]]

## Tags

- xss
- node-js
- installation
