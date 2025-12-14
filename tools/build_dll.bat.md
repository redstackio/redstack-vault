---
id: tool-build-dll
url: >-
  https://labs.bishopfox.com/tech-blog/cve-2019-18935-remote-code-execution-in-telerik-ui
tags:
  - compilation
  - gadget
type: tool
verified: false
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:33.100Z'
validated: true
submitted: true
---
# build_dll.bat

**Status**: Unverified

## Overview

build_dll.bat is a Windows batch script for compiling C# DLL gadgets used in .NET deserialization attacks against Telerik UI, facilitating RCE payloads like sleep or reverse shells.

## Description

Sourced from BishopFox research, this script automates building deserialization chains with Visual Studio, targeting vulnerabilities like CVE-2019-18935. It compiles source into executable DLLs for upload and execution in web app contexts.

## Features

- Feature 1: Automated C# compilation to DLL
- Feature 2: Support for gadget chains (sleep, shell)
- Feature 3: Integration with VS build environment

## Installation

### Requirements

- Visual Studio with .NET Framework
- Windows OS

### Install Commands

```bash
# Download from BishopFox article
# Place in project dir with C# sources
# Run in VS Developer Command Prompt
```

## Basic Usage

```batch
build_dll.bat
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A (batch script) | Modify source files for custom payloads |

## Examples

### Example 1: Basic Usage

```batch
build_dll.bat
```

### Example 2: Advanced Usage

Edit C# for reverse shell before running.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[PowerShell]] PowerShell (.NET equiv)

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Local compilation artifacts (DLLs)
- VS build logs
- Not directly detectable on target

## Related Procedures


## Related Tools

- [[tools/Visual-Studio]]

## References

- BishopFox article: https://labs.bishopfox.com/tech-blog/cve-2019-18935-remote-code-execution-in-telerik-ui
