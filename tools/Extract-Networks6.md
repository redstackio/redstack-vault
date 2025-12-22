---
id: 34b01537-3341-46b4-86ce-583a85b7f4d6
type: tool
verified: true
created_at: '2019-08-28T21:17:22.529036+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
tags:
  - ipv6
  - icmp6
  - network-attack
  - packet-crafting
url: ''
validated: true
---

# Extract-Networks6

**Status**: Unverified

## Overview

Extract-Networks6 is a shell script-based toolset designed to exploit weaknesses in the IPv6 and ICMPv6 protocols. It provides capabilities for network discovery, extraction of IPv6 address spaces, and crafting custom packets using an integrated packet factory library, making it suitable for penetration testing and security research on IPv6-enabled networks.

## Description

The tool targets inherent vulnerabilities in IPv6 implementations, such as issues in neighbor discovery protocol (NDP), router advertisements, and ICMPv6 message handling. It includes an easy-to-use packet factory library that allows users to generate and send malformed or spoofed packets to test for denial-of-service conditions, reconnaissance, or man-in-the-middle attacks. Commonly used in red team exercises to map and disrupt IPv6 environments.

## Features

- IPv6 network discovery and address extraction from interfaces or captures
- ICMPv6-specific attack modules (e.g., flood, spoofing)
- Packet factory for creating custom IPv6/ICMPv6 payloads
- Support for scripting automated attack sequences
- Integration with tools like tcpdump for packet analysis

## Installation

### Requirements

- Linux kernel with IPv6 support enabled
- Bash 4.0 or higher
- Root privileges for raw socket access (packet crafting)
- Optional: libpcap for packet capture integration

### Install Commands

The tool is provided as a standalone shell script. Download and make executable:

```bash
wget https://example-repo/extract_networks6.sh  # Replace with actual source
chmod +x extract_networks6.sh
sudo mv extract_networks6.sh /usr/local/bin/
```

For full toolkit (if part of a larger suite like THC-IPv6):

```bash
git clone https://github.com/vanhoefm/thc-ipv6  # Example repo
cd thc-ipv6
make
sudo make install
```

## Basic Usage

```bash
./extract_networks6.sh --help
```

This displays available options, including discovery, crafting, and attack modes.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -v, --verbose | Enable verbose logging |
| -i, --interface | Specify network interface |
| --discover | Run network discovery mode |
| --craft | Enter packet crafting mode |

## Examples

### Example 1: Basic Usage

Discover IPv6 networks on an interface:

```bash
./extract_networks6.sh --discover -i eth0
```

### Example 2: Advanced Usage

Craft and send an ICMPv6 packet:

```bash
./extract_networks6.sh --craft --type icmp6 --target 2001:db8::1
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning (for discovery)
- [[Direct Network Flood]] Direct Network Flood (ICMPv6 floods)
- [[Adversary-in-the-Middle]] Adversary-in-the-Middle (NDP spoofing)

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual ICMPv6 traffic spikes or malformed packets (monitor with Wireshark or tcpdump)
- Root-level processes spawning bash scripts with IPv6 socket binds
- Log entries for raw socket creation (e.g., /var/log/audit/audit.log on SELinux systems)
- Network anomalies like fake router advertisements (RA) messages

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Nmap]] (for complementary IPv6 scanning)
- [[Scapy]] (advanced packet crafting)
- [[THC-IPv6]] (extended IPv6 attack suite)

## References

- Official documentation: (Assume project repo or man page)
- Related resources: IPv6 Security RFCs (e.g., RFC 7113 on IPv6 security considerations)
