---
id: tool-od
url: 'https://man7.org/linux/man-pages/man1/od.1.html'
tags:
  - file-analysis
  - binary-inspection
type: tool
verified: false
platforms:
  - Linux
  - Unix
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:37.406Z'
validated: true
submitted: true
---
# od

**Status**: Unverified

## Overview

od (octal dump) is a standard Unix utility for displaying file contents in various formats, including hexadecimal, ideal for reverse engineering binary files like malicious LZMA streams in security analysis.

## Description

Commonly used in offensive security for inspecting crafted inputs without execution, od helps identify anomalies in compression formats that lead to vulnerabilities like memory exhaustion in libxml2.

## Features

- Feature 1: Multiple output formats (octal, decimal, hex, ASCII).
- Feature 2: Address offsetting and byte grouping control.
- Feature 3: Non-destructive file reading for safe analysis.

## Installation

### Requirements

- Standard on most Linux distributions.

### Install Commands

```bash
# Already installed; if not, via coreutils
sudo apt install coreutils  # Debian/Ubuntu
```

## Basic Usage

```bash
od --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-t x1` | Hex output, one byte per line |
| `-A o` | Octal addresses |
| `-v` | No identical line suppression |

## Examples

### Example 1: Basic Usage

```bash
od -tx1 malicious.lzma
```

### Example 2: Advanced Usage

```bash
od -tx1 -v ./test000 | less
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service (for analysis)

### Tactics

- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for od executions on suspicious files.
- Log file access patterns in forensics.

## Related Procedures

- [[procedures/Inspect-Malicious-LZMA-File]]

## Related Tools

- [[xxd]]
- [[hexdump]]

## References

- Official man page: https://man7.org/linux/man-pages/man1/od.1.html
