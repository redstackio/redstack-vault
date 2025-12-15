---
url: 'https://www.charlesproxy.com/'
tags:
  - proxy
  - web
  - debug
type: tool
verified: false
platforms:
  - macOS
  - Windows
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:36.045Z'
id: 5fd0cd15-0160-4efb-b368-d1478af111a4
validated: true
submitted: true
---
# Charles-Proxy

**Status**: Unverified

## Overview

Charles is a web debugging proxy used in security testing to intercept, inspect, and modify HTTP/HTTPS traffic, ideal for analyzing API requests like CSRF exploits.

## Description

Charles acts as a man-in-the-middle proxy, allowing capture of requests to endpoints such as Yelp's auto-api. Features include SSL decryption, request replay, and breakpoint editing. In offensive security, it's used to dissect vulnerable requests, save sessions, and simulate attacks without browser interference.

## Features

- Feature 1: SSL proxying for HTTPS inspection
- Feature 2: Request/response modification and replay
- Feature 3: Traffic throttling and bandwidth simulation

## Installation

### Requirements

- Java 8+ runtime
- Admin privileges for proxy setup

### Install Commands

```bash
# Download from official site; no CLI install, GUI app
# For macOS: brew install --cask charles
```

## Basic Usage

```bash
# Launch GUI and configure system proxy to 127.0.0.1:8888
charles
```

### Common Options

| Option | Description |
|--------|-------------|
| Enable SSL Proxying | Decrypt HTTPS traffic |
| Breakpoints | Pause and edit requests |
| Save Session | Export captured traffic |

## Examples

### Example 1: Basic Usage

Intercept browser traffic to auto-api.yelp.com and inspect POST to /account/create_secure.

### Example 2: Advanced Usage

```bash
# Replay a captured request
# In GUI: Right-click request > Repeat
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Proxy traffic on port 8888
- Anomalous CA certificate in trust store
- Logs showing intercepted requests

## Related Procedures


## Related Tools

- [[Burp Suite]]
- [[Wireshark]]

## References

- Official documentation: https://www.charlesproxy.com/documentation/
- Related resources: OWASP proxy usage guides
