---
id: 52573100-be86-424c-872d-bbdc37472d61
name: zbdump
type: tool
verified: true
created_at: '2019-08-28T21:17:38.172515+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - wireless
  - zigbee
  - iot
  - capture
url: 'https://github.com/riverloopsec/killerbee'
validated: true
---

# zbdump

**Status**: Unverified

## Overview

zbdump is a command-line tool from the KillerBee framework designed for capturing and dumping ZigBee and IEEE 802.15.4 network traffic. It enables passive eavesdropping on wireless IoT networks, making it essential for security assessments of smart home devices, industrial sensors, and other ZigBee-based systems.

## Description

zbdump operates with compatible IEEE 802.15.4 radio interfaces (e.g., Atmel RZUSBstick or Texas Instruments CC2531) to sniff raw frames from ZigBee networks. It supports saving captures in pcap format for analysis with tools like Wireshark. Part of the open-source KillerBee suite, zbdump is used in offensive security for reconnaissance, traffic analysis, and identifying encryption weaknesses in ZigBee implementations. It does not perform active attacks but provides foundational data for further exploitation.

## Features

- Feature 1: Passive packet capture on specified or all channels (11-26 for ZigBee)
- Feature 2: Output to standard pcap format for compatibility with analysis tools
- Feature 3: Support for various radio dongles via libusb
- Feature 4: Optional verbose logging and frame counting during capture

## Installation

### Requirements

- Python 2.7 or 3.x (KillerBee is Python-based)
- libusb-1.0 for radio interface communication
- Compatible hardware: Atmel RZUSBstick, TI CC2531 USB dongle, or similar IEEE 802.15.4 transceivers
- Wireshark or tshark for post-capture analysis

### Install Commands

```bash
# Clone the KillerBee repository (zbdump is included)
git clone https://github.com/riverloopsec/killerbee.git
cd killerbee

# Install dependencies on Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip libusb-1.0-0-dev

# Install KillerBee (includes zbdump)
sudo python3 setup.py install

# For Kali Linux (often pre-configured, but verify)
sudo apt install killerbee
```

## Basic Usage

```bash
zbdump --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and options |
| -i, --interface | Specify the radio interface device |
| -w, --write | Output file for pcap dump |
| -c, --channel | Capture on a specific channel (e.g., 11-26) |
| -v, --verbose | Enable verbose output during capture |

## Examples

### Example 1: Basic Usage

```bash
zbdump -i /dev/ttyUSB0 -w capture.pcap
```

Capture traffic from the connected dongle and save to capture.pcap. Run for a set duration or until Ctrl+C.

### Example 2: Advanced Usage

```bash
zbdump -i /dev/ttyUSB0 -w filtered.pcap -c 15 -v
```

Capture verbose output on channel 15, useful for targeting known ZigBee networks.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning (for wireless network discovery)
- [[Network Sniffing]] Network Sniffing

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual USB device connections (e.g., IEEE 802.15.4 dongles) via USB logs (/var/log/usb.log)
- Detection method 2: libusb process activity or pcap files in unexpected locations
- Detection method 3: Network monitoring for IEEE 802.15.4 traffic anomalies in air-gapped or IoT segments

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
- [[tools/Wireshark]] (for analyzing captures)

## References

- Official GitHub: https://github.com/riverloopsec/killerbee
- Documentation: https://killerbee.readthedocs.io/
- Hardware compatibility: Check repo for supported dongles
