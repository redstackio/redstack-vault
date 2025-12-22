---
type: tool
description: >-
  DHCPig is a Python-based tool for executing advanced DHCP exhaustion attacks
  on local area networks, consuming available IP addresses and disrupting
  network connectivity.
url: 'https://github.com/Hood3x3/dhcpig'
tags:
  - dhcp
  - exhaustion
  - dos
  - network-attack
platforms:
  - Linux
verified: true
validated: true
---

# DHCPig

**Status**: Unverified

## Overview

DHCPig is a specialized tool designed for offensive security testing, focusing on DHCP protocol exploitation. It performs an exhaustion attack by requesting and consuming all available DHCP leases on a network, preventing legitimate users from obtaining IP addresses. Additionally, it releases existing leases and sends gratuitous ARP packets to disrupt Windows hosts, effectively knocking them offline. This tool is useful in red team exercises simulating network denial-of-service scenarios within controlled environments.

## Description

DHCPig leverages the Scapy library to craft and send DHCP packets at high volume. Once executed on a specified network interface, it floods the DHCP server with discovery requests, assigns itself multiple IP addresses, and then releases them to force reallocation cycles. The gratuitous ARP component poisons ARP caches on Windows machines, leading to communication failures. It requires administrative privileges for raw socket access and has been tested across various Linux distributions and DHCP servers like ISC DHCP and Windows Server implementations. No configuration files are needed; operation is straightforward with interface specification.

## Features

- **IP Exhaustion**: Consumes all available DHCP leases to block new connections.
- **Lease Release**: Forces release of active leases to increase disruption.
- **Gratuitous ARP Attacks**: Targets Windows hosts to cause offline disruptions.
- **No Configuration Required**: Simple execution with minimal parameters.
- **Cross-Server Compatibility**: Works against ISC, Windows 2003/2008, and similar DHCP implementations.

## Installation

### Requirements

- Python 3.x
- Scapy library version 2.1 or higher
- Administrative (root) privileges for packet crafting
- Linux kernel with raw socket support

### Install Commands

```bash
# Install Scapy if not present (on Ubuntu/Debian)
sudo apt update && sudo apt install python3-scapy

# Or via pip
pip3 install scapy

# Download the tool (assuming from GitHub)
git clone https://github.com/Hood3x3/dhcpig.git
cd dhcpig
# The main script is pig.py
```

For Kali Linux, Scapy is often pre-installed, but verify with `pip3 show scapy`.

## Basic Usage

```bash
python3 pig.py $_INTERFACE
```

Replace `$_INTERFACE` with your network interface (e.g., `eth0` or `wlan0`). Run as root for full functionality.

### Common Options

| Option | Description |
|--------|-------------|
| No additional CLI options; interface is the only parameter | Pass network interface directly |

## Examples

### Example 1: Basic Exhaustion Attack

```bash
sudo python3 pig.py eth0
```

This initiates the attack on the `eth0` interface, consuming IPs and sending ARP disruptions.

### Example 2: Advanced Usage

The tool does not support extensive options, but you can monitor with Wireshark simultaneously:

```bash
# Run in one terminal
sudo python3 pig.py wlan0

# In another, capture traffic
sudo wireshark -i wlan0 -f "udp port 67 or 68"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Denial of Service]] Network Denial of Service
- [[Direct Network Flood]] IPv4 Address Conflict

### Tactics

- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Sudden spike in DHCP Discover/Offer packets from a single MAC address.
- Rapid IP lease consumption and releases visible in DHCP server logs.
- Gratuitous ARP packets flooding the network, detectable via ARP monitoring tools like arpwatch.
- High outbound UDP traffic on ports 67/68 from an unexpected source.
- Use network intrusion detection systems (e.g., Snort rules for DHCP floods) or SIEM alerts for anomalous DHCP activity.

## Related Commands

- [[commands/dhcpig-run-exhaustion]]

## References

- Official GitHub Repository: https://github.com/Hood3x3/dhcpig
- Scapy Documentation: https://scapy.net/
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1498/
