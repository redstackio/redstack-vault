---
url: 'https://requests.readthedocs.io/'
tags:
  - http-client
  - comparison
  - python
type: tool
verified: false
platforms:
  - Python
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.352Z'
id: bced332c-8fc8-432b-8f9c-90b3bb580404
validated: true
submitted: true
---
# requests-python

**Status**: Unverified

## Overview

Requests is a popular Python HTTP library for making requests to web services. It is referenced here for comparison, as it properly clears sensitive headers like Proxy-Authorization during cross-domain redirects, unlike vulnerable versions of undici.

## Description

Requests handles sessions, authentication, and redirects automatically, with built-in security features for header management. In the context of this vulnerability, its source code (e.g., sessions.py) demonstrates correct behavior by stripping Proxy-Authorization on redirects, serving as a benchmark for secure HTTP client implementation.

## Features

- Feature 1: Simple API for GET/POST requests
- Feature 2: Automatic redirect handling with header clearing
- Feature 3: Session management for persistent connections

## Installation

### Requirements

- Python 3.6+

### Install Commands

```bash
pip install requests
```

## Basic Usage

```bash
python -c "import requests; print(requests.__version__)"
```

### Common Options

| Option | Description |
|--------|-------------|
| allow_redirects | Boolean to enable redirects (default: True) |
| headers | Dict of custom headers |

## Examples

### Example 1: Basic Usage

```python
import requests
response = requests.get('https://example.com')
```

### Example 2: Advanced Usage

```python
response = requests.get('http://target.com', headers={'Proxy-Authorization': 'test'}, allow_redirects=True)
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Python process with requests module loaded
- Detection method 2: Network logs showing Python User-Agent

## Related Procedures


## Related Tools

- [[tools/undici]]

## References

- Official documentation: https://requests.readthedocs.io/
- Source: https://github.com/psf/requests/blob/main/src/requests/sessions.py#L318
