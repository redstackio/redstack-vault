---
id: tool-uuid-4
url: 'https://man7.org/linux/man-pages/man1/ldd.1.html'
tags:
  - binary-analysis
  - dependencies
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:19.153Z'
validated: true
submitted: true
---
# ldd

**Status**: Unverified

## Overview

ldd prints shared library dependencies of executable files, used to verify ASAN linkage in Squid binary.

## Description

Quickly checks if libasan is dynamically linked, essential for confirming sanitizer instrumentation before exploitation.

## Features

- Feature 1: List dynamic dependencies
- Feature 2: Path resolution for libraries
- Feature 3: Recursive dependency tracing

## Installation

### Requirements

- Standard in glibc

### Install Commands

```bash
# Usually pre-installed
ldd --version
```

## Basic Usage

```bash
ldd --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -v | Verbose output |
| -r | Perform relocations |

## Examples

### Example 1: Basic Usage

```bash
ldd squid
```

### Example 2: Advanced Usage

```bash
ldd squid | grep asan
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- ldd executions in logs
- Binary analysis attempts

## Related Procedures

- [[procedures/Verify-ASAN-Linkage-and-Monitor-Crash-with-GDB]]

## Related Tools

- [[tools/GDB]]

## References

- Man page: https://man7.org/linux/man-pages/man1/ldd.1.html
