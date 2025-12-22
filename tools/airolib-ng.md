---
id: ac46f5e8-7e8f-4b15-88cd-99562b1372d7
name: airolib-ng
type: tool
verified: true
created_at: '2019-08-28T21:17:42.764940+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - wireless
  - wpa-cracking
  - pmk
  - aircrack-ng
url: 'https://www.aircrack-ng.org/doku.php?id=airolib-ng'
validated: true
---

# airolib-ng

**Status**: Unverified

## Overview

airolib-ng is a tool from the aircrack-ng suite designed for efficient WPA/WPA2 cracking. It manages ESSID and password lists, precomputes Pairwise Master Keys (PMKs) offline, and tests them against captured handshakes, significantly speeding up dictionary attacks on WiFi networks.

## Description

airolib-ng uses a lightweight SQLite3 database to store imported ESSIDs, passwords, and computed PMKs. This allows for batch precomputation of keys, reducing the time needed for cracking WPA/WPA2 handshakes with tools like aircrack-ng or cowpatty. It's particularly useful in wireless penetration testing for handling large wordlists without recomputing PMKs repeatedly. The tool supports importing from text files and integrates seamlessly with other aircrack-ng components for full WiFi assessment workflows.

## Features

- ESSID and password list import into SQLite database
- Batch PMK precomputation for offline storage
- Handshake testing against precomputed keys
- Support for large datasets with progress tracking
- Integration with aircrack-ng ecosystem for WPA/WPA2 cracking

## Installation

### Requirements

- Linux environment (Kali Linux recommended)
- aircrack-ng suite (airolib-ng is included)
- SQLite3 (usually pre-installed)

### Install Commands

```bash
# On Kali Linux: Pre-installed with aircrack-ng
# On Ubuntu/Debian:
apt update
apt install aircrack-ng

# Verify installation
airolib-ng --help
```

## Basic Usage

```bash
airolib-ng --help
```

### Common Options

| Option | Description |
|--------|-------------|
| --help, -h | Show help message and usage |
| --batch | Compute PMKs for all ESSID/password pairs |
| --import | Import data (essid or passwd) into database |
| --test | Test database against a PCAP handshake file |

## Examples

### Example 1: Basic Usage

Create a database and import data:

```bash
airolib-ng wpa_test.db  # Create database
airolib-ng wpa_test.db --import essid essids.txt
airolib-ng wpa_test.db --import passwd rockyou.txt
```

### Example 2: Advanced Usage

Precompute and test:

```bash
airolib-ng wpa_test.db --batch  # Compute PMKs
airolib-ng wpa_test.db --test   # Test against handshake.pcap (prompted)
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning (for wireless network discovery leading to cracking)
- [[Credentials in Files]] Password Cracking (WPA/WPA2 key recovery)

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Processes named airolib-ng or sqlite3 with database files in /tmp or working directories
- High CPU/disk usage during batch PMK computation on assessment machines
- Presence of .db files with wireless-related imports (e.g., via file forensics)
- Network captures showing aircrack-ng suite tools in use

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
- [[tools/airmon-ng]]
- [[tools/aireplay-ng]]

## References

- Official aircrack-ng documentation: https://www.aircrack-ng.org/
- airolib-ng specific guide: https://www.aircrack-ng.org/doku.php?id=airolib-ng
