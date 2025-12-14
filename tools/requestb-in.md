---
url: 'http://requestb.in'
tags:
  - webhook-tester
  - request-capture
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:11.014Z'
id: d1a22a7b-5e9e-4a04-b69a-eb42335c7bf8
validated: true
submitted: true
---
# requestb-in

**Status**: Unverified

## Overview

requestb.in is a web service for creating unique endpoints to capture and inspect incoming HTTP requests, useful for verifying webhook deliveries in security testing.

## Description

It generates a temporary URL (e.g., http://requestb.in/17m30us1) that logs all POST/GET requests, headers, and payloads, ideal for confirming exfiltration in webhook-based attacks without setting up a full server.

## Features

- Feature 1: Instant endpoint creation with request history
- Feature 2: View raw payloads, headers, and query params
- Feature 3: Shareable bins for collaborative inspection

## Installation

### Requirements

- Web browser access

### Install Commands

```bash
# No installation needed; access via browser
# Create a bin at http://requestb.in
```

## Basic Usage

```bash
# N/A - Web-based
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Generate bin ID via site |
| Inspect | View requests on bin page |

## Examples

### Example 1: Basic Usage

1. Visit http://requestb.in
2. Create a new request bin
3. Use the URL in webhook address
4. Refresh page to see incoming requests

### Example 2: Advanced Usage

```bash
# Simulate sending to bin
curl -X POST http://requestb.in/abc123 -d '{"test":"data"}'
# Then inspect at http://requestb.in/abc123
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning: Scanning IP Blocks
- [[Network Sniffing]] Network Sniffing

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- Outbound traffic to requestb.in domains from internal systems
- Unusual HTTP POSTs to temporary-looking URLs
- Log analysis for requestbin.io subdomains

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/ngrok]]
- [[tools/Webhook.site]]

## References

- Official documentation: http://requestb.in/docs
- Related resources: Webhook testing tutorials
