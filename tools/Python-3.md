---
id: tool-001
url: 'https://www.python.org/downloads/'
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
updated_at: '2025-12-14T17:29:36.179Z'
validated: true
submitted: true
---
# Python 3

**Status**: Unverified

## Overview

Python 3 is a versatile programming language used here to run a custom HTTPS server script for hosting the malicious HTML exploit payload locally.

## Description

In this context, Python 3 executes server.py to provide a simple HTTPS server on port 5000 with an invalid self-signed certificate, enabling the delivery of disable_features2.html over a secure protocol to Internet Explorer.

## Features

- Feature 1: Cross-platform scripting for server automation
- Feature 2: Built-in http.server module for quick web hosting
- Feature 3: Support for SSL/TLS via custom scripts

## Installation

### Requirements

- Windows OS
- Internet access for download

### Install Commands

```bash
# Download from official site or use winget
winget install Python.Python.3.11
```

## Basic Usage

```bash
python --version
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help |
| -V, --version | Display version |

## Examples

### Example 1: Basic Usage

```bash
python server.py
```

Starts the HTTPS server.

### Example 2: Advanced Usage

```bash
python -m http.server 5000
```

Runs built-in HTTP server (adapt for HTTPS).

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Python]] Python

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for python.exe with network binds on port 5000
- Network logs showing localhost HTTPS traffic
- File system scans for server.py scripts

## Related Procedures

- [[procedures/Setup-Local-HTTPS-Server-for-Malicious-HTML]]

## Related Tools

- [[tools/server-py]]

## References

- Official documentation: https://docs.python.org/3/
