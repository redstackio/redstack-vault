---
id: p4d5e6f7-g8h9-0123-defg-4567890123
tags:
  - wordpress
  - file-upload
  - php
  - shell
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
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:30:47.346Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-Malicious-PHP-Shell-to-WordPress-Theme

## Summary

This procedure uploads a PHP shell file via the media uploader to the theme directory, disguised as a text file, leveraging the modified upload_path for placement in an executable location.

## Description

WordPress media uploader places files based on upload_path without extension checks for PHP in this context. Uploading 'shell.txt' with '<?php phpinfo(); ?>' or webshell code results in a file that can be executed if included, as themes are parsed for PHP.

## Requirements

1. Upload_path set to theme directory
2. Writable theme permissions
3. Admin media upload access

## Defense

Defensive measures and detection strategies:

- Scan uploads for PHP signatures
- Disable PHP execution in upload directories via .htaccess
- Monitor file creations in themes via logs

## Objectives

1. Place executable code in theme
2. Bypass upload filters
3. Set up for inclusion-based execution

## Instructions

### Step 1: Prepare Shell File

**Context**: Create the malicious content.

Prepare a file named 'shell.txt' with content: '<?php phpinfo(); ?>' or full shell code.

### Step 2: Upload via Media

**Context**: Use the uploader to place it in theme.

Go to Media > Add New and upload shell.txt.

> File saves as wp-content/themes/current-theme/shell.txt due to path.

### Step 3: Confirm Placement

**Context**: Verify the file is in place.

Check the theme directory listing or recent uploads in admin.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- wordpress
- file-upload
- php
- shell
