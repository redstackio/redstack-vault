---
id: 3d86923a-5301-420d-8eea-205a786c1e67
name: php-compare-empty-string-to-zero
type: command
executor: bash
data: php -r "var_dump('' == 0);"
output: null
created_at: '2023-04-06T03:56:40.613167+00:00'
updated_at: '2023-04-06T03:56:40.632803+00:00'
platforms:
  - PHP
tags:
  - type-juggling
  - php
verified: true
validated: true
---

# php-compare-empty-string-to-zero

## Command

```bash
php -r "var_dump('' == 0);"
```

## Description

Compares an empty string to the integer 0 using ==, coercing the string to 0.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Fixed comparison | No |

## Examples

### Basic Usage

```bash
php -r "var_dump('' == 0);"
```

## Expected Output

```
bool(true)
```

## Related

- [[procedures/Exploit-PHP-Type-Juggling-for-Authentication-Bypass]]
