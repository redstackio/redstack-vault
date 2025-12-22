---
url: 'https://portswigger.net/burp'
tags:
  - proxy
  - intercept
  - xss
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:33.776Z'
id: ed60a886-bcd0-4e0c-81c3-0c4720e005f7
validated: true
submitted: true
---
# Web-Intercept-Proxy

**Status**: Unverified

## Overview

A web intercept proxy, such as Burp Suite, is used in security testing to capture, inspect, and modify HTTP/HTTPS traffic between a client browser and a web server. It is essential for tampering with form submissions, like injecting XSS payloads during checkout processes in applications such as WooCommerce.

## Description

Web intercept proxies act as man-in-the-middle tools, allowing pentesters to break and resume requests, edit parameters, and replay traffic. In offensive operations, they enable bypassing client-side validation by altering POST data on-the-fly, facilitating attacks like parameter injection for XSS or other vulnerabilities. Common in web app testing, they support decoding/encoding, fuzzing, and scanning integrations.

## Features

- Feature 1: Request interception and modification in real-time.
- Feature 2: Support for HTTPS via CA certificate installation.
- Feature 3: Built-in repeater and intruder for manual/automated testing.

## Installation

### Requirements

- Java Runtime Environment (JRE) 8 or higher.
- Browser configuration to use the proxy (e.g., set to 127.0.0.1:8080).

### Install Commands

```bash
# For Burp Suite Community (free edition)
# Download from official site and run: java -jar burpsuite_community.jar
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

Launch Burp Suite, configure browser proxy to 127.0.0.1:8080, enable Intercept in Proxy tab, and submit a form to capture/modify requests.

### Example 2: Advanced Usage

```bash
# In Burp: Intercept on, edit POST params like billing_state="><script>alert(1)</script>, forward request
```
Intercept checkout POST, URL-decode and modify state parameter to include XSS payload, then forward to complete injection.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]
- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual proxy traffic or CA certificates in browser trust stores.
- Anomalous request modifications logged in server access logs (e.g., encoded payloads).

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Burp-Suite]]
- [[ZAP]]

## References

- Official documentation: https://portswigger.net/burp/documentation
- Related resources: OWASP Testing Guide
