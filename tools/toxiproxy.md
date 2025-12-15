---
url: 'https://github.com/Shopify/toxiproxy'
tags:
  - proxy
  - tcp
  - testing
type: tool
platforms:
  - macOS
  - Linux
description: >-
  TCP proxy to simulate network conditions and unreliable connections for
  testing.
id: 3eaac190-c03c-4834-a6a2-7de42accdb4e
created_at: '2025-12-14T17:27:29.688Z'
updated_at: '2025-12-14T17:27:29.688Z'
verified: false
validated: true
submitted: true
---
# toxiproxy

**Status**: Unverified

## Overview

Toxiproxy creates proxies for TCP connections with added 'toxics' for latency, timeouts, etc., vulnerable to CSRF in its HTTP API for security testing.

## Description

Used in offensive ops to pivot traffic or simulate attacks on internal networks via browser-controlled proxies.

## Features

- Feature 1: HTTP API for proxy creation/modification
- Feature 2: Upstream target flexibility (local/remote)
- Feature 3: No auth by default, enabling CSRF/SSRF

## Installation

### Requirements

- Go 1.13+ or Homebrew

### Install Commands

```bash
brew install toxiproxy
```

## Basic Usage

```bash
toxiproxy-server &
```

### Common Options

| Option | Description |
|--------|-------------|
| --listen | API bind address (default :8474) |

## Examples

### Example 1: Basic Usage

```bash
toxiproxy-server -listen 127.0.0.1:8474
```

### Example 2: Advanced Usage

```bash
toxiproxy-server -host 0.0.0.0
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Connection Proxy]]
- [[Exploit Public-Facing Application]]

### Tactics

- [[Lateral Movement]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process listening on port 8474
- API logs showing POST to /proxies

## Related Procedures

- [[procedures/CSRF-Creation-of-New-Proxy-via-Fetch-API]]

## Related Tools

- [[tools/toxiproxy-cli]]

## References

- GitHub repo
