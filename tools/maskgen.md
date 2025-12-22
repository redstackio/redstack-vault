---
id: 8504137b-ec36-4fea-b9f2-27a182eac3a8
name: maskgen
type: tool
verified: true
created_at: '2019-08-28T21:17:25.307557+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - password-cracking
  - credential-access
  - mask-generation
url: 'https://github.com/kc5tja/Password-Analysis-and-Cracking-Toolkit'
validated: true
---

# maskgen

**Status**: Unverified

## Overview

maskgen is a component of the Password Analysis and Cracking Toolkit (PACK), designed to generate optimized password candidate masks for use with cracking tools like Hashcat or John the Ripper. It analyzes statistical patterns from password datasets (via statsgen) to create efficient masks that go beyond brute-force, targeting common construction methods such as leetspeak, keyboard patterns, and personal information incorporation. Commonly used in red team operations for credential dumping scenarios or password recovery exercises.

## Description

Developed for the Defcon 2010 "Crack Me If You Can" competition, PACK's maskgen tool processes statistical databases generated from real-world password leaks or training sets. It identifies probable password structures (e.g., length distributions, character types, positional preferences) and outputs Hashcat-compatible mask files. This enables faster cracking by focusing on high-probability patterns rather than exhaustive searches. maskgen does not perform cracking itself but enhances the efficiency of GPU/CPU-based crackers. It's particularly useful in post-exploitation phases for cracking local hashes or in preparation for targeted attacks on known password policies.

## Features

- Feature 1: Statistical mask generation based on analyzed password corpora
- Feature 2: Support for variable password lengths and character sets (?l for lowercase, ?d for digits, etc.)
- Feature 3: Integration with PACK's statsgen for input data
- Feature 4: Output formats compatible with oclHashcat/Hashcat-plus
- Feature 5: Customizable complexity levels for mask sophistication

## Installation

### Requirements

- Python 2.7 or 3.x
- Git
- PACK toolkit dependencies (e.g., SQLite for stats database)

### Install Commands

```bash
# Clone the PACK repository
git clone https://github.com/kc5tja/Password-Analysis-and-Cracking-Toolkit.git
cd Password-Analysis-and-Cracking-Toolkit

# Install dependencies (if any Python requirements.txt exists)
pip install -r requirements.txt

# No formal setup.py; tools like maskgen are run directly as Python scripts
```

For Kali Linux: PACK is not pre-installed; follow the git clone steps above.
For Ubuntu: Same as above, ensure Python is installed via `apt install python3`.
For Windows: Use Git Bash or WSL, then run via Python.

## Basic Usage

```bash
python maskgen.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -s, --stats | Input statistical database file |
| -l, --length | Password length or range (e.g., 8 or 6-10) |
| -o, --output | Output file for masks |
| -c, --complexity | Set pattern complexity (low/medium/high) |
| -t, --type | Mask type (basic, advanced, custom) |

## Examples

### Example 1: Basic Usage

Generate masks for 8-character passwords from a stats file:

```bash
python maskgen.py -s stats.db -l 8 -o basic_masks.txt
```

### Example 2: Advanced Usage

Generate complex masks with symbols for lengths 6-10:

```bash
python maskgen.py -s stats.db -l 6-10 -c high -t full-charset -o advanced_masks.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Brute Force]] Brute Force
- [[Password Guessing]] Password Guessing
- [[Unsecured Credentials]] Unsecured Credentials

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Presence of PACK repository or maskgen.py in forensic analysis of attacker systems
- Detection method 2: Unusual Python script executions involving SQLite stats files during cracking operations
- Detection method 3: High GPU/CPU usage patterns correlated with Hashcat runs using custom masks
- Detection method 4: Network transfers of password stats databases or mask files

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
- [[tools/john-the-ripper]]
- [[tools/statsgen]]

## References

- Official GitHub: https://github.com/kc5tja/Password-Analysis-and-Cracking-Toolkit
- Defcon 2010 Context: https://defcon.org/html/defcon-18/dc-18-archive.html
- Hashcat Mask Documentation: https://hashcat.net/wiki/doku.php?id=mask_attack
