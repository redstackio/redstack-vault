---
id: 8b9ed289-7826-4c0c-b675-4c4dc441ef1c
name: zbconvert
type: tool
verified: true
created_at: '2019-08-28T21:17:30.250139+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - zigbee
  - ieee802.15.4
  - wireless
  - conversion
url: 'https://github.com/riverloopsec/killerbee'
validated: true
---

# zbconvert

**Status**: Unverified

## Overview

zbconvert is a utility tool from the KillerBee framework designed for converting packet captures between different formats for ZigBee and IEEE 802.15.4 networks. It is particularly useful for analyzing, replaying, or transforming wireless protocol data during security assessments of IoT and embedded systems.

## Description

KillerBee is a Python-based framework for testing the security of ZigBee and IEEE 802.15.4 networks. zbconvert specifically handles format conversions, such as from PCAP (used by Wireshark) to text dumps or vice versa, enabling easier manipulation of frames for fuzzing, replay attacks, or detailed inspection. It requires a compatible radio interface like the Atmel RZUSBstick or similar for capture, but zbconvert itself operates on existing files.

## Features

- Feature 1: Convert PCAP to human-readable text for manual analysis
- Feature 2: Convert text dumps back to PCAP for replay with tools like zbreplay
- Feature 3: Filter conversions by frame type, channel, or other attributes
- Feature 4: Support for ZigBee-specific dissections and IEEE 802.15.4 headers

## Installation

### Requirements

- Python 2.7 or 3.x (KillerBee is Python-based)
- Scapy library (for packet handling)
- Compatible hardware for capture (e.g., RZUSBstick), though not required for conversion
- Linux environment recommended (Kali Linux has partial support)

### Install Commands

```bash
# Clone the KillerBee repository
git clone https://github.com/riverloopsec/killerbee.git
cd killerbee

# Install dependencies
pip install -r requirements.txt

# For Ubuntu/Debian (Kali)
sudo apt update
sudo apt install python3-scapy python3-usb

# Make tools executable
chmod +x tools/zb*
```

## Basic Usage

```bash
zbconvert --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -r, --read | Specify input file to read |
| -f, --format | Output format (text, pcap) |
| -w, --write | Output file path |
| --filter | Apply filters (e.g., type=beacon) |
| -h, --help | Show help message |

## Examples

### Example 1: Basic Usage

Convert a PCAP to text:

```bash
zbconvert -r capture.pcap -f text -w output.txt
```

### Example 2: Advanced Usage

Convert text to PCAP with channel filter:

```bash
zbconvert -r dump.txt -f pcap -w replay.pcap --channel 26
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Vulnerability Scanning]] Scan Network (Wireless Scanning for ZigBee networks)
- [[Stage Capabilities]] Stage Capabilities (Converting payloads for wireless exploitation)

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for KillerBee Python scripts in process lists (e.g., ps aux | grep zbconvert)
- Detection method 2: Network anomalies in 2.4GHz spectrum, especially IEEE 802.15.4 traffic
- Detection method 3: File system artifacts like .pcap files with ZigBee dissections or KillerBee logs

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

## References

- Official GitHub: https://github.com/riverloopsec/killerbee
- KillerBee Documentation: https://killerbee.readthedocs.io/
- ZigBee Security Testing Guide
