---
url: ''
tags:
  - proxy
  - intercept
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:29.230Z'
id: 1ab8edf5-7f55-45c9-a729-e9abe569010d
validated: true
submitted: true
---
# Local-Proxy

**Status**: Unverified

## Overview

A local HTTP proxy tool (e.g., mitmproxy, Charles) for intercepting, inspecting, and modifying web traffic, essential for capturing UUIDs and crafting malicious requests in IDOR/XSS exploits.

## Description

Tools like mitmproxy or Fiddler act as man-in-the-middle to log requests, allowing extraction of sensitive params like UUIDs and replay of modified PUT requests. Commonly used in pentesting for web app vulns.

## Features

- Feature 1: Real-time traffic interception and editing
- Feature 2: Scripting for automated modifications
- Feature 3: Export/import of requests for analysis

## Installation

### Requirements

- Python 3+ for mitmproxy; Java for others

### Install Commands

```bash
# For mitmproxy
pip install mitmproxy
mitmproxy --listen-port 8080
```

## Basic Usage

```bash
mitmproxy
```

### Common Options

| Option | Description |
|--------|-------------|
| `-p 8080` | Listen on port 8080 |
| `--scripts script.py` | Load automation script |

## Examples

### Example 1: Basic Usage

```bash
mitmproxy -p 8080
```
Configure browser to proxy through localhost:8080, trigger requests.

### Example 2: Advanced Usage

```bash
mitmproxy --set block_global=false
```
Intercept and modify PUT body for IDOR.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Sniffing]] Network Sniffing
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Discovery]] Discovery
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Proxy traffic anomalies or CA cert installations
- Logs showing localhost redirects

## Related Procedures


## Related Tools

- [[tools/Burp-Suite]]
- [[tools/OWASP-ZAP]]
- [[tools/Fiddler]]

## References

- mitmproxy docs: https://docs.mitmproxy.org/
