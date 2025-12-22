---
id: 1a22ef4d-3802-49f4-93b0-30378ff6333f
name: detect-new-ip6
type: tool
verified: true
created_at: '2019-08-28T21:17:40.416679+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - ipv6
  - icmp6
  - reconnaissance
  - exploitation
url: 'https://example.com/detect-new-ip6-repo'
validated: true
---

# detect-new-ip6

**Status**: Unverified

## Overview

detect-new-ip6 is a specialized toolkit for identifying and exploiting weaknesses in IPv6 and ICMPv6 protocols. It includes modules for host discovery, packet crafting, and sending custom ICMPv6 messages, making it ideal for security testing in IPv6 environments, such as penetration testing IPv6 networks or simulating attacks on protocol implementations.

## Description

This tool provides a comprehensive set of utilities to detect new IPv6 configurations, discover hosts via neighbor discovery protocols, and craft malicious packets to test for vulnerabilities like router advertisement spoofing, duplicate address detection flaws, or ICMPv6 amplification. The included packet factory library allows users to build custom IPv6 packets programmatically, supporting offensive security operations in modern networks transitioning to IPv6.

## Features

- Feature 1: IPv6 host discovery using ICMPv6 neighbor solicitations and advertisements.
- Feature 2: Custom ICMPv6 packet generation for protocol weakness testing (e.g., floods, spoofing).
- Feature 3: Packet factory library for scripting advanced IPv6 attacks.
- Feature 4: Support for pcap output to integrate with tools like Wireshark or Scapy.

## Installation

### Requirements

- Linux kernel with IPv6 support enabled.
- Python 3.6+ (for the packet factory library).
- libpcap-dev for packet capture functionality.

### Install Commands

```bash
# Clone the repository (assuming GitHub source)
git clone https://github.com/example/detect-new-ip6.git
cd detect-new-ip6

# Install dependencies
pip install -r requirements.txt

# Build and install
make install
```

For Ubuntu/Debian:

```bash
sudo apt update
sudo apt install libpcap-dev python3-dev
# Then follow the clone steps above
```

## Basic Usage

```bash
detect-new-ip6 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -i, --interface | Specify network interface |
| -v, --verbose | Enable verbose logging |
| --target | Set target IPv6 address or prefix |

## Examples

### Example 1: Basic Usage

Discover hosts on an IPv6 network:

```bash
detect-new-ip6 --discover --interface eth0 --target 2001:db8::/64
```

### Example 2: Advanced Usage

Craft and send a custom ICMPv6 packet:

```bash
detect-new-ip6 --icmp6 --type 133 --target 2001:db8::1 --source fe80::dead:beef
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning (for host discovery)
- [[Network Denial of Service]] Network Denial of Service (for ICMPv6 floods)

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual ICMPv6 traffic spikes (e.g., excessive Router Solicitations).
- Detection method 2: Network logs showing crafted IPv6 packets from unexpected sources.
- Detection method 3: Process monitoring for 'detect-new-ip6' binary or Python scripts using libpcap.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/scapy]] (for advanced packet crafting)
- [[tools/Nmap]] (IPv6 scanning complement)

## References

- Official documentation: https://example.com/detect-new-ip6-docs
- IPv6 Security Considerations: RFC 4940
- THC-IPv6 Toolkit (inspirational reference)

## Related Commands

- [[commands/detect-new-ip6-discover-hosts]]
- [[commands/detect-new-ip6-send-icmp6]]
- [[commands/detect-new-ip6-packet-craft]]
