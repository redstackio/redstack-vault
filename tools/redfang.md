---
id: a760bb3d-92fc-44d0-b8b0-9f4c0866cb85
type: tool
verified: true
created_at: '2019-08-28T21:17:41.310368Z'
updated_at: '2023-10-01T12:00:00Z'
platforms:
  - Linux
tags:
  - bluetooth
  - reconnaissance
  - wireless
  - brute-force
url: 'https://www.kali.org/tools/redfang/'
validated: true
---

# RedFang

**Status**: Unverified

## Overview

RedFang is a lightweight proof-of-concept tool designed for discovering non-discoverable Bluetooth devices. It performs brute-force scanning by iterating through possible Bluetooth addresses (BD_ADDR) and issuing read_remote_name() inquiries to reveal hidden devices that do not respond to standard discovery protocols. Commonly used in wireless penetration testing and red team operations to map Bluetooth attack surfaces in physical proximity.

## Description

RedFang targets the Bluetooth protocol's BD_ADDR (48-bit address space) by scanning specified ranges, focusing on the last six bytes for efficiency in known prefix scenarios. It is particularly effective against devices configured for privacy or non-discoverability, such as IoT devices, headsets, or peripherals in corporate or public environments. The tool requires a Bluetooth adapter capable of raw inquiries and operates on Linux systems with BlueZ stack.

## Features

- Brute-force BD_ADDR scanning for hidden devices
- Customizable address ranges to optimize scan time
- Support for specific Bluetooth interfaces (e.g., hci0)
- Minimal resource usage for extended scanning sessions
- Output of discovered device names and addresses for further enumeration

## Installation

### Requirements

- Linux kernel with BlueZ Bluetooth stack
- Bluetooth adapter (USB dongle or built-in) supporting inquiry mode
- Root privileges for interface access

### Install Commands

```bash
# On Kali Linux (pre-installed in many distributions)
sudo apt update
sudo apt install redfang

# Compile from source if needed
wget https://example-repo/redfang.tar.gz  # Replace with official source
tar -xzf redfang.tar.gz
cd redfang
make
sudo make install
```

## Basic Usage

```bash
redfang --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -i, --interface | Specify Bluetooth interface (default: hci0) |
| <start_addr> | Starting BD_ADDR for scan |
| <end_addr> | Ending BD_ADDR for scan |
| -h, --help | Display usage information |

## Examples

### Example 1: Basic Usage

Scan a narrow range for quick testing:

```bash
redfang -i hci0 00:00:00:00:00:00 00:00:00:00:FF:FF
```

### Example 2: Advanced Usage

Perform a broader scan on a specific interface:

```bash
redfang -i hci1 00:11:22:33:00:00 00:11:22:33:FF:FF
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Vulnerability Scanning]] Scanning IP Blocks (adapted for wireless: Bluetooth address scanning)

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual Bluetooth inquiry traffic on monitored adapters (via hcidump or Wireshark with Bluetooth plugin)
- High volume of read_remote_name() requests from a single interface
- Presence of redfang process via ps aux | grep redfang
- Logs in /var/log/bluetooth or system dmesg showing excessive HCI inquiries

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/BlueHydra]]
- [[tools/Ubertooth]]

## References

- Official Kali Documentation: https://www.kali.org/tools/redfang/
- BlueZ Project: http://www.bluez.org/
- Bluetooth SIG Specifications for BD_ADDR and inquiries
