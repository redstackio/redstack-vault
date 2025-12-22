---
id: 006e4573-b946-45b6-93d0-9966d1083d3c
name: sendpeesmp6
type: tool
verified: true
created_at: '2019-08-28T21:17:38.837021+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - ipv6
  - icmpv6
  - network-attack
  - packet-craft
url: 'https://github.com/example/sendpeesmp6'
validated: true
---

# sendpeesmp6

**Status**: Unverified

## Overview

sendpeesmp6 is a comprehensive toolkit designed to exploit vulnerabilities in IPv6 and ICMPv6 protocols. It provides utilities for crafting malicious packets, performing network attacks like rogue router advertisements and floods, and includes a flexible packet factory library for custom packet generation. Commonly used in penetration testing to demonstrate IPv6 protocol weaknesses in enterprise networks.

## Description

The tool targets inherent flaws in IPv6 and ICMPv6, such as lack of authentication in router advertisements and susceptibility to amplification attacks. It supports both command-line invocations for quick attacks and a Python library for advanced scripting. Ideal for red team operations assessing IPv6 security postures, including neighbor discovery manipulation and denial-of-service scenarios.

## Features

- Feature 1: Rogue RA and RS packet sending to hijack IPv6 routing
- Feature 2: ICMPv6 flood attacks for DoS testing
- Feature 3: Packet factory library for building custom IPv6/ICMPv6 payloads
- Feature 4: Spoofing support for source IP and MAC addresses
- Feature 5: Integration with Scapy-like syntax for packet manipulation

## Installation

### Requirements

- Python 3.6+
- Scapy library (pip install scapy)
- Root privileges for raw socket access
- Linux kernel with IPv6 enabled

### Install Commands

```bash
# Clone from repository (assuming GitHub source)
git clone https://github.com/example/sendpeesmp6.git
cd sendpeesmp6

# Install dependencies
pip install -r requirements.txt

# Install the tool
pip install .
```

For Kali Linux: Available via apt or manual install as above.

## Basic Usage

```bash
tool-name --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -v, --verbose | Enable verbose output for debugging |
| -i, --interface | Specify network interface |
| --spoof-source | Spoof source IP/MAC |

## Examples

### Example 1: Basic Usage

Send a simple ICMPv6 echo request:

```python
sendpeesmp6 --send-icmp6 --type 128 2001:db8::1
```

### Example 2: Advanced Usage

Build and send a custom RA using factory:

```python
sendpeesmp6 --factory --build ipv6_ra --options "{\"prefix\": \"fd00::/64\"}" --send
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Denial of Service]] Network Denial of Service
- [[Archive via Utility]] Archive Files (for packet payloads)
- [[Network Service Scanning]] Network Service Scanning (via ICMPv6 discovery)

### Tactics

- [[Impact]] Impact
- [[Initial Access]] Initial Access (via network manipulation)

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual ICMPv6 traffic spikes (e.g., high volume of type 134 RAs)
- Detection method 2: Anomaly in IPv6 neighbor discovery logs
- Detection method 3: Packet captures showing spoofed source IPs in ICMPv6
- Detection method 4: Process monitoring for python/sendpeesmp6 executions with raw sockets

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

- Official GitHub: https://github.com/example/sendpeesmp6
- IPv6 Security Toolkit documentation
- RFC 4861: Neighbor Discovery for IP version 6
