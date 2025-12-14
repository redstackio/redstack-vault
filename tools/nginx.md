---
id: tool-nginx-001
url: 'https://nginx.org/'
tags:
  - web-server
  - proxy
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:01.377Z'
validated: true
submitted: true
---
# nginx

**Status**: Unverified

## Overview

High-performance web server used as an external Validating Webhook endpoint to receive and respond to admission reviews in the DoS attack.

## Description

Nginx is configured to handle TLS on 443, proxy /validator to /ok with JSON allowance, and log large bodies (up to 5M). Custom log format captures timings for analysis.

## Features

- Feature 1: Reverse proxy for webhooks
- Feature 2: TLS termination
- Feature 3: Body size handling for large payloads

## Installation

### Requirements

- Linux distro (Ubuntu)

### Install Commands

```bash
sudo apt update && sudo apt install -y nginx
```

## Basic Usage

```bash
nginx -t
sudo systemctl start nginx
```

### Common Options

| Option | Description |
|--------|-------------|
| `-t` | Test config |
| `-s reload` | Reload config |

## Examples

### Example 1: Basic Usage

```bash
nginx
```

### Example 2: Advanced Usage

Configure with nginx.conf for webhook proxy.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Connection Proxy]] Proxy

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Nginx access logs with admission review payloads
- Outbound connections to public IPs from cluster

## Related Procedures

- [[procedures/Set-Up-External-Webhook-Endpoint-with-Nginx]]

## Related Tools

- [[tools/curl]]

## References

- Official documentation: https://nginx.org/en/docs/
