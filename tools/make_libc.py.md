---
id: tool-make-libc-py
url: null
tags:
  - exploit-generation
  - library-hijacking
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:20.718Z'
validated: true
submitted: true
---
# make_libc.py

**Status**: Unverified

## Overview

Python script to generate a malicious libc.so.6 library for the Snapcraft dynamic linker hijacking exploit.

## Description

This custom tool crafts a shared library that intercepts dlopen calls or executes payloads when loaded, enabling RCE in the snap environment. Used to populate the 'tls' directory in POC archives.

## Features

- Feature 1: Generate fake ELF shared library
- Feature 2: Embed RCE payload (e.g., shell commands)
- Feature 3: Mimic legitimate libc for evasion

## Installation

### Requirements

- Python 3
- Libraries like ctypes for ELF manipulation

### Install Commands

```bash
# Download script from POC source
python3 make_libc.py --help
```

## Basic Usage

```bash
python3 make_libc.py
```

### Common Options

| Option | Description |
|--------|-------------|
| --payload | Specify shell payload |
| --output | Output file (libc.so.6) |

## Examples

### Example 1: Basic Usage

```bash
python3 make_libc.py --payload "echo pwned"
```

### Example 2: Advanced Usage

```bash
python3 make_libc.py --output tls/libc.so.6 --payload "bash -i"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Dynamic Linker Hijacking]] Dynamic Linker Search Order Hijacking

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Scan for non-standard ELF files in cwd
- Monitor python executions generating .so files

## Related Procedures

- [[procedures/Prepare-Malicious-Directory-for-Snap-RCE]]

## Related Tools

- [[tools/tar]]

## References

- POC-specific; see HackerOne report
