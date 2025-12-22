---
id: 9c1d35a1-c6e8-47b5-92ca-b069813e8c95
name: ssh2john
type: tool
verified: true
created_at: '2020-02-18T19:16:01.973601+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
tags:
  - brute-force
  - cryptography
url: >-
  https://github.com/magnumripper/JohnTheRipper/raw/bleeding-jumbo/run/ssh2john.py
commands:
  - '[[commands/ssh2john-extract-hash-from-encrypted-ssh-key]]'
validated: true
---

# ssh2john

**Status**: ✓ Verified

## Overview

ssh2john is a Python script included with John the Ripper, designed to extract passphrase hashes from encrypted SSH private keys. It converts the key file into a format compatible with John the Ripper for offline cracking. This tool is particularly useful in credential access scenarios where attackers obtain encrypted SSH keys and need to recover weak passphrases. Note that the resulting hashes are specifically formatted for John the Ripper and are not compatible with other crackers like Hashcat. It supports RSA, DSA, and EC key types.

Category: Credential Access

## Description

ssh2john processes encrypted private SSH key files (typically in OpenSSH format) by parsing the key structure and extracting the encryption components, such as the salt and initialization vector, into a crackable hash. This enables brute-force or dictionary attacks against the passphrase protecting the key. The tool is lightweight and runs via Python, making it suitable for use in penetration testing, red team operations, or forensic analysis of compromised systems. It requires the key to be passphrase-protected; unencrypted keys will not produce a usable hash.

## Features

- Extracts hashes from RSA, DSA, and ECDSA private keys
- Outputs in John the Ripper-specific format ($sshng$ prefix)
- Supports OpenSSH key formats
- Integrates seamlessly with John the Ripper for cracking
- Cross-platform compatibility via Python

## Installation

### Requirements

- Python 2.7 or 3.x (depending on John the Ripper version)
- John the Ripper (for subsequent cracking)

### Install Commands

#### Kali Linux
ssh2john is pre-installed with John the Ripper:
```bash
# Already available at /usr/share/john/ssh2john.py
john --help  # Verify installation
```

#### Ubuntu/Debian
```bash
sudo apt update
sudo apt install john
# ssh2john.py will be at /usr/share/john/ssh2john.py
```

#### Windows
Download John the Ripper Jumbo edition from the official repository and extract. ssh2john.py is in the run/ directory. Ensure Python is installed.

#### Manual Download (Any Platform)
```bash
wget https://github.com/magnumripper/JohnTheRipper/raw/bleeding-jumbo/run/ssh2john.py
chmod +x ssh2john.py
```

## Basic Usage

```bash
python ssh2john.py <encrypted_key_file>
```

### Common Options

| Option | Description |
|--------|-------------|
| None (script args) | Input file path only; output to stdout |
| > output.txt | Redirect hash to file for John the Ripper |

## Examples

### Example 1: Basic Usage

Extract hash from an encrypted key and save to file:
```bash
python /usr/share/john/ssh2john.py id_rsa.enc > ssh_key_hash.txt
```

### Example 2: Advanced Usage

Process a key from a custom path:
```bash
python ssh2john.py /path/to/user/.ssh/id_dsa > extracted_hash.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials
- [[Brute Force]] Brute Force

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of ssh2john.py in unusual locations (e.g., /tmp/ or user downloads)
- Python processes invoking ssh2john.py on key files
- File system monitoring for access to .ssh directories followed by hash extraction
- John the Ripper logs or processes cracking $sshng$ hashes

## Related Procedures

No direct procedure links available in this batch.

## Related Tools

- [[tools/John the Ripper]]
- [[tools/Hashcat]] (Note: Incompatible with ssh2john output)

## References

- Official John the Ripper Repository: https://github.com/openwall/john
- Jumbo Edition (includes ssh2john): https://github.com/magnumripper/JohnTheRipper

*Last updated: 2023-10-01*
