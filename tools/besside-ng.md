---
id: 9d9f9097-aff4-44ef-b8df-2131bb7bfb0c
type: tool
verified: true
created_at: '2019-08-28T21:17:24.776660+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - wireless
  - wep
  - wpa
  - cracking
  - aircrack-ng
url: 'https://www.aircrack-ng.org/doku.php?id=besside-ng'
commands:
  - '[[commands/besside-ng-basic-wep-crack]]'
  - '[[commands/besside-ng-wpa-handshake-capture]]'
validated: true
---

# besside-ng

**Status**: Unverified

## Overview

besside-ng is a wireless network auditing tool from the aircrack-ng suite, designed for automated WEP key cracking and WPA/WPA2 handshake capture. It is commonly used in penetration testing to assess the security of wireless networks by exploiting weak encryption protocols like WEP or capturing authentication handshakes for offline analysis.

## Description

besside-ng automates the process of capturing traffic on wireless interfaces in monitor mode. For WEP networks, it performs ARP replay attacks and keystream analysis to recover encryption keys quickly. For WPA networks, it logs 4-way handshakes triggered by deauthentication packets, which can later be cracked using dictionary or brute-force methods with tools like aircrack-ng or hashcat. It supports multi-channel scanning and threading for efficiency, making it suitable for red team operations targeting enterprise or home Wi-Fi environments.

## Features

- Feature 1: Automatic WEP cracking via packet injection and PTW attack method.
- Feature 2: WPA handshake capture with targeted deauthentication.
- Feature 3: Multi-threaded operation for concurrent network monitoring and attack execution.
- Feature 4: Support for channel hopping and ESSID filtering.

## Installation

### Requirements

- Linux kernel with wireless extensions.
- Compatible wireless chipset supporting monitor mode (e.g., Atheros, Ralink).
- aircrack-ng suite dependencies (libpcap, libssl).

### Install Commands

```bash
# On Kali Linux (pre-installed)
sudo apt update && sudo apt install aircrack-ng

# On Ubuntu
sudo apt update && sudo apt install aircrack-ng

# From source
wget https://download.aircrack-ng.org/aircrack-ng-1.7.tar.gz
tar -xzf aircrack-ng-1.7.tar.gz
cd aircrack-ng-1.7
make && sudo make install
```

## Basic Usage

```bash
besside-ng --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -v, --verbose | Increase verbosity level (1-3) |
| -c <channel> | Lock to specific channel |
| -f <file> | Output file for captures |
| -W <file> | WPA-specific output file |
| -s <ssid> | Filter by ESSID |

## Examples

### Example 1: Basic Usage

```bash
besside-ng -c 6 -f capture.cap wlan0mon
```

### Example 2: Advanced Usage

```bash
besside-ng -c 11 -f all.cap -W wpa.cap -v 2 -s TargetSSID wlan0mon
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Vulnerability Scanning]] Wireless Scanning
- [[Forge Web Credentials]] Forge Web Credentials (for handshake capture leading to credential attacks)

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual deauthentication packets in wireless traffic (using Wireshark or Kismet).
- Detection method 2: Monitor mode interface activation on suspicious devices (e.g., via `iwconfig` or `airmon-ng` traces).
- Detection method 3: High volume of ARP replay or probe requests on monitored channels.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/aircrack-ng]]
- [[tools/aireplay-ng]]
- [[tools/airodump-ng]]

## References

- Official documentation: https://www.aircrack-ng.org/doku.php?id=besside-ng
- Aircrack-ng GitHub: https://github.com/aircrack-ng/aircrack-ng
