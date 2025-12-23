---
id: tool-python-http-001
url: 'https://docs.python.org/3/library/http.server.html'
name: Python-HTTP-Server
tags:
  - listener
  - http
  - poc
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:02.092Z'
validated: true
submitted: true
---
# Python-HTTP-Server

**Status**: Unverified

## Overview

Python's built-in HTTP server module is a lightweight tool for serving files or acting as a request listener in security testing, commonly used in SSRF POCs to capture application fetches without needing external dependencies.

## Description

The http.server module provides a simple, single-threaded HTTP server ideal for development and testing. In offensive security, it's used to listen for inbound connections from vulnerable apps, logging requests to confirm exploits like SSRF. It supports GET/POST handling and can be bound to specific interfaces/ports. No installation beyond Python is required.

## Features

- Feature 1: Basic HTTP/1.1 request handling and logging
- Feature 2: Customizable port and bind address
- Feature 3: Serves directory contents or responds to all paths

## Installation

### Requirements

- Python 3.x

### Install Commands

```bash
# Python is pre-installed on most systems; otherwise:
sudo apt install python3  # On Debian/Ubuntu
```

## Basic Usage

```bash
python3 -m http.server --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-p PORT, --port PORT` | Port to serve on (default 8000) |
| `--bind ADDRESS` | IP to bind to (default 0.0.0.0) |
| `-d DIRECTORY` | Directory to serve |

## Examples

### Example 1: Basic Usage

```bash
python3 -m http.server 4444
```

### Example 2: Advanced Usage

```bash
python3 -m http.server 4444 --bind 127.0.0.1
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Network scans showing port 4444 open with basic HTTP responses
- Logs of simple 200/404 responses without advanced features
- Process lists including python3 -m http.server

## Related Procedures

- [[procedures/Setup-HTTP-Listener-for-SSRF-POC]]

## Related Tools

- [[netcat]]
- [[SimpleHTTPServer]]

## References

- Official documentation: https://docs.python.org/3/library/http.server.html
