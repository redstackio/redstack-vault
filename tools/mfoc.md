---
id: 859b7c58-1b3c-4020-afc7-f0837262b990
type: tool
verified: true
created_at: '2019-08-28T21:17:19.689105+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - rfid
  - mifare
  - cracking
  - physical-security
  - nfc
url: 'https://github.com/nfc-tools/mfoc'
validated: true
---

# mfoc

**Status**: Unverified

## Overview

MFOC (MIFARE Classic Offline Cracker) is an open-source tool implementing the "offline nested" attack developed by Nethemba. It is designed for recovering authentication keys from MIFARE Classic RFID cards, commonly used in access control systems, public transport, and identification. MFOC is particularly useful in physical security assessments, red teaming scenarios involving badge cloning, or auditing NFC-enabled systems. It requires physical proximity to the target card via an NFC reader and works only if at least one known key (default or custom) is available to initiate the attack.

## Description

MFOC performs a nested attack by exploiting the way MIFARE Classic cards handle authentication between sectors. Starting from a known key (either the default factory keys hardcoded in the tool or user-provided keys), it recovers keys for adjacent sectors through offline computation and targeted reads. This allows full dumping of the card's memory blocks without needing all keys upfront. The tool interfaces with libnfc for reader communication and outputs dumps in MFD format, which can be analyzed or replayed with tools like mfcuk or nfc-mfclassic.

Key limitations: It targets only MIFARE Classic 1K/4K cards (not DESFire or newer standards), requires a compatible NFC reader (e.g., ACR122U), and the attack may fail on hardened cards with non-default keys or anti-collision protections.

## Features

- Offline nested key recovery starting from a single known key
- Support for default MIFARE keys (e.g., FFFFFFFFFFFF)
- Custom key provision via command line
- Output in MFD dump format for further analysis
- Verbose logging for debugging reader interactions
- Integration with libnfc for broad NFC reader compatibility

## Installation

### Requirements

- Linux kernel with NFC support
- libnfc library and development headers
- libpcsclite for smart card readers
- GCC and make for compilation

### Install Commands

```bash
# On Kali Linux (pre-built package available)
sudo apt update
sudo apt install mfoc libnfc-bin

# On Ubuntu (compile from source if not in repos)
sudo apt update
sudo apt install libnfc-dev libpcsclite-dev git build-essential

git clone https://github.com/nfc-tools/mfoc.git
cd mfoc
make
sudo make install
```

For macOS or Windows, use Docker or compile via libnfc ports, but Linux (Kali) is recommended for pentesting.

## Basic Usage

```bash
mfoc --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -O, --output | Specify output dump file (MFD format) |
| -P, --nested | Starting sector for nested attack (0-39) |
| -k, --key | Provide custom key for initial sector (hex) |
| -R, --reader | Specify NFC reader device |
| -v, --verbose | Enable verbose output for debugging |
| -h, --help | Show usage help |

## Examples

### Example 1: Basic Usage

```bash
mfoc -O card.dump /dev/nfc0
```
(Dumps card using default keys starting from sector 0)

### Example 2: Advanced Usage

```bash
mfoc -O card.dump -P 5 -k A0A1A2A3A4A5 /dev/nfc0
```
(Starts nested attack from sector 5 with custom key A0A1A2A3A4A5)

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Brute Force]] Brute Force (for key recovery in credential access)
- [[Unsecured Credentials]] Unsecured Credentials (recovering RFID keys as access tokens)

### Tactics

- [[Credential Access]] Credential Access
- [[Initial Access]] Initial Access (physical)

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual NFC reader activity or libnfc logs on monitoring systems
- Presence of mfoc binary or libnfc processes in process lists
- Network traces if using remote NFC over IP (rare)
- Physical security logs showing repeated card reads near access points
- File artifacts like .mfd dumps on analyst machines

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/libnfc]]
- [[tools/mfcuk]]
- [[tools/nfc-tools]]

## References

- Official GitHub: https://github.com/nfc-tools/mfoc
- Libnfc Documentation: https://nfc-tools.org/
- MIFARE Classic Attack Paper: http://www.nethemba.org/research/ndeftools/
- Related: RFID security auditing guides from SANS or DEF CON talks
