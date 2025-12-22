---
id: 09585bec-0eac-4d81-940b-ab5410f84638
type: tool
verified: true
created_at: '2019-08-28T21:17:28.078663Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - ipv6
  - icmp6
  - reconnaissance
  - host-discovery
  - packet-crafting
url: 'https://github.com/vanhauser-thc/thc-ipv6 (related toolkit)'
validated: true
---

# extract_hosts6

**Status**: Unverified

## Overview

extract_hosts6 is a bash-based tool designed to exploit weaknesses in IPv6 and ICMPv6 protocols for host discovery and reconnaissance. It includes capabilities for packet crafting and analysis, making it suitable for identifying IPv6 addresses in network traffic during security assessments.

## Description

This tool targets inherent vulnerabilities in IPv6 implementations, such as neighbor discovery protocol flaws, to extract and enumerate hosts. It can process captured traffic or perform live monitoring, providing a packet factory library for custom ICMPv6 manipulations. Commonly used in red team operations for mapping IPv6 networks where traditional IPv4 tools fall short.

## Features

- Host extraction from PCAP files using IPv6/ICMPv6 parsing
- Live interface monitoring for real-time discovery
- Custom packet crafting for protocol attacks
- Support for link-local and global IPv6 address detection
- Output formatting for integration with other tools like Nmap

## Installation

### Requirements

- Linux environment with bash and tcpdump/libpcap
- Root privileges for packet capture
- IPv6-enabled network interface

### Install Commands

```bash
# Download the script (assuming from a repository)
wget https://example.com/extract_hosts6.sh
chmod +x extract_hosts6.sh

# Or if part of THC-IPv6 toolkit:
git clone https://github.com/vanhauser-thc/thc-ipv6.git
cd thc-ipv6
make
# Note: extract_hosts6.sh may be a custom wrapper or extension
```

## Basic Usage

```bash
./extract_hosts6.sh --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -v, --verbose | Enable verbose output for debugging |
| -f | Process PCAP file |
| -i | Specify interface for live capture |

## Examples

### Example 1: Basic Usage

Extract hosts from a PCAP:

```bash
./extract_hosts6.sh -f network_capture.pcap -o hosts.txt
```

### Example 2: Advanced Usage

Live capture on interface:

```bash
sudo ./extract_hosts6.sh -i eth0 -t 300 -o live_ipv6_hosts.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote System Discovery]] Remote System Discovery (IPv6-specific enumeration)
- [[Network Service Scanning]] Network Service Scanning (via ICMPv6)

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual ICMPv6 traffic spikes (e.g., excessive neighbor solicitations)
- Process monitoring for bash scripts accessing raw sockets
- Network logs showing IPv6 packet crafting anomalies
- PCAP analysis revealing scripted extraction patterns

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/thc-ipv6-toolkit]]
- [[tools/tcpdump]]
- [[tools/Nmap]]

## References

- THC-IPv6 Toolkit documentation
- IPv6 Security Best Practices (RFCs)
