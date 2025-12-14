---
id: proc-uuid-003
tags:
  - symlink
  - linux
type: procedure
tools:
  - '[[tools/ln]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/ln-create-symlink-passwd]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Bypass User Account Control]]'
updated_at: '2025-12-14T17:26:17.381Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Bypass User Account Control]]'
---
# Create-Symlink-to-Sensitive-File

## Summary

This procedure creates a symbolic link to a sensitive system file like /etc/passwd within the server's directory, setting up the path traversal exploit.

## Description

Symbolic links allow bypassing directory restrictions in vulnerable servers. On Linux, 'ln -s' creates the link, which the statics-server will follow without checks, enabling arbitrary reads.

## Requirements

1. Write access to the server directory
2. Read access to target file (/etc/passwd)
3. ln command available (standard on Linux)

## Defense

Defensive measures and detection strategies:

- Disable symlink creation in served directories
- Use nofollow_symlinks in server configs
- Monitor filesystem for unexpected symlinks

## Objectives

1. Bridge served directory to sensitive files
2. Prepare for HTTP-based exploitation
3. Demonstrate symlink abuse

## Instructions

### Step 1: Create the Symlink

**Context**: Link /etc/passwd to a file name servable by the server.

**Command** ([[commands/ln-create-symlink-passwd]]):
```bash
ln -s /etc/passwd passwdsym
```

> Creates 'passwdsym' pointing to /etc/passwd. No output on success.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Bypass User Account Control]] Bypass User Account Control (symlink abuse context)

### Sub-Techniques


## Commands Used

- [[commands/ln-create-symlink-passwd]]

## Tools Used

- [[tools/ln]]

## Tags

- symlink
- linux
