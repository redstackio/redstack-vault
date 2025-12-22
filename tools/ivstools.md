---
id: d0d88eca-238a-4b2b-a7a9-2e80eaecffb0
type: tool
verified: true
created_at: '2019-08-28T21:17:19.894739+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - wireless
  - aircrack-ng
  - packet-manipulation
url: 'https://www.aircrack-ng.org/doku.php?id=ivstools'
validated: true
---

# ivstools

**Status**: Unverified

## Overview

ivstools is a command-line utility included in the aircrack-ng suite, designed for manipulating IVS (Interleaved Value Stream) files. These files store data from wireless packet injection and capture operations, such as those performed by aireplay-ng or airodump-ng. Common use cases include merging multiple IVS files from fragmented sessions and converting them to standard formats like PCAP for broader compatibility and analysis in offensive security testing, particularly in Wi-Fi penetration testing and WEP/WPA cracking workflows.

## Description

ivstools provides essential file handling for wireless attack tools in aircrack-ng. It supports merging IVS files to consolidate data from multiple captures and converting IVS to PCAP/CAP formats, enabling integration with analysis tools like Wireshark or further processing in aircrack-ng for key recovery. It is lightweight, requiring no additional dependencies beyond the aircrack-ng installation, and is typically used in post-capture phases of wireless assessments to prepare data for cracking or forensic review.

## Features

- **File Merging**: Combine multiple IVS files into a single file for unified processing.
- **Format Conversion**: Convert IVS to PCAP/CAP formats for compatibility with standard network analysis tools.
- **Simple Syntax**: Straightforward command-line interface with minimal options, focused on core IVS manipulation.
- **Integration**: Seamlessly works within aircrack-ng ecosystem for Wi-Fi security testing.

## Installation

### Requirements

- Linux environment (Kali Linux recommended for pentesting).
- aircrack-ng package (ivstools is bundled within it).

### Install Commands

```bash
# On Kali Linux (pre-installed)
sudo apt update && sudo apt install aircrack-ng

# On Ubuntu
sudo apt update && sudo apt install aircrack-ng

# From source (optional)
git clone https://github.com/aircrack-ng/aircrack-ng.git
cd aircrack-ng
make && sudo make install
```

## Basic Usage

```bash
ivstools --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -o, --output | Specify output file (for merging).
| (No flag) | For conversion, simply provide input and output filenames; extension determines format (e.g., .cap for PCAP). |

## Examples

### Example 1: Basic Usage

Merge IVS files:

```bash
ivstools -o merged.ivs file1.ivs file2.ivs
```

### Example 2: Advanced Usage

Convert IVS to CAP:

```bash
ivstools input.ivs output.cap
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Sniffing]] Network Sniffing (for post-capture processing in wireless reconnaissance and lateral movement via Wi-Fi).
- [[Archive Collected Data]] Archive Collected Data (merging files as part of data preparation for exfiltration or analysis).

### Tactics

- [[Impact]] Network Attacks
- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of aircrack-ng processes or IVS/CAP files in temporary directories.
- Network monitoring for wireless interface manipulations (e.g., via monitor mode).
- File system scans for .ivs or newly created .cap files with timestamps matching capture activities.
- Logs from package managers showing aircrack-ng installation on non-standard systems.

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
- [[tools/Wireshark]]

## References

- Official aircrack-ng documentation: https://www.aircrack-ng.org/
- IVS file format details: https://www.aircrack-ng.org/doku.php?id=ivstools
