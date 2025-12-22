---
id: tool-002
url: null
tags:
  - https-server
  - exploit-hosting
type: tool
verified: false
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.174Z'
validated: true
submitted: true
---
# server.py

**Status**: Unverified

## Overview

server.py is a custom rudimentary HTTPS server script designed to host malicious HTML files for exploits, using Python 3 and featuring an invalid self-signed certificate.

## Description

This script serves the disable_features2.html file on https://localhost:5000/, enabling local testing of browser-based vulnerabilities like the Kaspersky interception exploit. It lacks production hardening, focusing on simplicity for offensive security demos.

## Features

- Feature 1: HTTPS support with self-signed cert
- Feature 2: Serves static HTML files on port 5000
- Feature 3: Minimal logging for exploit verification

## Installation

### Requirements

- Python 3
- No additional deps; uses standard library

### Install Commands

```bash
# Download script manually from exploit source
curl -o server.py https://example-exploit-source/server.py
```

## Basic Usage

```bash
python server.py
```

### Common Options

| Option | Description |
|--------|-------------|
| Port | Defaults to 5000; edit script for changes |
| Cert | Invalid self-signed; generated in script |

## Examples

### Example 1: Basic Usage

```bash
python server.py
```

Hosts files in current dir.

### Example 2: Advanced Usage

Edit script to change port or cert path, then run.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Suspicious python processes binding to 5000
- Local HTTPS traffic with invalid certs
- Presence of disable_features2.html

## Related Procedures

- [[procedures/Setup-Local-HTTPS-Server-for-Malicious-HTML]]

## Related Tools

- [[tools/Python-3]]

## References

- Custom script from HackerOne report #470547
