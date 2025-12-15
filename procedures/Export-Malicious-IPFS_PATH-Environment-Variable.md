---
id: ba27280f-07a1-488c-ae0f-09b22794ad95
name: Export-Malicious-IPFS_PATH-Environment-Variable
type: procedure
verified: false
submitted: true
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:17.052Z'
tactics:
  - '[[Defense Evasion]]'
techniques:
  - '[[DLL Search Order Hijacking]]'
sub_techniques: []
tags:
  - environment-variable
  - path-traversal
  - hijack
commands:
  - '[[commands/export-ipfs-path]]'
platforms:
  - Linux
tools:
  - '[[tools/bash]]'
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[DLL Search Order Hijacking]]'
---

# Export-Malicious-IPFS_PATH-Environment-Variable

## Summary

This procedure sets the IPFS_PATH environment variable to the exploit directory, hijacking curl's IPFS resolution to enable path traversal to arbitrary files.

## Description

Curl uses IPFS_PATH without sanitization for IPFS URLs, allowing attackers to point it to a controlled directory with symlinks. This leads to traversal (e.g., via '../') resolving to system files, leaking content in errors. Applicable in Linux shells where curl is invoked.

## Requirements

1. Exploit directory created from prior step
2. Bash environment for export
3. No root required; user-level access suffices

## Defense

Defensive measures and detection strategies:

- Block or sanitize environment variables in curl invocations (e.g., via wrappers)
- Monitor env var changes with auditd for IPFS_PATH
- Use container namespaces to isolate env vars

## Objectives

1. Redirect curl's IPFS path resolution to attacker-controlled location
2. Enable symlink-based traversal to sensitive files
3. Prepare for curl execution without altering curl code

## Instructions

### Step 1: Export the Variable

**Context**: Set IPFS_PATH to trick curl into using the symlinked 'gateway' path for resolution.

**Command** ([[commands/export-ipfs-path]]):
```bash
export IPFS_PATH="$EXPLOIT_DIR"
```

> Sets the variable for the current shell session. Expected output: None; verify with echo $IPFS_PATH.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[DLL Search Order Hijacking]] Hijack Execution Flow: Environment Variable Manipulation

### Sub-Techniques


## Commands Used

- [[commands/export-ipfs-path]]

## Tools Used

- [[tools/bash]]

## Tags

- [[environment-variable]]
- [[path-traversal]]
- [[hijack]]
