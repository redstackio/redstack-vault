---
id: d4e5f6g7-h8i9-0123-defg-456789012345
url: 'https://portswigger.net/burp/documentation/desktop/getting-started'
tags:
  - proxy
  - traffic-analysis
  - web-security
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:12.012Z'
validated: true
submitted: true
---
# Local-Proxy-for-Traffic-Monitoring

**Status**: Unverified

## Overview

A local proxy tool, such as Burp Suite or mitmproxy, used to intercept, inspect, and modify HTTP/HTTPS traffic between the browser and target servers, ideal for detecting information leaks like Referer header exposures in web applications.

## Description

Local proxies act as man-in-the-middle for web traffic, allowing security researchers to monitor requests and responses in real-time. In offensive security, they are crucial for identifying misconfigurations like referrer policy failures that lead to sensitive data leakage to third parties.

## Features

- Feature 1: Real-time traffic interception and logging
- Feature 2: Header inspection and modification
- Feature 3: HTTPS decryption with CA certificate installation

## Installation

### Requirements

- Java Runtime Environment (for Burp Suite)
- Python (for mitmproxy alternative)

### Install Commands

```bash
# For Burp Suite Community (download from official site)
# No CLI install; run JAR file
java -jar burpsuite_community.jar

# Alternative: mitmproxy
pip install mitmproxy
```

## Basic Usage

```bash
mitmproxy --mode transparent
```

### Common Options

| Option | Description |
|--------|-------------|
| `-p, --port` | Specify listening port (default 8080) |
| `-v, --verbose` | Increase verbosity for detailed logs |

## Examples

### Example 1: Basic Usage

```bash
mitmproxy
```

Run mitmproxy and configure browser to use localhost:8080 as proxy to start intercepting traffic.

### Example 2: Advanced Usage

```bash
mitmproxy --set confdir=~/.mitmproxy --listen-port 8080
```

Capture traffic while loading a page, then filter logs for Referer headers.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Sniffing]] Network Sniffing

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual proxy settings in browser configurations
- Detection method 2: CA certificate mismatches in HTTPS handshakes

## Related Procedures


## Related Tools

- [[Burp Suite]]
- [[Wireshark]]

## References

- Official documentation: https://docs.mitmproxy.org/stable/
- Related resources: OWASP Testing Guide on Proxies
