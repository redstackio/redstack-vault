---
tags:
  - node-js
  - installation
  - vulnerable-module
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/npm-install-md-fileserver]]'
platforms:
  - Node.js
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 261af13a-a5e9-4bec-92fc-c475022ada0c
created_at: '2025-12-14T17:26:05.910Z'
updated_at: '2025-12-14T17:26:05.910Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Install-md-fileserver-Module

## Summary

This procedure installs the vulnerable md-fileserver Node.js module (v1.3.2) globally using npm, preparing the environment for exploiting a path traversal vulnerability in a local file server scenario.

## Description

The md-fileserver module is a Node.js package designed to serve markdown files locally but contains a path traversal flaw in version 1.3.2. Installing it globally allows access to the mdstart command, which launches the server. This step is the prerequisite for reproducing the vulnerability discovered in the HackerOne report #509697, where attackers can manipulate URL paths to access files outside the intended directory. The target environment is a development or testing machine with Node.js installed, typically on Linux for accessing system files like /etc/passwd.

## Requirements

1. Node.js and npm installed on the system
2. Internet access to the npm registry
3. Local user privileges sufficient for global installation (may require sudo on some systems)

## Defense

Defensive measures and detection strategies:

- Use package managers with vulnerability scanning (e.g., npm audit) before installation
- Restrict global installations and monitor npm traffic for known vulnerable packages
- Implement application-level allowlisting for third-party modules in production environments

## Objectives

1. Download and install md-fileserver v1.3.2 globally
2. Make the mdstart command available system-wide
3. Set up for subsequent server launch and exploitation

## Instructions

### Step 1: Install the Module Globally

**Context**: This step downloads the package from the npm registry and installs it globally, enabling the vulnerable server command.

**Command** ([[commands/npm-install-md-fileserver]]):
```bash
npm install -g md-fileserver
```

> This command fetches md-fileserver version 1.3.2 (or latest vulnerable) and installs it system-wide. Expected output includes progress logs and a success message like "added X packages". Verify by running `mdstart --help` afterward.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/npm-install-md-fileserver]]

## Tools Used

- [[tools/npm]]

## Tags

- node-js
- installation
