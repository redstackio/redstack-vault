---
id: tool-ida-pro
url: 'https://www.hex-rays.com/ida-pro/'
tags:
  - disassembly
  - reverse-engineering
type: tool
verified: false
platforms:
  - Windows
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:08.873Z'
validated: true
submitted: true
---
# IDA-Pro

**Status**: Verified

## Overview

IDA Pro is a powerful interactive disassembler used to analyze and confirm vulnerabilities in binaries, such as added bounds checks in patched Source Engine releases or initial vuln discovery.

## Description

It decompiles and disassembles game client binaries to inspect network handlers, verifying OOB read patterns and post-patch fixes like upper bound comparisons.

## Features

- Feature 1: Interactive disassembly and graphing
- Feature 2: Hex-Rays decompiler
- Feature 3: Binary patching and scripting

## Installation

### Requirements

- License key

### Install Commands

```bash
# Commercial download from hex-rays.com
```

## Basic Usage

```bash
ida64.exe client.dll
```

### Common Options

| Option | Description |
|--------|-------------|
| -h | Help |
| -A | Analysis mode |

## Examples

### Example 1: Basic Usage

```bash
ida64.exe -A csgo.exe
```

### Example 2: Advanced Usage

```bash
ida64.exe -Sscript.idc target.dll
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1583.001]] Acquire Infrastructure: Domains (adapted to RE)

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Rarely detected; monitor for binary analysis tools in forensics

## Related Procedures


## Related Tools


## References

- Official: https://www.hex-rays.com/ida-pro/
