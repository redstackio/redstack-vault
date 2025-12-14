---
id: proc-monkey-patch-buffer
name: Monkey-Patch-Buffer-utf8Write
type: procedure
verified: false
submitted: true
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.230Z'
tactics:
  - '[[Privilege Escalation]]'
techniques:
  - '[[Process Injection]]'
sub_techniques: []
tags:
  - monkey-patch
  - buffer
  - path-traversal
commands:
  - '[[commands/buffer-utf8write-monkeypatch]]'
platforms:
  - Node.js
  - Linux
tools:
  - '[[tools/Node.js]]'
skill_level: intermediate
impact_level: medium
detection_risk: high
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Process Injection]]'
---

# Monkey-Patch-Buffer-utf8Write

## Summary

This procedure monkey-patches the Buffer.prototype.utf8Write method to intercept and modify path strings during conversion in the Node.js permission model, enabling path traversal by replacing prefixes after path.resolve() sanitization.

## Description

In the Node.js permission model, paths are resolved with path.resolve() for sanitization but then converted to Buffers using Buffer.from(), which calls utf8Write. By overwriting this prototype method, attackers can alter the path post-resolution without triggering re-sanitization, as seen in lib/internal/fs/utils.js's possiblyTransformPath function. This bypasses restrictions like --allow-fs-read=/tmp.

## Requirements

1. Node.js REPL running with experimental permissions enabled
2. JavaScript execution access in the REPL
3. Knowledge of Buffer internals

## Defense

Defensive measures and detection strategies:

- Avoid using experimental permission model
- Freeze prototypes to prevent monkey-patching (e.g., Object.freeze(Buffer.prototype))
- Audit for prototype modifications in runtime logs

## Objectives

1. Intercept Buffer string writes
2. Modify paths to include traversal sequences
3. Enable unauthorized access post-sanitization

## Instructions

### Step 1: Overwrite utf8Write Method

**Context**: Apply the patch in the REPL to hook into Buffer.from() calls used by fs operations.

**Command** ([[commands/buffer-utf8write-monkeypatch]]):
```javascript
Buffer.prototype.utf8Write = ((w) => function (str, ...args) { return w.apply(this, [str.replace(/^\/exploit/, '/tmp/..'), ...args]); })(Buffer.prototype.utf8Write);
```

> This captures the original method 'w', replaces '/exploit' with '/tmp/..' in the string, and calls the original. Expected output is the function reference. Verify by checking Buffer.prototype.utf8Write.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Process Injection]]

### Sub-Techniques


## Commands Used

- [[commands/buffer-utf8write-monkeypatch]]

## Tools Used

- [[tools/Node.js]]

## Tags

- monkey-patch
- buffer
- path-traversal
