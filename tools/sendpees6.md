---
id: cf6a73ed-2b2b-4544-9bcb-43acf83d98c1
type: tool
description: >-
  A complete tool set to attack the inherent protocol weaknesses of IPv6 and
  ICMPv6, including an easy-to-use packet factory library for crafting custom
  packets.
verified: true
created_at: '2019-08-28T21:17:30.433544+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - ipv6
  - icmp6
  - network-attack
  - packet-crafting
  - dos
url: ''
validated: true
---

# sendpees6

**Status**: Unverified

## Overview

sendpees6 is a specialized toolkit for exploiting vulnerabilities in IPv6 and ICMPv6 protocols. It provides command-line utilities for launching attacks like floods and spoofing, along with a packet factory library that enables users to generate custom malicious packets. Commonly used in penetration testing to assess IPv6 network security, identify protocol weaknesses, and simulate real-world attacks such as denial-of-service or reconnaissance.

## Description

The tool addresses inherent flaws in IPv6 and ICMPv6, including issues with neighbor discovery, router advertisements, and packet fragmentation. It supports both direct attacks via CLI commands and programmatic packet crafting through its library, making it versatile for red team operations, vulnerability research, and educational purposes. sendpees6 requires root privileges for raw socket access and is most effective on Linux systems with IPv6 enabled.

## Features

- **CLI Attack Modules**: Pre-built commands for common IPv6/ICMPv6 attacks like RA flooding, NS spoofing, and echo amplification.
- **Packet Factory Library**: Python-based API for creating and manipulating IPv6/ICMPv6 packets with fine-grained control over headers and payloads.
- **Spoofing Support**: Built-in capabilities to spoof source IPs and MAC addresses for anonymous attacks.
- **Output Formats**: Generate packets as PCAP files for analysis with Wireshark or integration with other tools like Scapy.
- **Interface Selection**: Specify network interfaces to target specific network segments.

## Installation

### Requirements

- Linux kernel with IPv6 support
- Python 3.6+
- Root/admin privileges for raw packet sending
- Optional: libpcap-dev for PCAP output

### Install Commands

```bash
# Clone the repository (assuming GitHub source; adjust if different)
git clone https://github.com/sendpees6/sendpees6.git
cd sendpees6

# Install dependencies
pip3 install -r requirements.txt  # Typically includes scapy or similar

# Make executable (if needed)
chmod +x sendpees6

# For system-wide install
sudo cp sendpees6 /usr/local/bin/
```

On Kali Linux, it may be available via apt or custom repos; otherwise, build from source.

## Basic Usage

```bash
sendpees6 --help
```

This displays all available subcommands and global options.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and exit |
| -v, --verbose | Enable verbose output for packet details |
| -i, --interface | Specify the network interface (e.g., eth0) |
| --spoof | Enable IP/MAC spoofing |

## Examples

### Example 1: Basic ICMPv6 Echo

```bash
sudo sendpees6 icmp6-echo --target 2001:db8::1 --interface eth0
```

Sends a single ICMPv6 echo request to probe the target.

### Example 2: RA Flood Attack

```bash
sudo sendpees6 ra-flood --target-network 2001:db8::/64 --count 1000 --interface eth0 --spoof-source
```

Floods the network with 1000 spoofed router advertisements.

### Example 3: Craft Custom Packet

```bash
sendpees6 craft --type icmp6_ns --output custom.pcap --params "{\"target\": \"2001:db8::1\"}"
```

Crafts a neighbor solicitation packet and saves it to a PCAP file.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Denial of Service]] Network Denial of Service (e.g., RA floods to disrupt IPv6 routing)
- [[Network Service Scanning]] Network Service Scanning (e.g., ICMPv6 probes for host discovery)

### Tactics

- [[Impact]] Impact (DoS attacks)
- [[Initial Access]] Initial Access (Recon via ICMPv6)

## Detection

Indicators and methods for detecting this tool's usage:

- **Network Traffic Anomalies**: Sudden spikes in ICMPv6 traffic (e.g., excessive Router Advertisements or Neighbor Solicitations) visible in tools like Wireshark or tcpdump.
- **Packet Inspection**: Malformed IPv6 headers or unusual source IPs in ICMPv6 packets; use IDS rules for IPv6-specific signatures (e.g., Snort rules for RA floods).
- **System Logs**: Root-level processes spawning network-bound Python scripts; monitor for 'sendpees6' in process lists or firewall logs.
- **PCAP Analysis**: Crafted packets often have non-standard options or extensions; correlate with host logs for unusual interface activity.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Scapy]] (For advanced packet manipulation)
- [[tools/THC-IPv6]] (Companion toolkit for IPv6 attacks)

## References

- Official repository or documentation (if available; check GitHub or security forums)
- IPv6 Security RFCs (e.g., RFC 7113 for ICMPv6 issues)
- MITRE ATT&CK for Enterprise: Network Denial of Service techniques
