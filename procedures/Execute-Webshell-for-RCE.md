---
id: proc-005
tags:
  - rce
  - webshell
  - php
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/php-webshell-execute]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Python]]'
updated_at: '2025-12-14T17:23:33.051Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
---
# Execute-Webshell-for-RCE

## Summary

This procedure accesses the deployed PHP webshell to execute arbitrary system commands on the ownCloud server, confirming RCE and enabling post-exploitation.

## Description

After deserialization writes the webshell to `/tmp/pwned.php`, it can be accessed via HTTP GET with the `exec` parameter to run system commands through PHP's `system()` function. This provides full server control, assuming the web server has execution permissions on `/tmp`. The payload includes a comment for attribution.

## Requirements

1. Webshell file created at `/tmp/pwned.php`
2. Web server access to the `/tmp` directory
3. Knowledge of target commands (e.g., `id`, `ls`)

## Defense

Defensive measures and detection strategies:

- Restrict web server write/execute permissions on temporary directories
- Scan for anomalous PHP files in `/tmp`
- Monitor HTTP requests for suspicious parameters like `exec`

## Objectives

1. Verify webshell deployment
2. Execute arbitrary commands remotely
3. Escalate to full server compromise

## Instructions

### Step 1: Access Webshell

**Context**: Navigate to the webshell URL to test execution.

Use browser or curl to access `http://target/tmp/pwned.php?exec=id`.

> Output shows user ID, confirming execution.

### Step 2: Run Arbitrary Commands

**Context**: Use the webshell for post-exploitation.

Execute [[commands/php-webshell-execute]] by appending commands to the URL, e.g., `?exec=whoami`.

> Command output displayed in response body.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Python]] PHP

### Sub-Techniques


## Commands Used

- [[commands/php-webshell-execute]]

## Tools Used


## Tags

- [[rce]]
- [[webshell]]
- [[php]]
