---
url: 'https://portswigger.net/burp'
tags:
  - web-proxy
  - intercept
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:22.885Z'
id: 9ce69e42-34cf-4901-8714-50392ef0a9fb
validated: true
submitted: true
---
---

# Burp-Suite

**Status**: Unverified

## Overview

Burp Suite is a comprehensive toolkit for web application security testing, primarily used for intercepting, modifying, and analyzing HTTP/S traffic to identify vulnerabilities like arbitrary file uploads.

## Description

Burp Suite's capabilities include proxy interception, repeater for request manipulation, and intruder for fuzzing parameters. In offensive security, it's essential for exploiting web flaws by capturing upload requests and altering paths or payloads to test for directory traversal and extension bypasses.

## Features

- Feature 1: Proxy for real-time traffic interception and modification
- Feature 2: Repeater module to manually edit and resend requests
- Feature 3: Scanner for automated vulnerability detection

## Installation

### Requirements

- Java Runtime Environment (JRE) 11 or higher
- Sufficient RAM (at least 4GB recommended)

### Install Commands

```bash
# Download from official site and run
java -jar burpsuite_community.jar
```

## Basic Usage

```bash
# Launch Burp Suite
burpsuite
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `--no-update` | Disable automatic updates |

## Examples

### Example 1: Basic Usage

```bash
# Configure browser proxy to 127.0.0.1:8080 and intercept traffic
# In Burp: Proxy > Intercept > On
```

### Example 2: Advanced Usage

```bash
# Use Repeater: Intercept upload request, modify path parameter, forward
# Example: Change 'path=profile/' to 'path=../../other/'
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Drive-by Compromise]]

### Tactics

- [[Initial Access]]
- [[Privilege Escalation]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual proxy traffic on port 8080
- Anomalous HTTP requests with modified headers or payloads in logs

## Related Procedures

- [[procedures/Exploit-Arbitrary-File-Upload-via-Profile-Photo]]

## Related Tools

- [[ZAP]]
- [[Wireshark]]

## References

- Official documentation: https://portswigger.net/burp/documentation
- Related resources: OWASP Testing Guide
