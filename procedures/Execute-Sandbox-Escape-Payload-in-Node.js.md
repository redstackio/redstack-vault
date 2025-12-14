---
id: d4e5f6g7-h8i9-0123-defg-456789012345
name: Execute-Sandbox-Escape-Payload-in-Node.js
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:24.377Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - rce
  - sandbox-escape
commands:
  - '[[commands/console-log-safeeval]]'
platforms:
  - Node.js
tools:
  - '[[tools/runkit]]'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Execute-Sandbox-Escape-Payload-in-Node.js

## Summary

This procedure evaluates the crafted malicious JavaScript using safeEval in Node.js, escaping the sandbox to load the util module and execute arbitrary code, demonstrating RCE.

## Description

By passing the payload to safeEval, the procedure triggers the prototype manipulation, rebinds the Function constructor, and executes Node.js-specific code like process.mainModule.constructor._load('util').log('pwned'). This bypasses the module's attempt to wrap globals, allowing full RCE. Use in a controlled environment like runkit for testing. Expected outcome: Successful log output indicating escape.

## Requirements

1. Loaded safeEval from notevil
2. Defined malicious code string
3. Node.js REPL or script executor

## Defense

Defensive measures and detection strategies:

- Disable or remove notevil in production; use vm module with stricter contexts
- Log all safeEval invocations and inspect AST for suspicious patterns like getOwnPropertyDescriptors
- Implement canary tokens in global objects to detect unauthorized access

## Objectives

1. Trigger sandbox escape via safeEval
2. Verify RCE with module load
3. Confirm no restrictions on process access

## Instructions

### Step 1: Evaluate and Log

**Context**: Run the payload through safeEval to execute the escape.

**Command** ([[commands/console-log-safeeval]]):
```javascript
console.log(safeEval(code));
```

> This calls safeEval on the code string and logs the result. Expected output: 'pwned' printed to console via util.log.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/console-log-safeeval]]

## Tools Used

- [[tools/runkit]]

## Tags

- [[rce]]
- [[sandbox-escape]]
