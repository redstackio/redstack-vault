---
url: 'https://github.com/symmetryinvestments/stunner'
tags:
  - turn-testing
  - socks-proxy
type: tool
verified: false
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:44.147Z'
id: 9a2077b7-a818-4776-85b6-832cc6672c0d
validated: true
submitted: true
---
---

# Stunner

**Status**: Unverified

## Overview

Stunner is an open-source tool for testing and exploiting TURN/STUN servers, including recon, port scanning, and SOCKS proxy creation to abuse relays for internal access.

## Description

Designed for WebRTC security, it authenticates with TURN creds, probes configs, and sets up proxies. Key in detecting open relays without peer controls, enabling pivots to internal nets like AWS.

## Features

- Feature 1: Recon mode for relay and peer checks
- Feature 2: Port scanner via relay
- Feature 3: SOCKS5 proxy for tunneling traffic

## Installation

### Requirements

- Go 1.16+
- Linux/macOS

### Install Commands

```bash
go install github.com/symmetryinvestments/stunner/cmd/stunner@latest
```

## Basic Usage

```bash
stunner --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `recon` | Perform server reconnaissance |
| `-u` | Username for auth |

## Examples

### Example 1: Basic Usage

```bash
stunner recon tls://example.com:443 -u user
```

### Example 2: Advanced Usage

```bash
stunner proxy tls://example.com:443 -u user -p 1080
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Protocol Tunneling]]

### Tactics

- [[Discovery]]
- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual TURN allocation requests from single IP
- Proxy traffic patterns to internal IPs

## Related Procedures

- [[procedures/Reconnaissance-on-TURN-Server-Using-Stunner]]
- [[procedures/Access-Internal-Services-via-TURN-SOCKS-Proxy]]

## Related Tools

- [[Turnutils]]
- [[Trickle-ice]]

## References

- Official documentation: https://github.com/symmetryinvestments/stunner

---
