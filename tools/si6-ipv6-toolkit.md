---
type: tool
verified: true
created_at: '2024-01-01T00:00:00Z'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Linux
tags:
  - ipv6
  - network-security
  - assessment
  - toolkit
url: 'https://www.si6networks.com/tools/ipv6toolkit/'
commands:
  - '[[commands/icmp6-send-destination-unreachable]]'
  - '[[commands/icmp6-send-time-exceeded]]'
  - '[[commands/ra6-send-fake-router-advertisement]]'
  - '[[commands/scan6-discover-ipv6-hosts]]'
validated: true
---

# SI6-IPv6-Toolkit

**Status**: Unverified

## Overview

The SI6 IPv6 Toolkit is a comprehensive set of tools for IPv6 security assessment, troubleshooting, and attack simulation. It enables testing of IPv6 network resilience, performing real-world attacks like Neighbor Discovery manipulation, and scanning IPv6 address spaces. Commonly used in penetration testing for IPv6 environments.

## Description

This toolkit includes multiple utilities for crafting and sending IPv6 packets, assessing protocol implementations, and identifying vulnerabilities. Tools range from simple packet senders to advanced scanners, supporting tasks like DoS testing, MITM attacks via fake RAs, and host discovery. It is particularly valuable for red team operations targeting modern IPv6 deployments.

## Features

- IPv6 packet crafting and injection
- Security assessment of IPv6 stacks (e.g., fragmentation, flow labels)
- Attack simulation (ICMPv6 errors, ND spoofing, RA floods)
- Network scanning and discovery
- Troubleshooting utilities for IPv6 issues

## Installation

### Requirements

- Linux kernel with IPv6 support
- libpcap and libnet for packet handling
- Compiler (gcc) for building from source

### Install Commands

```bash
# On Kali Linux (pre-built package)
apt update && apt install ipv6toolkit

# On Ubuntu (from source)
git clone https://github.com/fgontar/THC-IPv6.git  # Note: Community fork; official binaries from si6networks
cd THC-IPv6
make
make install

# Verify installation
icmp6 --help
```

## Basic Usage

```bash
icmp6 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -v | Verbose output |
| -i | Specify interface |

## Examples

### Example 1: Basic Usage

Scan for hosts:
```bash
scan6 -L 2001:db8::/64
```

### Example 2: Advanced Usage

Send fake RA:
```bash
ra6 -n eth0
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning (for scan6)
- [[Network Denial of Service]] Network Denial of Service (for ICMPv6 floods)
- [[Adversary-in-the-Middle]] Adversary-in-the-Middle (for RA/NS spoofing)

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Discovery]] Discovery
- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual ICMPv6 traffic spikes (e.g., excessive error messages)
- Network logs showing spoofed ND/RA packets
- Process monitoring for icmp6, ra6, scan6 binaries
- IPv6 firewall alerts on anomalous packet types

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Nmap]]
- [[THC-IPV6]] (related suite)

## References

- Official website: https://www.si6networks.com/tools/ipv6toolkit/
- GitHub fork: https://github.com/fgontar/THC-IPv6
- Documentation: Included man pages (man icmp6)
