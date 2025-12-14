---
tags:
  - nodejs
  - rce
  - privilege-escalation
  - sandbox-escape
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/crypto-trigger-operation]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:28:44.841Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 418f0170-aa0c-4417-b57e-4657f2ea8313
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploitation for Privilege Escalation]]'
---
# Achieve-Arbitrary-Code-Execution-Bypassing-Permissions

## Summary

This procedure executes arbitrary native code loaded via an OpenSSL engine in Node.js, bypassing the permission model to disable restrictions and escalate privileges. It allows full control over the runtime, enabling further attacks like data exfiltration or persistence.

## Description

Once an OpenSSL engine is loaded, its native bind_fn executes C/C++ code unchecked by Node.js permissions. This code can manipulate internal structures, such as setting Permission::enabled_ to false, effectively disabling the model. The result is arbitrary code execution, where attackers can run unrestricted JavaScript or native operations. This targets secured Node.js environments, with impact including complete compromise. Prerequisites: Permission model enabled and engine loaded from prior procedure.

## Requirements

1. Loaded malicious OpenSSL engine from previous step.
2. Node.js 20.x runtime with permissions active.
3. Access to trigger crypto operations invoking the engine.

## Defense

Defensive measures and detection strategies:

- Patch Node.js to versions fixing OpenSSL engine restrictions in permissions.
- Use process monitoring tools to detect native code execution in sandboxed runtimes.
- Implement application-level allowlists for crypto engines.

## Objectives

1. Execute native code to alter permission state.
2. Disable the permission model for escalation.
3. Validate unrestricted access post-execution.

## Instructions

### Step 1: Invoke Engine for Native Execution

**Context**: Trigger a crypto operation that calls the engine's native functions, executing arbitrary code (e.g., permission disable).

**Command** ([[commands/crypto-trigger-operation]]):
```javascript
const hash = crypto.createHash('sha256').update('data').digest();
console.log(hash);
```

> The operation invokes the engine's bind_fn, running native code. Expected output: Successful hash computation plus any side effects from native code, like console logs indicating permission disable.

### Step 2: Verify Bypass and Escalation

**Context**: Test a previously restricted operation (e.g., native addon load or file write) to confirm permissions are bypassed.

**Command** ([[commands/node-test-escalated-access]]):
```javascript
const fs = require('fs');
fs.writeFileSync('/tmp/escalated.txt', 'bypassed');
console.log('Escalation successful');
```

> Expected output: File written without permission denial, confirming arbitrary execution and privilege escalation.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[JavaScript]]
- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used

- [[commands/crypto-trigger-operation]]
- [[commands/node-test-escalated-access]]

## Tools Used


## Tags

- nodejs
- rce
- privilege-escalation
- sandbox-escape
