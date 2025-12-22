---
data: 'valgrind ./out/php [script involving Phar::__construct with malicious PHAR]'
tags:
  - memory-debugging
  - php
  - phar
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:19.564Z'
id: 2524292f-26ec-423b-8014-d77172c55943
verified: false
validated: true
submitted: true
---
# valgrind-php-phar-test

## Command

```bash
valgrind ./out/php [script involving Phar::__construct with malicious PHAR]
```

## Description

Runs the PHP interpreter under Valgrind to detect memory errors like invalid reads and overflows during processing of a malicious PHAR archive, confirming stack-based vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `./out/php` | Path to the custom or built PHP binary | Yes |
| `[script]` | PHP script file (e.g., phar_test.php or load_phar.php) that loads the malicious PHAR | Yes |

## Examples

### Basic Usage

```bash
valgrind ./out/php phar_test.php
```

### Advanced Usage

```bash
valgrind --tool=memcheck --leak-check=full ./out/php load_phar.php 2> valgrind.log
```

## Expected Output

Invalid read of size 8 at zend_mm_alloc_small (zend_alloc.c:1291), stack trace through PHAR functions like phar_fix_filepath (phar.c:2080), Process terminating with SIGSEGV and General Protection Fault at address 0xdbdbdbdbdbdbdbdb.

## Related

- [[Related Procedure: Create-and-Test-Malicious-PHAR-Archive]]
