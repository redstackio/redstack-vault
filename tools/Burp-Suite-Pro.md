---
url: 'https://portswigger.net/burp'
tags:
  - proxy
  - intercept
  - web
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:22.943Z'
id: 683a8404-90a5-4c71-a674-fbbf3155594e
validated: true
submitted: true
---
# Burp-Suite-Pro

**Status**: Unverified

## Overview

Burp Suite Pro is a comprehensive web vulnerability scanner and proxy tool used for intercepting, modifying, and replaying HTTP requests in security testing, particularly for identifying and exploiting web application flaws like race conditions.

## Description

Burp Suite Pro provides features like Proxy, Intruder, Repeater, and extensions support (e.g., Turbo Intruder). In offensive security, it's used to capture traffic, manipulate parameters, and automate attacks on web apps. For this exploit, it's essential for intercepting the redemption POST request.

## Features

- Feature 1: Traffic interception and modification via Proxy
- Feature 2: Extension ecosystem for advanced automation like Turbo Intruder
- Feature 3: Session handling and CSRF token management

## Installation

### Requirements

- Java 8+ runtime
- License for Pro version

### Install Commands

```bash
# Download from official site and run installer
java -jar burpsuite_pro.jar
```

## Basic Usage

```bash
burpsuite
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| --session | Load saved session |

## Examples

### Example 1: Basic Usage

Launch Burp and configure browser proxy to 127.0.0.1:8080 for interception.

### Example 2: Advanced Usage

Intercept request: Enable Intercept in Proxy > Intercept tab, then submit form in browser.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual User-Agent strings in logs (e.g., Burp's default)
- High volume of repeated requests from single IP

## Related Procedures


## Related Tools

- [[tools/Turbo-Intruder]]

## References

- Official documentation: https://portswigger.net/burp/documentation
- Related resources: PortSwigger Web Security Academy
