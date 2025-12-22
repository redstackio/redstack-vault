---
id: 439c4a07-4af0-46c1-911b-0e2cafd3c7c9
type: tool
verified: true
created_at: '2020-02-28T19:44:43.267568+00:00'
updated_at: '2023-05-30T19:46:57.361580+00:00'
platforms:
  - Linux
tags:
  - convert
  - Cryptography
url: 'https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html'
commands:
  - '[[commands/puttygen-convert-ppk-to-pem]]'
validated: true
---

# puttygen

**Status**: ✓ Verified

## Overview

puttygen is a public-key generator and key management tool from the PuTTY suite. It is primarily used for generating RSA/DSA/ECDSA/Ed25519 SSH key pairs, modifying existing keys (e.g., adding or changing passphrases), and converting between different key formats, such as PuTTY's .ppk to OpenSSH's .pem. In security testing, it is commonly employed to prepare SSH keys for cross-platform compatibility during remote access, lateral movement, or persistence operations.

## Description

puttygen provides a graphical interface on Windows but can be run in command-line mode on Linux for automation. Key functionalities include key generation with customizable bit lengths, public key extraction, and format conversions essential for tools like OpenSSH, which do not natively support PuTTY formats. It supports passphrase protection to secure private keys and is lightweight, making it suitable for inclusion in penetration testing toolkits.

## Features

- Feature 1: Generate new public/private key pairs in various algorithms (RSA, DSA, ECDSA, Ed25519) with selectable key sizes.
- Feature 2: Convert keys between PuTTY (.ppk), OpenSSH (.pem), and other formats like SSH.com or PKCS#8.
- Feature 3: Modify keys by adding, removing, or changing passphrases without regenerating the key.
- Feature 4: Extract public keys from private keys for authorized_keys files.
- Feature 5: Command-line operation for scripting and batch processing.

## Installation

### Requirements

- Standard Unix-like environment with build essentials (for compilation if needed).
- PuTTY source or pre-built binaries.

### Install Commands

```bash
# On Debian/Ubuntu (includes putty-tools package)
apt update && apt install putty-tools

# On Kali Linux (pre-installed or via apt)
apt install putty-tools

# Manual build from source (if needed)
# Download from official site, then:
# make -C unix
```

## Basic Usage

```bash
puttygen --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -t | Specify key type (e.g., rsa, dsa, ecdsa, ed25519) |
| -b | Specify number of bits in the key (e.g., 2048) |
| -O | Specify output type (e.g., private-openssh for PEM) |
| -o | Output file name |
| -P | Do not prompt for passphrase |

## Examples

### Example 1: Basic Usage

Generate a new 2048-bit RSA key:

```bash
puttygen -t rsa -b 2048 -o mykey.ppk
```

### Example 2: Advanced Usage

Convert a PPK to PEM (see related command):

```bash
puttygen mykey.ppk -O private-openssh -o mykey.pem
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Private Keys]] Private Keys (for key conversion in credential access scenarios)

### Tactics

- [[Persistence]] Persistence (SSH key management for backdoors)
- [[Lateral Movement]] Lateral Movement (SSH access preparation)

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for puttygen process execution in logs (e.g., via Sysmon or auditd).
- Detection method 2: File system changes to .ppk or .pem files in temporary directories.
- Detection method 3: Network anomalies if generated keys are used for unauthorized SSH connections.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/openssh]]
- [[tools/ssh]]

## References

- Official PuTTY documentation: https://www.chiark.greenend.org.uk/~sgtatham/putty/docs.html
- PuTTY download: https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html
