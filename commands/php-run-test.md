---
data: ./sapi/cli/php test_overflow.php
tags:
  - php
  - testing
  - vulnerability
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:13.028Z'
id: 22374ee8-9615-4f3d-9fe3-da93c6f7711c
verified: false
validated: true
submitted: true
---
# php-run-test

## Command

```bash
./sapi/cli/php test_overflow.php
```

## Description

Executes a PHP script using a custom-built binary to test for runtime errors like buffer overflows. Use in vulnerability reproduction scenarios targeting PHP core functions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `./sapi/cli/php` | Path to ASan-instrumented PHP CLI binary | Yes |
| `test_overflow.php` | Script file with overflow-triggering code | Yes |

## Examples

### Basic Usage

```bash
./sapi/cli/php vuln_test.php
```

### Advanced Usage

```bash
ASAN_OPTIONS=abort_on_error=1 ./sapi/cli/php test_overflow.php 2> asan.log
```

## Expected Output

PHP execution output or ASan error report detailing the buffer overflow, including address, size, and stack trace.

## Related

- [[Related Procedure|procedures/Reproduce-Buffer-Overflow-in-PHP-mkgmtime]]
