---
id: 9384ec90-29fb-4618-81d2-d09074883607
name: php-compare-empty-string-zero-false-null
type: command
executor: bash
data: php -r "var_dump('' == 0 == false == NULL);"
output: null
created_at: '2023-04-06T03:56:40.613123+00:00'
updated_at: '2023-04-06T03:56:40.632776+00:00'
platforms:
  - PHP
tags:
  - type-juggling
  - php
verified: true
validated: true
---

# php-compare-empty-string-zero-false-null

## Command

```bash
php -r "var_dump('' == 0 == false == NULL);"
```

## Description

Tests chained loose equality between empty string, 0, false, and NULL in PHP, showing all falsy values are equivalent.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Fixed chained comparison | No |

## Examples

### Basic Usage

```bash
php -r "var_dump('' == 0 == false == NULL);"
```

## Expected Output

```
bool(true)
```

## Related

- [[procedures/Exploit-PHP-Type-Juggling-for-Authentication-Bypass]]
