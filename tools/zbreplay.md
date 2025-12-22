---
id: ace2b2b0-f17f-4d51-81a2-92b24fb6f0b0
type: tool
verified: true
created_at: '2019-08-28T21:17:18.756233+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - zigbee
  - ieee-802-15-4
  - wireless
  - replay
  - killerbee
url: 'https://github.com/riverloopsec/killerbee'
validated: true
---

# zbreplay

**Status**: Unverified

## Overview

zbreplay is a command-line tool within the KillerBee framework designed for replaying captured ZigBee and IEEE 802.15.4 network traffic. It allows security researchers to simulate attacks by retransmitting intercepted frames, useful for testing device responses, fuzzing, or demonstrating vulnerabilities in wireless IoT networks.

## Description

KillerBee is a Python-based framework for interacting with ZigBee and IEEE 802.15.4 networks. zbreplay specifically handles the replay of previously captured packets from PCAP files using compatible radio interfaces like Atmel RZUSBStick or Texas Instruments CC2420. It supports features like channel hopping and timed replays, enabling realistic attack simulations without generating new traffic.

## Features

- Feature 1: Replay of PCAP-captured ZigBee frames with precise timing preservation
- Feature 2: Support for multiple radio interfaces and channel configurations
- Feature 3: Integration with other KillerBee tools for capture-replay workflows
- Feature 4: Offline analysis and modification of replayed frames before transmission

## Installation

### Requirements

- Python 2.7 or 3.x
- Compatible IEEE 802.15.4 radio hardware (e.g., RZUSBStick)
- Scapy library for packet handling
- libpcap for PCAP support

### Install Commands

```bash
# Clone the KillerBee repository (zbreplay is included)
git clone https://github.com/riverloopsec/killerbee.git
cd killerbee

# Install dependencies on Ubuntu/Debian
sudo apt update
sudo apt install python3-pip libpcap-dev
pip3 install -r requirements.txt

# For Kali Linux (often pre-configured)
sudo apt install killerbee
```

## Basic Usage

```bash
zbreplay --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -v, --verbose | Enable verbose output for debugging |
| -f | Specify input PCAP file for replay |
| -i | Set the radio interface device |

## Examples

### Example 1: Basic Usage

```bash
zbreplay -f capture.pcap -i /dev/ttyUSB0
```

### Example 2: Advanced Usage

```bash
zbreplay -f capture.pcap -i /dev/ttyUSB0 -c
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Container Administration Command]] Container Administration (for IoT device manipulation)
- [[Abuse Elevation Control Mechanism]] Abuse Elevation Control Mechanism (wireless privilege escalation testing)

### Tactics

- [[Defense Evasion]] Defense Evasion
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual IEEE 802.15.4 radio transmissions on non-standard channels
- Detection method 2: Presence of KillerBee Python processes or PCAP files with ZigBee frames
- Detection method 3: Network monitoring for replayed packet patterns matching known captures

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
- [[tools/Wireshark]] (for PCAP analysis)

## References

- Official GitHub: https://github.com/riverloopsec/killerbee
- Documentation: https://killerbee.readthedocs.io/en/latest/tools/zbreplay.html
