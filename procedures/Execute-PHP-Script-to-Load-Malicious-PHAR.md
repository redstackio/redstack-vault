---
tags:
  - rce
  - phar
  - spl
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
updated_at: '2025-12-14T17:23:19.574Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 2ea7068f-3ee5-4ef4-9a1d-d9fc5c0b15f5
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Execute-PHP-Script-to-Load-Malicious-PHAR

## Summary

This procedure loads the malicious PHAR archive using a PHP script invoking Phar::__construct and SPL directory functions, triggering the buffer overflow and SIGSEGV.

## Description

The overflow propagates from phar_fix_filepath to spl_filesystem_dir_open and phar_parse_url, causing corrupted memory access at addresses like 0xdbdbdbdbdbdbdbdb. This demonstrates RCE potential in applications accepting untrusted PHAR inputs. Target: PHP on Linux with PHAR and SPL enabled.

## Requirements

1. Malicious PHAR from prior procedure
2. PHP binary at ./out/php
3. Valgrind for execution tracing

## Defense

Defensive measures and detection strategies:

- Sanitize PHAR filenames and contents before processing
- Implement PHP's disable_functions for risky extensions
- Use application-level input validation to reject malformed archives

## Objectives

1. Trigger overflow via archive loading
2. Achieve EIP manipulation
3. Simulate RCE in controlled environment

## Instructions

### Step 1: Prepare Loading Script

**Context**: Write load_phar.php to open PHAR as directory stream.

Include code: $phar = new Phar('malicious.phar'); opendir('phar://malicious.phar');

### Step 2: Run Under Valgrind

**Context**: Execute to propagate overflow.

**Command** ([[commands/valgrind-php-phar-test]]):
```bash
valgrind ./out/php load_phar.php
```

> Expected: SIGSEGV due to uninitialized memory, trace involving Phar::__construct.

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

- rce
- phar
- spl
