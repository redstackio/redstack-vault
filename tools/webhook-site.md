---
id: tool-webhook-site-001
url: 'https://webhook.site'
tags:
  - monitoring
  - ssrf
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.374Z'
validated: true
submitted: true
---
# Webhook.site

**Status**: Unverified

## Overview

Webhook.site is a free online service for generating temporary HTTP endpoints to capture and inspect incoming requests, commonly used in security testing to verify SSRF, CSRF, or webhook behaviors without setting up local servers.

## Description

It provides a unique URL upon page load, allowing real-time viewing of request headers, body, and metadata. Ideal for confirming if a target server makes outbound requests during exploits like SSRF in Lichess API testing. No installation needed; browser-based.

## Features

- Feature 1: Instant unique URL generation for request capture
- Feature 2: Real-time dashboard for headers, JSON, and raw data inspection
- Feature 3: Export logs and one-time or multi-use modes

## Installation

### Requirements

- Web browser
- Internet access

### Install Commands

No installation; access via https://webhook.site

## Basic Usage

```bash
# No CLI; use browser to visit site and copy URL
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Browser-based; refresh dashboard for updates |

## Examples

### Example 1: Basic Usage

Visit https://webhook.site, copy the URL, inject into SSRF payload, and monitor the page for incoming requests.

### Example 2: Advanced Usage

Use the URL in curl: `curl "https://target.com?callback=https://webhook.site/unique-id"`; view details on site.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Outbound DNS queries to webhook.site
- Unusual HTTP traffic to temporary webhook domains

## Related Procedures


## Related Tools

- [[ngrok]]
- [[requestbin]]

## References

- Official site: https://webhook.site
- Documentation: Built-in help on the platform
