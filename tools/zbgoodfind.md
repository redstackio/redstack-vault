---
id: 63da2438-e8c1-4f63-bded-f7adff80019c
name: zbgoodfind
type: tool
verified: true
created_at: '2019-08-28T21:17:40.847816+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
tags:
  - zigbee
  - ieee-802-15-4
  - wireless
  - reconnaissance
url: 'https://github.com/riverloopsec/killerbee'
validated: true
---

# zbgoodfind

**Status**: Unverified

## Overview

zbgoodfind is a utility within the KillerBee framework designed to scan IEEE 802.15.4 channels and identify the most active channel for effective ZigBee network monitoring and analysis. It helps security testers locate networks with high traffic to focus eavesdropping or replay attacks.

## Description

The KillerBee framework, including zbgoodfind, is a Python-based toolkit for interacting with ZigBee and IEEE 802.15.4 devices. zbgoodfind specifically scans all 16 possible channels (11-26) to measure packet activity and recommends the channel with the highest signal or packet count. This is useful in reconnaissance phases for discovering and targeting ZigBee networks in environments like smart homes, industrial control systems, or IoT deployments. It requires a compatible radio interface such as the Atmel RZUSBstick or similar.

## Features

- Channel scanning across IEEE 802.15.4 frequencies
- Activity detection based on packet counts
- Automatic selection of the optimal channel for further operations
- Integration with other KillerBee tools for seamless workflow

## Installation

### Requirements

- Python 2.7 (KillerBee is not fully compatible with Python 3)
- Compatible IEEE 802.15.4 radio hardware (e.g., RZUSBstick, MRF24J40)
- Linux kernel with USB support for the radio interface

### Install Commands

```bash
# Clone the KillerBee repository
git clone https://github.com/riverloopsec/killerbee.git
cd killerbee

# Install dependencies (on Ubuntu/Debian)
sudo apt update
sudo apt install python-dev libusb-1.0-0-dev

# Install KillerBee
sudo python setup.py install
```

For Kali Linux, KillerBee may be available via apt:

```bash
sudo apt install killerbee
```

After installation, ensure your radio device is connected and recognized (e.g., via `lsusb`).

## Basic Usage

```bash
python zbgoodfind.py -i $_INTERFACE
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and usage |
| `-i, --interface $_INTERFACE` | Specify the radio interface device (e.g., `/dev/ttyUSB0`) |
| `-c, --channel $_CHANNEL` | Scan a specific channel instead of all |
| `-t, --time $_TIME` | Scan duration in seconds per channel (default: 10) |

## Examples

### Example 1: Basic Usage

Scan all channels to find the most active one:

```bash
python zbgoodfind.py -i /dev/ttyUSB0
```

### Example 2: Advanced Usage

Scan for 20 seconds per channel on a specific interface:

```bash
python zbgoodfind.py -i /dev/ttyUSB0 -t 20
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning
- [[Network Sniffing]] Network Sniffing

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual USB device connections (e.g., RZUSBstick detected in logs)
- Python processes with KillerBee modules loaded
- Wireless interface activity on 2.4GHz band (channels 11-26)
- Network logs showing IEEE 802.15.4 packet captures

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/KillerBee]]
- [[tools/Wireshark]] (for analyzing captured ZigBee traffic)

## References

- Official GitHub: https://github.com/riverloopsec/killerbee
- KillerBee Documentation: https://killerbee.readthedocs.io/
- ZigBee Security Testing Guide: https://www.blackhat.com/docs/us-13/US-13-Wright-ZigBee.pdf
