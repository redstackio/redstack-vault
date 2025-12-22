---
id: 0ecbe590-ab35-4b7f-a1bf-6c4d86771574
name: zbdsniff
type: tool
verified: true
created_at: '2019-08-28T21:17:19.705989+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - zigbee
  - ieee-802-15-4
  - wireless
  - sniffing
  - reconnaissance
url: 'https://github.com/riverloopsec/killerbee'
commands:
  - '[[commands/zbdsniff-basic-capture]]'
  - '[[commands/zbdsniff-capture-with-channel]]'
  - '[[commands/zbdsniff-capture-to-pcap]]'
validated: true
---

# zbdsniff

**Status**: Unverified

## Overview

zbdsniff is a packet capture tool within the KillerBee framework, designed for sniffing and analyzing ZigBee and IEEE 802.15.4 wireless network traffic. It is primarily used in security testing to eavesdrop on IoT devices, smart home systems, and industrial control networks that rely on these protocols, enabling reconnaissance, traffic analysis, and potential exploitation of weak encryption or misconfigurations.

## Description

KillerBee is a Python-based framework for testing the security of ZigBee and IEEE 802.15.4 networks. zbdsniff specifically allows users to capture raw packets from compatible radio interfaces, such as Atmel RZUSBstick or similar IEEE 802.15.4 transceivers. It supports passive monitoring, channel hopping, and output in formats like PCAP for further analysis with tools like Wireshark. Common use cases include identifying network keys, replaying captured frames, or detecting unencrypted traffic in environments like home automation (e.g., Philips Hue) or SCADA systems.

## Features

- Feature 1: Passive packet sniffing on specified channels or with hopping
- Feature 2: Support for multiple IEEE 802.15.4 radio interfaces
- Feature 3: Output to PCAP or text files for offline analysis
- Feature 4: Integration with other KillerBee tools for replay and injection

## Installation

### Requirements

- Python 2.7 or 3.x (KillerBee is Python-based)
- Compatible IEEE 802.15.4 hardware (e.g., RZUSBstick, MRF24J40)
- Scapy library for packet manipulation
- Wireshark or tshark for PCAP analysis

### Install Commands

```bash
# Clone the KillerBee repository (zbdsniff is included)
git clone https://github.com/riverloopsec/killerbee.git
cd killerbee

# Install dependencies (for Ubuntu/Debian)
sudo apt update
sudo apt install python3-pip libusb-1.0-0-dev
pip3 install -r requirements.txt

# For Kali Linux, it's often pre-packaged or install via apt
git clone https://github.com/riverloopsec/killerbee.git
# Follow build instructions for your radio interface
```

Note: Hardware setup requires flashing firmware to the radio device; refer to KillerBee docs for device-specific instructions.

## Basic Usage

```bash
zbdsniff -h
```

### Common Options

| Option | Description |
|--------|-------------|
| `-i, --interface` | Specify the radio interface (e.g., `/dev/ttyUSB0` for RZUSBstick) |
| `-c, --channel` | Set the ZigBee channel (11-26) |
| `-w, --write` | Output captured packets to a file (PCAP or text) |
| `-f, --file` | Read from a file instead of live capture |
| `-h, --help` | Show help message |

## Examples

### Example 1: Basic Usage

Capture packets on default channel using a connected interface:

```bash
zbdsniff -i /dev/ttyUSB0
```

### Example 2: Advanced Usage

Capture on channel 15 and save to PCAP:

```bash
zbdsniff -i /dev/ttyUSB0 -c 15 -w capture.pcap
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning (for wireless networks)
- [[Network Sniffing]] Network Sniffing

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Command and Control]] Command and Control (for traffic analysis)

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual USB device connections (e.g., RZUSBstick) monitored via USB logs
- Detection method 2: High volume of IEEE 802.15.4 radio activity on monitored channels
- Detection method 3: Process monitoring for `zbdsniff.py` or KillerBee scripts
- Detection method 4: Network anomaly detection in ZigBee traffic patterns

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/KillerBee]] (parent framework)
- [[tools/Wireshark]] (for PCAP analysis)
- [[tools/ubertooth]] (for Bluetooth sniffing)

## References

- Official GitHub: https://github.com/riverloopsec/killerbee
- Documentation: https://killerbee.readthedocs.io/
- Hardware Guide: Atmel RZUSBstick setup in repo

*Last updated: 2023-10-01*
