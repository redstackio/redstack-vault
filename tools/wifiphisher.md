---
id: 7a9b5083-7d47-41de-b024-c64e30c3f176
type: tool
verified: true
created_at: '2019-08-28T21:17:34.757082+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - phishing
  - wifi
  - social-engineering
  - wireless
url: 'https://github.com/wifiphisher/wifiphisher'
description: >-
  Automated phishing tool for Wi-Fi networks to capture WPA/WPA2 credentials via
  rogue access points and fake portals.
validated: true
---

# wifiphisher

**Status**: Unverified

## Overview

Wifiphisher is a rogue Access Point framework for conducting phishing attacks against Wi-Fi networks. It automates the process of creating fake hotspots that impersonate legitimate networks, deauthenticating clients and serving phishing pages to steal credentials or deliver malware. Commonly used in wireless security testing and red team operations for social engineering simulations.

## Description

Wifiphisher performs man-in-the-middle attacks by setting up an Evil Twin access point. Once clients connect, it redirects HTTP traffic to customizable phishing pages, such as fake firmware updates or captive portals. Unlike brute-force methods, it relies on social engineering to trick users into voluntarily entering WPA/WPA2 passphrases. The attack unfolds in phases: deauthentication from the real AP, connection to the rogue AP, and presentation of a tailored phishing interface.

## Features

- Feature 1: Automated deauthentication and rogue AP creation using hostapd and similar tools.
- Feature 2: Built-in phishing scenarios like firmware upgrades, OAuth logins, and router configuration pages.
- Feature 3: Customizable templates for phishing pages and real-time credential capture.
- Feature 4: Support for jamming legitimate APs and handling multiple clients simultaneously.
- Feature 5: Integration with tools like dnsmasq for DHCP and iptables for traffic redirection.

## Installation

### Requirements

- Linux system with wireless card supporting monitor mode (e.g., Atheros or Ralink chipsets).
- Python 3.7+ and dependencies like hostapd, dnsmasq, iptables.
- Root privileges for interface manipulation.

### Install Commands

```bash
# On Ubuntu/Debian (not pre-installed)
git clone https://github.com/wifiphisher/wifiphisher.git
cd wifiphisher
sudo python3 setup.py install

# Or via pip (if available)
pip3 install wifiphisher
```

On Kali Linux, Wifiphisher is pre-installed and can be updated via apt.

```bash
sudo apt update && sudo apt install wifiphisher
```

## Basic Usage

```bash
wifiphisher --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -nI, --niface | Network interface for the attack |
| -e, --essid | Target ESSID to impersonate |
| -T, --template | Phishing scenario template (e.g., firmware-upgrade) |
| -p, --port | Port for the web server |
| -v, --verbose | Enable verbose logging |

## Examples

### Example 1: Basic Usage

```bash
wifiphisher -nI wlan0 -e "Target Network"
```

Launches a default phishing attack on the specified interface targeting the given ESSID.

### Example 2: Advanced Usage

```bash
wifiphisher -nI wlan0 -e "Target Network" -T firmware-upgrade --essid "Target Network"
```

Uses the firmware-upgrade template for a more convincing phishing page.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Phishing]] Phishing
- [[Active Scanning]] Active Scanning

### Tactics

- [[Initial Access]] Initial Access
- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual deauthentication frames in Wi-Fi traffic (monitor with Wireshark or airodump-ng).
- Detection method 2: Rogue APs broadcasting identical SSIDs with stronger signals; use Wi-Fi analyzers like Kismet.
- Detection method 3: Traffic redirection to suspicious phishing domains; inspect DNS queries and HTTP redirects.
- Detection method 4: High volume of DHCP requests from a single MAC or unusual ARP spoofing patterns.

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
- [[tools/bettercap]]

## References

- Official GitHub: https://github.com/wifiphisher/wifiphisher
- Documentation: https://wifiphisher.readthedocs.io/
- Related resources: Wi-Fi security testing guides on Offensive Security.
