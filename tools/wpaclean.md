---
id: 5aa23035-485d-4873-b571-8708c8dc3611
name: wpaclean
type: tool
verified: true
created_at: '2019-08-28T21:17:24.430453+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - wireless
  - wpa
  - aircrack-ng
  - packet-processing
url: 'https://www.aircrack-ng.org/doku.php?id=wpaclean'
validated: true
---

# wpaclean

**Status**: Unverified

## Overview

wpaclean is a lightweight utility from the Aircrack-ng suite designed for processing wireless packet captures. It filters pcap files to isolate 4-way handshake packets and beacon frames, which are essential for cracking WPA/WPA2 pre-shared keys (PSKs). This tool is commonly used in wireless penetration testing to prepare capture data for offline analysis and cracking with tools like aircrack-ng or hashcat.

## Description

wpaclean scans input pcap files from tools like airodump-ng and removes irrelevant packets, retaining only those involved in the authentication handshake between clients and access points. This reduces file size significantly (often by 90% or more) and eliminates noise, making subsequent cracking more efficient. It supports standard pcap formats and is particularly useful in scenarios where large captures from wardriving or targeted deauth attacks need streamlining. wpaclean does not perform cracking itself but serves as a preprocessing step in WiFi attack workflows.

## Features

- **Handshake Isolation**: Automatically detects and extracts 4-way EAPOL handshake packets.
- **Beacon Retention**: Keeps beacon frames for access point identification and ESSID details.
- **File Optimization**: Reduces pcap size by discarding non-relevant traffic like data frames or probes.
- **Lightweight Processing**: Fast execution on large captures without requiring additional dependencies.
- **Integration**: Seamlessly works with other Aircrack-ng tools for end-to-end WiFi auditing.

## Installation

### Requirements

- Linux environment with wireless monitoring support (e.g., compatible WiFi adapter).
- Aircrack-ng suite (wpaclean is included).

### Install Commands

On Kali Linux (pre-installed):

```bash
# Already available, but update if needed
apt update && apt install aircrack-ng
```

On Ubuntu/Debian:

```bash
sudo apt update
sudo apt install aircrack-ng
```

On other Linux distributions:

```bash
# From source
wget https://download.aircrack-ng.org/aircrack-ng-1.7.tar.gz
 tar -xzf aircrack-ng-1.7.tar.gz
 cd aircrack-ng-1.7
 make && sudo make install
```

## Basic Usage

```bash
wpaclean --help
```

This displays available options, primarily specifying input and output files.

### Common Options

| Option | Description |
|--------|-------------|
| (No flags) | Basic filtering; options are minimal, focused on file I/O. |

## Examples

### Example 1: Basic Usage

Filter a capture from airodump-ng:

```bash
wpaclean filtered.cap raw_capture.cap
```

This creates 'filtered.cap' containing only handshakes and beacons from 'raw_capture.cap'.

### Example 2: Advanced Usage

Process multiple captures or pipe output (though wpaclean uses files):

```bash
wpaclean output.cap input1.cap input2.cap  # Note: wpaclean takes one input
```

For multiple files, run sequentially or use scripts.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Steal Web Session Cookie]] Steal Web Session Cookie (adapted for wireless session hijacking via handshakes)
- [[Modify Authentication Process]] Modify Authentication Process (WPA handshake manipulation)

### Tactics

- [[Initial Access]] Initial Access (Wireless network compromise)
- [[Credential Access]] Credential Access (PSK cracking preparation)

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of filtered pcap files with only EAPOL/beacon packets in forensic analysis.
- Aircrack-ng suite processes running on attacker machines (e.g., via process monitoring).
- Unusual file I/O patterns involving wireless captures in logs.
- Network defenders can monitor for airodump-ng captures preceding cracking attempts.

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
- [[tools/aireplay-ng]]

## References

- Official Aircrack-ng Documentation: https://www.aircrack-ng.org/doku.php?id=wpaclean
- Aircrack-ng GitHub: https://github.com/aircrack-ng/aircrack-ng
