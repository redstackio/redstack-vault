---
url: 'https://visualstudio.microsoft.com/vs/older-downloads/'
tags:
  - development
  - compilation
type: tool
verified: false
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:48.890Z'
id: 7230aa3e-d28e-443f-ba71-30446aca59ef
validated: true
submitted: true
---
# Visual Studio 2017

**Status**: Unverified

## Overview

Visual Studio 2017 is an integrated development environment (IDE) from Microsoft used for compiling C++ applications, including proof-of-concept exploits for vulnerabilities like memory leaks in Windows DLLs.

## Description

This tool supports building Windows executables targeting x64 architecture, essential for compiling PoCs that interact with system DLLs such as OCUtil_x64.dll. It includes debuggers and linkers for verifying code that uses Windows APIs like LoadLibrary and GetProcAddress. Commonly used in offensive security for creating custom exploits.

## Features

- Feature 1: C++ compiler with MSVC toolchain for native Windows binaries
- Feature 2: Integrated debugger for stepping through memory allocation code
- Feature 3: Project templates for console applications and DLL integration

## Installation

### Requirements

- Windows 7 or later
- 4 GB RAM minimum

### Install Commands

Download from the official site and run the installer; select "Desktop development with C++" workload.

```bash
# No CLI install; use GUI installer
```

## Basic Usage

```bash
# Launch via Start Menu: Visual Studio 2017
```

### Common Options

| Option | Description |
|--------|-------------|
| Build > Build Solution | Compiles the project (Ctrl+Shift+B) |
| Debug > Start Debugging | Runs with breakpoints (F5) |

## Examples

### Example 1: Basic Usage

Open .sln file and build to generate .exe.

### Example 2: Advanced Usage

Configure for x64: Project Properties > Configuration Manager > Active solution platform: x64.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Endpoint Denial of Service]]

### Tactics

- [[Impact]]

## Detection

Indicators and methods for detecting this tool's usage:

- Visual Studio processes running during non-development activities
- Compiled binaries in temp directories

## Related Procedures


## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- Official documentation: https://docs.microsoft.com/en-us/visualstudio/
- Related resources: MSDN C++ guides
