---
id: f100aaf8-85c5-4a7b-9b46-e4a6505ccd71
type: tool
verified: true
description: >-
  Aircrack-ng is a suite of tools for assessing WiFi network security, including
  packet capture, injection, and key cracking for WEP and WPA-PSK protocols.
url: 'https://www.aircrack-ng.org/'
tags:
  - wireless
  - cracking
  - wep
  - wpa
  - penetration-testing
platforms:
  - Linux
commands:
  - '[[commands/airodump-ng-monitor-mode-capture]]'
  - '[[commands/aireplay-ng-deauthentication-attack]]'
  - '[[commands/aircrack-ng-crack-wep-key]]'
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
validated: true
---

# aircrack-ng

**Status**: Unverified

## Overview

Aircrack-ng is a powerful suite of tools designed for wireless network auditing and security assessment. It is primarily used in penetration testing to capture WiFi packets, perform traffic injection, and crack encryption keys for WEP and WPA-PSK networks. Common use cases include identifying weak wireless configurations, testing network resilience against attacks, and educational purposes in cybersecurity training.

## Description

The aircrack-ng suite includes multiple utilities that work together to perform 802.11 protocol attacks. It recovers WEP keys using the FMS attack with optimizations like KoreK and PTW, making it significantly faster than earlier tools. For WPA-PSK, it supports dictionary-based cracking of captured handshakes. The suite requires a compatible wireless adapter that supports monitor mode and packet injection. It is widely used in red team operations for lateral movement via wireless networks or reconnaissance of target environments with WiFi infrastructure.

## Features

- **Packet Capture**: Tools like airodump-ng for monitoring and capturing wireless traffic in real-time.
- **Packet Injection**: Aireplay-ng for forging packets, including deauthentication attacks to force reconnections.
- **Key Cracking**: Aircrack-ng core for statistical attacks on WEP and dictionary attacks on WPA handshakes.
- **IVs Analysis**: Tools to test and replay initialization vectors for WEP vulnerabilities.
- **Cross-Platform Support**: Primarily Linux, but adaptable to other Unix-like systems with compatible hardware.

## Installation

### Requirements

- Compatible wireless network adapter (e.g., Atheros AR9271, Ralink RT3070) supporting monitor mode and injection.
- Linux kernel with wireless extensions.
- Root privileges for interface manipulation.

### Install Commands

```bash
# On Kali Linux (pre-installed)
# No action needed

# On Ubuntu/Debian
sudo apt update
sudo apt install aircrack-ng

# On macOS (via Homebrew, limited functionality)
brew install aircrack-ng

# From source (advanced)
git clone https://github.com/aircrack-ng/aircrack-ng.git
cd aircrack-ng
make
sudo make install
```

## Basic Usage

```bash
aircrack-ng --help
```

This displays the help for the main aircrack-ng tool. For suite-specific help, use individual tool names (e.g., `airodump-ng --help`).

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message for the tool |
| `-v, --verbose` | Increase verbosity level for detailed output |
| `--bssid` | Specify target BSSID (MAC address) |
| `-w` | Output file prefix for captures |

## Examples

### Example 1: Basic Usage

Refer to specific commands for detailed examples:
- Capture packets: [[commands/airodump-ng-monitor-mode-capture]]
- Perform deauth: [[commands/aireplay-ng-deauthentication-attack]]
- Crack keys: [[commands/aircrack-ng-crack-wep-key]]

### Example 2: Advanced Usage

Combine tools in a workflow: First capture with airodump-ng, inject with aireplay-ng, then crack with aircrack-ng.

```bash
# Enable monitor mode (using airmon-ng)
airmon-ng start wlan0

# Capture (see linked command)
airodump-ng -w capture mon0

# Deauth (see linked command)
aireplay-ng -0 5 -a BSSID mon0

# Crack (see linked command)
aircrack-ng -w wordlist capture.cap
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Vulnerability Scanning]] Wireless Scanning (Reconnaissance via packet capture)
- [[Password Guessing]] Password Guessing (Brute force for WPA-PSK handshakes)
- [[Archive via Utility]] Archive Collected Data: Archive via Utility (Packet capture files)

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual wireless interface modes (monitor mode via `iwconfig` or `airmon-ng`).
- High volume of deauthentication packets or injection traffic on the network (use Wireshark or IDS like Snort).
- Suspicious processes like `airodump-ng`, `aireplay-ng` in process lists (`ps aux | grep air`).
- Monitor for .cap files or temporary files in /tmp with wireless packet data.
- Wireless IDS alerts for rogue AP scanning or injection attempts.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Wireshark]] (for packet analysis)
- [[tools/kismet]] (alternative wireless sniffer)
- [[tools/Hashcat]] (for advanced cracking)

## References

- Official website: https://www.aircrack-ng.org/
- GitHub repository: https://github.com/aircrack-ng/aircrack-ng
- Documentation: https://www.aircrack-ng.org/doku.php
- Kali Linux tools page: https://www.kali.org/tools/aircrack-ng/
