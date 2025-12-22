---
id: 98851ca5-90dc-48b2-a989-54350a175f1f
name: p7zip
type: tool
verified: true
created_at: '2020-02-21T21:32:53.721580+00:00'
updated_at: '2023-05-30T19:48:16.852098+00:00'
commands:
  - '[[commands/7z-extract-password-protected-zip]]'
platforms:
  - Linux
tags:
  - '[[compression]]'
url: 'https://www.7-zip.org/'
validated: true
---

# p7zip

**Status**: ✓ Verified

## Overview

p7zip is a command-line port of 7-Zip for POSIX systems and Linux. It implements the popular 7-Zip compression algorithm, and if the full package is installed (p7zip-full), includes support for ZIP, ARJ, GZIP, BZIP2, TAR, CPIO, RPM, ISO, most filesystem images, and DEB format. p7zip is especially useful for decompressing ZIP archives which use a password and AES-256 encryption, as the standard "unzip" utility does not support these features.

## Description

p7zip provides high compression ratios and strong encryption support, making it a versatile tool for handling various archive formats in security testing environments. It is commonly used in penetration testing for extracting sensitive data from protected archives obtained during reconnaissance or post-exploitation phases.

## Features

- Feature 1: Support for 7z, ZIP, GZIP, BZIP2, TAR, and more archive formats
- Feature 2: AES-256 encryption for secure archiving and extraction
- Feature 3: High compression ratios with LZMA algorithm
- Feature 4: Command-line interface for scripting and automation

## Installation

### Requirements

- POSIX-compliant system (Linux recommended)
- Standard package manager (apt for Debian-based)

### Install Commands

```bash
# On Debian/Ubuntu/Kali
sudo apt update
sudo apt install p7zip-full
```

For basic functionality, `p7zip` suffices, but `p7zip-full` is recommended for broader format support.

## Basic Usage

```bash
7z --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v, --verbose` | Verbose output during operations |
| `x` | Extract files from archive |
| `a` | Add files to archive |
| `-p` | Set password for encryption/extraction |

## Examples

### Example 1: Basic Usage

```bash
7z l archive.7z
```

Lists contents of a 7z archive without extracting.

### Example 2: Advanced Usage

```bash
7z a -psecret encrypted.7z file1.txt file2.txt
```

Creates a password-protected 7z archive.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Archive Collected Data]] Archive Collected Data (for compressing exfiltrated data)
- [[Obfuscated Files or Information]] Obfuscated Files or Information (via encryption)

### Tactics

- [[Command and Control]] Command and Control
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Process monitoring for '7z' or '7za' executions
- Detection method 2: File system changes indicating archive extraction or creation
- Detection method 3: Network logs if archives are transferred (though tool itself is local)

## Related Procedures

No related procedures linked yet.

## Related Tools

- [[tools/zip]] (standard ZIP handling)
- [[tools/rar]] (for RAR archives)

## References

- Official website: https://www.7-zip.org/
- p7zip documentation: https://sourceforge.net/projects/p7zip/
