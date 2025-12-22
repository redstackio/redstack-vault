---
id: ef944d8e-76a8-4eb7-978e-962ec931b797
type: tool
verified: true
created_at: '2019-08-28T21:17:39.263453+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
tags:
  - wireless
  - wifi
  - deauthentication
  - dos
  - exploitation
url: 'https://www.kali.org/tools/mdk3/'
validated: true
---

# mdk3

**Status**: Unverified

## Overview

mdk3 is a proof-of-concept tool designed to exploit common weaknesses in the IEEE 802.11 wireless protocol. It is primarily used for testing WiFi network resilience against various denial-of-service (DoS) and disruption attacks, such as deauthentication floods and beacon storms. Common use cases in offensive security include assessing wireless network security during red team engagements, but it requires explicit permission from the network owner to avoid legal issues.

## Description

mdk3 enables attackers to perform layer 2 attacks on wireless networks by crafting and sending malicious 802.11 frames. It supports monitor mode on compatible wireless interfaces and can target access points (APs), clients, or entire channels. Key capabilities include deauthentication/disassociation attacks to disconnect clients, authentication request floods to overwhelm APs, and beacon frame floods to create fake networks. It is typically run on Linux systems with a compatible WiFi adapter supporting packet injection.

## Features

- Deauthentication and disassociation attacks to force client disconnections
- Authentication DoS floods to exhaust AP resources
- Beacon frame generation for network spoofing and flooding
- Probe response floods to amplify traffic
- Support for channel hopping and specific BSSID targeting
- Compatible with monitor mode interfaces like those using ath9k or rtl8187 drivers

## Installation

### Requirements

- Linux kernel with wireless extensions
- Compatible WiFi adapter supporting monitor mode and packet injection (e.g., Alfa AWUS036N with Atheros chipset)
- Root privileges for interface manipulation

### Install Commands

```bash
# On Kali Linux (pre-compiled package available)
sudo apt update
sudo apt install mdk3

# On Ubuntu/Debian (from source if needed)
sudo apt install git build-essential libpcap-dev
cd /opt
sudo git clone https://github.com/aircrack-ng/mdk3.git  # Note: mdk3 is often bundled or forked; use Kali repo for stability
cd mdk3
sudo make && sudo make install
```

## Basic Usage

```bash
mdk3 --help
```
This displays all available attack modes and options.

### Common Options

| Option | Description |
|--------|-------------|
| `-i <interface>` | Specify the wireless interface in monitor mode |
| `-c <channel>` | Target a specific channel |
| `-b <BSSID>` | Target a specific access point MAC address |
| `-s <packets/sec>` | Set packet transmission speed |
| `-t <time>` | Duration of the attack in seconds |
| `--bssid <BSSID>` | Filter by BSSID for client-targeted attacks |

## Examples

### Example 1: Basic Usage - Deauthentication Flood

```bash
# Put interface in monitor mode first (using airmon-ng)
sudo airmon-ng start wlan0
mdk3 wlan0mon d -b <AP_BSSID> -c 6
```
This performs a deauth attack on the specified AP on channel 6.

### Example 2: Advanced Usage - Beacon Flood

```bash
mdk3 wlan0mon b -n "FakeAP" -c 11 -s 100
```
This floods the channel with beacon frames for a fake SSID "FakeAP" at 100 packets per second.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[Network Denial of Service]] Network Denial of Service

### Tactics

- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual spikes in deauthentication/disassociation frames on wireless networks (monitor with Wireshark or tcpdump on WiFi interface)
- High volume of malformed 802.11 management frames from a single source MAC
- Client disconnections without valid reasons, logged in AP event logs (e.g., syslog on hostapd)
- Presence of mdk3 process or related libraries in memory forensics (e.g., via Volatility)
- Wireless intrusion detection systems (WIDS) like Kismet alerting on DoS patterns

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
- [[tools/Wireshark]]
- [[tools/kismet]]

## References

- Official Kali Documentation: https://www.kali.org/tools/mdk3/
- GitHub Repository (forks): https://github.com/t6x/mdk3
- Aircrack-ng Suite Integration: https://www.aircrack-ng.org/
