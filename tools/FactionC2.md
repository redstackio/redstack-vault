---
id: 6dc7196c-6617-4db3-8e57-609eda71a691
type: tool
verified: true
created_at: '2019-08-28T21:17:39.941116+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - c2
  - redteam
  - websockets
  - post-exploitation
url: 'https://github.com/FactionC2/FactionC2'
validated: true
---

# FactionC2

**Status**: Unverified

## Overview

FactionC2 is a post-exploitation Command and Control (C2) framework designed for red team operations. It leverages a websockets-based API for low-latency communication between the server and deployed agents, supporting multiple transport layers for evasion and reliability. Commonly used for maintaining persistence, executing commands, and exfiltrating data in simulated attacks.

## Description

FactionC2 provides a flexible C2 infrastructure with a RESTful API backend powered by websockets, allowing operators to interact with agents across diverse environments. Agents can be generated in formats like PowerShell, EXE, or DLL, and support features such as tasking, file transfer, and screenshot capture. The framework emphasizes modularity, with customizable profiles for different operational needs, making it suitable for advanced persistent threat simulations.

## Features

- Feature 1: Websockets-based communication for real-time agent control and reduced latency.
- Feature 2: Multi-transport support (HTTP, HTTPS, DNS) for bypassing network restrictions.
- Feature 3: Agent generation in multiple formats (PowerShell, EXE, DLL, raw shellcode).
- Feature 4: Built-in evasion techniques like domain fronting and jittered beacons.
- Feature 5: REST API for integration with external tools and automation scripts.

## Installation

### Requirements

- Python 3.6+
- Git
- pip and virtualenv recommended

### Install Commands

```bash
# Clone the repository
git clone https://github.com/FactionC2/FactionC2.git
cd FactionC2

# Install dependencies
pip3 install -r requirements.txt

# For Kali/Ubuntu
sudo apt update && sudo apt install python3-pip git
```

## Basic Usage

```bash
python3 faction.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and options |
| `--rest-host` | Bind REST API to specific host (default: 127.0.0.1) |
| `--rest-port` | Bind REST API to specific port (default: 4743) |
| `--profile` | Load a custom profile JSON for transports and settings |
| `--debug` | Enable debug logging |

## Examples

### Example 1: Basic Usage

Start the server on all interfaces:

```bash
python3 faction.py --rest-host 0.0.0.0 --rest-port 4743
```

### Example 2: Advanced Usage

Start with a custom profile:

```bash
python3 faction.py --rest-host 0.0.0.0 --rest-port 4743 --profile my_profile.json
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Standard Application Layer Protocol]] Application Layer Protocol
- [[Non-Standard Port]] Non-Standard Port
- [[Standard Non-Application Layer Protocol]] Non-Application Layer Protocol

### Tactics

- [[Command and Control]] Command and Control
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual outbound websocket traffic on non-standard ports (e.g., 4743).
- Detection method 2: Presence of Python processes with network connections to C2 domains.
- Detection method 3: Agent artifacts like encoded PowerShell scripts in memory or temporary files.
- Detection method 4: API endpoint patterns in proxy logs (/api/v1/agents).

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

## References

- Official GitHub: https://github.com/FactionC2/FactionC2
- Documentation: https://factionc2.readthedocs.io/
- Related resources: Red Team C2 Frameworks comparison articles
