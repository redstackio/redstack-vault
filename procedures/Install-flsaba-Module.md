---
id: proc-uuid-1
name: Install flsaba Module
tags:
  - setup
  - node-js
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/npm-install-flsaba]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:26.382Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---

# Install flsaba Module

## Summary

This procedure installs the vulnerable flsaba Node.js module globally, enabling the setup of a simple HTTP server with directory listing that is susceptible to stored XSS attacks.

## Description

The flsaba module version 1.1.0 is a lightweight HTTP server that lists directory contents without sanitizing file or directory names, allowing XSS payloads to be injected and executed when viewed in a browser. This step prepares the environment by installing it via npm, assuming Node.js is already present on a Linux system.

## Requirements

1. Node.js and npm installed on the system
2. Internet access to npm registry
3. Shell access with write permissions to global npm directory

## Defense

Defensive measures and detection strategies:

- Monitor npm installations for suspicious packages like flsaba
- Use package vulnerability scanners (e.g., npm audit) to detect known issues
- Restrict global npm installs via policy

## Objectives

1. Make flsaba command available for server execution
2. Set up the vulnerable component for exploitation testing
3. Verify installation without errors

## Instructions

### Step 1: Install Globally

**Context**: Use npm to fetch and install flsaba from the registry, making it executable system-wide.

**Command** ([[commands/npm-install-flsaba]]):
```bash
npm install -g flsaba
```

> This command downloads and installs version 1.1.0 (vulnerable) globally. Expected output includes progress bars and a success message confirming the module is added to the PATH.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/npm-install-flsaba]]

## Tools Used

- [[tools/npm]]

## Tags

- setup
- node-js

