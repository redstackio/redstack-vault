---
id: 5b6e140b-69de-4105-a693-017fcd7f659c
type: tool
verified: true
created_at: '2019-08-28T21:17:21.360080+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - usb
  - autorun
  - payload-injection
  - hardware
  - persistence
url: 'https://github.com/dhobsd/u3-pwn'
validated: true
---

# u3-pwn

**Status**: Unverified

## Overview

u3-pwn is a specialized tool for modifying Sandisk U3 smart USB devices to inject executable payloads. It automates the creation of autorun-enabled ISOs, enabling persistence or initial access via removable media in red team operations or hardware pentesting.

## Description

u3-pwn targets legacy U3-enabled USB drives by extracting and replacing the original ISO file with a customized version that includes autorun.inf configurations to execute payloads automatically when inserted into a target system. This is particularly useful for social engineering attacks, supply chain compromises, or testing autorun defenses. The tool assumes the USB has the default U3 software installation and works on Linux environments for preparation.

## Features

- Automated ISO extraction and replacement
- Payload injection with autorun.inf generation
- Support for Windows executables (.exe)
- Backup of original USB contents
- Command-line interface for scripting

## Installation

### Requirements

- Python 3.x
- Access to a Linux system with USB mounting capabilities
- Sandisk U3 smart USB device

### Install Commands

```bash
# Clone the repository
git clone https://github.com/dhobsd/u3-pwn.git
cd u3-pwn

# Install dependencies (if any, typically minimal)
pip3 install -r requirements.txt

# Make executable
chmod +x u3-pwn.py
```

For Kali Linux, it may require additional USB tools like `mount` and `mkisofs`:

```bash
sudo apt update && sudo apt install genisoimage
```

## Basic Usage

```bash
python3 u3-pwn.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| --extract | Extract original ISO without modification |
| --inject | Specify payload for injection (default mode) |
| -v, --verbose | Enable verbose output for debugging |

## Examples

### Example 1: Basic Usage

Mount the USB device, then inject a payload:

```bash
python3 u3-pwn.py /media/usb /home/user/backdoor.exe
```

### Example 2: Advanced Usage

Extract first, then inject with custom autorun:

```bash
python3 u3-pwn.py --extract /media/usb
python3 u3-pwn.py /media/usb /home/user/payload.exe --autorun custom.inf
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Replication Through Removable Media]] Replication Through Removable Media
- [[Remote File Copy]] Ingress Tool Transfer

### Tactics

- [[Persistence]] Persistence
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual ISO files on USB devices with autorun.inf
- Modified U3 partitions on Sandisk drives
- Execution of payloads from removable media (monitor Autorun events in Windows)
- File system changes on USB (e.g., via forensic tools like Volatility or USBDeview)

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Rubber-Ducky]]
- [[tools/USB-Autorun-Tools]]

## References

- Official GitHub: https://github.com/dhobsd/u3-pwn
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1091/
- USB Forensics Guide: https://www.sans.org/reading-room/whitepapers/forensics/
