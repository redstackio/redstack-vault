---
id: tool-curl
url: 'https://curl.se/'
tags:
  - web
  - http
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:24.024Z'
validated: true
submitted: true
---
# curl

**Status**: Unverified

## Overview

Curl is a versatile command-line tool for transferring data with URLs, commonly used in security testing to probe web endpoints and verify service status.

## Description

For subdomain takeover verification, curl checks HTTP responses from abandoned services like Zendesk subdomains to confirm unclaimed status through headers or redirects.

## Features

- Feature 1: Support for HTTP, HTTPS, and various protocols
- Feature 2: Custom headers, methods (GET, HEAD, POST)
- Feature 3: Output control and following redirects

## Installation

### Requirements

- Standard on most systems

### Install Commands

```bash
# On Ubuntu: sudo apt install curl
# On macOS: Already installed
```

## Basic Usage

```bash
curl https://example.com
```

### Common Options

| Option | Description |
|--------|-------------|
| `-I` | HEAD request |
| `-L` | Follow redirects |
| `-v` | Verbose output |

## Examples

### Example 1: Basic Usage

```bash
curl -I https://support.easycontactnow.com
```

### Example 2: Advanced Usage

```bash
curl -I -L -v https://support.easycontactnow.com
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- User-Agent strings in logs matching curl defaults
- HEAD requests to sensitive endpoints

## Related Procedures

- [[procedures/Verify-Service-Abandonment-for-Takeover]]

## Related Tools

- [[tools/wget]]
- [[tools/httpie]]

## References

- Official documentation: https://curl.se/docs/manpage.html
