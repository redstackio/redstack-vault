---
url: 'https://requests.readthedocs.io/en/latest/'
tags:
  - http-client
  - exploitation
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:51.970Z'
id: 8860d3df-ccf2-45f1-a927-2813f2fac937
validated: true
submitted: true
---
# requests-Library

**Status**: Unverified

## Overview

The requests library is a Python HTTP client used to send crafted JSON POST requests to vulnerable login endpoints, enabling NoSQL injection payloads in the express-cart exploitation.

## Description

It simplifies making HTTP calls with JSON data, authentication, and response handling, crucial for blind injection where multiple requests are needed to infer data from response differences. No specific configuration beyond import; works with Python 2.7+.

## Features

- Feature 1: Simple POST with JSON: requests.post(url, json=data)
- Feature 2: Response parsing for status and text analysis
- Feature 3: Session handling for repeated requests

## Installation

### Requirements

- Python 2.7+

### Install Commands

```bash
pip install requests
```

## Basic Usage

```bash
python -c "import requests; print('Installed')"
```

### Common Options

| Option | Description |
|--------|-------------|
| `json=` | Send data as JSON |
| `headers=` | Custom headers |

## Examples

### Example 1: Basic Usage

```python
import requests
r = requests.post('http://example.com', json={'key': 'value'})
print(r.text)
```

Sends injection payload.

### Example 2: Advanced Usage

```python
session = requests.Session()
for payload in payloads:
    r = session.post(url, json=payload)
    if 'match' in r.text:
        print('Found')
```

For recursive enumeration.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Standard Application Layer Protocol]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Python processes importing requests with high request volume
- WAF logs showing JSON payloads with $ operators

## Related Procedures

- [[procedures/Craft-NoSQL-Injection-Payloads-for-Email-Enumeration]]

## Related Tools

- [[tools/Python]]

## References

- Official documentation: https://requests.readthedocs.io/
- Related resources: PyPI requests page
