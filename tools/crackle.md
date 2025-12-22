---
id: ce488d90-544e-44d3-b889-cb1179bd2004
type: tool
verified: true
created_at: '2019-08-28T21:17:25.730814+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - ble
  - bluetooth
  - cracking
  - credential-access
  - wireless
url: 'https://github.com/mikeryan/crackle'
commands:
  - '[[commands/crackle-crack-ble-pcap]]'
validated: true
---

# crackle

**Status**: Unverified

## Overview

Crackle is a specialized tool for cracking Bluetooth Low Energy (BLE) encryption by exploiting weaknesses in the pairing process. It allows security researchers and penetration testers to brute-force the Temporary Key (TK), derive the Short Term Key (STK) and Long Term Key (LTK), and decrypt captured BLE communications. Commonly used in wireless security assessments to test BLE device security.

## Description

Crackle targets a vulnerability in the BLE pairing protocol where the TK can be guessed or rapidly brute-forced due to limited entropy in certain pairing modes (e.g., Just Works or Passkey Entry). By analyzing PCAP captures of the pairing handshake, crackle computes possible TK values, derives session keys, and decrypts subsequent encrypted traffic between BLE master and slave devices. This enables analysis of otherwise protected BLE data, such as sensor readings or control commands, in scenarios like IoT device testing or supply chain attacks.

## Features

- Feature 1: Rapid brute-force of 1-million possible TK values in seconds
- Feature 2: Derivation of STK and LTK from captured pairing data
- Feature 3: Decryption of BLE Link Layer packets in PCAP format
- Feature 4: Support for common BLE pairing association models
- Feature 5: Output of decrypted keys and traffic for further analysis

## Installation

### Requirements

- Linux environment (Kali Linux recommended)
- Git and build essentials (gcc, make)
- libpcap-dev for PCAP handling

### Install Commands

```bash
# Clone the repository
git clone https://github.com/mikeryan/crackle.git
cd crackle

# Compile the tool
make

# Install to system path (optional)
sudo make install
```

On Kali Linux, it may be available via apt:

```bash
sudo apt update && sudo apt install crackle
```

## Basic Usage

```bash
crackle --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -i, --input | Input PCAP file path |
| -o, --output | Output directory for results |
| -e, --encrypt | Enable key extraction and decryption |
| -v, --verbose | Increase output verbosity |
| -h, --help | Show help message |

## Examples

### Example 1: Basic Usage

Crack a captured BLE pairing PCAP:

```bash
crackle -i ble_pairing.pcap -o decrypted -e
```

This processes the PCAP, brute-forces the TK, and outputs decrypted files to the 'decrypted' directory.

### Example 2: Advanced Usage

Process with verbose output:

```bash
crackle -i full_ble_traffic.pcap -o keys_and_decrypts -e -v
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials
- [[Steal Web Session Cookie]] Steal Web Session Cookie (adapted for BLE sessions)

### Tactics

- [[Credential Access]] Credential Access
- [[Initial Access]] Initial Access (via wireless)

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for high CPU usage during brute-force operations on systems with BLE captures
- Detection method 2: Network/USB traffic analysis for PCAP processing tools; look for crackle binary or GitHub downloads
- Detection method 3: File system scans for output directories containing STK/LTK files or decrypted BLE PCAPs
- Detection method 4: BLE device logs showing unexpected pairing attempts or key derivation failures

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Wireshark]] (for capturing BLE traffic)
- [[tools/ubertooth]] (for BLE sniffing hardware)

## References

- Official GitHub: https://github.com/mikeryan/crackle
- BLE Security Overview: Bluetooth SIG Documentation
- Related Research: Black Hat talks on BLE vulnerabilities
