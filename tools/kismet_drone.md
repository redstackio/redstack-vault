---
id: 5042dad4-dfa1-40ba-a9ca-472ed6c35075
type: tool
verified: true
description: >-
  Remote sensor component of Kismet for distributed wireless network detection
  and sniffing.
url: 'https://www.kismetwireless.net/docs/readme/drones_and_sensors/'
created_at: '2019-08-28T21:17:28.451700+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - wireless
  - sniffing
  - reconnaissance
  - ids
commands:
  - '[[commands/kismet-drone-start-basic]]'
  - '[[commands/kismet-drone-verbose-start]]'
validated: true
---

# kismet_drone

**Status**: Unverified

## Overview

Kismet Drone is the remote sensor component of the Kismet wireless network detector, sniffer, and intrusion detection system (IDS). It enables distributed deployment for capturing 802.11 wireless traffic across multiple locations, streaming data back to a central Kismet server for analysis. Ideal for large-scale wireless reconnaissance, monitoring, and intrusion detection in security testing.

## Description

Kismet Drone works with wireless cards supporting raw monitoring (rfmon) mode to passively sniff 802.11a/b/g/n/ac/ax traffic. It supports integration with external programs for audio alerts, network summaries via speech synthesis, and GPS coordinates for mobile deployments. As part of the Kismet ecosystem, the drone handles remote capture sources, allowing operators to scale sniffing operations without a single point of presence. It connects to a Kismet server over TCP, sending packet data, alerts, and metadata for centralized processing and visualization.

## Features

- **Distributed Sensing**: Deploy multiple drones to cover wide areas or hidden locations for comprehensive wireless coverage.
- **Protocol Support**: Captures and decodes 802.11 traffic including management, control, and data frames.
- **Alerting**: Generates real-time alerts for detected networks, deauth attacks, or unusual activity.
- **GPS Integration**: Logs location data for mobile or vehicle-based deployments.
- **Encryption Handling**: Supports WEP, WPA, and WPA2 cracking integration via external tools.
- **Low Resource Footprint**: Designed for embedded or low-power devices like Raspberry Pi.

## Installation

### Requirements

- Linux kernel with wireless extensions support.
- Wireless adapter compatible with monitor mode (e.g., Atheros AR9271, Ralink RT3070).
- Kismet server running elsewhere in the network.

### Install Commands

```bash
# On Kali Linux (pre-installed with Kismet package)
sudo apt update && sudo apt install kismet

# On Ubuntu
sudo apt update && sudo apt install kismet

# From source (for latest version)
git clone https://www.kismetwireless.net/git/kismet.git
cd kismet
./configure
make
depmod -a
sudo make suidinstall
```

After installation, configure /etc/kismet/kismet_drone.conf with server details and interfaces.

## Basic Usage

```bash
kismet_drone --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -c, --config | Specify configuration file path |
| -v, --verbose | Enable verbose logging |
| --help | Show help and options |
| --log-level | Set logging level (debug, info, etc.) |

## Examples

### Example 1: Basic Usage

Start the drone with default config:

```bash
kismet_drone -c /etc/kismet/kismet_drone.conf
```

### Example 2: Advanced Usage

Start with verbose output and custom log level:

```bash
kismet_drone -c /etc/kismet/kismet_drone.conf -v --log-level debug
```

Related Commands:
- [[commands/kismet-drone-start-basic]]
- [[commands/kismet-drone-verbose-start]]

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning (for wireless network discovery)
- [[Network Sniffing]] Network Sniffing

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for 'kismet_drone' executable.
- Unusual network traffic to Kismet server ports (default 3501 TCP).
- Wireless interface in monitor mode (check via 'iwconfig' or 'iw dev').
- Log files in /var/log/kismet/ with drone activity.
- Increased CPU usage on wireless adapters during sniffing.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/kismet]] (main server and client)
- [[tools/aircrack-ng]] (for cracking captured handshakes)

## References

- Official Documentation: https://www.kismetwireless.net/docs/readme/drones_and_sensors/
- Kismet GitHub: https://www.kismetwireless.net/git/
