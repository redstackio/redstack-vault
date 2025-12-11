---
url: null
tags:
  - arbitrary-file-read
  - vpn-exploit
type: tool
platforms:
  - Linux
description: >-
  Python script for exploiting CVE-2019-11510 to download arbitrary files from
  Pulse Secure VPN.
id: 381d4d95-87df-4880-ac76-b574d5e0dcda
created_at: '2025-12-11T03:47:59.563Z'
updated_at: '2025-12-11T03:47:59.563Z'
verified: false
validated: true
submitted: true
---
# download.py

**Status**: Unverified

## Overview

A custom Python script designed to exploit the pre-auth arbitrary file reading vulnerability (CVE-2019-11510) in Pulse Secure SSL VPN, allowing unauthenticated file downloads.

## Description

The tool sends crafted requests to vulnerable endpoints to retrieve files like /etc/passwd or session databases, commonly used in initial access phases of VPN attacks.

## Features

- Target specification via URL
- File path input for arbitrary reads
- Automated exploitation without authentication

## Installation

### Requirements

- Python 3.x
- Requests library

### Install Commands

```bash
pip install requests
# Assume script is manually created or downloaded
```

## Basic Usage

```bash
download.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `--target` | VPN URL |
| `--file` | Path to download |

## Examples

### Example 1: Basic Usage

```bash
download.py --target https://vpn.target.com --file /etc/passwd
```

### Example 2: Advanced Usage

```bash
download.py --target https://vpn.target.com --file /data/runtime/mtmp/system
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for suspicious GET requests to VPN endpoints
- Log anomalous file access patterns

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- #grep

## References

- CVE-2019-11510 details
