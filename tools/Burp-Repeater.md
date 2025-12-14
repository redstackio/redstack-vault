---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
url: 'https://portswigger.net/burp/documentation/desktop/tools/repeater'
tags:
  - web-proxy
  - xss-testing
  - http-manipulation
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T03:46:31.380Z'
validated: true
submitted: true
---
# Burp-Repeater

**Status**: Unverified

## Overview

Burp Repeater is a core component of Burp Suite, a professional web vulnerability scanner, used for manually intercepting, modifying, and replaying HTTP requests to test for issues like XSS, SQLi, and authentication bypasses in web applications.

## Description

Burp Repeater allows precise control over HTTP traffic by letting users edit requests parameter-by-parameter and resend them to the server. It's ideal for crafting payloads in scenarios like reflected XSS, where requests need URL-encoding and repeated testing. Integrated with Burp's Proxy and Intruder, it supports offensive security operations on platforms like WordPress by simulating user interactions without full automation.

## Features

- Feature 1: Request/response editing with syntax highlighting and auto-formatting
- Feature 2: Built-in encoders/decoders for payloads (e.g., URL, HTML, Base64)
- Feature 3: History of sent requests for comparison and chaining attacks

## Installation

### Requirements

- Java Runtime Environment (JRE) 11 or higher
- 4GB+ RAM for smooth operation

### Install Commands

```bash
# Download from PortSwigger (community edition free)
# No install; run the JAR
java -jar burpsuite_community_v2023.x.x.jar
```

## Basic Usage

```bash
tool-name --help
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Burp Repeater is GUI-based; launched via Burp Suite interface |
| Proxy integration | Automatically captures from Proxy tab |

## Examples

### Example 1: Basic Usage

Launch Burp Suite, enable Intercept in Proxy, submit a form on target site, forward to Repeater, edit, and send.

### Example 2: Advanced Usage

```bash
# In Repeater: Edit body, use Inspector for params, send multiple times with variations
```

For XSS: Paste request, modify param, encode payload, send, inspect response.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]
- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual User-Agent strings (e.g., Burp/2023.x) in server logs
- Detection method 2: Repeated identical requests from single IP with modified params

## Related Procedures


## Related Tools

- [[Burp-Suite]]
- [[ZAP]]

## References

- Official documentation: https://portswigger.net/burp/documentation
- Related resources: OWASP Testing Guide
