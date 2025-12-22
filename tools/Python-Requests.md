---
id: tool-uuid-001
url: 'https://requests.readthedocs.io/en/latest/'
tags:
  - http-client
  - automation
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:06.379Z'
validated: true
submitted: true
---
# Python-Requests

**Status**: Unverified

## Overview

Requests is a Python library for making HTTP requests, commonly used in security testing for automating API interactions, fuzzing, and exploit delivery like blind injection payloads.

## Description

It simplifies sending GET/POST requests with parameters, headers, and handling responses, ideal for scripting NoSQL injection tests against web endpoints like FlintCMS's /admin/verify.

## Features

- Feature 1: Simple syntax for params and JSON payloads
- Feature 2: Session management for stateful interactions
- Feature 3: Response parsing for status, redirects, and content

## Installation

### Requirements

- Python 2.7 or 3.x

### Install Commands

```bash
pip install requests
```

## Basic Usage

```bash
python -c "import requests; r = requests.get('http://example.com'); print(r.status_code)"
```

### Common Options

| Option | Description |
|--------|-------------|
| `params=` | Dictionary for query parameters |
| `allow_redirects=False` | Disable following redirects |

## Examples

### Example 1: Basic Usage

```python
import requests
r = requests.get('http://localhost:4000/admin/verify', params={'t': 'test'})
print(r.url)
```

### Example 2: Advanced Usage

```python
payload = {'t': {'$regex': '^a'}}
r = requests.get('http://localhost:4000/admin/verify', params=payload)
if 'sp/' in r.url:
    print('Match!')
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Python]]

### Tactics

- [[Execution]]
- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing rapid sequential requests to verify endpoints
- User-Agent strings indicating Python/requests

## Related Procedures


## Related Tools

- [[Related Tool: Burp Suite]]
- [[Related Tool: curl]]

## References

- Official documentation: https://requests.readthedocs.io/
