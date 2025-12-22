---
id: c8d95ec3-891f-41b5-af83-07d34cd1783e
type: tool
verified: true
created_at: '2019-08-28T21:17:35.657905+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
tags:
  - wireless
  - decryption
  - aircrack-ng
  - wep
  - wpa
  - pcap
url: 'https://www.aircrack-ng.org/doku.php?id=airdecap-ng'
validated: true
---

# Airdecap-ng and Airdecloak-ng

**Status**: Unverified

## Overview

Airdecap-ng and airdecloak-ng are utilities from the Aircrack-ng suite used in wireless security testing. Airdecap-ng decrypts WEP, WPA, and WPA2 capture files or strips wireless headers from unencrypted captures, producing a decrypted or cleaned output file. Airdecloak-ng specifically removes WEP cloaking from pcap files by analyzing and filtering packets from a target network to identify and uncloaked disguised traffic. These tools are commonly used in penetration testing for processing captured wireless traffic to extract plaintext data or prepare files for further analysis like cracking handshakes.

## Description

Airdecap-ng processes captured wireless packets to decrypt encrypted traffic using provided keys or passphrases, or to remove 802.11 headers from unencrypted captures, converting them to standard Ethernet frames for tools like Wireshark. It supports WEP (using a WEP key), WPA/WPA2 (using the ESSID and passphrase to derive the key), and outputs a new file with the '-dec.cap' suffix. Airdecloak-ng focuses on WEP cloaking detection and removal, where attackers hide data in unused IVs or other fields. It reads pcap files, selects packets by BSSID or ESSID, classifies them (unknown, uncloaked, potentially cloaked, cloaked), and applies user-specified filters in sequence to update statuses, ultimately outputting an uncloaked pcap file. These tools aid in post-capture analysis during wireless assessments, such as after using airodump-ng to capture traffic.

## Features

- **Airdecap-ng**:
  - Decryption of WEP/WPA/WPA2 captures using keys or passphrases.
  - Stripping of wireless headers from unencrypted captures.
  - Output in standard pcap format compatible with analysis tools.
  - Support for multiple input files.

- **Airdecloak-ng**:
  - Packet selection by BSSID, ESSID, or channel.
  - Classification of packets for cloaking status.
  - Sequential filter application (e.g., IV-based, sequence number checks).
  - Output of filtered, uncloaked pcap files.

## Installation

### Requirements

- Linux environment (Kali Linux recommended).
- Aircrack-ng suite dependencies (libpcap, etc.).

### Install Commands

```bash
# On Kali Linux (pre-installed)
sudo apt update && sudo apt install aircrack-ng

# On Ubuntu
sudo apt update && sudo apt install aircrack-ng

# From source (optional)
git clone https://github.com/aircrack-ng/aircrack-ng
git checkout master
make && sudo make install
```

## Basic Usage

```bash
airdecap-ng --help
airdecloak-ng --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v, --verbose` | Enable verbose output for debugging |
| `-e ESSID` (airdecap-ng) | Specify network ESSID for WPA decryption |
| `-p KEY` (airdecap-ng) | Provide WEP key for decryption |
| `-b BSSID` (airdecloak-ng) | Filter packets by BSSID |
| `-f FILTER` (airdecloak-ng) | Apply specific uncloaking filter |

## Examples

### Example 1: Basic Usage (Airdecap-ng WEP Decryption)

```bash
airdecap-ng -p 0123456789ABCDEFFEDCBA0987654321 capture.cap
```

This decrypts a WEP capture using the provided hex key and outputs 'capture-dec.cap'.

### Example 2: Advanced Usage (Airdecloak-ng with BSSID Filter)

```bash
airdecloak-ng -i capture.pcap -o uncloaked.pcap -b AA:BB:CC:DD:EE:FF -f iv_filter
```

This processes a pcap file, filters by BSSID, applies an IV-based uncloaking filter, and saves the result.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Credentials in Files]] Password Policy Discovery (for wireless credential cracking workflows)
- [[Active Scanning]] Active Scanning (processing captured wireless traffic)

### Tactics

- [[Initial Access]] Initial Access (wireless network entry via decrypted captures)
- [[Discovery]] Discovery (analyzing network traffic post-capture)

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for 'airdecap-ng' or 'airdecloak-ng' executions on systems with packet captures.
- File system artifacts: Presence of '-dec.cap' files or modified pcaps in working directories.
- Network logs showing wireless capture tools (e.g., airodump-ng) followed by decryption attempts.
- IDS alerts on unusual pcap processing or key derivation activities.

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

- Official Aircrack-ng Documentation: https://www.aircrack-ng.org/
- Airdecap-ng Man Page: https://www.aircrack-ng.org/doku.php?id=airdecap-ng
- Airdecloak-ng Man Page: https://www.aircrack-ng.org/doku.php?id=airdecloak-ng
