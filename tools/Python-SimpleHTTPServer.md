---
url: null
tags:
  - server
  - capture
  - python
type: tool
platforms:
  - Linux
  - macOS
  - Windows
description: >-
  Built-in Python module to start a basic HTTP server for listening to incoming
  requests on localhost
id: 9e55ea34-5ad3-4988-b8fb-d089c00bc568
created_at: '2025-12-14T04:39:09.623Z'
updated_at: '2025-12-14T04:39:09.623Z'
verified: false
validated: true
submitted: true
---
# Python-SimpleHTTPServer

**Status**: Unverified

## Overview

SimpleHTTPServer is a Python standard library module for quickly spinning up an HTTP server to serve files or log requests, useful for SSRF capture in testing.

## Description

It provides a minimal HTTP/1.0 server that logs requests to stdout. In Python 3, it's replaced by http.server but functions similarly. Requires sudo for ports <1024; alternatives include nginx for production.

## Features

- Feature 1: Automatic directory listing
- Feature 2: Request logging to console
- Feature 3: Basic file serving

## Installation

### Requirements

- Python 2.7 or 3.x

### Install Commands

```bash
# Built-in, no install needed
python -m SimpleHTTPServer 80
```

## Basic Usage

```bash
python -m SimpleHTTPServer
```

### Common Options

| Option | Description |
|--------|-------------|
| `-m` | Run as module |
| `port` | Bind port (default 8000) |

## Examples

### Example 1: Basic Usage

```bash
python -m SimpleHTTPServer 80
```

### Example 2: Advanced Usage

```bash
python -m SimpleHTTPServer 8080
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Sniffing]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Ephemeral python processes on low ports
- HTTP logs showing simple server responses

## Related Procedures

- [[procedures/Start-Local-HTTP-Server-to-Capture-SSRF]]

## Related Tools

- [[tools/Burp-Suite]]

## References

- Python docs: https://docs.python.org/3/library/http.server.html
