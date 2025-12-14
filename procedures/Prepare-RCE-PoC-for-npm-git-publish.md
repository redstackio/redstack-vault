---
tags:
  - rce
  - poc-creation
  - command-injection
type: procedure
tools:
  - '[[tools/node]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Linux
  - Node.js
techniques:
  - '[[Unix Shell]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 91aa9992-5a2f-4a35-9f6e-17aa3b6feac2
created_at: '2025-12-14T17:23:20.109Z'
updated_at: '2025-12-14T17:23:20.109Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Prepare-RCE-PoC-for-npm-git-publish

## Summary

This procedure creates a proof-of-concept JavaScript script to exploit the RCE vulnerability in npm-git-publish by crafting a malicious remote URL that injects shell commands, setting the stage for command execution during the publish function call.

## Description

The npm-git-publish module in version 0.2.4-beta suffers from command injection due to unsanitized user input in the remote URL parameter, interpolated directly into a git push shell command at lib/publish.ts:151. This procedure focuses on preparing the PoC script and verifying the initial environment state, ensuring a clean setup before installation and execution. It targets Node.js environments on Linux, where shell commands like `touch` can create files as proof of execution. Prerequisites include a text editor and basic file system access.

## Requirements

1. Node.js installed (for later execution, though not used here)
2. Text editor (e.g., vim, nano) for script creation
3. Local directory with write permissions
4. Linux shell for manual verification

## Defense

Defensive measures and detection strategies:

- Audit dependencies for known vulnerabilities using tools like npm audit or Snyk
- Enforce input validation in third-party modules or fork/patch vulnerable code
- Monitor for unexpected file creations in development directories via filesystem auditing (e.g., auditd on Linux)
- Use containerized environments to isolate npm installs and executions

## Objectives

1. Generate a functional PoC script that triggers the vulnerable publish function
2. Confirm clean initial state to validate post-exploitation changes
3. Prepare for safe demonstration of RCE without prior artifacts

## Instructions

### Step 1: Create PoC Script

**Context**: Write the JavaScript file that loads the module and calls publish with injected commands to demonstrate RCE.

**Command** (Manual file creation):

Create `poc.js` with:
```javascript
const git = require('npm-git-publish');
git.publish('.', 'http://gihub.com ;touch HACKED; #');
```

> This loads the module and passes a malicious URL: a fake repo followed by `;touch HACKED; #` to inject the command after the git push attempt. The semicolon separates commands, and the comment (#) prevents parsing errors.

### Step 2: Verify No HACKED File

**Context**: Ensure the environment is pristine to measure exploitation impact.

**Command** (Manual check):
```bash
ls -la | grep HACKED
```

> Run `ls` or equivalent to list files; expected output is no match for HACKED, confirming absence.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/node]]

## Tags

- [[rce]]
- [[poc-creation]]
- [[command-injection]]
