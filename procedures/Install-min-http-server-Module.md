---
id: proc-uuid-1234
tags:
  - installation
  - node-js
  - setup
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/npm-install-min-http-server]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:17.332Z'
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
# Install-min-http-server-Module

## Summary

This procedure installs the vulnerable min-http-server Node.js module globally using npm, preparing the environment for demonstrating the path traversal vulnerability.

## Description

The min-http-server is a lightweight HTTP static resource server. Installing it globally allows execution from the command line. This step is essential for reproducing the vulnerability in a controlled local environment. The target is a local Node.js setup, and no remote access is required. Expected outcome is a successful installation enabling server startup.

## Requirements

1. Node.js and npm installed on the system
2. Internet access for package download
3. Administrative privileges for global installation

## Defense

Defensive measures and detection strategies:

- Monitor npm installations for unauthorized packages
- Use package managers with audit features to scan for known vulnerabilities
- Restrict global installs via policy

## Objectives

1. Prepare the vulnerable module for exploitation testing
2. Ensure the server binary is available system-wide
3. Verify installation integrity

## Instructions

### Step 1: Install the Module

**Context**: This installs min-http-server globally, making it executable from any directory.

**Command** ([[commands/npm-install-min-http-server]]):
```bash
npm install min-http-server -g
```

> This command downloads and installs the package. Expected output includes progress logs and a confirmation message like "added X packages".

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/npm-install-min-http-server]]

## Tools Used

- [[tools/npm]]

## Tags

- installation
- node-js
