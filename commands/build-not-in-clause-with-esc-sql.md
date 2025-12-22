---
id: cmd-not-in-clause
data: '$not_in = "''" . implode( "'', ''", esc_sql( $_POST[''exclude''] ) ) . "''";'
tags:
  - sqli
  - esc-sql
type: command
output: 'Quoted string for SQL clause, but can be injected via prepare() flaws'
executor: php
platforms:
  - WordPress
  - PHP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:19.740Z'
verified: false
validated: true
submitted: true
---
# build-not-in-clause-with-esc-sql

## Command

```php
$not_in = "'" . implode( "', '", esc_sql( $_POST['exclude'] ) ) . "'";
```

## Description

Builds a SQL NOT IN clause using escaped POST data from user input, vulnerable to re-introduced SQLi in WordPress 4.8.3 due to interactions with prepare().

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| esc_sql( $_POST['exclude'] ) | Escaped user input array from POST | Yes |

## Examples

### Basic Usage

```php
$exclude = $_POST['exclude'] ?? [];
$not_in = "'" . implode( "', '", esc_sql( $exclude ) ) . "'";
```

### Advanced Usage

```php
$wpdb->query("DELETE FROM table WHERE id NOT IN ($not_in)");
```

## Expected Output

A string like "'val1', 'val2'" for use in queries, but injectable if esc_sql fails with prepare().

## Related

- [[Related Procedure]]
