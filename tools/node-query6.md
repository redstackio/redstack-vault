---
id: a16018cb-a3d6-4a2f-9b5f-b95f7906dac8
name: node-query6
type: tool
verified: true
created_at: '2019-08-28T21:17:26.579437+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
tags:
  - ipv6
  - icmp6
  - network-attack
  - packet-craft
url: 'https://github.com/example/node-query6'
validated: true
---

# node-query6

**Status**: Unverified

## Overview

node-query6 is a comprehensive toolkit designed to exploit weaknesses in IPv6 and ICMPv6 protocols. It provides utilities for sending crafted packets, performing denial-of-service attacks, and spoofing network discovery messages, along with an integrated packet factory library for custom packet generation. Commonly used in red team operations for IPv6 network reconnaissance and disruption.

## Description

This tool targets inherent vulnerabilities in IPv6 implementations, such as improper handling of ICMPv6 messages, Neighbor Discovery Protocol flaws, and extension header processing. The packet factory library allows users to build and manipulate IPv6 packets programmatically, making it ideal for protocol fuzzing, evasion testing, and targeted attacks in IPv6 environments.

## Features

- ICMPv6 flood attacks for DoS testing
- Neighbor Discovery (ND) spoofing for MITM scenarios
- Custom IPv6 packet crafting with extension headers
- Support for malformed packets to test protocol robustness
- Easy-to-use library for scripting advanced attacks

## Installation

### Requirements

- Node.js (v14 or higher)
- npm package manager
- Linux or macOS with IPv6 support enabled

### Install Commands

```bash
# Clone the repository (assuming open-source; adjust URL as needed)
git clone https://github.com/example/node-query6.git
cd node-query6

# Install dependencies
npm install

# For global installation (optional)
npm install -g .
```

On Kali Linux, it may require additional IPv6 kernel modules: `modprobe ipv6`.

## Basic Usage

```bash
node_query6 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and available modes |
| -v, --verbose | Enable verbose logging for packet details |
| --target | Specify IPv6 target address or network |
| --interface | Bind to a specific network interface (e.g., eth0) |

## Examples

### Example 1: Basic Usage

Perform an ICMPv6 echo flood:

```bash
node_query6 --icmp6-echo-flood --target 2001:db8::1 --count 100
```

### Example 2: Advanced Usage

Spoof ND messages:

```bash
node_query6 --nd-spoof --target-network 2001:db8::/64 --spoof-ip 2001:db8::fake
```

Create a custom packet:

```bash
node_query6 --packet-factory --create --type icmp6-echo --output custom.pcap
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning (for IPv6 discovery)
- [[Network Denial of Service]] Network Denial of Service (ICMPv6 floods)
- [[Adversary-in-the-Middle]] Adversary-in-the-Middle (ND spoofing)

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual ICMPv6 traffic volumes or malformed packets (monitor with tcpdump: `tcpdump ip6 and icmp6`)
- Unexpected ND cache updates on hosts (check with `ndp -a` on BSD/macOS or `ip -6 neigh` on Linux)
- Node.js processes with high network I/O in IPv6 interfaces
- Custom pcap files or library imports in attack scripts

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Scapy]] (for advanced packet crafting)
- [[tools/THC-IPv6]] (alternative IPv6 attack toolkit)

## References

- Official GitHub: https://github.com/example/node-query6
- IPv6 Security Considerations: RFC 4940
- ICMPv6 Attacks: https://tools.ietf.org/html/rfc4890
