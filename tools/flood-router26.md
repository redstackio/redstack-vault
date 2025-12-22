---
id: 167403c9-d439-4b16-a265-0685e20ae3a6
name: flood-router26
type: tool
verified: true
created_at: '2019-08-28T21:17:26.617192+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - ipv6
  - icmpv6
  - network-attack
  - dos
url: 'https://github.com/flood-router26/example-repo'
validated: true
---

# flood-router26

**Status**: Unverified

## Overview

flood_router26 is a specialized toolkit for exploiting weaknesses in IPv6 and ICMPv6 protocols. It includes utilities for packet crafting, flooding attacks, and protocol manipulation, making it useful for security testing IPv6 networks, denial-of-service simulations, and research into protocol vulnerabilities.

## Description

The tool provides a complete set of features to target inherent flaws in IPv6 and ICMPv6, such as excessive packet processing or spoofing opportunities. It features an easy-to-use packet factory library for custom IPv6 packet construction. Common use cases include testing router resilience to floods, simulating rogue advertisements, and educational demonstrations of IPv6 security issues.

## Features

- ICMPv6 flood generation for DoS testing
- Rogue Router Advertisement (RA) spoofing
- Custom IPv6 packet factory for advanced crafting
- Support for various network interfaces
- Scriptable via Python for automation

## Installation

### Requirements

- Python 3.6+
- Scapy library (pip install scapy)
- Root privileges for raw socket access
- Linux kernel with IPv6 support

### Install Commands

```bash
# Clone the repository (assuming GitHub source)
git clone https://github.com/example/flood-router26.git
cd flood-router26

# Install dependencies
pip install -r requirements.txt

# Make executable (if needed)
chmod +x flood_router26.py
```

For Kali Linux, it may be available via apt or custom repos; otherwise, build from source.

## Basic Usage

```bash
tool-name --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -v, --verbose | Enable verbose output for debugging |
| --interface | Specify network interface |
| --mode | Select attack mode (e.g., icmp6-flood, ra-flood) |

## Examples

### Example 1: Basic Usage

```python
python flood_router26.py --mode icmp6-flood --target 2001:db8::1
```

### Example 2: Advanced Usage

```python
python flood_router26.py --mode ra-flood --interface eth0 --target-network 2001:db8::/64 --lifetime 1800
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Denial of Service]] Network Denial of Service
- [[Data Manipulation]] Data Manipulation (for protocol spoofing)

### Tactics

- [[Impact]] Impact
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual ICMPv6 traffic spikes (e.g., excessive echo requests)
- Rogue RA packets via network monitoring (e.g., Wireshark filters for ICMPv6 type 134)
- High outbound IPv6 traffic from non-router hosts
- Process monitoring for flood_router26 or scapy usage

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
- [[tools/THC-IPv6]]

## References

- Official documentation: https://github.com/example/flood-router26
- IPv6 Security Considerations: RFC 7113
- Related resources: THC-IPv6 Toolkit documentation
