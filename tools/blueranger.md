---
type: tool
description: >-
  A Bash script for locating Bluetooth device radios using link quality
  measurements from L2CAP pings.
url: 'https://github.com/gsidoni/BlueRanger'
tags:
  - bluetooth
  - reconnaissance
  - wireless
  - discovery
platforms:
  - Linux
verified: true
validated: true
---

# blueranger

**Status**: Unverified

## Overview

BlueRanger is a simple Bash script designed for Bluetooth device location estimation. It works by sending L2CAP (Logical Link Control and Adaptation Protocol) pings to nearby Bluetooth radios, leveraging the link quality metric to approximate distance. Most Bluetooth devices respond to these pings without requiring authentication, making it useful for passive discovery in reconnaissance scenarios. Use a Class 1 Bluetooth adapter for longer-range detection or a Class 3 adapter for precise short-range locating.

## Description

The tool establishes temporary connections via L2CAP pings between the attacker's Bluetooth interface and target devices. The link quality value (ranging from 0 to 255) is used as a proxy for proximity—the higher the value, the closer the device. Factors like adapter quality, environmental interference, and device responsiveness can affect accuracy, and fluctuations may occur even with stationary devices. This is particularly useful in wireless penetration testing for mapping Bluetooth-enabled assets in physical security assessments.

## Features

- Feature 1: L2CAP ping-based discovery without authentication
- Feature 2: Link quality measurement for rough distance estimation
- Feature 3: Support for different Bluetooth adapter classes for varying range and precision
- Feature 4: Simple script-based operation, easy to integrate into larger toolchains

## Installation

### Requirements

- Linux system with Bluetooth support (e.g., BlueZ stack)
- Bluetooth adapter (Class 1 recommended for range)
- Bash shell

### Install Commands

```bash
# Clone the repository
sudo apt update && sudo apt install git -y
git clone https://github.com/gsidoni/BlueRanger.git
cd BlueRanger
chmod +x blueranger.sh
```

On Kali Linux, it may be available via package managers, but cloning ensures the latest version.

## Basic Usage

```bash
./blueranger.sh --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -i, --interface | Specify Bluetooth interface (default: hci0) |
| -h, --help | Show usage information |

## Examples

### Example 1: Basic Usage

Scan using the default interface:

```bash
./blueranger.sh -i hci0
```

### Example 2: Advanced Usage

Run a continuous scan on a specific interface to monitor dynamic environments:

```bash
./blueranger.sh -i hci0
```

Output will list discovered MAC addresses with corresponding link quality scores.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote System Discovery]] Remote System Discovery (for identifying nearby Bluetooth devices)

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for unusual L2CAP ping traffic on Bluetooth interfaces using tools like hcidump or Wireshark with Bluetooth sniffing
- Detection method 2: Log Bluetooth adapter activity for unauthorized scanning sessions
- Detection method 3: High link quality fluctuations or repeated connection attempts from unknown MAC addresses

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
- [[tools/btscanner]]

## References

- Official GitHub Repository: https://github.com/gsidoni/BlueRanger
- BlueZ Documentation: https://www.bluez.org/
