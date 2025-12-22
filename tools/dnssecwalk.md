---
id: fa7331cb-fbc2-4842-a4d2-927e27a75cf2
type: tool
verified: true
created_at: '2019-08-28T21:17:18.682416+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
tags:
  - ipv6
  - icmp6
  - exploitation
  - packet-crafting
url: 'https://example.com/dnssecwalk'
commands:
  - '[[commands/dnssecwalk-craft-icmp6-packet]]'
  - '[[commands/dnssecwalk-send-ipv6-packet]]'
  - '[[commands/dnssecwalk-factory-create-packet]]'
validated: true
---

# dnssecwalk

**Status**: Unverified

## Overview

A complete tool set to attack the inherent protocol weaknesses of IPv6 and ICMPv6, including an easy-to-use packet factory library for crafting and sending malicious packets in security testing and red team operations.

## Description

dnssecwalk is designed for offensive security professionals to exploit vulnerabilities in IPv6 and ICMPv6 protocols, such as neighbor discovery manipulation, router advertisement spoofing, and duplicate address detection attacks. The integrated packet factory allows for rapid prototyping of custom packets without deep programming knowledge, making it suitable for penetration testing IPv6-enabled networks.

## Features

- Feature 1: Packet crafting for ICMPv6 types like neighbor solicitation, router advertisements, and echo requests.
- Feature 2: Easy packet injection over specified network interfaces.
- Feature 3: Programmable factory library for automating packet generation in scripts.
- Feature 4: Support for spoofing source addresses and custom payload injection.

## Installation

### Requirements

- Python 3.6+
- Scapy library (pip install scapy)
- Root privileges for packet injection

### Install Commands

```bash
# Clone from repository (assuming GitHub or similar)
git clone https://github.com/example/dnssecwalk.git
cd dnssecwalk
pip install -r requirements.txt
# Or direct pip install if available
pip install dnssecwalk
```

## Basic Usage

```bash
dnssecwalk --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -v, --verbose | Enable verbose output for debugging |
| --interface | Specify network interface for sending packets |

## Examples

### Example 1: Basic Usage

Craft and send a simple ICMPv6 echo request:

```bash
dnssecwalk --craft icmp6 --type echo-request --target 2001:db8::1 --send --interface eth0
```

### Example 2: Advanced Usage

Use the factory to create a spoofed router advertisement:

```bash
dnssecwalk --factory create --protocol icmp6 --options '{"type":134,"code":0,"router-lifetime":3600}' --save ra.pcap --send --interface wlan0
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning (for IPv6 discovery)
- [[Network Denial of Service]] Network Denial of Service (via ICMPv6 floods)

### Tactics

- [[Impact]] Impact
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual ICMPv6 traffic spikes or malformed packets in network logs.
- Packet captures showing crafted IPv6 headers with invalid checksums or spoofed sources.
- Process monitoring for python processes loading scapy or similar libraries on non-standard ports.

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

- Official documentation: https://example.com/dnssecwalk/docs
- IPv6 Security Considerations: RFC 7113
