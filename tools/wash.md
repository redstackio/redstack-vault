---
id: 7af812ae-89cd-40a3-8cb6-789fe09eb290
type: tool
verified: true
created_at: '2019-08-28T21:17:34.186289+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - wireless
  - wps
  - pixie-dust
  - reaver-fork
url: 'https://github.com/t6x/reaver-wps-fork-t6x'
validated: true
---

# wash

**Status**: Unverified

## Overview

Wash is a command-line tool designed for wireless security auditing, specifically targeting Wi-Fi Protected Setup (WPS)-enabled access points. It scans for WPS APs and implements the Pixie Dust attack, which exploits a flaw in the WPS PIN generation algorithm to recover the PIN offline rapidly (often in under a minute) on vulnerable devices. This allows derivation of the WPA/WPA2 passphrase without lengthy brute-force attempts. Wash is commonly used in penetration testing for assessing wireless network security.

## Description

Wash is a fork/extension of Reaver, optimized for the Pixie Dust vulnerability discovered by Craig Heffner (t6x). It identifies WPS-enabled routers, checks for vulnerability to offline PIN recovery, and performs the attack. Unlike traditional brute-force tools, Pixie Dust leverages weak random number generation in some chipsets (e.g., Broadcom, Ralink) to guess the PIN quickly. It supports both 2.4GHz and 5GHz bands and provides detailed AP information like vendor, model, and WPS lock status. Wash is particularly effective against older or misconfigured enterprise and home routers.

## Features

- Feature 1: WPS AP discovery via passive scanning of beacons and probes.
- Feature 2: Pixie Dust offline PIN recovery for vulnerable implementations.
- Feature 3: Detailed output including signal strength, encryption, and device fingerprints.
- Feature 4: Support for monitor mode interfaces and channel hopping.
- Feature 5: Integration with tools like Reaver for follow-on brute-force if Pixie Dust fails.

## Installation

### Requirements

- Linux kernel with wireless extensions.
- Wireless adapter supporting monitor mode (e.g., Alfa AWUS036N).
- Dependencies: libpcap, libsqlite3 (for some forks).

### Install Commands

```bash
# On Kali Linux (pre-installed in many distributions)
sudo apt update
sudo apt install wash

# From source (t6x fork)
git clone https://github.com/t6x/reaver-wps-fork-t6x.git
cd reaver-wps-fork-t6x/src
./configure
make
sudo make install
```

## Basic Usage

```bash
wash --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -i, --interface | Specify the wireless interface |
| -b, --bssid | Target a specific AP by BSSID |
| -C | Skip WPS checksum validation |
| -5 | Scan/use 5GHz band |
| -o, --output | Save scan results to file |

## Examples

### Example 1: Basic Usage

Scan for WPS APs:

```bash
wash -i wlan0mon
```

### Example 2: Advanced Usage

Target specific AP and attempt Pixie Dust:

```bash
wash -i wlan0mon -b AA:BB:CC:DD:EE:FF
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Vulnerability Scanning]] Scan Network (Wireless Scanning)
- [[Forge Web Credentials]] Forge Web Credentials (WPS PIN Recovery)

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for high-volume probe requests or deauth frames on wireless networks.
- Detection method 2: Log WPS registrar interactions or PIN attempts on AP firmware.
- Detection method 3: Network IDS signatures for Pixie Dust packet patterns (e.g., specific EAPOL exchanges).
- Detection method 4: Enable WPS lockout after failed attempts and monitor for tool signatures like wash process on compromised hosts.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/reaver]] (Companion brute-force tool)
- [[tools/aircrack-ng]] (Wireless suite for monitor mode setup)
- [[tools/wifite]] (Automated wireless auditor that integrates wash)

## References

- Official GitHub: https://github.com/t6x/reaver-wps-fork-t6x
- Pixie Dust Paper: https://dl.aircrack-ng.org/breaking_wps.pdf
- Kali Tools Documentation: https://www.kali.org/tools/wash/
