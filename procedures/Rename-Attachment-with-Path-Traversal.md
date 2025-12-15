---
tags:
  - path-traversal
  - filename-manipulation
  - android
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:24:42.975Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: f9c7d2dd-ddf1-4987-a6f6-69c642e140f7
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Rename-Attachment-with-Path-Traversal

## Summary

This procedure renames an uploaded attachment in an Evernote note using path traversal sequences to direct the download to a sensitive app directory, exploiting lack of sanitization.

## Description

The Evernote Android app allows renaming attachments without validating for traversal characters. By setting the name to `../../../lib-1/libjnigraphics`, the filename extracted from the Content-Disposition header during download bypasses the intended cache path (`/data/data/com.evernote/cache/preview/:UUID/`) and writes to `/data/data/com.evernote/lib-1/`. The `.so` extension is preserved internally despite omission in the rename.

## Requirements

1. Attached malicious library in an Evernote note
2. Evernote Android app (vulnerable version)
3. Knowledge of target directory structure (`lib-1` for native libs)

## Defense

Defensive measures and detection strategies:

- Sanitize filenames by removing `../` and absolute paths in Content-Disposition handling
- Use secure file paths with whitelisting in React Native code
- Log and alert on attachment renames with suspicious characters

## Objectives

1. Embed traversal payload in filename for directory escape
2. Target specific sensitive path for library overwrite
3. Preserve file extension for native loading

## Instructions

### Step 1: Access Attachment Rename

**Context**: Open the note containing the attachment and initiate rename.

In the Evernote note editor, long-press or tap the attachment and select rename option.

### Step 2: Set Traversal Filename

**Context**: Input the crafted name to exploit the download logic.

Enter `../../../lib-1/libjnigraphics` as the new name. Confirm the change.

> The app accepts the input without validation; the full path `../../../lib-1/libjnigraphics.so` is used in the header during download.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- path-traversal
- android
- evernote
