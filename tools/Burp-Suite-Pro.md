---
url: 'https://portswigger.net/burp'
tags:
  - proxy
  - web-testing
  - tampering
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: >-
  Professional web vulnerability scanner and proxy for intercepting, modifying,
  and replaying HTTP/S traffic.
id: 863c4b36-5d81-47b3-ac82-4047226fc772
created_at: '2025-12-14T05:32:10.170Z'
updated_at: '2025-12-14T05:32:10.170Z'
verified: false
validated: true
submitted: true
---
# Burp-Suite-Pro

**Status**: Unverified

## Overview

Burp Suite Pro is a comprehensive toolkit for web application security testing, primarily used for manual and automated exploration of web vulnerabilities like parameter tampering, file upload bypasses, and request manipulation. In offensive security, it's essential for intercepting traffic in scenarios like this LISTSERV exploit to modify uploads.

## Description

Burp Suite Pro includes modules like Proxy (for interception), Repeater (for manual tampering), Intruder (for fuzzing), and Scanner (for automated vuln detection). It excels in handling complex payloads like multipart/form-data for file uploads, allowing precise edits to parameters and bodies without breaking protocols. Commonly used in pentests to simulate attacks on web apps like CGI scripts.

## Features

- Feature 1: Real-time HTTP/S proxy with breakpoint interception for request/response modification
- Feature 2: Repeater tool for iterative testing of tampered requests
- Feature 3: Support for encoding/decoding binary data in payloads, ideal for file appends

## Installation

### Requirements

- Java 11+ runtime
- 4GB+ RAM for Pro features

### Install Commands

```bash
# Download from official site (requires license)
wget https://portswigger.net/burp/releases/download?product=pro&type=Linux -O burpsuite_pro.jar
java -jar burpsuite_pro.jar
```

## Basic Usage

```bash
java -jar burpsuite_pro.jar
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `--no-update` | Skip auto-updates |

## Examples

### Example 1: Basic Usage

Launch Burp and configure browser proxy to 127.0.0.1:8080 for interception.

### Example 2: Advanced Usage

In Proxy > Options, enable invisible proxying. Intercept a POST, send to Repeater, modify params, and send.

```bash
# No CLI for advanced; GUI-based
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Remote File Copy]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual user agents (Burp defaults to 'BurpSuite')
- High volume of repeated requests from single IP
- Proxy-like delays in traffic patterns

## Related Procedures


## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- Official documentation: https://portswigger.net/burp/documentation
- Related resources: OWASP Testing Guide
