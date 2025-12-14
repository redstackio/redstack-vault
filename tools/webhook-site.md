---
id: tool-webhook-001
url: 'https://webhook.site'
tags:
  - webhook
  - monitoring
  - ssrf
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.668Z'
validated: true
submitted: true
---
# webhook-site

**Status**: Unverified

## Overview

Webhook.site is a free online service for generating unique URLs to capture and inspect incoming HTTP requests, commonly used in security testing to confirm server-side interactions like SSRF exploits.

## Description

It provides temporary endpoints that log all details of requests (headers, body, IP), making it ideal for verifying if a target server (e.g., Lichess) fetches a controlled URL during exploitation. No installation needed; works via browser.

## Features

- Feature 1: Instant unique URL generation
- Feature 2: Real-time request logging with full headers/payload
- Feature 3: Export logs for analysis; supports GET/POST

## Installation

### Requirements

- Web browser
- Internet access

### Install Commands

No installation; access via https://webhook.site

## Basic Usage

```bash
# No CLI; use browser to generate URL, then curl to test
curl https://webhook.site/unique-id -v
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Browser-based; refresh page for new logs |

## Examples

### Example 1: Basic Usage

Visit webhook.site, copy URL, send request: curl https://your-webhook-url -v. Check site for logs.

### Example 2: Advanced Usage

Integrate in scripts: Use the URL in SSRF payload and monitor for hits.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Vulnerability Scanning]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Outbound requests to webhook.site domains from servers
- Unusual HTTP traffic to temporary/debug endpoints

## Related Procedures


## Related Tools

- [[ngrok]]
- [[requestbin]]

## References

- Official site: https://webhook.site
- Documentation: Built-in help on site
