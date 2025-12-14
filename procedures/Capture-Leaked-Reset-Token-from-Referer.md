---
tags:
  - token-capture
  - log-parsing
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:25:12.908Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 27c5f226-c831-4f2e-a458-3a3041595142
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Capture-Leaked-Reset-Token-from-Referer

## Summary

This procedure involves monitoring and extracting the password reset token from the referer header logged on an external server after a cross-domain request from the vulnerable reset page.

## Description

Once the user navigates to the external site, the HTTP request includes a referer header like `Referer: https://hackerone.com/users/password/edit?reset_password_token=HERE_IS_THE_VALUE_OF_RESET_PASSWORD_TOKEN`. The attacker, controlling the external site, reviews access logs (e.g., Apache/Nginx logs) to parse the URL and isolate the token value. This step assumes basic server logging is enabled. The token can then be used immediately if not expired.

## Requirements

1. Control over external web server with logging enabled
2. Recent cross-domain request from the target reset page
3. Tools for log parsing (e.g., grep, awk)

## Defense

Defensive measures and detection strategies:

- Disable or sanitize referer logging on public-facing servers
- Implement WAF rules to block or anonymize sensitive referers
- Use SIEM to detect patterns of referer leaks to external domains

## Objectives

1. Identify the incoming request with leaked referer
2. Extract the token parameter value
3. Validate token format for use in next steps

## Instructions

### Step 1: Review Server Logs

**Context**: Access the web server's access log file.

No specific command; tail the log file (e.g., `tail -f /var/log/nginx/access.log`).

> Expected: Entry showing GET to external path with referer header containing the reset URL.

### Step 2: Parse and Extract Token

**Context**: Use text processing to isolate the token.

Example using grep and sed:

```bash
grep "hackerone.com/users/password/edit" /var/log/nginx/access.log | sed 's/.*reset_password_token=\([^&]*\).*/\1/'
```

> Expected: Output of the token string, e.g., `HERE_IS_THE_VALUE_OF_RESET_PASSWORD_TOKEN`.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[token-extraction]]
- [[referer-log]]
