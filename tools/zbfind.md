---
id: afe67047-0b7c-4f5a-b0d3-0c0c1bb1801f
name: zbfind
type: tool
verified: true
created_at: '2019-08-28T21:17:26.895061+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
description: >-
  A reconnaissance tool within the KillerBee framework for discovering ZigBee
  networks by scanning IEEE 802.15.4 channels for beacons and coordinators.
url: 'https://github.com/riverloopsec/killerbee'
tags:
  - zigbee
  - wireless
  - reconnaissance
  - iot
platforms:
  - Linux
validated: true
---

# zbfind

**Status**: Unverified

## Overview

zbfind is a Python-based script from the KillerBee framework used for passive reconnaissance of ZigBee and IEEE 802.15.4 networks. It scans for active coordinators by detecting beacon frames, identifying network parameters such as channel, PAN ID, and MAC addresses. This tool is essential for security assessments of IoT devices and smart home systems relying on ZigBee protocols.

## Description

zbfind operates by putting a compatible radio interface into promiscuous mode and listening across ZigBee channels (11-26) for network beacons. It supports various hardware transceivers and can output details for further analysis or targeted attacks. Commonly used in wireless penetration testing to map ZigBee deployments without active transmission, reducing detection risk.

## Features

- Multi-channel scanning for beacon detection
- Identification of PAN IDs, channels, and coordinator extended addresses
- Configurable scan timeouts and interface selection
- Output in human-readable format for quick analysis
- Integration with other KillerBee tools for deeper exploitation

## Installation

### Requirements

- Python 2.7 (KillerBee is a legacy framework)
- Compatible IEEE 802.15.4 radio (e.g., Atmel RZUSBStick, Texas Instruments CC2420 USB dongle)
- Linux kernel with USB support for the radio device
- Dependencies: Scapy, USB libraries (libusb)

### Install Commands

```bash
# Clone and install KillerBee (zbfind is included)
git clone https://github.com/riverloopsec/killerbee.git
cd killerbee
sudo apt update && sudo apt install -y python-usb libusb-1.0-0-dev
sudo python setup.py install
```

After installation, zbfind is available as `python tools/zbfind.py`.

## Basic Usage

```bash
python tools/zbfind.py -h
```

This displays help with all options.

### Common Options

| Option | Description |
|--------|-------------|
| `-i, --iface INTERFACE` | Specify the radio interface (e.g., `/dev/ttyUSB0`) |
| `-c, --channel CHANNEL` | Scan a specific channel (11-26) |
| `-t, --timeout SECONDS` | Scan duration per channel in seconds (default: 30) |
| `-h, --help` | Show help message |

## Examples

### Example 1: Basic Usage

Scan all channels using default interface and timeout.

```bash
python tools/zbfind.py -i /dev/ttyUSB0
```

### Example 2: Advanced Usage

Scan a specific channel for an extended period.

```bash
python tools/zbfind.py -i /dev/ttyUSB0 -c 15 -t 120
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning (Wireless)
- [[Network Service Scanning]] Network Service Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual USB device connections (e.g., RZUSBStick enumerated in logs)
- High radio transmission/reception activity on 2.4GHz band (IEEE 802.15.4)
- Process monitoring for `zbfind.py` or KillerBee scripts
- Network traffic analysis showing ZigBee beacon sniffing patterns

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/KillerBee]] (Parent framework)
- [[tools/ubertooth]] (For Bluetooth reconnaissance)

## References

- Official GitHub: https://github.com/riverloopsec/killerbee
- ZigBee Security Testing Guide: https://www.blackhat.com/docs/us-13/US-13-Wright-ZigBee.pdf
