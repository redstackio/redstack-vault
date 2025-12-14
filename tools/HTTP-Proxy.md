---
id: tool-uuid-1
url: 'https://portswigger.net/burp/documentation'
tags:
  - proxy
  - traffic-interception
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:10.140Z'
description: >-
  A tool for intercepting and analyzing HTTP traffic during web vulnerability
  testing.
validated: true
submitted: true
---
# HTTP-Proxy

**Status**: Unverified

## Overview

HTTP Proxy tools, such as Burp Suite, are essential for intercepting, inspecting, and modifying web traffic in security assessments, particularly for verifying file uploads and payload executions in web applications like ExpressionEngine.

## Description

These tools act as man-in-the-middle proxies to capture requests and responses, allowing testers to observe server behavior during exploits like arbitrary file uploads. Commonly used in offensive security to debug and confirm vulnerabilities without direct server access.

## Features

- Feature 1: Request interception and modification
- Feature 2: Traffic logging and replay
- Feature 3: Integration with browsers via PAC files

## Installation

### Requirements

- Java Runtime Environment (for Burp Suite)
- Administrative privileges for proxy setup

### Install Commands

```bash
# For Burp Suite Community (download from official site)
# No CLI install; run jar file
java -jar burpsuite_community.jar
```

## Basic Usage

```bash
tool-name --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v, --verbose` | Verbose output |

## Examples

### Example 1: Basic Usage

```bash
# Configure browser to use proxy at 127.0.0.1:8080
# Intercept traffic during form submission
```

### Example 2: Advanced Usage

```bash
# In Burp, enable intercept on target requests to /images/avatars/
# Observe file download response
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Sniffing]]
- [[Adversary-in-the-Middle]]

### Tactics

- [[Collection]]
- [[Impact]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual proxy traffic on network segments
- Anomalous HTTP headers in logs (e.g., X-Forwarded-For mismatches)

## Related Procedures


## Related Tools

- [[Burp Suite]]
- [[ZAP]]

## References

- Official documentation: https://portswigger.net/burp
- Related resources: OWASP Testing Guide
