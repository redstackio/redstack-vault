---
tags:
  - wordpress
  - file-update
type: procedure
tools:
  - '[[tools/Google-Chrome]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:12.631Z'
sub_techniques: []
id: 918d6eba-2871-42cb-9942-3584121da551
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Update-WordPress-Theme-File

## Summary

This procedure saves the modified PHP file containing the XSS payload, storing it on the server for persistent exploitation.

## Description

After injecting the payload, the Update File button submits the changes via POST to wp-admin/theme-editor.php, updating the theme directory file. This stores the malicious comment, which will be reflected unescaped on subsequent loads.

## Requirements

1. Modified file content in editor
2. Permissions to write to theme files
3. Stable connection to avoid partial saves

## Defense

Defensive measures and detection strategies:

- Implement file integrity monitoring for theme directories
- Log all file updates in wp-admin and alert on suspicious changes

## Objectives

1. Persist the injected payload
2. Confirm successful save
3. Prepare for triggering

## Instructions

### Step 1: Submit Update

**Context**: Save changes to the server.

Click the 'Update File' button at the bottom of the editor.

> A success message like 'File updated' appears, and the file list refreshes.

### Step 2: Verify Persistence

**Context**: Reload the file to check if changes stuck.

Select the file again; payload should still be in the content.

> Content reloads with the comment intact.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Chrome]]

## Tags

- wordpress
- file-update
