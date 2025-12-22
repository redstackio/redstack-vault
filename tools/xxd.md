---
id: tool-xxd
url: 'https://linux.die.net/man/1/xxd'
tags:
  - hex
  - conversion
type: tool
verified: false
platforms:
  - Linux
  - Unix
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:48.455Z'
validated: true
submitted: true
---
# xxd

**Status**: Unverified

## Overview

xxd is a hexadecimal dump and hex editor utility for creating or reversing hexdumps, useful in security testing for crafting binary payloads from hex strings, such as malformed protocol frames.

## Description
This tool is useful for verifying the structure of crafted binary data, such as AJP payloads in request smuggling attacks, by displaying hexadecimal and ASCII representations.

Part of the vim package, xxd converts between hex text and binary data, essential for preparing exploits like HTTP/2 payloads without custom encoders. In attacks, it's piped to send binary over netcat.

## Features

- Feature 1: Reversible hexdump creation
- Feature 2: Plain style for easy scripting
- Feature 3: Binary output for direct network transmission

## Installation

### Requirements

- Standard Unix-like system

### Install Commands

```bash
# Usually pre-installed; if not
apt install vim-common  # Includes xxd
```

## Basic Usage

```bash
xxd -r -p hex_input > binary_output
```

### Common Options

| Option | Description |
|--------|-------------|
| `-r` | Reverse (hex to binary) |
| `-p` | Plain hexdump style (no offsets) |

## Examples

### Example 1: Basic Usage

```bash
echo '48656c6c6f' | xxd -r -p  # Outputs 'Hello'
```

### Example 2: Advanced Usage

```bash
cat payload.hex | xxd -r -p | nc target 80
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Process calls in scripts sending binary data
- Hex strings in memory or logs

## Related Procedures

### Requirements
- Linux system (typically pre-installed on many distributions)

## Related Tools

- [[Related Tool 1|tools/hexdump]]
- [[Related Tool 2|tools/xxd alternatives like python binascii]]

## References

- Official documentation: man xxd
- Related resources: Vim wiki on xxd
