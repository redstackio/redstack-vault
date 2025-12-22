---
id: 025f5e7b-2f10-43e3-a17a-9391d6749f85
name: ndpexhaust26
type: tool
verified: true
created_at: '2019-08-28T21:17:25.758765+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - ipv6
  - icmp6
  - exploitation
  - network
url: 'https://github.com/example/ndpexhaust26'
validated: true
---

# ndpexhaust26

**Status**: Unverified

## Overview

ndpexhaust26 is a comprehensive toolset for exploiting inherent weaknesses in IPv6 and ICMPv6 protocols. It provides utilities for conducting exhaustion attacks, flooding, and custom packet crafting using an integrated packet factory library, making it suitable for network security testing and red team operations targeting IPv6 environments.

## Description

The tool focuses on protocol-level vulnerabilities in IPv6 and ICMPv6, such as address exhaustion, neighbor discovery manipulation, and packet flooding. It includes a user-friendly packet factory for building custom payloads, allowing testers to simulate real-world attacks without needing low-level programming knowledge. Commonly used in penetration testing to assess IPv6 network resilience.

## Features

- IPv6 address exhaustion attacks to deplete router or host resources
- ICMPv6 flooding for denial-of-service simulations
- Packet factory library for crafting arbitrary IPv6/ICMPv6 packets
- Multi-threaded packet generation for high-volume attacks
- Support for pcap output for analysis with tools like Wireshark

## Installation

### Requirements

- Python 3.6 or higher
- Scapy library (for packet manipulation)
- Root privileges for raw socket access
- Linux kernel with IPv6 enabled

### Install Commands

```bash
# Clone the repository
sudo git clone https://github.com/example/ndpexhaust26.git
cd ndpexhaust26

# Install dependencies
pip3 install -r requirements.txt

# Make executable (if needed)
chmod +x ndpexhaust26
```

For Kali Linux, it may be available via apt or custom repos; otherwise, build from source.

## Basic Usage

```bash
ndpexhaust26 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and exit |
| `-v, --verbose` | Enable verbose output for debugging |
| `--interface` or `-i` | Specify network interface (e.g., eth0) |

## Examples

### Example 1: Basic Usage

Display help to get started:

Use [[commands/ndpexhaust26-display-help]] for an overview of subcommands.

### Example 2: Advanced Usage

Perform an IPv6 exhaustion attack:

Use [[commands/ndpexhaust26-ipv6-exhaust]] to target a network.

Craft a custom packet:

Use [[commands/ndpexhaust26-craft-packet]] to generate a pcap file.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Denial of Service]] Network Denial of Service
- [[OS Exhaustion Flood]] OS Exhaustion Floods

### Tactics

- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Anomalous high-volume IPv6 or ICMPv6 traffic from a single source
- Packet captures showing crafted or malformed IPv6 headers
- System logs indicating resource exhaustion (e.g., high CPU/network usage)
- Network IDS alerts for ICMPv6 rate anomalies or NDP spoofing

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Scapy]] (for advanced packet crafting)
- [[tools/hping3]] (for ICMP flooding alternatives)
- [[tools/Nmap]] (for IPv6 scanning prior to attacks)

## References

- Official GitHub Repository: https://github.com/example/ndpexhaust26
- IPv6 Security Considerations: RFC 7113
