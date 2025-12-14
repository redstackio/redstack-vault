---
url: 'https://docs.python.org/3/library/http.server.html'
tags:
  - web-server
  - python-module
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:18.978Z'
id: 96dfe029-e0ce-49df-ab99-c4176d0e1f78
validated: true
submitted: true
---
# http.server

**Status**: Unverified

## Overview

http.server is a Python module for creating simple HTTP servers, extended here with SSL for HTTPS and ALPN for HTTP/2 support in the PoC.

## Description

Custom handler responds to specific paths; integrated with ssl for TLS termination on localhost:8443.

## Features

- Feature 1: Custom request handling
- Feature 2: HTTPS via ssl wrapper
- Feature 3: ALPN protocol negotiation

## Installation

### Requirements

- Python 3 standard library

### Install Commands

```bash
# Built-in
python3 -m http.server --help
```

## Basic Usage

```bash
python3 -m http.server 8000
```

### Common Options

| Option | Description |
|--------|-------------|
| `-b` | Bind address |
| `-p` | Port |

## Examples

### Example 1: Basic Usage

```bash
python3 -m http.server 8000
```

### Example 2: Advanced Usage

```python
from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl
# Custom setup as in PoC
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Python]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Python http.server processes on non-standard ports

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/python3]]
- [[tools/nginx]]

## References

- Official documentation: https://docs.python.org/3/library/http.server.html
