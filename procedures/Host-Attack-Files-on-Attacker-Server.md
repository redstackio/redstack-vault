---
tags:
  - hosting
  - php-server
  - ssrf
type: procedure
tools:
  - '[[tools/PHP-Built-in-Server]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/php-built-in-server-host]]'
platforms:
  - Linux
  - Web
techniques:
  - '[[Remote File Copy]]'
skill_level: beginner
impact_level: low
detection_risk: medium
sub_techniques: []
id: 16431a99-e43c-4d98-851b-772975f29142
created_at: '2025-12-14T04:08:55.344Z'
updated_at: '2025-12-14T04:08:55.344Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Host-Attack-Files-on-Attacker-Server

## Summary

This procedure sets up a simple HTTP server on an attacker-controlled machine to host the SSRF exploitation files (stealer.php and PoC.html), enabling the vulnerable service to fetch and execute them.

## Description

To facilitate the SSRF attack on Lemlist's API, the attacker hosts the prepared files using PHP's built-in server, binding to all interfaces on port 80 for public accessibility. This allows the service to redirect to localhost via the attacker's domain. The environment assumes PHP is installed, and the server runs locally or on a VPS. Expected outcome is a publicly reachable URL for the files.

## Requirements

1. PHP 7+ installed on the attacker machine
2. Prepared stealer.php and PoC.html files in a directory
3. Firewall allowing inbound traffic on port 80

## Defense

Defensive measures and detection strategies:

- Block or monitor sudden PHP development servers in environments
- Use WAF to detect anomalous hosting patterns
- Scan for exposed development servers on public IPs

## Objectives

1. Make exploitation files accessible via HTTP
2. Ensure binding to all interfaces for remote access
3. Verify file serving without errors

## Instructions

### Step 1: Place Files and Start Server

**Context**: Position the files in the server root and launch the PHP server to host them.

**Command** ([[commands/php-built-in-server-host]]):
```bash
php -S 0.0.0.0:80
```

> This starts the PHP development server on all interfaces (0.0.0.0) listening on port 80. Expected output: 'PHP 7.x.x Development Server (http://0.0.0.0:80) started'. Access http://[attacker-ip]/stealer.php to confirm redirection to PoC.html.

### Step 2: Verify Hosting

**Context**: Test that files are served correctly and accessible remotely.

Use a browser or curl to hit the endpoints:

```bash
curl http://[attacker-ip]/stealer.php
```

> Should return a 301 redirect header. Success if files load and redirect works.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used

- [[commands/php-built-in-server-host]]

## Tools Used

- [[tools/PHP-Built-in-Server]]

## Tags

- hosting
- server-setup
