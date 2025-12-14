---
id: tool-uuid-2
url: 'https://requests.readthedocs.io/'
tags:
  - http-client
  - python
  - automation
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:09.326Z'
validated: true
submitted: true
---
# python-requests

**Status**: Unverified

## Overview

Requests is a Python HTTP library for sending HTTP requests extremely easily, used in security testing for automating web interactions, including SSRF payload delivery and response timing analysis for port scanning.

## Description

In exploits, it's used in scripts like exp.py to send GET requests with gopher payloads to vulnerable endpoints, handling timeouts to detect open ports. Simpler than urllib, supports sessions, headers, and JSON. Ideal for Python-based automation in web app pentesting.

## Features

- Feature 1: Simple API for GET/POST with params
- Feature 2: Timeout and exception handling
- Feature 3: Custom headers and proxies

## Installation

### Requirements

- Python 3.x

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
| timeout= | Set request timeout |
| headers= | Custom headers dict |
| params= | Query parameters |

## Examples

### Example 1: Basic Usage

```bash
import requests
r = requests.get('https://example.com')
print(r.status_code)
```

### Example 2: Advanced Usage

```bash
r = requests.get('https://target.com/endpoint/gopher://127.0.0.1:25/', timeout=5)
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Network Service Scanning]] Network Service Scanning

### Tactics

- [[Initial Access]] Initial Access
- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Python process with requests module importing.
- HTTP logs showing scripted request patterns (e.g., rapid gopher URLs).

## Related Procedures


## Related Tools

- [[Related Tool: curl]]
- [[Related Tool: httpx]]

## References

- Official documentation: https://requests.readthedocs.io/
- Related resources: PyPI requests
