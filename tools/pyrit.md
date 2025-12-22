---
id: 38699ef8-8cb8-4c3c-bef1-8d449b7f1a8d
type: tool
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - wireless
  - cracking
  - wpa
  - gpu
  - cuda
  - opencl
url: 'https://github.com/JPaulMora/Pyrit'
commands:
  - '[[commands/pyrit-import-passwords]]'
  - '[[commands/pyrit-attack-capture]]'
  - '[[commands/pyrit-strip-packets]]'
  - '[[commands/pyrit-create-essid]]'
validated: true
---

# Pyrit

**Status**: Unverified

## Overview

Pyrit is a powerful tool for performing offline dictionary and brute-force attacks against WPA/WPA2-PSK networks. It leverages GPU acceleration via CUDA, OpenCL, or ATI Stream to create massive pre-computed databases of authentication handshakes, enabling rapid cracking of captured Wi-Fi traffic. Commonly used in wireless penetration testing to recover pre-shared keys from captured packets.

## Description

Pyrit exploits the space-time tradeoff in WPA/WPA2 authentication by pre-computing Pairwise Master Key (PMK) and Pairwise Transient Key (PTK) candidates. It supports importing password lists, stripping irrelevant packets from captures, creating ESSID profiles, and launching attacks against pcap files. This makes it ideal for red team operations targeting enterprise Wi-Fi networks, where captured handshakes can be cracked offline without real-time constraints.

## Features

- GPU-accelerated cracking using CUDA, OpenCL, or CPU fallbacks
- Database management for storing pre-computed chains
- Support for importing wordlists and attacking pcap captures
- ESSID profile creation for targeted attacks
- Packet stripping to focus on authentication handshakes

## Installation

### Requirements

- Python 2.7 (legacy tool)
- For GPU support: NVIDIA CUDA toolkit (for CUDA), or OpenCL libraries
- libpcap for packet processing
- Supported on Linux; Windows possible with cygwin or virtual env

### Install Commands

```bash
# On Kali Linux or Debian-based distros (includes basic CPU support)
sudo apt update
sudo apt install pyrit

# For CUDA support (NVIDIA GPU)
# Install CUDA toolkit first: https://developer.nvidia.com/cuda-downloads
sudo apt install pyrit-cuda

# For OpenCL support
sudo apt install pyrit-opencl

# Compile from source for custom setups
 git clone https://github.com/JPaulMora/Pyrit.git
 cd Pyrit
 python setup.py build
 sudo python setup.py install
```

## Basic Usage

```bash
pyrit --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and usage |
| `-v, --verbose` | Enable verbose output for debugging |
| `-u, --unverify` | Unverify database entries during attacks |
| `-e ESSID` | Specify ESSID for profile creation or attacks |
| `-r FILE` | Input pcap file for stripping or attacking |

## Examples

### Example 1: Basic Usage

Import a password list and check database status:

```bash
pyrit import_passwords /usr/share/wordlists/rockyou.txt
pyrit databases
```

### Example 2: Advanced Usage

Strip packets and attack a capture with GPU acceleration:

```bash
pyrit -r capture.pcap stripLive
pyrit -r capture.pcap -e "TargetNetwork" attack_db
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Password Guessing]] Password Guessing (for dictionary attacks on WPA-PSK)
- [[Password Spraying]] Password Spraying (adapted for offline cracking)

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- High GPU/CPU utilization on attacker machines during cracking sessions
- Network captures showing airodump-ng or similar tools followed by Pyrit processes
- Database files (.pyrit) in temporary directories or forensic artifacts
- Process monitoring for 'pyrit' executable with CUDA/OpenCL libraries loaded

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
- [[tools/Hashcat]] (alternative GPU cracker)
- [[tools/john-the-ripper]] (CPU-based password cracking)

## References

- Official GitHub: https://github.com/JPaulMora/Pyrit
- Kali Tools Documentation: https://www.kali.org/tools/pyrit/
- WPA Cracking Guide: https://www.aircrack-ng.org/
