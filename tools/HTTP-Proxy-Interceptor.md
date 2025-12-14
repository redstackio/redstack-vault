---
url: 'https://portswigger.net/burp'
tags:
  - proxy
  - interception
  - web-testing
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:30.609Z'
id: e3314fd3-f147-4e5c-a99e-6ab8044934c8
validated: true
submitted: true
---
# HTTP-Proxy-Interceptor

**Status**: Unverified

## Overview

HTTP Proxy Interceptor tools, such as Burp Suite, are essential for web security testing, allowing interception, inspection, and modification of HTTP/HTTPS traffic between a client (e.g., browser) and server. In this context, it's used to capture and replay authentication responses in replay attacks.

## Description

These tools act as man-in-the-middle proxies, enabling pentesters to view request/response details, replay messages, and tamper with data. For offensive operations, they facilitate vulnerability discovery like improper auth by saving and reusing responses. Common in web app pentesting for Basecamp-like scenarios.

## Features

- Feature 1: Traffic interception and visualization
- Feature 2: Request/response editing and replay
- Feature 3: Scope filtering and HTTPS decryption via CA certificate

## Installation

### Requirements

- Java Runtime Environment (for Burp Suite)
- Administrative privileges for CA installation

### Install Commands

```bash
# Download and run Burp Suite Community Edition
wget https://portswigger.net/burp/releases/download?product=community&type=Linux -O burpsuite_community.jar
java -jar burpsuite_community.jar
```

## Basic Usage

```bash
# Launch the tool (GUI-based)
java -jar burpsuite_community.jar
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help (if CLI variant) |
| `--no-sandbox` | Disable sandbox for compatibility |

## Examples

### Example 1: Basic Usage

Launch Burp, set browser proxy to 127.0.0.1:8080, install CA cert, and browse to target. Intercept tab shows traffic.

### Example 2: Advanced Usage

In Proxy > Intercept, enable interception on login requests. Edit response: right-click saved response > Send to Repeater > Modify and forward.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials
- [[Forge Web Credentials]] Forge Web Credentials

### Tactics

- [[Initial Access]] Initial Access
- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual TLS handshakes or self-signed certs in traffic
- Proxy headers (e.g., X-Forwarded-For) in logs
- High latency from interception delays

## Related Procedures


## Related Tools

- [[Wireshark]]
- [[ZAP]]

## References

- Official documentation: https://portswigger.net/burp/documentation
- Related resources: OWASP Testing Guide
