---
id: proc-001
tags:
  - npm
  - installation
  - vulnerable-package
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/npm-install-node-df]]'
verified: false
platforms:
  - Node.js
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:24.015Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Install-Vulnerable-node-df-Module

## Summary

This procedure installs the vulnerable version (0.1.4) of the node-df Node.js module using npm, setting up the environment for command injection exploitation in a local Node.js project.

## Description

The node-df module provides disk usage information but in version 0.1.4, it insecurely concatenates user input into shell commands. Installing this specific version allows subsequent exploitation by requiring the module in a script and passing tainted input. This is typically done in a development or test environment on Linux with Node.js installed. Expected outcome is a successful installation enabling PoC execution without immediate detection.

## Requirements

1. Node.js and npm installed on a Linux system
2. Local project directory initialized (e.g., via npm init)
3. Internet access for npm registry

## Defense

Defensive measures and detection strategies:

- Use npm audit to scan for known vulnerabilities before installation
- Pin dependencies to secure versions in package.json
- Monitor npm install logs for suspicious package versions

## Objectives

1. Install node-df@0.1.4 to reproduce the RCE vulnerability
2. Prepare environment for PoC script execution
3. Ensure module is available for require() in JavaScript

## Instructions

### Step 1: Initialize Project if Needed

**Context**: Ensure a Node.js project exists to install the package.

**Command** ([[commands/npm-init-project]]):
```bash
npm init -y
```

> Initializes package.json. Expected output: Basic package.json file created.

### Step 2: Install Vulnerable Module

**Context**: Install the specific vulnerable version using npm.

**Command** ([[commands/npm-install-node-df]]):
```bash
npm i node-df@0.1.4
```

> Installs node-df version 0.1.4. Expected output: Logs showing download and addition to node_modules.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques


## Commands Used

- [[commands/npm-install-node-df]]

## Tools Used

- [[tools/npm]]

## Tags

- npm
- installation
- vulnerable-package
