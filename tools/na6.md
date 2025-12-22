---
id: c893b9bd-e521-4387-b19b-07dc563f4a83
type: tool
verified: true
created_at: '2019-08-28T21:17:19.670292+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - ipv6
  - networking
  - security-assessment
  - neighbor-discovery
url: 'https://www.si6networks.com/tools/ipv6toolkit/'
validated: true
---

# na6

**Status**: Unverified

## Overview

na6 is a command-line tool from the SI6 Networks' IPv6 Toolkit designed to send arbitrary IPv6 Neighbor Advertisement (NA) messages. It is primarily used for security assessments of IPv6 networks, testing the resiliency of devices against Neighbor Discovery Protocol (NDP) manipulation, and troubleshooting IPv6 networking issues related to NA handling.

## Description

The tool allows users to craft and transmit custom NA packets, which are part of the ICMPv6 protocol used in IPv6 for address resolution and duplicate address detection. Common use cases include simulating NA spoofing attacks to evaluate firewall rules, intrusion detection systems, or device configurations that rely on NDP. It supports options for spoofing source addresses, setting flags like Solicited or Override, and specifying link-layer addresses, making it valuable for red team exercises focused on IPv6 layer 2/3 attacks.

## Features

- Feature 1: Send arbitrary NA messages with customizable source and target IPv6 addresses.
- Feature 2: Spoof link-layer (MAC) addresses in NA payloads to test for ARP-like poisoning in IPv6.
- Feature 3: Set NA flags (Solicited, Override) to mimic legitimate or malicious traffic patterns.
- Feature 4: Interface-specific transmission for targeted network segments.
- Feature 5: Integration with packet capture tools for verification during assessments.

## Installation

### Requirements

- Linux kernel with IPv6 support enabled.
- libnetfilter-queue and libpcap development libraries.
- GCC compiler for building from source.

### Install Commands

The na6 tool is part of the full IPv6 Toolkit. Install on Ubuntu/Debian-based systems:

```bash
# Install dependencies
sudo apt update
sudo apt install build-essential libnetfilter-queue-dev libpcap-dev libdnet-dev libfdisk-dev libjson-c-dev bison flex

# Download and build the IPv6 Toolkit from source
wget https://www.si6networks.com/tools/ipv6toolkit/ipv6toolkit-v2.0.tar.gz
 tar -xzf ipv6toolkit-v2.0.tar.gz
 cd ipv6toolkit-v2.0
 ./configure
 make
 sudo make install
```

On Kali Linux, it may be available via package manager:

```bash
sudo apt update
sudo apt install ipv6toolkit
```

## Basic Usage

```bash
na6 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Display help message and usage |
| -d | Enable debug mode for verbose output |
| -i interface | Specify the network interface (e.g., eth0) |
| -s src_linkaddr | Set source link-layer address (MAC) |
| -t target_addr | Target IPv6 address for the NA |
| -S | Set the Solicited flag |
| -T | Set the Target Address flag |

## Examples

### Example 1: Basic Usage

Send a simple NA to a link-local address:

```bash
na6 -i eth0 -t fe80::1%eth0 fe80::1%eth0
```

### Example 2: Advanced Usage

Send a spoofed solicited NA:

```bash
na6 -i eth0 -s 00:11:22:33:44:55 -S -t fe80::1%eth0 fe80::1%eth0
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle (for NDP spoofing scenarios)
- [[Network Sniffing]] Network Sniffing (when combined with capture tools)

### Tactics

- [[Discovery]] Discovery (network mapping via NDP manipulation)
- [[Initial Access]] Initial Access (exploiting IPv6 misconfigurations)

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for anomalous ICMPv6 NA packets with spoofed source IPs or MACs using tools like Snort or Suricata rules for NDP anomalies.
- Detection method 2: Log unusual NDP traffic volumes or flags (e.g., unsolicited NAs) on IPv6-enabled interfaces.
- Detection method 3: Process monitoring for na6 executions in /proc or via auditd.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/scan6]] (IPv6 scanning companion tool)
- [[tools/ns6]] (Neighbor Solicitation tool for paired attacks)
- [[tools/tcpdump]] (For capturing and verifying NA traffic)

## References

- Official documentation: https://www.si6networks.com/tools/ipv6toolkit/na6
- IPv6 Toolkit GitHub: https://github.com/six-networks/ipv6-toolkit
- RFC 4861: Neighbor Discovery for IP version 6
