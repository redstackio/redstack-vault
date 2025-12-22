---
id: 961c543f-b290-4d01-a18d-8287872c3f9f
type: tool
verified: true
created_at: '2019-08-28T21:17:38.455399+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - zigbee
  - ieee-802-15-4
  - wireless
  - killerbee
  - iot
url: 'https://github.com/riverloopsec/killerbee'
validated: true
---

# zbid

**Status**: Unverified

## Overview

zbid is a command-line tool within the KillerBee framework designed for identifying and enumerating ZigBee and IEEE 802.15.4 devices. It sends targeted association requests to discover device IEEE addresses, PAN IDs, and capabilities, making it essential for reconnaissance in wireless IoT security assessments.

## Description

KillerBee is a Python-based framework for testing the security of ZigBee and IEEE 802.15.4 networks. The zbid tool specifically focuses on device identification by interacting with coordinators, routers, and end-devices. With a compatible radio interface like the Atmel RZUSBStick, zbid enables eavesdropping, active probing, and network mapping. It supports channel scanning, association frame analysis, and basic fuzzing primitives, allowing security researchers to explore vulnerabilities in smart home, industrial control, and other ZigBee deployments.

## Features

- Device identification via association requests
- Channel-specific scanning (11-26)
- Passive sniffing of association frames
- Support for multiple radio interfaces
- Integration with other KillerBee tools for replay and fuzzing

## Installation

### Requirements

- Python 2.7 or 3.x
- Compatible IEEE 802.15.4 radio (e.g., Atmel RZUSBStick, TI CC2420 USB dongle)
- Linux kernel with USB serial support

### Install Commands

```bash
# Clone the KillerBee repository
git clone https://github.com/riverloopsec/killerbee.git
cd killerbee

# Install dependencies (Python 2/3)
pip install -r requirements.txt

# For RZUSBStick, ensure firmware is loaded
# (Refer to KillerBee docs for radio-specific setup)
```

Kali Linux often has KillerBee pre-installed or available via apt: `apt install killerbee`

## Basic Usage

```bash
tool-name --help
```

zbid requires root privileges for radio access and is invoked as `python zbid.py`.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -i, --interface | Specify radio interface |
| -c, --channel | Set ZigBee channel |
| -d, --dest | Target short address for directed probes |

## Examples

### Example 1: Basic Usage

```python
python zbid.py -i /dev/ttyUSB0 -c 11
```

This scans channel 11 for devices and outputs identification details.

### Example 2: Advanced Usage

```python
python zbid.py -i /dev/ttyUSB0 -c 15 --sniff -o associations.log
```

This passively sniffs associations on channel 15 and logs to file.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning
- [[Network Service Scanning]] Network Service Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual USB device attachments (e.g., RZUSBStick VID/PID)
- High volume of IEEE 802.15.4 frames on monitored channels
- Python processes with killerbee/zbid.py signatures in logs
- Network anomalies in ZigBee spectrum (using tools like Wireshark with ZigBee dissectors)

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
- [[tools/Wireshark]]
- [[Scapy]]

## References

- Official GitHub: https://github.com/riverloopsec/killerbee
- Documentation: https://killerbee.readthedocs.io/
- Related resources: ZigBee security papers and IEEE 802.15.4 specs
