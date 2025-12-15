---
id: tool-web-debugging-proxy-001
url: ''
tags:
  - proxy
  - traffic-interception
  - api-testing
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:27.416Z'
validated: true
submitted: true
---
# Web-Debugging-Proxy

**Status**: Unverified

## Overview

A web debugging proxy (e.g., Burp Suite, Charles Proxy, or mitmproxy) intercepts and modifies HTTP/HTTPS traffic between clients like Android apps and servers, essential for analyzing API calls in mobile security assessments.

## Description

These tools act as man-in-the-middle proxies, allowing inspection, replay, and manipulation of requests/responses. In this context, they reveal Grab App's OTP endpoints by capturing POSTs during login, enabling identification of rate limiting flaws. Features include SSL decryption via CA installation, request repeating, and scripting for automation.

## Features

- Feature 1: Real-time traffic viewing and filtering by endpoint or method
- Feature 2: HTTPS decryption with custom certificates for mobile apps
- Feature 3: Request editing and intrusion tools for testing vulnerabilities

## Installation

### Requirements

- Java 8+ for Burp; Python 3 for mitmproxy
- Admin privileges for CA installation on emulators

### Install Commands

```bash
# For mitmproxy (open-source alternative)
pip install mitmproxy
mitmproxy --listen-host 0.0.0.0

# For Burp Suite: Download from PortSwigger
```

## Basic Usage

```bash
mitmproxy -p 8080
```

### Common Options

| Option | Description |
|--------|-------------|
| -p, --port | Set listening port (default 8080) |
| --set block_global=false | Allow external connections |

## Examples

### Example 1: Basic Usage

Run proxy and configure emulator to route through it; capture Grab App login requests.

### Example 2: Advanced Usage

```bash
mitmproxy --mode transparent --listen-port 8080
```
Use for seamless interception; export HAR files for analysis.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Sniffing]] Network Sniffing

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Anomalous CA certificates on devices
- Proxy headers in requests (e.g., X-Forwarded-For)
- High latency from interception

## Related Procedures


## Related Tools

- [[tools/Burp-Suite]]
- [[tools/Charles-Proxy]]

## References

- Official documentation: Varies by tool (e.g., mitmproxy.org)
- Related resources: OWASP Mobile Security Testing Guide
