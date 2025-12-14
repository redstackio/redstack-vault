---
id: 123e4567-e89b-12d3-a456-426614174007
name: PortSwigger-WebSocket-Lab
type: tool
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:35.943Z'
platforms:
  - Web
tags:
  - websocket
  - lab
  - testing
url: 'https://portswigger.net/web-security/websockets/cross-site-websocket-hijacking'
validated: true
submitted: true
---

# PortSwigger-WebSocket-Lab

**Status**: Unverified

## Overview

PortSwigger's WebSocket Lab is an interactive training environment for learning and testing Cross-Site WebSocket Hijacking (CSWSH) vulnerabilities, providing hands-on examples of hijacking WebSocket connections to steal data.

## Description

This lab simulates vulnerable WebSocket implementations, allowing users to craft malicious pages that exploit missing CSRF protections. It's ideal for offensive security testing, mirroring real-world scenarios like the Stripo Inc report where handshakes lacked origin validation.

## Features

- Feature 1: Interactive exploit challenges for CSWSH
- Feature 2: Detailed explanations of WebSocket security pitfalls
- Feature 3: Burp Suite integration for proxying and inspecting connections

## Installation

### Requirements

- Modern web browser
- Burp Suite Community Edition (optional for advanced inspection)

### Install Commands

```bash
# No installation needed; access via web browser
# Optional: Download Burp Suite from portswigger.net/burp
```

## Basic Usage

```bash
# Visit the lab URL and follow guided challenges
browser https://portswigger.net/web-security/websockets/cross-site-websocket-hijacking/lab
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | N/A (web-based) |
| `-v, --verbose` | Enable Burp logging for detailed traces |

## Examples

### Example 1: Basic Usage

```bash
# Open lab in browser and attempt cross-origin WebSocket connection
# Use provided malicious HTML template
```

### Example 2: Advanced Usage

```bash
# Integrate with Burp: Proxy traffic and modify headers
# In Burp, intercept WebSocket upgrade requests
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Drive-by Compromise]]
- [[JavaScript]]

### Tactics

- [[Initial Access]]
- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Browser traffic to portswigger.net domains during testing
- Anomalous WebSocket requests in proxy logs

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
- [[Chrome DevTools]]

## References

- Official documentation: https://portswigger.net/web-security/websockets
- Related resources: OWASP WebSocket Security Cheat Sheet
