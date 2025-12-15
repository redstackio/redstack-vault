---
id: uuid-10
url: 'https://portswigger.net/burp'
tags:
  - proxy
  - interception
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:12.504Z'
validated: true
submitted: true
---
# Intercepting-Proxy

**Status**: Unverified

## Overview

An intercepting proxy like Burp Suite captures, inspects, and modifies HTTP/HTTPS traffic between the browser and target server, essential for testing and exploiting web vulnerabilities such as endpoint manipulation.

## Description

In offensive security, it's used to analyze requests, tamper with parameters (e.g., email in POST bodies), and replay modified traffic. For this attack, it captures resend-verify requests for enumeration testing.

## Features

- Feature 1: Request/response interception and editing
- Feature 2: Traffic repeater for multiple sends
- Feature 3: Scope filtering for target-specific proxying

## Installation

### Requirements

- Java 8+ for Burp Suite
- Admin rights for proxy setup

### Install Commands

```bash
# Download and run Burp Suite Community (free)
java -jar burpsuite_community.jar
```

## Basic Usage

```bash
# Launch and configure proxy listener on 127.0.0.1:8080
# Set browser to use this proxy
```

### Common Options

| Option | Description |
|--------|-------------|
| Intercept on | Toggle to capture requests |
| Forward | Send modified request |
| Drop | Discard request |

## Examples

### Example 1: Basic Usage

Configure browser proxy, navigate to target, intercept POST request, edit email, forward.

### Example 2: Advanced Usage

Use Repeater tab: Paste captured request, modify, send multiple times with varying emails.

```bash
# Equivalent curl for repeat, but use UI for ease
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Account Discovery]] Account Discovery
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual user-agents or proxy headers in logs
- High volume of identical requests from single IP
- Anomalous referer or nonce values

## Related Procedures

- [[procedures/Intercept-and-Modify-Resend-Verify-Requests]]
- [[procedures/Manual-Username-Enumeration-via-Resend-Verify]]

## Related Tools

- [[tools/ZAP Proxy]]

## References

- Official documentation: https://portswigger.net/burp/documentation
- Related resources: OWASP Testing Guide
