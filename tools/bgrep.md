---
id: d6901f30-1c68-44a9-9113-5fabb08039b9
type: tool
verified: true
created_at: '2019-08-28T21:17:19.216326+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
tags:
  - binary-analysis
  - reverse-engineering
  - malware-analysis
url: 'https://github.com/mborgerding/bgrep'
validated: true
---

# bgrep

**Status**: Unverified

## Overview

bgrep is a binary grep tool designed for searching patterns, strings, and byte sequences in binary files. It's particularly useful in security testing for malware analysis, reverse engineering, and forensic investigations where traditional text-based grep falls short on non-text data like executables, memory dumps, or firmware images.

## Description

bgrep extends the grep utility to handle binary data efficiently, supporting string searches, hex pattern matching, and case-insensitive options. It outputs match locations with offsets, making it easier to locate interesting artifacts such as embedded credentials, API calls, or malicious payloads in binaries. Commonly used in offensive security for analyzing captured binaries during post-exploitation or in defensive scenarios for threat hunting.

## Features

- Feature 1: String and regex pattern matching in binaries
- Feature 2: Hexadecimal byte sequence searches
- Feature 3: Case-insensitive and inverted matching options
- Feature 4: Output formatting with offsets for precise location
- Feature 5: Support for large files and streams

## Installation

### Requirements

- Go 1.16+ (if building from source)
- Standard Unix tools (grep, etc., for comparison)

### Install Commands

```bash
# From source (recommended)
go install github.com/mborgerding/bgrep@latest

# Or download pre-built binary from releases
wget https://github.com/mborgerding/bgrep/releases/download/v1.0.0/bgrep-linux-amd64
chmod +x bgrep-linux-amd64
sudo mv bgrep-linux-amd64 /usr/local/bin/bgrep

# On Kali/Debian (if packaged)
sudo apt update && sudo apt install bgrep
```

## Basic Usage

```bash
bgrep --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-i` | Case-insensitive search |
| `-x` | Hex pattern mode |
| `-c` | Count matches only |
| `-o` | Output file for matches |

## Examples

### Example 1: Basic Usage

Search for a string in a binary:

```bash
bgrep "password" malware.bin
```

### Example 2: Advanced Usage

Hex search for NOP sled:

```bash
bgrep -x "90 90 90" shellcode.bin
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Obfuscated Files or Information]] Obfuscated Files or Information (for analyzing hidden patterns)
- [[File and Directory Discovery]] File and Directory Discovery (binary content inspection)

### Tactics

- [[Discovery]] Discovery
- [[Command and Control]] Command and Control

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Process monitoring for bgrep executions in analysis environments
- Detection method 2: File system scans for bgrep binaries in non-standard locations
- Detection method 3: Network logs if used with piped data from remote sources

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[strings]]
- [[tools/xxd]]
- [[tools/binwalk]]

## References

- Official GitHub: https://github.com/mborgerding/bgrep
- Man page: bgrep(1)
