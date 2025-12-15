---
tags:
  - rce
  - php
  - execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/redirect-to-plugin-file]]'
platforms:
  - Web
techniques:
  - '[[PowerShell]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 2a1af1e6-91d0-481b-a64c-3aa8db69e983
created_at: '2025-12-14T17:23:20.675Z'
updated_at: '2025-12-14T17:23:20.675Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[PowerShell]]'
---
# Execute-Injected-PHP-for-RCE

## Summary

This procedure redirects the browser to the modified plugin file, triggering server-side execution of the injected PHP code to achieve remote code execution.

## Description

After injection, a delayed redirect to `/wp-content/plugins/hello.php` forces the server to parse and run the PHP, demonstrating RCE with outputs like phpinfo(). This compromises the site fully, as the code runs with web server privileges. In WordPress 4.8.1, direct access to plugin files is unrestricted.

## Requirements

1. PHP code successfully injected into hello.php
2. Web server executing PHP (e.g., Apache with mod_php)
3. Direct URL access to wp-content/plugins

## Defense

Defensive measures and detection strategies:

- Restrict plugin file access: Use .htaccess to block direct execution
- File integrity monitoring: Alert on changes to plugin files
- WAF rules: Block suspicious redirects or PHP injections

## Objectives

1. Trigger server-side code execution
2. Verify RCE with diagnostic output
3. Enable further site compromise

## Instructions

### Step 1: Delay and Redirect

**Context**: Wait for save to complete before execution.

Use setTimeout for 2000ms, then execute [[commands/redirect-to-plugin-file]]:

```javascript
window.location.href = "http://127.0.0.1:8090/wp-content/plugins/hello.php";
```

> Browser navigates to the file, server executes PHP.

### Step 2: Validate Execution

**Context**: Observe output to confirm RCE.

Check for phpinfo() page with server details.

> Detailed PHP configuration and environment variables displayed.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[PowerShell]]

### Sub-Techniques


## Commands Used

- [[commands/redirect-to-plugin-file]]

## Tools Used


## Tags

- [[redirect]]
- [[server-execution]]
