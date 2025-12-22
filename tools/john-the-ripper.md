---
id: 79597cc8-1f13-43bb-9d1d-e2d4f75c8038
name: John-the-Ripper
type: tool
verified: true
created_at: '2019-08-28T21:17:18.565076+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
commands:
  - '[[commands/john-dictionary-attack-on-hash-file]]'
platforms:
  - Linux
  - Windows
tags:
  - Brute-Force
url: 'https://www.openwall.com/john/'
validated: true
---

# John-the-Ripper

**Status**: Unverified

## Overview

John the Ripper is a fast password cracker that supports numerous hash types and cracking modes, including dictionary attacks, brute-force, and hybrid methods. It is widely used in offensive security for offline password recovery from extracted hashes obtained during penetration testing or forensic analysis.

## Description

John the Ripper is an open-source tool designed for cracking passwords from their hashed forms. It supports a vast array of hash formats, including those from Unix/Linux systems (e.g., MD5, SHA), Windows (e.g., NTLM), and various applications (e.g., PDF, ZIP). Users provide a file of hashes and a wordlist or rules, and John attempts to match the hashes by generating and testing candidate passwords. It is particularly effective for weak passwords and is often used in red team operations to escalate access after credential dumping.

## Features

- Feature 1: Supports over 100 hash types, including custom formats via plugins.
- Feature 2: Multiple cracking modes: wordlist/dictionary, incremental (brute-force), and Markov-based hybrid attacks.
- Feature 3: Highly optimized for multi-core processors and GPU acceleration via external drivers like OpenCL.
- Feature 4: Session management to resume interrupted cracking sessions.
- Feature 5: Custom rules for wordlist mutation (e.g., appending numbers, changing case).

## Installation

### Requirements

- A compatible operating system (Linux or Windows).
- Sufficient CPU/GPU resources for intensive cracking tasks.
- Wordlists (e.g., rockyou.txt) for dictionary attacks.

### Install Commands

#### Kali Linux / Ubuntu

John the Ripper is pre-installed on Kali Linux. For Ubuntu:

```bash
sudo apt update
sudo apt install john
```

#### Windows

1. Download the latest version from the official site: [Openwall John the Ripper](https://www.openwall.com/john/).
2. Extract the archive to a directory (e.g., C:\JohnTheRipper).
3. Add the `run` directory to your PATH or navigate to it to execute `john.exe`.

## Basic Usage

```bash
john --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Display help message and exit |
| --wordlist=FILE | Use a specific wordlist for dictionary attacks |
| --format=FORMAT | Specify the hash format (e.g., raw-md5, nt) |
| --incremental | Perform brute-force incremental mode |
| --rules | Apply wordlist rules for mutations |
| --show | Display cracked passwords from a hash file |

## Examples

### Example 1: Basic Usage

Perform a dictionary attack on a hash file:

```bash
john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt
```

### Example 2: Advanced Usage

Crack with format specification and show results:

```bash
john --wordlist=rockyou.txt --format=sha512crypt hashes.txt
john hashes.txt --show
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Brute Force]] Brute Force
- [[Password Guessing]] Password Guessing
- [[Password Cracking]] Password Cracking

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for high CPU/GPU usage on systems without typical workloads.
- Detection method 2: Log file accesses to common wordlists (e.g., rockyou.txt) or hash dumps.
- Detection method 3: Network indicators if hashes are exfiltrated prior to cracking; process monitoring for `john` executable.

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
- [[tools/Hydra]]

## References

- Official website: https://www.openwall.com/john/
- GitHub repository: https://github.com/openwall/john
- Documentation: Included in the distribution or online at Openwall.
