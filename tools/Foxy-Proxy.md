---
id: tool-foxy-proxy-001
url: 'https://getfoxyproxy.org/'
tags:
  - proxy
  - browser
  - traffic-routing
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
  - Browser Extension
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:06.623Z'
validated: true
submitted: true
---
# Foxy-Proxy

**Status**: Unverified

## Overview

Foxy Proxy is a browser extension for managing proxy configurations, commonly used to route traffic through tools like Burp Suite for secure testing of web applications.

## Description

It simplifies switching proxies in Firefox or Chrome, ensuring all browser requests (e.g., profile updates) are captured by Burp without manual PAC file setup. Ideal for intermittent interception during IDOR testing.

## Features

- Feature 1: Easy toggle between proxy modes (e.g., Burp on 127.0.0.1:8080)
- Feature 2: Pattern-based routing for specific domains
- Feature 3: Integration with Burp for seamless traffic capture

## Installation

### Requirements

- Compatible browser (Firefox/Chrome)

### Install Commands

No CLI; install via browser store:

```bash
# For Firefox: Search 'FoxyProxy' in add-ons
# Enable and add proxy: 127.0.0.1:8080
```

## Basic Usage

```bash
# In browser: Toggle FoxyProxy to 'Use proxies: Burp'
```

### Common Options

| Option | Description |
|--------|-------------|
| `Enable` | Activate proxy for session |
| `Patterns` | Route specific URLs (e.g., target.com/*) |

## Examples

### Example 1: Basic Usage

Install extension, add proxy to localhost:8080, enable before profile update.

### Example 2: Advanced Usage

Set pattern for https://target.com/EditUserProfile/* to route through Burp only.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Extension presence in browser profiles
- Proxy headers or delays in request logs

## Related Procedures

- [[procedures/Intercept-and-Analyze-Profile-Update-Request]]
- [[procedures/Enumerate-Victims-User-ID]]

## Related Tools

- [[tools/Burp-Suite]]
- [[tools/Charles-Proxy]]

## References

- Official documentation: https://getfoxyproxy.org/help/
- Related resources: Browser proxy guides
