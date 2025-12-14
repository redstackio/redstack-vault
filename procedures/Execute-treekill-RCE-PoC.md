---
id: proc-003
tags:
  - rce
  - command-injection
  - poc
  - node-js
type: procedure
tools:
  - '[[tools/node]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/run-node-poc-script]]'
verified: false
platforms:
  - Windows
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:20.589Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
  - '[[Exploitation for Client Execution]]'
---
# Execute-treekill-RCE-PoC

## Summary

This procedure runs a proof-of-concept script that exploits the treekill module's command injection vulnerability on Windows by passing a malicious PID string, resulting in arbitrary command execution via taskkill concatenation.

## Description

The vulnerability (HackerOne #703415) stems from index.js line 32, where pid is unsanitized and appended to 'taskkill /F /PID ' using child_process.exec on Windows. The PoC script requires treekill, then calls kill() with '3333332 & echo "HACKED" > HACKED.txt & ', injecting the echo command. This executes alongside the invalid PID kill attempt, creating the file and demonstrating RCE. Linux is unaffected due to use of kill(). Prerequisites include installed treekill and a poc.js file.

## Requirements

1. treekill@1.0.0 installed
2. Node.js runtime on Windows
3. poc.js script in current directory with: const kill = require('treekill'); kill('3333332 & echo "HACKED" > HACKED.txt & ', true);

## Defense

Defensive measures and detection strategies:

- Update to patched treekill version
- Sanitize all user inputs in shell commands
- Use spawn() over exec() for better security
- Monitor child_process.exec calls in Node.js apps

## Objectives

1. Inject malicious command via PID
2. Achieve arbitrary code execution
3. Create indicator file for validation

## Instructions

### Step 1: Run the PoC Script

**Context**: Execute the Node.js script to trigger treekill with malicious input, exploiting the concatenation flaw.

**Command** ([[commands/run-node-poc-script]]):
```bash
node poc.js
```

> The script imports treekill and invokes the vulnerable kill function. Expected output is minimal (possible taskkill error for invalid PID), but the side-effect command runs silently, creating HACKED.txt.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Windows Command Shell]] Windows Command Shell
- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used

- [[commands/run-node-poc-script]]

## Tools Used

- [[tools/node]]

## Tags

- rce
- poc
- command-injection
