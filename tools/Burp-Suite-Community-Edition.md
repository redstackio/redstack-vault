---
id: uuid-tool-1
url: 'https://portswigger.net/burp/communitydownload'
tags:
  - proxy
  - web-testing
  - vulnerability-scanner
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:26.955Z'
validated: true
submitted: true
---
# Burp-Suite-Community-Edition

**Status**: Unverified

## Overview

Burp Suite Community Edition is a free web vulnerability scanner and proxy tool used for intercepting, inspecting, and modifying HTTP/S traffic to test for issues like open redirects, XSS, and more in web applications.

## Description

It includes modules like Proxy for interception, Repeater for request replay, and an embedded browser for response viewing. Ideal for manual security testing of endpoints like Reddit's AMA form.

## Features

- Feature 1: Traffic interception and modification via proxy
- Feature 2: Request repeater for controlled sending
- Feature 3: Built-in browser for safe response rendering

## Installation

### Requirements

- Java 8 or higher
- 2GB RAM minimum

### Install Commands

```bash
# Download from official site and run
java -jar burpsuite_community_v2023.x.x.jar
```

## Basic Usage

```bash
# Launch Burp
java -jar burpsuite_community.jar
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help (via GUI) |
| `--no-update` | Disable auto-updates |

## Examples

### Example 1: Basic Usage

Launch Burp and configure proxy to 127.0.0.1:8080, then browse target site.

### Example 2: Advanced Usage

Use Repeater: Intercept request, send to Repeater, modify, and send.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Tactics

- [[Initial Access]]
- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual proxy traffic on port 8080
- Anomalous repeated requests from testing IPs

## Related Procedures


## Related Tools

- [[ZAP]]
- [[Wireshark]]

## References

- Official documentation: https://portswigger.net/burp/documentation
- Related resources: OWASP Testing Guide
