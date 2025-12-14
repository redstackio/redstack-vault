---
url: 'https://pypi.org/project/bcrypt/'
tags:
  - hashing
type: tool
verified: false
platforms:
  - Linux
  - Python
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.753Z'
id: 830f09cf-119f-46f8-a579-8429bb4b10be
validated: true
submitted: true
---
# bcrypt

**Status**: Unverified

## Overview

Python library for bcrypt password hashing, used if verifying or generating hashes in the exploit.

## Description

Provides secure hashing for password-related operations, potentially for crafting valid resets or verifications.

## Features

- Feature 1: Secure PBKDF
- Feature 2: Salt generation
- Feature 3: Hash verification

## Installation

### Requirements

- Python3, libffi

### Install Commands

```bash
pip3 install bcrypt
```

## Basic Usage

```bash
python3 -c "import bcrypt; print('Installed')"
```

### Common Options

N/A (library)

## Examples

### Example 1: Basic Usage

```python
import bcrypt
hashed = bcrypt.hashpw('pass'.encode(), bcrypt.gensalt())
```

## MITRE ATT&CK Mapping

### Techniques

- [[Unsecured Credentials]]

### Tactics

- [[Credential Access]]

## Detection

- Rarely detected; monitor imports in scripts

## Related Procedures

- [[procedures/Reset-Admin-Password-Using-Leaked-Token]]

## Related Tools

- [[tools/Python3]]

## References

- https://pypi.org/project/bcrypt/
