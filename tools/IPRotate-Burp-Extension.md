---
url: 'https://github.com/RhinoSecurityLabs/IPRotate_Burp_Extension'
tags:
  - burp
  - proxy
  - extension
type: tool
platforms:
  - Web
description: >-
  Burp Suite extension for rotating IP addresses via proxies during web attacks
  like brute-forcing.
id: b665d18e-816e-406b-9d3e-0b071099680d
created_at: '2025-12-14T17:30:26.687Z'
updated_at: '2025-12-14T17:30:26.687Z'
verified: false
validated: true
submitted: true
---
# IPRotate-Burp-Extension

**Status**: Unverified

## Overview

Burp Suite extension that automates IP rotation using proxy chains, facilitating bypass of rate limits in tools like Intruder for credential brute-force.

## Description

Integrates with Burp's proxy and scanner; configure proxy lists to rotate on each request, ideal for MoPub-like endpoints.

## Features

- Feature 1: Automatic proxy switching
- Feature 2: Integration with Burp Intruder
- Feature 3: Custom rotation intervals

## Installation

### Requirements

- Burp Suite Professional
- Jython or Java

### Install Commands

```bash
# Download JAR from GitHub, load in Burp Extender
# No CLI install; manual in Burp UI
```

## Basic Usage

Load extension in Burp > Extender > Extensions.

### Common Options

| Option | Description |
|--------|-------------|
| Proxy List | Configure rotating proxies |
| Rotation Mode | Per-request or interval |

## Examples

### Example 1: Basic Usage

In Burp Intruder, enable IPRotate for payload positions in login requests.

### Example 2: Advanced Usage

Set up chain: Burp > IPRotate proxies > Target.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Connection Proxy]] Proxy
- [[Brute Force]] Brute Force

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Requests from chained proxies
- Burp-like User-Agents in logs

## Related Procedures

- [[procedures/Alternative-Bypass-with-AWS-API-Gateway-or-Bash-Proxy-Script]]

## Related Tools

- [[tools/curl]]

## References

- GitHub: https://github.com/RhinoSecurityLabs/IPRotate_Burp_Extension
