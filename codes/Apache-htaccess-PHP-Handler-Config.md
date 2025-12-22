---
id: c15bdc11-9bad-423d-9c67-2dfbf98e636e
name: Apache-htaccess-PHP-Handler-Config
type: code
language: apache
verified: true
created_at: '2023-04-06T03:56:40.869926+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Apache
tags:
  - htaccess
  - php
  - config
validated: true
---

# Apache-htaccess-PHP-Handler-Config

## Code

```apache
AddType application/x-httpd-php .rce
```

## Description

This .htaccess directive configures Apache to treat files with the .rce extension as PHP scripts, enabling execution of PHP code in uploaded .rce files. It exploits environments where .htaccess overrides are allowed and file uploads are weakly validated.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| .rce | Custom file extension to associate with PHP handler | .rce (can be changed to any non-standard extension) |

## Usage

Save this as .htaccess and upload to the web root via a vulnerable upload endpoint. Then upload a .rce file with PHP code and access it (e.g., http://target.com/shell.rce) to execute. Used in web RCE attacks when direct .php uploads are blocked.

## Detection

- Monitor web server access logs for .htaccess uploads or modifications.
- Scan .htaccess files for AddType directives with unusual extensions.
- WAF rules to block uploads containing 'AddType' or PHP-related config.
- File integrity monitoring alerting on changes to web root .htaccess.

## Related

- [[procedures/Configure-Apache-PHP-Handler-via-htaccess-for-RCE]]
