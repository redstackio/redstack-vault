---
id: f7f8e0b6-76fd-4f39-972a-a16a97f719b1
type: tool
verified: true
created_at: '2019-08-28T21:17:29.172113+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - wireless
  - rogue-ap
  - wpa
  - phishing
  - exploitation
url: 'https://github.com/OpenSecurityTrainingInfoSec/hostapd-wpe'
commands:
  - '[[commands/hostapd-wpe-start-rogue-ap]]'
  - '[[commands/hostapd-wpe-debug-mode]]'
validated: true
---

# hostapd-wpe

**Status**: Unverified

## Overview

hostapd-wpe is a customized version of the hostapd daemon, enhanced with Wireless Pwnage Edition (WPE) patches. It is designed for creating rogue wireless access points (APs) to perform man-in-the-middle attacks, capture WPA/WPA2 handshakes, and phish enterprise credentials (e.g., via PEAP/MSCHAPv2). Commonly used in wireless penetration testing for evil twin attacks and credential harvesting.

## Description

This tool allows testers to emulate legitimate WiFi networks, luring clients to connect and revealing sensitive authentication data. It supports open, WPA-PSK, and WPA-Enterprise modes, logging captured hashes or plaintext credentials to files for offline cracking. Ideal for assessing WiFi security in red team engagements, but requires compatible wireless hardware (e.g., Atheros or Ralink chipsets in monitor mode).

## Features

- Rogue AP creation with customizable SSID, channel, and encryption
- Capture of WPA/WPA2-PSK handshakes in pcap format
- Enterprise credential phishing (EAP-PEAP, EAP-TTLS) with MSCHAPv2 hash extraction
- Integration with tools like aircrack-ng for deauth attacks
- Debug and daemon modes for flexible operation
- Logging of authentication events for analysis

## Installation

### Requirements

- Linux kernel with nl80211 support
- Compatible wireless adapter (e.g., Alfa AWUS036N)
- libnl, libssl, libpcap development libraries

### Install Commands

On Kali Linux (pre-built package):

```bash
sudo apt update
sudo apt install hostapd-wpe
```

From source (for custom builds):

```bash
sudo apt install git build-essential libnl-3-dev libnl-genl-3-dev libssl-dev pkg-config
wget https://w1.fi/releases/hostapd-wpe-2.9.tar.gz  # Or latest from repo
tar -xzf hostapd-wpe-2.9.tar.gz
cd hostapd-wpe-2.9/hostapd
cp defconfig .config
make
sudo make install
```

Verify installation:

```bash
hostapd-wpe -v
```

## Basic Usage

```bash
hostapd-wpe --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -B | Run in background (daemon) mode |
| -d | Enable debug/verbose output |
| -f | Log file path for output |
| -K | Include keys in debug logs (insecure, for testing only) |

## Examples

### Example 1: Basic Usage

Start a simple open rogue AP:

```bash
# First, configure interface
sudo ifconfig wlan0 up 0.0.0.0
sudo iwconfig wlan0 mode managed essid "FreeWiFi" channel 6

# Run with config
[[commands/hostapd-wpe-start-rogue-ap]]  # Using /etc/hostapd/open.conf
```

### Example 2: Advanced Usage

Enterprise phishing AP with debug:

```bash
[[commands/hostapd-wpe-debug-mode]]  # Using /etc/hostapd/enterprise.conf
```

Monitor logs in /tmp/hs20.log for captured credentials.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Multi-Factor Authentication Request Generation]] Multi-Factor Authentication Request Generation (for credential phishing)
- [[LLMNR-NBT-NS Poisoning and SMB Relay]] Adversary-in-the-Middle (for evil twin attacks)
- [[SAML Tokens]] Forge Web Credentials (credential capture)

### Tactics

- [[Initial Access]] Initial Access
- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual SSIDs mimicking legitimate networks (monitor with Kismet or Wireshark)
- Rogue APs broadcasting on common channels without proper certificates
- Increased deauthentication frames (use airodump-ng to detect)
- Log analysis for hostapd processes on unauthorized devices
- Network traffic showing EAPOL exchanges to fake APs
- Wireless intrusion detection systems (WIDS) alerting on AP spoofing

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/aircrack-ng]] (for handshake cracking)
- [[tools/Wireshark]] (for packet analysis)
- [[tools/airmon-ng]] (for interface management)

## References

- Official GitHub: https://github.com/OpenSecurityTrainingInfoSec/hostapd-wpe
- Hostapd Documentation: https://w1.fi/hostapd/
- Wireless Pwnage Guide: https://www.aircrack-ng.org/doku.php?id=hostapd-wpe
