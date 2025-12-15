---
id: tool-uuid-1
url: 'https://github.com/bao7uo/dp_crypto'
tags:
  - brute-force
  - telerik
  - crypto
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:28.464Z'
validated: true
submitted: true
---
# dp-crypto

**Status**: Unverified

## Overview

dp_crypto is a Python-based tool designed for brute-forcing weak ASP.NET machine keys in Telerik DialogHandler endpoints, specifically targeting CVE-2017-9248 to enable access to protected resources like DNN file managers in web applications.

## Description

This script automates the enumeration and prediction of machine keys using specified lengths, character sets, and threading. It's commonly used in penetration testing against unpatched Telerik/DNN setups, outputting keys and encoded links for further exploitation like file uploads.

## Features

- Feature 1: Multi-threaded brute-forcing for speed
- Feature 2: Support for ASCII and custom charsets
- Feature 3: Automatic generation of base64-encoded access links

## Installation

### Requirements

- Python 3.x
- requests library (pip install requests)

### Install Commands

```bash
# Clone the repository
git clone https://github.com/bao7uo/dp_crypto
cd dp_crypto
pip install -r requirements.txt  # If requirements exist
```

## Basic Usage

```bash
python dp_crypto.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-k, --key-url` | Target DialogHandler URL |
| `--length` | Key length (default 88) |
| `--charset` | Character set (all, hex, etc.) |
| `--threads` | Number of parallel threads |

## Examples

### Example 1: Basic Usage

```bash
python dp_crypto.py -k https://target/DialogHandler.aspx 88 all 21
```

### Example 2: Advanced Usage

```bash
python dp_crypto.py -k https://target/DialogHandler.aspx 128 all 10
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Brute Force]]
- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- High volume of HTTP requests to DialogHandler paths
- Python process with network activity to target ports 80/443
- Anomalous base64 patterns in request payloads

## Related Procedures

- [[procedures/Brute-Force-ASP-NET-Machine-Key-Using-dp-crypto]]

## Related Tools


## References

- GitHub Repository: https://github.com/bao7uo/dp_crypto
- CVE-2017-9248 Details: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-9248
