---
id: aa7d29fa-f3bf-4333-a40b-2898230cbf41
type: tool
verified: true
created_at: '2019-08-28T21:17:28.830155Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - ipv6
  - icmpv6
  - mld
  - multicast
  - network-attack
  - dos
url: 'https://github.com/vanhauser-thc/thc-ipv6'
commands:
  - '[[commands/fake-mld6-advertise-multicast-group]]'
  - '[[commands/fake-mld6-delete-multicast-group]]'
validated: true
---

# fake_mld6 – Ad(d)vertise or delete yourself

**Status**: Unverified

## Overview

fake_mld6 is a specialized tool from the THC-IPv6 toolkit designed to exploit weaknesses in IPv6 Multicast Listener Discovery (MLD) protocol. It allows attackers to advertise fake multicast group memberships or delete existing ones, enabling network disruption, denial-of-service attacks, or reconnaissance in IPv6 environments. The tool is particularly useful for testing IPv6 multicast routing resilience and identifying misconfigurations in routers and hosts.

## Description

fake_mld6 targets the MLDv1 and MLDv2 protocols, which are IPv6 equivalents of IGMP in IPv4. By sending spoofed MLD reports or leave messages, it can manipulate multicast forwarding tables on routers, causing traffic blackholing, flooding, or redirection. The tool includes an easy-to-use packet factory library for crafting custom ICMPv6 and IPv6 packets, making it extensible for advanced IPv6 attacks. Common use cases include red team exercises simulating multicast-based DoS, protocol fuzzing, and evasion of IPv6 network defenses.

## Features

- **Advertise Mode**: Spoof MLD reports to join fake multicast groups, potentially overwhelming routers with invalid state.
- **Delete Mode**: Send MLD leave messages to remove legitimate group memberships, disrupting multicast services.
- **Packet Factory Library**: Build and send custom IPv6/ICMPv6 packets for broader protocol attacks.
- **Interface Support**: Operates on specific network interfaces for targeted attacks.
- **Spoofing Capabilities**: Supports source IP spoofing to impersonate hosts.

## Installation

### Requirements

- Linux kernel with IPv6 support enabled.
- libnetfilter-queue and libpcap development libraries.
- GCC compiler.

### Install Commands

```bash
# Clone the THC-IPv6 repository
git clone https://github.com/vanhauser-thc/thc-ipv6.git
cd thc-ipv6

# Install dependencies (on Debian/Ubuntu)
apt update
apt install libnetfilter-queue-dev libpcap-dev libpthread-stubs0-dev libssl-dev

# Build the toolkit
make

# The fake_mld6 binary will be in the current directory
./fake_mld6 -h
```

For Kali Linux, the THC-IPv6 toolkit is often pre-installed or available via `apt install thc-ipv6`.

## Basic Usage

```bash
fake_mld6 -h
```

Displays help with options for advertise (-A) and delete modes.

### Common Options

| Option | Description |
|--------|-------------|
| -A | Advertise/join a multicast group (send MLD report) |
| -D | Delete/leave a multicast group (send MLD done) |
| -i $_INTERFACE | Specify the network interface |
| -s $_SOURCE_IP | Spoof source IPv6 address |
| -d | Debug mode for verbose output |

## Examples

### Example 1: Basic Usage

```bash
fake_mld6 eth0 ff02::1
```

Sends an MLD leave message for the all-nodes group on eth0.

### Example 2: Advanced Usage

```bash
fake_mld6 -A -s fe80::1 eth0 ff02::1:2
```

Advertises a fake join for a custom group with spoofed source IP.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Denial of Service]] Network Denial of Service
- [[Network Service Scanning]] Network Service Scanning

### Tactics

- [[Impact]] Impact
- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual MLDv2 report or leave messages in IPv6 traffic (monitor with tcpdump: `tcpdump -i eth0 ip6 and icmp6`).
- Sudden changes in multicast group memberships on routers without legitimate host activity.
- Presence of THC-IPv6 binaries or library dependencies on compromised systems.
- Anomalous ICMPv6 traffic volumes targeting multicast addresses (ff02::/16).

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
- THC-IPv6 Documentation: Included in repository README
- IPv6 Security Best Practices: RFC 7112 (Implications of IPv6 on MLD)
