---
type: tool
description: >-
  A specialized tool for flooding MLDv2 Router Advertisements in IPv6 networks
  to perform denial-of-service attacks on routers and multicast listeners.
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - ipv6
  - dos
  - flood
  - multicast
url: 'https://github.com/vanhauser-thc/thc-ipv6'
commands:
  - '[[commands/flood-mldrouter6-basic-flood]]'
  - '[[commands/flood-mldrouter6-with-source-ip-spoofing]]'
validated: true
---

# flood-mldrouter6

**Status**: Unverified

## Overview

flood_mldrouter6 is part of the THC-IPv6 toolkit, designed to exploit weaknesses in IPv6 and ICMPv6 protocols. It specifically targets Multicast Listener Discovery (MLD) by flooding routers with bogus MLDv2 Router Advertisements, leading to resource exhaustion and denial of service on IPv6-enabled networks. Commonly used in penetration testing to assess IPv6 multicast resilience.

## Description

This tool generates and sends high volumes of MLDv2 Router Advertisement packets, which can overwhelm router processing queues, disrupt multicast group management, and cause network instability. It supports options for interface selection, duration control, and source IP spoofing. The tool is lightweight and requires raw socket access, making it suitable for Linux-based attack machines in controlled environments.

## Features

- Feature 1: High-rate MLDv2 packet flooding to simulate DoS conditions
- Feature 2: Source IP spoofing to evade basic network tracing
- Feature 3: Configurable flood duration and target specification (unicast or multicast addresses)
- Feature 4: Integration with other IPv6 tools in the THC suite for chained attacks

## Installation

### Requirements

- Linux kernel with IPv6 support
- Root privileges for raw socket access
- libnetfilter-queue and other THC-IPv6 dependencies

### Install Commands

```bash
# Clone the THC-IPv6 repository
git clone https://github.com/vanhauser-thc/thc-ipv6.git
cd thc-ipv6

# Install dependencies (on Debian/Ubuntu)
apt update && apt install -y libnetfilter-queue-dev libpcap-dev libdnet-dev

# Build the toolkit
./configure
make
sudo make install
```

For Kali Linux, the tool may be available via `apt install thc-ipv6`.

## Basic Usage

```bash
flood_mldrouter6 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -i, --interface | Specify network interface (e.g., eth0) |
| -s, --srcip | Spoof source IPv6 address |
| -d, --duration | Set flood duration in seconds |
| -h, --help | Show usage help |

## Examples

### Example 1: Basic Usage

```bash
flood_mldrouter6 -i eth0 2001:db8::1
```

This floods the target IPv6 address indefinitely using the default interface.

### Example 2: Advanced Usage

```bash
flood_mldrouter6 -i eth0 -s fe80::dead:beef -d 300 ff02::16
```

This spoofs the source IP and floods the all-MLD-routers multicast group for 5 minutes.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Denial of Service]] Network Denial of Service
- [[OS Exhaustion Flood]] OS Exhaustion Flood

### Tactics

- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for anomalous spikes in MLDv2 Router Advertisement packets using tools like tcpdump or Wireshark (filter: `icmp6 and ip6[40] == 143`)
- Detection method 2: Router logs showing multicast group join/leave floods or CPU/memory exhaustion
- Detection method 3: Network IDS alerts on excessive ICMPv6 traffic from spoofed sources
- Detection method 4: Process monitoring for flood_mldrouter6 binary or high raw socket usage

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
- IPv6 Security Considerations: RFC 7112 (Multicast Security)
