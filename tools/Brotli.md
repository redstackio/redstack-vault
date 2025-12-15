---
id: 123e4567-e89b-12d3-a456-426614174005
url: 'https://github.com/google/brotli'
name: Brotli
tags:
  - compression
  - dos
  - payload-generation
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-04T00:00:00Z'
updated_at: '2025-12-14T17:26:48.701Z'
validated: true
submitted: true
---
# Brotli

**Status**: Unverified

## Overview

Brotli is a lossless compression algorithm and tool developed by Google, used for web content compression. In security testing, it's employed to craft payloads exploiting decompression vulnerabilities, such as in Node.js fetch() DoS scenarios.

## Description

Brotli offers superior compression ratios to gzip, with levels 0-11 for speed vs. size trade-offs. The CLI tool (brotli binary) allows encoding/decoding files or streams, making it ideal for generating malicious compressed data that expands excessively during decoding, leading to resource exhaustion attacks.

## Features

- Feature 1: High compression ratios (up to 26% better than gzip)
- Feature 2: Streaming support for large inputs
- Feature 3: Quality levels for balancing CPU and output size

## Installation

### Requirements

- Build tools (cmake, gcc)
- Git

### Install Commands

```bash
# Clone and build
git clone --recurse-submodules https://github.com/google/brotli.git
cd brotli
mkdir out && cd out
cmake .. -DCMAKE_BUILD_TYPE=Release
make
sudo make install
```

Or via package manager:
```bash
# Ubuntu/Debian
sudo apt install brotli
# macOS
brew install brotli
```

## Basic Usage

```bash
brotli --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-q N, --quality N` | Compression quality (0-11) |
| `-o FILE` | Output file |
| `-d` | Decompress mode |

## Examples

### Example 1: Basic Usage

```bash
brotli input.txt -o input.txt.br
```

### Example 2: Advanced Usage

```bash
cat large_input | brotli -q 11 -o compressed.br -
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Endpoint Denial of Service]]

### Tactics

- [[Impact]]

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of brotli binary or .br files in temp directories
- High CPU usage during compression of large payloads
- Network transfers of .br files in exploit scenarios

## Related Procedures

- [[procedures/Exploit-Brotli-Decoding-DoS-in-Node-js]]

## Related Tools

- [[zlib]]
- [[gzip]]

## References

- Official documentation: https://github.com/google/brotli
- Related resources: HackerOne Report #2284065
