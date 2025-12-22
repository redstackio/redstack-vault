---
url: 'https://github.com/github/cmark-gfm'
tags:
  - markdown
  - parser
  - dos
type: tool
verified: false
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.258Z'
id: de529af8-6ee6-4232-8f73-a69153df0ddf
validated: true
submitted: true
---
# cmark-gfm

**Status**: Unverified

## Overview

cmark-gfm is GitHub's fork of the CommonMark markdown parsing library in C, used for rendering markdown content. Vulnerable versions prior to 0.29.0.gfm.6 suffer from polynomial time complexity in the autolink extension, enabling DoS attacks.

## Description

This library processes markdown inputs into HTML, with extensions like autolink for automatic URL detection. The vulnerability allows crafted inputs with repeated patterns to cause excessive computation, leading to resource exhaustion. Commonly used in services like GitHub's markdown API.

## Features

- Feature 1: CommonMark spec-compliant parsing
- Feature 2: GitHub Flavored Markdown (GFM) extensions including autolink
- Feature 3: Fast C implementation for high-performance rendering

## Installation

### Requirements

- C compiler (gcc/clang)
- CMake

### Install Commands

```bash
# Clone and build
mkdir cmark-gfm && cd cmark-gfm
git clone https://github.com/github/cmark-gfm.git .
cmake .
make
sudo make install
```

## Basic Usage

```bash
cmark-gfm --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-e, --extension` | Enable extension (e.g., autolink) |
| `-t, --to` | Output format (html, commonmark) |
| `-s, --standalone` | Include full document |

## Examples

### Example 1: Basic Usage

```bash
echo "Hello, world!" | cmark-gfm
```

### Example 2: Advanced Usage

```bash
cat input.md | cmark-gfm -e autolink -t html
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[OS Exhaustion Flood]]

### Tactics

- [[Impact]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for cmark-gfm processes with high CPU
- Log input sizes to parsing binaries
- Detect repeated pattern inputs

## Related Procedures

- [[procedures/Verify-Vulnerability-in-cmark-gfm-Locally]]

## Related Tools

- [[tools/python3]]

## References

- Official documentation: https://github.com/github/cmark-gfm
- Vulnerability details: https://hackerone.com/reports/1619604
