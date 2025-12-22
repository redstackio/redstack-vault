---
url: 'https://requests.readthedocs.io'
tags:
  - http-client
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.389Z'
id: 8a360914-de6f-48e0-8a50-2dfcf144c2cc
validated: true
submitted: true
---
# requests

**Status**: Unverified

## Overview

Python HTTP library for sending API requests to Rocket.Chat endpoints during exploitation.

## Description

Used in the script for POST/GET to /api/v1/users.list with JSON payloads containing injection operators.

## Features

- Feature 1: Simple API for sessions and auth
- Feature 2: JSON encoding/decoding
- Feature 3: Response handling for blind inference

## Installation

### Requirements

- Python 3

### Install Commands

```bash
pip3 install requests
```

## Basic Usage

```bash
python3 -c "import requests; print(requests.get('http://example.com'))"
```

### Common Options

N/A (library)

## Examples

### Example 1: Basic Usage

```python
import requests
r = requests.post(url, json=payload)
```

## MITRE ATT&CK Mapping

### Techniques

- [[Web Protocols]] Web Protocols

### Tactics

- [[Initial Access]]

## Detection

- Outbound HTTP to internal APIs with suspicious payloads

## Related Procedures

- [[procedures/Leak-Admin-Email-via-Blind-Injection]]

## Related Tools

- [[tools/Python3]]

## References

- Requests documentation
