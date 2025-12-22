---
id: b17eb553-04f6-4fb1-947e-2b8a920f07c7
type: tool
verified: true
created_at: '2019-08-28T21:17:38.196036+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - wireless
  - reconnaissance
  - oui
url: 'https://www.aircrack-ng.org/'
validated: true
---

# airodump-ng-oui-update

**Status**: Unverified

## Overview

airodump-ng-oui-update is a lightweight utility bundled with the aircrack-ng suite, designed specifically to fetch and update the Organizationally Unique Identifier (OUI) database from the IEEE. This database resolves the first three bytes (OUI) of MAC addresses to manufacturer names, enhancing the readability of wireless capture outputs in tools like airodump-ng, particularly when exporting to NetXML formats for further analysis.

It is commonly used in wireless security auditing to ensure accurate vendor identification during reconnaissance phases of penetration testing.

## Description

The tool automates the download of the IEEE OUI registry, which is a plain-text file listing MAC address prefixes and their corresponding manufacturers. Once updated, this data integrates seamlessly with airodump-ng, allowing for enriched packet captures where device vendors are automatically populated instead of showing raw MAC addresses. This is valuable for identifying device types in Wi-Fi networks, such as distinguishing between consumer routers, enterprise access points, or IoT devices.

Key capabilities include:
- Fetching the latest OUI list via HTTP from the IEEE website.
- Parsing and formatting the data into aircrack-ng's expected structure.
- Overwriting the local OUI file without manual intervention.

It does not perform any scanning or capturing itself but supports the broader wireless toolkit.

## Features

- Feature 1: Automatic download and parsing of IEEE OUI registry.
- Feature 2: Integration with aircrack-ng tools for vendor resolution in captures.
- Feature 3: Simple, non-interactive execution suitable for scripting in update routines.

## Installation

### Requirements

- Linux environment (Kali Linux recommended for pentesting).
- Internet connectivity for downloading the OUI list.
- aircrack-ng suite (this tool is included in it).

### Install Commands

On Kali Linux (pre-installed):

```bash
# Already available; verify with
which airodump-ng-oui-update
```

On Ubuntu/Debian:

```bash
sudo apt update
sudo apt install aircrack-ng
```

On other distributions, compile from source:

```bash
sudo apt install libssl-dev git build-essential
git clone https://github.com/aircrack-ng/aircrack-ng.git
cd aircrack-ng
make
sudo make install
```

## Basic Usage

```bash
airodump-ng-oui-update --help
```

(Note: This tool has no --help flag; it runs directly.)

### Common Options

| Option | Description |
|--------|-------------|
| None | Runs the update silently; outputs progress to stdout. |
| sudo | Use with elevated privileges for system-wide file updates. |

## Examples

### Example 1: Basic Usage

```bash
airodump-ng-oui-update
```

This fetches and installs the latest OUI list to the default path (typically /usr/share/aircrack-ng/oui.txt).

### Example 2: Advanced Usage

Integrate into a script for periodic updates:

```bash
#!/bin/bash
airodump-ng-oui-update
if [ $? -eq 0 ]; then
    echo "OUI updated successfully."
else
    echo "Update failed."
fi
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning (for wireless reconnaissance preparation).

### Tactics

- [[Reconnaissance]] Reconnaissance.

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Network traffic to ieee.org domains from security tools.
- Detection method 2: File modifications in /usr/share/aircrack-ng/oui.txt with recent timestamps.
- Detection method 3: Process listings showing airodump-ng-oui-update execution in audit logs.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/aircrack-ng]]
- [[tools/airodump-ng]]

## References

- Official documentation: https://www.aircrack-ng.org/doku.php?id=airodump-ng-oui-update
- Aircrack-ng GitHub: https://github.com/aircrack-ng/aircrack-ng
- IEEE OUI Registry: https://standards-oui.ieee.org/oui/oui.txt
