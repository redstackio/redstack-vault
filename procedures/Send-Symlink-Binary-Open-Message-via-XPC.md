---
tags:
  - xpc
  - symlink
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:30:07.321Z'
sub_techniques: []
id: a635aee9-0751-46ef-bf73-c9284fb3eb5c
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Send Symlink Binary Open Message via XPC

## Summary

This procedure sends a crafted XPC message to the privileged NordVPN helper to request opening a binary via a symlink in a user-controlled directory, setting up for TOCTOU exploitation.

## Description

With an established XPC connection, the attacker instructs the helper to launch a binary from a controlled path like `/tmp/`, using a symlink to point to the legitimate NordVPN executable. The helper's resolution logic trusts the symlink during path validation, allowing manipulation. This exploits insufficient checks on user-writable directories.

## Requirements

1. Active XPC connection from prior procedure.
2. Write access to a temporary directory (e.g., `/tmp/`).
3. Symlink creation permissions.

## Defense

Defensive measures and detection strategies:

- Harden helper processes to only accept paths in trusted directories.
- Use file system monitoring (e.g., `fseventsd`) to detect rapid symlink changes in app-related paths.
- Audit XPC messages for suspicious binary launch requests.

## Objectives

1. Dispatch open request for symlink-targeted binary.
2. Ensure initial resolution to legitimate path.
3. Prepare for race condition exploitation.

## Instructions

### Step 1: Create Controlled Directory and Symlink

**Context**: Set up the symlink in a writable location pointing to the real binary.

Create directory and symlink:

```bash
mkdir -p /tmp/nord-controlled
ln -s /Applications/NordVPN.app/Contents/MacOS/NordVPN /tmp/nord-controlled/target
```

> Expected: Symlink resolves to legitimate binary when checked with `ls -l`.

### Step 2: Craft and Send XPC Message

**Context**: Build payload requesting launch of `/tmp/nord-controlled/target`.

Use XPC API to encode the message with the path key and send via the connection. Include necessary plist or dictionary for the open action.

> Expected: Helper receives and begins symlink resolution process.

### Step 3: Monitor Resolution

**Context**: Verify the helper attempts to open the path.

Trace with `sudo fs_usage | grep Nord` to see file access attempts.

> Expected: Logs show resolution of symlink to legitimate path.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[xpc]]
- [[symlink]]
