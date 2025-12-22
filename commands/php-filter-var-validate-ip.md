---
id: 00000000-0000-0000-0000-000000000006
name: php-filter-var-validate-ip
type: command
executor: php
data: >-
  filter_var("[0:0:0:0:0:ffff:127.0.0.1]", FILTER_VALIDATE_IP,
  FILTER_FLAG_NO_PRIV_RANGE | FILTER_FLAG_NO_RES_RANGE)
output: null
created_at: '2023-12-14T00:00:00Z'
updated_at: '2025-12-14T04:08:48.758Z'
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

# php-filter-var-validate-ip

## Command

```php
filter_var("[0:0:0:0:0:ffff:127.0.0.1]", FILTER_VALIDATE_IP, FILTER_FLAG_NO_PRIV_RANGE | FILTER_FLAG_NO_RES_RANGE)
```

## Description

PHP function call to validate an IP address string, applying flags to reject private and reserved ranges; used to analyze why bracketed IPv6 inputs fail validation, highlighting the bypass when brackets are removed.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| input | IP string to validate (e.g., bracketed IPv6 with embedded IPv4) | Yes |
| filter | FILTER_VALIDATE_IP to check if it's a valid IP | Yes |
| flags | FILTER_FLAG_NO_PRIV_RANGE | FILTER_FLAG_NO_RES_RANGE to reject private/reserved IPs | Yes |

## Examples

### Basic Usage

```php
<?php var_dump(filter_var("[::1]", FILTER_VALIDATE_IP, FILTER_FLAG_NO_PRIV_RANGE)); ?>
```

### Advanced Usage

```php
<?php var_dump(filter_var("[0:0:0:0:0:ffff:127.0.0.1]", FILTER_VALIDATE_IP, FILTER_FLAG_NO_PRIV_RANGE | FILTER_FLAG_NO_RES_RANGE)); ?>
```

## Expected Output

Returns false for invalid or restricted IPs, e.g., bool(false) for bracketed private embeds, demonstrating the need for bracket removal in the bypass.

## Related

- [[Related Command: php-filter-var-validate-ip-no-flags]]
