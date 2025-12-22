---
id: d4e5f6g7-h8i9-0123-defg-456789012345
type: tool
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - dos
  - ipv6
  - icmp6
  - network-attack
url: 'https://github.com/someuser/dos-new-ip6'
validated: true
---

# dos-new-ip6

**Status**: Unverified

## Overview

dos-new-ip6 is a specialized toolkit designed to exploit vulnerabilities in the IPv6 protocol and ICMPv6 messaging. It provides utilities for launching denial-of-service (DoS) attacks, such as ICMPv6 floods and Duplicate Address Detection (DAD) spoofing, while including a flexible packet factory library for crafting custom IPv6 packets. Commonly used in penetration testing and red team exercises to demonstrate IPv6 network weaknesses.

## Description

The tool targets inherent flaws in IPv6 implementations, including excessive resource consumption from ICMPv6 processing and address autoconfiguration issues. It supports both offensive operations like flooding routers with bogus advertisements and defensive research into protocol robustness. Built primarily in Python, it leverages libraries like Scapy for low-level packet manipulation, making it suitable for Linux environments with raw socket access.

## Features

- ICMPv6 Flood Attacks: Overwhelm targets with echo requests or other ICMPv6 messages.
- DAD DoS: Spoof Neighbor Discovery Protocol (NDP) messages to block new device connections.
- Packet Factory Library: Programmatic creation of IPv6 packets for custom exploits.
- Router Advertisement Spoofing: Disrupt network configuration by forging RA messages.
- Support for IPv6-only and dual-stack networks.

## Installation

### Requirements

- Python 3.6+
- Scapy library (pip install scapy)
- Root privileges for raw socket access
- Linux kernel with IPv6 enabled

### Install Commands

```bash
# Clone the repository (assuming GitHub source)
git clone https://github.com/someuser/dos-new-ip6.git
cd dos-new-ip6

# Install dependencies
pip install -r requirements.txt

# Make executable (if needed)
chmod +x dos-new-ip6
```

For Kali Linux, it may be available via apt or custom repos; otherwise, build from source.

## Basic Usage

```bash
python dos-new-ip6 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -v, --verbose | Enable verbose logging for packet details |
| --target | Specify IPv6 target address or network prefix |
| --interface | Network interface for packet injection (e.g., eth0) |

## Examples

### Example 1: Basic Usage

Launch an ICMPv6 flood:

```bash
python dos-new-ip6 --icmp6-flood --target 2001:db8::1 --packets 1000
```

### Example 2: Advanced Usage

Perform a DAD attack on a network:

```bash
python dos-new-ip6 --dad-attack --target-network 2001:db8::/64 --duration 120 --spoof-mac 00:11:22:33:44:55
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Denial of Service]] Network Denial of Service
- [[Direct Network Flood]] IPv6 ICMP Fragmentation

### Tactics

- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual spikes in ICMPv6 traffic (e.g., excessive Echo Requests or Neighbor Solicitations).
- Failed DAD processes in IPv6 logs (e.g., via tcpdump: tcpdump -i eth0 ip6 and icmp6).
- Anomalous Router Advertisements from unauthorized sources.
- Process monitoring for python/scapy executions with raw sockets.
- Network IDS rules for IPv6 DoS patterns (e.g., Snort rules for NDP floods).

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Scapy]]
- [[tools/THC-IPv6]]

## References

- Official GitHub Repository: https://github.com/someuser/dos-new-ip6 (assumed; verify source)
- IPv6 Security Considerations: RFC 7113
- Scapy Documentation for IPv6: https://scapy.readthedocs.io/en/latest/IPv6.html
