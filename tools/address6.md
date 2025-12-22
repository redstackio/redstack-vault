---
id: 07a380c9-7f9b-4cc1-afd8-5b08584efff4
type: tool
verified: true
created_at: '2019-08-28T21:17:42.199605+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - ipv6
  - reconnaissance
  - network-attack
url: 'https://github.com/vanhauser-thc/thc-ipv6'
validated: true
---

# address6

**Status**: Unverified

## Overview

address6 is a command-line tool from the THC-IPv6 toolkit designed to generate IPv6 addresses based on the EUI-64 format derived from MAC addresses. It is primarily used in network reconnaissance and IPv6 attack scenarios to predict or spoof link-local and global IPv6 addresses on a target network, exploiting the protocol's address generation mechanisms.

## Description

address6 leverages the IEEE 802 address (MAC) to construct IPv6 addresses using the EUI-64 standard, which embeds the MAC into the lower 64 bits of the IPv6 address. This tool is useful for attackers performing IPv6 neighbor discovery manipulation, address resolution attacks, or mapping possible host addresses in an IPv6 environment. It is part of the broader THC-IPv6 suite, which targets inherent weaknesses in IPv6 and ICMPv6 protocols, including an easy-to-use packet factory library for custom packet crafting.

## Features

- Generates EUI-64 compliant IPv6 addresses from MAC addresses or network interfaces.
- Supports link-local address prediction for stealthy network enumeration.
- Integrates with other THC-IPv6 tools for comprehensive IPv6 attacks.
- Lightweight and scriptable for automation in penetration testing.

## Installation

### Requirements

- Linux kernel with IPv6 support.
- Root privileges for interface access.
- THC-IPv6 toolkit dependencies (libnet, libpcap).

### Install Commands

On Kali Linux (pre-installed):
```bash
# Already available as part of thc-ipv6 package
apt update && apt install thc-ipv6
```

On Ubuntu/Debian:
```bash
apt update && apt install thc-ipv6
```

From source (GitHub):
```bash
git clone https://github.com/vanhauser-thc/thc-ipv6.git
cd thc-ipv6
./configure
make
sudo make install
```

## Basic Usage

```bash
address6 [interface]
```

### Common Options

| Option | Description |
|--------|-------------|
| No options | Generates addresses from default interface MAC |
| [interface] | Specify network interface (e.g., eth0) |
| [MAC address] | Provide a specific MAC address as input |

## Examples

### Example 1: Basic Usage

Generate IPv6 addresses from the default interface:
```bash
address6
```

### Example 2: Advanced Usage

Generate from a specific interface:
```bash
address6 eth0
```

Generate from a provided MAC address:
```bash
address6 00:11:22:33:44:55
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[System Network Configuration Discovery]] System Network Configuration Discovery
- [[Network Service Scanning]] Network Service Scanning

### Tactics

- [[Discovery]] Discovery
- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for unusual IPv6 address generation patterns or EUI-64 derivations in logs.
- Network traffic analysis showing ICMPv6 neighbor solicitation floods.
- Process monitoring for 'address6' executions in reconnaissance phases.
- IPv6 firewall logs for anomalous address resolution attempts.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[thc-ipv6]] (Parent suite)
- [[scapy]] (Packet crafting alternative)
- [[tools/Nmap]] (IPv6 scanning)

## References

- Official GitHub: https://github.com/vanhauser-thc/thc-ipv6
- THC-IPv6 Documentation: Included in the repository README
- IPv6 Security Considerations: RFC 4941 (Privacy Extensions for Stateless Address Autoconfiguration)
