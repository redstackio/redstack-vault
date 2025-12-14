---
id: cmd-php-ip-validate-001
data: >-
  $x = gethostbyname('0x7f000001');

  $is_valid = filter_var($x, FILTER_VALIDATE_IP, FILTER_FLAG_IPV4) ||
  filter_var($x, FILTER_VALIDATE_IP, FILTER_FLAG_IPV6);


  if((!$is_valid) || ($x =="127.0.0.1")){
   print $x." is not valid";
  }else{
   print $x." is valid";
  }
tags:
  - mitigation
  - validation
  - ssrf-defense
type: command
output: 127.0.0.1 is not valid
executor: php
platforms:
  - PHP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:10.136Z'
verified: false
validated: true
submitted: true
---
# php-ip-validation-mitigation

## Command

```php
$x = gethostbyname('0x7f000001');
$is_valid = filter_var($x, FILTER_VALIDATE_IP, FILTER_FLAG_IPV4) || filter_var($x, FILTER_VALIDATE_IP, FILTER_FLAG_IPV6);

if((!$is_valid) || ($x =="127.0.0.1")){
 print $x." is not valid";
}else{
 print $x." is valid";
}
```

## Description

This PHP snippet resolves a hostname or IP (including hex representations like 0x7f000001 for 127.0.0.1) and validates it as a valid IPv4 or IPv6 address, explicitly blocking localhost (127.0.0.1) to mitigate SSRF attempts in applications like phpBB.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `gethostbyname` | Resolves input string to IP address | Yes |
| `filter_var` with `FILTER_VALIDATE_IP` | Checks if resolved IP is valid IPv4/IPv6 | Yes |
| Hardcoded check for `127.0.0.1` | Blocks localhost specifically | Yes |

## Examples

### Basic Usage

```php
$x = gethostbyname('0x7f000001');
$is_valid = filter_var($x, FILTER_VALIDATE_IP, FILTER_FLAG_IPV4) || filter_var($x, FILTER_VALIDATE_IP, FILTER_FLAG_IPV6);

if((!$is_valid) || ($x =="127.0.0.1")){
 print $x." is not valid";
}else{
 print $x." is valid";
}
```

### Advanced Usage

Adapt for dynamic input:

```php
$input = $_POST['jabber_server']; // From form
$x = gethostbyname($input);
$is_valid = filter_var($x, FILTER_VALIDATE_IP, FILTER_FLAG_IPV4 | FILTER_FLAG_IPV6) && $x != '127.0.0.1' && !preg_match('/^10\./', $x) && !preg_match('/^192\.168\./', $x); // Block private ranges too
if (!$is_valid) {
    die('Invalid server');
}
```

## Expected Output

For localhost input: `127.0.0.1 is not valid`
For external valid IP: `8.8.8.8 is valid`

## Related

- [[procedures/Exploit-phpBB-SSRF-for-Port-Scanning]] (as mitigation context)
