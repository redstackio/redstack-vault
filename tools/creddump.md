---
id: adffcae4-5128-4f20-9cde-4fb0731f5be3
name: creddump
type: tool
verified: true
created_at: '2019-08-28T21:17:29.357790+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - credential-access
  - offline-extraction
  - windows-registry
url: 'https://github.com/Neohapsis/creddump'
validated: true
---

# creddump

**Status**: Unverified

## Overview

creddump is a Python-based tool for extracting various credentials and secrets from offline Windows registry hives. It supports dumping LM and NT hashes (protected by SYSKEY), cached domain passwords, and LSA secrets. This tool is platform-independent and performs offline analysis, making it useful for forensic investigations, red team operations, and credential recovery in controlled environments. It replicates the functionality of tools like bkhive/samdump2, cachedump, and lsadump2 but in a unified, open-source Python package.

## Description

creddump operates by parsing Windows registry files (SYSTEM, SAM, SECURITY, etc.) extracted from a target system. It requires the registry hives to be available offline, typically obtained via tools like RegRipper or direct file copy during post-exploitation. The tool decrypts SYSKEY-protected data using the extracted system key and outputs hashes or secrets in formats compatible with cracking tools like Hashcat or John the Ripper. Common use cases include:
- Recovering local user hashes from compromised Windows machines.
- Extracting cached domain credentials for lateral movement.
- Dumping LSA secrets for service account passwords or Kerberos keys.

It does not require running on Windows and can be executed from Linux or macOS environments.

## Features

- Offline extraction of LM/NT hashes from SAM hive.
- Decryption of cached domain logon credentials.
- Parsing and dumping of LSA secrets from SECURITY hive.
- SYSKEY extraction from SYSTEM hive.
- Output in crackable formats (e.g., NTLM hashes).
- Platform-independent Python implementation.

## Installation

### Requirements

- Python 2.7 (compatible with Python 3 with minor adjustments).
- No additional dependencies beyond standard library (uses PyCrypto for decryption).

### Install Commands

```bash
# Clone from GitHub mirror (original Google Code archive)
git clone https://github.com/Neohapsis/creddump.git
cd creddump

# No formal install; run scripts directly
python bkhive.py --help  # Test installation
```

On Kali Linux, it may be available via apt, but manual clone is recommended for the latest version:
```bash
apt update && apt install python2
# Then clone as above
```

For macOS:
```bash
brew install python@2
# Then clone and run
```

## Basic Usage

```bash
python bkhive.py SYSTEM output.syskey  # Extract SYSKEY
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message for the script |
| No verbose flag; output is to stdout by default |

## Examples

### Example 1: Basic Usage - Extract SYSKEY

```bash
python bkhive.py ./hives/SYSTEM syskey.txt
```

This extracts the SYSKEY needed for decrypting other hives.

### Example 2: Advanced Usage - Dump Cached Credentials

First extract SYSKEY, then:
```bash
python cachedump.py syskey.txt ./hives/CACHE/cachefile output.hashes
```

This dumps cached domain hashes.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Credential Dumping]] OS Credential Dumping
- [[Boot or Logon Autostart Execution]] Boot or Logon Autostart Execution (for LSA secrets context)

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of extracted registry hives (SYSTEM, SAM, SECURITY) on analyst machines.
- Python processes invoking creddump scripts during forensic analysis.
- Output files with .hashes or .syskey extensions.
- Network transfer of registry hives (if obtained remotely).

Since it's offline, detection focuses on the acquisition phase (e.g., [[Data from Local System]] Data from Local System).

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Impacket-Secedit]]
- [[tools/Mimikatz]]
- [[tools/regripper]]

## References

- Official GitHub: https://github.com/Neohapsis/creddump
- Original project: https://code.google.com/archive/p/creddump/
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1003/
