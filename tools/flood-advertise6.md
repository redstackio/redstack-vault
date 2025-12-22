---
id: c1d759ac-ccab-4476-b0f6-5b02f452a0c7
type: tool
verified: true
created_at: '2019-08-28T21:17:35.742614+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - ipv6
  - icmpv6
  - dos
  - packet-crafting
url: 'https://github.com/vanhauser-thc/thc-ipv6'
validated: true
---

# flood-advertise6

**Status**: Unverified

## Overview

flood_advertise6 is a specialized tool from the THC-IPv6 toolkit designed to exploit weaknesses in IPv6 and ICMPv6 protocols by flooding networks with Router Advertisement (RA) packets. It is commonly used in penetration testing to demonstrate denial-of-service (DoS) vulnerabilities in IPv6 autoconfiguration processes, such as overwhelming devices with fake RA messages that disrupt default router selection and address assignment.

## Description

This tool targets inherent protocol flaws in IPv6 Neighbor Discovery Protocol (NDP), particularly Router Advertisements, to cause network disruption. It includes capabilities for rate-controlled flooding and custom packet crafting using an integrated packet factory library, allowing testers to simulate attacks like RA flooding for DoS or prefix spoofing for misconfiguration. Ideal for red team exercises assessing IPv6 resilience in enterprise or lab environments.

## Features

- Feature 1: High-rate RA flooding to saturate IPv6 autoconfiguration on target devices.
- Feature 2: Customizable packet parameters, including prefixes, lifetimes, and router preferences via packet factory.
- Feature 3: Support for link-local and global IPv6 addressing in attacks.
- Feature 4: Integration with other THC-IPv6 tools for chained IPv6 exploits.

## Installation

### Requirements

- Linux kernel with IPv6 support enabled.
- Root privileges for raw socket access.
- THC-IPv6 toolkit dependencies (libnet, libpcap).

### Install Commands

```bash
# Clone the THC-IPv6 repository
git clone https://github.com/vanhauser-thc/thc-ipv6.git
cd thc-ipv6

# Compile the toolkit
make

# Install (as root)
sudo make install
```

On Kali Linux, it may be pre-installed or available via:

```bash
sudo apt update && sudo apt install thc-ipv6
```

## Basic Usage

```bash
flood_advertise6 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -i, --interface | Specify network interface (e.g., eth0) |
| -r, --rate | Packets per second rate |
| -p, --packets | Number of packets to send (for non-flood modes) |
| --custom-prefix | Advertise a forged IPv6 prefix |
| -h, --help | Show usage help |

## Examples

### Example 1: Basic Usage

Flood RAs on a local network:

```bash
flood_advertise6 -i eth0 -r 100 2001:db8::/64
```

### Example 2: Advanced Usage

Send custom RA with spoofed prefix:

```bash
flood_advertise6 -i eth0 -p 1000 --custom-prefix 2001:db8:evil::/64 fe80::1
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Denial of Service]] Network Denial of Service
- [[Data Manipulation]] Data Manipulation (for prefix spoofing)

### Tactics

- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for excessive ICMPv6 Type 134 (RA) packets using tools like tcpdump: `tcpdump -i eth0 ip6 and icmp6[0] == 134`.
- Detection method 2: Anomalous IPv6 prefix changes on hosts; check router logs for duplicate RAs.
- Detection method 3: High outbound traffic on raw sockets from untrusted processes.

## Related Procedures

- [[procedures/Perform-IPv6-DoS-Attack]]
- [[procedures/Spoof-IPv6-Router-Advertisements]]

## Related Tools

- [[thc-ipv6-toolkit]]
- [[scapy]]

## References

- Official GitHub: https://github.com/vanhauser-thc/thc-ipv6
- THC-IPv6 Documentation: Included in repository README
- IPv6 Security Considerations: RFC 7113
