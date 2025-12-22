---
id: cbb197c9-55a3-449b-bab9-f7c225df3097
type: tool
verified: true
created_at: '2019-08-28T21:17:25.066256+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - rfid
  - nfc
  - mifare
  - physical-security
  - access-control
url: 'https://nfc-tools.org/index.php?title=Libnfc'
validated: true
---

# mfterm

**Status**: Unverified

## Overview

mfterm is an interactive terminal-based tool for working with Mifare Classic RFID tags. It provides a shell-like interface for reading, writing, dumping, and manipulating data on proximity cards commonly used in access control systems, public transportation, and identification badges. Ideal for physical security assessments, red team operations involving badge cloning, and RFID pentesting.

## Description

mfterm is part of the libnfc library ecosystem and offers a user-friendly command-line interface for NFC/RFID interactions focused on Mifare Classic 1K/4K tags. It supports tab completion for commands and filenames, command history for easy recall, and interactive sessions that allow real-time tag manipulation. Use it to enumerate tag sectors, crack weak keys, dump card contents, or emulate tags during physical penetration tests. Requires compatible NFC hardware like ACR122U or PN532 readers.

## Features

- Feature 1: Interactive shell with tab completion for commands (e.g., `load`, `dump`, `read`) and file arguments.
- Feature 2: Command history navigation using arrow keys, similar to bash.
- Feature 3: Support for Mifare Classic tag operations including key authentication, block reading/writing, and data dumping.
- Feature 4: Device selection for multi-reader setups.
- Feature 5: Integration with libnfc for low-level NFC protocol handling.

## Installation

### Requirements

- Compatible NFC reader hardware (e.g., ACR122U, PN532).
- libnfc library dependencies.
- Root privileges may be required for USB device access.

### Install Commands

```bash
# On Kali Linux (pre-installed in many distributions)
sudo apt update
sudo apt install libnfc-bin libnfc-dev

# Compile from source if needed
wget https://bintray.com/artifact/download/nfc-tools/sources/libnfc-1.8.0.tar.bz2
 tar -xjf libnfc-1.8.0.tar.bz2
cd libnfc-1.8.0
./configure --with-drivers=pn532_i2c
make
sudo make install
```

For Ubuntu/Debian, the apt method suffices. Verify installation with `nfc-list` to detect hardware.

## Basic Usage

```bash
mfterm
```

This launches the interactive shell. Place a Mifare Classic tag on the reader to begin interaction. Common in-shell commands include:
- `help`: Show available commands.
- `load`: Load a key file.
- `dump`: Dump tag contents to a file.
- `read <sector> <block>`: Read specific data block.
- `quit`: Exit the shell.

### Common Options

| Option | Description |
|--------|-------------|
| `-d, --device <index>` | Select NFC device by index (default: auto-detect). |
| `-h, --help` | Show help message and exit. |
| `-v, --version` | Display version information. |

## Examples

### Example 1: Basic Usage

```bash
mfterm
```

In the shell:
```
mfterm> load keys.dic
mfterm> dump tag_dump.mfd
```

Dumps the tag using loaded keys.

### Example 2: Advanced Usage

```bash
mfterm -d 0
```

Launches with specific device, then in shell:
```
mfterm> auth 0 A ffffffffffff
mfterm> read 0 0
```

Authenticates sector 0 with default key and reads block 0.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Password Spraying]] Password Spraying (for brute-forcing Mifare keys in access control systems).
- [[Port Knocking]] Hardware Additions (emulating or cloning RFID tags for unauthorized access).

### Tactics

- [[Lateral Movement]] Lateral Movement (gaining physical access via cloned badges).
- [[Defense Evasion]] Defense Evasion (bypassing RFID-based authentication).

## Detection

Indicators and methods for detecting this tool's usage:
- Detection method 1: Monitor USB device connections for NFC readers (e.g., via USB logs or udev rules).
- Detection method 2: Network anomalies if combined with other tools; look for libnfc process spawning (`ps aux | grep mfterm`).
- Detection method 3: Physical security logs for unauthorized tag reads/writes near access points.
- Detection method 4: File system artifacts like dumped .mfd files or key dictionaries in temp directories.

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
- [[tools/mfoc]]
- [[tools/mfcuk]]

## References

- Official libnfc documentation: https://nfc-tools.org/index.php?title=Libnfc
- GitHub repository: https://github.com/nfc-tools/libnfc
- Usage guide: https://nfc-tools.org/index.php?title=Tools:mfterm
