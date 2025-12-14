---
id: tool-uuid-002
url: 'https://portswigger.net/burp'
tags:
  - proxy
  - interception
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:23.585Z'
validated: true
submitted: true
---
# Proxy-Tool

**Status**: Unverified

## Overview

A man-in-the-middle proxy like Burp Suite for intercepting HTTP/HTTPS and WebSocket traffic, used to modify requests such as POST bodies for code injection in backtests.

## Description

Proxies enable tampering with application traffic, crucial for injecting malicious code into endpoints like start_backtest without altering the source. In this context, it's used for stealthy payload insertion targeting collaborators.

## Features

- Feature 1: HTTPS decryption and request editing
- Feature 2: POST body manipulation for large payloads
- Feature 3: Session handling and repeater for testing

## Installation

### Requirements

- Java runtime for Burp

### Install Commands

```bash
# Download and run Burp Suite Community
wget https://portswigger.net/burp/releases/download?product=community&type=Jar
java -jar burp-suite-community.jar
```

## Basic Usage

```bash
# Configure browser proxy to 127.0.0.1:8080
```

### Common Options

| Option | Description |
|--------|-------------|
| Intercept | Pause and edit requests |
| Repeater | Replay modified requests |

## Examples

### Example 1: Basic Usage

Intercept POST /start_backtest, view code param.

### Example 2: Advanced Usage

Edit code body to insert class, forward to trigger backtest.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Certificate pinning bypass attempts
- Unusual request timings

## Related Procedures

- [[procedures/Exploit-Collaborator-via-POST-Interception]]

## Related Tools

- [[tools/WebSocket-Interceptor]]

## References

- PortSwigger Burp Documentation
