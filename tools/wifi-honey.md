---
id: bbf51a54-d9ac-481d-94af-c5650bb62733
type: tool
verified: true
created_at: '2019-08-28T21:17:25.009955+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - wifi
  - wireless
  - honeypot
  - monitor-mode
  - deauthentication
url: ''
validated: true
---

# wifi-honey

**Status**: Unverified

## Overview

wifi-honey is a bash script designed for wireless security testing, particularly in WiFi penetration testing scenarios. It automates the configuration of multiple monitor mode interfaces from a single WiFi adapter, enabling simultaneous rogue access point (AP) operations and packet capturing. This tool is useful for creating WiFi honeypots, conducting deauthentication attacks, or monitoring network traffic in red team engagements.

## Description

The script leverages the aircrack-ng suite to bring a physical WiFi interface into monitor mode and splits it into five virtual monitor interfaces: four for hosting rogue APs (e.g., for evil twin attacks or client deauth) and one dedicated to running airodump-ng for real-time packet sniffing and analysis. To streamline management, all background processes are encapsulated within GNU screen sessions, each labeled for easy identification and switching (e.g., via Ctrl+A followed by the session number). This setup is ideal for environments requiring multi-interface WiFi operations without manual terminal juggling, such as in wardriving, WiFi auditing, or adversarial simulations targeting wireless networks.

## Features

- Feature 1: Automates creation of up to five monitor mode interfaces from one adapter.
- Feature 2: Launches rogue AP processes and airodump-ng in isolated screen sessions.
- Feature 3: Labeled sessions for quick attachment and monitoring (e.g., screen -r wifi-ap1).
- Feature 4: Compatible with compatible WiFi chipsets supporting monitor mode (e.g., Atheros AR9271).

## Installation

### Requirements

- Linux distribution with kernel support for monitor mode (e.g., Kali Linux).
- Compatible USB WiFi adapter (e.g., Alfa AWUS036ACH).
- aircrack-ng suite installed.
- GNU screen utility.
- Root privileges for interface manipulation.

### Install Commands

```bash
# Install dependencies on Debian-based systems (e.g., Kali, Ubuntu)
sudo apt update
sudo apt install aircrack-ng screen

# Download the wifi-honey script (assuming from a GitHub repo or local source)
# wget https://example.com/wifi-honey.sh
# chmod +x wifi-honey.sh
```

Place the script in a directory like ~/tools/ and ensure it's executable.

## Basic Usage

```bash
./wifi-honey.sh --help
```

The script typically accepts the base interface as an argument.

### Common Options

| Option | Description |
|--------|-------------|
| No flags | Default setup with four APs and one capture session |
| -i, --interface | Specify the WiFi interface (default: wlan0) |
| -h, --help | Show usage information |

## Examples

### Example 1: Basic Usage

```bash
sudo ./wifi-honey.sh wlan0
```

This initiates the setup on wlan0, creating mon0-mon4 interfaces and starting screen sessions.

### Example 2: Advanced Usage

Run on a specific interface with verbose output if supported:

```bash
sudo ./wifi-honey.sh -i wlan1
```

After setup, attach to sessions: `screen -r wifi-capture` to view airodump-ng output.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Steal Web Session Cookie]] Steal Web Session Cookie (for capturing credentials in honeypot scenarios)
- [[Forge Web Credentials]] Forge Web Credentials (rogue AP for phishing)
- [[Domain Controller Authentication]] Wireless Mouse/Keyboard (extended to WiFi manipulation)

### Tactics

- [[Initial Access]] Initial Access (via rogue APs)
- [[Impact]] Impact (deauthentication for DoS)

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual monitor mode interfaces (e.g., multiple 'monX' via `iwconfig`).
- Detection method 2: GNU screen processes with WiFi-related names (e.g., `ps aux | grep screen` showing wifi-ap*).
- Detection method 3: High volume of deauth packets or rogue SSIDs via wireless IDS (e.g., Kismet).
- Detection method 4: aircrack-ng processes in process list (`ps aux | grep air`).

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
- [[tools/kismet]]

## References

- Aircrack-ng Documentation: https://www.aircrack-ng.org/
- GNU Screen Manual: https://www.gnu.org/software/screen/
