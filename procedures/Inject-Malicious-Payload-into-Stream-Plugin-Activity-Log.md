---
tags:
  - xss
  - injection
  - wordpress
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-inject-xss-referer]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T00:11:09.221Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 293374df-b62f-4a4e-ab70-a87bf47c9238
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-Malicious-Payload-into-Stream-Plugin-Activity-Log

## Summary

This procedure exploits a lack of sanitization in the Stream WordPress plugin's activity logging for wp_redirect events, allowing unauthenticated attackers to inject HTML/JavaScript payloads via the 'file' query parameter in a crafted Referer header.

## Description

The Stream plugin (version 1.4.9) logs user activity from redirects, such as those triggered by plugin-editor.php, without properly escaping the 'file' parameter. By sending a POST request to wp-login.php with action=postpass and a malicious Referer header, the redirect logs the unsanitized payload into the database. This stored content is later displayed in the admin dashboard's Stream tab, enabling XSS execution when viewed by administrators. The attack requires no authentication and targets the connectors/installer.php file's logging mechanism.

## Requirements

1. Network access to the target WordPress site's wp-login.php endpoint
2. [[tools/curl]] installed for sending HTTP requests
3. Knowledge of the target URL (e.g., https://newsroom.uber.com)

## Defense

Defensive measures and detection strategies:

- Sanitize all logged parameters in plugins, especially query strings from redirects
- Implement Content Security Policy (CSP) to restrict inline JavaScript execution
- Monitor for anomalous Referer headers in access logs and unusual POST requests to wp-login.php

## Objectives

1. Store malicious JavaScript in the Stream plugin's database log
2. Prepare for admin-privileged execution upon dashboard view
3. Enable potential site takeover via JS-driven actions

## Instructions

### Step 1: Craft and Send Injection Request

**Context**: Simulate a redirect from plugin-editor.php by setting a Referer header with URL-encoded JavaScript in the 'file' parameter, triggering the log entry.

**Command** ([[commands/curl-inject-xss-referer]]):
```bash
curl -v -H 'Referer: /hello?plugin-editor.php&file=aaa%3cscript%3ealert(%27stored%20xss%27);%3c/script%3e' --data 'post-password=foo' 'https://newsroom.uber.com/wp-login.php?action=postpass'
```

> This command sends a verbose POST request with a dummy post-password to trigger the postpass action, logging the Referer payload. Expected output includes a 302 redirect and confirmation of the request in verbose mode; the payload is now stored unsanitized.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-inject-xss-referer]]

## Tools Used

- [[tools/curl]]

## Tags

- xss
- injection
- wordpress
