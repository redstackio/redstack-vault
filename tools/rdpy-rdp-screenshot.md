---
id: 8e9eac8e-6930-4d24-900c-3d7364c3aa82
type: tool
verified: true
description: >-
  Pure Python implementation of RDP protocol with screenshot capture
  capabilities for remote desktop sessions.
url: 'https://github.com/citronneur/rdpy'
tags:
  - rdp
  - screenshot
  - remote-access
  - post-exploitation
platforms:
  - Linux
  - Windows
commands:
  - '[[commands/rdpy-rdp-screenshot-capture]]'
created_at: '2019-08-28T21:17:22.679777+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
validated: true
---

# rdpy-rdp-screenshot

**Status**: Unverified

## Overview

rdpy-rdp-screenshot is part of the RDPY library, a pure Python implementation of the Microsoft Remote Desktop Protocol (RDP) for both client and server sides. It enables capturing screenshots of remote Windows desktops during security testing, such as post-exploitation or lateral movement scenarios. Built on the Twisted event-driven networking engine, it supports standard RDP security, RDP over SSL, and Network Level Authentication (NLA) via NTLMv2.

## Description

RDPY allows security professionals to interact with RDP services without relying on native Windows tools. The screenshot functionality is particularly useful for gathering visual intelligence from compromised systems, verifying session control, or documenting remote environments. It operates as a lightweight RDP client that connects to a target, authenticates, and extracts screen captures without full desktop interaction. Common use cases include red team operations for stealthy reconnaissance after gaining initial access via RDP credentials.

## Features

- Pure Python RDP client and server implementation
- Support for RDP security layer (RDP, SSL/TLS)
- NLA authentication using NTLMv2
- Screenshot capture from active RDP sessions
- Event-driven architecture via Twisted for efficient handling of protocol exchanges
- No external dependencies beyond Python standard libraries and Twisted

## Installation

### Requirements

- Python 2.7 or 3.x (tested on 3.6+)
- Twisted library (pip install twisted)
- Access to a target RDP-enabled Windows system

### Install Commands

```bash
# Clone the repository
git clone https://github.com/citronneur/rdpy.git
cd rdpy

# Install dependencies
pip install twisted

# Install RDPY
python setup.py install
```

On Kali Linux, you can also use:
```bash
apt update && apt install python3-pip git
pip3 install twisted
git clone https://github.com/citronneur/rdpy.git && cd rdpy && python3 setup.py install
```

## Basic Usage

```bash
python3 -m rdpy.screenshot --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and usage |
| `--user` | Specify RDP username |
| `--password` | Specify RDP password |
| `--host` | Target hostname or IP |
| `--output` | Output file for screenshot (default: screenshot.png) |
| `--security` | Security layer (rdp, tls, nla) |

## Examples

### Example 1: Basic Usage

Capture a screenshot from a target RDP server using basic credentials:

```bash
python3 -m rdpy.screenshot --host 192.168.1.100 --user administrator --password P@ssw0rd
```

This connects to the target, authenticates, and saves a PNG screenshot of the desktop.

### Example 2: Advanced Usage with TLS and Custom Output

```bash
python3 -m rdpy.screenshot --host target.example.com --user user --password pass --security tls --output remote_desktop.png
```

Uses TLS security and saves the screenshot to a custom file.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote Desktop Protocol]] Remote Desktop Protocol
- [[System Information Discovery]] System Information Discovery (via visual screenshot)

### Tactics

- [[Lateral Movement]] Lateral Movement
- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic on TCP port 3389 (RDP) originating from non-Windows systems or unusual sources
- Python processes (e.g., python.exe or python3) establishing RDP connections
- Log entries in Windows Event Logs for RDP authentication from Python-based clients
- File artifacts like screenshot.png in temporary directories on the attacker's system
- Anomalous RDP sessions without corresponding Remote Desktop client usage

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/nc]] (for port forwarding RDP traffic)
- [[tools/Impacket]] (for RDP credential handling)

## References

- Official GitHub Repository: https://github.com/citronneur/rdpy
- RDP Protocol Documentation: https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rdp/
- Twisted Documentation: https://twistedmatrix.com/documents/

*Last updated: 2023-05-29T16:48:53.029709+00:00*
