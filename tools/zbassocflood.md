---
id: 73c4aa34-a11d-46db-a55b-227800c58c80
type: tool
verified: true
created_at: '2019-08-28T21:17:39.389313+00:00'
updated_at: '2023-10-01T12:00:00+00:00'
platforms:
  - Linux
tags:
  - zigbee
  - ieee-802-15-4
  - iot
  - denial-of-service
  - killerbee
url: 'https://github.com/riverloopsec/killerbee'
validated: true
---

# zbassocflood

**Status**: Unverified

## Overview

zbassocflood is a specialized tool within the KillerBee framework designed for performing association request flooding attacks against ZigBee and IEEE 802.15.4 networks. It targets coordinators by overwhelming them with fake association requests, leading to denial of service (DoS) conditions that prevent legitimate devices from joining the network. Commonly used in IoT security testing and red teaming for wireless networks.

## Description

KillerBee is a Python-based framework for testing the security of ZigBee and IEEE 802.15.4 devices and networks. zbassocflood specifically exploits the association process in ZigBee protocols by generating and transmitting a high volume of association requests from spoofed device addresses. This can exhaust the coordinator's resources, causing it to drop legitimate requests. The tool requires a compatible IEEE 802.15.4 radio interface (e.g., Atmel RZUSBstick or Raspberry Pi with NRF24L01). It supports channel-specific targeting, PAN ID specification, and options for node emulation or scanning.

## Features

- Feature 1: Generates customizable association request floods with variable packet counts and intervals.
- Feature 2: Supports multiple radio interfaces for flexibility in hardware setups.
- Feature 3: Includes scanning modes to discover active channels and PANs before attacking.
- Feature 4: Spoofs device addresses to mimic multiple joining devices.
- Feature 5: Real-time statistics on packets sent and potential responses.

## Installation

### Requirements

- Python 2.7 or 3.x (KillerBee is Python-based)
- Compatible IEEE 802.15.4 radio hardware (e.g., RZUSBstick, MRF24J40)
- Linux kernel with USB support for the radio interface
- Scapy library for packet crafting (included in KillerBee)

### Install Commands

```bash
# Clone the KillerBee repository
git clone https://github.com/riverloopsec/killerbee.git
cd killerbee

# Install dependencies (on Ubuntu/Debian)
sudo apt update
sudo apt install python3 python3-pip libusb-1.0-0-dev

# Install KillerBee
sudo python3 setup.py install

# For hardware-specific drivers (e.g., Atmel)
sudo apt install atmel-firmware
```

On Kali Linux, KillerBee and zbassocflood are often pre-installed or available via apt:

```bash
sudo apt install killerbee
```

## Basic Usage

```bash
tool-name --help
python zbassocflood.py -h
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and options |
| -i, --interface | Specify the radio interface (e.g., rpi_usb) |
| -v, --verbose | Enable verbose output for debugging |
| -c, --channel | Target ZigBee channel (11-26) |

## Examples

### Example 1: Basic Usage

```bash
python zbassocflood.py -i rpi_usb -c 11 -p 0x1234 -n 1000
```

This floods channel 11 on PAN 0x1234 with 1000 association requests using the rpi_usb interface.

### Example 2: Advanced Usage

```bash
python zbassocflood.py -i atmel_usb -c 15 --scan -n 500 --node
```

This scans for active PANs starting on channel 15, then floods with 500 requests in node emulation mode.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Denial of Service]] Network Denial of Service
- [[OS Exhaustion Flood]] OS Exhaustion Floods

### Tactics

- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor IEEE 802.15.4 traffic for anomalous high volumes of association requests from varied MAC addresses on the same PAN.
- Detection method 2: Use ZigBee sniffers (e.g., Wireshark with ZigBee plugin) to detect flooding patterns on specific channels.
- Detection method 3: Log radio interface activity on potential attacker machines for KillerBee library usage.
- Detection method 4: Network intrusion detection systems (NIDS) tuned for IoT protocols showing coordinator overload (e.g., delayed associations).

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
- [[tools/zbid]]
- [[tools/zbreplay]]

## References

- Official GitHub: https://github.com/riverloopsec/killerbee
- Documentation: https://killerbee.readthedocs.io/
- Related resources: ZigBee specification (IEEE 802.15.4) for association protocol details
