---
id: tool-uuid-3
url: 'https://github.com/google/sanitizers'
tags:
  - sanitizer
  - memory-debug
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.161Z'
validated: true
submitted: true
---
# AddressSanitizer

**Status**: Unverified

## Overview

AddressSanitizer (ASAN) is a fast memory error detector for C/C++ programs, identifying heap overflows and use-after-free issues at runtime.

## Description

Integrated during Squid compilation with -fsanitize=address; detects the buffer overflow in base64 decoding and aborts with detailed reports.

## Features

- Feature 1: Heap buffer overflow detection
- Feature 2: Stack/use-after-free checks
- Feature 3: Runtime error reporting

## Installation

### Requirements

- GCC/Clang with sanitizer support

### Install Commands

```bash
# Typically bundled with compiler
apt install gcc g++
```

## Basic Usage

```bash
# Compile with flag
gcc -fsanitize=address program.c -o program
# Run with options
ASAN_OPTIONS=... ./program
```

### Common Options

| Option | Description |
|--------|-------------|
| abort_on_error=true | Abort on first error |
| verbosity=2 | Detailed logs |

## Examples

### Example 1: Basic Usage

```bash
gcc -fsanitize=address -g test.c -o test
ASAN_OPTIONS=abort_on_error=1 ./test
```

### Example 2: Advanced Usage

```bash
ASAN_OPTIONS="abort_on_error=true:detect_leaks=1" ./squid
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- libasan.so loaded in processes
- ASAN error messages in logs
- Compiler flags in binaries

## Related Procedures

- [[procedures/Build-and-Run-Squid-with-AddressSanitizer]]

## Related Tools

- [[tools/GDB]]

## References

- Official documentation: https://clang.llvm.org/docs/AddressSanitizer.html
