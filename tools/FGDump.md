---
id: 869c3136-1e3f-43e0-93eb-861bc956b7d1
name: FGDump
type: tool
verified: true
created_at: '2020-02-27T03:30:40.293357+00:00'
updated_at: '2023-05-30T19:54:18.751630+00:00'
commands:
  - '[[commands/fgdump-local-ntlm-lm-dump]]'
platforms:
  - Windows
tags:
  - '[[administrator]]'
  - '[[Cryptography]]'
  - '[[NTLM]]'
url: 'http://www.foofus.net/fizzgig/fgdump/fgdump-2.1.0-exeonly.zip'
validated: true
---

# FGDump

**Status**: ✓ Verified

## Overview

FGDump is a Windows utility designed for dumping password hashes, including NTLM and LM hashes, from local or remote Windows systems. It is particularly useful in penetration testing scenarios where an attacker has gained initial access to a Windows NT/2000/XP/2003 machine and needs to extract credentials for further lateral movement or privilege escalation.

## Description

FGDump extracts SAM (Security Account Manager) hashes and cached credentials from the target system. It supports both local execution (when run on the target) and remote dumping over SMB with provided credentials. The tool outputs results in pwdump format, which can be cracked offline using tools like Hashcat or John the Ripper. Note that FGDump is an older tool targeted at legacy Windows versions and may not work on modern systems without modifications.

## Features

- Local hash dumping without parameters
- Remote dumping using SMB with username/password or pass-the-hash
- Extraction of both LM and NTLM hashes
- Support for cached domain credentials
- Output in standard pwdump format for compatibility with cracking tools

## Installation

### Requirements

- Windows NT/2000/XP/2003 (target system)
- Administrative privileges on the target for full access
- No additional dependencies; it's a standalone executable

### Install Commands

FGDump is distributed as a pre-compiled binary. Download and extract it to a directory on the target or attacker machine:

1. Download the archive from the official source.
2. Extract `fgdump.exe` to your working directory (e.g., `C:\temp\`).

No compilation required.

## Basic Usage

```cmd
fgdump.exe -?
```

This displays the help menu with all options, including local and remote dump parameters.

### Common Options

| Option | Description |
|--------|-------------|
| `-h <host>` | Target hostname or IP for remote dump |
| `-u <user>` | Username for remote authentication |
| `-p <pass>` | Password for remote authentication |
| `-k` | Use Kerberos authentication (if available) |
| `-?` | Show help |

## Examples

### Example 1: Basic Usage

Local dump on the current machine:

```cmd
fgdump.exe
```

This performs a local credential dump and saves output to files like `127.0.0.1.pwdump`.

### Example 2: Advanced Usage

Remote dump using credentials:

```cmd
fgdump.exe -h 192.168.1.100 -u administrator -p Summer18!
```

This connects to the remote host and extracts hashes if authentication succeeds.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Credential Dumping]] OS Credential Dumping
- [[Security Account Manager]] Security Account Manager

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of `fgdump.exe` in process lists or temporary directories
- Unusual SMB connections from internal hosts
- File creation of `.pwdump` files in user directories
- Event logs showing SAM access (Event ID 4656/4663 on modern Windows)
- Network traffic to port 445 (SMB) with authentication attempts

## Related Procedures

- [[Dump-Windows-Credentials-Locally]]
- [[Extract-Hashes-for-Pass-the-Hash]]

## Related Tools

- [[tools/Mimikatz]]
- [[Secretsdump]]

## References

- Official download: http://www.foofus.net/fizzgig/fgdump/
- Foofus.net archives (tool is no longer actively maintained)
