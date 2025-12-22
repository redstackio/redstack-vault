---
id: eb615c9a-08e3-4c4b-b788-f031e776416d
type: tool
verified: true
created_at: '2019-08-28T21:17:37.629988+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - ipv6
  - network-attacks
  - spoofing
  - router-advertisement
url: 'http://www.si6networks.com/tools/ipv6-toolkit/ra6'
validated: true
---

# ra6

**Status**: Unverified

## Overview

ra6 is a command-line tool from the SI6 Networks' IPv6 Toolkit designed to send arbitrary IPv6 Router Advertisement (RA) messages. It is primarily used for security assessments of IPv6 networks, testing the resiliency of devices against RA spoofing attacks, and troubleshooting IPv6 routing issues. Common use cases include simulating rogue routers to influence host routing tables, prefix delegation, and DNS server configurations.

## Description

ra6 allows users to craft and transmit custom RA messages over a specified network interface. These messages can include options like prefixes for address autoconfiguration (SLAAC), recursive DNS servers (RDNSS), and MTU settings. In offensive security, it can be leveraged to perform man-in-the-middle attacks by redirecting traffic or poisoning IPv6 configurations. The tool operates at the link-local level, targeting the IPv6 all-routers multicast address (ff02::2) or all-nodes (ff02::1).

## Features

- Feature 1: Custom RA crafting with options for prefix, source link-layer address, RDNSS, and more.
- Feature 2: Support for hop limit, router lifetime, and reachable time customization.
- Feature 3: Interface-specific transmission with MAC spoofing capabilities.
- Feature 4: Integration with other IPv6 toolkit tools for comprehensive network assessment.

## Installation

### Requirements

- Linux kernel with IPv6 support enabled.
- libnetfilter-queue and libpcap development libraries.
- GCC compiler for building from source.

### Install Commands

The ra6 tool is part of the full IPv6 Toolkit. Install on Ubuntu/Debian-based systems (including Kali Linux):

```bash
# Install dependencies
sudo apt update
sudo apt install build-essential libnetfilter-queue-dev libpcap-dev libdnet-dev libfdisk-dev

# Download and build the IPv6 Toolkit
git clone https://github.com/six2dez/six6s.git  # Note: Actual repo may vary; check official site
cd six6s
./configure
make
sudo make install
```

For Kali Linux, it may be available via:

```bash
sudo apt install ipv6-toolkit
```

Official download: http://www.si6networks.com/tools/ipv6-toolkit/

## Basic Usage

```bash
ra6 --help
```

This displays all available options, such as -i for interface, --prefix for advertising prefixes, and --rdnss for DNS spoofing.

### Common Options

| Option | Description |
|--------|-------------|
| -i, --interface | Specify the network interface (required). |
| -s, --source | Source IPv6 address for the RA. |
| --prefix | Advertise an IPv6 prefix (e.g., --prefix 2001:db8::/64). |
| --rdnss | Include recursive DNS server option. |
| --spoofmac | Spoof the source MAC address. |
| -h, --help | Show help message. |

## Examples

### Example 1: Basic Usage

Send a simple RA on interface eth0:

```bash
ra6 -i eth0
```

### Example 2: Advanced Usage

Spoof an RA with a custom prefix and DNS server:

```bash
ra6 -i eth0 --prefix 2001:db8::/64 --rdnss 2001:db8::53
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle (for traffic redirection via spoofed RAs).
- [[Disable or Modify Tools]] Impair Defenses: Disable or Modify Tools (IPv6 config manipulation).

### Tactics

- [[Defense Evasion]] Defense Evasion.
- [[Discovery]] Discovery (network mapping via RA responses).

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for unexpected RA messages using tools like tcpdump: `tcpdump -i eth0 ip6 and icmp6 and 'icmp6[0] == 134'`.
- Detection method 2: Log anomalies in IPv6 routing tables or prefix changes on hosts (e.g., via `ip -6 route`).
- Detection method 3: Network IDS signatures for RA floods or spoofed sources.
- Detection method 4: Check for multiple/default router inconsistencies in IPv6 neighbor cache (`ndp -a`).

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/thm6]]
- [[tools/na6]]
- [[tools/scan6]]

## References

- Official documentation: http://www.si6networks.com/tools/ipv6-toolkit/ra6
- GitHub repository: https://github.com/six2dez/six6s (if available)
- RFC 4861: Neighbor Discovery for IP version 6
