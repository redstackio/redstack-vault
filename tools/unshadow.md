---
id: 2a6cd084-3baa-4125-a6e6-71a0338cce6f
type: tool
verified: true
created_at: '2019-08-28T21:17:34.627707+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
tags:
  - credential-access
  - password-cracking
  - hash-extraction
url: 'https://www.openwall.com/john/'
commands:
  - '[[commands/unshadow-combine-passwd-shadow]]'
validated: true
---

# unshadow

**Status**: Unverified

## Overview

unshadow is a utility included with John the Ripper, a popular password cracking tool. It is specifically designed to combine the /etc/passwd and /etc/shadow files on Unix-like systems (primarily Linux) into a single file format that includes both user account details and encrypted password hashes. This prepared file can then be fed into password crackers like John the Ripper for offline brute-force or dictionary attacks. unshadow is commonly used in penetration testing and red team operations for credential access after gaining initial system access.

## Description

unshadow addresses the challenge of Unix password storage, where sensitive hash data is separated into the shadow file for security. By merging these files, unshadow creates a crackable format without needing root privileges to read shadow (assuming the attacker already has access to both files). It supports various hash types used in modern Linux distributions, including SHA-512, SHA-256, and older DES-based crypt hashes. As part of John the Ripper, unshadow benefits from the suite's optimizations but focuses solely on the extraction and formatting step, not the cracking itself.

## Features

- Feature 1: Merges passwd and shadow files into John-compatible format
- Feature 2: Handles multiple hash types (DES, MD5, SHA-256, SHA-512)
- Feature 3: Simple command-line interface with output redirection support
- Feature 4: No additional dependencies beyond John the Ripper installation

## Installation

### Requirements

- Linux system (e.g., Ubuntu, Kali)
- Root or sufficient privileges to read /etc/shadow (often requires initial compromise)
- John the Ripper package

### Install Commands

```bash
# On Kali Linux (pre-installed)
sudo apt update && sudo apt install john

# On Ubuntu
sudo apt update && sudo apt install john

# From source (for latest version)
wget https://www.openwall.com/john/j/john-1.9.0-jumbo-1-win64.zip  # Adjust for platform
unzip john-*.zip
cd john/run
./unshadow  # Test
```

## Basic Usage

```bash
unshadow --help
```

### Common Options

| Option | Description |
|--------|-------------|
| No options needed for basic merge | Simply provide input files |
| Output redirection | Use > to save to file (e.g., > hashes.txt) |

## Examples

### Example 1: Basic Usage

```bash
unshadow /etc/passwd /etc/shadow > combined.txt
```

This creates a file ready for john --wordlist=rockyou.txt combined.txt

### Example 2: Advanced Usage

```bash
unshadow passwd_copy shadow_copy > extracted_hashes.txt
```

Use with copied files to avoid direct system access.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Credential Dumping]] OS Credential Dumping
- [[Credentials in Files]] Password Policy Discovery (for hash extraction prep)

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for access to /etc/shadow by non-root processes (e.g., via auditd logs)
- Detection method 2: File creation events for combined hash files (e.g., via Sysmon or file integrity monitoring)
- Detection method 3: Process execution of 'unshadow' in command-line logs

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

- Official John the Ripper documentation: https://www.openwall.com/john/doc/
- unshadow man page: man unshadow
