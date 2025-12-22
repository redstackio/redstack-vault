---
id: ef462889-0e62-4757-8a54-35bf61d96960
type: tool
verified: true
created_at: '2019-08-28T21:17:22.065289+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
tags:
  - wordlists
  - password-cracking
  - brute-force
  - kali
url: 'https://www.kali.org/tools/wordlists/'
validated: true
---

# Wordlists

**Status**: Unverified

## Overview

The Wordlists package is a collection of dictionary files used in security testing for tasks such as password cracking, brute-force attacks, and fuzzing. It includes the popular rockyou wordlist, which contains over 14 million real-world passwords leaked from a 2009 breach, along with symlinks to other password files available in Kali Linux. This tool is essential for offensive security operations involving credential attacks and is commonly used with tools like Hashcat, John the Ripper, or Hydra.

## Description

Wordlists provide pre-compiled lists of common passwords, usernames, and other strings that can be used to test the strength of authentication mechanisms. The package organizes these files in /usr/share/wordlists/ and includes compressed versions to save space. Key files include rockyou.txt (common passwords), dirb (web directories), and various others for specific use cases like SQL injection payloads or user enumeration. The installation size is approximately 134 MB, making it lightweight yet comprehensive for red team exercises.

## Features

- Access to rockyou.txt: A massive list of real leaked passwords for offline cracking.
- Symlinks to Kali's built-in password files: Easy access to dirbuster, fasttrack, and more without manual downloads.
- Support for multiple formats: Plaintext, compressed (.gz), and categorized lists (e.g., by length or type).
- Integration with cracking tools: Directly usable as input for GPU/CPU-based password recovery.

## Installation

### Requirements

- A Debian-based Linux distribution (Kali Linux recommended).
- Root or sudo access for package installation.
- At least 150 MB free disk space.

### Install Commands

```bash
sudo apt update
sudo apt install wordlists
```

After installation, the wordlists are available in /usr/share/wordlists/. The rockyou file is compressed by default (rockyou.txt.gz).

## Basic Usage

```bash
ls /usr/share/wordlists/
```

This lists all available wordlists and directories.

### Common Options

Wordlists are files, so no direct options, but common operations include decompression and statistics:

| Operation | Description |
|-----------|-------------|
| `gunzip` | Decompress .gz files for use |
| `wc -l` | Count lines (passwords) in a list |
| `head -n 10` | View first 10 entries |

## Examples

### Example 1: Decompress and Inspect Rockyou

First, decompress the rockyou wordlist:

```bash
sudo gunzip /usr/share/wordlists/rockyou.txt.gz
```

Then, check the number of passwords:

```bash
wc -l /usr/share/wordlists/rockyou.txt
```

### Example 2: Use in Password Cracking (with Hashcat)

Pipe the wordlist to a cracking tool:

```bash
hashcat -m 0 -a 0 hashes.txt /usr/share/wordlists/rockyou.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Brute Force]] Brute Force
- [[Valid Accounts]] Valid Accounts

### Tactics

- [[Persistence]] Persistence
- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- File access logs showing reads from /usr/share/wordlists/.
- High CPU/GPU usage during cracking sessions with dictionary inputs.
- Network traffic if wordlists are downloaded or shared (e.g., via scp or wget).
- Process monitoring for tools like hashcat or john referencing wordlist paths.

## Related Commands

- [[commands/decompress-rockyou-wordlist]]
- [[commands/list-available-wordlists]]
- [[commands/wordlist-line-count]]

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
- [[tools/Hydra]]

## References

- Official Kali Documentation: https://www.kali.org/tools/wordlists/
- Rockyou Dataset: https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
- SecLists Alternative: https://github.com/danielmiessler/SecLists
