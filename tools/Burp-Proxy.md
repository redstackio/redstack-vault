---
url: 'https://portswigger.net/burp/documentation/desktop/proxy'
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
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:30.794Z'
id: 996f2d36-65aa-4e02-b5dd-a62122fd30e3
validated: true
submitted: true
---
# Burp-Proxy

**Status**: Unverified

## Overview

Burp Proxy is a component of Burp Suite used for intercepting, inspecting, and modifying HTTP/S traffic between the browser and target web application, ideal for capturing session cookies in security testing.

## Description

Burp Proxy acts as a man-in-the-middle to log requests and responses, allowing pentesters to analyze authentication mechanisms like cookies and CSRF tokens. It's commonly used in web vulnerability assessments to capture artifacts for replay attacks.

## Features

- Feature 1: Real-time request interception and editing
- Feature 2: History logging of all traffic
- Feature 3: Integration with other Burp tools like Repeater

## Installation

### Requirements

- Java 8 or higher
- Burp Suite Professional or Community Edition

### Install Commands

```bash
# Download and run Burp Suite (Java-based)
java -jar burpsuite_pro_v2023.x.x.jar
```

## Basic Usage

```bash
# Launch Burp and configure proxy listener on 127.0.0.1:8080
# No CLI; GUI-based
```

### Common Options

| Option | Description |
|--------|-------------|
| Intercept | Toggle to capture requests |
| Forward | Send intercepted request to server |
| Drop | Discard request |

## Examples

### Example 1: Basic Usage

Configure browser to use proxy at 127.0.0.1:8080, navigate to target, and intercept requests to capture cookies.

### Example 2: Advanced Usage

```bash
# In Burp GUI: Proxy > Options > Add listener, then Intercept > On for cookie capture
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Pass the Hash]] Pass the Ticket

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual proxy traffic on port 8080
- Anomalous delays in web requests due to interception

## Related Procedures


## Related Tools

- [[tools/Burp-Repeater]]
- [[tools/ZAP-Proxy]]

## References

- Official documentation: https://portswigger.net/burp/documentation
- Related resources: OWASP Testing Guide
