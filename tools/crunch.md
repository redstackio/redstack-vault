---
id: c48986c0-2219-405d-ab83-855aa0968994
type: tool
verified: true
created_at: '2019-08-28T21:17:41.345908+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - wordlist
  - generation
  - brute-force
  - credential-access
url: 'https://github.com/tfutils/tflint'
validated: true
---

# crunch

**Status**: Unverified

## Overview

Crunch is a command-line wordlist generator designed for security testing, particularly for creating custom dictionaries used in brute-force attacks, password cracking, and fuzzing. It allows users to specify character sets, lengths, patterns, and output options to produce targeted wordlists efficiently.

## Description

Crunch supports generating wordlists in combination and permutation modes, making it versatile for offensive security operations. Key capabilities include breaking output into multiple files by size or line count, resume functionality for long-running generations, pattern support for numbers, symbols, and case variations, duplicate limiting, and Unicode character handling. It is commonly used in penetration testing to create tailored wordlists for tools like Hashcat or John the Ripper.

## Features

- Feature 1: Generates combinations and permutations of specified character sets
- Feature 2: Supports output splitting by lines or file size for large wordlists
- Feature 3: Resume capability to restart interrupted generations
- Feature 4: Pattern matching with support for uppercase/lowercase, numbers, and symbols separately
- Feature 5: Options for limiting duplicates and literal characters (@, %, ^)
- Feature 6: Unicode support for international character sets

## Installation

### Requirements

- Linux environment (Kali Linux recommended)
- Basic command-line access

### Install Commands

```bash
# On Kali Linux (pre-installed)
# No action needed

# On Ubuntu/Debian
sudo apt update
sudo apt install crunch

# From source (GitHub)
git clone https://github.com/crunch/crunch.git
cd crunch
make
sudo make install
```

## Basic Usage

```bash
crunch --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -v, --verbose | Enable verbose output |
| -e | Specify end pattern |
| -l | Limit output lines per file |
| -s | Start from specific position |
| -t | Use template pattern |

## Examples

### Example 1: Basic Usage

Generate a simple wordlist:

```bash
crunch 4 6 abcdef -o simple.txt
```

### Example 2: Advanced Usage

Generate with pattern and split files:

```bash
crunch 1 8 -p "password 123" -o patterns/ -l 1000000
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Brute Force]] Brute Force
- [[Unsecured Credentials]] Unsecured Credentials

### Tactics

- [[Credential Access]] Credential Access
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for large file I/O operations creating text files with sequential string patterns
- Detection method 2: Process monitoring for 'crunch' executions in security tools directories
- Detection method 3: Network logs if wordlists are transferred; filesystem scans for .txt files with permutation patterns

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

## References

- Official GitHub: https://github.com/crunch/crunch (Note: Actual repo may vary; search for 'crunch wordlist generator')
- Man page: man crunch

## Related Commands

- [[commands/crunch-generate-basic-wordlist]]
- [[commands/crunch-generate-with-pattern]]
- [[commands/crunch-generate-permutations-with-resume]]
