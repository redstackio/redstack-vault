---
tags:
  - buffer-overflow
  - phar
  - php
type: procedure
tools:
  - '[[tools/Valgrind]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/valgrind-php-phar-test]]'
verified: false
platforms:
  - Linux
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:19.582Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: de356227-9834-4b27-8ed8-4f08bd26ed06
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Create-and-Test-Malicious-PHAR-Archive

## Summary

This procedure involves crafting a malicious PHAR archive with a manipulated filepath to exploit a stack-based buffer overflow in PHP's phar_fix_filepath function, tested under Valgrind to detect initial memory corruption.

## Description

In a PHP environment with the PHAR extension, untrusted archives can lead to overflows during filepath parsing. This targets phar.c:2080, propagating through phar_split_fname, phar_parse_url, and Phar::__construct. The attack scenario assumes an application processes external PHAR files, enabling RCE via EIP control. Prerequisites include a Linux system with PHP built from source.

## Requirements

1. Linux OS with PHP source code compiled to ./out/php
2. Valgrind installed for memory debugging
3. Basic scripting knowledge to generate malformed PHAR files

## Defense

Defensive measures and detection strategies:

- Disable PHAR extension if not needed or validate all inputs strictly
- Use sandboxing for PHP processes handling untrusted files
- Monitor for segmentation faults in PHP logs and deploy memory sanitizers in development

## Objectives

1. Generate a PHAR archive that overflows the stack buffer
2. Detect invalid memory reads during initial testing
3. Confirm vulnerability in PHAR filepath handling

## Instructions

### Step 1: Craft Malicious PHAR File

**Context**: Create a PHAR with oversized filepath to cause overflow in phar_fix_filepath.

Use PHP or a hex editor to build the archive with corrupted data leading to uninitialized memory access.

**Command** ([[commands/valgrind-php-phar-test]]):
```bash
valgrind ./out/php phar_test.php
```

> This runs a test script loading the PHAR, with Valgrind detecting issues in zend_mm_alloc_small.

### Step 2: Initial Valgrind Testing

**Context**: Execute under Valgrind to capture memory errors.

Prepare phar_test.php to invoke Phar::__construct on the malicious file.

**Command** ([[commands/valgrind-php-phar-test]]):
```bash
valgrind ./out/php phar_test.php
```

> Expected: Invalid read of size 8 at phar.c:2080, stack trace through PHAR functions.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques


## Commands Used

- [[commands/valgrind-php-phar-test]]

## Tools Used

- [[tools/Valgrind]]

## Tags

- buffer-overflow
- phar
- php
