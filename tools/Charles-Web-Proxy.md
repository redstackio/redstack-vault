---
id: k1l2m3n4-o5p6-7890-klmn-123456789012
url: 'https://www.charlesproxy.com/'
tags:
  - proxy
  - interception
type: tool
verified: false
platforms:
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:42.896Z'
validated: true
submitted: true
---
# Charles-Web-Proxy

**Status**: Unverified

## Overview

Web debugging proxy for intercepting and analyzing HTTP/HTTPS traffic from apps and browsers.

## Description

Charles captures mobile app requests, enabling header extraction like x-mts-ssid from Grab API calls. Configured with emulators for Android testing.

## Features

- Feature 1: SSL proxying for HTTPS
- Feature 2: Request/response modification
- Feature 3: Traffic logging and filtering

## Installation

### Requirements

- Java 8+

### Install Commands

```bash
# Download and run installer
# macOS: brew install --cask charles
```

## Basic Usage

```bash
# Launch Charles, enable proxy on port 8888
charles &  # Background
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Help |
| --port | Custom port |

## Examples

### Example 1: Basic Usage

Start Charles, set client proxy to localhost:8888.

### Example 2: Advanced Usage

Enable SSL proxying: Tools > SSL Proxying > Enable for host p.grabtaxi.com.

## MITRE ATT&CK Mapping

### Techniques

- [[Network Sniffing]] Network Sniffing

### Tactics

- [[Discovery]] Discovery

## Detection

- Proxy port 8888 traffic
- Certificate pinning bypass attempts

## Related Procedures


## Related Tools

- [[tools/Burp-Suite]]
- [[tools/Fiddler]]

## References

- Official documentation: https://www.charlesproxy.com/documentation/
