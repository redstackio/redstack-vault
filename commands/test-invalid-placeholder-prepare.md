---
id: cmd-wp-prepare-invalid-ph
data: '$wpdb->prepare("%1$%s", "grr")'
tags:
  - sqli
  - wordpress
type: command
output: null
executor: php
platforms:
  - PHP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:56.607Z'
verified: false
validated: true
submitted: true
---
# test-invalid-placeholder-prepare

## Command

```php
$wpdb->prepare("%1$%s", "grr")
```

## Description

Tests the WordPress $wpdb->prepare() method with an invalid numbered placeholder (%1$%s), demonstrating insecure handling that leaves inputs unescaped, potentially leading to SQL injection in patched versions like 4.8.3.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| "%1$%s" | Invalid numbered placeholder format | Yes |
| "grr" | Test input string | Yes |

## Examples

### Basic Usage

```php
$wpdb->prepare("%1$%s", "grr")
```

### Advanced Usage

```php
$result = $wpdb->prepare("SELECT * FROM %1$%s WHERE id = %d", "wp_users", 1);
$wpdb->query($result);
```

## Expected Output

Broken query or unescaped input leading to potential SQLi, e.g., malformed prepared statement exposing raw "grr" in SQL.

## Related

- [[Related Procedure]]
