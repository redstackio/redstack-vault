---
url: 'https://pypi.org/project/proxyrequests/'
tags:
  - proxy
  - python
  - brute-force
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: >-
  Python library for HTTP requests through rotating proxies to bypass IP
  restrictions.
id: fc9f6679-d924-4314-b348-c62dfc91b750
created_at: '2025-12-14T17:30:26.693Z'
updated_at: '2025-12-14T17:30:26.693Z'
verified: false
validated: true
submitted: true
---
# ProxyRequests

**Status**: Unverified

## Overview

ProxyRequests is a Python wrapper for requests library that simplifies proxy rotation for evading rate limits in web attacks.

## Description

Extends requests.Session() to handle proxy lists, useful for distributed brute-force on endpoints like MoPub login.

## Features

- Feature 1: Automatic proxy cycling
- Feature 2: Session persistence with proxies
- Feature 3: Compatible with requests methods (post, get)

## Installation

### Requirements

- Python 3+
- pip

### Install Commands

```bash
pip install proxyrequests
```

## Basic Usage

```bash
python -c "import proxyrequests; print('Installed')"
```

### Common Options

| Option | Description |
|--------|-------------|
| proxies | List of proxy URLs |
| session.proxies | Set per session |

## Examples

### Example 1: Basic Usage

```python
import proxyrequests as pr
pr.get('https://example.com', proxies={'http': 'proxy:port'})
```

### Example 2: Advanced Usage

```python
pr.post('https://app.mopub.com/login', json=payload, proxies=proxy_list)
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Connection Proxy]] Proxy
- [[Brute Force]] Brute Force

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Python processes with proxy library imports
- Traffic from multiple proxy IPs to single endpoint

## Related Procedures

- [[procedures/Bypass-Rate-Limiting-Using-Proxy-Rotation-in-Python]]

## Related Tools

- [[tools/curl]]

## References

- PyPI: https://pypi.org/project/proxyrequests/
