---
tags:
  - nodejs
  - installation
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/npm-install-global-http-file-server]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:31.314Z'
sub_techniques: []
id: 53701447-da74-4de3-95a6-8ac2db4fa1ad
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Install-http-file-server-Module

## Summary

This procedure installs the vulnerable http-file-server Node.js module globally using npm, enabling the command-line tool for serving directories and demonstrating the stored XSS vulnerability.

## Description

The http-file-server module (version 0.2.6) is a simple HTTP server for file sharing, but it suffers from stored XSS due to unsanitized filename rendering. Installing it globally allows execution from any directory. This step is a prerequisite for setting up the exploitation environment on a Linux system with Node.js.

## Requirements

1. Linux OS with Node.js and npm installed
2. Internet access for package download
3. Administrative privileges if needed for global install

## Defense

Defensive measures and detection strategies:

- Monitor npm installations for suspicious packages like http-file-server in production environments
- Use package vulnerability scanners (e.g., npm audit) to detect known issues
- Restrict global npm installs via policy

## Objectives

1. Prepare the vulnerable server for execution
2. Enable directory serving on localhost
3. Set up for subsequent XSS payload injection

## Instructions

### Step 1: Install the Module Globally

**Context**: Use npm to download and install http-file-server globally, making the 'http-file-server' command available.

**Command** ([[commands/npm-install-global-http-file-server]]):
```bash
npm install -g http-file-server
```

> This command fetches the package from the npm registry and installs it in the global node_modules directory. Expected output includes progress logs and a final success message like "+ http-file-server@0.2.6".

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/npm-install-global-http-file-server]]

## Tools Used

- [[tools/npm]]

## Tags

- nodejs
- installation
