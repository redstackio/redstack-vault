---
id: uuid-host-redirect
tags:
  - ssrf
  - php
  - redirect
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/php-redirect-to-aws-metadata]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T03:53:38.743Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Host-Redirecting-PHP-File-for-Bypass

## Summary

This procedure creates and hosts a PHP file that redirects HTTPS requests to the internal AWS EC2 metadata HTTP endpoint, bypassing the readapi variable's HTTPS restriction.

## Description

A simple PHP script with a Location header redirect targets http://169.254.169.254/latest/meta-data/. Hosted on an attacker-controlled HTTPS domain, it tricks the backend into following to internal resources. Used in SSRF attacks against services like Streamlabs Cloudbot.

## Requirements

1. PHP-enabled web server (e.g., Apache)
2. Attacker domain with HTTPS (SSL certificate)
3. File upload access to server

## Defense

Defensive measures and detection strategies:

- Scan for suspicious redirects in hosted content
- Block requests to link-local IPs (169.254.x.x) in WAF
- Audit external content fetches for redirect chains

## Objectives

1. Create redirect to AWS metadata
2. Host on HTTPS for compatibility
3. Enable SSRF trigger

## Instructions

### Step 1: Create PHP File

**Context**: Write the redirect script.

Use [[commands/php-redirect-to-aws-metadata]] to generate slpoc.php:

```php
<?php header('Location: http://169.254.169.254/latest/meta-data/'); ?>
```

> Expected: File created with 302 redirect capability.

### Step 2: Host the File

**Context**: Upload and serve via HTTPS.

Upload slpoc.php to server and access https://mydomain/slpoc.php.

> Expected: Browser or curl shows redirect to metadata URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used

- [[commands/php-redirect-to-aws-metadata]]

## Tools Used


## Tags

- [[ssrf]]
- [[php]]
- [[redirect]]
