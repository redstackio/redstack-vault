---
id: 2b75b232-01b3-415d-ba59-13667c7ec87f
type: tool
verified: true
created_at: '2019-08-28T21:17:31.129720+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - wireless
  - credential-access
  - dictionary-attack
  - eap-md5
  - 802.1x
url: 'https://github.com/davidkilroy/eapmd5pass'
validated: true
---

# eapmd5pass

**Status**: Unverified

## Overview

Eapmd5pass is a specialized tool for exploiting the vulnerabilities in EAP-MD5 authentication, a legacy mechanism used in 802.1X wireless networks. It captures authentication exchanges either live from a monitor-mode interface or from pcap files and performs offline dictionary attacks to recover user credentials, exposing them to brute-force risks.

## Description

EAP-MD5 provides weak protection for user credentials in wireless authentication scenarios, allowing attackers to perform offline dictionary attacks. The tool monitors network traffic for EAP-MD5 challenge-response exchanges, extracts the necessary data, and uses a wordlist to crack the passwords. This is particularly useful in red team engagements targeting enterprise WiFi networks with outdated authentication protocols.

## Features

- Feature 1: Live capture from monitor-mode interfaces for real-time extraction and cracking.
- Feature 2: Offline processing of libpcap files for post-capture analysis.
- Feature 3: Dictionary-based offline attacks on extracted MD5 challenge-response pairs.
- Feature 4: Verbose output for monitoring progress and results.

## Installation

### Requirements

- Linux system with wireless card supporting monitor mode (e.g., compatible with airmon-ng).
- libpcap development libraries.
- GCC compiler for building from source.
- Wordlist files (e.g., rockyou.txt).

### Install Commands

```bash
# Clone the repository
git clone https://github.com/davidkilroy/eapmd5pass.git
cd eapmd5pass

# Compile the tool
make

# For Kali Linux (may require manual build as it's not pre-packaged)
sudo apt update
sudo apt install libpcap-dev build-essential
git clone https://github.com/davidkilroy/eapmd5pass.git
cd eapmd5pass
make
sudo cp eapmd5pass /usr/local/bin/
```

## Basic Usage

```bash
eapmd5pass --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -i, --interface | Specify monitor-mode interface |
| -r, --pcap | Input pcap file for offline processing |
| -w, --wordlist | Path to dictionary wordlist |
| -v, --verbose | Enable verbose output |
| -h, --help | Show help message |

## Examples

### Example 1: Basic Usage

Live capture and crack:

```bash
eapmd5pass -i wlan0mon -w /usr/share/wordlists/rockyou.txt
```

### Example 2: Advanced Usage

Process pcap file:

```bash
eapmd5pass -r auth_capture.pcap -w custom.txt -v
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle
- [[Password Guessing]] Password Guessing

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for wireless interfaces in monitor mode (e.g., via `iwconfig` or `airmon-ng` usage).
- Detection method 2: Network logs showing unusual EAP-MD5 traffic or dictionary attack attempts (if verbose).
- Detection method 3: Process monitoring for `eapmd5pass` binary on endpoints.

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
- [[tools/Wireshark]]

## References

- Official GitHub: https://github.com/davidkilroy/eapmd5pass
- Related resources: Aircrack-ng suite documentation
