---
id: 8d51c9b5-b7ed-47eb-b311-ef260902b0fe
name: php-compare-zero-to-false
type: command
executor: bash
data: php -r "var_dump(0 == false);"
output: null
created_at: '2023-04-06T03:56:40.613233+00:00'
updated_at: '2023-04-06T03:56:40.632862+00:00'
platforms:
  - PHP
tags:
  - type-juggling
  - php
verified: true
validated: true
---

# php-compare-zero-to-false

## Command

```bash
php -r "var_dump(0 == false);"
```

## Description

Executes a PHP one-liner to compare the integer 0 to the boolean false using loose equality (==), demonstrating type coercion where both are falsy and equal.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; fixed comparison | No |

## Examples

### Basic Usage

```bash
php -r "var_dump(0 == false);"
```

## Expected Output

```
bool(true)
```

## Related

- [[procedures/Exploit-PHP-Type-Juggling-for-Authentication-Bypass]]
