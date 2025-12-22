---
id: 4cedf688-f7bc-478e-a8c6-f1d443159307
name: findmyhash
type: tool
verified: true
created_at: '2019-08-28T21:17:26.874352+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - hash-cracking
  - credential-access
  - password-recovery
url: 'https://github.com/brannondorsey/findmyhash'
commands:
  - '[[commands/findmyhash-crack-hash-online]]'
  - '[[commands/findmyhash-crack-hash-offline]]'
validated: true
---

# findmyhash

**Status**: Unverified

## Overview

findmyhash is a Python-based tool for cracking password hashes by querying online databases and performing offline dictionary attacks. It supports a wide range of hash algorithms including MD4, MD5, SHA1, SHA256, NTLM, LM, and others. Commonly used in penetration testing for credential access during post-exploitation phases.

## Description

The tool automates hash cracking by first attempting to identify the hash type and then querying multiple online services (e.g., CrackStation, md5decrypter, netmd5) for quick lookups. If online methods fail, it supports offline modes using local wordlists for dictionary or brute-force attacks. It is particularly useful for cracking weak or common passwords from captured hashes in scenarios like NTLM relay attacks or database dumps.

## Features

- Automatic hash type detection from supported algorithms: MD4, MD5, SHA1, SHA224, SHA256, SHA384, SHA512, RMD160, GOST, WHIRLPOOL, LM, NTLM, MySQL, Cisco7, Juniper, LDAP_MD5, LDAP_SHA1.
- Online cracking via multiple public databases.
- Offline dictionary and brute-force modes.
- Charset-based mutations for advanced cracking.
- Multi-threaded lookups for efficiency.

## Installation

### Requirements

- Python 2.7 or 3.x
- pip
- Internet access for online mode

### Install Commands

On Kali Linux (pre-installed in some repos, but for latest):

```bash
sudo apt update && sudo apt install python3-pip
pip3 install findmyhash
```

From source (recommended for latest features):

```bash
git clone https://github.com/brannondorsey/findmyhash.git
cd findmyhash
python setup.py install
```

On Ubuntu:

```bash
sudo apt install python3-pip git
pip3 install findmyhash
```

On macOS:

```bash
brew install python3
pip3 install findmyhash
```

On Windows: Use Python installer and pip as above.

## Basic Usage

```bash
findmyhash.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --hash | Hash to crack |
| -t, --type | Specify hash type (auto-detect default) |
| -m, --mode | Cracking mode (0: dict, 1: permute, 2: brute) |
| -w, --wordlist | Path to wordlist for offline mode |
| -c, --charset | Charset for mutations (e.g., l=lowercase) |
| -l, --length | Password length for brute-force |

## Examples

### Example 1: Basic Online Cracking

```bash
findmyhash.py -h 5f4dcc3b5aa765d61d8327deb882cf99
```

This attempts online lookup for the MD5 hash of 'password'.

### Example 2: Offline Dictionary Attack

```bash
findmyhash.py -h 5f4dcc3b5aa765d61d8327deb882cf99 -w /usr/share/wordlists/rockyou.txt -m 0
```

Uses rockyou.txt for dictionary attack.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Brute Force]] Brute Force
- [[Unsecured Credentials]] Unsecured Credentials

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to known hash cracking services (e.g., crackstation.net, md5decrypter.co.uk).
- Python processes with 'findmyhash' in command line arguments (monitor via Sysmon or process auditing).
- Unusual outbound DNS queries to cracking domains.
- File system artifacts like downloaded wordlists or temporary hash files.

## Related Procedures

- [[procedures/Identify-and-Crack-Hashes]]
- [[procedures/Extract-and-Cracking-NTLM-Hashes]]

## Related Tools

- [[tools/Hashcat]]
- [[tools/john-the-ripper]]

## References

- Official GitHub: https://github.com/brannondorsey/findmyhash
- Supported Algorithms: RFC 1320 (MD4), RFC 1321 (MD5), etc.
