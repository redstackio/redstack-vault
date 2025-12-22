---
id: a2d2a55c-1752-4023-9276-3821b59b5644
type: tool
verified: true
created_at: '2019-08-28T21:17:28.140649+00:00'
updated_at: '2023-10-01T12:00:00+00:00'
platforms:
  - Linux
tags:
  - wireless
  - cracking
  - wpa
  - psk
  - dictionary-attack
url: 'http://www.wirelessdefence.org'
commands:
  - '[[commands/cowpatty-generate-pmk]]'
  - '[[commands/cowpatty-dictionary-attack]]'
validated: true
---

# cowpatty

**Status**: Unverified

## Overview

Cowpatty is a specialized tool for performing offline dictionary attacks against WPA/WPA2 networks that use Pre-Shared Key (PSK) authentication, commonly known as WPA-Personal. It is particularly useful in penetration testing wireless networks where enterprise setups opt for simpler PSK mechanisms over full WPA-Enterprise with RADIUS and certificates. The tool excels when paired with precomputed Pairwise Master Key (PMK) files, enabling faster cracking of captured handshakes.

## Description

Cowpatty implements an efficient dictionary-based brute-force attack on WPA/WPA2 PSK handshakes captured using tools like airodump-ng. By precomputing PMKs for a given SSID and passphrase list, it avoids computationally expensive operations during the attack phase, making it suitable for assessing weak passwords in Wi-Fi environments. It supports standard capture files from aircrack-ng suite and outputs cracked passphrases if found within the dictionary. This tool is ideal for red team exercises targeting wireless access points in corporate or home networks.

## Features

- Offline dictionary attacks on WPA/WPA2-PSK handshakes
- PMK precomputation to accelerate cracking (via genpmk utility)
- Support for large wordlists and rainbow table integration
- Progress reporting and speed optimization for repeated SSID attacks
- Compatibility with aircrack-ng capture formats (.cap files)

## Installation

### Requirements

- Linux-based system (e.g., Kali Linux, Ubuntu)
- Build essentials: gcc, make
- Optional: Large wordlists for effective cracking

### Install Commands

On Kali Linux (pre-compiled package available):

```bash
sudo apt update
sudo apt install cowpatty
```

For manual compilation from source (recommended for latest features):

```bash
# Clone from GitHub mirror (original from wirelessdefence.org)
git clone https://github.com/joswr1ght/cowpatty.git
cd cowpatty
make
sudo make install
```

Verify installation:

```bash
cowpatty --help
genpmk --help
```

## Basic Usage

```bash
cowpatty --help
```

This displays available options, including file paths, SSID specification, and PMK usage.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -v | Enable verbose output for debugging |
| -s SSID | Specify the target network SSID |
| -f FILE | Input capture file (.cap) |
| -d DICT | Dictionary wordlist file |
| -S PMKFILE | Use precomputed PMK file |

## Examples

### Example 1: Basic Usage

Perform a dictionary attack on a captured handshake:

```bash
cowpatty -f capture.cap -d wordlist.txt -s TargetSSID -o output.txt
```

### Example 2: Advanced Usage

Use a precomputed PMK for faster cracking:

```bash
cowpatty -f enterprise.cap -d rockyou.txt -s CorporateNet -S corporate.pmk -o cracked_pass.txt
```

For PMK generation, see [[commands/cowpatty-generate-pmk]].

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Brute Force]] Brute Force (dictionary attacks on wireless credentials)
- [[Unsecured Credentials]] Unsecured Credentials (extracting PSK from handshakes)

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of cowpatty or genpmk binaries in process lists (ps aux | grep cowpatty)
- High CPU usage during PMK computation or cracking on assessment machines
- Network captures showing airodump-ng or similar tools followed by offline analysis
- File artifacts: .pmk files, temporary wordlist processing logs
- Wireless monitoring: Anomalous deauth floods or handshake captures preceding use

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/aircrack-ng]] (for capturing handshakes)
- [[tools/Hashcat]] (alternative GPU-accelerated cracking)

## References

- Official site: http://www.wirelessdefence.org
- GitHub mirror: https://github.com/joswr1ght/cowpatty
- Aircrack-ng documentation for capture integration
