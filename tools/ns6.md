---
id: 1045a252-7998-4c90-a3c1-e4fc42ae16a5
name: ns6
type: tool
verified: true
created_at: '2019-08-28T21:17:33.260164Z'
updated_at: '2023-05-29T16:48:53.029709Z'
platforms:
  - Linux
tags:
  - ipv6
  - network
  - reconnaissance
  - neighbor-discovery
url: 'https://www.si6networks.com/tools/ipv6toolkit/id1.html'
commands:
  - '[[commands/ns6-send-basic-neighbor-solicitation]]'
  - '[[commands/ns6-send-spoofed-neighbor-solicitation]]'
validated: true
---

# ns6

**Status**: Unverified

## Overview

ns6 is a specialized tool from the SI6 Networks' IPv6 Toolkit designed to send arbitrary IPv6 Neighbor Solicitation (NS) messages. It is used for security assessments of IPv6 networks, testing device resiliency against neighbor discovery attacks, and troubleshooting IPv6 connectivity issues. Common use cases include probing for neighbor cache poisoning vulnerabilities, validating NS message processing, and simulating rogue router scenarios in IPv6 environments.

## Description

Part of the comprehensive SI6 IPv6 Toolkit, ns6 allows users to craft and transmit custom NS messages, including options for spoofing source addresses, adding extensions, and specifying query types. This enables real-world attacks like NS flooding or spoofed solicitations to evaluate IPv6 implementations. The toolkit as a whole includes related tools like na6 (Neighbor Advertisement), rs6 (Router Solicitation), and scan6 (IPv6 scanning), but ns6 focuses specifically on NS-based operations.

## Features

- Feature 1: Craft arbitrary NS messages with customizable source IP, target, and options (e.g., source link-layer address).
- Feature 2: Support for spoofing to test IPv6 security features like Secure Neighbor Discovery (SEND).
- Feature 3: Verbose output for packet inspection, including hex dumps for debugging.
- Feature 4: Integration with libnet for low-level packet manipulation on Unix-like systems.

## Installation

### Requirements

- Linux kernel with IPv6 support enabled.
- libnet development libraries (libnet-dev on Debian-based systems).
- gcc and make for compilation.

### Install Commands

For Kali Linux (pre-built package):

```bash
sudo apt update
sudo apt install ipv6toolkit
```

For Ubuntu (compile from source):

```bash
sudo apt install libnet-dev libpcap-dev gcc make
wget https://www.si6networks.com/tools/ipv6toolkit/ipv6toolkit-3.1.0.tar.gz
# Verify checksum and extract
tar -xzf ipv6toolkit-3.1.0.tar.gz
cd ipv6toolkit-3.1.0
./configure
make
sudo make install
```

The toolkit installs all tools, including ns6, typically to /usr/local/bin.

## Basic Usage

```bash
ns6 --help
```

This displays available options, such as -i for interface, -s for source IP, -t for target, and -v for verbose.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and exit |
| -i, --interface | Specify network interface |
| -s, --srcaddr | Spoof source IPv6 address |
| -t, --target | Target IPv6 address for solicitation |
| -v, --verbose | Enable verbose packet output |

## Examples

### Example 1: Basic Usage

Send a simple NS message:

```bash
ns6 -i eth0 2001:db8::1
```

### Example 2: Advanced Usage

Send a spoofed NS with verbose output:

```bash
ns6 -s 2001:db8::dead:beef -i eth0 -v 2001:db8::1
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning (for IPv6 discovery)
- [[Active Scanning]] Active Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for unusual NS message volumes or spoofed sources using tools like tcpdump: `tcpdump -i eth0 icmp6 and 'icmp6[0] == 135'` (NS type 135).
- Detection method 2: IPv6 firewall logs showing unexpected NS queries from internal sources.
- Detection method 3: Process monitoring for ns6 binary or libnet usage in network captures.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/na6]]
- [[tools/scan6]]
- [[tools/thc-ipv6]]

## References

- Official SI6 IPv6 Toolkit documentation: https://www.si6networks.com/tools/ipv6toolkit/
- IPv6 Neighbor Discovery Protocol (RFC 4861)
- Related resources: https://datatracker.ietf.org/doc/html/rfc4861
