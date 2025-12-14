---
id: f6g7h8i9-j0k1-2345-fghi-678901234567
url: 'https://clang.llvm.org/docs/AddressSanitizer.html'
tags:
  - memory-sanitizer
  - debugging
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:36.923Z'
configuration: Used in x64 Linux GCC build for MRuby analysis
validated: true
submitted: true
---
# ASAN

**Status**: Unverified

## Overview

AddressSanitizer (ASAN) is a fast memory error detector integrated into compilers like GCC and Clang, designed to identify issues such as null pointer dereferences, use-after-free, and buffer overflows during program execution.

## Description

ASAN instruments code at compile-time and provides runtime checks, making it ideal for analyzing vulnerabilities in engines like MRuby. In this case, it's used to build and run the MRuby sandbox, detecting the null pointer dereference in mrb_obj_instance_eval during PoC execution.

## Features

- Feature 1: Runtime detection of invalid memory accesses.
- Feature 2: Detailed reports with stack traces for errors.
- Feature 3: Low overhead for development testing.

## Installation

### Requirements

- GCC 4.8+ on Linux x64.
- MRuby source code.

### Install Commands

```bash
# ASAN is built into GCC; no separate install needed
# Ensure GCC is installed
gcc --version
```

## Basic Usage

```bash
gcc -fsanitize=address -g program.c -o program
./program
```

### Common Options

| Option | Description |
|--------|-------------|
| -fsanitize=address | Enable ASAN |
| -g | Debug info for traces |
| -O1 | Optimize while keeping instrumentation |

## Examples

### Example 1: Basic Usage

```bash
gcc -fsanitize=address -g -o mrb vm.c
./mrb script.rb
```

### Example 2: Advanced Usage

```bash
gcc -fsanitize=address,undefined -g -O0 -o mrb vm.c libmruby.a
ASAN_OPTIONS=abort_on_error=1 ./mrb script.rb
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service (for vulnerability detection)

### Tactics

- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Binaries compiled with -fsanitize=address flag.
- ASAN error reports in logs or console output.

## Related Procedures

- [[procedures/Trigger-MRuby-Segmentation-Fault-with-PoC-Script]]

## Related Tools

- [[tools/GDB]]

## References

- Official documentation: https://gcc.gnu.org/onlinedocs/gcc/Instrumentation-Options.html
- Related resources: Clang ASAN docs
