---
id: b0799f84-4254-4121-8146-d29209fb9758
type: tool
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - ipv6
  - icmp6
  - flood
  - exploitation
url: 'https://github.com/vulnersCom/flood_mld26'
validated: true
---

# flood_mld26

**Status**: Unverified

## Overview

flood_mld26 is a comprehensive toolset designed to exploit vulnerabilities in IPv6 and ICMPv6 protocols. It includes utilities for flooding attacks on Multicast Listener Discovery (MLD) and other ICMPv6 mechanisms, as well as an easy-to-use packet factory library for crafting custom IPv6 packets. Commonly used in penetration testing for assessing IPv6 network resilience against denial-of-service attacks.

## Description

This tool targets inherent weaknesses in IPv6 multicast protocols, such as MLDv2, by generating and sending high volumes of packets to overwhelm routers and endpoints. The packet factory allows for precise control over packet construction, enabling tests for protocol robustness, reconnaissance, and targeted exploits. It's particularly useful in red team operations simulating IPv6-based DoS scenarios without requiring complex setups.

## Features

- Feature 1: MLD flooding capabilities to disrupt multicast group management
- Feature 2: ICMPv6 packet generation for neighbor discovery attacks
- Feature 3: Packet factory library for custom IPv6 payload creation
- Feature 4: Support for spoofed sources and interface binding
- Feature 5: Verbose logging and pcap output for analysis

## Installation

### Requirements

- Linux kernel with IPv6 support enabled
- Python 3.x
- Scapy library (pip install scapy)
- Root privileges for raw socket access

### Install Commands

```bash
# Clone the repository (assuming GitHub source)
git clone https://github.com/vulnersCom/flood_mld26.git
cd flood_mld26

# Install dependencies
pip3 install -r requirements.txt

# Make executable
chmod +x flood_mld26
```

For Kali Linux, it may be available via apt or custom repos; otherwise, build from source.

## Basic Usage

```bash
./flood_mld26 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -i, --interface | Specify network interface |
| -v, --verbose | Enable detailed packet logging |
| -c, --count | Number of packets to send |

## Examples

### Example 1: Basic Usage

Send a single MLD query:

```bash
./flood_mld26 -i eth0 -s fe80::1 -d ff02::1 MLD_QUERY
```

### Example 2: Advanced Usage

Flood MLD with 10000 packets:

```bash
./flood_mld26 -i eth0 -s fe80::1 -d ff02::1 -c 10000 -v MLD_FLOOD
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

- Detection method 1: High volume of MLD/ICMPv6 packets from unusual sources (monitor with tcpdump or Wireshark)
- Detection method 2: Sudden multicast group churn or router CPU spikes
- Detection method 3: Anomalous IPv6 traffic patterns in network logs (e.g., Snort rules for MLD floods)

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[thc-ipv6]]
- [[Scapy]]

## References

- Official GitHub: https://github.com/vulnersCom/flood_mld26
- IPv6 Security Resources: https://ipv6security.net
