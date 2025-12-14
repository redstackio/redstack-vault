---
id: tool-rau-crypto
url: 'https://github.com/bao7uo/RAU_crypto'
tags:
  - upload
  - encryption
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:33.118Z'
validated: true
submitted: true
---
# RAU_crypto.py

**Status**: Unverified

## Overview

RAU_crypto.py is a Python script for encrypting and uploading files to Telerik RadAsyncUpload handlers, bypassing version-specific protections to detect and exploit file upload vulnerabilities.

## Description

Designed for offensive security testing against Telerik UI in ASP.NET apps, it generates encryption keys based on Telerik versions, crafts POST requests to the rau endpoint, and handles responses to confirm uploads. Commonly used for CVE-2017-11317 exploitation.

## Features

- Feature 1: Version-based encryption key generation
- Feature 2: File upload simulation to .axd endpoints
- Feature 3: Response parsing for success indicators like fileInfo

## Installation

### Requirements

- Python 3.x
- Requests library (pip install requests)

### Install Commands

```bash
# Clone repo
git clone https://github.com/bao7uo/RAU_crypto
cd RAU_crypto
pip install requests
```

## Basic Usage

```bash
python3 RAU_crypto.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -P | Server path for upload |
| -v | Telerik version (implied) |
| file | Local file to upload |
| url | Target endpoint |

## Examples

### Example 1: Basic Usage

```bash
python3 RAU_crypto.py -P 'C:\Windows\Temp' '2016.2.607' testfile.txt https://target/endpoint
```

### Example 2: Advanced Usage

Integrate in loops for version brute-force.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to .axd with encrypted POST payloads
- Multiple version-specific requests
- Anomalous file uploads in web logs

## Related Procedures


## Related Tools

- [[tools/CVE-2019-18935.py]]

## References

- GitHub repo: https://github.com/bao7uo/RAU_crypto
