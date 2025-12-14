---
tags:
  - wordpress
  - theme-editor
type: procedure
tools:
  - '[[tools/Google-Chrome]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:12.637Z'
sub_techniques: []
id: 5827f676-7a0b-4eb4-af22-d7b7943ff56e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Select-Theme-File-for-Editing

## Summary

This procedure involves selecting a PHP file in the WordPress theme editor that lacks a predefined template name, ensuring clean injection of the XSS payload without conflicts.

## Description

The theme editor displays files from the active theme. Files like back-compat.php are ideal as they do not have existing Template Name comments, avoiding display issues. This step sets up the environment for payload insertion, targeting the get_file_description() function's output.

## Requirements

1. Access to the theme editor interface
2. Active WordPress theme with editable PHP files
3. Browser capable of handling form interactions

## Defense

Defensive measures and detection strategies:

- Disable theme editor in production via wp-config.php (DISALLOW_FILE_EDIT)
- Audit theme file access logs for unusual selections

## Objectives

1. Identify and load a suitable file for modification
2. Display file content in the editor
3. Avoid files with conflicting template metadata

## Instructions

### Step 1: Choose File from List

**Context**: Select a non-conflicting PHP file to edit.

From the file dropdown or list, select back-compat.php.

> The file's PHP code loads into the textarea editor.

### Step 2: Verify File State

**Context**: Ensure the file is ready for editing without errors.

Check for any existing comments; if clean, proceed.

> No output; visual confirmation in the editor.

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
- theme-editor
