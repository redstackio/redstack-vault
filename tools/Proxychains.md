---
url: 'https://github.com/haad/proxychains'
tags:
  - proxy
  - socks
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:44.144Z'
id: 42bb5c72-04d2-4f7f-8823-6b36d24cbaa8
validated: true
submitted: true
---
---

# Proxychains

**Status**: Unverified

## Overview

Proxychains is a hooking library that forces TCP connections through SOCKS4/5 or HTTP proxies, ideal for routing tools like telnet through TURN-generated proxies to reach internal hosts.

## Description

Version 4.x supports dynamic chains and DLL injection. Configured with TURN SOCKS, it enables firewall bypass by relaying traffic via the open TURN server to localhost or AWS internals.

## Features

- Feature 1: Support for SOCKS5 proxies from tools like stunner
- Feature 2: Chain multiple proxies if needed
- Feature 3: Logs proxy usage for debugging

## Installation

### Requirements

- Linux with make

### Install Commands

```bash
git clone https://github.com/haad/proxychains.git
cd proxychains && make && make install
```

## Basic Usage

```bash
proxychains -h
```

### Common Options

| Option | Description |
|--------|-------------|
| `-f config` | Load custom config file |
| `-q` | Quiet mode, no logs |

## Examples

### Example 1: Basic Usage

```bash
proxychains -f config telnet 127.0.0.1 5766
```

### Example 2: Advanced Usage

```bash
proxychains -f config curl 169.254.169.254/latest/meta-data/
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Protocol Tunneling]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Log entries showing proxied connections to internal IPs
- Anomalous TCP traffic patterns from TURN endpoints

## Related Procedures

- [[procedures/Access-Internal-Services-via-TURN-SOCKS-Proxy]]

## Related Tools

- [[Tsocks]]
- [[Proxifier]]

## References

- Official documentation: https://github.com/haad/proxychains

---
