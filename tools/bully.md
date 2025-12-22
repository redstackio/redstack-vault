---
id: 9a6244fb-cf9b-4b59-b4e8-36b95738d0e6
type: tool
verified: true
created_at: '2019-08-28T21:17:33.499397+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
tags:
  - wireless
  - wps
  - brute-force
  - wifi
url: 'https://github.com/aanarchyy/bully'
commands:
  - '[[commands/bully-wps-brute-force]]'
  - '[[commands/bully-wps-brute-force-with-dictionary]]'
validated: true
---

# Bully

**Status**: Unverified

## Overview

Bully is a command-line tool for performing brute-force attacks against Wi-Fi Protected Setup (WPS) PINs on vulnerable access points. It exploits the design flaw in the WPS protocol that allows PIN guessing, enabling unauthorized access to Wi-Fi networks. Commonly used in wireless penetration testing to assess WPS security.

## Description

Bully is a C-based implementation of WPS brute force attacks, offering improvements over tools like Reaver. It supports low-level Wi-Fi packet crafting and transmission using tools like libpcap and lorcon. Key advantages include reduced dependencies, better CPU and memory efficiency, proper endianness handling, and robust option sets. Designed for Linux, including embedded systems like OpenWrt, it works across architectures. Bully handles anomalous scenarios effectively and has been tested against various vendor access points.

## Features

- Brute-force WPS PIN recovery with online attacks
- Support for dictionary-based PIN lists
- Pixie Dust attack integration for faster vulnerable AP cracking
- Session resumption for interrupted attacks
- Verbose logging and progress tracking
- Compatible with monitor-mode wireless interfaces

## Installation

### Requirements

- Linux kernel with wireless support
- Monitor-mode capable Wi-Fi adapter (e.g., Atheros AR9271)
- libpcap and libsqlite3 development libraries

### Install Commands

```bash
# On Kali Linux (pre-installed in many distributions)
sudo apt update && sudo apt install bully

# On Ubuntu
sudo apt update && sudo apt install bully

# From source (GitHub)
git clone https://github.com/aanarchyy/bully.git
cd bully/src
make
sudo make install
```

## Basic Usage

```bash
bully --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and exit |
| `-v, --verbose` | Enable verbose output for debugging |
| `-B, --bssid` | Specify target BSSID (MAC address) |
| `-c, --channel` | Set Wi-Fi channel (1-14) |
| `-d, --dict` | Use PIN dictionary file |
| `-i, --iface` | Wireless interface in monitor mode |
| `-s, --session` | Resume from session file |
| `-P, --pin` | Test specific PIN |

## Examples

### Example 1: Basic Usage

Perform a standard WPS PIN brute-force attack on a target AP.

```bash
bully -b 00:11:22:33:44:55 -c 6 wlan0mon
```

### Example 2: Advanced Usage

Brute-force using a custom PIN dictionary and resume session.

```bash
bully -b 00:11:22:33:44:55 -c 6 -d pins.txt -s session.bully wlan0mon
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Password Guessing]] Password Guessing (brute-forcing WPS PINs)
- [[Vulnerability Scanning]] Scan for Network Services (wireless scanning)

### Tactics

- [[Initial Access]] Initial Access (gaining network access via WPS exploit)
- [[Discovery]] Discovery (identifying vulnerable wireless networks)

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual deauthentication or probe request floods on Wi-Fi channels
- High volume of WPS M1-M7 message exchanges
- Monitor-mode interface activity on penetration testing tools
- Log analysis for repeated WPS PIN attempts (e.g., via wpa_supplicant logs)
- Wireless IDS alerts for brute-force patterns

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/reaver]] (alternative WPS attack tool)
- [[tools/aircrack-ng]] (suite for wireless auditing)

## References

- Official GitHub: https://github.com/aanarchyy/bully
- WPS Vulnerability Details: https://www.wi-fi.org/discover-wi-fi/security
