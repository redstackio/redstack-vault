---
id: bf3d60e5-55bc-4d01-844e-2c8e9b50f9c0
type: tool
verified: true
created_at: '2019-08-28T21:17:33.354241+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - gui
  - pentest
  - reconnaissance
  - enumeration
  - scanning
url: 'https://github.com/t0mmt/sparta'
validated: true
---

# SPARTA

**Status**: Unverified

## Overview

SPARTA (Scans, Probes, Automation, Reconnaissance, and Tracking Analysis) is a Python-based GUI application designed to streamline the reconnaissance and enumeration phases of network penetration testing. It integrates multiple command-line tools into a user-friendly graphical interface, allowing testers to manage hosts, execute scans, and review outputs efficiently without repetitive command-line interactions.

## Description

SPARTA aids penetration testers by providing point-and-click access to essential tools such as Nmap, Nikto, DNS enumeration utilities, and more. The interface organizes hosts in a tree view, automates workflow progression (e.g., from port scanning to service enumeration), and consolidates tool outputs in dedicated tabs for easy analysis. This reduces setup time and focuses efforts on interpreting results, making it ideal for infrastructure assessments in controlled environments like red team engagements or vulnerability assessments.

## Features

- **Host Management**: Tree-based organization of targets with status tracking (e.g., scanned, vulnerable).
- **Integrated Tools**: Pre-configured access to Nmap, Masscan, Nikto, DNSRecon, and others via GUI buttons.
- **Automated Workflows**: Sequential execution of scans (e.g., auto-run service detection after port scan).
- **Output Consolidation**: Tabbed views for tool results, with search and export capabilities.
- **Customization**: Scriptable extensions and configurable tool paths.

## Installation

### Requirements

- Python 3.x
- Required dependencies: GTK3, PyGObject (for GUI), and various pentest tools (Nmap, etc.).
- Supported on Debian-based systems like Kali Linux or Ubuntu.

### Install Commands

```bash
# Clone the repository
sudo apt update
sudo apt install git python3-gi python3-gi-cairo gir1.2-gtk-3.0

# Install SPARTA
git clone https://github.com/t0mmt/sparta.git
cd sparta
chmod +x install.sh
sudo ./install.sh
```

On Kali Linux, SPARTA is available in the repositories:

```bash
sudo apt update
sudo apt install sparta
```

## Basic Usage

```bash
sparta
```

Or launch via the command generated for Python execution:

```bash
[[commands/sparta-launch-gui]]
```

### Common Options

SPARTA is primarily GUI-driven, but supports limited CLI flags for the launcher:

| Option | Description |
|--------|-------------|
| `--help` | Show available options |
| `--config PATH` | Load a custom configuration file |
| `-v, --verbose` | Enable verbose logging |

## Examples

### Example 1: Basic Usage

Launch SPARTA and add a target host:

1. Run `sparta` to open the GUI.
2. Right-click in the host tree and select "Add Host".
3. Enter the target IP (e.g., 192.168.1.100).
4. Click "Nmap" to initiate a port scan.

### Example 2: Advanced Usage

Automate a full recon workflow:

1. Add multiple hosts from a file (File > Import Hosts).
2. Select hosts and run initial discovery scan.
3. Upon completion, use the "Auto" button to progress to service enumeration and web scanning.
4. Review consolidated outputs in the Results tab.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning
- [[Active Scanning]] Active Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- **Process Monitoring**: Look for `python3 sparta.py` or `sparta` processes on endpoints.
- **Network Traffic**: Increased outbound scanning traffic from the tester's machine (e.g., SYN scans from Nmap integration).
- **File Artifacts**: Presence of SPARTA installation directory (`/opt/sparta` or `~/.sparta`) and log files.
- **GUI Activity**: Window titles or clipboard data containing SPARTA-related strings during live sessions.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Nmap]]
- [[tools/Nikto]]
- [[tools/DNSRecon]]

## References

- Official GitHub Repository: https://github.com/t0mmt/sparta
- Kali Tools Documentation: https://www.kali.org/tools/sparta
- Original Paper/Author Resources: Search for "SPARTA pentest GUI" for community guides.
