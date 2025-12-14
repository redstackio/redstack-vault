---
id: tool-uuid-001
url: 'https://requestb.in'
tags:
  - request-logging
  - ssrf-testing
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.274Z'
validated: true
submitted: true
---
# requestb.in

**Status**: Unverified

## Overview

requestb.in is a free service for creating endpoints to inspect and log incoming HTTP requests, ideal for confirming blind SSRF vulnerabilities by capturing server-initiated traffic.

## Description

Users generate a unique URL (e.g., https://requestb.in/15rxmgv1) to receive GET/POST requests, viewing headers, body, and IP origin. Commonly used in web security testing for out-of-band validation without custom servers.

## Features

- Feature 1: Instant endpoint creation with unique URLs
- Feature 2: Real-time request inspection including raw data
- Feature 3: Support for multiple requests per bin with timestamps

## Installation

### Requirements

- Web browser

### Install Commands

No installation; access via https://requestb.in

## Basic Usage

```bash
# No CLI; use browser to create bin
curl -X GET https://requestb.in  # Visit site
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Web-based only |

## Examples

### Example 1: Basic Usage

Visit https://requestb.in, create bin, use URL in payload, inspect requests.

### Example 2: Advanced Usage

Integrate with scripts to poll for new requests.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Outbound requests to requestb.in domains
- Unusual GET requests from application servers to dynamic bins

## Related Procedures

- [[procedures/Inject-Absolute-URL-in-SVG-Fill-for-Blind-SSRF-Discovery]]

## Related Tools

- [[tools/netcat]]

## References

- Official site: https://requestb.in
