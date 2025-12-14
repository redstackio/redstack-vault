---
id: tool-uuid-foxy-proxy
url: 'https://getfoxyproxy.org/'
tags:
  - proxy
  - browser-extension
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:48.135Z'
validated: true
submitted: true
---
# Foxy-Proxy

**Status**: Unverified

## Overview

FoxyProxy is a browser extension that simplifies switching between proxies, commonly used to route web traffic through tools like Burp Suite for security testing and interception.

## Description

It allows quick toggling of proxy configurations without manual browser settings changes. In web vuln exploitation, it's paired with Burp to capture application requests, enabling payload modification for SSRF testing without disrupting normal browsing.

## Features

- Feature 1: Pattern-based proxy switching
- Feature 2: Integration with Burp, ZAP, etc.
- Feature 3: Whitelisting/blacklisting for selective routing

## Installation

### Requirements

- Firefox or Chrome browser

### Install Commands

```bash
# Install via browser extension store; no CLI needed
# For Firefox: https://addons.mozilla.org/en-US/firefox/addon/foxyproxy-standard/
```

## Basic Usage

```bash
# In extension: Add pattern for target domain, set proxy to 127.0.0.1:8080 (Burp)
```

### Common Options

| Option | Description |
|--------|-------------|
| Enable | Activate proxy for current session |
| Use patterns | Route specific URLs via proxy |
| Disable | Revert to direct connection |

## Examples

### Example 1: Basic Usage

Configure proxy for `https://target.com/*` to localhost:8080; enable to route all target traffic through Burp.

### Example 2: Advanced Usage

Set up multiple proxies: One for Burp interception, another for direct access to avoid loops.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Protocol Tunneling]] Protocol Tunneling (for proxy chaining)

### Tactics

- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Extension presence in browser profiles
- Proxy headers or delays in requests
- Inconsistent User-Agent with proxy use

## Related Procedures


## Related Tools

- [[tools/Burp-Suite]]
- [[tools/Proxy-SwitchyOmega]]

## References

- Official documentation: https://getfoxyproxy.org/help/
- Related resources: Browser extension repositories
