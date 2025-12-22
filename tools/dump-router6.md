---
id: 05ab9ab8-2800-4508-ba13-dc5918a3d728
name: dump-router6
type: tool
verified: true
created_at: '2019-08-28T21:17:23.716541+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - ipv6
  - icmp6
  - reconnaissance
  - network-attack
  - packet-craft
url: 'https://github.com/vanhauser-thc/thc-ipv6'
validated: true
---

# dump-router6

**Status**: Unverified

## Overview

Dump_router6 is a specialized tool from the THC-IPv6 toolkit designed to sniff and analyze IPv6 Router Advertisement (RA) packets and other ICMPv6 traffic. It exploits inherent weaknesses in IPv6 and ICMPv6 protocols for network reconnaissance, router discovery, and potential attack setup. Commonly used in red team operations to map IPv6 network topology, identify default routers, and detect misconfigurations that enable attacks like router advertisement spoofing or denial-of-service.

## Description

This tool provides a complete set for attacking IPv6 and ICMPv6 protocol weaknesses, including passive sniffing of router advertisements and integration with a packet factory library for crafting custom IPv6 packets. It helps in scenarios where IPv6 is deployed, allowing attackers to gather critical network information such as prefixes, MTU settings, DNS servers, and router lifetimes without active probing that might trigger alerts.

## Features

- Feature 1: Passive capture of IPv6 RA packets to extract router details and network prefixes.
- Feature 2: Real-time display of ICMPv6 messages for immediate reconnaissance.
- Feature 3: Integration with THC-IPv6 packet crafting library for extending to active attacks like RA flooding.
- Feature 4: Low-level protocol analysis to identify exploitable protocol flaws.

## Installation

### Requirements

- Linux kernel with IPv6 support enabled.
- Root privileges for packet capture (libpcap).
- THC-IPv6 toolkit dependencies (e.g., libnetfilter-queue).

### Install Commands

On Kali Linux (pre-installed in many distros):

```bash
# Update and install THC-IPv6 toolkit
sudo apt update
sudo apt install thc-ipv6
```

On Ubuntu:

```bash
sudo apt update
sudo apt install thc-ipv6
```

Manual build from source:

```bash
git clone https://github.com/vanhauser-thc/thc-ipv6.git
cd thc-ipv6
./configure
make
sudo make install
```

## Basic Usage

```bash
dump_router6 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-i, --interface` | Specify the network interface (default: all IPv6 interfaces) |
| `-v, --verbose` | Increase verbosity for detailed packet dissection |
| `-f, --file` | Output to a pcap file for later analysis |

## Examples

### Example 1: Basic Usage

Sniff RA packets on the default interface:

```bash
sudo dump_router6
```

### Example 2: Advanced Usage

Capture on a specific interface and save to file:

```bash
sudo dump_router6 -i eth0 -f ra_capture.pcap
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Sniffing]] Network Sniffing
- [[Active Scanning]] Active Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for unusual libpcap usage or promiscuous mode on interfaces (e.g., via `tcpdump` or host IDS).
- Detection method 2: Network logs showing ICMPv6 RA traffic spikes or analysis tools like Wireshark detecting THC-IPv6 signatures.
- Detection method 3: Process monitoring for `dump_router6` binary or THC-IPv6 toolkit processes.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[thc-ipv6-toolkit]]
- [[scapy]]

## References

- Official GitHub: https://github.com/vanhauser-thc/thc-ipv6
- THC-IPv6 Documentation: Included in toolkit man pages (`man dump_router6`)
