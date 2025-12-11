---
url: null
tags:
  - exploit
  - file-download
type: tool
platforms:
  - Linux
description: >-
  Python script to exploit CVE-2019-11510 for arbitrary file downloads from
  Pulse Secure VPN.
id: 92a27757-98b1-4255-8983-b72627ea815b
created_at: '2025-12-11T06:10:40.261Z'
updated_at: '2025-12-11T06:10:40.261Z'
verified: false
validated: true
submitted: true
---
# download.py

**Status**: Unverified

## Overview

A custom Python script designed to exploit the pre-auth arbitrary file reading vulnerability (CVE-2019-11510) in Pulse Secure SSL VPN, allowing download of sensitive files.

## Description

This tool automates the process of sending crafted requests to the VPN endpoint to read and retrieve arbitrary files without authentication, commonly used in reconnaissance and data exfiltration.

## Features

- Targets specific file paths
- Handles VPN-specific request formats
- Saves downloaded files locally

## Installation

### Requirements

- Python 3.x
- Requests library

### Install Commands

```bash
pip install requests
```

## Basic Usage

```bash
download.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `--target` | VPN URL |
| `--path` | File path to download |

## Examples

### Example 1: Basic Usage

```bash
download.py --target https://vpn.target.com --path /etc/passwd
```

### Example 2: Advanced Usage

```bash
download.py --target https://vpn.target.com --path /data/runtime/mtmp/system --output system.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual access patterns to VPN endpoints
- Logs showing file read attempts without auth

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[curl]]

## References

- CVE-2019-11510 details
