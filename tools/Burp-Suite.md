---
id: tool-001
url: 'https://portswigger.net/burp'
tags:
  - proxy
  - web-testing
  - intercept
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:33:34.518Z'
validated: true
submitted: true
---
# Burp-Suite

**Status**: Unverified

## Overview

Burp Suite is a comprehensive platform for web application security testing, primarily used for intercepting, inspecting, and modifying HTTP/S traffic to identify and exploit vulnerabilities like the GitLab password reset issue.

## Description

Burp Suite Professional includes Proxy, Repeater, Intruder, and extensions for tasks like request manipulation. In offensive operations, it's essential for man-in-the-middle attacks on web apps, allowing payload alterations without custom scripts.

## Features

- Feature 1: Traffic interception and modification in real-time
- Feature 2: Request repeater for testing variations
- Feature 3: Extensible via BApp Store plugins for format conversions

## Installation

### Requirements

- Java 11+ runtime
- 4GB+ RAM for smooth operation

### Install Commands

```bash
# Download from official site and run
java -jar burpsuite_pro.jar
```

## Basic Usage

```bash
tool-name --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `--project-file` | Load/save project files |

## Examples

### Example 1: Basic Usage

Launch Burp and configure browser proxy to 127.0.0.1:8080 for interception.

### Example 2: Advanced Usage

Use Repeater: Intercept request, send to Repeater, modify, and resend.

```bash
# No CLI; GUI-based
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Valid Accounts]] Valid Accounts

### Tactics

- [[Initial Access]] Initial Access
- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual TLS certificate (Burp CA) in browser traffic
- High volume of repeated requests from single IP
- Proxy headers like X-Forwarded-For in logs

## Related Procedures

- [[procedures/Intercept-and-Convert-Reset-Request-to-JSON]]
- [[procedures/Modify-JSON-Payload-for-Email-Injection]]

## Related Tools

- [[tools/ZAP]]
- [[tools/Fiddler]]

## References

- Official documentation: https://portswigger.net/burp/documentation
- Related resources: OWASP Testing Guide
