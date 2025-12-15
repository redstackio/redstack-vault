---
tags:
  - path-traversal
  - node-js
  - installation
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/npm-i-mcstatic]]'
platforms:
  - Node.js
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 9165105b-338b-4c26-a0af-b5de1a460422
created_at: '2025-12-14T17:26:16.810Z'
updated_at: '2025-12-14T17:26:16.810Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Install-Vulnerable-mcstatic-Module

## Summary

This procedure installs the vulnerable mcstatic Node.js module (version 0.0.20) from the npm registry, setting up the environment for exploiting a server directory traversal vulnerability.

## Description

The mcstatic module is a static HTTP server for Node.js that suffers from improper path sanitization, allowing directory traversal attacks. Installation via npm places the module in the local node_modules directory, enabling subsequent server startup and exploitation. This step is the prerequisite for demonstrating the vulnerability in a controlled or target environment, such as a development server.

## Requirements

1. Node.js and npm installed on the system
2. Internet access to the npm registry
3. Write permissions to the current directory for node_modules creation

## Defense

Defensive measures and detection strategies:

- Use package vulnerability scanners like npm audit or Snyk to detect known vulnerable dependencies before installation
- Implement dependency pinning in package.json to avoid outdated vulnerable versions
- Monitor npm install logs for unauthorized package installations in production environments

## Objectives

1. Acquire the vulnerable mcstatic module for server setup
2. Prepare the binary executable for launching the server
3. Enable path to exploitation without prior access to the target system

## Instructions

### Step 1: Install mcstatic

**Context**: This installs the specific vulnerable version of mcstatic, pulling it from the public npm registry.

**Command** ([[commands/npm-i-mcstatic]]):
```bash
npm i mcstatic
```

> This command fetches and installs mcstatic@0.0.20 (or latest if not specified, but vulnerable in 0.0.20), creating a node_modules/mcstatic directory with the bin executable. Expected output includes progress logs and a summary like "added 1 package".

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/npm-i-mcstatic]]

## Tools Used

- [[tools/npm]]

## Tags

- path-traversal
- node-js
