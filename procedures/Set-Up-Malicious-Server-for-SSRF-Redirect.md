---
tags:
  - ssrf
  - malicious-server
  - php-redirect
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/php-redirect-script-for-ssrf]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Service Scanning]]'
updated_at: '2025-12-14T04:08:46.186Z'
sub_techniques: []
id: 2237c851-9fa1-4b07-a079-78e46b91014c
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
---
# Set-Up-Malicious-Server-for-SSRF-Redirect

## Summary

This procedure sets up an attacker-controlled HTTP server to receive Phabricator's status request and redirect it via SSRF to internal or external targets, facilitating reconnaissance or exfiltration.

## Description

Phabricator sends a GET /status to the configured admin server. The malicious server, implemented with PHP, responds with a 302 redirect to arbitrary URLs (e.g., internal metadata endpoints). This allows scanning open ports, retrieving service versions, or accessing restricted resources, though scoped to admin capabilities.

## Requirements

1. Server hosting capability (e.g., VPS with PHP support)
2. Port 22281 open and accessible from Phabricator
3. Target redirect URLs prepared (internal like http://169.254.169.254/ or custom)

## Defense

Defensive measures and detection strategies:

- Block outbound connections from Phabricator to untrusted hosts
- Monitor HTTP redirects in application logs
- Use network segmentation to isolate internal resources

## Objectives

1. Receive and log Phabricator's incoming request
2. Issue redirect to exploit SSRF
3. Observe Phabricator following the redirect for impact

## Instructions

### Step 1: Deploy PHP Script on Server

**Context**: Create the redirect handler at /status.

Use [[commands/php-redirect-script-for-ssrf]] to set up index.php:

```php
<?php
header("Location: http://anywhere.loc/bad_intentions");
?>
```

> Explanation: This script issues an HTTP redirect; customize Location for specific targets. Expected output: 302 response on access.

### Step 2: Start HTTP Server and Monitor

**Context**: Listen on the configured port for Phabricator's connection.

Run a PHP development server: php -S X.X.X.X:22281

> Expected output: Server logs show GET /status from Phabricator IP, followed by redirect execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Network Service Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/php-redirect-script-for-ssrf]]

## Tools Used


## Tags

- [[ssrf]]
- [[malicious-server]]
- [[php-redirect]]
