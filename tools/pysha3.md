---
id: tool-uuid-3
url: 'https://pypi.org/project/pysha3/'
tags:
  - crypto
  - library
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:56.316Z'
validated: true
submitted: true
---
# pysha3

**Status**: Unverified

## Overview

pysha3 is a Python library implementing SHA3 hashing algorithms, used in the RSKJ DoS PoC to generate the malformed RLP-encoded data for the UDP packet payload.

## Description

Provides Keccak-based SHA3 functions (224, 256, 384, 512) for cryptographic operations; in this exploit, aids in crafting RLP with specific byte patterns triggering the negative length return in bytesToLength.

## Features

- Feature 1: SHA3-256 hashing for data integrity
- Feature 2: Pure Python implementation, no C dependencies
- Feature 3: Compatible with Python 3.x

## Installation

### Requirements

- Python 3 and pip

### Install Commands

```bash
pip install pysha3
```

## Basic Usage

```bash
python3 -c "from pysha3 import sha3_256; print(sha3_256(b'test').hexdigest())"
```

### Common Options

N/A (library, used via import)

## Examples

### Example 1: Basic Usage

```bash
import pysha3
hash_obj = pysha3.sha3_256()
hash_obj.update(b'malformed_rlp')
print(hash_obj.hexdigest())
```

### Example 2: Advanced Usage

```bash
from pysha3 import sha3_512
# Use in PoC for longer hashes if needed
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Obfuscated Files or Information]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Package manager logs showing pysha3 install
- Python scripts importing sha3 in exploit contexts
- Unusual hash computations in network tools

## Related Procedures


## Related Tools

- [[tools/Python-3]]

## References

- PyPI: https://pypi.org/project/pysha3/
