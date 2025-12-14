---
url: 'https://pmt.sourceforge.net/pngcrush'
tags:
  - image-optimization
  - png
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:37.357Z'
id: 03b245e5-8a57-4d21-a1d1-b38227d02f1e
validated: true
submitted: true
---
# pngcrush

**Status**: Unverified

## Overview

pngcrush is a command-line utility for optimizing PNG images by recompressing data and removing unnecessary chunks, commonly used in web and image processing workflows. In security testing, it's exploited here for its double-free vulnerability in sPLT chunk handling.

## Description

The tool reads PNG files, applies various compression methods, and writes optimized output. Versions prior to 1.7.87 suffer from a double-free in png_free_data when freeing sPLT chunk memory, leading to crashes. It's typically used offline but can be integrated into services for batch processing.

## Features

- Feature 1: Multiple compression trials with -brute option
- Feature 2: Chunk reduction with -reduce to minimize file size
- Feature 3: Support for various PNG chunks including sPLT (palette suggestions)

## Installation

### Requirements

- Linux or compatible OS
- C compiler for building from source

### Install Commands

```bash
# Download and build from source
wget https://prdownloads.sourceforge.net/pmt/pngcrush-1.7.86.tar.gz
# For vulnerable version <1.7.87; extract and ./configure && make && sudo make install
```

## Basic Usage

```bash
pngcrush --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-reduce` | Reduce ancillary chunks |
| `-brute` | Brute-force compression methods |

## Examples

### Example 1: Basic Usage

```bash
pngcrush input.png output.png
```

### Example 2: Advanced Usage

```bash
pngcrush -reduce -brute input.png /dev/null
```

(Triggers vuln with sPLT input, discards output.)

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Endpoint Denial of Service]]

### Tactics

- [[Privilege Escalation]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for pngcrush executions
- Log segfaults in image processing services
- Scan for vulnerable versions via package managers

## Related Procedures

- [[procedures/Trigger-Double-Free-Crash-in-pngcrush]]

## Related Tools

- [[tools/Valgrind]]
- [[tools/GDB]]

## References

- Official documentation: https://pmt.sourceforge.net/pngcrush
- CVE-2015-7700 report
