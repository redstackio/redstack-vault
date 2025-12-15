---
id: tool-007
url: 'https://valgrind.org/'
tags:
  - dynamic-analysis
  - memory
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:27.920Z'
validated: true
submitted: true
---
# valgrind

**Status**: Unverified

## Overview

Valgrind is a dynamic analysis tool for detecting memory leaks and errors in programs like cURL.

## Description

Memcheck tool instruments code to track memory usage; used with --leak-check=full for cURL tests.

## Features

- Feature 1: Leak detection
- Feature 2: Buffer overflow checks
- Feature 3: Origin tracking

## Installation

### Requirements

- Linux with glibc

### Install Commands

```bash
sudo apt-get install valgrind
```

## Basic Usage

```bash
valgrind --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `--tool=memcheck` | Memory tool |
| `--leak-check=full` | Full leaks |

## Examples

### Example 1: Basic Usage

```bash
valgrind ./program
```

### Example 2: Advanced Usage

```bash
valgrind --tool=memcheck --track-origins=yes ./program
```

## MITRE ATT&CK Mapping

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Tactics

- [[Execution]] Execution

## Detection

- Valgrind runtime overhead
- Log files generated

## Related Procedures

- [[procedures/Dynamic-Memory-Testing-of-cURL-with-Valgrind]]

## Related Tools

- [[tools/AddressSanitizer]]

## References

- Valgrind docs
