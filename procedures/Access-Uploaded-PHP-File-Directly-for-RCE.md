---
tags:
  - rce
  - php
  - misconfiguration
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Python]]'
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: eb4689eb-e47d-49cb-999b-abca1b6b81e2
created_at: '2025-12-14T17:23:24.048Z'
updated_at: '2025-12-14T17:23:24.048Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
  - '[[Exploit Public-Facing Application]]'
---
# Access-Uploaded-PHP-File-Directly-for-RCE

## Summary

This procedure directly accesses the uploaded PHP file via its URL, exploiting the data directory's web root placement to execute code and achieve RCE.

## Description

In misconfigured Nextcloud (data dir in /var/www/nextcloud/data), direct URLs like https://www.ournextclouddomain.com/data/attacker/files/shell.php execute PHP without .htaccess blocks. Requires prior upload; outcomes include arbitrary command execution if AllowOverride All is absent on Apache.

## Requirements

1. Uploaded PHP file in data directory
2. Knowledge of direct path (e.g., /data/<username>/files/shell.php)
3. Web browser or curl for access

## Defense

Defensive measures and detection strategies:

- Set Apache directive AllowOverride All in data directory config
- Use mod_security or similar to block direct script access
- Monitor web server access logs for unusual /data/ paths

## Objectives

1. Bypass Nextcloud's file viewer for direct execution
2. Trigger PHP interpreter on uploaded payload
3. Confirm RCE capability

## Instructions

### Step 1: Construct Direct URL

**Context**: Build the path to the uploaded file.

Determine the base domain and append /data/attacker/files/shell.php.

> Full URL: https://www.ournextclouddomain.com/data/attacker/files/shell.php

### Step 2: Navigate to URL

**Context**: Request the file to execute it.

Enter the URL in a browser or use curl -X GET "https://www.ournextclouddomain.com/data/attacker/files/shell.php?cmd=whoami".

> PHP executes; output like 'www-data' appears if successful.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Python]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[rce]]
- [[php]]
- [[misconfiguration]]
