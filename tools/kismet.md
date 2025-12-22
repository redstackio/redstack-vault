---
id: 8ba9797e-0b6d-498b-9030-e54143bf329d
type: tool
verified: true
created_at: '2019-08-28T21:17:37.133660+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - wireless
  - sniffing
  - reconnaissance
  - ids
url: 'https://www.kismetwireless.net/'
validated: true
---

# kismet

**Status**: Unverified

## Overview

Kismet is an open-source 802.11 layer-2 wireless network detector, sniffer, and intrusion detection system (IDS). It passively monitors wireless traffic on supported interfaces in monitor (rfmon) mode, identifying networks, clients, and potential security events without generating detectable traffic. Commonly used in penetration testing for reconnaissance of Wi-Fi environments, mapping access points, and detecting misconfigurations or attacks like deauthentication floods.

## Description

Kismet supports 802.11a/b/g/n/ac protocols and can integrate with GPS for wardriving, audio alerts for events, and external tools for enhanced analysis. The core components include a server for capture and processing, a web-based UI for visualization, and logging in formats like PCAP for Wireshark integration. It excels in passive operations, making it stealthy for red team wireless assessments, but requires compatible hardware (e.g., Atheros or Ralink chipsets) that support monitor mode.

## Features

- **Packet Sniffing**: Captures raw 802.11 frames, decrypting WEP/WPA if keys are provided.
- **Network Detection**: Discovers SSIDs, BSSIDs, encryption types, and client associations.
- **Intrusion Detection**: Alerts on anomalies like rogue APs, evil twin attacks, or DoS attempts.
- **Web Interface**: Real-time dashboard at http://localhost:2501 for monitoring and alerts.
- **Logging and Export**: Supports PCAP, Kismet DB, and JSON logs for post-analysis.
- **Channel Hopping**: Automatically scans all channels to avoid missing networks.
- **GPS Integration**: Logs location data for mobile reconnaissance.

## Installation

### Requirements

- Linux kernel with wireless extensions.
- Compatible wireless adapter supporting monitor mode (e.g., Alfa AWUS036N).
- libpcap, libmicrohttpd, and protobuf libraries.

### Install Commands

```bash
# On Kali Linux (pre-installed)
sudo apt update && sudo apt install kismet

# On Ubuntu
sudo apt update && sudo apt install kismet

# From source (latest version)
git clone https://www.kismetwireless.net/git/kismet.git
cd kismet
./configure && make && sudo make suidinstall
```

Post-install: Ensure your wireless interface supports monitor mode with `iwconfig` or `airmon-ng`.

## Basic Usage

```bash
kismet --help
```
Displays help and available options.

### Common Options

| Option | Description |
|--------|-------------|
| -c, --channel | Set specific channel for capture |
| -v, --verbose | Increase verbosity level |
| --capture-source | Specify interface (e.g., wlan0) |
| --log-types | Enable specific logs (e.g., pcapng,alerts) |

## Examples

### Example 1: Basic Usage

```bash
kismet --capture-source wlan0mon
```
Starts capture on monitor-mode interface wlan0mon, accessible via web UI.

### Example 2: Advanced Usage

```bash
kismet -v --log-types all --gps on
```
Starts with verbose logging, all log types, and GPS enabled for wardriving.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning (for wireless reconnaissance)
- [[Network Sniffing]] Network Sniffing

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor mode enabled on interfaces (e.g., `iwconfig` shows MON).
- Unusual processes: `kismet` or `kismet_server` running.
- Network logs showing no transmitted packets but high reception on wireless.
- Web server on port 2501 or logs in /var/log/kismet/.
- Use tools like `ps aux | grep kismet` or IDS rules for monitor mode transitions.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Wireshark]]
- [[tools/aircrack-ng]]

## References

- Official Documentation: https://www.kismetwireless.net/docs/README/
- Kali Tools Page: https://www.kali.org/tools/kismet/
- GitHub Repository: https://www.kismetwireless.net/git/
