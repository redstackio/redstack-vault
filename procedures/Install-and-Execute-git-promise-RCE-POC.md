---
id: proc-uuid-3
tags:
  - rce
  - installation
  - execution
type: procedure
tools:
  - '[[tools/npm]]'
  - '[[tools/node]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/npm-install-git-promise]]'
  - '[[commands/node-execute-poc]]'
verified: false
platforms:
  - Linux
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
  - '[[Compromise Hardware Supply Chain]]'
updated_at: '2025-12-14T17:23:24.764Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
  - '[[Compromise Hardware Supply Chain]]'
---
# Install-and-Execute-git-promise-RCE-POC

## Summary

This procedure installs the vulnerable git-promise module version 0.3.1 using npm and executes the PoC script with Node.js, triggering the RCE via command injection in child_process.exec.

## Description

The installation pulls the affected module into node_modules, then running the PoC invokes the insecure git function, concatenating user input into a shell command. This exploits the lack of sanitization on line 9 of index.js, allowing execution of 'touch HACKED' on Linux. It requires Node.js and npm, simulating a developer or server environment incorporating the module.

## Requirements

1. Node.js and npm installed
2. Internet access for npm install
3. PoC script already created in the working directory
4. Write permissions for node_modules

## Defense

Defensive measures and detection strategies:

- Pin dependencies to safe versions and use npm audit
- Scan for vulnerable packages with tools like Snyk or OWASP Dependency-Check
- Avoid direct shell execution in Node.js modules; prefer execFile
- Monitor npm installs and Node executions in logs

## Objectives

1. Deploy the vulnerable dependency
2. Trigger command injection for RCE
3. Execute arbitrary OS command as proof

## Instructions

### Step 1: Install Vulnerable Module

**Context**: Use npm to fetch git-promise@0.3.1.

**Command** ([[commands/npm-install-git-promise]]):
```bash
npm i git-promise
```

> Installs the package; expected output includes logs like 'added 1 package' and confirmation of version 0.3.1 in node_modules.

### Step 2: Execute PoC Script

**Context**: Run the script to invoke the vulnerable function.

**Command** ([[commands/node-execute-poc]]):
```bash
node poc.js
```

> Executes the script; expected output logs the git branch (e.g., 'master') and implicitly creates 'HACKED' via injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]
- [[Compromise Hardware Supply Chain]]

### Sub-Techniques


## Commands Used

- [[commands/npm-install-git-promise]]
- [[commands/node-execute-poc]]

## Tools Used

- [[tools/npm]]
- [[tools/node]]

## Tags

- rce
- installation
- execution
