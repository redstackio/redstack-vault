---
url: 'https://pypi.org/project/bcrypt'
tags:
  - hashing
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.384Z'
id: 839eeffa-a870-4f88-a774-c428534f7ce4
validated: true
submitted: true
---
# bcrypt

**Status**: Unverified

## Overview

Python library for bcrypt password hashing and verification, used if leaked hashes need processing.

## Description

In the exploit, aids in handling any password-related operations post-leakage, though primarily for verification.

## Features

- Feature 1: Secure hashing
- Feature 2: Salt generation
- Feature 3: Compatibility with Node.js bcrypt

## Installation

### Requirements

- Python 3, libffi

### Install Commands

```bash
pip3 install bcrypt
```

## Basic Usage

```bash
python3 -c "import bcrypt; print(bcrypt.hashpw(b'pass', bcrypt.gensalt()))"
```

### Common Options

N/A

## Examples

### Example 1: Basic Usage

```python
import bcrypt
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
```

## MITRE ATT&CK Mapping

### Techniques

- [[Credentials In Files]] Password Policy Discovery (adapted)

### Tactics

- [[Credential Access]]

## Detection

- Rarely indicative alone

## Related Procedures


## Related Tools

- [[tools/Python3]]

## References

- PyPI bcrypt
