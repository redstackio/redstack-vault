---
id: c2a186c0-9f7c-4baf-a13f-5e8b3c64a73b
type: tool
verified: true
created_at: '2019-08-28T21:17:39.872445+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
tags:
  - wireless
  - monitor-mode
  - aircrack-ng
url: 'https://www.aircrack-ng.org/doku.php?id=airmon-ng'
validated: true
---

# airmon-ng

**Status**: Unverified

## Overview

airmon-ng is a utility from the aircrack-ng suite designed to enable and disable monitor mode on wireless network interfaces. Monitor mode allows capturing all wireless traffic on a channel, which is crucial for wireless security testing, packet injection, and attacks like deauthentication or WEP/WPA cracking. It can also revert interfaces back to managed mode after testing.

## Description

airmon-ng interacts with the wireless driver to switch interfaces into monitor mode, creating virtual monitor interfaces (e.g., mon0) for raw packet capture. It handles common issues like conflicting processes (e.g., NetworkManager) and supports chipsets like Atheros, Ralink, and Broadcom. Commonly used in offensive security for Wi-Fi reconnaissance and exploitation, but requires hardware support for monitor mode.

## Features

- Enable monitor mode on supported wireless interfaces
- Disable monitor mode and restore managed mode
- Detect and optionally kill interfering processes (e.g., dhclient, wpa_supplicant)
- Create virtual monitor interfaces for packet sniffing/injection
- Channel-specific monitor mode activation

## Installation

### Requirements

- Linux kernel with wireless extensions (most modern distributions)
- Wireless adapter supporting monitor mode (e.g., Alfa AWUS036N with Atheros chipset)
- Root privileges (sudo)

### Install Commands

```bash
# On Kali Linux (pre-installed)
# No action needed

# On Ubuntu/Debian
sudo apt update
sudo apt install aircrack-ng

# On Arch Linux
sudo pacman -S aircrack-ng

# Verify installation
airmon-ng --help
```

## Basic Usage

```bash
airmon-ng --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `check` | List interfering processes |
| `start` | Enable monitor mode |
| `stop` | Disable monitor mode |
| `-h, --help` | Show help message |
| `--info` | Display wireless interface information |

## Examples

### Example 1: Check for Interfering Processes

```bash
airmon-ng check wlan0
```

Use the related command: [[commands/airmon-ng-check-interfering-processes]]

### Example 2: Start Monitor Mode

First kill processes if needed:

```bash
airmon-ng check kill
```

Then start:

```bash
airmon-ng start wlan0
```

Use the related command: [[commands/airmon-ng-start-monitor-mode]]

### Example 3: Stop Monitor Mode

```bash
airmon-ng stop mon0
```

Use the related command: [[commands/airmon-ng-stop-monitor-mode]]

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Vulnerability Scanning]] Wireless Scanning
- [[Steal Web Session Cookie]] Steganography (for packet injection in wireless attacks)

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access (via wireless exploitation)

## Detection

- Monitor for interface name changes (e.g., wlan0 to mon0) using tools like `iwconfig` or `ip link`
- Detect process kills of NetworkManager or similar services
- Log unusual wireless driver interactions or module loads (e.g., mac80211)
- Endpoint detection rules for aircrack-ng binaries

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/airodump-ng]] (for packet capturing in monitor mode)
- [[tools/aireplay-ng]] (for packet injection)
- [[tools/aircrack-ng]] (for cracking)

## References

- Official Documentation: https://www.aircrack-ng.org/doku.php?id=airmon-ng
- Aircrack-ng Suite: https://www.aircrack-ng.org/
