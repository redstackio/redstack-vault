---
id: 18219876-17bf-40d5-9b40-371787a089ae
type: tool
verified: true
created_at: '2019-08-28T21:17:32.994122+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - wireless
  - wps
  - brute-force
  - wpa-cracking
url: 'http://www.reaver-wps-fork-t6x.org/'
validated: true
---

# Reaver

**Status**: Unverified

## Overview

Reaver is a tool designed for brute-force attacks against WiFi Protected Setup (WPS) registrar PINs to recover WPA/WPA2 passphrases. It targets vulnerabilities in WPS implementations on access points, allowing recovery of the pre-shared key (PSK) without directly cracking the WPA handshake. Commonly used in wireless penetration testing for assessing WPS security.

## Description

Reaver performs automated brute-force attempts on the 8-digit WPS PIN, exploiting the offline verification aspect of WPS protocols. It sends crafted authentication requests to the access point and analyzes responses to narrow down the PIN. The tool is robust against various access points and WPS versions, with an average recovery time of 4-10 hours, though it can be faster depending on the target's lockout policies and signal strength. It requires a compatible wireless interface in monitor mode and is often paired with tools like wash for target discovery.

## Features

- Automated PIN brute-force with progress tracking
- Support for session resumption to continue interrupted attacks
- Verbose logging and delay options to evade rate limiting
- Integration with external tools for channel hopping and deauthentication
- PIN validation and passphrase extraction upon success

## Installation

### Requirements

- Linux kernel with wireless extensions
- Compatible wireless chipset (e.g., Atheros AR9271, Ralink RT3070)
- Aircrack-ng suite for monitor mode setup

### Install Commands

```bash
# On Kali Linux (pre-installed)
sudo apt update && sudo apt install reaver

# On Ubuntu
sudo apt update && sudo apt install reaver

# From source (if needed)
git clone https://github.com/t6x/reaver-wps-fork-t6x.git
cd reaver-wps-fork-t6x
./configure && make && sudo make install
```

## Basic Usage

```bash
reaver --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-i, --interface=IFACE` | Wireless interface in monitor mode |
| `-b, --bssid=ADDR` | Target access point BSSID |
| `-c, --channel=NUM` | WiFi channel of the target |
| `-v, --verbose` | Increase verbosity level (up to 9) |
| `-s, --session=FILE` | Session file for resuming attacks |
| `-d, --delay=SEC` | Delay between PIN attempts in seconds |
| `-K, --pixie-dust` | Attempt Pixie Dust attack (offline WPS crack) |
| `-L, --lock-delay=SEC` | Delay after WPS lockout |

## Examples

### Example 1: Basic Usage

Initiate a WPS PIN brute-force attack on a target AP.

```bash
reaver -i mon0 -b 00:11:22:33:44:55 -c 6 -vv
```

### Example 2: Advanced Usage

Resume a previous session with delay to avoid lockouts.

```bash
reaver -i mon0 -b 00:11:22:33:44:55 -c 6 -s session.wps -d 5 -vv
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning (for wireless discovery)
- [[Credentials in Files]] Hardware Keylogger (WPS PIN brute-force as credential access)

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual deauthentication frames or probe requests on monitored networks
- High volume of WPS association requests from a single MAC address
- Wireless interface in promiscuous/monitor mode (via netlink or procfs)
- Log entries for WPS PIN attempts in AP firmware logs
- Tools like Wireshark for capturing EAPOL/WPS exchanges

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
- [[tools/wash]]
- [[tools/bully]]

## References

- Official GitHub: https://github.com/t6x/reaver-wps-fork-t6x
- Original Paper: WPS PIN Brute Force Vulnerability (Dominik Bongartz)
- Kali Tools Documentation: https://www.kali.org/tools/reaver/
