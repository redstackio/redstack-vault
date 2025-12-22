---
id: 449508fc-57e5-4c88-b76b-7a69d5c86b5b
name: php-compare-strings-to-hexadecimals
type: command
executor: bash
data: >-
  php -r "var_dump('0010e2' == '1e3'); var_dump('0xABCdef' == ' 0xABCdef');
  var_dump('0xABCdef' == '     0xABCdef'); var_dump('0x01' == 1);
  var_dump('0x1234Ab' == '1193131');"
output: null
created_at: '2023-04-06T03:56:40.612827+00:00'
updated_at: '2023-04-06T03:56:40.632426+00:00'
platforms:
  - PHP
tags:
  - type-juggling
  - php
  - magic-hashes
verified: true
validated: true
---

# php-compare-strings-to-hexadecimals

## Command

```bash
php -r "var_dump('0010e2' == '1e3'); var_dump('0xABCdef' == ' 0xABCdef'); var_dump('0xABCdef' == '     0xABCdef'); var_dump('0x01' == 1); var_dump('0x1234Ab' == '1193131');"
```

## Description

Runs multiple var_dump comparisons of strings, hex values, and numbers, highlighting loose typing and whitespace handling in PHP.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Fixed set of comparisons | No |

## Examples

### Basic Usage

```bash
php -r "var_dump('0010e2' == '1e3'); var_dump('0xABCdef' == ' 0xABCdef'); var_dump('0xABCdef' == '     0xABCdef'); var_dump('0x01' == 1); var_dump('0x1234Ab' == '1193131');"
```

## Expected Output

```
bool(true)
bool(true)  // PHP 5.0, false in 7.0
bool(true)  // PHP 5.0, false in 7.0
bool(true)  // PHP 5.0, false in 7.0
bool(false)
```

## Related

- [[procedures/Exploit-PHP-Type-Juggling-for-Authentication-Bypass]]
