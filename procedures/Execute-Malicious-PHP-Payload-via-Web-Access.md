---
id: proc-execute-php-payload
tags:
  - rce
  - php-execution
  - web-access
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
updated_at: '2025-12-14T17:23:24.867Z'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
---
# Execute-Malicious-PHP-Payload-via-Web-Access

## Summary

This final procedure triggers the RCE by directly accessing the copied PHP file via the web URL, where the .htaccess now permits execution in the data directory.

## Description

With files local and .htaccess overriding defaults, browsing to the PHP file executes the payload, allowing arbitrary command execution on the server.

## Requirements

1. Malicious files copied to local data dir
2. Web access to target instance
3. Knowledge of data dir path (e.g., /data/userid/files/)

## Defense

Defensive measures and detection strategies:

- Block PHP execution in data dirs via .htaccess and mod_php config
- WAF rules to detect suspicious PHP access in non-web dirs
- Monitor access logs for direct file hits in data paths

## Objectives

1. Achieve RCE via web request
2. Confirm payload execution
3. Demonstrate full compromise

## Instructions

### Step 1: Construct URL

**Context**: Build direct access URL to PHP file.

Use format: http://target/data/userid/files/attack/attack.php?cmd=<command>

> Replace userid and command (e.g., ?cmd=id).

### Step 2: Access in Browser

**Context**: Trigger execution.

Enter URL in browser or use curl for testing.

> Expected output: Command output displayed (e.g., uid=33(www-data)).

### Step 3: Validate RCE

**Context**: Test with escalating commands.

Try ?cmd=whoami or ?cmd=cat /etc/passwd.

> Expected output: Sensitive info or shell access confirmed.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Python]] PHP

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- rce-execution
