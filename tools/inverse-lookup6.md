---
id: 1e2efe90-2d4a-48ab-b70c-79ff7296acc6
type: tool
verified: true
created_at: '2019-08-28T21:17:32.426231+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - ipv6
  - icmpv6
  - reconnaissance
  - packet-crafting
url: 'https://github.com/vanhauser-thc/thc-ipv6'
validated: true
---

# inverse-lookup6

**Status**: Unverified

## Overview

inverse_lookup6 is a specialized tool from the THC-IPv6 toolkit designed to exploit weaknesses in IPv6 and ICMPv6 protocols for inverse address resolution. It performs reverse DNS lookups by crafting and sending ICMPv6 packets, allowing attackers to map IPv6 addresses to hostnames without relying on standard DNS infrastructure. Commonly used in reconnaissance phases of IPv6 network assessments.

## Description

This tool targets inherent flaws in IPv6 Neighbor Discovery Protocol (NDP) and ICMPv6, enabling passive or active inverse lookups. It includes a packet factory library for custom ICMPv6 packet construction, making it versatile for advanced IPv6 attacks like address spoofing and resolution bypassing. Use it in environments where IPv6 is deployed but DNS is misconfigured or sparse.

## Features

- Feature 1: Single host inverse lookup via ICMPv6 queries
- Feature 2: Network-wide scanning for hostname resolution
- Feature 3: Custom packet crafting library for ICMPv6 payloads
- Feature 4: Exploitation of NDP weaknesses for stealthy reconnaissance

## Installation

### Requirements

- Linux kernel with IPv6 support
- libnetfilter-queue and other THC dependencies
- Git and make utilities

### Install Commands

```bash
# Clone the THC-IPv6 repository
git clone https://github.com/vanhauser-thc/thc-ipv6.git
cd thc-ipv6

# Compile the toolkit
./configure
make
sudo make install
```

On Kali Linux, it may be available via apt: `sudo apt install thc-ipv6`.

## Basic Usage

```bash
inverse_lookup6 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h | Single host lookup mode |
| -n | Network prefix scan mode |
| -v | Verbose output for debugging packets |
| --help | Display usage information |

## Examples

### Example 1: Basic Usage

Perform a single host lookup:

```bash
inverse_lookup6 -h 2001:db8::1
```

### Example 2: Advanced Usage

Scan a /64 network:

```bash
inverse_lookup6 -n 2001:db8::/64 -v
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning
- [[Network Service Scanning]] Network Service Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual ICMPv6 traffic spikes (e.g., Echo Requests/Responses) monitored via tools like tcpdump or Wireshark
- Detection method 2: Log anomalous NDP packets or inverse query patterns in IPv6 firewalls
- Detection method 3: Network IDS alerts for crafted ICMPv6 payloads targeting reverse resolution

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
- IPv6 Security Resources: RFC 4443 (ICMPv6) and related attack papers
