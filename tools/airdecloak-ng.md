---
id: 3384ec59-3087-4c41-bee7-6bbc2466f02d
type: tool
verified: true
created_at: '2019-08-28T21:17:25.731739+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - wireless
  - wep
  - decloak
  - aircrack-ng
url: 'https://www.aircrack-ng.org/doku.php?id=airdecloak-ng'
validated: true
---

# airdecloak-ng

**Status**: Unverified

## Overview

airdecloak-ng is a utility from the Aircrack-ng suite designed to remove WEP (Wired Equivalent Privacy) cloaking from PCAP capture files. It processes wireless packet captures to identify and decloak encrypted WEP traffic, making the underlying data accessible for further analysis or cracking. Commonly used in wireless penetration testing to preprocess captures for tools like aircrack-ng.

## Description

airdecloak-ng reads an input PCAP file containing wireless traffic, filters packets based on a specified ESSID (network name), and classifies them into categories such as unknown, uncloaked, potentially cloaked, or cloaked. It then applies user-defined filters in sequence to decloak WEP-encrypted packets, often using a dictionary of potential keys. The tool outputs a processed file or stream with cloaking removed, enabling clearer analysis of network activity. It is particularly useful for handling obfuscated WEP implementations that hide packet contents to evade detection.

Note: This tool focuses on decloaking; for full WEP/WPA decryption, pair it with airdecap-ng.

## Features

- ESSID-based packet filtering to target specific networks
- Packet classification (unknown, uncloaked, cloaked)
- Sequential filter application for progressive decloaking
- Dictionary support for key-based decloaking
- Integration with Aircrack-ng ecosystem for wireless auditing
- Verbose logging for debugging filter effectiveness

## Installation

### Requirements

- Linux kernel with wireless support
- Aircrack-ng suite dependencies (libpcap, etc.)

### Install Commands

airdecloak-ng is part of the Aircrack-ng suite.

```bash
# On Kali Linux (pre-installed)
sudo apt update && sudo apt install aircrack-ng

# On Ubuntu
sudo apt update && sudo apt install aircrack-ng

# From source
sudo apt install libpcap-dev
wget https://download.aircrack-ng.org/aircrack-ng-1.7.tar.gz
 tar -xzf aircrack-ng-1.7.tar.gz
 cd aircrack-ng-1.7
 make
 sudo make install
```

## Basic Usage

```bash
airdecloak-ng --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and exit |
| -v, --verbose | Enable verbose output for detailed processing logs |
| -e <essid> | Filter packets by ESSID |
| -d <dictfile> | Use dictionary file for key-based decloaking |

## Examples

### Example 1: Basic Usage

```bash
airdecloak-ng -e "TargetNetwork" -d /usr/share/wordlists/wepkeys.dic input.pcap
```

This decloaks WEP packets from "TargetNetwork" using the specified dictionary and processes input.pcap.

### Example 2: Advanced Usage

```bash
airdecloak-ng -e "TargetNetwork" -d /path/to/custom.dic -v input.pcap -o output-decloaked.pcap
```

Processes with verbose output and saves to a new PCAP file.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Steal Web Session Cookie]] Steal Web Session Cookie (adapted for wireless session hijacking post-decloaking)
- [[Forge Web Credentials]] Forge Web Credentials (via recovered WEP keys)

### Tactics

- [[Initial Access]] Initial Access (wireless network entry)
- [[Discovery]] Discovery (network mapping via decloaked traffic)

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for airdecloak-ng execution on systems with PCAP files
- File system changes: Creation of -decloaked.pcap or similar output files
- Network analysis: Unusual processing of wireless captures in logs
- Dependency checks: Aircrack-ng suite installed on non-standard systems

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
- [[tools/aireplay-ng]]
- [[tools/airdecap-ng]]

## References

- Official Aircrack-ng Documentation: https://www.aircrack-ng.org/doku.php?id=airdecloak-ng
- GitHub Repository: https://github.com/aircrack-ng/aircrack-ng
