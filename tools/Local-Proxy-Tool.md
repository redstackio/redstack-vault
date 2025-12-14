---
id: tool-002
url: null
tags:
  - proxy
  - traffic-intercept
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.419Z'
validated: true
submitted: true
---
# Local-Proxy-Tool

**Status**: Unverified

## Overview

A local proxy tool (e.g., Burp Suite or Fiddler) intercepts and modifies HTTP/HTTPS traffic from a browser, used in security testing to observe request/response flows, such as token exposure in redirect chains during password reset link access.

## Description

This tool acts as a man-in-the-middle proxy on the local machine, allowing inspection of all browser traffic. In this context, it's attached to the browser to capture the exact HTTP requests to Mandrillapp and subsequent redirects, revealing clear-text tokens before HTTPS. It's essential for simulating MITM without external network control, focusing on web application vulnerabilities.

## Features

- Feature 1: Request/response interception and editing
- Feature 2: History logging of all proxied traffic
- Feature 3: SSL/TLS decryption for HTTPS legs

## Installation

### Requirements

- Java runtime (for tools like Burp)
- Browser extension or system proxy configuration

### Install Commands

```bash
# For Burp Suite Community (example implementation)
# Download from portswigger.net/burp
java -jar burpsuite_community.jar
```

## Basic Usage

```bash
# Launch and configure proxy listener on 127.0.0.1:8080
```

### Common Options

| Option | Description |
|--------|-------------|
| `--host 127.0.0.1` | Bind to localhost |
| `--port 8080` | Listen on port 8080 |
| `--verbose` | Enable detailed logging |

## Examples

### Example 1: Basic Usage

Configure browser to use proxy at 127.0.0.1:8080 and access the target link.

### Example 2: Advanced Usage

Intercept and break on GET requests to mandrillapp.com:

Set breakpoint rules in the proxy UI for specific hosts.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Adversary-in-the-Middle]]

### Tactics

- [[Defense Evasion]]

## Detection

Indicators and methods for detecting this tool's usage:

- Proxy processes running locally (e.g., java for Burp)
- Browser proxy settings altered

## Related Procedures

- [[procedures/Intercept-Token-via-Network-Traffic-Capture]]

## Related Tools

- [[Burp-Suite]]
- [[OWASP-ZAP]]

## References

- Related resources: Proxy tool documentation for specific implementations
