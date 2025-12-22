---
id: proc-install-http-file-server
tags:
  - setup
  - node-js
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
  - Node.js
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:12.592Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Install-Vulnerable-http-file-server

## Summary

This procedure installs the vulnerable http-file-server Node.js module version 0.2.6 globally using npm, setting up the environment for reproducing the path traversal vulnerability in a controlled testing scenario.

## Description

The http-file-server module is a simple HTTP file server for Node.js that, in version 0.2.6, suffers from a path traversal vulnerability due to unvalidated URL path concatenation. This procedure prepares the module for local testing by installing it globally, allowing subsequent steps to start the server and exploit the issue. It targets Node.js environments and assumes npm is available.

## Requirements

1. Node.js v8.9.3 or later installed
2. npm 6.4.1 or compatible package manager
3. Internet access for downloading the module from npm registry
4. Local execution privileges on a Linux or compatible system

## Defense

Defensive measures and detection strategies:

- Monitor npm installations for suspicious packages in production environments
- Use package vulnerability scanners like npm audit to detect known issues in http-file-server
- Restrict global installations with policy tools like .npmrc configurations

## Objectives

1. Install the specific vulnerable version for accurate reproduction
2. Verify module availability for server startup
3. Prepare for path traversal testing without affecting production systems

## Instructions

### Step 1: Install the Module Globally

**Context**: Use npm to fetch and install http-file-server globally, ensuring the vulnerable 0.2.6 version is used for testing.

**Command** ([[commands/npm-install-global-http-file-server]]):
```bash
npm install -g http-file-server@0.2.6
```

> This command downloads and installs the module globally. Expected output includes progress logs and a confirmation like "+ http-file-server@0.2.6 added". Verify with `http-file-server --version`.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/npm-install-global-http-file-server]]

## Tools Used

- [[tools/npm]]

## Tags

- [[setup]]
- [[node-js]]
