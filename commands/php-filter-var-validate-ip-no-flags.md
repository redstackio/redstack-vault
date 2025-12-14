---
id: 00000000-0000-0000-0000-000000000007
name: php-filter-var-validate-ip-no-flags
type: command
executor: php
data: 'filter_var("0:0:0:0:0:ffff:127.0.0.1", FILTER_VALIDATE_IP)'
output: null
created_at: '2023-12-14T00:00:00Z'
updated_at: '2025-12-14T04:08:48.753Z'
platforms:
  - PHP
tags:
  - validation
  - ssrf
  - bypass
verified: false
validated: true
submitted: true
---

# php-filter-var-validate-ip-no-flags

## Command

```php
filter_var("0:0:0:0:0:ffff:127.0.0.1", FILTER_VALIDATE_IP)
```

## Description

PHP function to validate an IP address without range restriction flags, showing basic format checking; illustrates why embedded IPv4 in IPv6 may not be recognized as valid, but app logic allows progression in SSRF bypass.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| input | Bracket-removed IPv6 string with embedded IPv4 (e.g., 0:0:0:0:0:ffff:127.0.0.1) | Yes |
| filter | FILTER_VALIDATE_IP to check validity | Yes |

## Examples

### Basic Usage

```php
<?php var_dump(filter_var("127.0.0.1", FILTER_VALIDATE_IP)); ?>
```

### Advanced Usage

```php
<?php var_dump(filter_var("0:0:0:0:0:ffff:127.0.0.1", FILTER_VALIDATE_IP)); ?>
```

## Expected Output

Returns false for unrecognized formats like embedded IPv4 in IPv6, e.g., bool(false), but in vulnerability context, incomplete checks enable the exploit.

## Related

- [[Related Command: php-filter-var-validate-ip]]
