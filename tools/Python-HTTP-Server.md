---
url: null
tags:
  - http
  - server
  - exploitation
type: tool
platforms:
  - Linux
  - macOS
  - Windows
description: Built-in Python module for creating a simple HTTP server to handle requests
id: b22ab479-fd0d-4567-81b6-203cae4e75be
created_at: '2025-12-13T09:00:27.240Z'
updated_at: '2025-12-13T09:00:27.240Z'
verified: false
validated: true
submitted: true
---
# Python HTTP Server

**Status**: Unverified

## Overview

Python's http.server module is a built-in tool for quickly setting up an HTTP server, commonly used in security testing to receive callbacks or log requests during exploits like XXE or SSRF.

## Description

This tool provides a lightweight way to serve files and handle HTTP requests without additional installations, ideal for proof-of-concept demonstrations in offensive security.

## Features

- Simple HTTP serving
- Request logging
- Customizable port and binding

## Installation

### Requirements

- Python 3.x installed

### Install Commands

```bash
# No installation needed, built-in module
```

## Basic Usage

```bash
python -m http.server --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `--bind` | Specify alternate bind address |
| `--directory` | Specify alternate directory |

## Examples

### Example 1: Basic Usage

```bash
python -m http.server 8000
```

### Example 2: Advanced Usage

```bash
python -m http.server 8080 --bind 0.0.0.0
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for Python processes listening on unusual ports
- Check network logs for inbound HTTP connections

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[SimpleHTTPServer]]

## References

- Python official documentation: https://docs.python.org/3/library/http.server.html
