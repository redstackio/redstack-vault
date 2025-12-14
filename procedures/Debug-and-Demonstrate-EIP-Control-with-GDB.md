---
id: proc-debug-eip-gdb
tags:
  - debugging
  - gdb
  - exploit-verification
type: procedure
tools:
  - '[[tools/GDB]]'
  - '[[tools/PHP]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/gdb-debug-php-script]]'
  - '[[commands/info-registers-eip]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:28:20.183Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Debug-and-Demonstrate-EIP-Control-with-GDB

## Summary

This procedure executes the PHP POC script under GDB to observe the heap overflow crash and verify attacker control over the EIP register, demonstrating potential for arbitrary code execution.

## Description

Run the bz_poc.php script via PHP CLI in GDB, which triggers SIGSEGV due to the heap overflow. Inspect registers post-crash to confirm EIP is overwritten with 0x42424242 from the 'BBBB' input. Target: 32-bit Linux with PHP 7.1 and Bzip2. Prerequisites: Compiled POC script and GDB installed.

## Requirements

1. GDB debugger
2. PHP 7.1 CLI binary (sapi/cli/php)
3. POC script at ../crash/bz_poc.php

## Defense

Defensive measures and detection strategies:

- Use stack/heap canaries in PHP builds
- Log and monitor debugger attachments to processes
- Deploy W^X memory protections to prevent code execution

## Objectives

1. Confirm crash from heap overflow
2. Validate EIP hijacking
3. Prove RCE feasibility

## Instructions

### Step 1: Launch GDB with PHP Script

**Context**: Start debugging the PHP execution to catch the overflow.

**Command** ([[commands/gdb-debug-php-script]]):
```bash
gdb --args sapi/cli/php -f ../crash/bz_poc.php
```

> Run 'run' in GDB; expect SIGSEGV during bzdecompress(). Output shows crash details and registers.

### Step 2: Inspect EIP Register

**Context**: After crash, check if EIP is controlled by input.

**Command** ([[commands/info-registers-eip]]):
```bash
i r eip
```

> Expected: eip 0x42424242 0x42424242, confirming overwrite from 'BBBB'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used

- [[commands/gdb-debug-php-script]]
- [[commands/info-registers-eip]]

## Tools Used

- [[tools/GDB]]
- [[tools/PHP]]

## Tags

- debugging
- gdb
- eip-control
