---
id: tool-uuid-2
url: 'https://www.zaproxy.org/'
tags:
  - proxy
  - web-testing
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:34.254Z'
validated: true
submitted: true
---
# OWASP ZAP

**Status**: Unverified

## Overview

OWASP ZAP (Zed Attack Proxy) is an open-source web app security scanner and proxy, alternative to Burp for intercepting and modifying requests.

## Description

Used here as an alternative to Burp Suite for capturing Remitly password reset requests and tokens during the initiation phase.

## Features

- Feature 1: Built-in proxy and request editor
- Feature 2: Active/passive scanning
- Feature 3: Scripting support for custom attacks

## Installation

### Requirements

- Java 8+ or Docker

### Install Commands

```bash
# Ubuntu: sudo apt install zaproxy
# Or download JAR: java -jar ZAP_2.14.0.jar
```

## Basic Usage

```bash
# Launch: zap.sh -cmd -autorun manual_explore
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h` | Help |
| `-port 8080` | Set proxy port |

## Examples

### Example 1: Basic Usage

Set browser proxy to 127.0.0.1:8080, launch ZAP, intercept requests.

### Example 2: Advanced Usage

Use Manual Request tool to edit and resend.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Valid Accounts]] Valid Accounts

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Proxy-like request timings and headers
- Installed ZAP root CA in browser trust store

## Related Procedures


## Related Tools

- [[tools/Burp-Suite]]

## References

- Official documentation: https://www.zaproxy.org/docs/
