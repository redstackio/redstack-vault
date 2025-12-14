---
tags:
  - gitlab-import
  - file-leak
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-25T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:08.375Z'
sub_techniques: []
id: 22cd924b-c979-4eb7-b0a5-f080084d5220
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upload-Malicious-Export-for-Partial-File-Read

## Summary

This procedure uploads a symlink-modified GitLab export to trigger partial arbitrary file read via the VERSION file check during import.

## Description

Targeting GitLab's project creation import interface, the modified tar.gz is uploaded, causing the VersionChecker to dereference the symlink and read the first line with readline(), which appears in the error message due to exception handling. The scenario assumes attacker access to import functionality. Outcomes: Exposure of partial sensitive data like usernames from /etc/passwd.

## Requirements

1. Modified export with VERSION symlink
2. GitLab account with import permissions
3. Web browser access to GitLab

## Defense

Defensive measures and detection strategies:

- Sanitize inputs in import process to prevent symlink following
- Rate-limit import attempts
- Audit error logs for leaked content

## Objectives

1. Trigger VERSION validation to leak first line
2. Confirm partial read capability
3. Gather initial intel from sensitive files

## Instructions

### Step 1: Access Import Interface

**Context**: Prepare for upload.

Go to https://gitlab.example.com/projects/new, select "Import project" > "GitLab export".

### Step 2: Upload Archive

**Context**: Submit the malicious tar.gz.

Upload test.tar.gz and initiate import.

**Expected Output**: Version mismatch error displaying first line of symlinked file (e.g., "root:x:0:0:root:/root:/bin/bash").

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[gitlab-import]]
- [[file-leak]]
