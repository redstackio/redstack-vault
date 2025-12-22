---
id: db375520-8582-4081-8bf3-2521689a6960
type: tool
verified: true
created_at: '2019-08-28T21:17:27.800412+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
tags:
  - ipv6
  - network
  - reconnaissance
  - exploitation
url: 'https://github.com/fgontipof/the-ipv6-toolkit'
validated: true
---

# rs6-ipv6-router-solicitation

**Status**: Unverified

## Overview

rs6 is a component of the SI6 Networks’ IPv6 Toolkit, designed for sending arbitrary IPv6 Router Solicitation (RS) messages. It is used in IPv6 security assessments to solicit Router Advertisements, test network configurations, and evaluate device responses to crafted RS packets for reconnaissance or attack simulation.

## Description

The SI6 IPv6 Toolkit provides a suite of tools for IPv6 security assessment and troubleshooting, including rs6 for Router Solicitation operations. rs6 allows crafting and sending custom RS messages, supporting options for source spoofing, flooding, and interface specification. It helps identify routers, test IPv6 protocol implementations, and simulate attacks like RS flooding. Other toolkit tools include addr6 for address manipulation, ra6 for Router Advertisements, and scan6 for network scanning.

## Features

- Send arbitrary RS messages to unicast or multicast addresses
- Source address and MAC spoofing
- Packet flooding with configurable count and pause
- Interface binding and hop limit control
- Verbose output for packet details

## Installation

### Requirements

- Linux system with IPv6 kernel support
- libpcap and libnet development libraries
- GCC compiler

### Install Commands

```bash
# Clone the repository
git clone https://github.com/fgontipof/the-ipv6-toolkit.git
cd the-ipv6-toolkit

# Configure and build
./configure
make
sudo make install
```

On Kali Linux, it may be available via apt: `sudo apt install ipv6toolkit`

## Basic Usage

```bash
rs6 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -V, --version | Display version |
| -i interface | Bind to specific interface |
| -s srcaddr | Set source IPv6 address |
| -c count | Send multiple packets |
| -p pause | Pause between packets (seconds) |

## Examples

### Example 1: Basic Usage

Send a single RS to all-routers multicast:

```bash
rs6 ff02::2
```

### Example 2: Advanced Usage

Flood RS messages with custom source:

```bash
rs6 -s 2001:db8::100 -c 50 -p 0.5 2001:db8::1
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Vulnerability Scanning]] Scanning IP Blocks (for network discovery via RS)
- [[Network Denial of Service]] Network Denial of Service (for flooding attacks)

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual ICMPv6 RS traffic volume or from spoofed sources
- Network logs showing RS to multicast addresses like ff02::2
- PCAP captures with crafted RS packets lacking standard options
- Host firewall alerts on unexpected IPv6 ICMP traffic

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Nmap]] (for general port scanning)
- [[tools/scapy]] (for custom packet crafting)

## References

- Official GitHub: https://github.com/fgontipof/the-ipv6-toolkit
- SI6 Networks Documentation: https://www.si6networks.com/tools/ipv6toolkit/ipsv6toolkit.shtml
