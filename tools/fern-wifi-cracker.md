---
id: 66fc66de-8a7f-4094-a161-16829f4726e3
type: tool
verified: true
created_at: '2019-08-28T21:17:21.953910+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - wireless
  - cracking
  - wep
  - wpa
  - wps
  - auditing
url: 'https://github.com/savio-code/fern-wifi-cracker'
validated: true
---

# fern-wifi-cracker

**Status**: Unverified

## Overview

Fern Wifi Cracker is a Python-based GUI tool for wireless security auditing and attack simulations. It enables penetration testers to assess the security of WEP, WPA, and WPS-secured networks by cracking keys and performing related network attacks. Commonly used in red team exercises for wireless reconnaissance and exploitation.

## Description

Developed using Python and the Qt GUI library, Fern Wifi Cracker provides an intuitive interface for launching wireless attacks. It supports key recovery for vulnerable wireless protocols and includes features for session hijacking, MAC spoofing, and MITM attacks. The tool automates complex wireless operations, making it accessible for auditing Wi-Fi networks in controlled environments. It requires a compatible wireless adapter supporting monitor mode and packet injection.

## Features

- Feature 1: WEP cracking using fragmentation, chop-chop, caffe-latte, hirte, ARP replay, or WPS attacks.
- Feature 2: WPA/WPA2 cracking via dictionary attacks or WPS PIN brute-forcing.
- Feature 3: Automatic key storage in a local database upon successful cracks.
- Feature 4: Automated attack system targeting access points.
- Feature 5: Session hijacking in passive and Ethernet modes.
- Feature 6: Geo-location tracking of access point MAC addresses.
- Feature 7: Built-in MITM engine for traffic interception.
- Feature 8: Bruteforce attacks against HTTP, HTTPS, TELNET, and FTP services.
- Feature 9: Integrated update support for maintaining the latest version.

## Installation

### Requirements

- Compatible wireless adapter (e.g., Alfa AWUS036N) supporting monitor mode.
- Python 2/3 and Qt libraries.
- Root access for interface management.
- Debian-based Linux distribution (e.g., Kali Linux).

### Install Commands

```bash
sudo apt update
sudo apt install fern-wifi-cracker
```

On Kali Linux, the tool is often pre-installed or available via the repositories. For source installation:

```bash
git clone https://github.com/savio-code/fern-wifi-cracker.git
cd fern-wifi-cracker
sudo python setup.py install
```

## Basic Usage

```bash
tool-name --help
```

Launch the GUI with:

```bash
sudo fern-wifi-cracker
```

Select a wireless interface, enable monitor mode, scan for networks, and choose attack methods from the interface.

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and available options |
| `--monitor` | Automatically set the interface to monitor mode (if supported) |
| `-i, --interface` | Specify the wireless interface (e.g., wlan0) |

## Examples

### Example 1: Basic Usage

```bash
sudo fern-wifi-cracker
```

Opens the GUI; scan for nearby networks and select a target for WEP cracking.

### Example 2: Advanced Usage

```bash
sudo fern-wifi-cracker -i wlan0
```

Launches with a specific interface pre-selected for auditing.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Vulnerability Scanning]] Wireless Sniffing (for network scanning and capture)
- [[Password Guessing]] Password Guessing (for dictionary-based WPA cracking)
- [[Credentials in Files]] Password Policy Discovery (WPS PIN enumeration)

### Tactics

- [[Reconnaissance]] Reconnaissance (scanning wireless networks)
- [[Initial Access]] Initial Access (cracking wireless credentials for network entry)

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Wireless interface in monitor mode (e.g., via `iwconfig` showing "Mode:Monitor").
- Detection method 2: Unusual deauthentication floods or ARP replay traffic in wireless captures.
- Detection method 3: Process monitoring for `fern-wifi-cracker` or Python Qt processes with high CPU during cracking.
- Detection method 4: Database files created by Fern (e.g., FernDB) containing cracked keys.

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
- [[tools/reaver]]

## References

- Official GitHub: https://github.com/savio-code/fern-wifi-cracker
- Kali Tools Documentation: https://www.kali.org/tools/fern-wifi-cracker
