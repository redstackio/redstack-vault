---
id: 3c10d636-35b3-4396-b364-37c23add0946
type: tool
verified: true
description: >-
  A Python-based toolset for exploiting IPv6 and ICMPv6 protocol weaknesses,
  including packet crafting and fragmentation attacks.
url: 'https://github.com/mandatoryprogrammer/fragmentation6'
created_at: '2019-08-28T21:17:39.709408+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - ipv6
  - icmpv6
  - fragmentation
  - packet-crafting
  - network-attacks
commands:
  - '[[commands/fragmentation6-send-fragmented-ipv6-packet]]'
  - '[[commands/fragmentation6-icmpv6-attack]]'
  - '[[commands/fragmentation6-create-packet-factory]]'
validated: true
---

# fragmentation6

**Status**: Unverified

## Overview

fragmentation6 is a specialized toolset designed to target vulnerabilities in IPv6 and ICMPv6 protocols. It provides utilities for crafting and sending fragmented packets, performing ICMPv6 floods, and generating custom packet scripts via an integrated packet factory library. Commonly used in red teaming for network reconnaissance, denial-of-service testing, and bypassing IPv6 firewalls through fragmentation exploits.

## Description

The tool exploits inherent weaknesses in IPv6 fragmentation handling and ICMPv6 message processing, such as improper reassembly, extension header parsing errors, and neighbor discovery spoofing. It includes a Python library for easy packet manipulation, making it suitable for both manual testing and automated attack scripts. Ideal for environments transitioning to IPv6 where protocol implementations may have unpatched flaws.

## Features

- IPv6 packet fragmentation and reassembly testing
- ICMPv6 attack vectors (e.g., NS/NA floods, RA spoofing)
- Packet factory library for custom protocol payloads
- Support for extension headers and tunneling protocols
- Integration with Scapy for advanced crafting

## Installation

### Requirements

- Python 3.6+
- Scapy library (pip install scapy)
- Linux kernel with IPv6 enabled

### Install Commands

```bash
# Clone the repository
git clone https://github.com/mandatoryprogrammer/fragmentation6.git
cd fragmentation6

# Install dependencies
pip install -r requirements.txt

# Make executable
chmod +x fragmentation6
```

## Basic Usage

```bash
./fragmentation6 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -v, --verbose | Enable verbose packet logging |
| --target | Specify IPv6 target address |
| --interface | Select network interface (e.g., eth0) |

## Examples

### Example 1: Basic Usage

Send a simple fragmented IPv6 packet:

```bash
./fragmentation6 --send-fragment --target 2001:db8::1 --payload "Hello"
```

### Example 2: Advanced Usage

Launch an ICMPv6 neighbor discovery flood:

```bash
./fragmentation6 --icmpv6-attack --type 135 --target 2001:db8::/64 --count 1000
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning (for IPv6 discovery)
- [[Network Denial of Service]] Network Denial of Service (fragmentation floods)
- [[Archive via Utility]] Archive Collected Data: Archive via Utility (packet crafting for exfil)

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual IPv6 traffic spikes or malformed fragments (monitor with tcpdump: tcpdump ip6 and fragment)
- ICMPv6 type anomalies (e.g., excessive NS messages) via Wireshark filters
- Python processes with Scapy imports and high network I/O
- Log anomalous extension header usage in IPv6 firewalls

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Scapy]]
- [[tools/hping3]]

## References

- Official GitHub: https://github.com/mandatoryprogrammer/fragmentation6
- IPv6 Security Considerations: RFC 4940
- ICMPv6 Attacks: https://www.cisco.com/c/en/us/about/security-center/ipv6-best-practices.html
