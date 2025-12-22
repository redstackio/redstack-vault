---
tags:
  - node.js
  - permission-model
  - setup
type: procedure
tools:
  - '[[tools/Node.js]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/node-enable-permissions]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:30:07.393Z'
sub_techniques: []
id: b9409ce6-d9f6-4208-84b1-1f9ca845206b
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Enable Node.js Experimental Permission Model

## Summary

This procedure starts Node.js 20.x with the experimental permission model enabled, restricting file system reads to a specific directory like /tmp to simulate a sandboxed environment vulnerable to the path traversal bypass.

## Description

The experimental permission model in Node.js 20 aims to provide fine-grained control over file system access, but it can be bypassed via path manipulation. This step sets up the restricted context by invoking Node.js with --experimental-permission and --allow-fs-read flags. It requires Node.js 20.x installed on Linux and is the foundation for demonstrating the vulnerability in lib/internal/fs/utils.js where possiblyTransformPath relies on the potentially overwritten path.resolve.

## Requirements

1. Node.js 20.x installed on a Linux system
2. Local shell access to execute Node.js
3. No prior permissions setup needed

## Defense

Defensive measures and detection strategies:

- Avoid using the experimental permission model in production until fully patched
- Monitor for unusual Node.js flag usage in process lists (e.g., ps aux | grep node)
- Implement code reviews to detect path module overwrites

## Objectives

1. Activate the permission model with FS read restrictions
2. Verify restrictions by attempting an unauthorized read
3. Prepare environment for path traversal exploit

## Instructions

### Step 1: Launch Node.js with Permissions

**Context**: Invoke Node.js to enable the model and restrict reads to /tmp, simulating an application sandbox.

**Command** ([[commands/node-enable-permissions]]):
```bash
node --experimental-permission --allow-fs-read=/tmp/
```

> This starts an interactive REPL or can run a script. Expected output is the Node.js prompt (>) with permissions active. Test by running fs.readFileSync('/etc/passwd'), which should throw a permission error.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/node-enable-permissions]]

## Tools Used

- [[tools/Node.js]]

## Tags

- node.js
- permission-model
