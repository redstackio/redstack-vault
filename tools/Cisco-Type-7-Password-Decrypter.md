---
id: 6ac896ad-0f13-46d6-9bb9-58925a0a55c1
name: Cisco-Type-7-Password-Decrypter
type: tool
verified: true
created_at: '2020-02-20T05:07:07.355399+00:00'
updated_at: '2023-05-30T19:57:39.419103+00:00'
commands:
  - '[[commands/ciscot7-decrypt-password]]'
tags:
  - '[[Cryptography]]'
  - '[[known vulnerability]]'
  - '[[Network]]'
  - '[[credentials]]'
  - '[[cisco]]'
platforms:
  - Linux
  - Windows
  - macOS
url: 'https://github.com/search?q=cisco+type+7+decrypt'
validated: true
---

# Cisco-Type-7-Password-Decrypter

**Status**: ✓ Verified

## Overview

The Cisco Type 7 Password Decrypter is a lightweight Python script designed to decrypt or encrypt passwords obfuscated using Cisco IOS Type 7 encryption. This weak, reversible algorithm is commonly used in Cisco device configurations to obscure passwords in plain text files, such as those exported from routers or switches. It is useful in penetration testing, network auditing, and recovery scenarios where Type 7 hashed passwords need to be revealed for credential analysis or reconfiguration.

## Description

Cisco IOS Type 7 passwords use a simple XOR-based obfuscation with a fixed key, making them easily decryptable with the known algorithm. The tool implements this algorithm in Python, supporting both decryption (primary use) and encryption modes. It processes the hexadecimal string representation of the Type 7 password and outputs the plaintext equivalent. This tool is particularly valuable for red teamers analyzing network device configs obtained via reconnaissance or initial access, as it can quickly yield usable credentials without advanced cracking tools.

## Features

- Decrypts Cisco Type 7 passwords using the public XOR algorithm
- Supports encryption of plaintext to Type 7 format
- Simple command-line interface with minimal dependencies
- Works with Python 2 or 3
- Handles standard hex-encoded inputs from Cisco configs

## Installation

### Requirements

- Python 2.7 or 3.x (standard library only, no external dependencies)

### Install Commands

The tool is a single Python script (ciscot7.py). Download it from a trusted source or create it manually:

```bash
# Download or clone from repository (example GitHub search for implementations)
# For manual creation, save the script content to ciscot7.py

# On Kali/Ubuntu:
apt update && apt install python3  # If not pre-installed

# On Windows:
# Use Python installer from python.org

# On macOS:
brew install python  # If using Homebrew
```

To obtain the script:
1. Search for "cisco type 7 decrypt python" on GitHub and clone a verified repository, e.g.:
```bash
git clone https://github.com/your-repo/ciscot7.git
cd ciscot7
```
2. Or, create ciscot7.py with the standard implementation (public domain code available online).

## Basic Usage

```bash
python3 ciscot7.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-d, --decrypt` | Decrypt mode (default) |
| `-e, --encrypt` | Encrypt mode |
| `-p, --password` | Input password (hex string for decrypt, plaintext for encrypt) |
| `-h, --help` | Show help message |

## Examples

### Example 1: Basic Decryption

Decrypt a Type 7 password from a Cisco config:

```bash
python3 ciscot7.py -d -p 01000307490e121c60
```

### Example 2: Encryption

Encrypt plaintext to Type 7 format:

```bash
python3 ciscot7.py -e -p "mysecretpassword"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials (for extracting weak/obfuscated credentials from configs)
- [[Credential Dumping]] OS Credential Dumping (in network device contexts)

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Python processes executing scripts with "ciscot7" or similar names
- Command-line arguments containing Cisco hex strings (e.g., patterns like 0[0-9A-F]{2}...)
- File access to downloaded Python scripts or config files with Type 7 patterns
- Network logs showing config exports from Cisco devices prior to decryption attempts

## Related Procedures

No related procedures documented yet.

## Related Tools

- [[tools/john-the-ripper]] (for stronger hash cracking)
- [[tools/Hashcat]] (GPU-accelerated cracking, though not needed for Type 7)
- [[config-extractors]] (tools for parsing Cisco configs)

## References

- Cisco IOS Password Encryption Documentation: https://www.cisco.com/c/en/us/support/docs/ios-nx-os-software/ios-software-releases-121-mainline/46930-type7.html
- Public Algorithm Explanation: Various GitHub repos and security blogs
