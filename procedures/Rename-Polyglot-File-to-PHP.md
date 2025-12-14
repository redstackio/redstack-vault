---
id: proc-uuid-polyglot-rename-001
tags:
  - file-rename
  - extension-bypass
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Linux
  - Windows
  - macOS
submitted: true
created_at: '2024-10-05T12:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T05:32:10.156Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Rename-Polyglot-File-to-PHP

## Summary

This simple procedure renames the polyglot JPEG-PHP file to a .php extension, preparing it for upload while relying on the file's dual nature to bypass extension-based checks.

## Description

Renaming disguises the file as a PHP script for potential execution post-upload, though in Nextcloud, the server renames it to 'avatar_upload'. This step is crucial if future configurations or bypasses allow direct PHP serving. The rename does not alter the file content, preserving its JPEG validity.

## Requirements

1. Local file system access to the polyglot file
2. Basic file management capabilities

## Defense

Defensive measures and detection strategies:

- Server-side always rename uploads to safe extensions (e.g., .jpg) and store outside web root
- Scan for polyglot files during upload by checking for multiple valid parses (image and script)
- Audit file naming patterns in logs

## Objectives

1. Change extension to .php without corrupting content
2. Maintain MIME type as image/jpeg for bypass
3. Prepare for upload

## Instructions

### Step 1: Locate File

**Context**: Ensure the polyglot file is ready.

Navigate to the directory containing `image1.jpg`.

### Step 2: Perform Rename

**Context**: Update the extension to enable PHP interpretation if executed.

Use file explorer to rename `image1.jpg` to `image1.php`, or via command line:

```bash
mv image1.jpg image1.php
```

**Expected Output**: File now named `image1.php`.

### Step 3: Verify Integrity

**Context**: Confirm no changes to content.

Check MIME type with `file image1.php` (should still show JPEG) and open in image viewer.

**Expected Output**: File remains valid as image.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- file-rename
- extension-bypass
