---
id: 7ff3d3bc-f689-4e2d-aa6e-814193630200
name: airtun-ng
type: tool
verified: true
created_at: '2019-08-28T21:17:25.791865+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - wireless
  - aircrack-ng
  - tunnel
  - injection
  - wids
url: 'https://www.aircrack-ng.org/doku.php?id=airtun-ng'
commands:
  - '[[commands/airtun-ng-create-tunnel-wep]]'
  - '[[commands/airtun-ng-create-tunnel-wpa]]'
validated: true
---

# airtun-ng

**Status**: Unverified

## Overview

Airtun-ng is a utility within the Aircrack-ng suite designed to create virtual tunnel interfaces. It enables monitoring of encrypted wireless traffic for wireless Intrusion Detection System (wIDS) purposes or the injection of arbitrary traffic into a wireless network. This tool is particularly useful in wireless penetration testing scenarios where direct interaction with encrypted networks is required.

## Description

Airtun-ng bridges monitor-mode wireless interfaces with standard network interfaces by creating a TUN/TAP virtual device. This allows tools like tcpdump or other Aircrack-ng components to process or inject traffic as if it were on a wired connection. For monitoring, it decrypts traffic using provided keys, making it suitable for wIDS data gathering. For injection, it facilitates sending crafted packets into the target network. Usage requires prior knowledge of the target's encryption key (WEP or WPA passphrase) and BSSID/ESSID. It is commonly used in environments with compatible wireless hardware supporting monitor mode.

## Features

- Virtual tunnel creation for WEP and WPA-encrypted networks
- Decryption of monitored traffic for analysis
- Support for packet injection into wireless networks
- Integration with other Aircrack-ng tools like airodump-ng and aireplay-ng
- Compatible with TUN/TAP kernel modules for seamless bridging

## Installation

### Requirements

- Linux system with wireless card supporting monitor mode (e.g., Atheros or Ralink chipsets)
- Kernel support for TUN/TAP devices (enabled by default in most distributions)
- Aircrack-ng suite dependencies (libpcap, etc.)

### Install Commands

```bash
# On Kali Linux (pre-installed)
# No action needed

# On Ubuntu/Debian
sudo apt update
sudo apt install aircrack-ng

# Verify installation
airtun-ng --help
```

## Basic Usage

```bash
airtun-ng --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -i, --interface | Specify the monitor-mode interface (e.g., wlan0mon) |
| -e, --essid | Target network ESSID |
| -p, --passphrase | WPA passphrase for decryption/injection |
| -k, --key | WEP key in ASCII or hex format |
| -a, --bssid | Target BSSID (MAC address) |
| -d, --driver | Specify wireless driver if needed |

## Examples

### Example 1: Basic Usage

Create a tunnel for a WEP network (detailed in related commands).

### Example 2: Advanced Usage

```bash
airtun-ng -i wlan0mon -e "MyNetwork" -p "mypassword" -a AA:BB:CC:DD:EE:FF
```
This sets up a WPA tunnel with specified BSSID for injection or monitoring.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Vulnerability Scanning]] Wireless Scanning (for reconnaissance via monitoring)
- [[Exploitation of Remote Services]] Exploitation of Remote Services (for packet injection into wireless services)

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of unexpected TUN/TAP interfaces (e.g., via `ip link show` or `ifconfig`)
- Unusual wireless monitor mode activity on network interfaces
- Decrypted traffic anomalies in wIDS logs
- Process monitoring for airtun-ng execution in wireless pentest environments
- Kernel logs showing TUN device creation

## Related Commands

- [[commands/airtun-ng-create-tunnel-wep]]
- [[commands/airtun-ng-create-tunnel-wpa]]

## References

- Official Aircrack-ng Documentation: https://www.aircrack-ng.org/
- Man page: `man airtun-ng`
