---
id: 3fa5b6fc-518f-4b92-ba47-f06f6a94c984
type: tool
verified: true
created_at: '2019-08-28T21:17:35.060500+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - ipv6
  - icmp6
  - reconnaissance
  - network-attack
url: 'https://github.com/vanhauser-thc/thc-ipv6'
validated: true
---

# parasite6

**Status**: Unverified

## Overview

parasite6 is a command-line tool from the THC-IPv6 toolkit designed to exploit weaknesses in IPv6 and ICMPv6 protocols. It focuses on neighbor discovery manipulation, such as discovering neighbors, poisoning caches, and sending fake advertisements, making it ideal for IPv6 network reconnaissance and disruption in penetration testing.

## Description

parasite6 sends forged ICMPv6 packets to perform actions like neighbor solicitation for discovery or neighbor advertisement spoofing for cache poisoning. It includes a packet factory library for custom IPv6 packet crafting. Commonly used in red team operations to map IPv6 networks, perform MITM attacks, or cause DoS by overwhelming neighbor caches. It requires root privileges and an IPv6-enabled interface.

## Features

- Feature 1: Neighbor discovery via ICMPv6 solicitations
- Feature 2: Neighbor cache poisoning with spoofed advertisements
- Feature 3: Custom packet crafting for advanced ICMPv6 attacks
- Feature 4: Support for link-local and global IPv6 addresses

## Installation

### Requirements

- Linux kernel with IPv6 support
- Root access for raw socket usage
- THC-IPv6 toolkit dependencies (libnet, libpcap)

### Install Commands

```bash
# On Kali Linux (pre-installed in many distros)
sudo apt update && sudo apt install thc-ipv6

# Manual build from source
wget https://github.com/vanhauser-thc/thc-ipv6/archive/master.zip
unzip master.zip
cd thc-ipv6-master
./configure
make
sudo make install
```

## Basic Usage

```bash
parasite6 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -i, --interface | Specify network interface |
| -t, --target | Target IPv6 address |
| -S, --spoof | Spoof source address |
| -d, --debug | Enable debug output |
| -v, --verbose | Verbose mode |

## Examples

### Example 1: Basic Usage

Discover neighbors on interface eth0:

```bash
sudo parasite6 -i eth0
```

### Example 2: Advanced Usage

Poison cache of target with spoofed IP:

```bash
sudo parasite6 -i eth0 -t fe80::1 -S fe80::dead:beef
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Discovery (for neighbor enumeration)
- [[Adversary-in-the-Middle]] Adversary-in-the-Middle (for cache poisoning)

### Tactics

- [[Discovery]] Discovery
- [[TA0108]] Network Effects (for DoS via poisoning)

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for unusual ICMPv6 neighbor solicitation/advertisement floods using tools like tcpdump or Wireshark (filter: icmp6 and (nd_na or nd_ns))
- Detection method 2: Check IPv6 neighbor tables for inconsistencies (ip -6 neigh show) and log anomalous entries
- Detection method 3: Network IDS alerts on high-volume ICMPv6 type 135/136 packets from unexpected sources

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
- [[scapy]]

## References

- Official GitHub: https://github.com/vanhauser-thc/thc-ipv6
- THC-IPv6 Documentation: Included in toolkit man pages
- IPv6 Security Guide: RFC 7113 (Implementation of Neighbor Discovery Protocol)
