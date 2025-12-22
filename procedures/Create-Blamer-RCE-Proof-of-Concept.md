---
tags:
  - rce
  - poc
  - node.js
type: procedure
tools:
  - '[[tools/node]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:24.817Z'
sub_techniques: []
id: 1e957465-cca6-4f36-a535-393095e8a50d
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Create-Blamer-RCE-Proof-of-Concept

## Summary

This procedure creates a JavaScript proof-of-concept (PoC) script that exploits the command injection vulnerability in the blamer Node.js module by passing a malicious filename to the blameByFile method, enabling arbitrary shell command execution.

## Description

The blamer module in version 0.1.13 insecurely formats user-supplied filenames into Git shell commands without validation, as seen in src/vcs/git.js line 24. By crafting a filename like 'test; touch HACKED;#', attackers can inject commands separated by semicolons and terminate the original command with a comment. This procedure focuses on writing the PoC script in a Node.js environment, assuming Git is available on the host. Prerequisites include a basic understanding of Node.js and shell injection techniques. Expected outcome is a functional script ready for execution post-installation.

## Requirements

1. Node.js installed on the system
2. Text editor or IDE for script creation
3. Git executable available in PATH

## Defense

Defensive measures and detection strategies:

- Audit third-party Node.js dependencies for known vulnerabilities using tools like npm audit
- Implement input sanitization in custom modules or avoid direct shell command usage
- Monitor for unexpected file creations or shell executions in development environments

## Objectives

1. Prepare a script that initializes blamer and triggers the vulnerable method
2. Demonstrate command injection payload construction
3. Set up for verification of RCE impact

## Instructions

### Step 1: Write the PoC Script

**Context**: Create the JavaScript file that loads the blamer module and calls the vulnerable function with injected payload.

**Command** (Manual file creation):

Create `poc.js` with:

```javascript
const Blamer = require('blamer');
const blamer = new Blamer('git');
blamer.blameByFile('poc.js', 'test; touch HACKED;#');
```

> This code requires blamer, initializes it for Git, and passes a malicious filename. The semicolon injects 'touch HACKED', and '#' comments out the rest. Expected output: Script saves without syntax errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/node]]

## Tags

- rce
- poc
- command-injection
