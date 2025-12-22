---
type: tool
verified: true
created_at: '2020-02-06T00:37:43.504273+00:00'
updated_at: '2023-05-30T19:46:31.514897+00:00'
platforms:
  - Linux
tags:
  - cryptography
  - data-encryption
  - luks
url: 'https://cryptsetup-team.pages.debian.net/cryptsetup/'
commands:
  - '[[commands/dd-extract-luks-header]]'
validated: true
---

# cryptsetup

**Status**: ✓ Verified

## Overview

Cryptsetup is a command-line utility for managing encrypted block devices using the Linux device-mapper (dm-crypt) subsystem. It is primarily used for handling LUKS (Linux Unified Key Setup) encrypted volumes, enabling users to format, open, close, and manage encrypted partitions. In security testing and forensics, it is commonly used to interact with encrypted storage, extract headers for analysis, or mount volumes after cracking passphrases.

## Description

Cryptsetup provides a user-friendly interface to dm-crypt, supporting LUKS for full disk encryption. Key functionalities include creating encrypted containers, adding/removing key slots, dumping header information, and resizing volumes. It is essential for red team operations involving encrypted data exfiltration or post-exploitation persistence on Linux systems, as well as blue team forensics for analyzing encrypted artifacts. Cryptsetup does not perform cracking itself but facilitates extraction of material for tools like Hashcat.

## Features

- **LUKS Management**: Format devices with LUKS, open/close mappings, and manage multiple key slots.
- **Header Operations**: Dump or repair LUKS headers without mounting the volume.
- **Plain Mode**: Support for non-LUKS dm-crypt setups for simpler encryption.
- **Keyfile Support**: Use files or hardware tokens for authentication.
- **Batch Mode**: Non-interactive operations for scripting.

## Installation

### Requirements

- Linux kernel with dm-crypt support (standard on most distributions).
- libdevmapper and libcryptsetup libraries.

### Install Commands

#### Kali Linux
Pre-installed on Kali Linux.

#### Debian/Ubuntu
```bash
sudo apt update
sudo apt install cryptsetup
```

#### CentOS/RHEL/Fedora
```bash
sudo dnf install cryptsetup  # Fedora
# or
sudo yum install cryptsetup  # Older versions
```

## Basic Usage

```bash
cryptsetup --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-v, --verbose` | Verbose output for debugging |
| `-q, --quiet` | Suppress warnings |
| `--key-file` | Specify a keyfile for authentication |
| `--cipher` | Set the cipher algorithm (default: aes-xts-plain64) |

## Examples

### Example 1: Basic Usage - Format a LUKS Container

```bash
cryptsetup luksFormat /dev/sdb1
```

This prompts for a passphrase and formats the device as LUKS.

### Example 2: Advanced Usage - Open and Mount a LUKS Volume

```bash
cryptsetup luksOpen /dev/sdb1 encrypted_vol
mount /dev/mapper/encrypted_vol /mnt
```

This opens the volume and mounts it for access.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Credentials in Files]] Password Policy Discovery (for analyzing encryption setups)
- [[Execution Guardrails]] Execution Guardrails (bypassing encryption for persistence)

### Tactics

- [[Persistence]] Persistence
- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for `cryptsetup` executions in unusual contexts (e.g., non-admin mounting).
- Audit logs showing device-mapper mappings or LUKS operations.
- File system changes to `/dev/mapper/` or unusual mounts.

## Related Commands

- [[commands/dd-extract-luks-header]]

## References

- Official Documentation: https://cryptsetup-team.pages.debian.net/cryptsetup/
- Man Page: `man cryptsetup`
