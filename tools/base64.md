---
url: ''
tags:
  - encoding
type: tool
platforms:
  - Linux
  - macOS
description: 'Utility for encoding and decoding base64 data, used for preparing payloads.'
id: f64cdcf7-e4e4-400c-aa88-da3ed9a665a2
created_at: '2025-12-11T03:47:39.211Z'
updated_at: '2025-12-11T03:47:39.211Z'
verified: false
validated: true
submitted: true
---
# base64

**Status**: Unverified

## Overview

base64 is a command-line utility for encoding binary data to base64 format, commonly used in security to prepare encoded payloads for web exploits.

## Description

It converts files or input to base64 strings, essential for including data in URL-encoded parameters without corruption.

## Features

- Feature 1: Encode/decode modes
- Feature 2: Wrap control
- Feature 3: Standard compliance

## Installation

### Requirements

- Included in coreutils on Linux/macOS

### Install Commands

```bash
# Usually pre-installed
```

## Basic Usage

```bash
base64 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-d` | Decode mode |
| `-w` | Wrap encoded lines |

## Examples

### Example 1: Basic Usage

```bash
base64 file.txt
```

### Example 2: Advanced Usage

```bash
base64 -w 0 file.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Valid Accounts]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor shell commands for base64 usage
- Detection method 2: Check for base64 in payloads

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- #openssl
- #xxd

## References

- Official documentation: GNU coreutils
- Related resources: Man base64
