---
url: 'https://docs.python.org/3/library/http.server.html'
tags:
  - http-server
  - static-hosting
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:53.223Z'
id: 25f5bb1f-5286-439f-a284-3d0edf9651bb
validated: true
submitted: true
---
# Python-Built-in-HTTP-Server

**Status**: Unverified

## Overview

The Python http.server module provides a simple, built-in static file server ideal for quickly hosting proof-of-concept files during security assessments, such as HTML pages for WebSocket or JavaScript-based exploits.

## Description

This tool is part of the Python standard library (no installation needed for Python 3+). It handles GET requests for static content, making it perfect for bypassing browser security restrictions like CORS when testing client-side attacks. In this context, it's used to serve a PoC HTML file that connects to a remote GraphQL WebSocket endpoint.

## Features

- Feature 1: Serves static files (HTML, JS, CSS) from the current directory
- Feature 2: Default port 8000, configurable via command-line argument
- Feature 3: Lightweight and runs without external dependencies

## Installation

### Requirements

- Python 3.x installed

### Install Commands

```bash
# No installation required; it's built-in
python3 --version  # Verify Python 3 is available
```

## Basic Usage

```bash
python3 -m http.server
```

### Common Options

| Option | Description |
|--------|-------------|
| `-m http.server` | Execute the server module |
| `PORT` (positional) | Specify port (e.g., python3 -m http.server 8080) |

## Examples

### Example 1: Basic Usage

```bash
python3 -m http.server
```

> Serves on http://localhost:8000; access files via browser.

### Example 2: Advanced Usage

```bash
python3 -m http.server 9000
```

> Custom port for the PoC hosting.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Python]] Python

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing HTTP traffic on non-standard ports like 8000 from local IPs
- Process monitoring for python3 -m http.server executions
- File access logs for PoC HTML files

## Related Procedures

- [[procedures/Start-Local-HTTP-Server-for-PoC-Hosting]]

## Related Tools

- [[Related Tool 1|tools/nginx]]
- [[Related Tool 2|tools/apache-httpd]]

## References

- Official documentation: https://docs.python.org/3/library/http.server.html
- Python security usage guides
