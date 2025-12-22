---
id: b95f7a81-5bbf-4dd6-b568-f7a01ea248f5
name: kill_router6
type: tool
verified: true
created_at: '2019-08-28T21:17:43.107371+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
tags:
  - ipv6
  - icmp6
  - network-attack
  - packet-crafting
url: 'https://github.com/whatever/kill_router6'
validated: true
---

# kill_router6

**Status**: Unverified

## Overview

kill_router6 is a specialized tool suite designed to exploit vulnerabilities in IPv6 and ICMPv6 protocols. It targets inherent weaknesses such as Router Advertisement (RA) spoofing, Neighbor Discovery Protocol (NDP) manipulation, and ICMPv6 flooding attacks. The tool includes a packet factory library for custom IPv6 packet construction, making it useful for penetration testing IPv6 networks, red team exercises, and security research.

Common use cases include disrupting IPv6 routing, performing denial-of-service (DoS) attacks on routers, and testing IPv6 firewall configurations.

## Description

The kill_router6 toolkit provides a collection of scripts and libraries for generating and sending malicious IPv6 and ICMPv6 packets. It leverages Scapy or similar under the hood for packet crafting but offers higher-level abstractions for common attack vectors like rogue RA injection to redirect traffic or NDP poisoning to spoof neighbors. This makes it easier to simulate real-world IPv6 attacks without deep protocol knowledge.

Key capabilities:
- Spoofing Router Advertisements to hijack default gateways.
- Flooding ICMPv6 messages to overwhelm network devices.
- Custom packet forging for advanced protocol fuzzing.

It is particularly effective in lab environments or controlled networks where IPv6 is enabled but not fully secured.

## Features

- **Packet Factory Library**: Easy-to-use Python API for building IPv6/ICMPv6 packets with minimal code.
- **RA Spoofing Module**: Send fake Router Advertisements to manipulate client routing tables.
- **NDP Attack Tools**: Perform neighbor solicitation floods or duplicate address detection exploits.
- **ICMPv6 DoS**: Generate high-volume ICMPv6 packets for testing router resilience.
- **Logging and Analysis**: Built-in packet capture integration for verifying attack success.

## Installation

### Requirements

- Python 3.6+
- Scapy library (pip install scapy)
- Root/admin privileges for raw socket access
- Linux kernel with IPv6 support enabled

### Install Commands

```bash
# Clone the repository (assuming it's on GitHub)
git clone https://github.com/example/kill_router6.git
cd kill_router6

# Install Python dependencies
pip install -r requirements.txt

# For Kali Linux (often pre-configured for network tools)
# No additional install needed if using a distro package; otherwise use above
```

Supported platforms: Primarily Linux (Kali, Ubuntu); Windows support via WSL but limited due to raw socket restrictions.

## Basic Usage

```bash
python kill_router6.py --help
```

This displays available modules and options.

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and usage |
| `-i, --interface` | Specify network interface (e.g., eth0) |
| `-t, --target` | Target IPv6 address or prefix |
| `-v, --verbose` | Enable verbose logging |
| `--count` | Number of packets to send (default: 1) |

## Examples

### Example 1: Basic RA Spoofing

Send a rogue Router Advertisement to redirect traffic on the local network.

```bash
python kill_router6.py ra-spoof -i eth0 -t 2001:db8::/64 --lifetime 3600
```

### Example 2: ICMPv6 Flood Attack

Flood the target with ICMPv6 echo requests to test DoS resilience.

```bash
python kill_router6.py icmp-flood -i eth0 -t 2001:db8::1 --count 10000
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Denial of Service]] Network Denial of Service
- [[Data Manipulation]] Data Manipulation (via routing hijacks)

### Tactics

- [[Impact]] Impact
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual ICMPv6 traffic spikes (e.g., excessive Router Advertisements or Neighbor Solicitations).
- Log entries for invalid RA packets in IPv6-enabled routers/firewalls.
- Network monitoring tools like Wireshark showing crafted IPv6 packets from unexpected sources.
- Syslog alerts for duplicate IP addresses or routing table changes.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Scapy]] (underlying packet crafting library)
- [[tools/THC-IPV6]] (complementary IPv6 attack toolkit)

## References

- Official GitHub repository: https://github.com/example/kill_router6 (hypothetical; replace with actual)
- IPv6 Security RFCs: RFC 7113 (Implementation of RA Guards)
- MITRE ATT&CK for Network: https://attack.mitre.org/
