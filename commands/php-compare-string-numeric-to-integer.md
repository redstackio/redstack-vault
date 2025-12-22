---
id: a31739c7-2719-4449-8d3a-dbdcada68121
name: php-compare-string-numeric-to-integer
type: command
executor: bash
data: php -r "var_dump('123' == 123);"
output: null
created_at: '2023-04-06T03:56:40.612979+00:00'
updated_at: '2023-04-06T03:56:40.632632+00:00'
platforms:
  - PHP
tags:
  - type-juggling
  - php
verified: true
validated: true
---

# php-compare-string-numeric-to-integer

## Command

```bash
php -r "var_dump('123' == 123);"
```

## Description

Compares a numeric string to an integer, coercing the string to int.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Fixed comparison | No |

## Examples

### Basic Usage

```bash
php -r "var_dump('123' == 123);"
```

## Expected Output

```
bool(true)
```

## Related

- [[procedures/Exploit-PHP-Type-Juggling-for-Authentication-Bypass]]
