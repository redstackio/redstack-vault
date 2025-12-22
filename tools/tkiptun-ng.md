---
id: 5eab8495-4e87-4392-ba01-cbebb42b31aa
type: tool
verified: true
created_at: '2019-08-28T21:17:23.051428+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - wireless
  - wpa
  - tkip
  - exploitation
url: 'https://www.aircrack-ng.org/'
validated: true
---

# tkiptun-ng

**Status**: Unverified

## Overview

tkiptun-ng is a proof-of-concept tool for exploiting vulnerabilities in WPA/TKIP encryption. It implements attacks described in the paper 'Practical Attacks Against WEP and WPA' by Martin Beck and Erik Tews, enabling packet injection and decryption in TKIP-secured wireless networks. Commonly used in wireless penetration testing for educational and research purposes.

## Description

tkiptun-ng creates virtual tunnel interfaces to facilitate the injection of crafted packets into WPA/TKIP networks, exploiting weaknesses in the TKIP protocol to bypass encryption or decrypt traffic. It is part of the aircrack-ng suite and requires a wireless card in monitor mode. This tool demonstrates theoretical attacks but has limited practical success against modern WPA2 implementations due to mitigations.

## Features

- Virtual tunnel creation for packet injection
- TKIP key stream manipulation
- Support for crafted packet files (pcap format)
- Integration with other aircrack-ng tools like aireplay-ng

## Installation

### Requirements

- Linux kernel with TUN/TAP support
- Wireless card supporting monitor mode (e.g., Atheros AR9271)
- aircrack-ng suite

### Install Commands

```bash
# On Kali Linux (pre-installed)
sudo apt update && sudo apt install aircrack-ng

# On Ubuntu
declare -a deps=('build-essential' 'libssl-dev' 'libnl-3-dev' 'libnl-genl-3-dev' 'pkg-config' 'libsqlite3-dev')
for i in "${deps[@]}"; do sudo apt install $i; done

# Compile from source
git clone https://github.com/aircrack-ng/aircrack-ng.git
cd aircrack-ng
make
sudo make install
```

## Basic Usage

```bash
tkiptun-ng --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -i, --interface | Specify the wireless interface |
| -e, --essid | Target ESSID |
| --inject | Inject packets from a file |
| -v, --verbose | Enable verbose output |

## Examples

### Example 1: Basic Usage

Create a virtual interface:

```bash
tkiptun-ng -i wlan0mon
```

### Example 2: Advanced Usage

Inject packets after setup:

```bash
tkiptun-ng -i wlan0mon --inject exploit.pcap
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Credentials in Files]] - Wi-Fi Credential Dumping (for related wireless attacks)
- [[Archive Collected Data]] - Archive Collected Data (in context of packet capture)

### Tactics

- [[Discovery]] - Discovery (network discovery via wireless)
- [[Execution]] - Execution (adversary-in-the-middle via injection)

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for TUN/TAP interface creation (e.g., via `ip link show`)
- Wireless card switching to monitor mode (iwconfig or iw commands)
- Unusual packet injection traffic on wireless interfaces
- Process monitoring for tkiptun-ng execution

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
- [[tools/airodump-ng]]

## References

- Official aircrack-ng documentation: https://www.aircrack-ng.org/doku.php?id=tkiptun-ng
- Research paper: Practical Attacks Against WEP and WPA (Beck & Tews, 2008)
