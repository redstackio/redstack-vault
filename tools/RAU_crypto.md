---
url: 'https://github.com/bao7uo/RAU_crypto'
tags:
  - exploit
  - crypto
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:37.406Z'
id: a491ee14-e38d-4555-aefb-f2185295cca6
validated: true
submitted: true
---
# RAU_crypto

**Status**: Unverified

## Overview

RAU_crypto is a Python tool for encrypting payloads to bypass Telerik RadAsyncUpload handler protections in vulnerable versions.

## Description

It generates version-specific encryption for file uploads, enabling success detection during brute-forcing. Used in CVE-2019-18935 reconnaissance to identify exploitable configurations.

## Features

- Feature 1: Version-based encryption
- Feature 2: File upload simulation
- Feature 3: JSON response parsing

## Installation

### Requirements

- Python 3
- Git

### Install Commands

```bash
# Clone repo
git clone https://github.com/bao7uo/RAU_crypto
cd RAU_crypto
pip install -r requirements.txt
```

## Basic Usage

```bash
python3 RAU_crypto.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-P` | Password for encryption | 
| Version | Target Telerik version |
| File | Input file to encrypt |
| URL | Target endpoint |

## Examples

### Example 1: Basic Usage

```bash
python3 RAU_crypto.py -P 'pass' '2017.2.621' test.txt https://target/rau
```

### Example 2: Advanced Usage

```bash
python3 RAU_crypto.py -P 'pass' '2017.2.621' --output encrypted.bin test.txt URL
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Obfuscated Files or Information]] Obfuscated Files or Information

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Python processes accessing .axd endpoints
- Encrypted payloads in upload requests
- Version-specific traffic patterns

## Related Procedures

- [[procedures/Identify-Vulnerable-Telerik-Version]]

## Related Tools

- [[tools/CVE-2019-18935.py]]

## References

- GitHub repo: https://github.com/bao7uo/RAU_crypto
