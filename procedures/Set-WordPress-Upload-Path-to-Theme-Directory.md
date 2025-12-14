---
id: p3c4d5e6-f7g8-9012-cdef-3456789012
tags:
  - wordpress
  - file-upload
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:47.348Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Set-WordPress-Upload-Path-to-Theme-Directory

## Summary

This procedure updates the upload_path option to target the theme directory after permissions have been escalated, allowing subsequent uploads to sensitive locations.

## Description

With directories now writable due to prior chmod, setting upload_path to 'wp-content/themes/current-theme/' redirects media uploads directly to the theme folder. WordPress does not validate this path against protected areas, enabling placement of files in executable contexts.

## Requirements

1. Permissions escalated from previous step
2. Admin access to options.php
3. Known theme directory path

## Defense

Defensive measures and detection strategies:

- Lock down upload_path to default via code or plugins
- Audit option changes in wp_options table
- Use file permissions to prevent theme writes

## Objectives

1. Redirect uploads to executable directory
2. Prepare for malicious file placement
3. Exploit writability without further traversals

## Instructions

### Step 1: Access Options Page

**Context**: Re-enter the admin options to modify the path.

Navigate to wp-admin/options.php.

### Step 2: Set Theme Path

**Context**: Update to the writable theme location.

Enter 'wp-content/themes/current-theme/' in the upload_path field and save.

> Verify with get_option('upload_path') to confirm the change.

### Step 3: Test Redirection

**Context**: Ensure uploads now target the theme.

Attempt a small test upload to confirm file placement.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- wordpress
- file-upload
