---
id: 9963b305-ad16-4c8d-a93c-4022111ab0f6
name: flood_mld6
type: tool
verified: true
created_at: '2019-08-28T21:17:34.169106+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
tags:
  - ipv6
  - dos
  - flood
  - icmp6
  - mld6
url: 'https://github.com/vanhauser-thc/thc-ipv6'
validated: true
---

# flood_mld6

**Status**: Unverified

## Overview

flood_mld6 is a specialized tool from the THC-IPv6 Attack Toolkit designed to perform denial-of-service (DoS) attacks by flooding Multicast Listener Discovery version 6 (MLD6) messages on IPv6 networks. It exploits weaknesses in IPv6 multicast protocols to overwhelm routers and hosts, potentially causing network disruption, resource exhaustion, or disruption of multicast group management. Commonly used in penetration testing to assess IPv6 network resilience against protocol-based floods.

## Description

The tool generates and sends a high volume of MLD6 packets (such as MLD Query, Report, and Done messages) to a target IPv6 address or multicast group. This can lead to excessive processing on receiving devices, consuming CPU and bandwidth resources. It includes an easy-to-use packet factory library for customizing packet contents. flood_mld6 is particularly effective against misconfigured IPv6 routers that do not rate-limit MLD traffic, simulating real-world attack scenarios like network reconnaissance denial or service disruption.

## Features

- Floods MLD6 messages (Queries, Reports, Done) to target hosts or multicast groups
- Customizable packet rates and durations for controlled testing
- Supports interface binding for source IP spoofing in IPv6 environments
- Integrated packet crafting for advanced protocol manipulation
- Lightweight and focused on IPv6/ICMPv6 protocol weaknesses

## Installation

### Requirements

- Linux kernel with IPv6 support enabled
- Root privileges for raw socket access
- libnetfilter-queue and libpcap development libraries
- GCC compiler

### Install Commands

flood_mld6 is part of the THC-IPv6 toolkit. Install from source:

```bash
# Clone the repository
git clone https://github.com/vanhauser-thc/thc-ipv6.git
cd thc-ipv6

# Install dependencies (on Ubuntu/Debian)
apt update
apt install libnetfilter-queue-dev libpcap-dev libpcre3-dev libev-dev

# Build and install
make
make install
```

On Kali Linux, it may be available via package manager:

```bash
apt update
apt install thc-ipv6
```

Verify installation:

```bash
flood_mld6 -h
```

## Basic Usage

```bash
flood_mld6 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-i INTERFACE` | Specify network interface (e.g., eth0) |
| `-d DURATION` | Flood duration in seconds (default: infinite) |
| `-r RATE` | Packet rate in packets per second |
| `-s SOURCE_IP` | Spoof source IPv6 address |
| `-t TARGET_IP` | Target IPv6 address or multicast group |
| `-v` | Verbose output for packet details |

## Examples

### Example 1: Basic Usage

Perform a basic MLD6 flood on a target IPv6 address using the default interface:

```bash
flood_mld6 -t 2001:db8::1
```

This sends continuous MLD6 report messages to the target until interrupted (Ctrl+C).

### Example 2: Advanced Usage

Flood with a rate limit of 1000 packets/second for 60 seconds on a specific interface, spoofing the source IP:

```bash
flood_mld6 -i eth0 -t ff02::1 -s 2001:db8::dead:beef -r 1000 -d 60
```

This targets the all-nodes multicast group, simulating a network-wide disruption.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Denial of Service]] Network Denial of Service
- [[Direct Network Flood]] IPv6 and ICMPv6 Flooding (inferred for protocol-specific exhaustion)

### Tactics

- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual spike in MLD6/ICMPv6 traffic via network monitoring (e.g., Wireshark filters for MLDv2)
- High CPU utilization on IPv6 routers due to multicast processing
- Logs of rapid MLD Query/Report messages from a single source IP
- Enable IPv6 firewall rules to rate-limit MLD traffic (e.g., ip6tables -A INPUT -p icmpv6 --icmpv6-type 143 -m limit --limit 10/s -j ACCEPT)
- Intrusion detection systems (IDS) signatures for THC-IPv6 toolkit patterns

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[thc-ipv6-toolkit]] (parent suite)
- [[tools/hping3]] (general packet crafting)
- [[scapy]] (Python-based packet manipulation)

## References

- Official GitHub: https://github.com/vanhauser-thc/thc-ipv6
- THC-IPv6 Documentation: Included in repo README
- IPv6 Security Best Practices: RFC 7112 (Multicast Listener Discovery)
