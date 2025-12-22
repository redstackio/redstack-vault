---
id: 468e1698-65e1-4035-b2ad-60dbf363a0be
name: PwDump7
type: tool
verified: true
created_at: '2019-08-28T21:17:41.902591+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
commands:
  - '[[commands/pwdump7-dump-ntlm-lm-hashes-local-windows]]'
platforms:
  - Windows
tags:
  - administrator
  - cryptography
  - ntlm
url: 'https://www.tarasco.org/security/pwdump_7/pwdump7.zip'
validated: true
---

# PwDump7

**Status**: Unverified

## Overview

PwDump7 is a lightweight password dumping utility designed for Windows systems. It specializes in extracting NTLM and LM hashes from the local SAM (Security Account Manager) and SYSTEM registry hives by directly accessing the binary files on the filesystem, bypassing some traditional API restrictions.

## Description

PwDump7 differs from other Windows password extraction tools by not relying on Windows APIs like LSASS dumping. Instead, it uses custom filesystem drivers (Rkdetector for NTFS and FAT32) to read the SAM and SYSTEM files directly. This makes it useful in scenarios where API-based dumping is blocked by antivirus or security software. It is particularly effective for post-exploitation on compromised Windows hosts to obtain local account hashes for offline cracking or pass-the-hash attacks.

## Features

- Feature 1: Direct extraction of SAM and SYSTEM files without API calls
- Feature 2: Support for NTFS and FAT32 filesystems via Rkdetector drivers
- Feature 3: Output in raw format compatible with hash cracking tools like Hashcat or John the Ripper
- Feature 4: Lightweight and portable; no installation required beyond extraction

## Installation

### Requirements

- Windows operating system (XP and later)
- Administrative privileges recommended for full access
- Rkdetector drivers (included in the download)

### Install Commands

Download the ZIP archive and extract it to a directory on the target Windows system. No formal installation is needed; simply run the executable from the extracted folder.

```cmd
# Download (manual step)
# Extract pwdump7.zip to C:\temp\pwdump7

# No additional commands required
```

For use on the target, transfer the extracted files via SMB, USB, or other means.

## Basic Usage

```cmd
PwDump7.exe
```

### Common Options

| Option | Description |
|--------|-------------|
| None | Default run dumps local hashes; no command-line options exposed |
| -h, --help | Not available; consult documentation for advanced usage |

## Examples

### Example 1: Basic Usage

Run on a local Windows system to dump hashes:

```cmd
PwDump7.exe
```

### Example 2: Advanced Usage

Redirect output to a file for later analysis:

```cmd
PwDump7.exe > hashes.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Security Account Manager]] Security Account Manager

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitoring for access to SAM and SYSTEM files (e.g., via Sysmon Event ID 11 for file creation/deletion)
- Detection method 2: Antivirus signatures for PwDump7.exe or Rkdetector drivers
- Detection method 3: Process monitoring for unusual executable runs in user directories
- Detection method 4: Hash dumps in temporary files or network exfiltration attempts

## Related Procedures

No related procedures currently linked.

## Related Tools

- [[tools/Mimikatz]] (for LSASS dumping)
- [[SecretsDump]] (Impacket tool for remote dumping)

## References

- Official download and documentation: https://www.tarasco.org/security/pwdump_7/pwdump7.zip
- Author: Andres Tarasco Acuna (http://www.514.es)
- Related reading: MITRE ATT&CK T1003.002
