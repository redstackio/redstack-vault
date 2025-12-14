---
id: tool-iptables-001
url: 'https://netfilter.org/projects/iptables/index.html'
tags:
  - firewall
  - nat
  - network
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:44.803Z'
validated: true
submitted: true
---
# iptables

**Status**: Unverified

## Overview

iptables is a Linux user-space utility for configuring the IPv4 packet filter ruleset (netfilter), commonly used for network redirection, NAT, and traffic manipulation in security testing and MITM setups.

## Description

Here, it's used to DNAT and REDIRECT HTTPS traffic from a rogue WiFi interface to a proxy, enabling transparent interception without altering client configs. Essential for Linux-based AP attacks on mobile apps.

## Features

- Feature 1: NAT table for address/port translation
- Feature 2: PREROUTING chain for incoming packet handling
- Feature 3: Protocol/port matching for targeted rules

## Installation

### Requirements

- Linux kernel with netfilter

### Install Commands

```bash
# Usually pre-installed; if not
apt install iptables
```

## Basic Usage

```bash
iptables --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-t nat` | NAT table |
| `-A` | Append rule |
| `-L` | List rules |

## Examples

### Example 1: Basic Usage

```bash
iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080
```

### Example 2: Advanced Usage

```bash
iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 443 -j DNAT --to 127.0.0.1:8080
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle
- [[SSH]] Traffic Tunneling (adapted)

### Tactics

- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Suspicious NAT rules in `iptables -L`
- Elevated pkts on PREROUTING chains
- Root processes modifying firewall

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/nftables]]
- [[tools/pf]]

## References

- Official documentation: https://netfilter.org/projects/iptables/
- Related resources: Linux firewall guides
