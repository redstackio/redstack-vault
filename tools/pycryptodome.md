---
url: 'https://pycryptodome.readthedocs.io/'
tags:
  - crypto
  - python-library
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.817Z'
id: 84cbd516-a1e0-4a46-b402-ecec0b096419
validated: true
submitted: true
---
# pycryptodome

**Status**: Unverified

## Overview

PyCryptodome is a Python library providing low-level cryptographic primitives, commonly used in security testing for handling encryption in exploits like Telerik file uploads.

## Description

It replaces the older PyCrypto and supports AES, RSA, and other algorithms essential for decoding Telerik's RadAsyncUpload encryption. In offensive operations, it's used to craft payloads for deserialization attacks, ensuring compatibility with .NET serialization formats.

## Features

- Feature 1: Comprehensive cipher implementations (AES, DES, etc.) for payload encryption
- Feature 2: Hashing and MAC functions for integrity in exploits
- Feature 3: Padding and encoding utilities for binary data handling in web uploads

## Installation

### Requirements

- Python 3.5+
- pip3

### Install Commands

```bash
pip3 install pycryptodome
```

## Basic Usage

```bash
from Crypto.Cipher import AES
cipher = AES.new(key, AES.MODE_CBC)
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Library imported via Python; no CLI options |

## Examples

### Example 1: Basic Usage

```bash
python3 -c "from Crypto.Cipher import AES; print('Installed')"
```

### Example 2: Advanced Usage

In exploit script: Use for decrypting Telerik keys before crafting serialized payloads.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Obfuscated Files or Information]]
- [[Deobfuscate-Decode Files or Information]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Python environment scans for pycryptodome imports in scripts
- Network logs of pip installs from untrusted sources

## Related Procedures

- [[procedures/Prepare-Telerik-Deserialization-Exploit]]

## Related Tools

- [[tools/telerik-deserialization-exploit]]

## References

- Official documentation: https://pycryptodome.readthedocs.io/
- PyPI: https://pypi.org/project/pycryptodome/
