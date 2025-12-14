---
id: proc-uuid-1
tags:
  - installation
  - setup
  - node.js
type: procedure
tools:
  - '[[tools/npm]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/npm-install-bunyan]]'
verified: false
platforms:
  - Node.js
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:36.185Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Install-Bunyan-Module

## Summary

This procedure installs the vulnerable version (1.8.12) of the bunyan Node.js logging module using npm, setting up the environment for exploiting the command injection vulnerability in its CLI tool.

## Description

The bunyan module is a popular JSON logging library for Node.js, but version 1.8.12 contains a critical flaw in its CLI binary where user input is unsafely interpolated into shell commands. Installation via npm places the vulnerable script at ./node_modules/bunyan/bin/bunyan, allowing local execution. This step is a prerequisite for reproduction and exploitation on a target system with Node.js installed.

## Requirements

1. Node.js runtime (version compatible with bunyan 1.8.12)
2. npm package manager access
3. Write permissions to the installation directory

## Defense

Defensive measures and detection strategies:

- Pin bunyan to patched versions (e.g., >=1.8.15)
- Monitor npm installations for bunyan in production environments
- Use containerization to isolate Node.js module executions

## Objectives

1. Deploy the vulnerable bunyan CLI tool
2. Prepare for command injection testing
3. Ensure reproducibility of the RCE vulnerability

## Instructions

### Step 1: Install Vulnerable Bunyan

**Context**: Fetch and install bunyan version 1.8.12 from the npm registry to access the flawed CLI.

**Command** ([[commands/npm-install-bunyan]]):
```bash
npm install bunyan@1.8.12
```

> This command downloads the package, installs dependencies, and creates the node_modules directory with the bunyan binary. Expected output includes installation progress and a summary confirming the addition to package.json if applicable.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques


## Commands Used

- [[commands/npm-install-bunyan]]

## Tools Used

- [[tools/npm]]

## Tags

- installation
- node.js
- setup
