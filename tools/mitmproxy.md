---
url: 'https://mitmproxy.org/'
tags:
  - mitm
  - proxy
  - web
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
validated: true
submitted: true
---
# mitmproxy

**Status**: Unverified

## Overview

mitmproxy is a free and open-source interactive HTTPS proxy used for intercepting, inspecting, modifying, and replaying web traffic, commonly in security testing for MITM attacks.

## Description

It allows users to view and manipulate HTTP/HTTPS traffic in real-time, making it ideal for debugging, testing, and exploiting web vulnerabilities like insecure redirects.

## Features

- Feature 1: Interactive console for traffic inspection
- Feature 2: Scriptable with Python for automation
- Feature 3: Supports SSL/TLS interception

## Installation

### Requirements

- Python 3.8+
- pip package manager

### Install Commands

```bash
pip install mitmproxy
```

## Basic Usage

```bash
mitmproxy
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-m, --mode` | Set proxy mode (e.g., transparent) |

## Examples

### Example 1: Basic Usage

```bash
mitmproxy --listen-port 8080
```

### Example 2: Advanced Usage

```bash
mitmproxy -s script.py
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Adversary-in-the-Middle]]
- [[Network Sniffing]]

### Tactics

- [[Initial Access]]
- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual proxy traffic or certificate changes
- Detection method 2: Network monitoring for intercepted connections

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Burp Suite]]
- [[Wireshark]]

## References

- Official documentation: https://docs.mitmproxy.org/
- Related resources: GitHub repository
