---
id: 309f7307-9c4f-49f9-a55e-7f62de46da6f
name: php-compare-null-to-empty-string
type: command
executor: bash
data: php -r "var_dump(NULL == '');"
output: null
created_at: '2023-04-06T03:56:40.613327+00:00'
updated_at: '2023-04-06T03:56:40.632973+00:00'
platforms:
  - PHP
tags:
  - type-juggling
  - php
verified: true
validated: true
---

# php-compare-null-to-empty-string

## Command

```bash
php -r "var_dump(NULL == '');"
```

## Description

Compares NULL to empty string, coercing to equal falsy values.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Fixed comparison | No |

## Examples

### Basic Usage

```bash
php -r "var_dump(NULL == '');"
```

## Expected Output

```
bool(true)
```

## Related

- [[procedures/Exploit-PHP-Type-Juggling-for-Authentication-Bypass]]
