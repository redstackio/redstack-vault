---
tags:
  - rce
  - installation
  - execution
type: procedure
tools:
  - '[[tools/npm]]'
  - '[[tools/node]]'
  - '[[tools/blamer]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/npm-install-blamer]]'
  - '[[commands/node-execute-poc]]'
verified: false
platforms:
  - Node.js
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:24.795Z'
sub_techniques: []
id: 47cfbc94-c708-477c-91fe-a40edff5bb8e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
  - '[[Exploitation for Client Execution]]'
---
# Install-and-Execute-Blamer-RCE-PoC

## Summary

This procedure installs the vulnerable blamer module version 0.1.13 and executes the PoC script, triggering the RCE via command injection in the Git blame function.

## Description

Exploitation requires installing the specific vulnerable version and running the prepared PoC, which calls blameByFile with injected payload. The module's src/vcs/git.js at line 24 directly interpolates the filename into a shell command, executing the injected 'touch HACKED'. This occurs in a local Node.js setup with Git. Expected outcome: Silent execution of the shell command, demonstrating RCE.

## Requirements

1. Node.js and npm installed
2. PoC script (`poc.js`) already created
3. Internet access for npm install

## Defense

Defensive measures and detection strategies:

- Pin dependencies to safe versions and use lockfiles
- Scan for vulnerable packages with tools like Snyk or npm audit
- Log npm installations and Node.js executions for anomalies

## Objectives

1. Deploy the vulnerable module
2. Invoke the exploitation path
3. Achieve arbitrary command execution

## Instructions

### Step 1: Install Vulnerable Module

**Context**: Use npm to install blamer version 0.1.13, setting up the environment.

**Command** ([[commands/npm-install-blamer]]):

```bash
npm i blamer@0.1.13
```

> Installs the module into node_modules. Expected output: Installation logs confirming version 0.1.13.

### Step 2: Execute PoC Script

**Context**: Run the script to trigger the vulnerable method and inject the shell command.

**Command** ([[commands/node-execute-poc]]):

```bash
node poc.js
```

> Executes the script, causing Git command injection. Expected output: No errors; injected command runs silently.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]
- [[Exploitation for Client Execution]]

### Sub-Techniques


## Commands Used

- [[commands/npm-install-blamer]]
- [[commands/node-execute-poc]]

## Tools Used

- [[tools/npm]]
- [[tools/node]]
- [[tools/blamer]]

## Tags

- rce
- install
- execute
