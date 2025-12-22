---
id: 830bd8f9-69f2-478a-9f9d-12c163a5ef1a
name: php-compare-false-to-null
type: command
executor: bash
data: php -r "var_dump(false == NULL);"
output: null
created_at: '2023-04-06T03:56:40.613255+00:00'
updated_at: '2023-04-06T03:56:40.632945+00:00'
platforms:
  - PHP
tags:
  - type-juggling
  - php
verified: true
validated: true
---

# php-compare-false-to-null

## Command

```bash
php -r "var_dump(false == NULL);"
```

## Description

Compares boolean false to NULL using loose equality, both falsy.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Fixed comparison | No |

## Examples

### Basic Usage

```bash
php -r "var_dump(false == NULL);"
```

## Expected Output

```
bool(true)
```

## Related

- [[procedures/Exploit-PHP-Type-Juggling-for-Authentication-Bypass]]
