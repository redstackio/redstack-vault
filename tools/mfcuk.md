---
id: c7c57b1b-bc36-4804-a3d1-077703d3a5f3
name: mfcuk
type: tool
verified: true
created_at: '2019-08-28T21:17:25.124244+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - rfid
  - nfc
  - mifare
  - cracking
  - physical-security
url: 'https://github.com/nfc-tools/mfcuk'
validated: true
---

# mfcuk

**Status**: Unverified

## Overview

mfcuk (Mifare Classic Universal toolKit) is a specialized toolkit for exploiting weaknesses in Mifare Classic RFID cards from NXP/Philips. It leverages libnfc for reader interactions and Crypto1 implementations to demonstrate and perform attacks like nested key recovery and Darkside exploits. Commonly used in physical security testing to assess access control systems vulnerable to RFID cloning or key cracking.

## Description

The toolkit focuses on practical exploitation of Mifare Classic cards' pseudo-random number generator (PRNG) biases and Crypto1 cipher weaknesses. It supports various NFC readers, particularly ACR122 devices, and provides tools for key recovery, tag emulation verification, and attack simulations. mfcuk is essential for red team operations targeting badge systems, door locks, or transit cards, allowing recovery of encryption keys to clone or bypass authentication.

## Features

- Feature 1: Nested attack mode for exhaustive key recovery on Mifare Classic 1k/4k cards
- Feature 2: Darkside attack implementation exploiting PRNG predictability for faster cracking
- Feature 3: Integration with libnfc for broad NFC reader compatibility (e.g., ACR122, PN532)
- Feature 4: Verbose logging and output to files for key dumps and attack traces
- Feature 5: Support for Crypto1 state analysis to verify theoretical attacks

## Installation

### Requirements

- libnfc development libraries
- pcsc-lite for smart card support
- build-essential (gcc, make)
- git for cloning the repository

### Install Commands

```bash
# Clone the repository
sudo apt update
git clone https://github.com/nfc-tools/mfcuk.git
cd mfcuk

# Install dependencies (Ubuntu/Debian)
sudo apt install libnfc-dev libpcsclite-dev libssl-dev

# Compile and install
make
sudo make install

# For Kali Linux (often pre-built or via apt)
sudo apt install mfcuk
```

## Basic Usage

```bash
mfcuk --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -C | Nested attack mode |
| -D | Darkside attack mode |
| -v | Verbose output |
| -R <index> | Specify NFC reader index |
| -t <attempts> | Limit attack attempts |

## Examples

### Example 1: Basic Usage

Perform a standard nested attack on a detected Mifare card:

```bash
mfcuk -C -R 0 -v /dev/nfc0
```

### Example 2: Advanced Usage

Run Darkside attack with limited attempts and save output:

```bash
mfcuk -D -v -R 0 -t 10000 /dev/nfc0 > attack_log.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T0855]] Hardware Access (for RFID exploitation in physical access control)
- [[Software Discovery]] Software Discovery (scanning for vulnerable RFID implementations)

### Tactics

- [[Defense Evasion]] Defense Evasion (bypassing physical authentication)
- [[Initial Access]] Initial Access (via cloned credentials)

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor NFC reader traffic for repeated authentication attempts indicative of key cracking
- Detection method 2: Log unusual USB device connections (ACR122 readers) combined with high CPU usage from libnfc processes
- Detection method 3: Presence of mfcuk binaries or libnfc traces in system logs
- Detection method 4: Anomalous RFID access patterns, such as multiple failed authentications followed by success

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[libnfc]]
- [[tools/mfoc]]
- [[nfc-tools]]

## References

- Official GitHub: https://github.com/nfc-tools/mfcuk
- libnfc Documentation: http://nfc-tools.org/
- Mifare Classic Weakness Analysis: https://www.nfc-tools.org/dl/mifare-classic-weaknesses.pdf
