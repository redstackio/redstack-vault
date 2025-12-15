---
id: tool-burpsuite
url: 'https://portswigger.net/burp'
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
updated_at: '2025-12-14T17:24:41.826Z'
validated: true
submitted: true
---
# BurpSuite

**Status**: Unverified

## Overview

BurpSuite is a comprehensive toolkit for web application security testing, primarily used for intercepting, inspecting, and modifying HTTP/S traffic between clients and servers. In offensive security, it's essential for discovering vulnerabilities like authentication weaknesses in mobile and web apps.

## Description

BurpSuite includes modules like Proxy for traffic interception, Repeater for manual request manipulation, Intruder for automated attacks (e.g., brute force), and Scanner for automated vulnerability detection. For mobile testing, it excels at proxying iOS/Android traffic after certificate installation, allowing replay of API calls without app modifications. The Professional edition adds advanced features like active scanning; Community is free for manual testing.

## Features

- Feature 1: Proxy interception with CA certificate generation for HTTPS
- Feature 2: Repeater and Intruder for request fuzzing and brute forcing
- Feature 3: Session handling and macros for stateful app testing

## Installation

### Requirements

- Java 11+ runtime
- 4GB+ RAM for smooth operation

### Install Commands

```bash
# Download from official site, then run
java -jar burpsuite_community_v2023.x.x.jar
```

For Linux: Add to PATH or use package managers like `apt install burpsuite` on Kali.

## Basic Usage

```bash
# Launch BurpSuite
java -jar burpsuite.jar
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help (via jar launch) |
| `--no-startup` | Skip welcome screen |

## Examples

### Example 1: Basic Usage

Launch Burp, configure Proxy listener, set browser proxy to 127.0.0.1:8080, and intercept requests.

### Example 2: Advanced Usage

```bash
# For mobile proxy: Bind to 0.0.0.0:8080, generate CA, install on device
# In UI: Proxy > Options > Add listener > Bind to port 8080, All interfaces
```
Use Repeater: Right-click request > Send to Repeater > Modify and Go.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Brute Force]] Brute Force

### Tactics

- [[Initial Access]] Initial Access
- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing traffic to localhost:8080 or unusual proxy chains
- Presence of Burp CA certificates on endpoints
- High request volumes from Burp user-agent strings

## Related Procedures


## Related Tools

- [[tools/ZAP]]
- [[tools/Charles-Proxy]]

## References

- Official documentation: https://portswigger.net/burp/documentation
- Related resources: OWASP Mobile Testing Guide
