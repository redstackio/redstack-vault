---
id: proc-php-redirect-unencoded
tags:
  - xss
  - redirect-bypass
type: procedure
tools:
  - '[[tools/PHP]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/php-redirect-script]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:20.808Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-PHP-Redirect-for-Unencoded-URLs

## Summary

This procedure creates a simple PHP script to perform a 302 redirect without encoding the target URL, allowing injection of HTML tags into paths that browsers would otherwise encode, specifically for exploiting unencoded inputs in web error pages like Twitter's 404.

## Description

In scenarios where client-side URL encoding prevents HTML injection, a server-side redirect can bypass this by issuing an unencoded Location header. This is used here to target sms-be-vip.twitter.com's 404 page, which reflects the path without sanitization. Prerequisites include a PHP-enabled web server for hosting the script. Expected outcome: Successful redirect to vulnerable endpoint with raw HTML in path.

## Requirements

1. PHP-enabled web hosting (e.g., Apache with PHP module)
2. Write access to host the script file
3. Basic knowledge of URL parameters

## Defense

Defensive measures and detection strategies:

- Encode all Location headers in redirects
- Sanitize URL paths in error pages
- Monitor for anomalous 302 redirects from external domains

## Objectives

1. Bypass client-side URL encoding for injection
2. Enable HTML/JS delivery to vulnerable endpoints
3. Set up for subsequent padding and POC testing

## Instructions

### Step 1: Write the PHP Script

**Context**: Create the redirect handler that takes a URL parameter and issues an unencoded redirect.

**Command** ([[commands/php-redirect-script]]):
```php
<?php $url=$_GET['x']; header("Location: $url"); ?>
```

> This script reads the 'x' GET parameter as the redirect URL and sends a 302 without modifications. Save as `redir.php` on your server. Expected output: No visible output; browser follows the redirect.

### Step 2: Host and Test the Script

**Context**: Upload and verify the script responds to requests.

**Command** (Browser access):
```url
http://yourserver.com/redir.php?x=https://example.com
```

> Access the script with a test URL. Expected output: Immediate redirect to example.com without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/php-redirect-script]]

## Tools Used

- [[tools/PHP]]

## Tags

- xss
- redirect-bypass
