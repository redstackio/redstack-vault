---
id: tool-burp-proxy-001
url: 'https://portswigger.net/burp'
tags:
  - proxy
  - intercept
  - web
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.717Z'
validated: true
submitted: true
---
# Burp-Suite-Proxy

**Status**: Unverified

## Overview

Burp Suite Proxy is a component of the Burp Suite web vulnerability scanner used for intercepting, inspecting, and modifying HTTP/S traffic between the browser and target server, essential for manual testing like SSRF exploitation.

## Description

It acts as a man-in-the-middle proxy, allowing capture of requests (e.g., Tumblr API calls) for editing parameters like 'url' in SSRF tests. Common in pentesting for request tampering without custom scripts.

## Features

- Feature 1: Real-time request/response interception and editing
- Feature 2: CA certificate generation for HTTPS decryption
- Feature 3: History logging and search for traffic analysis

## Installation

### Requirements

- Java 8+ runtime
- 2GB RAM minimum

### Install Commands

```bash
# Download from portswigger.net; run java -jar burpsuite_community.jar
wget https://portswigger.net/burp/releases/download?product=community&type=Linux -O burpsuite.jar
java -jar burpsuite.jar
```

## Basic Usage

```bash
# Launch and configure browser proxy to 127.0.0.1:8080
```

### Common Options

| Option | Description |
|--------|-------------|
| Intercept | Toggle on/off for pausing requests |
| Forward | Send intercepted request |
| Drop | Discard request |

## Examples

### Example 1: Basic Usage

Configure browser proxy, browse to tumblr.com, intercept follow request, edit URL, forward.

### Example 2: Advanced Usage

```bash
# In Burp: Proxy > Options > Add listener on 8080; Intercept > On; modify and forward API call
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual proxy traffic on port 8080 from testing environments
- CA certificate mismatches in browser
- Log entries for modified requests

## Related Procedures


## Related Tools

- [[Related Tool: Burp-Suite-Intruder]]

## References

- Official documentation: https://portswigger.net/burp/documentation
- Related resources: OWASP Testing Guide
