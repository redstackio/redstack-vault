---
tags:
  - buffer-overflow
  - php
  - memory-corruption
  - rce
type: procedure
tools:
  - '[[tools/AddressSanitizer]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/php-run-test]]'
  - '[[commands/compile-php-asan]]'
verified: false
platforms:
  - Linux
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:28:13.040Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 44d168b2-41fa-4668-8026-56e8002d1d15
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Reproduce Buffer Overflow in PHP mkgmtime

## Summary

This procedure demonstrates how to reproduce a global buffer overflow in PHP's mkgmtime() function, an internal time manipulation routine, by crafting inputs that exceed buffer bounds during date parsing. It is primarily used in vulnerability research to confirm memory corruption issues that could lead to denial of service or remote code execution in PHP applications processing user-supplied time data.

## Description

The mkgmtime() function in PHP's core (written in C) handles Gregorian-to-Unix timestamp conversion and lacks sufficient bounds checking when parsing large or malformed date components, resulting in a global buffer overflow. This can corrupt static memory areas, causing crashes or exploitable conditions. The procedure assumes a local Linux environment with PHP source code and uses AddressSanitizer for detection. Prerequisites include compiler access; outcomes include ASan reports confirming the overflow, useful for patching or exploitation development.

## Requirements

1. Linux environment with Clang or GCC supporting AddressSanitizer
2. PHP source code (vulnerable version, e.g., PHP 7.x pre-2017 patches)
3. Basic knowledge of C compilation and PHP internals

## Defense

Defensive measures and detection strategies:

- Compile PHP with memory sanitizers in production for early detection
- Input validation on time-related functions (e.g., limit date ranges in applications)
- Monitor for segmentation faults or unusual memory usage in PHP processes
- Apply upstream patches from PHP security advisories

## Objectives

1. Trigger and detect the buffer overflow to validate vulnerability
2. Analyze stack traces for exploitation vectors
3. Demonstrate impact on PHP application stability

## Instructions

### Step 1: Prepare PHP Binary with AddressSanitizer

**Context**: Instrument the PHP build to enable runtime memory error detection, focusing on buffer overflows in C code.

**Command** ([[commands/compile-php-asan]]):
```bash
make clean && CC=clang CFLAGS="-fsanitize=address -g" LDFLAGS="-fsanitize=address" ./configure --enable-debug && make -j$(nproc)
```

> This command cleans the build, configures PHP with ASan flags, and compiles the binary. Expected output includes a successful build log; verify with `ls sapi/cli/php` showing the instrumented executable.

### Step 2: Create and Run Overflow Test Script

**Context**: Craft a PHP script that invokes gmmktime() (which calls mkgmtime()) with oversized inputs to overflow the global buffer during time calculation.

**Command** ([[commands/php-run-test]]):
```bash
./sapi/cli/php test_overflow.php
```

> Run the test script using the ASan-enabled PHP. The script should contain code like `gmmktime(0, 0, 0, 1, 1, 2147483647 + 100000);` to force overflow. Expected output: ASan report like "==1234==ERROR: AddressSanitizer: global-buffer-overflow WRITE of size 4 at 0x..." with trace to mkgmtime in ext/date/lib/parse_iso_intervals.c or similar.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques


## Commands Used

- [[commands/compile-php-asan]]
- [[commands/php-run-test]]

## Tools Used

- [[tools/AddressSanitizer]]

## Tags

- buffer-overflow
- php
- memory-corruption
