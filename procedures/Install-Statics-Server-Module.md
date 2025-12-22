---
tags:
  - xss
  - node.js
  - installation
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/npm-install-statics-server]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:37.216Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 1f0cc382-364f-41bc-967f-be30a70f7664
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Install-Statics-Server-Module

## Summary

This procedure installs the vulnerable statics-server Node.js module version 0.0.9 using npm, setting up the environment for XSS exploitation via directory listings.

## Description

The statics-server module serves static files and generates HTML directory indexes without escaping filenames, allowing XSS. This step prepares the local environment by installing the module, which is necessary to reproduce the vulnerability discovered in the source code where template literals insert unescaped filenames into <a> tags.

## Requirements

1. Node.js and npm installed on the system
2. Local directory for project setup
3. Internet access for package download

## Defense

Defensive measures and detection strategies:

- Use package vulnerability scanners like npm audit to detect known issues in dependencies
- Restrict npm installations to trusted sources and review module source code before use

## Objectives

1. Install the affected module to enable server execution
2. Verify installation for vulnerability reproduction
3. Prepare for file creation and server startup

## Instructions

### Step 1: Execute NPM Install

**Context**: Install the statics-server package to add it to the local node_modules directory.

**Command** ([[commands/npm-install-statics-server]]):
```bash
npm install statics-server
```

> This command downloads and installs version 0.0.9 (vulnerable) of the module. Expected output includes installation progress and confirmation that statics-server is added.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/npm-install-statics-server]]

## Tools Used

- [[tools/npm]]

## Tags

- xss
- node.js
