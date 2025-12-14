---
id: proc-node-enable-permission
name: Node-Enable-Experimental-Permission-Model
type: procedure
verified: false
submitted: true
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.234Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - node.js
  - permission-model
commands:
  - '[[commands/node-enable-experimental-permission]]'
platforms:
  - Node.js
  - Linux
tools:
  - '[[tools/Node.js]]'
skill_level: intermediate
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Node-Enable-Experimental-Permission-Model

## Summary

This procedure launches the Node.js REPL with the experimental permission model enabled and restricts file system read access to the /tmp directory, setting up a controlled environment to demonstrate permission bypass vulnerabilities.

## Description

The experimental permission model in Node.js versions 20.x and 21.x allows granular control over file system operations. By enabling it with specific flags, attackers can simulate restricted environments and prepare for exploitation. This step is crucial as it establishes the baseline restrictions that subsequent monkey-patching will bypass, targeting the implementation in lib/internal/fs/utils.js where path sanitization occurs via path.resolve() before Buffer conversion.

## Requirements

1. Node.js version 20.x or 21.x installed
2. Linux environment with shell access
3. No prior permissions setup needed

## Defense

Defensive measures and detection strategies:

- Disable experimental permission model in production
- Monitor for unusual Node.js flag usage in process lists
- Use sandboxing tools like Docker to isolate Node.js execution

## Objectives

1. Activate the permission model to enforce FS restrictions
2. Limit read access to /tmp for testing
3. Verify restrictions by attempting unauthorized reads

## Instructions

### Step 1: Launch Node.js REPL with Flags

**Context**: Start the interactive REPL to enable permissions and set read restrictions, preparing the vulnerable runtime.

**Command** ([[commands/node-enable-experimental-permission]]):
```bash
node --experimental-permission --allow-fs-read=/tmp
```

> This command enables the experimental permission model and allows fs.read only within /tmp. Expected output is the Node.js welcome message. Test restrictions by trying fs.readFileSync('/etc/passwd') which should fail with a permission error.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/node-enable-experimental-permission]]

## Tools Used

- [[tools/Node.js]]

## Tags

- node.js
- permission-model
