---
tags:
  - path-traversal
  - bypass
  - javascript
type: procedure
tools:
  - '[[tools/Node.js]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/overwrite-path-resolve]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:30:07.391Z'
sub_techniques: []
id: f74a03ee-8755-495b-bcb9-3c8865b96603
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Overwrite path.resolve Function

## Summary

This procedure overwrites Node.js's built-in path.resolve function with a custom implementation that skips normalization of traversal sequences like '../', enabling subsequent path traversal attacks in the permission model.

## Description

In Node.js, the possiblyTransformPath function in lib/internal/fs/utils.js dynamically loads pathModule.resolve, which applications can overwrite. By replacing it with a function that returns the input unchanged, paths like '/tmp/../etc/passwd' are not resolved to '/etc/passwd', bypassing permission checks. This targets the CVE-2023-30584 patch insufficiency and requires an active Node.js session with permissions enabled.

## Requirements

1. Active Node.js REPL with experimental permissions
2. Access to the 'path' module (built-in)
3. JavaScript execution environment

## Defense

Defensive measures and detection strategies:

- Freeze or protect core modules like 'path' using module sealing
- Use strict mode and avoid dynamic require in permission-sensitive code
- Audit for function overwrites in application code

## Objectives

1. Disable path normalization for traversal bypass
2. Verify the overwrite does not trigger errors
3. Set up for unauthorized file access

## Instructions

### Step 1: Assign Custom Resolve Function

**Context**: In the Node.js REPL, redefine path.resolve to return the input string without processing, preventing '../' resolution.

**Command** ([[commands/overwrite-path-resolve]]):
```javascript
path.resolve = (s) => s;
```

> No output is produced. Verify with console.log(path.resolve('/tmp/../etc/passwd')), which should output '/tmp/../etc/passwd' unchanged instead of '/etc/passwd'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/overwrite-path-resolve]]

## Tools Used

- [[tools/Node.js]]

## Tags

- path-traversal
- bypass
