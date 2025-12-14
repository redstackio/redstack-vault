---
id: cmd-uuid-placeholder-001
data: php -d mbstring.func_overload=2 ./poc.php
tags:
  - php
  - poc
  - mbstring
type: command
output: null
executor: bash
platforms:
  - PHP
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:13.045Z'
verified: false
validated: true
submitted: true
---
# php-mbstring-overload-poc

## Command

```bash
php -d mbstring.func_overload=2 ./poc.php
```

## Description

Executes a PHP POC script with mbstring.func_overload enabled to demonstrate how unsafe string functions like strlen and substr behave incorrectly on multibyte strings, potentially bypassing security validations in applications like phpMyAdmin or Airship.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d mbstring.func_overload=2` | Enables full overloading of single-byte string functions by mbstring (0=off, 1=partial, 2=full, 4=double-quoted strings) | Yes |
| `./poc.php` | Path to the POC PHP script containing vulnerable string operations | Yes |

## Examples

### Basic Usage

```bash
php -d mbstring.func_overload=2 ./poc.php
```

### Advanced Usage

```bash
php -d mbstring.func_overload=2 -d display_errors=1 ./poc.php
```

Add -d display_errors=1 for verbose error output during testing.

## Expected Output

Dumps the unserialized object or string metrics, showing bypass of safe unserialize restrictions (e.g., allowing object instantiation or property access via multibyte tricks). Example: "Length: 3\nSubstring: [multibyte chars]\nBypass possible" indicating failed length check.

## Related

- [[Related Procedure]]
