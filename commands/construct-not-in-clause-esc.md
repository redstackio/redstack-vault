---
id: cmd-not-in-esc-sql
data: '$not_in = "''" . implode( "'', ''", esc_sql( $_POST[''exclude''] ) ) . "''";'
tags:
  - sqli
  - wordpress
type: command
output: null
executor: php
platforms:
  - PHP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:56.595Z'
verified: false
validated: true
submitted: true
---
# construct-not-in-clause-esc

## Command

```php
$not_in = "'" . implode( "', '", esc_sql( $_POST['exclude'] ) ) . "'";
```

## Description

Constructs a SQL NOT IN clause using esc_sql() on user input from $_POST['exclude'], but vulnerable when combined with $wpdb->prepare() quoting issues in plugins, allowing injection if prepare() double-quotes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| implode | Joins array elements with quotes | Yes |
| esc_sql( $_POST['exclude'] ) | Escaped user input from POST | Yes |

## Examples

### Basic Usage

```php
$exclude = $_POST['exclude'] ?? [];
$not_in = "'" . implode( "', '", esc_sql( $exclude ) ) . "'";
```

### Advanced Usage

```php
$query = $wpdb->prepare("SELECT * FROM wp_posts WHERE ID NOT IN ($not_in)", []);
```

## Expected Output

Quoted string for SQL clause, but can be broken by prepare method flaws, e.g., "'1', '2'" becoming injectable.

## Related

- [[Related Procedure]]
