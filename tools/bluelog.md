---
id: 0852c699-2f89-4795-9a5c-8a749390a370
type: tool
verified: true
created_at: '2019-08-28T21:17:40.862353+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - bluetooth
  - reconnaissance
  - wireless
  - scanning
url: 'https://www.digforensics.com/bluelog/'
commands:
  - '[[commands/bluelog-basic-scan]]'
  - '[[commands/bluelog-start-daemon]]'
validated: true
---

# bluelog

**Status**: Unverified

## Overview

Bluelog is a Linux-based Bluetooth scanner designed for site surveys and long-term monitoring of Bluetooth traffic. It identifies discoverable devices in an area, making it useful for reconnaissance in wireless security assessments, such as mapping Bluetooth-enabled assets in physical penetration tests.

## Description

Bluelog operates by passively scanning for Bluetooth devices using a compatible interface (e.g., USB Bluetooth dongle). It supports daemon mode for continuous operation and includes a simple web front-end for visualizing results. Common use cases include determining the density of Bluetooth devices in a location, tracking device movement over time, and identifying potential targets for further exploitation like Bluejacking or Bluesnarfing.

## Features

- Feature 1: Passive Bluetooth device discovery with MAC address, device name, and class identification
- Feature 2: Daemon mode for background, long-duration scans
- Feature 3: Web-based interface for real-time monitoring and historical data review
- Feature 4: Output logging in various formats for analysis
- Feature 5: Support for multiple Bluetooth interfaces

## Installation

### Requirements

- Linux kernel with Bluetooth support
- BlueZ stack (usually pre-installed on security distros)
- Compatible Bluetooth adapter (e.g., hci0 interface)

### Install Commands

```bash
# On Kali Linux (pre-installed in many cases)
sudo apt update && sudo apt install bluelog

# On Ubuntu
sudo apt update && sudo apt install bluelog

# From source (if needed)
git clone https://github.com/kimocoder/bluelog.git
cd bluelog
make
sudo make install
```

## Basic Usage

```bash
bluelog --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -i, --iface | Specify Bluetooth interface (default: hci0) |
| -o, --output | Output file for results |
| -D | Daemon mode |
| -w, --web | Start web server on port (default: 8000) |
| -v | Verbose output |

## Examples

### Example 1: Basic Usage

Perform a one-time scan:

```bash
bluelog -i hci0 -o results.txt
```

### Example 2: Advanced Usage

Start continuous monitoring with web interface:

```bash
bluelog -D -i hci0 -w 8000
```
Access the web UI at http://localhost:8000 to view discovered devices.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning (for wireless device discovery)
- [[Remote System Discovery]] Remote System Discovery (Bluetooth-specific)

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for Bluetooth interface activity (e.g., hciconfig or bluetoothctl logs showing frequent inquiries)
- Detection method 2: Process monitoring for bluelog executable or high CPU on Bluetooth-related processes
- Detection method 3: Network traffic if web interface is enabled (port 8000 inbound)
- Detection method 4: Log files created in /var/log or user directories with Bluetooth scan data

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/hcitool]]
- [[tools/bluez]]
- [[tools/ubertooth]]

## References

- Official GitHub: https://github.com/kimocoder/bluelog
- BlueZ Documentation: http://www.bluez.org/
- Wireless Reconnaissance Guide: https://www.offensive-security.com/metasploit-unleashed/wireless-attacks/
