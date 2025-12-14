---
url: 'https://clang.llvm.org/docs/AddressSanitizer.html'
tags:
  - sanitizer
  - memory-debug
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:30.907Z'
id: 98318766-98bd-4b86-95ed-392f2b4a97c9
validated: true
submitted: true
---
# Address Sanitizer (ASAN)

**Status**: Unverified

## Overview

Runtime memory error detector for buffer overflows, UAF, etc., in C/C++.

## Description

Integrates with GCC/Clang to catch issues at runtime during fuzzing/testing.

## Features

- Feature 1: Overflow detection
- Feature 2: UAF reporting
- Feature 3: Stack traces

## Installation

### Requirements

- GCC/Clang

### Install Commands

```bash
# Enabled via flags, no separate install
```

## Basic Usage

```bash
gcc -fsanitize=address code.c
```

### Common Options

| Option | Description |
|--------|-------------|
| -fsanitize=address | Enable ASAN |

## Examples

### Example 1: Basic Usage

```bash
gcc -fsanitize=address input.c
./a.out
```

### Example 2: Advanced Usage

```bash
gcc -g -fsanitize=address input.c
```

## MITRE ATT&CK Mapping

### Techniques

- [[Develop Capabilities]] Develop Capabilities

### Tactics

- [[Resource Development]] Resource Development

## Detection

- ASAN runtime errors in logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Valgrind]]

## References

- https://clang.llvm.org/docs/AddressSanitizer.html
