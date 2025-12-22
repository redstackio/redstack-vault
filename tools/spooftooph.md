---
id: f254dd5b-f364-4555-8458-cbcb9c66c4d4
type: tool
verified: true
created_at: '2019-08-28T21:17:22.724128+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - bluetooth
  - spoofing
  - defense-evasion
  - reconnaissance
url: 'https://github.com/nullsecuritynet/tools/blob/master/bluetooth/spooftooph'
validated: true
---

# spooftooph

**Status**: Unverified

## Overview

Spooftooph is a Linux-based tool designed to automate the spoofing or cloning of Bluetooth device information. It enables security testers to hide Bluetooth devices in plain sight by mimicking other devices' profiles, which is useful for evasion during physical security assessments, red team operations, or testing Bluetooth tracking defenses.

## Description

Spooftooph interacts with the BlueZ Bluetooth stack to modify the local adapter's discoverable attributes, such as BDADDR (Bluetooth Device Address), device name, and major/minor class. This allows for dynamic profile changes to avoid detection or impersonate legitimate devices. It is particularly valuable in scenarios involving Bluetooth reconnaissance, where an attacker needs to blend into a crowd of devices or clone a specific target's profile for social engineering follow-ups.

## Features

- **Clone and Log Device Information**: Scan and clone Bluetooth devices, logging details like BDADDR, name, and class for later use.
- **Generate Random Profiles**: Create synthetic Bluetooth identities with random attributes to evade tracking.
- **Interval-Based Changes**: Automatically rotate profiles at specified intervals to maintain evasion over time.
- **Custom Specification**: Manually set device name, class, and other attributes for precise control.
- **Scan Log Selection**: Select and clone devices directly from previous scan logs.

## Installation

### Requirements

- Linux kernel with BlueZ Bluetooth stack (version 4.0+ recommended).
- Root privileges (sudo) for modifying HCI (Host Controller Interface) settings.
- Dependencies: gcc, make, libbluetooth-dev (for compilation).

### Install Commands

Spooftooph is not typically pre-installed; compile from source:

```bash
# Clone the repository (from nullsecuritynet or similar fork)
git clone https://github.com/nullsecuritynet/tools.git
cd tools/bluetooth/spooftooph

# Install dependencies (on Debian/Ubuntu/Kali)
sudo apt update
sudo apt install build-essential libbluetooth-dev

# Compile and install
make
sudo make install
```

For Kali Linux, it may be available via custom repos or AUR equivalents, but source build is standard.

## Basic Usage

```bash
spooftooph --help
```

This displays available options like `-s` for scan, `-c` for clone, `-r` for random, `-i` for interval, `-n` for name, and `-C` for class.

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and usage |
| `-s` | Scan mode: Discover and log nearby devices |
| `-v` | Verbose output for debugging |
| `-l <file>` | Custom log file path (default: spooftooph.log) |

## Examples

### Example 1: Basic Usage (Scan Devices)

```bash
sudo spooftooph -s
```

Starts scanning and logs devices to spooftooph.log.

### Example 2: Advanced Usage (Clone and Rotate)

First scan, then clone and set interval:

```bash
sudo spooftooph -s  # Scan and note BDADDR
sudo spooftooph -c 00:11:22:33:44:55 -i 60  # Clone and change every 60s
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Disable or Modify Tools]] Impair Defenses: Disable or Modify Tools (Bluetooth profile manipulation to evade detection)
- [[Logon Scripts]] Boot or Logon Initialization Scripts (Altering device discovery attributes)

### Tactics

- [[Defense Evasion]] Defense Evasion
- [[Reconnaissance]] Reconnaissance (Bluetooth device discovery)

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual changes in local Bluetooth adapter attributes (monitor with `hciconfig` or `bluetoothctl`).
- Log entries in /var/log or custom files showing BDADDR modifications.
- High CPU/IO on bluetoothd process during profile rotations.
- Network anomalies if combined with other tools for data exfil over Bluetooth.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[bluetoothctl]] (BlueZ command-line utility for basic control)
- [[hcitool]] (Legacy HCI tool for inquiry and spoofing basics)

## References

- Official repository: https://github.com/nullsecuritynet/tools/tree/master/bluetooth/spooftooph
- BlueZ documentation: http://www.bluez.org/
- Related research on Bluetooth spoofing: Search for "Bluetooth MAC spoofing attacks"
