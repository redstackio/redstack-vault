---
id: e6742fe1-d3db-4eaa-aa09-fedc475ab453
name: ipv6-toolkit
type: tool
verified: true
created_at: '2019-08-28T21:17:22.718920+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - ipv6
  - security-assessment
  - reconnaissance
  - exploitation
url: 'https://www.si6networks.com/tools/ipv6toolkit/'
commands:
  - '[[commands/scan6-ipv6-network-scan]]'
  - '[[commands/ra6-send-router-advertisement]]'
  - '[[commands/ns6-send-neighbor-solicitation]]'
  - '[[commands/frag6-ipv6-fragmentation-attack]]'
validated: true
---

# ipv6-toolkit

**Status**: Unverified

## Overview

The SI6 Networks’ IPv6 Toolkit is a comprehensive suite of tools designed for IPv6 security assessment, troubleshooting, and testing device resiliency. It enables penetration testers and security researchers to evaluate IPv6 network configurations, perform targeted attacks simulating real-world threats, and diagnose IPv6-related issues. Common use cases include network reconnaissance, protocol manipulation, and vulnerability assessment in IPv6 environments.

## Description

This toolkit provides a range of specialized utilities for interacting with IPv6 protocols, from address analysis to advanced packet crafting and scanning. It is particularly valuable in modern networks transitioning to or fully implementing IPv6, where traditional IPv4 tools may fall short. The suite supports both offensive security operations, such as sending spoofed Neighbor Discovery packets, and defensive assessments, like testing fragmentation handling. Key components include tools for Router Advertisements, Neighbor Solicitations, and comprehensive network scanning, making it essential for IPv6-focused red teaming and blue team validation.

## Features

- IPv6 address analysis and manipulation (addr6)
- Flow Label security assessment (flow6)
- Fragmentation-based attacks and testing (frag6)
- ICMPv6 error message attacks (icmp6)
- Jumbogram handling evaluation (jumbo6)
- Arbitrary Neighbor Advertisement sending (na6)
- Node Information message attacks (ni6)
- Neighbor Solicitation spoofing (ns6)
- Router Advertisement manipulation (ra6)
- ICMPv6 Redirect attacks (rd6)
- Router Solicitation sending (rs6)
- IPv6 address and network scanning (scan6)
- TCP segment crafting and attacks (tcp6)

## Installation

### Requirements

- Linux kernel with IPv6 support enabled
- libpcap development libraries (for packet capture)
- GCC or compatible compiler
- Root privileges for raw socket access

### Install Commands

```bash
# On Ubuntu/Debian (from source)
git clone https://github.com/fgont/ipv6-toolkit.git
cd ipv6-toolkit
./configure
make
sudo make install

# On Kali Linux (pre-built package may be available)
sudo apt update
sudo apt install ipv6-toolkit
```

For macOS or Windows, compilation from source is recommended, with adjustments for libpcap.

## Basic Usage

```bash
toolkit-tool --help  # e.g., scan6 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -i, --interface | Specify network interface |
| -d, --dst | Set destination address |
| -h, --help | Display help and usage |
| -v, --verbose | Enable verbose output |

## Examples

### Example 1: Basic Usage

Scan an IPv6 prefix:
```bash
scan6 -i eth0 2001:db8::/64
```

### Example 2: Advanced Usage

Send a Router Advertisement:
```bash
ra6 -i eth0 -d ff02::1 -P 2001:db8::/64
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning (for scan6)
- [[Network Denial of Service]] Network Denial of Service (for frag6, ra6)
- [[Adversary-in-the-Middle]] Adversary-in-the-Middle (for ns6, rd6)

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access
- [[Privilege Escalation]] Privilege Escalation

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual IPv6 packet traffic (e.g., excessive RAs or NS messages) via tools like Wireshark or tcpdump
- Raw socket usage by processes matching toolkit binaries (e.g., scan6, ra6) in network monitoring logs
- Anomalous IPv6 neighbor cache entries on hosts
- Increased ICMPv6 error rates or fragmentation attempts in firewall logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Wireshark]] (for packet analysis)
- [[tools/Nmap]] (complementary IPv6 scanning)
- [[Scapy]] (general packet crafting)

## References

- Official documentation: https://www.si6networks.com/tools/ipv6toolkit/ipv6toolkit.shtml
- GitHub repository: https://github.com/fgont/ipv6-toolkit
- IPv6 Security Considerations: RFC 4940
