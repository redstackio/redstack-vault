---
tags:
  - setup
  - node.js
  - installation
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/npm-install-mcstatic]]'
platforms:
  - Node.js
  - Linux
techniques:
  - '[[Remote File Copy]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 36505daf-96e9-4cc3-ae4d-a3b6cdff8f91
created_at: '2025-12-14T17:26:12.260Z'
updated_at: '2025-12-14T17:26:12.260Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Install-mcstatic-Module

## Summary

This procedure installs the vulnerable mcstatic Node.js module version 0.0.20 using npm, setting up the environment for subsequent server startup and path traversal exploitation.

## Description

The mcstatic module is a simple file server for Node.js, but version 0.0.20 contains a path traversal vulnerability due to improper sanitization of request URLs in staticFileHandler.js and responseHandlers.js. Installation prepares the binary for execution, allowing the server to be run from the current directory. This step is a prerequisite for demonstrating the vulnerability in a controlled environment, typically on a Linux host with Node.js installed.

## Requirements

1. Node.js v8.9.4 LTS or compatible installed
2. npm 5.6.0 or later
3. Local write access to the current directory for node_modules

## Defense

Defensive measures and detection strategies:

- Use package vulnerability scanners like npm audit to detect known vulnerable dependencies
- Implement dependency pinning or lockfiles to avoid installing outdated versions
- Monitor npm install logs for suspicious package names

## Objectives

1. Install the specific vulnerable version of mcstatic
2. Verify the module is ready for server execution
3. Set up a reproducible environment for exploitation testing

## Instructions

### Step 1: Install the Module

**Context**: This step uses npm to fetch and install mcstatic version 0.0.20, placing it in the local node_modules directory.

**Command** ([[commands/npm-install-mcstatic]]):
```bash
npm install mcstatic
```

> This command downloads the package and its dependencies, outputting installation progress and confirmation. Expected output includes lines like "added 1 package" and the package.json update.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used

- [[commands/npm-install-mcstatic]]

## Tools Used

- [[tools/npm]]

## Tags

- setup
- node.js
