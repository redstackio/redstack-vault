---
id: 489b7109-f2f3-4e0a-9267-0310387927f6
name: airdecap-ng
type: tool
verified: true
created_at: '2019-08-28T21:17:28.370387+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - wireless
  - decryption
  - pcap
  - aircrack-ng
url: 'https://www.aircrack-ng.org/doku.php?id=airdecap-ng'
validated: true
---

# airdecap-ng

**Status**: Unverified

## Overview

airdecap-ng is a utility from the Aircrack-ng suite designed for decrypting WEP, WPA, and WPA2 encrypted wireless packet capture files. It can also strip 802.11 headers from unencrypted captures to convert them into standard pcap format compatible with other analysis tools like Wireshark. Commonly used in wireless penetration testing after capturing handshakes or traffic to recover plaintext data.

## Description

airdecap-ng processes .cap files obtained from tools like airodump-ng or tcpdump. For encrypted captures, it requires the network ESSID and passphrase to perform decryption. It outputs a new file with the suffix `-dec.cap` containing the decrypted or processed packets. This tool is essential for post-capture analysis in Wi-Fi security assessments, allowing testers to inspect application-layer traffic after cracking keys.

Note: airdecap-ng does not perform the cracking itself; it relies on pre-cracked keys or passwords. For WEP cloaking removal, use airdecloak-ng instead, which is a separate tool in the suite.

## Features

- Decryption of WEP, WPA, and WPA2 captures using provided keys
- Stripping of 802.11 headers and FCS (Frame Check Sequence) from unencrypted files
- Support for IV (Initialization Vector) extraction for WEP attacks
- Output in standard pcap format for compatibility with analysis tools
- Batch processing of multiple capture files

## Installation

### Requirements

- Linux kernel with wireless support
- libpcap development libraries
- Aircrack-ng suite dependencies (openssl, libssl-dev)

### Install Commands

airdecap-ng is part of the Aircrack-ng suite.

```bash
# On Kali Linux (pre-installed)
# No action needed

# On Ubuntu/Debian
sudo apt update
sudo apt install aircrack-ng

# On macOS (via Homebrew)
brew install aircrack-ng

# From source
wget https://download.aircrack-ng.org/aircrack-ng-1.7.tar.gz
tar -xzf aircrack-ng-1.7.tar.gz
cd aircrack-ng-1.7
make
sudo make install
```

## Basic Usage

```bash
airdecap-ng --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -e, --essid ESSID | Specify the wireless network ESSID |
| -p, --passphrase PSK | WPA/WPA2 pre-shared key |
| -w, --wepkey KEY | WEP key in hex or ASCII |
| -0 | Strip non-802.11 headers (no FCS) |
| -1 | Keep FCS in output |
| -o, --output FILE | Specify output file name |
| -h, --help | Show help message |
| -v, --verbose | Verbose output |

## Examples

### Example 1: Basic Usage (WPA Decryption)

Decrypt a WPA capture using ESSID and password:

```bash
airdecap-ng -e "TargetNetwork" -p "password123" wpa-capture.cap
```

This generates `wpa-capture-dec.cap` with decrypted packets.

### Example 2: Advanced Usage (Header Stripping)

Strip headers from an unencrypted capture:

```bash
airdecap-ng -0 unencrypted.cap -o stripped.pcap
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Credentials in Files]] Password Policy Discovery (for Wi-Fi PSK enumeration)
- [[Steal Web Session Cookie]] Steal Web Session Cookie (post-decryption traffic analysis)

### Tactics

- [[Credential Access]] Credential Access
- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- Execution of aircrack-ng binaries in process lists (e.g., via Sysmon or auditd)
- File creation patterns: .cap files being modified or new -dec.cap files appearing
- Network monitoring for wireless packet captures (high volume of 802.11 traffic)
- Log analysis for unusual pcap processing in security tools

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/airodump-ng]]
- [[tools/aircrack-ng]]
- [[tools/aireplay-ng]]

## References

- Official Aircrack-ng Documentation: https://www.aircrack-ng.org/doku.php?id=airdecap-ng
- Aircrack-ng GitHub: https://github.com/aircrack-ng/aircrack-ng
