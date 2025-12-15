---
id: proc-005
tags:
  - rce
  - privilege-escalation
  - php
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[PowerShell]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:23:32.432Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[PowerShell]]'
  - '[[JavaScript]]'
---
# Chain XSS to WordPress RCE

## Summary

This procedure uses the XSS-loaded JavaScript to exploit same-origin policy, accessing the WordPress plugin editor to inject and execute arbitrary PHP code, achieving remote code execution on the server.

## Description

With admin privileges, the wp-rce.js script leverages the victim's authenticated session to iframe the plugin editor at /wp-admin/plugin-editor.php?file=hello.php. It manipulates the DOM to insert PHP code into the editor textarea and submits the form, saving the file. A subsequent redirect executes the injected code, such as phpinfo(), demonstrating full RCE.

## Requirements

1. XSS execution in admin browser context
2. Access to /wp-admin/plugin-editor.php (admin-only)
3. hello.php plugin exists or is editable

## Defense

Defensive measures and detection strategies:

- Disable plugin editor in wp-config.php (DISALLOW_FILE_EDIT)
- Restrict file edit capabilities to trusted roles only
- Audit server logs for unexpected PHP file modifications

## Objectives

1. Manipulate admin interface via JavaScript
2. Inject and save malicious PHP
3. Execute code on server

## Instructions

### Step 1: Load and Run wp-rce.js

**Context**: The external script auto-executes post-XSS.

**Command** (Script Execution):

Script content: create iframe to /wp-admin/plugin-editor.php?file=hello.php; setTimeout(2000, access contentWindow.document.getElementById('newcontent').value = '<?php phpinfo(); ?>'); simulate click on #submit; setTimeout(4000, window.location = '/wp-content/plugins/hello.php');

> Expected output: Iframe loads editor; file saves with PHP.

### Step 2: Verify RCE

**Context**: Redirect executes the injected code.

**Command** (Access Execution):

Navigate to: /wp-content/plugins/hello.php

> Expected output: PHP info page displays server details, confirming RCE.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Privilege Escalation]]

### Techniques

- [[PowerShell]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- rce
- privilege-escalation
- php
