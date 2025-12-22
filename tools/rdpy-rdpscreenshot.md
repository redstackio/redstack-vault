---
id: 7309d8f9-fe12-41b4-9067-11f411c9c678
type: tool
verified: true
created_at: '2019-08-28T21:17:39.341614+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - rdp
  - screenshot
  - python
  - collection
  - lateral-movement
url: 'https://github.com/citronneur/rdpy'
commands:
  - '[[commands/rdpy-rdpscreenshot-take-screenshot]]'
validated: true
---

# rdpy-rdpscreenshot

**Status**: Unverified

## Overview

rdpy-rdpscreenshot is a component of the RDPY library, a pure Python implementation of the Microsoft Remote Desktop Protocol (RDP) for both client and server sides. It allows capturing screenshots from remote RDP sessions without requiring native Windows tools. Commonly used in red team operations for stealthy reconnaissance, automated data collection, or verifying remote access during lateral movement.

## Description

Built on the Twisted event-driven networking engine, RDPY supports standard RDP security (RDP, SSL/TLS), and Network Level Authentication (NLA) via NTLMv2. The rdpy-rdpscreenshot tool specifically enables connecting to an RDP endpoint, authenticating, and extracting a bitmap screenshot of the remote desktop. It is lightweight, cross-platform, and ideal for scripting in Python environments during penetration testing or post-exploitation.

## Features

- Pure Python RDP client implementation (no external dependencies beyond Twisted)
- Support for RDP security layers: Basic, TLS, CredSSP
- NLA authentication compatibility
- Screenshot capture in PNG format
- Scriptable for automated operations
- Handles RDP bitmap decompression for image rendering

## Installation

### Requirements

- Python 2.7 or 3.x
- Twisted library (pip install twisted)
- PIL/Pillow for image handling (pip install pillow)

### Install Commands

```bash
# Clone the repository
git clone https://github.com/citronneur/rdpy.git
cd rdpy

# Install dependencies
pip install twisted pillow

# The tool is available as rdpy-rdpscreenshot.py in the tools directory
```

On Kali Linux, it may be available via apt or manual install as above.

## Basic Usage

```bash
tool --help
```

Run `python rdpy-rdpscreenshot.py --help` for options.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -u, --username | Specify RDP username |
| -p, --password | Specify RDP password |
| -d, --domain | Optional domain for authentication |

## Examples

### Example 1: Basic Usage

```bash
python rdpy-rdpscreenshot.py 192.168.1.100 administrator password screenshot.png
```

This connects to the target RDP server, authenticates, captures the desktop, and saves it as screenshot.png.

### Example 2: Advanced Usage

For domain-joined systems:

```bash
python rdpy-rdpscreenshot.py -d DOMAIN 10.0.0.5 user pass output.png
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote Desktop Protocol]] Remote Desktop Protocol
- [[Automated Collection]] Automated Collection

### Tactics

- [[Lateral Movement]] Lateral Movement
- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual RDP connections from Python processes (monitor for twisted-python network activity)
- Network traffic on TCP 3389 with Python user-agent or non-standard RDP clients
- File creation of PNG screenshots with timestamps matching RDP logins
- Process monitoring for rdpy.py or twisted-related modules during RDP sessions

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/xfreerdp]]
- [[tools/rdesktop]]

## References

- Official GitHub: https://github.com/citronneur/rdpy
- RDPY Documentation: Included in repo README
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1021/001/
