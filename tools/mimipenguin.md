---
id: 93518ec8-b56c-4175-a267-47cd27a3e398
type: tool
verified: true
created_at: '2019-08-28T21:17:41.545308+00:00'
updated_at: '2023-10-01T12:00:00Z'
platforms:
  - Linux
tags:
  - credential-access
  - linux
  - memory-dump
  - post-exploitation
url: 'https://github.com/huntergregal/mimipenguin'
validated: true
---

# mimipenguin

**Status**: Unverified

## Overview

mimipenguin is a bash script designed to dump clear-text login passwords from the memory of the current Linux desktop user. Inspired by the Windows tool Mimikatz, it targets desktop environment credential stores such as Gnome Keyring, KWallet, and others to extract stored passwords without requiring root privileges.

## Description

This tool scans the current user's session memory for plaintext credentials stored by desktop applications. It is particularly useful in post-exploitation scenarios on Linux systems where an attacker has gained initial shell access as a standard user. mimipenguin supports multiple desktop environments and outputs credentials in a readable format, making it a quick way to harvest passwords for lateral movement or privilege escalation.

## Features

- Feature 1: Dumps passwords from Gnome Keyring, KWallet, and other stores
- Feature 2: No root access required; runs as the current user
- Feature 3: Lightweight bash implementation for easy deployment
- Feature 4: Outputs credentials directly to stdout for piping or logging

## Installation

### Requirements

- Linux system with bash (most distributions)
- Git for cloning the repository
- Target desktop environment (e.g., GNOME, KDE) with active session

### Install Commands

```bash
# Clone the repository
git clone https://github.com/huntergregal/mimipenguin.git

# Navigate to the directory
cd mimipenguin

# Make the script executable
chmod +x mimipenguin.sh
```

On Kali Linux, it can also be installed via apt if available in repositories, but cloning is recommended for the latest version.

## Basic Usage

```bash
./mimipenguin.sh
```

### Common Options

| Option | Description |
|--------|-------------|
| None | The script has no command-line options; it auto-detects and dumps from available stores |
| `--help` | Not supported; refer to the script source for details |

## Examples

### Example 1: Basic Usage

```bash
./mimipenguin.sh
```

This runs the dump and prints any found credentials.

### Example 2: Advanced Usage

Redirect output to a file for later analysis:

```bash
./mimipenguin.sh > dumped_creds.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Password Managers]] Credentials from Password Stores: Keychain
- [[-etc-passwd and -etc-shadow]] OS Credential Dumping: /etc/passwd and /etc/shadow (adapted for desktop stores)

### Tactics

- [[Credential Access]] Credential Access
- [[Privilege Escalation]] Privilege Escalation

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for bash script executions in user home directories with names like mimipenguin.sh
- Detection method 2: File integrity monitoring on keyring files (e.g., ~/.local/share/keyrings/)
- Detection method 3: Process monitoring for unusual memory reads in desktop processes (e.g., gnome-keyring-daemon)
- Detection method 4: Anomaly detection in credential access logs or session dumps

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Mimikatz]] (Windows equivalent)
- [[tools/LaZagne]] (Cross-platform credential dumper)

## References

- Official GitHub: https://github.com/huntergregal/mimipenguin
- Related resources: Mimikatz documentation for conceptual understanding
