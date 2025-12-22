---
id: tool-requests-001
url: 'https://requests.readthedocs.io/en/latest/'
tags:
  - http
  - automation
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:05.114Z'
validated: true
submitted: true
---
# Python-Requests-Library

**Status**: Unverified

## Overview

Requests is a Python library for making HTTP requests, commonly used in security testing for sending custom payloads to web endpoints, including exploitation scripts like SQL injection.

## Description

Requests simplifies HTTP interactions with support for GET, POST, sessions, and custom headers. In offensive security, it's ideal for automating vulnerability testing, such as injecting payloads in this SQLi scenario, handling encoding, and parsing responses.

## Features

- Feature 1: Simple API for GET/POST requests with parameters
- Feature 2: Automatic content decoding and length checks
- Feature 3: Support for URL quoting and encoding

## Installation

### Requirements

- Python 3.x

### Install Commands

```bash
pip install requests
```

## Basic Usage

```python
import requests
r = requests.get('http://example.com')
print(len(r.content))
```

### Common Options

| Option | Description |
|--------|-------------|
| `get(url, params={})` | Send GET with params |
| `headers={}` | Custom headers |
| `timeout=10` | Request timeout |

## Examples

### Example 1: Basic Usage

```python
r = requests.get('http://target.com/endpoint?p=payload')
if len(r.content) > 0:
    print('Match')
```

### Example 2: Advanced Usage

```python
from urllib.parse import quote
url = 'http://target.com?p=' + quote(encoded_payload)
r = requests.get(url)
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing Python User-Agent or high request volume
- Anomalous payloads in request bodies

## Related Procedures

- [[procedures/Test-Unsubscribe-Endpoint-for-SQL-Injection]]
- [[procedures/Extract-MySQL-User-via-Blind-SQL-Injection]]

## Related Tools

- [[Related Tool: curl]]

## References

- Official documentation: https://requests.readthedocs.io/
