---
id: d372ad9b-cade-438e-a840-bc0f32460dbc
type: tool
verified: true
description: >-
  Proxy-aware C2 framework written in PowerShell for red teaming,
  post-exploitation, and lateral movement.
url: 'https://github.com/nettitude/PoshC2'
tags:
  - c2
  - powershell
  - red-team
  - post-exploitation
  - lateral-movement
platforms:
  - Windows
  - Linux
commands:
  - '[[commands/poshc2-start-server]]'
  - '[[commands/poshc2-generate-implant]]'
  - '[[commands/poshc2-client-interact]]'
created_at: '2019-08-28T21:17:32.968798+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
validated: true
---

# PoshC2

**Status**: Verified

## Overview

PoshC2 is a proxy-aware command and control (C2) framework designed specifically for penetration testing and red team operations. Written entirely in PowerShell, it facilitates post-exploitation activities, lateral movement, and evasion of common defenses on Windows environments. It supports HTTP/HTTPS communication with built-in proxy support, making it suitable for use behind corporate firewalls.

## Description

PoshC2 provides a modular infrastructure for managing implants (payloads) on compromised hosts. It includes a server component for handling C2 communications, a client for interacting with implants, and tools for generating obfuscated payloads. Key use cases include maintaining persistence, executing modules for privilege escalation, credential dumping, and data exfiltration while minimizing detection through traffic obfuscation and jittered beacons.

## Features

- **Proxy Awareness**: Supports SOCKS and HTTP proxies for evading network restrictions.
- **PowerShell-Based**: All payloads and modules are in PowerShell, leveraging .NET for advanced functionality.
- **Modular Design**: Extensive library of pre-built modules for common post-exploitation tasks like keylogging, screenshot capture, and Mimikatz integration.
- **Evasion Techniques**: Implant obfuscation, domain fronting, and randomized communication patterns.
- **Cross-Platform Server**: Server runs on Linux or Windows, with implants targeting Windows hosts.

## Installation

### Requirements

- Python 3.x (for server components)
- PostgreSQL database (for storing implant data)
- Git for cloning the repository
- Supported on Kali Linux, Ubuntu, or Windows

### Install Commands

```bash
# Clone the repository
git clone https://github.com/nettitude/PoshC2.git
cd PoshC2

# Install Python dependencies
pip3 install -r requirements.txt

# Setup the database (PostgreSQL must be running)
python3 Setup-Database.py

# Configure the server (edit Config.yml for payloads, domains, etc.)
```

After installation, customize the configuration files in the PoshC2 directory, such as specifying C2 domains, user agents, and jitter settings.

## Basic Usage

```bash
python3 server.py
```

This starts the PoshC2 server, which listens for incoming implant connections. Use the client to interact with connected implants.

### Common Options

| Option | Description |
|--------|-------------|
| `--help` | Show help message |
| `-v` | Verbose logging |
| `--config` | Specify custom config file |

## Examples

### Example 1: Basic Usage

Start the server:

```bash
python3 server.py
```

Expected output: Server initialization messages, including database connection and listener setup.

### Example 2: Advanced Usage

Generate an implant and deploy it:

First, generate payload using [[commands/poshc2-generate-implant]]:

```bash
python3 PoshC2/Client.py --implant
```

Then interact with connected implants using [[commands/poshc2-client-interact]]:

```bash
python3 PoshC2/Client.py
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Standard Application Layer Protocol]] Application Layer Protocol (C2 over HTTP/HTTPS)
- [[PowerShell]] PowerShell (Implant execution)
- [[Protocol Tunneling]] Protocol Hijacking (Proxy support)

### Tactics

- [[Command and Control]] Command and Control
- [[Privilege Escalation]] Privilege Escalation
- [[Lateral Movement]] Lateral Movement

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual PowerShell processes with network connections to C2 domains.
- Base64-encoded PowerShell scripts in process arguments.
- Anomalous HTTP/HTTPS traffic with randomized user agents or jittered intervals.
- PostgreSQL queries related to implant tracking (if server is on-prem).
- Monitor for downloads of PoshC2 payloads via AMSI or EDR tools.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Covenant]]
- [[tools/Empire]]
- [[Cobalt-Strike]]

## References

- Official GitHub: https://github.com/nettitude/PoshC2
- Documentation: https://poshc2.readthedocs.io/
- Blog posts on evasion techniques from Nettitude.
