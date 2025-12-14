---
url: null
tags:
  - https-server
  - testing
type: tool
verified: false
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:58.602Z'
id: 6ed573d7-36b7-4350-a211-d487528f6f3c
validated: true
submitted: true
---
# ssl_server.py

**Status**: Unverified

## Overview

ssl_server.py is a simple Python script that implements a rudimentary HTTPS server for hosting local files during security testing, particularly useful for exploiting browser extensions that require HTTPS, such as Kaspersky's URL Advisor. It uses an invalid self-signed certificate to simulate secure but untrusted connections.

## Description

The tool starts an HTTPS server on localhost:5000, serving files from the current directory. In offensive security, it's used to host exploit HTML pages like disable_features3.html for drive-by or frame-injection attacks. It requires Python 3's built-in http.server and ssl modules, making it lightweight for quick setups in vulnerability reproduction.

## Features

- Feature 1: HTTPS serving with self-signed certificate on custom port
- Feature 2: Simple file serving from local directory
- Feature 3: No external dependencies beyond Python standard library

## Installation

### Requirements

- Python 3.6+

### Install Commands

```bash
# No installation needed; download the script
curl -O https://example.com/ssl_server.py  # From vulnerability report
```

## Basic Usage

```bash
python ssl_server.py
```

### Common Options

| Option | Description |
|--------|-------------|
| None (script-based) | Runs on port 5000 by default; edit script for changes |

## Examples

### Example 1: Basic Usage

```bash
python ssl_server.py
```

Hosts files; access via https://localhost:5000/file.html.

### Example 2: Advanced Usage

Place exploit files in directory and run; override cert in browser.

```bash
python ssl_server.py  # Serves disable_features3.html
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer
- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing HTTPS on non-standard port 5000 from Python process
- Self-signed cert warnings in browser history
- File system scans for ssl_server.py script

## Related Procedures

- [[procedures/Host-Malicious-Exploit-Page]]

## Related Tools

- [[tools/Python-3]]

## References

- Python ssl module documentation
- HackerOne Report #470553
