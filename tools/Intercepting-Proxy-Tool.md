---
id: tool-intercepting-proxy
url: null
tags:
  - proxy
  - man-in-the-middle
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:49.874Z'
validated: true
submitted: true
---
# Intercepting Proxy Tool

**Status**: Unverified

## Overview

Intercepting proxy tools like Burp Suite or OWASP ZAP capture and modify HTTP/S traffic, used here to relay and alter cookies during authentication bypass attacks.

## Description

These tools act as man-in-the-middle proxies, allowing inspection and editing of requests/responses. In the Uber exploit, it was used to inject stolen _csid cookies into SSO responses, bypassing protections.

## Features

- Feature 1: Traffic interception and modification
- Feature 2: Header editing (e.g., cookies, Set-Cookie)
- Feature 3: Scripting for automated relays

## Installation

### Requirements

- Java runtime for Burp/ZAP

### Install Commands

```bash
# For Burp Suite: Download from portswigger.net
# For ZAP: sudo apt install zaproxy
```

## Basic Usage

```bash
tool-name --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -proxy | Set as browser proxy |
| -intercept | Enable request/response breaks |

## Examples

### Example 1: Basic Usage

Configure browser to proxy through 127.0.0.1:8080, intercept auth.uber.com traffic.

### Example 2: Advanced Usage

Intercept response, edit Set-Cookie: _csid=victim_value, forward.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Pass the Hash]] Use Alternate Authentication Material: Pass the Cookie

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Anomalous proxy traffic in network logs
- Modified headers in auth requests

## Related Procedures

- [[procedures/Relay-Captured-Cookies-To-Bypass-Authentication]]

## Related Tools

- [[Burp Suite]]
- [[OWASP ZAP]]

## References

- Related resources: PortSwigger documentation
