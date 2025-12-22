---
id: 1eb8d348-1442-493a-bfdb-eaa5f01966c7
name: RainbowCrack
type: tool
verified: true
created_at: '2019-08-28T21:17:22.248652+00:00'
updated_at: '2024-10-01T00:00:00Z'
platforms:
  - Linux
  - Windows
tags:
  - hash-cracking
  - rainbow-tables
  - credential-access
url: 'http://project-rainbowcrack.com/'
validated: true
---

# RainbowCrack

**Status**: Unverified

## Overview

RainbowCrack is a specialized tool for cracking password hashes using precomputed rainbow tables based on a time-memory trade-off algorithm. It is commonly used in offensive security for offline password recovery from captured hashes, such as those from Windows NTLM, MD5, or SHA-1, providing faster results than traditional brute-force methods when tables are available.

## Description

RainbowCrack implements Philippe Oechslin's faster time-memory trade-off technique, where rainbow tables store chains of hash reductions to reduce storage needs while maintaining lookup efficiency. Unlike brute-force crackers that compute hashes on-the-fly for every possible plaintext, RainbowCrack relies on precomputed tables generated once and reused for multiple cracking sessions. The suite includes tools for table generation (rtgen), cracking (rcrack), table dumping (rtdump), and sorting (sorttbl). It is particularly effective for cracking hashes in controlled environments like penetration testing or forensic analysis, but requires significant disk space for large tables.

## Features

- **Time-Memory Trade-Off**: Uses rainbow chains to balance computation time and storage for efficient cracking.
- **Multiple Hash Support**: Handles LM, NTLM, MD5, SHA-1, and other algorithms via customizable table generation.
- **Table Management**: Tools to generate, sort, merge, and inspect rainbow tables.
- **Cross-Platform**: Available on Linux and Windows, with command-line interface for automation.
- **Offline Cracking**: No network required after table precomputation, ideal for air-gapped analysis.

## Installation

### Requirements

- C++ compiler (for building from source)
- Sufficient disk space (tables can be gigabytes in size)
- Supported platforms: Linux (x86/x64), Windows (x86/x64)

### Install Commands

On Kali Linux (pre-built binaries often available via repositories or direct download):

```bash
# Download from official site or use package manager if available
wget http://project-rainbowcrack.com/table.htm  # For precomputed tables
# Build from source (if needed)
git clone https://github.com/albertzeyer/rainbowcrack.git
cd rainbowcrack
make
# Or on Ubuntu/Debian
apt update && apt install build-essential  # For dependencies
```

On Ubuntu:

```bash
# Install dependencies
apt install build-essential libssl-dev
# Download and build
wget https://github.com/albertzeyer/rainbowcrack/archive/master.zip
unzip master.zip
cd rainbowcrack-master
make
sudo make install
```

On Windows: Download precompiled binaries from the official website and extract to a directory, adding to PATH.

## Basic Usage

```bash
rcrack --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Display help message and exit |
| `-v, --version` | Show version information |
| `--table-path=PATH` | Specify directory containing rainbow tables |
| `-l` | List available tables |

## Examples

### Example 1: Basic Usage (Crack a Hash)

Assume you have rainbow tables in `/path/to/tables/` and an NTLM hash to crack:

```bash
rcrack /path/to/tables/ -h 8846f7eaee8fb117ad06bdd830b7586c
```

This searches the tables for the plaintext corresponding to the provided hash.

### Example 2: Advanced Usage (Specify Hash Type and Charset)

For generating a table first (using rtgen), then cracking:

```bash
# Generate a sample table (this takes time and space)
rtgen md5 loweralpha-numeric 1 7 0 2400 10000000 0 rt_md5

# Crack using the generated table
rcrack rt_md5 -h 5f4dcc3b5aa765d61d8327deb882cf99
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Brute Force]] Brute Force
- [[Unsecured Credentials]] Unsecured Credentials

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of large rainbow table files (e.g., .rt files) on disk, often in hidden directories.
- High CPU/disk I/O during table generation (rtgen).
- Process monitoring for rcrack, rtgen executions in forensic timelines.
- Log analysis for hash cracking attempts in security tools like SIEM.

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

- Official website: http://project-rainbowcrack.com/
- GitHub repository: https://github.com/albertzeyer/rainbowcrack
- Table downloads: http://project-rainbowcrack.com/table.htm
