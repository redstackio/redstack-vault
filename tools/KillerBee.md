---
id: e59f38cd-bf81-4024-9865-5dc8c85507f7
type: tool
description: >-
  Python-based framework for testing and exploiting ZigBee and IEEE 802.15.4
  networks, enabling eavesdropping, traffic replay, and cryptosystem attacks.
verified: true
created_at: '2019-08-28T21:17:38.554000+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
url: 'https://github.com/riverloopsec/killerbee'
tags:
  - zigbee
  - iot
  - wireless
  - exploitation
  - eavesdropping
platforms:
  - Linux
commands:
  - '[[commands/killerbee-zbscan-network-discovery]]'
  - '[[commands/killerbee-zbdump-traffic-capture]]'
  - '[[commands/killerbee-zbreplay-traffic-replay]]'
validated: true
---

# KillerBee

**Status**: Unverified

## Overview

KillerBee is a Python-based framework and toolset designed for security testing of ZigBee and IEEE 802.15.4 wireless networks. It supports activities such as network discovery, traffic sniffing, replay attacks, fuzzing, and cryptosystem analysis, making it valuable for red team operations targeting IoT devices, smart home systems, and industrial control networks.

## Description

KillerBee provides a suite of command-line tools built on Python scripts that interface with compatible IEEE 802.15.4 radio hardware (e.g., Atmel RZUSBstick, Texas Instruments CC2531). Users can perform passive reconnaissance like eavesdropping on unencrypted traffic, active attacks such as replaying captured packets to disrupt networks or extract keys, and custom fuzzing for vulnerability discovery. The framework is extensible, allowing developers to create custom scripts for advanced ZigBee protocol manipulation. It is commonly used in wireless penetration testing to identify weaknesses in device authentication, encryption, and network association processes.

## Features

- **Network Scanning**: Discover active ZigBee networks, coordinators, and devices.
- **Traffic Capture**: Sniff and log raw or decrypted packets for analysis.
- **Replay Attacks**: Replay captured traffic to test network resilience or impersonate devices.
- **Fuzzing Support**: Inject malformed packets to uncover protocol vulnerabilities.
- **Key Extraction**: Attack weak cryptosystems like legacy ZigBee implementations.
- **Extensibility**: Python API for building custom tools and automating attacks.

## Installation

### Requirements

- Python 2.7 (legacy support; some forks use Python 3)
- Compatible IEEE 802.15.4 hardware (e.g., RZUSBstick, CC2531 USB dongle)
- Scapy library for packet manipulation
- Linux kernel with USB support for radio interfaces

### Install Commands

```bash
# Clone the repository
sudo apt update
sudo apt install git python2.7 python-scapy libusb-1.0-0-dev

git clone https://github.com/riverloopsec/killerbee.git
cd killerbee
sudo python2.7 setup.py install

# Flash firmware to hardware if needed (e.g., for CC2531)
# Use additional tools like flash_cc2531 for firmware
```

For Kali Linux, it may require manual dependency resolution due to Python 2 deprecation; consider community forks for Python 3 compatibility.

## Basic Usage

```bash
# List available KillerBee tools
ls /usr/local/bin/killerbee*

# Check hardware compatibility
zbid -h
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Display help for the specific tool |
| `-i, --interface` | Specify the radio interface device (e.g., /dev/ttyUSB0) |
| `-v, --verbose` | Enable verbose logging for debugging |

## Examples

### Example 1: Basic Usage

Scan for nearby ZigBee networks using the zbscan tool:

```bash
killerbee-zbscan -i /dev/ttyUSB0
```

### Example 2: Advanced Usage

Capture traffic to a pcap file and replay it:

```bash
# Capture
killerbee-zbdump -i /dev/ttyUSB0 -w capture.pcap

# Replay after capture
killerbee-zbreplay -i /dev/ttyUSB0 -r capture.pcap
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Vulnerability Scanning]] Wireless Scanning (for network discovery)
- [[Archive via Utility]] Archive Collected Data: Archive via Utility (for traffic capture and analysis)
- [[Forge Web Credentials]] Forge Web Credentials (for cryptosystem attacks in ZigBee)

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Discovery]] Discovery
- [[Command and Control]] Command and Control (via replay for C2 simulation)

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual USB device connections (e.g., IEEE 802.15.4 radios like CC2531)
- High volume of 2.4 GHz wireless traffic anomalies in network monitoring tools (e.g., Wireshark with ZigBee dissectors)
- Python processes with Scapy or KillerBee modules running on attacker machines
- Log entries for /dev/ttyUSB* access or firmware flashing attempts
- Disrupted ZigBee networks showing replayed packets or fuzzing artifacts

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Scapy]] (for packet crafting integration)
- [[tools/Wireshark]] (for analyzing captured ZigBee traffic)
- [[tools/Ubertooth]] (for Bluetooth companion testing)

## References

- Official GitHub: https://github.com/riverloopsec/killerbee
- Documentation: Included in repo README and tool --help outputs
- ZigBee Security Whitepapers: IEEE 802.15.4 standards and KillerBee research papers
