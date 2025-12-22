---
id: 933f2af6-2bbd-4805-b21b-1fc7df7df6d6
name: hashid
type: tool
verified: true
created_at: '2019-08-28T21:17:26.864088+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
commands:
  - '[[commands/hashid-identify-hashes-in-file]]'
tags:
  - cryptography
platforms:
  - Linux
url: 'https://github.com/chriscaswell/hashID'
validated: true
---

# hashid

**Status**: Unverified

## Overview

hashid is a Python-based tool designed for identifying over 210 unique hash types using regular expressions. It supports analyzing single hashes, parsing individual files, or scanning entire directories to detect hash formats. The tool is particularly useful in offensive security for quickly categorizing captured credentials or password dumps, enabling selection of appropriate cracking tools like hashcat or John the Ripper. It can also output compatible modes for these crackers.

## Description

hashid leverages pattern matching to recognize hash algorithms without requiring decryption or computation. It handles common formats like MD5, SHA-1, bcrypt, and crypt variants, making it an essential first step in password cracking workflows. The tool is lightweight, cross-platform compatible via Python, and integrates well with other security tools for credential analysis during red team engagements or forensic investigations.

## Features

- Feature 1: Identifies over 210 hash types using regex patterns for fast, non-computational detection.
- Feature 2: Processes single strings, files, or directories recursively.
- Feature 3: Outputs hashcat modes and John the Ripper formats for seamless integration with cracking tools.
- Feature 4: Supports mode filtering to focus on specific cracker compatibility.
- Feature 5: Command-line interface with options for verbose output and encoding specifications.

## Installation

### Requirements

- Python 3.x
- pip for dependency installation

### Install Commands

```bash
# Clone the repository
sudo apt update && sudo apt install git python3-pip -y
git clone https://github.com/chriscaswell/hashID.git
cd hashID

# Install dependencies
pip3 install -r requirements.txt

# Make executable (optional, for direct use)
chmod +x hashID.py

# For Kali Linux (pre-built package available)
sudo apt install hashid -y
```

On Kali Linux, hashid is available in the repositories and can be installed directly via apt for immediate use.

## Basic Usage

```bash
hashid --help
```

This displays the help menu with all available options, including file/directory modes and output formats.

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show the help message and exit |
| `-m` | Include hashcat modes in output |
| `-j` | Include John the Ripper formats in output |
| `-d $_DIRECTORY` | Scan all files in the specified directory |
| `-e $_ENCODING` | Specify file encoding (default: UTF-8) |

## Examples

### Example 1: Basic Usage

Identify a single hash string:

```bash
hashid "5f4dcc3b5aa765d61d8327deb882cf99"
```

Output: [+] MD5

### Example 2: Advanced Usage

Scan a file with hashcat mode output:

```bash
hashid -m hashes.txt
```

This analyzes 'hashes.txt' and includes hashcat mode numbers (e.g., 0 for MD5) for direct use in cracking commands.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials (for identifying credential formats during collection)
- [[Brute Force]] Brute Force (aiding in selecting cracking methods)

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for Python processes named 'hashID.py' or 'hashid' executions in security event logs.
- Detection method 2: Look for file access patterns on credential dumps (e.g., .txt, .dmp files) combined with regex pattern matching in process arguments.
- Detection method 3: Network indicators if used in conjunction with remote file transfers; otherwise, primarily host-based via command-line auditing.

## Related Procedures

- [[procedures/Extract-and-Identify-Credentials-from-Dump]]
- [[procedures/Crack-Password-Hashes-with-Hashcat]]

## Related Tools

- [[tools/Hashcat]]
- [[tools/john-the-ripper]]

## References

- Official GitHub Repository: https://github.com/chriscaswell/hashID
- Python Package Index (if pip-installed): https://pypi.org/project/hashID/
