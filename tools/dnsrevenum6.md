---
id: b6edca9d-2e71-4c28-bf6b-95844e8bf1d2
name: dnsrevenum6
type: tool
verified: true
created_at: '2019-08-28T21:17:26.676290+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - ipv6
  - icmp6
  - enumeration
  - exploitation
url: 'https://github.com/misskeyw/dnsrevenum6'
validated: true
---

# dnsrevenum6

**Status**: Unverified

## Overview

Dnsrevenum6 is a comprehensive toolset designed to exploit the inherent protocol weaknesses in IPv6 and ICMPv6. It provides capabilities for network enumeration, packet crafting, and targeted attacks, making it useful for security testing in IPv6 environments. Common use cases include reverse DNS enumeration, neighbor discovery manipulation, and protocol-based denial-of-service testing.

## Description

The tool includes an easy-to-use packet factory library for generating custom IPv6 and ICMPv6 packets. It targets vulnerabilities such as weak neighbor discovery protocols, allowing for spoofing, flooding, and reconnaissance in IPv6 networks. Dnsrevenum6 is particularly valuable in red team operations assessing IPv6 security postures, identifying misconfigurations, and demonstrating protocol flaws without requiring root privileges in some modes.

## Features

- Feature 1: Reverse DNS enumeration for IPv6 addresses using ICMPv6 queries
- Feature 2: Custom packet crafting library for ICMPv6 types like Neighbor Solicitation/Advertisement
- Feature 3: Attack modes for protocol exploitation, including ND floods and spoofing
- Feature 4: Support for multiple network interfaces and output formats (JSON, TXT)
- Feature 5: Integration with Scapy for advanced packet manipulation

## Installation

### Requirements

- Python 3.6+
- Scapy library (pip install scapy)
- Linux kernel with IPv6 support enabled
- Root privileges for packet injection (optional for enumeration modes)

### Install Commands

```bash
# Clone the repository
sudo apt update && sudo apt install git python3-pip -y
git clone https://github.com/misskeyw/dnsrevenum6.git
cd dnsrevenum6

# Install dependencies
pip3 install -r requirements.txt

# For Kali Linux (often pre-configured for IPv6 tools)
# No additional install needed if Scapy is present
```

## Basic Usage

```bash
python3 dnsrevenum6.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -v, --verbose | Enable verbose output for debugging |
| -i, --interface | Specify network interface (e.g., eth0) |
| -o, --output | Output file for results |

## Examples

### Example 1: Basic Usage (Enumeration)

```bash
python3 dnsrevenum6.py enumerate --interface eth0 --target 2001:db8::1
```

### Example 2: Advanced Usage (Packet Crafting)

```bash
python3 dnsrevenum6.py craft --type 135 --source 2001:db8::1 --destination ff02::1
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning (for enumeration)
- [[Network Denial of Service]] Network Denial of Service (for ICMPv6 floods)
- [[Windows Remote Management]] Windows Remote Services (adapted for IPv6 in cross-platform tests)

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual ICMPv6 traffic spikes (e.g., excessive Neighbor Discovery packets) via tools like Wireshark or tcpdump
- Detection method 2: Python processes with Scapy imports and IPv6 socket bindings in process lists (ps aux | grep dnsrevenum6)
- Detection method 3: Log entries for anomalous IPv6 PTR queries in DNS servers
- Detection method 4: Network IDS alerts for ICMPv6 type 135/136 floods

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
- [[tools/THC-IPV6]]

## References

- Official GitHub: https://github.com/misskeyw/dnsrevenum6
- IPv6 Security Documentation: https://tools.ietf.org/html/rfc8200
- Related Research: Black Hat presentations on IPv6 attacks
