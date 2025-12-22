---
id: f4023a3a-b04d-44c1-bfed-c8e121e11e10
type: tool
verified: true
created_at: '2019-08-28T21:17:29.621127+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - ipv6
  - dhcpv6
  - network-attack
  - exploitation
url: 'https://github.com/vanhauser-thc/thc-ipv6'
validated: true
---

# fake_dhcps6

**Status**: Unverified

## Overview

fake_dhcps6 is a tool from the THC-IPv6 toolkit designed to exploit weaknesses in the IPv6 and ICMPv6 protocols by implementing a fake DHCPv6 server. It allows attackers to perform network poisoning attacks, such as assigning malicious DNS servers, gateways, or prefixes to IPv6 clients, enabling man-in-the-middle (MitM) scenarios, traffic redirection, and further exploitation in IPv6 environments.

## Description

The tool creates a rogue DHCPv6 server that responds to client requests on the local network, advertising custom configuration options like fake DNS resolvers, search domains, and default gateways. This can lead to DNS spoofing, traffic interception, or denial of service by misconfiguring client network settings. It includes support for packet crafting via an integrated library, making it suitable for advanced IPv6 protocol attacks. Commonly used in penetration testing to demonstrate IPv6 deployment risks in enterprise or lab networks.

## Features

- Fake DHCPv6 server implementation for responding to Solicit/Request messages
- Advertisement of custom IPv6 prefixes, DNS servers, and domains
- Rogue Router Advertisement (RA) integration for gateway spoofing
- Verbose logging and packet inspection capabilities
- Easy integration with other THC-IPv6 tools for chained attacks
- Support for IPv6 multicast and link-local addressing

## Installation

### Requirements

- Linux kernel with IPv6 support enabled
- THC-IPv6 toolkit dependencies (libnetfilter-queue, libpcap, etc.)
- Root privileges for raw socket access

### Install Commands

```bash
# Clone the THC-IPv6 repository
git clone https://github.com/vanhauser-thc/thc-ipv6.git
cd thc-ipv6

# Install dependencies on Ubuntu/Debian
apt update
apt install build-essential libnetfilter-queue-dev libpcap-dev libdnet-dev libssl-dev

# Compile and install
make
make install
```

On Kali Linux, it is often pre-installed or available via `apt install thc-ipv6`.

## Basic Usage

```bash
fake_dhcps6 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and options |
| -v level | Set verbosity (0-4) |
| -i interface | Specify network interface |
| -e | Enable expert mode for advanced packet handling |

## Examples

### Example 1: Basic Usage

Start a fake DHCPv6 server assigning a prefix and fake DNS:

```bash
fake_dhcps6 -i eth0 -x 2001:db8::/64 -n 2001:db8::fake
```

### Example 2: Advanced Usage

Run with rogue RA and high verbosity:

```bash
fake_dhcps6 -i wlan0 -x 2001:db8:1::/64 -g 2001:db8:1::attacker -n 2001:db8:1::dnsfake -A -v 4
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle (for traffic interception via fake gateways)
- [[Encrypted Channel]] Encrypted Channel (if combined with tunneling)
- [[Network Denial of Service]] Network Denial of Service (by misconfiguring clients)

### Tactics

- [[Discovery]] Discovery (network configuration reconnaissance)
- [[Persistence]] Persistence (via persistent rogue server)
- [[Command and Control]] Command and Control (DNS poisoning for C2)

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual DHCPv6 traffic from non-legitimate sources (monitor with tcpdump: `tcpdump -i eth0 udp port 547`)
- Clients receiving unexpected prefixes or DNS servers (log DHCPv6 responses)
- Rogue RA messages (use tools like rdnssd or manual inspection)
- High verbosity logs or process monitoring for fake_dhcps6 binary
- Network anomalies like traffic redirection to attacker-controlled IPs

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
- [[scapy]] (for custom IPv6 packet crafting)
- [[tools/bettercap]] (for broader MitM capabilities)

## References

- Official GitHub: https://github.com/vanhauser-thc/thc-ipv6
- THC-IPv6 Documentation: Included in repo README
- IPv6 Security Best Practices: RFC 7113 (Implementation of DHCPv6)

*Last updated: 2023-10-01*
