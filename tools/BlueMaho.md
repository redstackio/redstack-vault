---
id: e55e0452-c57a-4a33-a76f-c648331b47fd
type: tool
verified: true
created_at: '2019-08-28T21:17:27.351126+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - bluetooth
  - wireless
  - vulnerability-testing
  - gui
url: 'https://github.com/gsf/bluemaho'
commands:
  - '[[commands/bluemaho-launch-gui]]'
validated: true
---

# BlueMaho

**Status**: Unverified

## Overview

BlueMaho is an open-source GUI frontend for a suite of Bluetooth security testing tools. Written in Python and using wxPython, it enables testers to assess Bluetooth devices for known and unknown vulnerabilities through an intuitive interface. Common use cases include device discovery, vulnerability scanning, and exploit execution in wireless penetration testing scenarios.

## Description

BlueMaho serves as a graphical shell for various Bluetooth analysis and exploitation tools. It is freeware and open-source, allowing users to scan for devices, retrieve detailed information (SDP records, vendor details), track device movements, perform continuous loop scans, set up alerts for new devices, and execute tests for vulnerabilities. The tool supports using multiple Bluetooth dongles for simultaneous scanning and exploitation, file transfers, modification of local HCI device properties (name, class, mode, BD_ADDR), database storage of results, and generation of statistics on unique devices, vendors, and services. It also includes customizable themes for user preference.

## Features

- **Device Scanning**: Discover nearby Bluetooth devices with advanced info like SDP records and vendor identification.
- **Device Tracking**: Monitor device appearances, name changes, and sighting frequency.
- **Loop Scanning**: Continuous scanning to identify online devices in real-time.
- **Alerts**: Audio notifications for newly discovered devices; customizable on-new-device commands.
- **Multi-Dongle Support**: Use separate adapters for scanning and tool execution.
- **File Operations**: Send files to remote devices.
- **Device Modification**: Alter local HCI device name, class, mode, and BD_ADDR.
- **Data Management**: Save scan results to a database and generate statistics (e.g., unique devices by time, vendors, services).
- **Vulnerability Testing**: Test remote devices for known exploits and unknown vulnerabilities.
- **Customization**: Theme support for interface personalization.

## Installation

### Requirements

- Python 2.7 or 3.x (tested on Python 2)
- wxPython (GUI library)
- Bluetooth adapter/dongle
- Additional dependencies: PyBluez or similar for Bluetooth stack interaction (may vary by OS)

### Install Commands

For Kali Linux or Ubuntu:

```bash
# Clone the repository (assuming it's available via git)
git clone https://github.com/gsf/bluemaho.git
cd bluemaho

# Install wxPython (if not pre-installed on Kali)
sudo apt update
sudo apt install python-wxgtk4.0  # For Python 3; use python-wxtools for Python 2

# Install other Python dependencies if specified in requirements
pip install -r requirements.txt  # If a requirements file exists; otherwise manual

# Ensure Bluetooth is enabled
sudo hciconfig hci0 up
```

For Windows:

- Install Python from python.org
- Install wxPython via pip: `pip install wxPython`
- Download and extract the BlueMaho source
- Run with `python bluemaho.py`

For macOS:

- Install Python via Homebrew: `brew install python`
- Install wxPython: `pip install wxPython`
- Clone/extract source and run `python bluemaho.py`

Note: BlueMaho is an older tool (circa 2000s); compatibility with modern Bluetooth stacks (e.g., BlueZ 5+) may require patches. Test in a virtual environment.

## Basic Usage

```bash
tool-name --help
```

BlueMaho is primarily GUI-driven; launch it and interact via the interface.

### Common Options

| Option | Description |
|--------|-------------|
| None (GUI) | No CLI options; all configuration done in the GUI windows for scans, tools, and exploits. |
| -h, --help | If supported, shows basic help (check source for CLI flags). |

## Examples

### Example 1: Basic Usage

Launch the GUI:

```bash
python bluemaho.py
```

Once open, select "Scan" to start device discovery.

### Example 2: Advanced Usage

For loop scanning with alerts:

1. Launch the GUI using [[commands/bluemaho-launch-gui]].
2. In the interface, enable loop scan and set audio alerts.
3. Specify a command to run on new device detection (e.g., a custom script).

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Sniffing]] Network Sniffing (for Bluetooth device discovery and tracking)
- [[Active Scanning]] Active Scanning (Bluetooth enumeration and vulnerability probing)

### Tactics

- [[Reconnaissance]] Reconnaissance (device discovery and service enumeration)
- [[Initial Access]] Initial Access (via Bluetooth pairing/exploits)

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for `python bluemaho.py` or wxPython processes.
- Bluetooth traffic anomalies: unusual inquiry packets or SDP requests.
- File system artifacts: BlueMaho database files or log outputs in the tool directory.
- Network/Bluetooth logs showing device scanning patterns from the attacker's adapter.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Hcitool]] (Bluetooth HCI utilities)
- [[tools/BlueHydra]] (Bluetooth device tracking)

## References

- Official repository: https://github.com/gsf/bluemaho
- wxPython documentation: https://wxpython.org
- Bluetooth security resources: Bluetooth SIG specifications
