---
id: 7705d554-8620-4f3c-9053-f5b3b75305ee
type: tool
name: statsgen
verified: true
created_at: '2019-08-28T21:17:40.415251+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - password-cracking
  - statistics
  - credential-access
  - hashcat
url: 'https://github.com/kahraman/Hash-Solo/tree/master/tools/PACK'
validated: true
---

# statsgen

**Status**: Unverified

## Overview

Statsgen is a Python-based tool from the Password Analysis and Cracking Toolkit (PACK), originally developed for the "Crack Me If You Can" competition at DEF CON 2010. It analyzes password lists to generate statistical data on character patterns, lengths, and compositions, helping to create optimized masks for password cracking tools like Hashcat or John the Ripper. This enables more efficient attacks than pure brute-force by focusing on common password structures.

## Description

Statsgen processes large password datasets to produce frequency statistics, such as common prefixes, suffixes, and character transitions. These stats inform the creation of probabilistic mask attacks, improving cracking speed for offline hash cracking scenarios. It does not perform cracking itself but serves as a preprocessing tool for better-targeted attacks. Commonly used in red team operations for credential dumping analysis or preparing for password spraying defenses.

## Features

- Analyzes password length distributions and character frequencies
- Generates stats for uppercase, lowercase, digits, and symbols
- Supports output in formats compatible with Hashcat mask generation
- Handles large wordlists efficiently
- Provides insights into password mangling rules (e.g., leetspeak patterns)

## Installation

### Requirements

- Python 2.7 or 3.x (compatible with both)
- Git for cloning the repository
- No additional dependencies beyond standard Python libraries

### Install Commands

```bash
# Clone the PACK repository (statsgen is included)
git clone https://github.com/kahraman/Hash-Solo.git
cd Hash-Solo/tools/PACK

# Make executable if needed (on Linux/macOS)
chmod +x statsgen.py
```

On Windows, run via `python statsgen.py` after cloning.

## Basic Usage

```bash
python statsgen.py input_wordlist.txt
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and usage |
| `-o, --output` | Specify output file for stats (default: stdout) |
| `-l, --length` | Analyze specific password length only |

## Examples

### Example 1: Basic Analysis

Analyze a password list to generate overall statistics:

```bash
python statsgen.py /path/to/rockyou.txt -o stats_output.txt
```

This outputs frequency data for character positions, useful for building Hashcat masks like ?u?l?l?l?d?d?s for common patterns.

### Example 2: Length-Specific Analysis

Focus on 8-character passwords:

```bash
python statsgen.py passwords.txt -l 8 -o length8_stats.txt
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

- Presence of PACK repository clones in user directories
- Python processes executing `statsgen.py` with large text files
- Generated stat files with password pattern data in working directories
- Network downloads of password lists or PACK tools

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Hashcat]]
- [[tools/John-the-Ripper]]
- [[tools/PACK]]

## References

- Original PACK GitHub: https://github.com/kahraman/Hash-Solo/tree/master/tools/PACK
- DEF CON 2010 Presentation: Search for "Crack Me If You Can"
- Hashcat Documentation on Masks: https://hashcat.net/wiki/doku.php?id=mask_attack
