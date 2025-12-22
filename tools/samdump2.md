---
id: 5a564e59-4842-4628-a7ce-da65f880b57b
type: tool
verified: true
created_at: '2019-08-28T21:17:35.115503+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
commands:
  - '[[commands/samdump2-extract-lm-ntlm-hashes-from-sam-and-system]]'
platforms:
  - Linux
tags:
  - '[[Cryptography]]'
  - '[[NTLM]]'
  - '[[pass the hash]]'
url: 'https://github.com/tripwire/samdump2'
validated: true
---

# samdump2

**Status**: Unverified

## Overview

samdump2 is a command-line tool for extracting LM and NTLM password hashes from Windows NT/2000/XP/Vista/7 registry hives. It is commonly used in offline password analysis during penetration testing, forensics, or red team operations to recover credentials from extracted SAM and SYSTEM files obtained via tools like Mimikatz or registry dumps.

## Description

samdump2 requires both the SAM hive (containing user account hashes) and the SYSTEM hive (providing the boot key for decryption). It decrypts the hashes using the SysKey from the SYSTEM hive and outputs them in a crackable format. This tool is particularly useful for pass-the-hash attacks or offline cracking with tools like Hashcat. It supports older Windows versions but may have limitations with newer encrypted formats (use alternatives like secretsdump for modern systems).

## Features

- Decrypts SAM hashes using SYSTEM boot key
- Outputs LM/NTLM hashes in John/Hashcat-compatible format
- Handles multiple user accounts in a single run
- Lightweight and scriptable for automation

## Installation

### Requirements

- Linux environment (Kali, Ubuntu, etc.)
- Basic build tools (gcc, make)

### Install Commands

```bash
# On Kali Linux (pre-installed or via package)
apt update && apt install samdump2

# On Ubuntu/Debian (compile from source if not in repos)
git clone https://github.com/tripwire/samdump2.git
cd samdump2
make
sudo cp samdump2 /usr/local/bin/

# On macOS (using Homebrew)
brew install samdump2
```

## Basic Usage

```bash
samdump2 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| No options needed for basic use | Directly specify hive files as arguments |

## Examples

### Example 1: Basic Usage

Extract hashes from hive files:

```bash
samdump2 SYSTEM SAM
```

### Example 2: Advanced Usage

Save output to file:

```bash
samdump2 SYSTEM SAM > extracted_hashes.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Credential Dumping]] OS Credential Dumping
- [[Boot or Logon Autostart Execution]] Boot or Logon Autostart Execution (for hive access)

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- File access to SAM/SYSTEM hives on compromised systems
- Process execution of samdump2 in memory forensics
- Network transfer of hive files (e.g., via SMB exfiltration)
- Presence of extracted hash files in staging directories

## Related Procedures

- [[procedures/Dump-Windows-Hashes-from-Offline-Hives]]

## Related Tools

- [[tools/Mimikatz]]
- [[tools/secretsdump]]

## References

- Official GitHub: https://github.com/tripwire/samdump2
- Related resources: Windows Internals documentation on registry hives
