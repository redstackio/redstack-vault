---
url: null
tags:
  - hex-dump
  - payload-verification
type: tool
platforms:
  - Linux
description: A hex dumping utility for viewing binary file contents.
id: 1af7275a-777c-4092-aa4d-a09ffdb27b07
created_at: '2025-12-13T09:01:21.817Z'
updated_at: '2025-12-13T09:01:21.817Z'
verified: false
validated: true
submitted: true
---
# xxd

**Status**: Unverified

## Overview
xxd is a command-line tool that creates a hex dump of a given file or standard input, commonly used in security testing to inspect binary payloads for exploits.

## Description
This tool is useful for verifying the structure of crafted binary data, such as AJP payloads in request smuggling attacks, by displaying hexadecimal and ASCII representations.

## Features
- Hexadecimal dumping
- ASCII side-by-side view
- Reverse dumping capability

## Installation

### Requirements
- Linux system (typically pre-installed on many distributions)

### Install Commands

```bash
sudo apt install vim-common  # If not installed
```

## Basic Usage

```bash
xxd --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-p` | Plain hex output |

## Examples

### Example 1: Basic Usage

```bash
xxd data2
```

### Example 2: Advanced Usage

```bash
xxd -p data2
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques
- [[Exploit Public-Facing Application]]

### Tactics
- [[Initial Access]]

## Detection
Indicators and methods for detecting this tool's usage:
- Command execution logs showing xxd usage
- File access patterns for binary files

## Related Procedures
```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

## References
- Man page: xxd(1)
