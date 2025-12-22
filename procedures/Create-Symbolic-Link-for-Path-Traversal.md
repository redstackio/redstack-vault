---
id: proc-create-symlink-traversal
tags:
  - symlink
  - path-traversal
  - file-system
type: procedure
tools:
  - '[[tools/ln]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/ln-create-symlink]]'
verified: false
platforms:
  - Linux
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:17.648Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Create Symbolic Link for Path Traversal

## Summary

This procedure creates a symbolic link (symlink) pointing to parent directories using the Unix `ln` command, setting up the foundation for path traversal attacks in vulnerable file servers like simplehttpserver by allowing access to files outside the intended web root.

## Description

In the context of exploiting path traversal vulnerabilities, attackers create symlinks that reference paths like '../../' to escape the web root. When a vulnerable server serves the directory containing this symlink without proper validation, accessing the symlink via HTTP resolves to unintended locations, enabling directory listing and file access. This is particularly effective against simple HTTP servers that append URL paths directly to the root. Prerequisites include a Unix-like environment with symlink support and write access to the target directory.

## Requirements

1. Unix-like OS (Linux or macOS) with `ln` command available
2. Write permissions in the current working directory
3. No elevated privileges needed for basic symlink creation

## Defense

Defensive measures and detection strategies:

- Disable symlink following in server configurations (e.g., Apache's `Options -FollowSymLinks`)
- Use chroot jails or containerization to restrict file system access
- Monitor file system changes for unexpected symlink creations via tools like auditd or OSSEC
- Implement path normalization and canonicalization in custom servers to block traversal sequences

## Objectives

1. Establish a symlink that points outside the web root for traversal
2. Prepare the environment for server exploitation
3. Enable unauthorized file access upon server request

## Instructions

### Step 1: Create the Symlink

**Context**: This step generates a symlink named 'symdir' targeting two parent directories ('../../'), which will be used to traverse outside the web root when accessed via the vulnerable server.

**Command** ([[commands/ln-create-symlink]]):
```bash
ln -s ../../ symdir
```

> The `ln -s` command creates a symbolic link. The `-s` flag specifies a soft/symbolic link, '../../' is the target path for traversal, and 'symdir' is the link name. Expected output is silent on success; verify with `ls -la` to see the symlink arrow (`symdir -> ../../`). If permissions are insufficient, an error like 'Permission denied' appears.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used

- [[commands/ln-create-symlink]]

## Tools Used

- [[tools/ln]]

## Tags

- symlink
- path-traversal
