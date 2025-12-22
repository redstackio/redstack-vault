---
id: 40eb3230-928e-4971-b67f-a701bf1547f9
name: secretsdump.py
type: tool
verified: true
created_at: '2020-03-16T03:14:52.907252+00:00'
updated_at: '2023-05-30T01:08:57.806518+00:00'
platforms:
  - Windows
tags:
  - dump
  - network
  - ntlm
url: 'https://github.com/SecureAuthCorp/impacket/blob/master/examples/secretsdump.py'
commands:
  - '[[commands/secretsdump-smb-sam-dump]]'
  - '[[commands/secretsdump-dcom-lsa-secrets-dump]]'
  - '[[commands/secretsdump-ntds-dit-extract]]'
validated: true
---

# secretsdump.py

**Status**: ✓ Verified

## Overview

secretsdump.py is a Python script from the Impacket suite designed to extract password hashes, SAM database entries, LSA secrets, and NTDS.dit files from remote Windows systems. It operates without executing any agent code on the target machine, leveraging protocols like SMB and DCOM for remote access. Commonly used in penetration testing for credential dumping during post-exploitation phases.

## Description

The tool performs remote credential extraction by authenticating to the target using provided credentials and then reading registry hives (SAM and SYSTEM) or NTDS.dit. For SAM and LSA secrets (including cached domain credentials), it first attempts to read directly from the registry. If needed, it saves the hives temporarily on the target (%SYSTEMROOT%\Temp) to extract additional data. It supports output in formats compatible with tools like Hashcat or John the Ripper for offline cracking. Use cases include dumping local accounts, service account hashes, and Kerberos keys in Active Directory environments.

## Features

- Remote SAM hash extraction via SMB or DCOM
- LSA secrets dumping (cached creds, DPAPI keys)
- NTDS.dit extraction for full domain credential harvesting
- No target-side execution required
- Support for NTLM and Kerberos authentication
- Output in crackable formats (NTLM, Kerberos TGS-REP)

## Installation

### Requirements

- Python 3.x
- Impacket library (version 0.9.24 or later)

### Install Commands

On Kali Linux (pre-installed in many distributions):

```bash
# Update and install if missing
sudo apt update && sudo apt install impacket-scripts
```

On Ubuntu/Debian:

```bash
pip3 install impacket
```

On Windows (with Python):

```bash
pip install impacket
```

Manual clone:

```bash
git clone https://github.com/SecureAuthCorp/impacket.git
cd impacket
pip install .
```

## Basic Usage

```bash
secretsdump.py --help
```

View full options and protocols supported.

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and exit |
| `-sam` | Dump SAM hashes only |
| `-system` | Dump SYSTEM registry hive |
| `-lsa` | Dump LSA secrets |
| `-ntds` | Extract NTDS.dit (requires SYSTEM and NTDS access) |
| `-just-dc` | Target only the Domain Controller |
| `-outputfile` | Specify output file for dumps |
| `-no-pass` | Don't prompt for password (use hash instead) |

## Examples

### Example 1: Basic SAM Dump via SMB

```bash
secretsdump.py DOMAIN/Administrator:Password123@192.168.1.10 -sam
```

Dumps local SAM hashes from the target.

### Example 2: Full Credential Dump with LSA and NTDS

```bash
secretsdump.py -just-dc DOMAIN/Administrator:Password123@dc01.domain.local -system -lsa -ntds
```

Extracts SYSTEM, LSA secrets, and NTDS.dit from a domain controller.
