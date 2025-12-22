---
id: 11bf73a7-50d1-4872-9e5e-cd518794967d
type: tool
verified: true
created_at: '2019-08-28T21:17:41.193186Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - macOS
tags:
  - credential-access
  - password-cracking
  - wordlist-generation
url: 'https://github.com/blark/RSMangler'
commands:
  - '[[commands/rsmangler-basic-mangle]]'
  - '[[commands/rsmangler-with-output-file]]'
  - '[[commands/rsmangler-multiword-permutations]]'
validated: true
---

# rsmangler

**Status**: Unverified

## Overview

rsmangler is a Python-based tool for generating password variations from a wordlist. It creates permutations and acronyms of input words before applying mangling rules similar to those in John the Ripper, making it useful for brute-force attacks and password cracking in red team operations.

## Description

rsmangler processes wordlists by first generating all possible permutations and acronyms (e.g., for "first last" it creates "FirstLast", "FL", etc.), then applies transformations like capitalization, appending numbers, and leetspeak substitutions. This is particularly effective for targeting user-specific passwords derived from names, common phrases, or dictionary words in credential access scenarios.

## Features

- Generates permutations and acronyms from multi-word inputs
- Applies John the Ripper-style mangling rules (e.g., @ for a, 3 for e)
- Filters output by length to match common password policies
- Supports output to files for integration with tools like hashcat
- Lightweight and scriptable for automation in attack chains

## Installation

### Requirements

- Python 3.x
- No additional dependencies beyond standard library

### Install Commands

```bash
# Clone the repository
git clone https://github.com/blark/RSMangler.git
cd RSMangler

# Run directly with Python (no install needed)
python3 rsmangler.py --help
```

For Kali Linux or Ubuntu:

```bash
# Pre-requisites
sudo apt update && sudo apt install git python3

# Clone and use
git clone https://github.com/blark/RSMangler.git
```

## Basic Usage

```bash
python3 rsmangler.py wordlist.txt
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and options |
| -o FILE | Output mangled passwords to FILE |
| --min-length N | Minimum password length |
| --max-length N | Maximum password length |
| -v, --verbose | Enable verbose output for debugging |

## Examples

### Example 1: Basic Usage

```bash
python3 rsmangler.py passwords.txt
```

This generates and prints basic mangled variations from passwords.txt.

### Example 2: Advanced Usage

```bash
python3 rsmangler.py user_names.txt -o mangled_output.txt --min-length 8
```

This creates length-filtered mangles and saves to a file.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Brute Force]] Brute Force
- [[Credentials from Password Stores]] Credentials from Password Stores

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Python processes named rsmangler.py or similar
- Large wordlist files with mangled outputs in temporary directories
- High CPU usage during permutation generation on wordlists
- Network traffic if integrated with online cracking services

## Related Procedures

- [[procedures/Generate-Password-Variations]]
- [[procedures/Offline-Password-Cracking]]

## Related Tools

- [[tools/John-the-Ripper]]
- [[tools/Hashcat]]

## References

- Official GitHub: https://github.com/blark/RSMangler
- John the Ripper documentation for comparable mangling rules
