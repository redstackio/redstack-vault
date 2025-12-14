---
id: cmd-quoting-break-test
data: >-
  $input = "' OR '1'='1"; $quoted = "'" . esc_sql($input) . "'"; $query =
  $wpdb->prepare("SELECT * FROM wp_posts WHERE post_title = %s", $quoted);
  $wpdb->query($query);
tags:
  - sqli
  - wordpress
type: command
output: null
executor: php
platforms:
  - PHP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:56.539Z'
verified: false
validated: true
submitted: true
---
# test-quoting-breakout-prepare

## Command

```php
$input = "' OR '1'='1"; $quoted = "'" . esc_sql($input) . "'"; $query = $wpdb->prepare("SELECT * FROM wp_posts WHERE post_title = %s", $quoted); $wpdb->query($query);
```

## Description

Tests quote breakout with pre-quoted input and %s.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $input | Payload | Yes |

## Examples

### Basic Usage

```php
// As above
```

## Expected Output

All posts returned.

## Related

- [[procedures/Demonstrate-Improper-Quoting-Issue]]
