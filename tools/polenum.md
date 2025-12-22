---
id: e472fbd1-f6d4-4f1c-a67c-80d51740d00b
name: polenum
type: tool
verified: true
created_at: '2019-08-28T21:17:30.582490+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - discovery
  - enumeration
  - windows
  - password-policy
url: 'https://github.com/SecureAuthCorp/impacket/blob/master/examples/polenum.py'
validated: true
---

# polenum

**Status**: Unverified

## Overview

Polenum is a Python script designed for extracting password policy information from remote Windows machines. It leverages the Impacket library to perform RPC queries over SMB, allowing security testers on non-Windows systems (Linux, macOS, BSD) to enumerate policies without needing a Windows environment. Common use cases include reconnaissance in Active Directory environments to understand password requirements like minimum length, history, and lockout settings.

## Description

Polenum connects to a target Windows system (domain controller or standalone server) using either null sessions or provided credentials. It queries the LSA (Local Security Authority) policy via NetrGetUserInfoLevel RPC calls to retrieve details on password constraints. This tool is particularly useful in red team engagements for passive discovery of security configurations that influence brute-force or cracking strategies. It supports both domain and local policies but requires network access to port 445 (SMB).

## Features

- Null session support for anonymous enumeration (if permitted)
- Credential-based authentication for restricted targets
- Extraction of key policy elements: min/max password age, length, history, lockout threshold/duration/observation window
- Cross-platform execution (Python-based, runs on Linux/macOS)
- Integration with Impacket for reliable SMB/RPC handling

## Installation

### Requirements

- Python 3.x
- Impacket library (provides SMB/RPC primitives)

### Install Commands

```bash
# Install Impacket via pip (includes polenum.py in examples/)
pip install impacket

# Or clone the repository
apt update && apt install git python3-pip  # On Debian/Ubuntu
pip install impacket

# For Kali Linux (pre-installed Impacket)
# No action needed, polenum.py is in /usr/share/doc/python3-impacket/examples/
```

After installation, locate polenum.py in the Impacket examples directory and ensure it's executable.

## Basic Usage

```python
python polenum.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -U, --user | Username for authentication (empty for null session) |
| -P, --password | Password (empty for null session) |
| -d, --domain | Domain name (optional) |
| -H, --hashes | NTLM hash instead of password |

## Examples

### Example 1: Null Session Enumeration

```python
python polenum.py -U '' -P '' 192.168.1.100
```

This attempts anonymous access to extract policy from the target.

### Example 2: Authenticated Enumeration

```python
python polenum.py -U administrator -P Passw0rd -d EXAMPLE 192.168.1.10
```

Uses credentials to query a domain controller.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Password Policy Discovery]] Password Policy Discovery

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual SMB/RPC connections (port 445) from non-Windows sources
- Queries to LSA policy endpoints (NetrGetUserInfoLevel)
- Event logs: Security event ID 4624 (logon attempts, even null sessions) or 4776 (credential validation)
- Network monitoring for Impacket signatures in traffic

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Impacket]]
- [[tools/enum4linux]]

## References

- Official Impacket GitHub: https://github.com/SecureAuthCorp/impacket
- Polenum script: https://github.com/SecureAuthCorp/impacket/blob/master/examples/polenum.py
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1201/
