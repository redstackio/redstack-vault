---
id: cmd-numbered-placeholder-test
data: '$wpdb->prepare("%1$%s", "grr");'
tags:
  - sqli
  - test
type: command
output: Broken query that doesn't protect against injection
executor: php
platforms:
  - WordPress
  - PHP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:19.752Z'
verified: false
validated: true
submitted: true
---
# test-numbered-placeholder-in-prepare

## Command

```php
$wpdb->prepare("%1$%s", "grr");
```

## Description

Tests the WordPress prepare method with an invalid numbered %s placeholder, demonstrating failure to quote properly and potential for SQL injection in incomplete fixes like 4.8.3.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| "%1$%s" | Invalid numbered placeholder for string | Yes |
| "grr" | Test input string | Yes |

## Examples

### Basic Usage

```php
$wpdb->prepare("%1$%s", "grr");
```

### Advanced Usage

```php
$wpdb->prepare("%1$%s WHERE id=%d", "payload' OR 1=1;", 1);
```

## Expected Output

A prepared query string like "SELECT * FROM table %1$s" with "grr" unescaped, leading to injection if payload is used.

## Related

- [[Related Procedure]]
