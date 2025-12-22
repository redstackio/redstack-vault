---
tags:
  - installation
  - npm
  - supply-chain
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/npm-install-windows-edge]]'
techniques:
  - '[[Compromise Software Supply Chain]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 4ab51936-dff9-42ee-ad65-01ae22e7b6f7
created_at: '2025-12-14T17:23:20.056Z'
updated_at: '2025-12-14T17:23:20.056Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Compromise Software Supply Chain]]'
---
# Install-Vulnerable-windows-edge

## Summary

This procedure installs the vulnerable windows-edge Node.js module (v1.0.1) using npm to prepare the environment for RCE exploitation.

## Description

The windows-edge module is fetched from the npm registry and installed locally, enabling the subsequent PoC execution that exploits the command injection flaw.

## Requirements

1. Node.js and npm installed on Windows
2. Internet access for npm registry

## Defense

Defensive measures and detection strategies:

- Use npm audit to scan for vulnerabilities before installation
- Pin dependencies to secure versions
- Monitor npm install logs for suspicious packages

## Objectives

1. Set up the vulnerable module
2. Enable PoC execution

## Instructions

### Step 1: Run Installation Command

**Context**: Install the module to create the exploitable setup.

**Command** ([[commands/npm-install-windows-edge]]):
```bash
npm i windows-edge
```

> This installs version 1.0.1 by default. Expected output: Logs showing package download and installation in node_modules.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Compromise Software Supply Chain]]

### Sub-Techniques


## Commands Used

- [[commands/npm-install-windows-edge]]

## Tools Used

- [[tools/npm]]

## Tags

- npm
- installation
- vulnerable-package
