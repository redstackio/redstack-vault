---
id: tool-python-3
url: 'https://www.python.org/'
tags:
  - scripting
  - server
type: tool
verified: false
platforms:
  - Windows
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:55.166Z'
validated: true
submitted: true
---
# Python-3

**Status**: Unverified

## Overview

Python 3 is a versatile programming language used here to run a simple HTTP server script for hosting PoC files in security testing, particularly for web-based exploits like XSS.

## Description

In offensive security, Python 3 executes scripts like server.py to create local web servers without additional setup, ideal for serving malicious HTML in controlled environments. It supports modules like http.server for quick HTTP hosting on ports like 5000.

## Features

- Feature 1: Built-in http.server for easy local hosting
- Feature 2: Cross-platform scripting for Windows testing
- Feature 3: Minimal dependencies for PoC environments

## Installation

### Requirements

- Windows OS
- Internet for download if not installed

### Install Commands

```bash
# Download from python.org or use winget
winget install Python.Python.3.11
```

## Basic Usage

```bash
python --version
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help for python |
| `-V, --version` | Display Python version |

## Examples

### Example 1: Basic Usage

```bash
python server.py
```

### Example 2: Advanced Usage

```bash
python -m http.server 5000
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for python.exe serving HTTP
- Network logs for localhost:5000 traffic
- File system scans for server.py scripts

## Related Procedures

- [[procedures/Host-Malicious-POC-Server-with-Python]]

## Related Tools

- [[tools/server.py]]

## References

- Official documentation: https://docs.python.org/3/library/http.server.html
