---
type: tool
description: >-
  RidEnum is a Python-based tool for performing RID cycling attacks to enumerate
  user accounts on Windows domains using null sessions and SID resolution, with
  optional brute force capabilities.
url: 'https://github.com/byt3bl33d3r/RidEnum'
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - enumeration
  - discovery
  - rid-cycling
  - brute-force
validated: true
---

# ridenum

**Status**: Unverified

## Overview

RidEnum is a specialized tool for Active Directory enumeration, focusing on RID (Relative Identifier) cycling to discover user accounts without valid credentials. It leverages null sessions to query the Security Account Manager (SAM) database via SID enumeration, making it useful for initial reconnaissance in red team engagements targeting Windows environments. Common use cases include identifying privileged accounts like Administrators during domain discovery.

## Description

RidEnum performs a RID cycling attack by iterating through possible RIDs (typically 500-1000+ for users) and resolving SIDs to usernames over null sessions. This exploits legacy Windows behavior allowing anonymous enumeration. If a password file is provided, it automatically transitions to brute forcing the enumerated accounts, testing common passwords or wordlists. The tool is lightweight, Python-based, and requires no installation beyond Python dependencies, making it suitable for quick deployment in penetration testing.

## Features

- Null session-based SID to username resolution
- Automated RID cycling for efficient enumeration
- Integrated brute force module for credential validation
- Output formatting for easy parsing (e.g., CSV or plain text)
- Support for domain controllers and member servers

## Installation

### Requirements

- Python 2.7 or 3.x
- Impacket library (for SMB/SID queries)

### Install Commands

```bash
# Clone the repository
git clone https://github.com/byt3bl33d3r/RidEnum.git
cd RidEnum

# Install dependencies (if not using a virtualenv)
pip install impacket

# For Kali Linux (often pre-configured with Impacket)
# No additional steps needed if Impacket is installed
```

On Ubuntu/Debian:

```bash
sudo apt update
sudo apt install python3-pip git
pip3 install impacket
```

## Basic Usage

```python
python RidEnum.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| --passlist | Path to password list for brute forcing |
| -o, --output | Output file for results |
| -d, --domain | Target domain name (if not inferred) |

## Examples

### Example 1: Basic Usage

Perform enumeration on a target IP:

```python
python RidEnum.py 192.168.1.100
```

### Example 2: Advanced Usage

Enumerate and brute force with a password list:

```python
python RidEnum.py 192.168.1.100 --passlist /path/to/passwords.txt -o enum_results.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1087.001]] Account Discovery: Local Account
- [[T1087.002]] Account Discovery: Domain Account

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic: SMB null sessions (IPC$ share) from unusual sources to port 445
- Event logs: Windows Security Event ID 4625 (failed logons) during brute force
- Process monitoring: Python processes with impacket modules loading
- Anomaly detection: High volume of LSA LookupNames queries

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Impacket-Suite]]
- [[tools/CrackMapExec]]

## References

- Official GitHub: https://github.com/byt3bl33d3r/RidEnum
- Impacket Documentation: https://github.com/SecureAuthCorp/impacket
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1087/
