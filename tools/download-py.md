---
id: tool-uuid-1
url: null
tags:
  - exploit
  - file-read
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.971Z'
validated: true
submitted: true
---
# download-py

**Status**: Unverified

## Overview

Custom Python script to exploit CVE-2019-11510 in Pulse Secure SSL VPN for pre-auth arbitrary file downloads.

## Description

The tool sends HTTP requests to the vulnerable /dana-na/auth/welcome.htm endpoint with traversal payloads to read and download files like /etc/passwd without authentication. Used in offensive security for VPN reconnaissance and credential theft.

## Features

- Feature 1: Directory traversal for arbitrary file paths
- Feature 2: Supports multiple file downloads in batch
- Feature 3: Handles HTTPS and session-less requests

## Installation

### Requirements

- Python 3.x
- requests library

### Install Commands

```bash
pip install requests
# Clone or create download.py script
```

## Basic Usage

```bash
python download.py https://target-vpn.com /etc/passwd output.txt
```

### Common Options

| Option | Description |
|--------|-------------|
| `-u, --url` | Target VPN URL |
| `-f, --file` | File path to read |
| `-o, --output` | Local output file |

## Examples

### Example 1: Basic Usage

```bash
python download.py https://vpn.example.com /etc/passwd passwd.txt
```

### Example 2: Advanced Usage

```bash
python download.py https://vpn.example.com /data/runtime/mtmp/system mtmp.txt --batch files.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Anomalous GET requests to /dana-na/auth/welcome.htm with ../ paths
- Increased file access logs on VPN server

## Related Procedures


## Related Tools

- [[tools/GPU-Hash-Cracking-Tool]]

## References

- CVE-2019-11510 advisory
