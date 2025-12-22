---
id: proc-copy-to-local-directory
tags:
  - blacklist-bypass
  - storage-copy
  - rce-setup
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Upload Malware]]'
updated_at: '2025-12-14T17:23:24.869Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Upload Malware]]'
---
# Copy-Shared-Folder-to-Local-Data-Directory

## Summary

This procedure copies the contents of the federated shared folder to the local data directory on the target, exploiting the lack of blacklist checks in Storage::copyFromStorage for folder contents.

## Description

The core flaw is in lib/private/Files/Storage.php where copyFromStorage skips validating blacklisted files within folders from external sources. This places .htaccess and PHP files locally, bypassing protections.

## Requirements

1. Accepted federated share on target
2. Authenticated user on target
3. File manager access

## Defense

Defensive measures and detection strategies:

- Patch the copyFromStorage function to validate all files
- Audit copy operations from external storage
- Use external storage mounts with read-only or filtered access

## Objectives

1. Transfer malicious files locally
2. Bypass .htaccess blacklist
3. Position files for web execution

## Instructions

### Step 1: Select and Copy Folder

**Context**: Use file manager to initiate copy.

Navigate to shared 'sharefolder/attack', select, and choose 'Copy to' /files/attack/.

> Expected output: Copy progress completes.

### Step 2: Confirm Local Placement

**Context**: Verify files in local dir.

Browse /files/attack/; .htaccess and attack.php should be present.

> Expected output: Local files match shared contents.

### Step 3: Check Permissions

**Context**: Ensure web server can read files.

Default permissions allow; test access to dir via browser (should 403 PHP initially).

> Expected output: Dir accessible but PHP blocked until .htaccess applies.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Upload Malware]] Dynamic Library Injection

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- storage-copy
- bypass
