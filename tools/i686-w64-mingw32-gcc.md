---
url: 'https://www.mingw-w64.org/'
tags:
  - compilation
  - cross-compile
type: tool
platforms:
  - Linux
  - Windows
description: >-
  MinGW-w64 cross-compiler for generating 32-bit Windows executables from C
  source on Linux or other non-Windows platforms.
id: 63998e37-562f-4fa6-aac0-ce2e97bce352
created_at: '2025-12-14T17:26:17.511Z'
updated_at: '2025-12-14T17:26:17.511Z'
verified: false
validated: true
submitted: true
---
# i686-w64-mingw32-gcc

**Status**: Unverified

## Overview

i686-w64-mingw32-gcc is a GNU Compiler Collection (GCC) variant for cross-compiling 32-bit Windows applications from Linux or macOS, commonly used in security testing to build payloads without a Windows environment.

## Description

This tool enables creation of Windows PE executables from C/C++ source, supporting static linking for standalone binaries. In offensive security, it's used to develop proof-of-concept exploits like the adduser.exe for service hijacking, ensuring compatibility with Windows service contexts.

## Features

- Feature 1: Cross-compilation to i686 (32-bit x86) Windows targets
- Feature 2: Support for Windows API calls (e.g., system() for net commands)
- Feature 3: Static linking to avoid DLL dependencies

## Installation

### Requirements

- Linux or macOS host
- GCC and binutils installed

### Install Commands

```bash
# On Ubuntu/Debian
sudo apt update && sudo apt install mingw-w64
```

## Basic Usage

```bash
i686-w64-mingw32-gcc --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -o | Specify output file |
| -static | Link statically |
| -Wall | Enable warnings |

## Examples

### Example 1: Basic Usage

```bash
i686-w64-mingw32-gcc adduser.c -o adduser.exe
```

### Example 2: Advanced Usage

```bash
i686-w64-mingw32-gcc -static -O2 adduser.c -o adduser.exe
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Develop Capabilities]] Develop Capabilities
- [[Remote File Copy]] Ingress Tool Transfer

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of MinGW binaries in build environments
- Compiled EXEs with MinGW signatures (check with strings or PEiD)
- Network downloads of mingw-w64 packages

## Related Procedures

- [[procedures/Compile-and-Place-Malicious-Executable-for-Path-Hijacking]]

## Related Tools

- [[GCC]]
- [[Visual Studio]]

## References

- Official documentation: https://gcc.gnu.org/onlinedocs/
- MinGW-w64 project
