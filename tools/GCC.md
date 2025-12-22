---
url: 'https://gcc.gnu.org/'
tags:
  - compiler
  - c
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:56.933Z'
id: 71090631-fce7-41fc-a92d-4fa3f1c4f399
validated: true
submitted: true
---
# gcc

**Status**: Unverified

## Overview

GCC (GNU Compiler Collection) is used to compile the logrotten C source into an executable for the privilege escalation exploit.

## Description

Compiles C programs on Unix-like systems, essential for building custom exploits from source in environments without pre-built binaries.

## Features

- Feature 1: C/C++ compilation
- Feature 2: Optimization flags
- Feature 3: Linking libraries

## Installation

### Requirements

- build-essential package

### Install Commands

```bash
apt-get install build-essential
```

## Basic Usage

```bash
gcc --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -o | Output file name |
| -Wall | Enable warnings |

## Examples

### Example 1: Basic Usage

```bash
gcc -o logrotten logrotten.c
```

### Example 2: Advanced Usage

```bash
gcc -O2 -o logrotten logrotten.c
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer (via compilation)

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- gcc process spawning in /tmp/
- New executables created post-clone
- Compilation errors in logs

## Related Procedures

- [[procedures/Compile-and-Execute-Logrotten-Exploit]]

## Related Tools

- [[tools/git]]
- [[tools/clang]]

## References

- Official site: https://gcc.gnu.org/
