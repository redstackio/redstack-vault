---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - wordpress
  - filesystem-modification
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-05T00:00:00Z'
techniques:
  - '[[Data Destruction]]'
updated_at: '2025-12-13T23:55:20.329Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Data Destruction]]'
---
# Break-Theme-by-Deleting-Style-CSS

## Summary

This procedure corrupts an uploaded WordPress theme by removing its required style.css file, causing WordPress to detect it as broken and display its folder name unsanitized on the themes page.

## Description

WordPress themes require a style.css file with specific headers for validation. Deleting this file via filesystem access makes the theme malformed, triggering error messages on the admin themes page that reflect the folder name without HTML encoding, enabling stored XSS. This assumes server-level access beyond the admin UI.

## Requirements

1. Filesystem write access to wp-content/themes/ (e.g., via FTP, SSH, or cPanel)
2. Knowledge of the uploaded theme's folder name
3. WordPress installation without immutable filesystem protections

## Defense

Defensive measures and detection strategies:

- Implement filesystem integrity monitoring (e.g., via WordPress security plugins like Wordfence)
- Restrict direct filesystem access for hosting environments
- Log and alert on deletions in themes directory

## Objectives

1. Invalidate the theme to invoke broken theme display logic
2. Set up for payload reflection in admin UI
3. Maintain stealth by avoiding full theme deletion

## Instructions

### Step 1: Locate Theme Folder

**Context**: Identify the path of the uploaded theme.

Navigate to wp-content/themes/ and find the folder (e.g., /wp-content/themes/test-theme/).

### Step 2: Delete style.css

**Context**: Remove the validation file to break the theme.

Using file manager or command line, delete style.css from the folder.

> WordPress will now flag the theme as broken on Appearance > Themes.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Data Destruction]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- wordpress
- filesystem-modification
