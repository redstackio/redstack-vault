---
url: 'https://gcc.gnu.org/'
tags:
  - compiler
  - c-language
type: tool
verified: false
platforms:
  - macOS
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:58.992Z'
id: 05c27de1-dff8-490f-87f5-69fdede40d3d
validated: true
submitted: true
---
# GCC-Compiler

**Status**: Unverified

## Overview

GCC (GNU Compiler Collection) is a mature compiler system for C and other languages, commonly used in security testing to build custom exploits and malicious binaries from source code.

## Description

GCC compiles C source into native executables, supporting macOS Mach-O binaries. In offensive security, it's essential for creating payloads that integrate with system calls like system() for shell execution in privilege escalation scenarios.

## Features

- Feature 1: Supports C, C++, Objective-C for cross-platform binaries
- Feature 2: Optimizations and debugging flags for exploit development
- Feature 3: Integration with makefiles for complex builds

## Installation

### Requirements

- macOS with Xcode Command Line Tools

### Install Commands

```bash
xcode-select --install
```

## Basic Usage

```bash
gcc --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-o filename` | Specify output file |
| `-Wall` | Enable all warnings |
| `-g` | Include debug info |

## Examples

### Example 1: Basic Usage

```bash
gcc test.c -o a.out
```

### Example 2: Advanced Usage

```bash
gcc -Wall -o malicious test.c
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Execution through Module Load]] Shared Modules

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for 'gcc' executions in user space
- Log compilation in restricted environments

## Related Procedures

- [[procedures/Compile-Malicious-Executable]]

## Related Tools

- [[tools/Python-Scripting]]

## References

- Official documentation: https://gcc.gnu.org/onlinedocs/
