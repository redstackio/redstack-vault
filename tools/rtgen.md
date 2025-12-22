---
id: 86e48758-0cea-4f05-b510-1c5ad9eeaed3
name: rtgen
type: tool
verified: true
created_at: '2019-08-28T21:17:28.398230+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
tags:
  - hash-cracking
  - rainbow-table
  - credential-access
url: 'http://project-rainbowcrack.com/'
validated: true
---

# rtgen

**Status**: Unverified

## Overview

rtgen is the rainbow table generator component of the RainbowCrack suite, implementing Philippe Oechslin's time-memory trade-off technique for cracking password hashes. It precomputes and stores chains of plaintext-hash pairs in rainbow tables, enabling faster cracking compared to brute-force methods. Commonly used in offensive security for cracking hashes obtained from network captures, memory dumps, or file extractions.

## Description

RainbowCrack uses a time-memory tradeoff algorithm to crack hashes more efficiently than traditional brute-force crackers, which compute hashes on-the-fly and discard intermediate results. rtgen performs the one-time expensive precomputation: it generates all possible plaintexts within specified parameters (algorithm, charset, length), computes their hashes, and stores reduction chains in .rt files. Once tables are generated, other RainbowCrack tools like rcrack can use them for rapid lookups. This is ideal for cracking weak passwords offline, such as MD5, SHA1, or NTLM hashes in red team engagements.

## Features

- Supports multiple hash algorithms: MD5, SHA1, LM, NTLM, etc.
- Customizable charsets for targeted cracking (e.g., lowercase, alphanumeric).
- Adjustable chain parameters for balancing table size and coverage.
- Generates large tables (gigabytes) for comprehensive cracking.
- Integrates with the full RainbowCrack workflow (generation, sorting, cracking).

## Installation

### Requirements

- C++ compiler (for building from source).
- Sufficient disk space (tables can be multi-GB).
- Supported on Linux and Windows.

### Install Commands

RainbowCrack (including rtgen) is available via source compilation or pre-built binaries.

For Ubuntu/Kali:

```bash
# Download and extract
wget http://project-rainbowcrack.com/table_dataset.htm  # For pre-built tables, but compile for rtgen

# Or build from source
git clone https://github.com/albertobsd/rainbowcrack.git
cd rainbowcrack
make
sudo make install
```

For Windows:

Download pre-built binaries from the official site and extract to a directory. Add to PATH.

```cmd
# No specific install; run executables directly
rtgen.exe md5 null 1 7 1 0 1 4000 0
```

Kali Linux: Often pre-installed or available via `apt search rainbowcrack`.

## Basic Usage

```bash
rtgen --help
```

rtgen requires parameters for hash type, charset, lengths, and chain settings.

### Common Options

| Option | Description |
|--------|-------------|
| No flags; all via positional args | Hash algo, charset, etc. |

## Examples

### Example 1: Basic Usage

Generate an MD5 rainbow table for 1-7 char lowercase passwords:

```bash
rtgen md5 null 1 7 1 0 1 4000 0
```

See [[commands/rtgen-generate-md5-table]] for details.

### Example 2: Advanced Usage

Generate NTLM table:

```bash
rtgen nt null 1 7 1 0 1 4000 0
```

See [[commands/rtgen-generate-ntlm-table]] for details.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Brute Force]] Brute Force
- [[Password Cracking]] Password Cracking

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Large disk writes to .rt files in temp directories.
- High CPU/disk usage during table generation.
- Process monitoring for rtgen.exe or similar.
- Network downloads of RainbowCrack binaries or table datasets.

## Related Procedures

- [[procedures/Generate-Rainbow-Tables-for-Cracking]]
- [[procedures/Crack-Captured-Hashes-Offline]]

## Related Tools

- [[tools/rainbowcrack]] (full suite)
- [[tools/Hashcat]] (alternative cracker)
- [[tools/john-the-ripper]] (brute-force alternative)

## References

- Official site: http://project-rainbowcrack.com/
- Table datasets: http://project-rainbowcrack.com/table.htm
- GitHub repo: https://github.com/albertobsd/rainbowcrack
