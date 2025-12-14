---
tags:
  - compilation
  - sanitizer
  - debugging
type: procedure
tools:
  - '[[tools/AddressSanitizer]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/configure-php-asan]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:28:13.034Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: aceeb35f-6b22-4f0b-878c-aa71d4a1c54d
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Compile PHP with AddressSanitizer

## Summary

This procedure outlines compiling PHP from source with AddressSanitizer enabled to detect memory errors like buffer overflows in its C/C++ internals, essential for vulnerability hunting in PHP core functions.

## Description

AddressSanitizer (ASan) is a compiler instrumentation tool that adds runtime checks for memory issues. For PHP, this involves configuring the build with ASan flags before make, targeting Linux environments. It helps identify issues like the mkgmtime() overflow by reporting violations during execution. Prerequisites: PHP source, Clang/GCC. Outcomes: An instrumented PHP binary that logs errors to stderr.

## Requirements

1. Linux with development tools (autoconf, make, clang)
2. Downloaded PHP source tarball
3. Sufficient disk space for build (~500MB)

## Defense

Defensive measures and detection strategies:

- Use ASan in CI/CD pipelines for proactive vulnerability detection
- Integrate with fuzzing tools like AFL for broader coverage
- Review ASan reports for false positives in non-production builds

## Objectives

1. Produce a debuggable PHP binary
2. Enable detection of memory corruption
3. Facilitate reproduction of specific vulnerabilities

## Instructions

### Step 1: Clean and Configure Build

**Context**: Prepare the source for ASan instrumentation by cleaning previous builds and setting compiler flags.

**Command** ([[commands/configure-php-asan]]):
```bash
make clean && CC=clang CFLAGS="-fsanitize=address -g" LDFLAGS="-fsanitize=address" ./configure --enable-debug --disable-all
```

> Cleans artifacts, sets ASan via environment variables, and configures minimal PHP features for faster build. Expected output: Configuration summary ending with "Thank you for using PHP."

### Step 2: Build the Binary

**Context**: Compile the instrumented source to generate the PHP executable.

**Command** ([[commands/make-php]]):
```bash
make -j$(nproc)
```

> Builds using all CPU cores. Expected output: Progress logs culminating in "Build complete." Verify with `./sapi/cli/php --version` showing ASan-enabled binary.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/configure-php-asan]]
- [[commands/make-php]]

## Tools Used

- [[tools/AddressSanitizer]]

## Tags

- compilation
- php-build
- memory-debugging
