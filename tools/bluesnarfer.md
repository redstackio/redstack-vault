---
type: tool
verified: true
created_at: '2019-08-28T21:17:37.961734+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
tags:
  - bluetooth
  - wireless
  - exploitation
  - reconaissance
url: 'https://www.kali.org/tools/bluesnarfer/'
commands:
  - '[[commands/bluesnarfer-basic-connection]]'
  - '[[commands/bluesnarfer-list-services]]'
  - '[[commands/bluesnarfer-extract-data]]'
validated: true
---

# bluesnarfer

**Status**: Unverified

## Overview

Bluesnarfer is a command-line tool designed for Bluetooth bluesnarfing attacks, which involve unauthorized access and extraction of data from Bluetooth-enabled devices, such as mobile phones, without proper authentication. It is commonly used in wireless penetration testing to demonstrate vulnerabilities in Bluetooth implementations, particularly in OBEX (Object Exchange) protocols for file and contact extraction.

## Description

Bluesnarfer exploits weaknesses in Bluetooth device security to connect to targets and retrieve sensitive information like phonebooks, calendars, or files. It requires a compatible Bluetooth adapter and is effective against older devices with default or weak PIN settings. The tool operates by establishing an RFCOMM connection over Bluetooth and issuing OBEX commands to pull data. It is part of offensive security toolkits like Kali Linux and is useful for assessing Bluetooth security in red team engagements or vulnerability assessments.

## Features

- Unauthorized data extraction via Bluetooth (bluesnarfing)
- Support for OBEX protocol interactions to retrieve contacts, messages, and files
- Channel scanning and service enumeration on target devices
- Integration with Bluetooth interfaces like hci0 for local adapter control
- Verbose output for debugging connection issues

## Installation

### Requirements

- Linux kernel with Bluetooth support (BlueZ stack)
- Compatible Bluetooth USB adapter (Class 1 recommended for range)
- Root privileges for interface access

### Install Commands

```bash
# On Kali Linux (pre-installed in many distributions)
sudo apt update
sudo apt install bluesnarfer

# On Ubuntu/Debian
echo 'deb http://http.kali.org/kali kali-rolling main contrib non-free' | sudo tee /etc/apt/sources.list.d/kali.list
wget -q -O - https://archive.kali.org/archive-key.asc | sudo apt-key add -
sudo apt update
sudo apt install bluesnarfer
```

## Basic Usage

```bash
bluesnarfer --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-i, --device INTERFACE` | Specify Bluetooth interface (e.g., hci0) |
| `-b, --bdaddr BDADDR` | Target device's Bluetooth address |
| `-c, --channel CHANNEL` | RFCOMM channel to connect on (default: 1 for OBEX) |
| `-d, --depth` | Recursively extract directory contents |
| `-f, --file FILE` | Save extracted data to FILE |
| `-r, --raw` | Output raw OBEX responses |
| `-s, --services` | List available services on target |
| `-V, --version` | Show version information |

## Examples

### Example 1: Basic Usage

Connect to a target device and extract basic information:

```bash
bluesnarfer -i hci0 -b 00:11:22:33:44:55
```

### Example 2: Advanced Usage

List services and extract phonebook to a file:

```bash
bluesnarfer -i hci0 -b 00:11:22:33:44:55 -s -f phonebook.vcf
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T0893]] Wireless Device Driver Exploitation
- [[Exploitation of Remote Services]] Exploitation of Remote Services

### Tactics

- [[Discovery]] Discovery
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual Bluetooth pairings or connections from unknown devices
- Monitoring for OBEX protocol traffic on RFCOMM channels (e.g., channel 10 for phonebook access)
- Bluetooth logs showing unauthorized service queries (use tools like btmon or Wireshark with Bluetooth plugin)
- Increased Bluetooth adapter activity on the target device
- File system changes if data is extracted (e.g., unexpected vCard files)

## Related Procedures

No related procedures documented yet.

## Related Tools

- [[hcitool]] (for device discovery and scanning)
- [[btscanner]] (Bluetooth scanner for enumeration)
- [[ubertooth]] (for deeper Bluetooth sniffing)

## References

- Official Kali Documentation: https://www.kali.org/tools/bluesnarfer/
- BlueZ Project: http://www.bluez.org/
- Bluetooth SIG Specifications: https://www.bluetooth.com/specifications/
