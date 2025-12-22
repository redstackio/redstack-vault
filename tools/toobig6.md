---
id: 2981762d-9de9-494f-9c80-651748e45e3f
type: tool
verified: true
created_at: '2019-08-28T21:17:38.041084+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - ipv6
  - icmp6
  - network-attack
  - dos
  - packet-crafting
url: 'https://github.com/vitlabuda/toobig6'
validated: true
---

# toobig6

**Status**: Unverified

## Overview

toobig6 is a specialized toolkit for exploiting vulnerabilities in IPv6 and ICMPv6 protocols. It provides utilities for launching denial-of-service attacks, such as fragmentation and flooding, and includes a Python-based packet factory library for crafting custom IPv6 packets. Commonly used in network penetration testing to identify and demonstrate weaknesses in IPv6 implementations.

## Description

The tool targets inherent protocol flaws in IPv6, including improper handling of fragmented packets, neighbor discovery spoofing, and ICMPv6 message processing. It supports both direct attacks and packet generation for advanced scenarios, making it valuable for red team operations assessing IPv6 network security.

## Features

- IPv6 fragmentation attacks to overwhelm reassembly buffers
- ICMPv6 flood attacks (e.g., echo requests, neighbor solicitations)
- Packet factory library for creating malformed or custom IPv6/ICMPv6 packets
- Support for pcap output for integration with other tools like Scapy
- Command-line interface for easy scripting and automation

## Installation

### Requirements

- Linux kernel with IPv6 support enabled
- Python 3.6+ for the packet factory
- libpcap-dev for packet capture/injection
- Root privileges for raw socket access

### Install Commands

```bash
# Clone the repository
git clone https://github.com/vitlabuda/toobig6.git
cd toobig6

# Install dependencies
sudo apt update
sudo apt install python3-pip libpcap-dev
pip3 install -r requirements.txt

# Build and install
make
sudo make install
```

## Basic Usage

```bash
toobig6 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -v, --verbose | Enable verbose output for debugging |
| --interface $_IFACE | Specify network interface (e.g., eth0) |
| --target $_TARGET | IPv6 target address |

## Examples

### Example 1: Basic Usage

Launch a simple ICMPv6 flood:

```bash
toobig6 --mode icmp6-flood --target 2001:db8::1 --rate 1000
```

### Example 2: Advanced Usage

Create and send fragmented packets:

```bash
toobig6 --mode fragmentation --target 2001:db8::1 --mtu 1280 --packets 2000 --interface eth0
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Denial of Service]] Network Denial of Service
- [[OS Exhaustion Flood]] OS Exhaustion Flood: IPv6 ICMP Fragmentation Flood

### Tactics

- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual IPv6 traffic spikes, especially fragmented packets or ICMPv6 echoes
- Monitoring for raw socket usage by processes named 'toobig6'
- Network IDS rules for oversized IPv6 fragments or high-rate ICMPv6
- System logs showing packet injection from unprivileged interfaces

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Scapy]]
- [[tools/hping3]]

## References

- Official GitHub: https://github.com/vitlabuda/toobig6
- IPv6 Security Considerations: RFC 4940
