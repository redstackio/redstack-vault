---
id: 4acbfe29-8e7b-45a0-87fc-7355af85348c
name: flood-solicitate6
type: tool
verified: true
created_at: '2019-08-28T21:17:37.862252+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - ipv6
  - icmp6
  - flood
  - ddos
  - packet-craft
url: 'https://github.com/example/flood-solicitate6'
validated: true
---

# Flood Solicitate6

**Status**: Unverified

## Overview

Flood Solicitate6 is a specialized toolkit designed to exploit vulnerabilities in IPv6 and ICMPv6 protocols. It provides capabilities for launching denial-of-service attacks through flooding techniques and includes a user-friendly packet factory library for crafting custom IPv6 packets. Commonly used in penetration testing to demonstrate protocol weaknesses in IPv6-enabled networks.

## Description

This tool targets inherent weaknesses in IPv6 and ICMPv6, such as excessive resource consumption during router discovery or neighbor solicitation processes. The packet factory allows testers to build and manipulate packets for advanced scenarios, including spoofing and amplification attacks. It is particularly useful for red team exercises assessing IPv6 network resilience.

## Features

- Router Solicitation (RS) flooding to disrupt IPv6 autoconfiguration
- ICMPv6 Echo Request/Reply floods for DoS
- Neighbor Solicitation (NS) attacks to poison caches
- Custom packet crafting library for IPv6/ICMPv6 payloads
- Support for spoofed sources and variable packet sizes
- PCAP output for packet analysis with tools like Wireshark

## Installation

### Requirements

- Linux kernel with IPv6 support
- Python 3.x (for packet factory scripts)
- libpcap-dev for packet capture
- Root privileges for raw socket operations

### Install Commands

```bash
# Clone the repository (assuming GitHub source)
git clone https://github.com/example/flood-solicitate6.git
cd flood-solicitate6

# Install dependencies (Ubuntu/Debian)
sudo apt update
sudo apt install python3-pip libpcap-dev
pip3 install -r requirements.txt

# Build and install
make
sudo make install
```

For Kali Linux, it may be available via apt: `sudo apt install flood-solicitate6` (if packaged).

## Basic Usage

```bash
flood_solicitate6 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -v, --verbose | Enable verbose logging for debugging |
| --interface $_IFACE | Specify network interface (e.g., eth0) |
| --spoof | Enable source IP spoofing |

## Examples

### Example 1: Basic Usage

Launch a simple RS flood:

```bash
flood_solicitate6 --flood-rs --target 2001:db8::1
```

### Example 2: Advanced Usage

Craft and save custom packets:

```bash
flood_solicitate6 --factory --type ns --output custom_ns.pcap --target 2001:db8::1 --spoof
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Denial of Service]] Network Denial of Service
- [[OS Exhaustion Flood]] OS Exhaustion Flood

### Tactics

- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual spikes in ICMPv6 traffic (RS, NS, Echo) via network monitoring (e.g., Snort rules for IPv6 floods)
- High CPU/network load on routers handling IPv6 discovery
- PCAP analysis showing malformed or high-volume IPv6 packets from single source
- Syslog entries for raw socket creations or unusual IPv6 transmissions

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/thc-ipv6]]
- [[tools/scapy]]

## References

- Official GitHub: https://github.com/example/flood-solicitate6
- IPv6 Security Considerations: RFC 7113
- THC-IPv6 Toolkit Documentation
