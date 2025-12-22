---
id: d3e3cb9f-b9e3-4c34-a413-a4524fa88fc8
type: tool
verified: true
created_at: '2019-08-28T21:17:25.453246+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - password-cracking
  - rainbow-tables
  - offline-attacks
url: 'http://ophcrack.sourceforge.net/'
validated: true
---

# ophcrack

**Status**: Verified

## Overview

Ophcrack is an open-source Windows password recovery and cracking tool that uses rainbow tables to crack LM and NTLM hashes offline. It is particularly effective against weak or default passwords in Windows environments. Commonly used in penetration testing for cracking local account hashes extracted from SAM files or memory dumps. Supports both GUI and limited CLI modes, and runs on multiple platforms including Linux via Wine.

## Description

Ophcrack implements the rainbow table algorithm for efficient cracking of Windows password hashes without brute-forcing. It comes bundled with free rainbow tables for Windows XP/2000 and Vista/7 (free tables cover simple passwords). Users can generate custom tables for stronger coverage. The tool audits live systems by booting from CD/USB or processes offline dumps. It excels at cracking short, dictionary-based passwords but struggles with complex, salted hashes from modern Windows versions.

## Features

- Feature 1: Rainbow table-based cracking for LM/NTLM hashes (fast for weak passwords)
- Feature 2: GUI interface for easy loading of dumps and tables
- Feature 3: CLI support for automated/batch cracking
- Feature 4: Multi-platform support (Windows native, Linux/macOS via Wine)
- Feature 5: Free precomputed tables for common Windows versions

## Installation

### Requirements

- Rainbow tables (download from official site; ~1-14GB depending on version)
- Wine (for Linux/macOS usage)
- Sufficient disk space for tables

### Install Commands

```bash
# On Kali Linux (pre-installed in some repos, or compile from source)
sudo apt update
sudo apt install ophcrack

# Download and extract rainbow tables (example for XP free tables)
wget http://ophcrack.sourceforge.net/tables.php -O tables.zip  # Download link from site
unzip tables.zip -d /opt/ophcrack/tables

# For Windows: Download installer from sourceforge.net/projects/ophcrack
# For macOS: Use Wine or virtual machine
brew install wine  # Then run Windows exe via wine
```

## Basic Usage

```bash
ophcrack --help  # Or wine ophcrack.exe --help for CLI options
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -t, --tables | Specify path to rainbow tables directory |
| -i, --input | Input file with hashes |
| -d, --dump | Load SAM/system dump file |
| -l, --lm | Crack only LM hashes (faster) |

## Examples

### Example 1: Basic Usage (CLI on Linux)

```bash
wine ophcrack.exe -t /opt/ophcrack/tables -i hashes.txt
```

### Example 2: Advanced Usage (Crack from Dump)

```bash
wine ophcrack.exe -d samdump.txt -t /opt/ophcrack/tables/vista
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Brute Force]] Brute Force (for offline hash cracking)
- [[Unsecured Credentials]] Unsecured Credentials (recovering weak passwords)

### Tactics

- [[Persistence]] Persistence (via cracked creds)
- [[Defense Evasion]] Defense Evasion (offline cracking avoids detection)

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Large rainbow table downloads (~GBs) in network logs or disk artifacts
- Detection method 2: Wine or ophcrack.exe processes on Linux endpoints
- Detection method 3: Bootable Ophcrack ISO in incident response forensics
- Detection method 4: Cracked password attempts in auth logs post-extraction

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/rainbowcrack]] (for generating custom tables)
- [[tools/john-the-ripper]] (alternative cracker for more hash types)
- [[tools/Hashcat]] (GPU-accelerated cracking)

## References

- Official website: http://ophcrack.sourceforge.net/
- Rainbow tables download: http://ophcrack.sourceforge.net/tables.php
- Source code: https://sourceforge.net/projects/ophcrack/
