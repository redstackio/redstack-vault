---
url: 'https://www.gnu.org/software/coreutils/dd'
tags:
  - data-copy
  - dos
type: tool
verified: false
platforms:
  - Linux
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:56.575Z'
id: 21298b1e-1451-4525-a543-ff81bec8e81c
validated: true
submitted: true
---
# dd

**Status**: Unverified

## Overview

dd is a Unix utility for low-level copying and conversion of data, commonly used in attacks to generate and write large files for resource exhaustion.

## Description

Copies input to output with optional conversions, ideal for filling files with zeros from /dev/zero to consume disk space in container environments.

## Features

- Feature 1: Block-based I/O control
- Feature 2: Infinite input from devices
- Feature 3: Status reporting

## Installation

### Requirements

- Standard on Linux (coreutils)

### Install Commands

```bash
# Usually pre-installed
sudo apt update && sudo apt install coreutils
```

## Basic Usage

```bash
dd --help
```

### Common Options

| Option | Description |
|--------|-------------|
| if= | Input file | 
| of= | Output file |
| bs= | Block size |
| count= | Block count |

## Examples

### Example 1: Basic Usage

```bash
dd if=/dev/zero of=testfile count=10 bs=1M
```

### Example 2: Advanced Usage

```bash
dd if=/dev/zero of=/etc/hosts count=1000000 bs=10M
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[OS Exhaustion Flood]]

### Tactics

- [[Impact]]

## Detection

Indicators and methods for detecting this tool's usage:

- High disk I/O from dd processes
- Sudden file size increases in /etc

## Related Procedures

- [[procedures/Overwrite-Etc-Hosts-with-Dd]]

## Related Tools

- [[tools/fallocate]]

## References

- Man page: man dd
