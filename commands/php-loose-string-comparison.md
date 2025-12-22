---
id: 62350208-b0e2-4193-ae2f-7c9ac5bf02f0
name: php-loose-string-comparison
type: command
executor: php
data: 'if (md5(''240610708'') == ''0'') { echo ''Bypass successful''; }'
output: Bypass successful
created_at: '2023-04-06T03:56:40.699339+00:00'
updated_at: '2023-04-06T03:56:40.708704+00:00'
platforms:
  - Web
  - PHP
tags:
  - type-juggling
  - magic-hash
verified: true
validated: true
---

# php-loose-string-comparison

## Command

```php
if (md5('240610708') == '0') { echo 'Bypass successful'; }
```

## Description

This PHP command demonstrates type juggling by loosely comparing the MD5 hash of a magic input to the string '0'. The hash starts with '0e', treated as 0 in scientific notation, causing a true result and bypassing strict equality checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| md5('240610708') | Computes MD5 hash of the input string | Yes |
| == '0' | Loose comparison to string '0' | Yes |

## Examples

### Basic Usage

```php
if (md5('240610708') == '0') { echo 'Bypass successful'; }
```

### Advanced Usage

```php
var_dump(md5('240610708') == 0); // bool(true)
```

## Expected Output

Bypass successful

Or for var_dump: bool(true)

## Related

- [[procedures/Bypass-PHP-Authentication-with-Type-Juggling-and-Magic-Hashes]]
