---
id: tool-python-http-server
url: 'https://docs.python.org/3/library/http.server.html'
tags:
  - hosting
  - static-server
type: tool
verified: false
platforms:
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:12.925Z'
validated: true
submitted: true
---
# Python-http-server

**Status**: Unverified

## Overview

Python's http.server is a built-in module for creating a simple HTTP server to host static files, ideal for quick demos of web exploits like burp.html in security testing.

## Description

This tool serves files from the current directory over HTTP, defaulting to port 8000. In the Burp attack, it's used to host the exploit page locally, allowing the browser to access JS payloads without complex setup. No installation needed beyond Python 3.

## Features

- Feature 1: Serves static HTML/JS files
- Feature 2: Directory listing if no index.html
- Feature 3: Customizable port and bindings

## Installation

### Requirements

- Python 3.6+

### Install Commands

```bash
# Built-in, no install needed
python3 --version
```

## Basic Usage

```bash
python -m http.server
```

### Common Options

| Option | Description |
|--------|-------------|
| Port arg | e.g., python -m http.server 8080 |
| --bind | Bind to specific IP (default 0.0.0.0) |

## Examples

### Example 1: Basic Usage

```bash
python -m http.server
```
Serves on port 8000.

### Example 2: Advanced Usage

```bash
python -m http.server 9000 --bind 127.0.0.1
```
Local-only on port 9000.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Process: python -m http.server
- Network: Listening on port 8000
- Logs: Console output in terminal

## Related Procedures

- [[procedures/Host-Burp-Exploit-Page]]

## Related Tools

- [[tools/Burp-Suite]]

## References

- Official documentation: https://docs.python.org/3/library/http.server.html
