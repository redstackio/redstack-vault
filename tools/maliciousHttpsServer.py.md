---
url: >-
  https://hackerone-us-west-2-production-attachments.s3.us-west-2.amazonaws.com/2YJSameMWd27VVEjALhXjowN?response-content-disposition=attachment%3B%20filename%3D%22maliciousHttpsServer.py%22%3B%20filename%2A%3DUTF-8%27%27maliciousHttpsServer.py&response-content-type=text%2Fx-python&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAQGK6FURQY5VCFHQ2%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T031259Z&X-Amz-Expires=3600&X-Amz-Security-Token=...
  (attachment link)
tags:
  - ssrf
  - https
type: tool
platforms:
  - Linux
description: Custom Python HTTPS server mimicking Docker daemon with SSRF redirects
id: 5c1e6c64-411d-430c-9a01-7272a710bd8d
created_at: '2025-12-14T04:08:47.984Z'
updated_at: '2025-12-14T04:08:47.984Z'
verified: false
validated: true
submitted: true
---
# maliciousHttpsServer.py

**Status**: Unverified

## Overview

Custom script for a malicious HTTPS server using stolen Docker certs to issue redirects for SSRF in GitLab Runner.

## Description

Implements HTTP server with TLS, parses Docker API requests, and redirects to internal targets like GCP metadata.

## Features

- Feature 1: TLS with custom certs
- Feature 2: Path-based redirects
- Feature 3: Support for GET/POST/DELETE

## Installation

### Requirements

- Python 3
- ssl, http.server modules

### Install Commands

```bash
# Download from attachment
wget [URL] -O maliciousHttpsServer.py
```

## Basic Usage

```bash
python3 maliciousHttpsServer.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| --cert | Server PEM | Yes |
| --key | Private key | Yes |
| --port | Listen port | Yes |

## Examples

### Example 1: Basic Usage

```bash
python3 maliciousHttpsServer.py --cert server.pem --key server-key.pem --port 1111
```

### Example 2: Advanced Usage

Configure redirects in code for specific paths.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Hijack Execution Flow]]

### Tactics

- [[Collection]]
- [[Lateral Movement]]

## Detection

Indicators and methods for detecting this tool's usage:

- Python processes with ssl context
- Outbound redirects in proxy logs

## Related Procedures


## Related Tools


## References

- HackerOne report attachment
