---
url: 'https://portswigger.net/burp'
tags:
  - proxy
  - intercept
  - web-testing
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:36.264Z'
id: 39f03e9b-1aa6-443e-9663-b77dd03f3311
validated: true
submitted: true
---
# HTTP-Proxy-Burp-Suite

**Status**: Unverified

## Overview

Burp Suite is a comprehensive platform for web application security testing, primarily used as an HTTP proxy to intercept, inspect, modify, and replay requests during vulnerability assessments like CAPTCHA bypasses and method tampering.

## Description

Burp Suite Professional includes Proxy, Repeater, Intruder, and other tools for manual and automated web attacks. In this context, it's used to tamper with HTTP methods and replay requests against WordPress APIs, enabling exploitation of business logic flaws without custom scripting.

## Features

- Feature 1: Real-time request interception and modification
- Feature 2: Repeater for manual request replay
- Feature 3: Support for HTTPS via CA certificate installation
- Feature 4: Session handling and scope limiting

## Installation

### Requirements

- Java 8+ runtime
- 4GB+ RAM for smooth operation

### Install Commands

```bash
# Download from official site (Community edition free)
# For Professional: License required
wget https://portswigger.net/burp/releases/download?product=pro&type=Linux -O burpsuite_pro.jar
java -jar burpsuite_pro.jar
```

## Basic Usage

```bash
# Launch Burp
java -jar burpsuite_community.jar
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help (in GUI, use Help menu) |
| `--no-startup` | Skip startup wizard |

## Examples

### Example 1: Basic Usage

Launch Burp, configure browser proxy to 127.0.0.1:8080, enable Intercept, and browse target.

### Example 2: Advanced Usage

Intercept a POST, send to Repeater, modify method to PUT, and send multiple times:

In Repeater tab: Edit > Send (repeat).

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual user-agent strings (Burp's default)
- High volume of repeated requests from single IP
- CA certificate mismatches in logs

## Related Procedures


## Related Tools

- [[tools/ZAP]]
- [[tools/Fiddler]]

## References

- Official documentation: https://portswigger.net/burp/documentation
- Related resources: OWASP Testing Guide
