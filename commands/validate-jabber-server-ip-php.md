---
id: cmd-validate-jabber-ip
data: >-
  $x = gethostbyname('0x7f000001'); $is_valid = filter_var($x,
  FILTER_VALIDATE_IP, FILTER_FLAG_IPV4) || filter_var($x, FILTER_VALIDATE_IP,
  FILTER_FLAG_IPV6); if((!$is_valid) || ($x =="127.0.0.1")){ print $x." is not
  valid"; }else{ print $x." is valid"; }
tags:
  - validation
  - mitigation
  - ssrf
type: command
output: 0x7f000001 is not valid
executor: php
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:18.797Z'
verified: false
validated: true
submitted: true
---
# validate-jabber-server-ip-php

## Command

```php
$x = gethostbyname('0x7f000001'); $is_valid = filter_var($x, FILTER_VALIDATE_IP, FILTER_FLAG_IPV4) || filter_var($x, FILTER_VALIDATE_IP, FILTER_FLAG_IPV6); if((!$is_valid) || ($x =="127.0.0.1")){ print $x." is not valid"; }else{ print $x." is valid"; }
```

## Description

This PHP snippet resolves a hostname or IP (e.g., hex-encoded localhost like '0x7f000001') using gethostbyname, validates it as IPv4 or IPv6 with filter_var, and blocks localhost (127.0.0.1) to mitigate SSRF in inputs like phpBB's Jabber server field. Use it server-side to sanitize user inputs before connection attempts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| gethostbyname | Resolves input to IP address | Yes |
| filter_var (FILTER_VALIDATE_IP, FILTER_FLAG_IPV4/IPv6) | Checks if resolved value is valid IP | Yes |
| $x == '127.0.0.1' | Explicit block for localhost | Yes |

## Examples

### Basic Usage

```php
$x = gethostbyname('0x7f000001'); $is_valid = filter_var($x, FILTER_VALIDATE_IP, FILTER_FLAG_IPV4) || filter_var($x, FILTER_VALIDATE_IP, FILTER_FLAG_IPV6); if((!$is_valid) || ($x =="127.0.0.1")){ print $x." is not valid"; }else{ print $x." is valid"; }
```

### Advanced Usage

Adapt for form input: Replace '0x7f000001' with $_POST['jabber_server'], and integrate into phpBB's settings handler to reject invalid inputs before connection.

```php
$input = $_POST['jabber_server']; $x = gethostbyname($input); // ... rest as above
```

## Expected Output

For localhost variants: '0x7f000001 is not valid'. For external valid IPs: 'example.ip is valid'.

## Related

- [[Related Procedure]]
