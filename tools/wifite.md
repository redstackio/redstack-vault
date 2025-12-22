---
id: 4ad1b30d-8a82-4f6f-9a03-edd449fe052e
type: tool
verified: true
created_at: '2019-08-28T21:17:40.462055+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - wireless
  - auditing
  - wpa
  - wep
  - wps
  - cracking
url: 'https://github.com/derv82/wifite2'
validated: true
---

# wifite

**Status**: Unverified

## Overview

Wifite is an automated wireless auditing tool designed to attack multiple WEP, WPA, and WPS encrypted networks sequentially. It prioritizes targets by signal strength for efficiency and supports customizable automation, making it ideal for penetration testing and red team wireless assessments.

## Description

Wifite automates the process of scanning, deauthenticating clients, capturing handshakes or WEP IVs, and cracking passwords for wireless networks. It integrates with tools like aircrack-ng suite, reaver, and bully for comprehensive coverage. Key use cases include auditing enterprise Wi-Fi security, identifying weak encryption, and demonstrating wireless vulnerabilities in controlled environments.

## Features

- Sorts targets by signal strength (in dB) and attacks closest access points first
- Automatically de-authenticates clients of hidden networks to reveal SSIDs
- Numerous filters to specify targets (e.g., WEP/WPA/both, signal strength thresholds, specific channels)
- Customizable settings (e.g., timeouts, deauth packets per second)
- "Anonymous" mode: Randomizes MAC address before attacks and restores it afterward
- Backs up all captured WPA handshakes to the current directory
- Smart de-authentication: Cycles between individual clients and broadcast deauths
- Interruptible attacks: Ctrl+C options to continue, skip to next target, jump to cracking, or exit
- Session summary on exit, displaying cracked keys
- Saves all passwords to cracked.txt

## Installation

### Requirements

- Linux system with wireless card supporting monitor mode (e.g., Atheros AR9271)
- aircrack-ng suite, reaver, bully, cowpatty (for cracking)
- Python 3

### Install Commands

```bash
# On Kali Linux (pre-installed)
sudo apt update && sudo apt install wifite

# On Ubuntu/Debian from source
git clone https://github.com/derv82/wifite2.git
cd wifite2
sudo python setup.py install

# Verify installation
wifite --help
```

## Basic Usage

```bash
wifite --help
```

Displays all available options, including filters and attack modes.

### Common Options

| Option | Description |
|--------|-------------|
| -i, --if | Specify wireless interface |
| --wpa | Target only WPA/WPA2 networks |
| --wep | Target only WEP networks |
| --wps | Target only WPS-enabled networks |
| --kill | Kill conflicting processes (aircrack-ng, etc.) |
| --verbose, -v | Increase verbosity |
| --quiet, -q | Suppress output |
| --anonymous | Randomize MAC address |
| --crack | Attempt to crack captured handshakes |

## Examples

### Example 1: Basic Usage

```bash
wifite
```

Automatically scans all interfaces, kills conflicts, and attacks all detected networks by signal strength.

### Example 2: Advanced Usage

```bash
wifite -i wlan0 --wpa --crack --dict /usr/share/wordlists/rockyou.txt
```

Uses wlan0, targets WPA only, captures handshakes, and cracks with a wordlist.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Vulnerability Scanning]] Wireless Scanning
- [[Steal Web Session Cookie]] Steal Web Session Cookie (adapted for wireless credential theft)

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor mode enabled on wireless interfaces (iwconfig shows 'Mode:Monitor')
- High volume of deauthentication packets (Wireshark filter: wlan.fc.type_subtype == 0x0c)
- Processes like aircrack-ng, aireplay-ng running alongside wifite.py
- Unusual MAC address changes or randomized OUI
- Captured .cap files in /root or working directory
- Network logs showing repeated deauths from a single source

## Related Procedures

No related procedures documented yet.

## Related Tools

- [[tools/aircrack-ng]]
- [[tools/reaver]]

## References

- Official GitHub: https://github.com/derv82/wifite2
- Kali Tools Documentation: https://www.kali.org/tools/wifite/
