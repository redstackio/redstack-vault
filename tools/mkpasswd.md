---
type: tool
description: >-
  mkpasswd is a utility for generating hashed passwords in various formats
  commonly used in Unix-like systems, such as those found in /etc/shadow files.
url: 'https://manpages.debian.org/bullseye/whois/mkpasswd.1.en.html'
tags:
  - cryptography
  - password-hashing
  - operating-systems
platforms:
  - Linux
verified: true
validated: true
---

# mkpasswd

**Status**: ✓ Verified

## Overview

mkpasswd is a command-line tool used to generate hashed passwords from plaintext input. It supports multiple hashing algorithms typically used in Unix-like operating systems for password storage, such as SHA-512, SHA-256, MD5, and DES-based crypt. This tool is commonly used in security testing for creating password hashes, simulating /etc/shadow entries, or preparing data for password cracking exercises.

## Description

The tool takes a plaintext password and optional salt, then applies the specified hashing method to produce an encrypted string. It is part of the 'whois' package on Debian-based systems and is useful for red team operations involving credential manipulation, hash generation for testing authentication bypasses, or creating realistic password files for lab environments. Available methods include sha512crypt (SHA-512), sha256crypt (SHA-256), md5crypt (MD5), and descrypt (DES-based).

## Features

- Support for multiple hashing algorithms: SHA-512, SHA-256, MD5, DES
- Customizable salt length and characters
- Round specification for stronger hashing (e.g., more iterations)
- Output in standard crypt format compatible with /etc/shadow

## Installation

### Requirements

- A Debian-based Linux distribution (e.g., Ubuntu, Kali)
- Root or sudo access for package installation

### Install Commands

```bash
# On Debian/Ubuntu/Kali
sudo apt update
sudo apt install whois
```

mkpasswd is pre-installed on many Kali Linux distributions.

## Basic Usage

```bash
mkpasswd --help
```

This displays the help message with all available options and algorithms.

### Common Options

| Option | Description |
|--------|-------------|
| -m, --method | Specify the hashing method (e.g., sha-512, sha-256, md5, des) |
| -S, --salt | Provide a custom salt string |
| -R, --rounds | Number of hashing rounds (higher for stronger hashes) |
| -h, --help | Show help message |
| -V, --version | Display version information |

## Examples

### Example 1: Basic Usage

Generate a SHA-512 hash with a custom salt.

See [[commands/mkpasswd-generate-sha512-hash]] for details.

### Example 2: Advanced Usage

```bash
mkpasswd -m sha-256 -S mysalt -R 50000 mypassword
```

This generates a SHA-256 hash with 50,000 rounds for increased security.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials (for generating or testing credential hashes)
- [[Brute Force]] Brute Force (in contexts of hash preparation for cracking)

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for 'mkpasswd' executions in security logs
- Unusual hash generation activity in forensic analysis of /tmp or user directories
- Integration with password cracking tools like Hashcat, which may log input sources

## Related Procedures

No related procedures documented yet.

## Related Tools

- [[tools/Hashcat]] (for cracking generated hashes)
- [[tools/john-the-ripper]] (alternative password cracking tool)

## References

- Official man page: https://manpages.debian.org/bullseye/whois/mkpasswd.1.en.html
- Debian package details: https://packages.debian.org/whois
