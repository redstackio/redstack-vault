---
url: 'https://github.com/PortSwigger/ip-rotate'
tags:
  - ip-rotation
  - bypass
  - extension
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:28.110Z'
id: 7babf1c1-37b0-41a4-97ee-2962af514a3d
validated: true
submitted: true
---
# IP-Rotate

**Status**: Unverified

## Overview

IP Rotate is a Burp Suite extension that rotates source IP addresses during requests, ideal for bypassing IP-based rate limits in web vulnerability testing.

## Description

As a BApp Store extension, it integrates with Burp's Proxy, Repeater, and Intruder to cycle through proxy lists or VPNs, simulating multiple clients. In the Nextcloud attack, it's enabled in Intruder with null payloads to flood requests without hitting limits.

## Features

- Feature 1: Automatic IP switching per request
- Feature 2: Integration with Burp's attack tools
- Feature 3: Support for proxy chains and custom IP lists

## Installation

### Requirements

- Burp Suite Professional
- Extension manager access

### Install Commands

```bash
# In Burp: Extender > BApp Store > Search 'IP Rotate' > Install
# Or manual: Download JAR, Extender > Add > Select JAR
```

## Basic Usage

In Burp Extender > Extensions > IP Rotate > Configure proxies.

### Common Options

| Option | Description |
|--------|-------------|
| Proxy List | Comma-separated proxies |
| Rotation Mode | Per-request or per-thread |

## Examples

### Example 1: Basic Usage

Enable in Intruder Options, add proxies (e.g., 127.0.0.1:8081, 127.0.0.1:8082), start attack.

### Example 2: Advanced Usage

Configure with external proxy list file for large-scale rotation.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Denial of Service]] Network Denial of Service

### Tactics

- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Requests from known proxy/VPN IP ranges
- Rapid IP changes in access logs for same endpoint
- Correlated User-Agent consistency across IPs

## Related Procedures


## Related Tools

- [[tools/Burp-Suite]]
- [[tools/Tor]]

## References

- Official documentation: PortSwigger BApp Store
- Related resources: Burp Extensions GitHub
