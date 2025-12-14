---
id: proc-upload-php-nextcloud
tags:
  - file-upload
  - rce
  - nextcloud
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
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T03:16:02.599Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-Malicious-PHP-Script-to-Nextcloud

## Summary

This procedure uploads a malicious PHP script through Nextcloud's file interface, storing it in the web-accessible data directory for later direct execution.

## Description

Nextcloud's file upload feature, when combined with a misconfigured data directory inside the web root, allows attackers to place executable PHP files in predictable paths like /data/<username>/files/. The procedure involves creating a simple PHP webshell and uploading it via the authenticated session. This sets up the conditions for RCE without additional validation, assuming default configurations on Apache/Debian setups.

## Requirements

1. Authenticated Nextcloud session with upload permissions
2. Malicious PHP payload (e.g., shell.php with system() function)
3. Access to the Files app in Nextcloud

## Defense

Defensive measures and detection strategies:

- Restrict file uploads to non-executable MIME types and scan for malicious content
- Place data directory outside web root and enable .htaccess with 'deny from all'
- Implement file execution prevention via mod_security or similar

## Objectives

1. Place executable code in the data directory
2. Ensure predictable URL path for direct access
3. Enable subsequent RCE without authentication

## Instructions

### Step 1: Prepare Malicious File

**Context**: Create the PHP script containing the payload for RCE.

In a text editor, write: <?php system($_GET['cmd']); ?>

> Save as shell.php.

### Step 2: Upload via Files Interface

**Context**: Use Nextcloud's upload feature to store the file.

In the Files app, click 'Upload' and select shell.php. It will be placed at /data/attacker/files/shell.php.

> Confirm upload success in the file list.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- file-upload
- rce
- nextcloud
