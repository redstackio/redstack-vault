---
id: 004ca6e2-2eac-4a76-b3d1-06f7af18e1c5
name: airodump-ng
type: tool
verified: true
created_at: '2019-08-28T21:17:32.644147+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - wireless
  - reconnaissance
  - packet-capture
  - aircrack-ng
url: 'https://www.aircrack-ng.org/doku.php?id=airodump-ng'
validated: true
---

# airodump-ng

**Status**: Unverified

## Overview

Airodump-ng is a packet capture tool from the Aircrack-ng suite, designed for capturing raw 802.11 WiFi frames. It is primarily used in wireless security testing for discovering access points, monitoring client activity, and collecting data for cracking tools like Aircrack-ng. Common use cases include network reconnaissance, WEP/WPA key recovery support, and logging access point locations with GPS integration.

## Description

Airodump-ng passively sniffs wireless traffic, displaying real-time information on nearby networks including BSSIDs, ESSIDs, encryption types, channels, signal strength, and associated clients. It supports output in formats like CSV for analysis and PCAP for Wireshark compatibility. Requires a compatible WiFi adapter in monitor mode. It excels in environments needing detailed wireless mapping without active probing.

## Features

- Feature 1: Real-time display of access points and clients with signal metrics
- Feature 2: GPS logging for access point geolocation
- Feature 3: Focused capture by channel, BSSID, or ESSID to reduce noise
- Feature 4: Multiple output formats (CSV, PCAP, IVS) for integration with other tools
- Feature 5: Channel hopping to scan all frequencies efficiently

## Installation

### Requirements

- Compatible WiFi adapter supporting monitor mode (e.g., Atheros AR9271, Ralink RT3070)
- Linux kernel with wireless extensions
- Root privileges for interface manipulation

### Install Commands

```bash
# On Kali Linux (pre-installed)
sudo apt update && sudo apt install aircrack-ng

# On Ubuntu
sudo apt update && sudo apt install aircrack-ng

# From source (optional)
git clone https://github.com/aircrack-ng/aircrack-ng.git
cd aircrack-ng
make && sudo make install
```

## Basic Usage

```bash
airodump-ng --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -c <channel> | Capture on specific channel |
| --bssid <bssid> | Filter by access point MAC |
| -w <prefix> | Output file prefix |
| --output-format <formats> | Specify formats (e.g., csv,pcap) |
| --gpsd | Enable GPS logging |

## Examples

### Example 1: Basic Usage

Scan all networks:

```bash
airodump-ng wlan0mon
```

### Example 2: Advanced Usage

Capture specific AP with GPS:

```bash
airodump-ng wlan0mon --bssid AA:BB:CC:DD:EE:FF --output-format csv,pcap -w capture --gpsd
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning (for wireless network discovery)
- [[Bypass User Account Control]] Bypass User Account Control (in context of wireless privilege escalation testing)

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for wireless interface mode changes (e.g., iwconfig showing monitor mode)
- Detection method 2: High volume of promiscuous WiFi traffic or PCAP file creation in /tmp
- Detection method 3: Process monitoring for airodump-ng execution via ps or audit logs
- Detection method 4: Anomalous GPS data logging if enabled

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
- [[tools/aireplay-ng]]
- [[tools/Wireshark]]

## References

- Official documentation: https://www.aircrack-ng.org/doku.php?id=airodump-ng
- Aircrack-ng GitHub: https://github.com/aircrack-ng/aircrack-ng

*Last updated: 2023-10-01*
