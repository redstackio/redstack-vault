---
url: 'https://netfilter.org/projects/iptables/'
tags:
  - firewall
  - dos
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:08.956Z'
id: 8765077d-386b-4941-9f06-a454f3f6df66
validated: true
submitted: true
---
# iptables

**Status**: Unverified

## Overview

Iptables is a Linux firewall utility for configuring packet filtering and NAT rules, used here to implement TARPIT for holding connections in DoS attacks.

## Description

In SSRF DoS, iptables TARPIT targets prolong TCP handshakes, exhausting victim resources when chained with vulnerable endpoints.

## Features

- Feature 1: Packet mangling and filtering
- Feature 2: Custom targets like TARPIT
- Feature 3: Chain management for rules

## Installation

### Requirements

- Linux kernel with netfilter

### Install Commands

```bash
# Usually pre-installed
apt install iptables
```

## Basic Usage

```bash
iptables --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-t` | Table (e.g., mangle) |
| `-A` | Append rule |
| `-j` | Jump target |

## Examples

### Example 1: Basic Usage

```bash
iptables -L
```

### Example 2: Advanced Usage

```bash
iptables -t mangle -A PREROUTING -p tcp --dport 12345 -j TARPIT
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Denial of Service]] Network Denial of Service

### Tactics

- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Iptables rule changes
- High SYN_RECV states in netstat

## Related Procedures

- [[procedures/Explore-FTP-DoS-with-Iptables-Tarpit]]

## Related Tools

- [[tools/nftables]]

## References

- Official documentation: https://netfilter.org/projects/iptables/index.html
