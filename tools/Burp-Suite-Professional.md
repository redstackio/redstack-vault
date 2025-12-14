---
id: tool-uuid-burp
url: 'https://portswigger.net/burp'
tags:
  - web-proxy
  - vulnerability-scanner
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:32.078Z'
validated: true
submitted: true
---
# Burp Suite Professional

**Status**: Unverified

## Overview

Burp Suite Professional is a comprehensive toolkit for web application security testing, used here for intercepting, modifying, and replaying HTTP requests to discover XSS and CSRF vulnerabilities in profile update endpoints.

## Description

Burp Suite provides proxy interception, request manipulation via Repeater, and PoC generation capabilities. In offensive operations, it's essential for analyzing traffic, injecting payloads, and validating exploits like reflected XSS in parameters such as frm_email.

## Features

- Feature 1: Proxy for real-time traffic interception and modification
- Feature 2: Repeater for manual request testing and payload injection
- Feature 3: Intruder for automated fuzzing of parameters

## Installation

### Requirements

- Java 8 or higher
- 4GB RAM minimum

### Install Commands

```bash
# Download from official site and run
java -jar burpsuite_pro.jar
```

## Basic Usage

```bash
# Launch the tool
gui
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v, --verbose` | Verbose output |

## Examples

### Example 1: Basic Usage

Configure browser proxy to 127.0.0.1:8080 and intercept requests in the Proxy tab.

### Example 2: Advanced Usage

Send request to Repeater: Right-click > Send to Repeater, then modify parameters and send.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning
- [[JavaScript]] JavaScript

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual proxy traffic on port 8080
- CA certificate mismatches in logs
- Frequent request modifications in WAF

## Related Procedures


## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- Official documentation: https://portswigger.net/burp/documentation
- Related resources: OWASP Testing Guide
