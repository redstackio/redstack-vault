---
id: tool-2140960-001
url: null
tags:
  - proxy
  - http-intercept
  - api-testing
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:30:35.334Z'
validated: true
submitted: true
---
# HTTP-Proxy

**Status**: Unverified

## Overview

HTTP Proxy tools like Burp Suite or ZAP are used for intercepting, inspecting, modifying, and replaying web traffic, essential for testing API endpoints like GraphQL for access control issues.

## Description

In offensive security, HTTP proxies facilitate manipulation of requests to bypass controls, such as altering parameters in API calls to access unauthorized data. For this vulnerability, it allows pasting raw requests, editing userIds, and sending to X's GraphQL API without browser limitations.

## Features

- Feature 1: Request interception and modification in real-time
- Feature 2: Header and parameter editing with URL decoding support
- Feature 3: Response viewing and repeating for iterative testing

## Installation

### Requirements

- Java Runtime Environment (for Burp/ZAP)
- Network interface for proxying traffic

### Install Commands

```bash
# For Burp Suite (download from portswigger.net)
# No CLI install; run JAR: java -jar burpsuite_pro.jar

# For OWASP ZAP
sudo apt update && sudo apt install zaproxy  # On Debian-based
```

## Basic Usage

```bash
# Configure browser to proxy through 127.0.0.1:8080
# In tool: Intercept > On, then navigate to target
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help (tool-specific) |
| `--verbose` | Enable detailed logging |

## Examples

### Example 1: Basic Usage

Intercept traffic: Set proxy in browser, load X.com, capture likes request in Repeater tab.

### Example 2: Advanced Usage

```bash
# In Burp Repeater: Paste request, edit variables, click Send
# View JSON response for hidden likes data
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Account Discovery]] Account Discovery

### Tactics

- [[Discovery]] Discovery
- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual outbound traffic to proxy ports (e.g., 8080)
- Anomalous User-Agent or header patterns in logs

## Related Procedures

- [[procedures/Modify-and-Send-Proxy-Request-for-Hidden-Likes]]

## Related Tools

- [[Burp Suite]]
- [[OWASP ZAP]]

## References

- PortSwigger Burp Suite Documentation
- OWASP ZAP User Guide
