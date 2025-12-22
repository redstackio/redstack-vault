---
id: e33478ef-87ff-47d6-ab19-094da2b70212
name: ndpexhaust6
type: tool
verified: true
created_at: '2019-08-28T21:17:29.807420Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - ipv6
  - icmpv6
  - ndp
  - packet-craft
  - dos
url: 'https://github.com/kmkz/ndpexhaust6'
validated: true
---

# ndpexhaust6

**Status**: Unverified

## Overview

ndpexhaust6 is a comprehensive toolkit designed to exploit weaknesses in IPv6 and ICMPv6 protocols, particularly focusing on Neighbor Discovery Protocol (NDP) exhaustion attacks. It includes utilities for flooding attacks and an easy-to-use packet factory library for crafting custom IPv6 packets. Commonly used in red teaming for network denial-of-service testing against IPv6-enabled networks.

## Description

The toolset targets inherent vulnerabilities in IPv6 and ICMPv6, such as NDP cache exhaustion through spoofed neighbor advertisements or router solicitations. The packet factory library allows for programmatic creation of malformed or high-volume packets, enabling advanced protocol testing and attack simulations. It's particularly useful in environments transitioning to IPv6 where protocol implementations may have unpatched flaws.

## Features

- NDP flood attacks to exhaust neighbor caches
- ICMPv6 echo request floods for DoS testing
- Custom packet crafting library for IPv6/ICMPv6
- Spoofing support for source IP/MAC addresses
- Configurable packet rates and counts
- PCAP output for packet generation and analysis

## Installation

### Requirements

- Python 3.6+
- Scapy library (pip install scapy)
- Linux kernel with IPv6 support enabled
- Root privileges for raw socket access

### Install Commands

```bash
# Clone the repository
git clone https://github.com/kmkz/ndpexhaust6.git
cd ndpexhaust6

# Install dependencies
pip install -r requirements.txt

# Make scripts executable
chmod +x ndpexhaust6.py packet_factory.py
```

## Basic Usage

```bash
tool-name --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -v, --verbose | Enable verbose logging |
| --interface | Specify network interface |
| --spoof-source | Enable source spoofing |

## Examples

### Example 1: Basic Usage

```python
python ndpexhaust6.py --mode ndp_flood --target 2001:db8::1 --interface eth0
```

### Example 2: Advanced Usage

```python
python packet_factory.py --type icmpv6_echo --output flood.pcap --target 2001:db8::1 --count 10000
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Denial of Service]] Network Denial of Service
- [[OS Exhaustion Flood]] OS Exhaustion Flood: ICMP Flood

### Tactics

- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- High volume of ICMPv6 echo requests or NDP packets from a single source
- Anomalous IPv6 traffic patterns, such as rapid neighbor advertisements
- PCAP analysis showing crafted IPv6 headers
- System logs indicating NDP cache exhaustion (e.g., /proc/net/ndisc_cache overflow)

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[scapy]]
- [[tools/hping3]]

## References

- Official GitHub: https://github.com/kmkz/ndpexhaust6
- IPv6 Security Considerations: RFC 4942
