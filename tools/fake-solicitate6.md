---
type: tool
description: >-
  A toolkit for exploiting IPv6 and ICMPv6 protocol weaknesses, including a
  packet factory for crafting custom packets.
url: 'https://github.com/example/fake-solicitate6'
tags:
  - ipv6
  - icmp6
  - exploitation
  - packet-crafting
platforms:
  - Linux
  - macOS
verified: true
validated: true
---

# fake-solicitate6

**Status**: Unverified

## Overview

fake_solicitate6 is a specialized toolkit designed to identify and exploit vulnerabilities in IPv6 and ICMPv6 protocols. It provides utilities for sending spoofed packets, performing network reconnaissance, and crafting custom ICMPv6 messages, making it useful for penetration testing IPv6-enabled networks.

## Description

This tool targets inherent weaknesses in IPv6 neighbor discovery and router discovery protocols, such as lack of authentication in ICMPv6 messages. It includes a Python-based packet factory library for easy creation of malformed or spoofed packets, enabling attacks like router spoofing, neighbor cache poisoning, and denial-of-service via excessive solicitations.

## Features

- Feature 1: Spoofing of Neighbor Solicitation, Router Advertisement, and other ICMPv6 types
- Feature 2: Packet factory library for programmatic packet construction using Scapy-like syntax
- Feature 3: Support for multiple network interfaces and rate limiting to avoid detection
- Feature 4: PCAP output for crafted packets, integrable with Wireshark or tcpdump

## Installation

### Requirements

- Python 3.6+
- Scapy library (pip install scapy)
- Root privileges for raw socket access

### Install Commands

```bash
# Clone from repository
sudo apt update && sudo apt install python3-pip git
pip3 install scapy

# For Kali Linux (pre-requisites often available)
git clone https://github.com/example/fake-solicitate6.git
cd fake-solicitate6
pip3 install -r requirements.txt
sudo make install
```

## Basic Usage

```bash
fake_solicitate6 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -v, --verbose | Enable verbose logging |
| --interface | Specify network interface |

## Examples

### Example 1: Basic Usage

Send a neighbor solicitation:

```bash
fake_solicitate6 --send-ns --target 2001:db8::1 --source 2001:db8::2 --interface eth0
```

### Example 2: Advanced Usage

Craft and save a router advertisement:

```bash
fake_solicitate6 --craft-packet --type 134 --output ra.pcap
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning (for IPv6 discovery)
- [[Network Denial of Service]] Network Denial of Service (via ICMPv6 floods)

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual ICMPv6 traffic volumes or spoofed source IPs (monitor with Wireshark filters like icmpv6.type == 135)
- Detection method 2: Anomalous router advertisements not matching known routers (RA Guard on switches)
- Detection method 3: Packet captures showing crafted payloads with invalid checksums

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Scapy]]
- [[THC-IPv6]]

## References

- Official documentation: https://github.com/example/fake-solicitate6
- IPv6 Security Considerations: RFC 7113
