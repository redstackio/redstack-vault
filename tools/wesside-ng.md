---
id: dd85105f-be5b-4be2-8ca4-4456129ece78
name: wesside-ng
type: tool
verified: true
created_at: '2019-08-28T21:17:33.046352+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
tags:
  - wireless
  - wep
  - cracking
  - penetration-testing
  - aircrack-ng
url: 'https://www.aircrack-ng.org/doku.php?id=wesside-ng'
commands:
  - '[[commands/wesside-ng-basic-initialization]]'
  - '[[commands/wesside-ng-specified-channel-start]]'
  - '[[commands/wesside-ng-essid-targeted-attack]]'
validated: true
---

# wesside-ng

**Status**: Unverified

## Overview

wesside-ng is an automated tool designed for wireless penetration testing, specifically to crack WEP keys from 802.11 networks. It automates the entire process, making it suitable for red team exercises targeting legacy wireless security.

## Description

wesside-ng integrates multiple techniques to obtain WEP keys efficiently. It begins by identifying target access points, associates with the network, captures pseudo-random generation algorithm (PRGA) XOR data from packets, determines the network's IP addressing scheme, reinjects ARP requests to generate traffic, and finally computes the WEP key. The tool operates with minimal user input, ideal for scenarios where manual packet manipulation is impractical. It is part of the aircrack-ng suite and requires a compatible wireless adapter in monitor mode.

## Features

- Automatic detection and selection of target wireless networks
- Seamless association and deauthentication handling
- PRGA XOR data collection for keystream analysis
- ARP request reinjection to accelerate traffic generation
- Fully automated WEP key extraction and display
- Support for interactive mode to monitor progress

## Installation

### Requirements

- Linux kernel with wireless extensions
- Compatible wireless card supporting monitor mode (e.g., Atheros AR9271)
- aircrack-ng suite dependencies (libpcap, libssl)

### Install Commands

```bash
# On Kali Linux (pre-installed as part of aircrack-ng)
# No action needed

# On Ubuntu/Debian
sudo apt update
sudo apt install aircrack-ng

# Verify installation
wesside-ng --help
```

## Basic Usage

```bash
wesside-ng --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-i, --iface <interface>` | Specify the wireless interface (e.g., wlan0) |
| `-c, --chan <channel>` | Target specific channel (1-14) |
| `-e, --essid <essid>` | Target specific ESSID |
| `-f, --file <file>` | Read/write from/to a capture file |
| `-v, --verbose` | Increase verbosity for debugging |

## Examples

### Example 1: Basic Usage

Start wesside-ng to automatically detect and attack nearby WEP networks using the default interface.

```bash
wesside-ng
```

### Example 2: Advanced Usage

Target a specific network on channel 11 with verbose output.

```bash
wesside-ng -i mon0 -c 11 -v
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning (wireless network discovery and probing)
- [[Unsecured Credentials]] Unsecured Credentials (extracting WEP keys from weak encryption)

### Tactics

- [[Reconnaissance]] Reconnaissance (network scanning)
- [[Initial Access]] Initial Access (gaining wireless network entry)

## Detection

Indicators and methods for detecting this tool's usage:

- Wireless adapter switching to monitor mode (e.g., via iwconfig or airmon-ng)
- Deauthentication floods or unusual probe requests in wireless traffic
- High volume of reinjected ARP packets on the target network
- Packet captures showing PRGA XOR collection patterns
- Process monitoring for wesside-ng or aircrack-ng binaries

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/aircrack-ng]] (companion suite for cracking)
- [[tools/aireplay-ng]] (packet injection and deauth)
- [[tools/airodump-ng]] (network scanning)

## References

- Official aircrack-ng documentation: https://www.aircrack-ng.org/
- wesside-ng specific guide: https://www.aircrack-ng.org/doku.php?id=wesside-ng
