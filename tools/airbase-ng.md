---
id: 8c459db6-e9dc-4437-a3dc-2ea4bdde0cb8
type: tool
verified: true
created_at: '2019-08-28T21:17:42.068113Z'
updated_at: '2023-05-29T16:48:53.029709Z'
platforms:
  - Linux
tags:
  - wireless
  - wep
  - wpa
  - cracking
  - rogue-ap
url: 'https://www.aircrack-ng.org/doku.php?id=airbase-ng'
commands:
  - '[[commands/airbase-ng-caffe-latte-attack]]'
  - '[[commands/airbase-ng-hirte-wep-client-attack]]'
  - '[[commands/airbase-ng-wpa-handshake-capture]]'
validated: true
---

# airbase-ng

**Status**: Unverified

## Overview

airbase-ng is a multi-purpose tool from the aircrack-ng suite designed for attacking wireless clients rather than access points directly. It is commonly used in wireless penetration testing to implement client-side attacks like the Caffe Latte and Hirte WEP attacks, capture WPA/WPA2 handshakes, and set up rogue access points for man-in-the-middle scenarios.

## Description

airbase-ng focuses on client-targeted wireless attacks, enabling testers to generate traffic, deauthenticate clients, and create fake APs to capture encryption keys or credentials. It supports WEP cracking via client-induced packet generation and WPA handshake interception through forced disassociations. The tool requires a wireless card capable of monitor mode and packet injection.

## Features

- Implements the Caffe Latte WEP client attack to recover keys from associated clients
- Supports the Hirte WEP client attack for targeting disconnected clients
- Captures WPA/WPA2 4-way handshakes by acting as a rogue AP
- Functions as an ad-hoc or full access point
- Filters traffic by SSID or client MAC addresses
- Manipulates and resends captured packets
- Encrypts outgoing packets and decrypts incoming ones

## Installation

### Requirements

- Linux kernel with wireless extensions
- Wireless card supporting monitor mode (e.g., Atheros AR9271)
- aircrack-ng suite dependencies (libpcap, libssl)

### Install Commands

```bash
# On Kali Linux (pre-installed)
sudo apt update && sudo apt install aircrack-ng

# On Ubuntu
sudo apt update && sudo apt install aircrack-ng

# From source
git clone https://github.com/aircrack-ng/aircrack-ng
git checkout latest-stable
make && sudo make install
```

## Basic Usage

```bash
airbase-ng --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -I <ifname> | Capture interface name |
| -c <channel> | Set channel |
| -e <essid> | Set ESSID for rogue AP |
| -v <level> | Verbosity level (1-4) |

## Examples

### Example 1: Basic Usage

Set up a simple rogue AP:

```bash
airbase-ng -c 6 -e "TestAP" wlan0mon
```

### Example 2: Advanced Usage

Perform a client attack with filtering:

```bash
airbase-ng -c 11 -e "TargetNet" -C AA:BB:CC:DD:EE:FF wlan0mon
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Container API]] Wireless Credentials
- [[Steal Web Session Cookie]] Steal Web Session Cookie (adapted for wireless sessions)

### Tactics

- [[Initial Access]] Initial Access
- [[Persistence]] Persistence

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual rogue SSIDs appearing in wireless scans
- High volume of deauthentication frames in packet captures (using tools like Wireshark)
- Monitor mode interfaces on suspicious systems (e.g., via `iwconfig` or `airmon-ng` traces)
- Traffic anomalies like forged probe responses or excessive disassociations

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

- Official documentation: https://www.aircrack-ng.org/doku.php?id=airbase-ng
- Aircrack-ng GitHub: https://github.com/aircrack-ng/aircrack-ng
