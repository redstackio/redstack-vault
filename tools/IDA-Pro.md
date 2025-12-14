---
url: 'https://hex-rays.com/ida-pro/'
tags:
  - reverse-engineering
  - disassembly
type: tool
verified: false
platforms:
  - Windows
  - Linux
  - macOS
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T05:32:10.348Z'
id: aa9627dd-79f7-4643-8393-1848c500f52d
validated: true
submitted: true
---
# IDA-Pro

**Status**: Unverified

## Overview

IDA Pro is a powerful interactive disassembler and debugger used for reverse engineering binaries, particularly in vulnerability analysis like examining GoldSource Engine functions.

## Description

IDA Pro enables static and dynamic analysis of executables, generating pseudocode and graphs for functions like CL_CheckFile. In this context, it was used to analyze build 7960 of the GoldSource Engine, revealing validation weaknesses. Common in offensive security for exploit development.

## Features

- Feature 1: Interactive disassembly with control flow graphs
- Feature 2: Decompiler to pseudocode (Hex-Rays plugin)
- Feature 3: Debugger integration for runtime analysis

## Installation

### Requirements

- 64-bit OS (Windows/Linux/macOS)
- Sufficient RAM (8GB+ recommended)

### Install Commands

```bash
# Download from official site; no direct install command, run setup executable
# Example for Linux: Extract and run ida64
./ida64
```

## Basic Usage

```bash
ida64 -B target.exe
```

### Common Options

| Option | Description |
|--------|-------------|
| -B | Batch mode for scripting |
| -A | Analysis options |
| -Sscript.hexrays | Load decompiler script |

## Examples

### Example 1: Basic Usage

```bash
ida64 client.dll
```

> Opens client.dll for disassembly; navigate to CL_CheckFile.

### Example 2: Advanced Usage

```bash
ida64 -A -Sanalyze.pseudocode.exe goldsource.exe
```

> Automates analysis to generate pseudocode for vulnerability spotting.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution (via RE)

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Process: ida.exe or ida64 running
- Network: No outbound, but file access to binaries
- Artifacts: .idb database files in working directories

## Related Procedures


## Related Tools

- [[tools/Ghidra]]
- [[tools/Radare2]]

## References

- Official documentation: https://hex-rays.com/ida-pro/
- Related resources: Reverse engineering tutorials for game engines
