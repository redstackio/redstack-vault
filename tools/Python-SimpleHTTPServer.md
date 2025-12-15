---
url: 'https://docs.python.org/2/library/simplehttpserver.html'
tags:
  - testing
  - http-server
type: tool
platforms:
  - Linux
description: >-
  Built-in Python module for a simple HTTP server used in testing to receive and
  log requests.
id: 5a9b9d9c-9e51-4f73-a590-98cdbeb0e283
created_at: '2025-12-14T17:26:30.093Z'
updated_at: '2025-12-14T17:26:30.093Z'
verified: false
validated: true
submitted: true
---
# Python-SimpleHTTPServer

**Status**: Unverified

## Overview

Python's SimpleHTTPServer is a basic HTTP server module for serving files over HTTP, commonly used in security testing to simulate targets and observe incoming traffic like request floods from exploits.

## Description

It provides a lightweight way to create a local web server without additional setup, logging all GET requests to stdout. In offensive security, it's used to reproduce vulnerabilities by capturing exploit-generated traffic, such as in curl globbing DoS tests.

## Features

- Feature 1: Serves directory contents as HTML index
- Feature 2: Logs all HTTP requests with timestamps and status codes
- Feature 3: Supports GET method for static file delivery

## Installation

### Requirements

- Python 2.x or 3.x (built-in, no install needed)

### Install Commands

```bash
# No installation required; use python -m
```

## Basic Usage

```bash
python -m SimpleHTTPServer
```

### Common Options

| Option | Description |
|--------|-------------|
| Port specification | Run as `python -m SimpleHTTPServer PORT` |

## Examples

### Example 1: Basic Usage

```bash
python -m SimpleHTTPServer 8000
```

### Example 2: Advanced Usage

```bash
python -m SimpleHTTPServer 8000 &  # Background
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Endpoint Denial of Service]]

### Tactics

- [[Impact]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for python -m SimpleHTTPServer
- Port scans showing HTTP on non-standard ports like 8000

## Related Procedures

- [[procedures/Set-Up-Local-HTTP-Server-for-Testing]]

## Related Tools

- [[tools/curl]]

## References

- Official documentation: https://docs.python.org/2/library/simplehttpserver.html
