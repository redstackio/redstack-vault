---
id: tool-uuid-001
url: 'https://portswigger.net/burp'
name: HTTP-Proxy-Burp-Suite
tags:
  - proxy
  - interception
  - web-testing
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T00:11:16.190Z'
validated: true
submitted: true
---
# HTTP-Proxy-Burp-Suite

**Status**: Unverified

## Overview

Burp Suite is a comprehensive web vulnerability scanner and proxy tool used for intercepting, modifying, and replaying HTTP/S traffic, ideal for manual testing of web applications like Shopify for issues such as XSS.

## Description

Burp Suite acts as a man-in-the-middle proxy, allowing security testers to inspect and alter requests in real-time. In offensive operations, it's commonly used to inject payloads into parameters during app interactions, such as modifying CSV file names in Shopify requests to exploit stored XSS. Features include repeater for tweaking requests, intruder for fuzzing, and scanner for automated vuln detection.

## Features

- Feature 1: Proxy interception and modification of live traffic
- Feature 2: Repeater tool for manual request editing and resending
- Feature 3: Integration with browser for seamless session handling

## Installation

### Requirements

- Java Runtime Environment (JRE) 11+
- 4GB+ RAM for professional edition

### Install Commands

```bash
# Download and run (Community Edition)
wget https://portswigger.net/burp/releases/download?product=community&type=Linux -O burpsuite_community.jar
java -jar burpsuite_community.jar
```

## Basic Usage

```bash
java -jar burpsuite_community.jar
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `--no-sandbox` | Run without sandbox for compatibility |

## Examples

### Example 1: Basic Usage

Launch Burp and configure browser proxy to 127.0.0.1:8080, then browse to target to intercept traffic.

### Example 2: Advanced Usage

In Proxy > Intercept tab, capture POST, edit parameters (e.g., csv_file_name), and forward:

Use Repeater to test payload: Send modified request and observe response.

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

- Unusual proxy traffic on port 8080
- Anomalous delays in web requests due to interception
- Log entries showing modified headers or parameters

## Related Procedures

- [[procedures/Intercept-and-Inject-XSS-Payload]]

## Related Tools

- [[Related Tool: ZAP Proxy]]
- [[Related Tool: Fiddler]]

## References

- Official documentation: https://portswigger.net/burp/documentation
- Related resources: OWASP Testing Guide
