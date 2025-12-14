---
id: tool-server.py
url: null
tags:
  - http-server
  - poc
type: tool
verified: false
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:55.163Z'
validated: true
submitted: true
---
# server.py

**Status**: Unverified

## Overview

server.py is a custom Python script acting as a rudimentary HTTP server to host proof-of-concept files for exploits, such as universal_xss.html in Kaspersky XSS attacks.

## Description

This script uses Python's http.server module to serve static files on port 5000, enabling local hosting of malicious HTML that interacts with browser frames via postMessage. It's lightweight and requires no installation beyond Python 3.

## Features

- Feature 1: Serves files from current directory on localhost:5000
- Feature 2: Handles GET requests for HTML like universal_xss.html
- Feature 3: Simple logging for request verification

## Installation

### Requirements

- Python 3
- Place script in directory with PoC files

### Install Commands

```bash
# Download or create server.py with http.server import
curl -o server.py https://example-poc/server.py
```

## Basic Usage

```bash
python server.py
```

### Common Options

| Option | Description |
|--------|-------------|
| Port | Hardcoded to 5000; edit script to change |

## Examples

### Example 1: Basic Usage

```bash
python server.py
```

### Example 2: Advanced Usage

```bash
# Run and access http://localhost:5000/universal_xss.html
python server.py
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Python processes bound to port 5000
- Local HTTP traffic to spoofed domains

## Related Procedures

- [[procedures/Host-Malicious-POC-Server-with-Python]]

## Related Tools

- [[tools/Python-3]]

## References

- Related resources: PoC from HackerOne report
