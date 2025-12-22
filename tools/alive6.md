---
id: fff06a1f-7eb5-4457-91fa-6bf884fb9137
type: tool
verified: true
created_at: '2019-08-28T21:17:39.768121Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - ipv6
  - icmpv6
  - reconnaissance
  - network-discovery
url: 'https://github.com/vanhauser-thc/thc-ipv6'
validated: true
---

# alive6

**Status**: Unverified

## Overview

alive6 is a specialized tool from the THC-IPV6 toolkit designed for discovering alive IPv6 hosts in a network by exploiting ICMPv6 protocols, particularly neighbor discovery mechanisms. It is commonly used in offensive security operations for initial reconnaissance in IPv6 environments, identifying live targets without standard tools like ping that may be blocked or ineffective in IPv6 setups.

## Description

alive6 attacks the inherent weaknesses in IPv6 and ICMPv6 protocols by sending crafted packets such as neighbor solicitations to a multicast group or specific prefix, eliciting responses from live hosts. It includes an easy-to-use packet factory library for custom ICMPv6 payloads. This tool is particularly valuable in red team engagements targeting modern networks transitioning to or fully using IPv6, where traditional IPv4 reconnaissance techniques fall short. It supports options for delaying packets, specifying source addresses, and probing upper-layer protocols to gather more detailed host information.

## Features

- Feature 1: Host discovery via ICMPv6 neighbor solicitations and echo requests
- Feature 2: Support for multicast addressing to scan entire prefixes efficiently
- Feature 3: Protocol probing (e.g., TCP/UDP ports) on discovered hosts
- Feature 4: Customizable packet crafting with delay and source spoofing options
- Feature 5: Verbose output for detailed response analysis

## Installation

### Requirements

- Linux kernel with IPv6 support enabled
- Root privileges for raw socket access
- THC-IPV6 toolkit dependencies (libnetfilter-queue, libpcap)

### Install Commands

```bash
# On Kali Linux (pre-compiled package)
apt update && apt install thc-ipv6

# From source (Ubuntu/Debian)
git clone https://github.com/vanhauser-thc/thc-ipv6.git
cd thc-ipv6
./configure
make
make install
```

## Basic Usage

```bash
alive6 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -v | Verbose output for detailed logging |
| -d $_DELAY | Set delay between packets in seconds |
| -p $_PROTOCOL | Probe specific upper-layer protocol/port |
| -s $_SRC_ADDR | Spoof source IPv6 address |

## Examples

### Example 1: Basic Usage

Discover alive hosts in an IPv6 prefix:

```bash
alive6 eth0 2001:db8::/64
```

### Example 2: Advanced Usage

Probe for HTTP services with verbose output:

```bash
alive6 -p 80 -v eth0 2001:db8::/64
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote System Discovery]] Remote System Discovery
- [[Network Service Scanning]] Network Service Scanning

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for unusual ICMPv6 neighbor solicitation floods from a single source
- Detection method 2: IPv6 firewall logs showing multicast NS packets to all-nodes address (ff02::1)
- Detection method 3: Network intrusion detection systems (NIDS) alerting on high-volume ICMPv6 traffic
- Detection method 4: Endpoint logs for raw socket usage by unknown processes

## Related Commands

- [[commands/alive6-discover-hosts-in-prefix]]
- [[commands/alive6-probe-with-protocol]]

## Related Tools

- [[tools/Nmap]] (for complementary IPv6 scanning)
- [[tools/thc-ipv6]] (parent toolkit)

## References

- Official GitHub: https://github.com/vanhauser-thc/thc-ipv6
- THC-IPV6 Toolkit Documentation: https://www.thc.org/thc-ipv6/
- IPv6 Security Considerations: RFC 7113
