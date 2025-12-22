---
id: 39bb50e0-a67a-4e4e-b3d8-cb6c347968d7
type: tool
verified: true
created_at: '2019-08-28T21:17:38.959570+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
tags:
  - wake-on-lan
  - network
  - apple
  - bruteforce
  - sniffing
url: 'https://github.com/scipag/wol-e'
description: >-
  A suite of tools for interacting with Wake-on-LAN (WoL) features, particularly
  on Apple devices.
validated: true
---

# wol-e

**Status**: Unverified

## Overview

wol-e is a suite of command-line tools designed to exploit and interact with the Wake-on-LAN (WoL) feature commonly enabled on network-attached computers, especially Apple devices where it is often active by default. It supports bruteforcing MAC addresses, sniffing WoL magic packets and passwords, waking individual or multiple clients, and scanning for WoL-enabled Apple devices on the network. This tool is useful in red teaming for remote device activation, network reconnaissance, and persistence scenarios.

## Description

The wol-e suite provides modular functionality for WoL operations over UDP (port 9 by default). It can be used to wake devices without physical access, sniff ongoing WoL traffic for intelligence gathering, and perform targeted or bulk activations. Key use cases include waking dormant targets for further exploitation, mapping network devices via WoL responses, and bruteforcing in environments with unknown MAC addresses. It requires root privileges for packet sniffing and is primarily targeted at Ethernet networks.

## Features

- Bruteforce MAC addresses to wake unknown clients
- Sniff and log WoL magic packets to disk
- Capture and decrypt WoL passwords from network traffic
- Send targeted WoL packets to single devices
- Scan networks for Apple devices with WoL enabled
- Broadcast bulk WoL requests to multiple detected clients

## Installation

### Requirements

- Python 3.x
- Scapy library for packet crafting and sniffing
- Root/admin privileges for network interface access
- Linux or macOS with compatible network stack

### Install Commands

```bash
# Clone the repository
git clone https://github.com/scipag/wol-e.git
cd wol-e

# Install dependencies
pip install -r requirements.txt

# For sniffing capabilities, ensure Scapy is installed
pip install scapy
```

On Kali Linux, it may be available via apt or manual build.

## Basic Usage

```bash
wol-e --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-i, --interface` | Specify network interface (e.g., eth0) |
| `-p, --port` | UDP port for WoL (default: 9) |
| `-v, --verbose` | Enable verbose output |
| `--mac` | Target MAC address (format: AA:BB:CC:DD:EE:FF) |

## Examples

### Example 1: Basic Usage - Wake a Single Device

```bash
wol-e wake --mac 00:11:22:33:44:55 --ip 192.168.1.100
```

This sends a WoL magic packet to wake the device at the specified IP.

### Example 2: Advanced Usage - Sniff WoL Packets

```bash
wol-e sniff --interface eth0 --output wol_log.pcap
```

Captures WoL traffic and saves to a PCAP file for analysis.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Discovery (for scanning WoL-enabled devices)
- [[Windows Remote Management]] Remote Services: Windows Remote Management (adapted for WoL remote activation)

### Tactics

- [[Discovery]] Discovery
- [[Lateral Movement]] Lateral Movement

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual UDP traffic on port 9 (WoL magic packets: FF:FF:FF:FF:FF:FF followed by MAC)
- High volume of broadcast ARP or UDP packets in network logs
- Packet captures showing repeated MAC bruteforcing patterns
- Root-level processes sniffing interfaces (e.g., via Scapy)
- Log entries for wol-e or Scapy in system process lists

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/ettercap]] (for general network sniffing)
- [[tools/Wireshark]] (for PCAP analysis of WoL traffic)

## References

- Official GitHub: https://github.com/scipag/wol-e
- Wake-on-LAN Protocol: https://en.wikipedia.org/wiki/Wake-on-LAN
- Scapy Documentation: https://scapy.net/

*Last updated: 2023-10-01*
