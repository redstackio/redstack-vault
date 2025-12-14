---
id: t1b2c3d4-e5f6-7890-abcd-ef1234567895
url: ''
tags:
  - proxy
  - intercept
  - web-testing
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-13T23:55:37.994Z'
validated: true
submitted: true
---
# Proxy

**Status**: Unverified

## Overview

Proxy tools like Burp Suite or OWASP ZAP are essential for intercepting and modifying HTTP/HTTPS traffic in web security testing, commonly used to manipulate requests in exploits like iFrame redirections for XSS chaining.

## Description

In offensive security, proxies act as man-in-the-middle to capture, inspect, and alter web requests/responses. For this attack, it intercepts forum iFrame loads to redirect to malicious URLs, enabling payload injection without direct server access. Features include request editing, replay, and scripting for automation.

## Features

- Feature 1: Real-time traffic interception and modification
- Feature 2: HTTPS decryption via CA certificate installation
- Feature 3: Request/response repeating and scripting

## Installation

### Requirements

- Java runtime (for Burp/ZAP)
- Administrative access for CA cert install

### Install Commands

```bash
# For Burp Suite (download from portswigger.net)
# Run via java -jar burpsuite.jar

# For OWASP ZAP
sudo apt update && sudo apt install zaproxy  # On Debian-based
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

```bash
# Launch Burp and configure browser proxy to 127.0.0.1:8080
java -jar burpsuite_community.jar
```
Intercept traffic and edit requests in the Proxy tab.

### Example 2: Advanced Usage

```bash
# In ZAP, use HUD mode for inline interception
zaproxy --hud
```
Redirect iFrame src by editing the GET request path.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual CA certificates in browser trust stores
- Anomalous proxy traffic patterns in network logs
- Modified requests with mismatched referers

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Burp Suite]]
- [[OWASP ZAP]]

## References

- Official documentation: portswigger.net/burp
- Related resources: OWASP testing guide
