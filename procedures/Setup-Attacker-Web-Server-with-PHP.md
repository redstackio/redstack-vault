---
id: proc-setup-attacker-server-001
tags:
  - setup
  - web-server
  - php
type: procedure
tools:
  - '[[tools/nginx]]'
  - '[[tools/PHP]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:48.955Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup-Attacker-Web-Server-with-PHP

## Summary

This procedure configures a publicly accessible web server using nginx and PHP to host custom scripts that deliver slow or large responses, simulating malicious image endpoints for proxy exploitation in DoS attacks.

## Description

In the context of attacking asset proxies like Chaturbate's camo.stream.highwebmedia.com, an attacker needs a controlled server to serve PHP scripts mimicking slowloris-style responses or oversized chunked data. The server must support high timeout values to handle long-running requests without interruption. This setup enables embedding URLs in target sites, causing the proxy to fetch and get stuck on the responses, exhausting resources.

## Requirements

1. VPS or cloud instance with public IP and root access
2. nginx and PHP installed (e.g., PHP 7+ with FPM)
3. High timeout configuration (e.g., 1800s in nginx)
4. Firewall allowing ports 80/443

## Defense

Defensive measures and detection strategies:

- Monitor for unusual outbound connections from proxies to unknown IPs
- Implement rate limiting on asset proxies for external fetches
- Use WAF to block suspicious image endpoints with chunked encoding

## Objectives

1. Establish a reliable host for malicious PHP scripts
2. Ensure server can handle concurrent long-duration requests
3. Prepare for embedding in target White Label pages

## Instructions

### Step 1: Install and Configure nginx

**Context**: Set up nginx as the web server with extended timeouts to support slow responses.

No specific command; configure /etc/nginx/sites-available/default with proxy_read_timeout 1800s; and fastcgi_read_timeout 1800s for PHP-FPM.

> Restart nginx: sudo systemctl restart nginx. Expected output: Server starts without errors, accessible via curl http://attacker-ip.

### Step 2: Install and Verify PHP

**Context**: Enable PHP execution for script hosting.

No specific command; install via apt install php-fpm php-cli; test with echo '<?php phpinfo(); ?>' > /var/www/html/info.php.

> Access http://attacker-ip/info.php. Expected output: PHP info page loads, confirming execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/nginx]]
- [[tools/PHP]]

## Tags

- setup
- web-server
