---
id: d3c3df8b-922f-4d6e-98fa-b1359792db5a
type: tool
verified: true
created_at: '2019-08-28T21:17:38.537733+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - ipv6
  - icmpv6
  - reconnaissance
  - exploitation
  - packet-crafting
url: 'https://github.com/example/passive_discovery6'
validated: true
---

# passive-discovery6

**Status**: Unverified

## Overview

passive_discovery6 is a comprehensive toolset designed to exploit weaknesses in IPv6 and ICMPv6 protocols. It enables passive network discovery, active probing, and custom packet crafting using an integrated packet factory library. Commonly used in red team operations for stealthy IPv6 reconnaissance and protocol-based attacks in modern network environments.

## Description

The tool targets inherent vulnerabilities in IPv6 and ICMPv6, such as neighbor discovery spoofing, duplicate address detection flaws, and router advertisement manipulation. It includes modes for passive monitoring (to avoid detection), active attacks, and a Python-based packet factory for building arbitrary IPv6 packets. Ideal for penetration testing IPv6-enabled networks, identifying misconfigurations, and simulating advanced persistent threats that leverage protocol weaknesses.

## Features

- Feature 1: Passive IPv6 address discovery via ICMPv6 traffic analysis without generating alerts.
- Feature 2: Active exploitation of ICMPv6 weaknesses, including DoS via router advertisement floods.
- Feature 3: Easy-to-use packet factory library for crafting custom IPv6/ICMPv6 packets in Python scripts.
- Feature 4: Support for multiple output formats (TXT, JSON, PCAP) for integration with other tools like Wireshark.
- Feature 5: Cross-interface monitoring and multi-threaded scanning for efficiency.

## Installation

### Requirements

- Python 3.6+ with Scapy library for packet manipulation.
- Linux kernel with IPv6 support enabled.
- Root privileges for raw socket access (packet crafting and sniffing).

### Install Commands

```bash
# Clone the repository
sudo apt update && sudo apt install python3-pip git
pip3 install scapy

git clone https://github.com/example/passive_discovery6.git
cd passive_discovery6
pip3 install -r requirements.txt

# Or install via pip if available
pip3 install passive-discovery6
```

## Basic Usage

```bash
passive_discovery6 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -v, --verbose | Enable verbose logging for debugging |
| --interface $_INTERFACE | Specify network interface (default: eth0) |
| --mode $_MODE | Set operation mode (passive, active, craft) |

## Examples

### Example 1: Basic Usage

Passive scan on default interface:

```bash
passive_discovery6 --mode passive --output discovery_results.txt
```

### Example 2: Advanced Usage

Craft and send a spoofed ICMPv6 packet:

```bash
passive_discovery6 --mode craft --packet-type icmpv6_na --target 2001:db8::1
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Discovery (for passive IPv6 host enumeration)
- [[Remote System Discovery]] Remote System Discovery (via ICMPv6 neighbor discovery attacks)

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual ICMPv6 traffic spikes (e.g., excessive Neighbor Solicitations/Advertisements) monitored via tools like Snort or Suricata.
- Detection method 2: Python processes with Scapy imports and raw socket binds on IPv6 interfaces.
- Detection method 3: Network logs showing crafted packets with anomalous IPv6 headers (e.g., invalid extension headers).

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

- Official GitHub: https://github.com/example/passive_discovery6
- IPv6 Security Guidelines: https://tools.ietf.org/html/rfc7113
- Scapy Documentation: https://scapy.net
