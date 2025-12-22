---
id: dae834ad-815f-4fef-bad6-19572309ebb8
type: tool
verified: true
created_at: '2019-08-28T21:17:29.967310Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - zigbee
  - wireless
  - reconnaissance
  - ieee-802-15-4
url: 'https://github.com/riverloopsec/killerbee'
validated: true
---

# zbstumbler

**Status**: Unverified

## Overview

zbstumbler is a command-line tool from the KillerBee framework designed for discovering active ZigBee and IEEE 802.15.4 networks. It passively scans radio channels for beacon frames emitted by network coordinators, making it ideal for initial reconnaissance in wireless security assessments targeting IoT and smart home environments.

## Description

zbstumbler operates by tuning into specific or all IEEE 802.15.4 channels (11-26) and capturing broadcast beacon packets from ZigBee coordinators. These beacons reveal critical network details such as PAN IDs, coordinator addresses, and protocol versions without actively injecting traffic. As part of the open-source KillerBee suite—a Python-based toolkit for ZigBee security research—zbstumbler requires compatible hardware like the Atmel RZUSBstick or Texas Instruments CC2420 radios. It's commonly used in red team operations to map ZigBee deployments before attempting eavesdropping, replay attacks, or cryptosystem exploitation.

## Features

- Feature 1: Multi-channel scanning for comprehensive network discovery across the 2.4GHz spectrum.
- Feature 2: Passive monitoring to avoid alerting network coordinators or triggering intrusion detection.
- Feature 3: Output parsing for PAN IDs, extended addresses, and beacon payloads to identify network topology.
- Feature 4: Integration with KillerBee's broader ecosystem for chaining into advanced attacks like frame injection.

## Installation

### Requirements

- Python 2.7 or 3.x (KillerBee is Python-based)
- Compatible IEEE 802.15.4 radio hardware (e.g., RZUSBstick, MRF24J40MB)
- USB access and udev rules for the radio interface
- Dependencies: Scapy, PyUSB, and other KillerBee libs

### Install Commands

```bash
# Clone the KillerBee repository (zbstumbler is included)
git clone https://github.com/riverloopsec/killerbee.git
cd killerbee

# Install Python dependencies
pip install -r requirements.txt

# For Ubuntu/Debian, install system deps
sudo apt update
sudo apt install python-usb libusb-1.0-0-dev

# Set up udev rules for radio (example for RZUSBstick)
sudo cp udev-rules/60-killerbee.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules
```

On Kali Linux, KillerBee may be available via apt, but building from source is recommended for the latest features.

## Basic Usage

```bash
zbstumbler --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -i, --interface | Specify the radio interface (e.g., /dev/ttyUSB0) |
| -c, --channel | Channel to scan (11-26 or 'all') |
| -v, --verbose | Enable detailed output including RSSI and frame hex |
| -s, --save | Save scan results to a pcap file for Wireshark analysis |

## Examples

### Example 1: Basic Usage

Scan all channels with default interface:

```bash
zbstumbler -c all
```

### Example 2: Advanced Usage

Targeted scan on channel 15 with verbose output and save:

```bash
zbstumbler -i /dev/ttyUSB0 -c 15 -v -s scan_results.pcap
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Vulnerability Scanning]] Wireless Scanning (for discovering ZigBee networks)

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual USB device connections (e.g., RZUSBstick) monitored via USB logs or endpoint detection.
- Detection method 2: Radio frequency spectrum analysis showing passive sniffing on 2.4GHz channels without active transmissions.
- Detection method 3: KillerBee Python processes (zbstumbler.py) in process lists or network forensics capturing IEEE 802.15.4 frames.

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
- [[tools/Wireshark]] (for analyzing captured pcap files)
- [[Zigbee2MQTT]] (for testing discovered networks)

## References

- Official GitHub: https://github.com/riverloopsec/killerbee
- KillerBee Documentation: https://killerbee.readthedocs.io/
- ZigBee Security Research: https://zbee2.readthedocs.io/en/latest/

*Last updated: 2023-10-01*
