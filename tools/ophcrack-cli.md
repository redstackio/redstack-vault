---
id: b4d56386-be9d-4822-9ee0-7c0c64afcfb9
name: ophcrack-cli
type: tool
verified: true
created_at: '2019-08-28T21:17:24.350590+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - password-cracking
  - windows-passwords
  - rainbow-tables
  - credential-access
url: 'https://ophcrack.sourceforge.net/'
validated: true
---

# ophcrack-cli

**Status**: Unverified

## Overview

Ophcrack-cli is the command-line version of Ophcrack, a free open-source tool for cracking Windows passwords using rainbow tables. It enables offline recovery of LM and NTLM hashes, making it ideal for post-exploitation credential dumping and analysis in security testing.

## Description

Ophcrack-cli implements the rainbow table algorithm for efficient password cracking without brute-forcing. It supports cracking passwords from SAM files, live sessions, or extracted hashes. The tool runs on multiple platforms and is particularly useful for recovering weak or common passwords in Windows environments during red team engagements or forensic analysis.

## Features

- Rainbow table-based cracking for LM/NTLM hashes
- Support for custom table sizes and languages
- Memory-efficient loading of large table sets
- Output in various formats for integration with other tools
- CLI automation for scripting in attack chains

## Installation

### Requirements

- Rainbow tables (download from official site or generate with rtgen)
- At least 1GB RAM for small tables; more for larger sets
- libxml2 and other dependencies for XML session handling

### Install Commands

```bash
# On Ubuntu/Debian (including Kali)
sudo apt update
sudo apt install ophcrack

# On Windows (via Cygwin or WSL)
# Install via package manager or compile from source

# On macOS (via Homebrew)
brew install ophcrack
```

Note: Rainbow tables must be downloaded separately from https://ophcrack.sourceforge.net/tables.php.

## Basic Usage

```bash
ophcrack --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -t, --tables | Specify rainbow tables directory |
| -i, --input | Input file with hashes |
| -o, --output | Output file for results |
| -m, --memory | Limit memory usage in MB |
| -s, --session | Load/save session file |

## Examples

### Example 1: Basic Usage

Load tables and crack hashes:

```bash
ophcrack -t /path/to/tables -i hashes.txt -o results.txt
```

### Example 2: Advanced Usage

With memory limit:

```bash
ophcrack -t /path/to/tables -m 256 -i sam_hashes.txt -o cracked.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Password Cracking]] Password Cracking

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for ophcrack.exe or ophcrack binary execution
- File system scans for rainbow table directories (large .tbl files)
- Memory forensics for loaded table data
- Network downloads of rainbow tables from known sources

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/john-the-ripper]]
- [[tools/Hashcat]]

## References

- Official website: https://ophcrack.sourceforge.net/
- Rainbow tables: https://ophcrack.sourceforge.net/tables.php
- Source code: https://github.com/ophcrack/ophcrack

*Last updated: 2023-10-01*
