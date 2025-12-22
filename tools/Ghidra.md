---
id: tool-ghidra
url: 'https://ghidra-sre.org/'
tags:
  - reverse-engineering
  - disassembly
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:41.376Z'
validated: true
submitted: true
---
# Ghidra

**Status**: Unverified

## Overview

Ghidra is a software reverse engineering suite developed by the NSA, used for vulnerability research, malware analysis, and exploit development on binaries like the 3DS Swapnote app.

## Description

Ghidra supports disassembly, decompilation, and scripting for various architectures including ARM (used in 3DS). It's ideal for analyzing embedded apps to find memory safety issues like heap overflows in parsers.

## Features

- Feature 1: Multi-platform binary analysis with ARM Thumb support
- Feature 2: Automated function identification and cross-references
- Feature 3: Scripting in Java/Python for custom analysis

## Installation

### Requirements

- Java 17+ runtime
- 8GB+ RAM for large binaries

### Install Commands

```bash
# Download and extract from official site
wget https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_10.4_build/ghidra_10.4_PUBLIC_20230818.zip
unzip ghidra_10.4_PUBLIC_20230818.zip
cd ghidra_10.4_PUBLIC
./ghidraRun
```

## Basic Usage

```bash
tool-name --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-import` | Import binary file |

## Examples

### Example 1: Basic Usage

Launch Ghidra and import the Swapnote binary for disassembly.

### Example 2: Advanced Usage

```bash
# Script to find memcpy calls
ghidraRun -scriptPath /path/to/scripts -postScript FindMemcpy.py
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for ghidraRun.exe
- Network traffic to Ghidra update servers

## Related Procedures


## Related Tools

- [[IDA-Pro]]
- [[Radare2]]

## References

- Official documentation: https://ghidra-sre.org/
- Related resources: NSA GitHub repo
