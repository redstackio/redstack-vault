---
id: uuid-ssl-server-py
url: ''
tags:
  - https-server
  - ssl
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-13T23:52:21.047Z'
validated: true
submitted: true
---
# ssl-server-py

**Status**: Unverified

## Overview

Custom Python script for running a simple local HTTPS server on port 443, used in web exploit scenarios requiring secure hosting of malicious pages, such as postMessage XSS attacks.

## Description

ssl_server.py leverages Python's http.server and ssl modules to create an HTTPS server with a self-signed certificate, ideal for simulating controlled domains in browser-based attacks without external hosting. It's lightweight and requires no additional dependencies beyond Python 3 stdlib.

## Features

- Feature 1: Binds to port 443 for standard HTTPS
- Feature 2: Serves static files like HTML exploits from current directory
- Feature 3: Self-signed cert generation for quick setup

## Installation

### Requirements

- Python 3.6+
- No external packages needed

### Install Commands

```bash
# Download or create the script manually
curl -O https://example.com/ssl_server.py  # Or from report source
```

## Basic Usage

```bash
tool-name --help  # Not applicable; run directly
```

### Common Options

| Option | Description |
|--------|-------------|
| None (script-based) | N/A |

## Examples

### Example 1: Basic Usage

```bash
sudo python3 ssl_server.py
```

### Example 2: Advanced Usage

Serve specific directory: Modify script to set document root.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Python process listening on TCP 443
- Self-signed cert warnings in browser logs

## Related Procedures

- [[procedures/Start-Local-SSL-Server]]

## Related Tools

- Python's built-in http.server

## References

- Python ssl documentation
