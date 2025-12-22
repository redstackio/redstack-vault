---
url: 'https://mitmproxy.org/'
tags:
  - proxy
  - interception
  - mobile
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: An interactive HTTPS proxy for man-in-the-middle attacks on web traffic
id: 1ad9d78d-7cad-4e3a-a23c-25346a46834e
created_at: '2025-12-13T09:01:26.380Z'
updated_at: '2025-12-13T09:01:26.380Z'
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.779Z'
id: 836068fb-7424-4b5e-aa4c-cdfeccd903c3
validated: true
submitted: true
---
# mitmproxy

**Status**: Unverified

## Overview

mitmproxy is an interactive HTTPS proxy for capturing and inspecting traffic, ideal for extracting tokens from mobile app sessions in security testing.

## Description

This tool allows decryption of TLS traffic, filtering requests, and scripting modifications. In offensive ops, it's used to intercept API calls from apps like Shopify Mobile to steal auth tokens for reuse.

## Features

- Feature 1: Interactive console for live traffic viewing
- Feature 2: Python scripting for automation
- Feature 3: CA certificate generation for HTTPS interception

## Installation

### Requirements

- Python 3.7+
- pip

### Install Commands

```bash
pip install mitmproxy
```

## Basic Usage

```bash
mitmproxy --mode transparent
```

### Common Options

| Option | Description |
|--------|-------------|
| `-p 8080` | Listen on port 8080 |
| `--set confdir=~/.mitmproxy` | Set config directory |

## Examples

### Example 1: Basic Usage

```bash
mitmproxy -p 8080
```
Configure device proxy to host:8080 and browse to capture traffic.

### Example 2: Advanced Usage

```bash
mitmdump -s script.py -p 8080
```
Run with a script to auto-extract headers.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unsecured Credentials]]
- [[Network Sniffing]]

### Tactics

- [[Initial Access]]
- [[Exfiltration]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual CA certificates on endpoints
- Proxy traffic patterns in network logs
- Anomalous user-agent in intercepted requests

## Related Procedures

- [[procedures/Capture-Access-Token-from-Mobile-Session]]

## Related Tools

- [[Burp Suite]]
- [[Wireshark]]

## References

- Official documentation: https://docs.mitmproxy.org/
- Related resources: OWASP Mobile Testing Guide
