---
id: tool-firefox-quantum
url: 'https://www.mozilla.org/en-US/firefox/new/'
tags:
  - browser
  - web
  - testing
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:29.143Z'
configuration: Version 59.0.2
validated: true
submitted: true
---
# Firefox-Quantum

**Status**: Unverified

## Overview

Firefox Quantum is a web browser used for navigating and testing web applications, configurable as a client for proxy tools like Burp Suite in security assessments.

## Description

As an open-source browser, Firefox supports extensions for developer tools and proxy configuration, making it ideal for manual testing of web vulnerabilities. Version 59.0.2 was used in this scenario for accessing Steam Community pages and proxying traffic.

## Features

- Feature 1: Built-in Developer Tools for inspecting elements and network
- Feature 2: Proxy settings for integration with security tools
- Feature 3: Extension support for additional testing capabilities

## Installation

### Requirements

- Standard OS with graphical interface

### Install Commands

```bash
# On Ubuntu
sudo apt update && sudo apt install firefox
# Or download from Mozilla
```

## Basic Usage

```bash
firefox https://steamcommunity.com
```

### Common Options

| Option | Description |
|--------|-------------|
| `-P` | Open profile manager |
| `--no-remote` | Allow multiple instances |

## Examples

### Example 1: Basic Usage

```bash
firefox --proxy-server=127.0.0.1:8080 https://steamcommunity.com
```

### Example 2: Advanced Usage

Launch with proxy for Burp: Set manual proxy in Preferences > Network Settings to HTTP 127.0.0.1:8080.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- User-Agent strings in logs
- Proxy configuration anomalies

## Related Procedures


## Related Tools

- [[tools/Chrome]]
- [[tools/Safari]]

## References

- Official documentation: https://support.mozilla.org/en-US/products/firefox
- Related resources: Mozilla Developer Network
