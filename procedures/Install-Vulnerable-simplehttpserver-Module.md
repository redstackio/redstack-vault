---
id: proc-install-simplehttpserver
tags:
  - npm
  - node-js
  - installation
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/npm-install-simplehttpserver]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Execution through Module Load]]'
updated_at: '2025-12-14T17:26:17.645Z'
skill_level: basic
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Execution through Module Load]]'
---
# Install Vulnerable simplehttpserver Module

## Summary

This procedure installs the vulnerable simplehttpserver Node.js module (v0.2.1) globally using npm, making the server executable available for deployment in a local attack setup to exploit path traversal weaknesses.

## Description

The simplehttpserver module mimics Python's SimpleHTTPServer but lacks proper path validation, allowing symlink-based traversal. Installing it globally via npm ensures the `simplehttpserver` command is accessible system-wide. This step is crucial for reproducing the vulnerability in a controlled environment, assuming Node.js and npm are pre-installed. The attack scenario involves a local attacker setting up the server to serve a directory with malicious symlinks.

## Requirements

1. Node.js (v10.9.0 or later) and npm (v6.4.1 or compatible) installed
2. Internet access to the npm registry
3. Write access to global npm directories (may require sudo on some systems)

## Defense

Defensive measures and detection strategies:

- Audit and restrict npm installations in production environments using .npmrc or policies
- Use package vulnerability scanners like npm audit to detect known issues (e.g., path traversal in simplehttpserver)
- Monitor for global installations via endpoint detection tools
- Prefer locked dependencies and avoid untrusted third-party modules

## Objectives

1. Deploy the vulnerable module for server execution
2. Enable the simplehttpserver command for the attack chain
3. Set up the environment for exploitation

## Instructions

### Step 1: Global Installation

**Context**: This installs the module from the npm registry, targeting version v0.2.1 which contains the path traversal flaw.

**Command** ([[commands/npm-install-simplehttpserver]]):
```bash
npm install simplehttpserver -g
```

> The `-g` flag installs globally, and 'simplehttpserver' is the package name. Expected output includes download progress and 'added X packages' on success. Errors may occur if network issues or permission denials arise; resolve with sudo if needed.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Execution through Module Load]] Shared Modules

### Sub-Techniques


## Commands Used

- [[commands/npm-install-simplehttpserver]]

## Tools Used

- [[tools/npm]]

## Tags

- npm
- installation
