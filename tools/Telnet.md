---
url: 'https://www.man7.org/linux/man-pages/man1/telnet.1.html'
tags:
  - telnet
  - remote-access
type: tool
verified: false
platforms:
  - Linux
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:44.140Z'
id: 1bf7bf6e-257a-4c26-b5f4-393b3fd5b9d1
validated: true
submitted: true
---
---

# Telnet

**Status**: Unverified

## Overview

Telnet is a standard client for connecting to remote services on specific ports, used here to interact with the coturn admin telnet interface for configuration access.

## Description

Insecure protocol, but useful for testing exposed services like coturn's management port 5766. When proxied, it allows remote control of internal servers.

## Features

- Feature 1: Interactive command execution
- Feature 2: Simple TCP connection to any port
- Feature 3: Escape sequences for session control

## Installation

### Requirements

- Standard on Linux; install via package manager

### Install Commands

```bash
# Ubuntu: sudo apt install telnet
# Or built-in on most systems
```

## Basic Usage

```bash
telnet --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `hostname port` | Connect to host:port |

## Examples

### Example 1: Basic Usage

```bash
telnet 127.0.0.1 5766
```

### Example 2: Advanced Usage

Proxied: `proxychains telnet 127.0.0.1 5766`

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Device CLI]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Telnet connections to management ports like 5766
- Unauthenticated access logs in coturn

## Related Procedures

- [[procedures/Access-Internal-Services-via-TURN-SOCKS-Proxy]]

## Related Tools

- [[Netcat]]
- [[SSH]]

## References

- Man page: https://www.man7.org/linux/man-pages/man1/telnet.1.html

---
