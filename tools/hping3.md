---
id: e49ad9f7-620f-495f-b2d2-60bd0957388d
type: tool
verified: true
created_at: '2019-08-28T21:17:40.218139+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - network
  - reconnaissance
  - scanning
  - packet-crafting
url: 'http://www.hping.org/'
commands:
  - '[[commands/hping3-icmp-echo-request]]'
  - '[[commands/hping3-tcp-syn-scan]]'
  - '[[commands/hping3-udp-flood]]'
  - '[[commands/hping3-traceroute]]'
validated: true
---

# hping3

**Status**: Unverified

## Overview

hping3 is a command-line oriented TCP/IP packet assembler and analyzer. Inspired by the ping utility, it extends beyond ICMP echo requests to support TCP, UDP, ICMP, and RAW-IP protocols. It includes traceroute mode, covert channel file transfer capabilities, and is commonly used for firewall testing, advanced port scanning, and network diagnostics in security testing.

## Description

hping3 allows users to craft and send custom packets for various protocols, making it versatile for network testing, security audits, and educational purposes. While historically a security tool, it aids in non-malicious tasks like path MTU discovery and TCP/IP stack auditing. Key use cases include firewall rule testing, port scanning beyond standard tools, and simulating network conditions with fragmentation or TOS manipulation.

## Features

- Feature 1: Supports TCP, UDP, ICMP, and RAW-IP packet crafting with customizable headers.
- Feature 2: Traceroute functionality across multiple protocols for path discovery.
- Feature 3: Covert channel support for file transfer over crafted packets.
- Feature 4: Advanced scanning options including SYN floods, fragmentation, and idle scanning.
- Feature 5: Remote OS fingerprinting and uptime guessing through packet responses.

## Installation

### Requirements

- Linux kernel with raw socket support.
- Root privileges for certain packet crafting features.

### Install Commands

```bash
# On Kali Linux (pre-installed)

# On Ubuntu/Debian
apt update && apt install hping3

# On macOS (via Homebrew)
brew install hping

# From source
wget http://www.hping.org/hping3-20050905.tar.gz
tar -xvzf hping3-20050905.tar.gz
cd hping3-20050905
./configure && make && sudo make install
```

## Basic Usage

```bash
hping3 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -1 | ICMP mode (echo request/reply) |
| --tcp | TCP mode |
| --udp | UDP mode |
| -p | Destination port |
| -c | Packet count |
| --flood | Send packets as fast as possible |
| --traceroute | Traceroute mode |
| -V | Verbose output |

## Examples

### Example 1: Basic Usage

```bash
hping3 -1 192.168.1.1
```

### Example 2: Advanced Usage

```bash
hping3 --syn -p 80 --flood 192.168.1.1
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning
- [[Active Scanning]] Active Scanning
- [[Network Denial of Service]] Network Denial of Service

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual packet patterns like fragmented or malformed TCP/UDP/ICMP traffic from a single source.
- Detection method 2: High volume of SYN packets without corresponding ACKs indicating scanning or flooding.
- Detection method 3: Network logs showing raw IP packets or non-standard protocol combinations.
- Detection method 4: Process monitoring for hping3 binary execution on endpoints.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Nmap]]
- [[tools/scapy]]

## References

- Official website: http://www.hping.org/
- Man page: man hping3
- GitHub mirror: https://github.com/antirez/hping
