---
id: fdcd8d6a-f268-425b-a3e3-2b980868fb65
name: flood_router6
type: tool
verified: true
created_at: '2019-08-28T21:17:32.056896+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - ipv6
  - icmp6
  - dos
  - packet-flood
url: 'https://github.com/mephi42/flood_router6'
validated: true
---

# flood_router6

**Status**: Unverified

## Overview

flood_router6 is a specialized toolset designed for offensive security testing of IPv6 networks, focusing on exploiting weaknesses in the IPv6 protocol and ICMPv6 messages. It includes utilities for packet flooding attacks and a flexible packet factory library for crafting custom IPv6 packets. Commonly used in red team exercises to simulate DoS attacks on IPv6 routers and hosts.

## Description

This tool provides a collection of scripts and a library to target inherent vulnerabilities in IPv6 and ICMPv6, such as excessive resource consumption from malformed or flooded packets. The packet factory allows easy creation of custom packets for advanced testing, while flooding modules can overwhelm targets with Router Advertisements (RA), Neighbor Solicitations (NS), and other ICMPv6 types. It's particularly useful for assessing IPv6 router resilience in enterprise or lab environments.

## Features

- Feature 1: ICMPv6 packet flooding (RA, NS, Redirect, etc.) to cause DoS
- Feature 2: Easy-to-use packet factory library for generating spoofed IPv6 packets
- Feature 3: Support for rate limiting, duration control, and source spoofing
- Feature 4: PCAP output for packet capture and analysis
- Feature 5: Modular design allowing extension for custom attack vectors

## Installation

### Requirements

- Python 3.6+
- Scapy library (pip install scapy)
- Root privileges for raw socket access
- Linux kernel with IPv6 enabled

### Install Commands

```bash
# Clone the repository
git clone https://github.com/mephi42/flood_router6.git
cd flood_router6

# Install dependencies
pip install -r requirements.txt

# For development setup
python setup.py develop
```

## Basic Usage

```bash
python flood_router6.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Display help message and usage |
| -v, --verbose | Enable verbose logging for packet details |
| --interface $_INTERFACE | Specify network interface (e.g., eth0) |
| --spoof-source | Enable source IP/MAC spoofing |

## Examples

### Example 1: Basic Usage

Flood with Router Advertisements:

```bash
python flood_router6.py --flood-ra --target 2001:db8::/64 --rate 1000 --duration 60
```

### Example 2: Advanced Usage

Generate custom packets using the factory:

```bash
python packet_factory.py --generate-icmp6 --type 133 --output flood.pcap --count 1000
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

- Detection method 1: High volume of ICMPv6 packets (RA/NS floods) in network traffic logs
- Detection method 2: Unusual IPv6 packet rates monitored via tools like Wireshark or IDS (e.g., Snort rules for ICMPv6 anomalies)
- Detection method 3: Process monitoring for python/scapy executions with raw sockets
- Detection method 4: PCAP files with spoofed IPv6 sources

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

- Official GitHub: https://github.com/mephi42/flood_router6
- IPv6 Security Considerations: RFC 7113
- Scapy Documentation for IPv6 crafting
