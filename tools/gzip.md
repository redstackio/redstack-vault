---
id: a5257bbf-cc0d-46f1-af6d-b2c8a3e14bf8
name: gzip
type: tool
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:42.076Z'
platforms:
  - Linux
  - macOS
tags:
  - compression
url: null
validated: true
submitted: true
---

# gzip

**Status**: Unverified

## Overview

Gzip is a compression tool for reducing data size, used in exploit development to fit large payloads into constrained fields like ViewState.

## Description

Processes stdin to stdout for piping in command chains, compressing binary or text data before encoding.

## Features

- Feature 1: Fast deflate compression
- Feature 2: Streaming via stdin/stdout
- Feature 3: Standard in Unix environments

## Installation

### Requirements

- Coreutils (pre-installed on most systems)

### Install Commands

```bash
# Pre-installed; via apt on Debian
sudo apt install gzip
```

## Basic Usage

```bash
gzip --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-` | Use stdin/stdout |
| `-d` | Decompress |
| `-h, --help` | Help |

## Examples

### Example 1: Basic Usage

```bash
echo "data" | gzip -
```

### Example 2: Advanced Usage

```bash
cat file | gzip - | base64
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Obfuscated Files or Information]]

### Tactics

- [[Defense Evasion]]

## Detection

Indicators and methods for detecting this tool's usage:

- Processes in encoding pipelines
- Compressed payloads in requests

## Related Procedures

- [[procedures/Generate-Malicious-Deserialization-Payload-with-ysoserial]]

## Related Tools

- [[tools/base64]]

## References

- Man page: man gzip
