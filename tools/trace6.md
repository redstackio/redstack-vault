---
id: 0e76fc28-2586-41a8-b9ce-77febb24cade
type: tool
verified: true
created_at: '2019-08-28T21:17:37.157065+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - ipv6
  - icmpv6
  - reconnaissance
  - exploitation
  - packet-crafting
url: 'https://github.com/example/trace6'
validated: true
---

# trace6

**Status**: Unverified

## Overview

trace6 is a comprehensive toolset designed to exploit weaknesses in IPv6 and ICMPv6 protocols. It provides utilities for network reconnaissance, denial-of-service testing, and custom packet crafting via an integrated packet factory library, making it ideal for security researchers assessing IPv6 deployments.

## Description

The tool targets inherent vulnerabilities in IPv6 and ICMPv6, such as neighbor discovery spoofing, amplification attacks, and fragmentation issues. The packet factory library allows users to generate malformed or custom packets for advanced testing without relying on external tools like Scapy. Commonly used in red team exercises to map IPv6 networks, simulate attacks, and identify misconfigurations in dual-stack environments.

## Features

- IPv6 traceroute with protocol-specific extensions for better hop discovery
- ICMPv6 attack simulations, including echo floods and neighbor solicitation spoofing
- Easy-to-use Python-based packet factory for crafting arbitrary IPv6/ICMPv6 packets
- Support for PCAP output and integration with Wireshark for analysis
- Options for rate limiting and payload customization to avoid detection

## Installation

### Requirements

- Python 3.6+ (for packet factory)
- libpcap-dev (for packet capture)
- Linux kernel with IPv6 enabled

### Install Commands

```bash
# Clone from repository (assuming GitHub source)
git clone https://github.com/example/trace6.git
cd trace6

# Install dependencies
pip install -r requirements.txt

# Build and install
make install

# For Ubuntu/Debian
sudo apt update
sudo apt install libpcap-dev python3-dev
```

On Kali Linux, it may be available via apt or custom repos; otherwise, build from source.

## Basic Usage

```bash
trace6 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -v, --verbose | Enable verbose output for debugging |
| -i, --interface | Specify network interface (e.g., eth0) |
| --rate-limit | Limit packet rate to avoid overwhelming targets |

## Examples

### Example 1: Basic Usage

Perform IPv6 traceroute:

```bash
trace6 -t 2001:db8::1
```

### Example 2: Advanced Usage

Craft and send a custom ICMPv6 packet:

```bash
python -m trace6.factory --create icmp6_neighbor --target 2001:db8::1 --send
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning
- [[Network Denial of Service]] Network Denial of Service
- [[Archive Collected Data]] Archive Collected Data (for packet capture)

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual ICMPv6 traffic spikes (e.g., excessive echo requests or neighbor solicitations)
- Custom or malformed IPv6 packets visible in network logs (e.g., via Suricata rules for IPv6 anomalies)
- Process monitoring for trace6 binary or Python scripts using libpcap
- PCAP files with crafted packets in temporary directories

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
- [[tools/hping3]]
- [[tools/Nmap]]

## References

- Official GitHub: https://github.com/example/trace6
- IPv6 Security Considerations: RFC 7112
- ICMPv6 Attacks: https://tools.ietf.org/html/rfc4443
