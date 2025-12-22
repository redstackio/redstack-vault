---
id: 16eb91f1-2b40-4ac0-a4b6-144b01cb5705
name: Impacket-GetNPUsers
type: tool
verified: true
created_at: '2020-03-21T00:28:50.481347+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
commands:
  - '[[commands/getnpusers-request-as-rep-no-preauth-users]]'
platforms:
  - Linux
  - Windows
tags:
  - active-directory
  - enumeration
  - kerberos
  - credential-access
url: 'https://github.com/SecureAuthCorp/impacket/blob/master/examples/GetNPUsers.py'
validated: true
---

# Impacket-GetNPUsers

**Status**: ✓ Verified

## Overview

Impacket-GetNPUsers is a Python script from the Impacket suite designed to identify and extract AS-REP (Authentication Service Request Reply) tickets for Active Directory users who have the "Do not require Kerberos preauthentication" flag (UF_DONT_REQUIRE_PREAUTH) enabled. This allows attackers to obtain crackable password hashes without needing valid credentials, facilitating offline password cracking with tools like Hashcat or John the Ripper. It is commonly used in red team engagements for credential access during lateral movement or privilege escalation in Windows/Active Directory environments.

## Description

The tool sends Kerberos AS-REQ messages to the domain controller for specified users. If the user account is configured not to require pre-authentication (a common misconfiguration for service accounts or legacy setups), the KDC responds with an AS-REP containing an encrypted ticket with the user's NTLM hash. This hash can then be cracked offline. The tool supports single users, user lists for brute-forcing, and output in formats compatible with popular cracking tools. It requires network access to the domain controller (typically port 88 UDP/TCP) and does not require domain authentication to run the requests.

## Features

- Enumerate users vulnerable to AS-REP roasting (pre-auth not required)
- Support for single user or batch requests from a file (enabling brute force against user lists)
- Output formats: Hashcat, John the Ripper, or raw
- Optional TGT request mode for further exploitation
- Debug mode for troubleshooting Kerberos interactions
- Auto-discovery of domain controller if not specified

## Installation

### Requirements

- Python 3.6+
- Impacket library (includes dependencies like pyasn1, pycryptodome)

### Install Commands

```bash
# Install Impacket via pip (includes GetNPUsers.py)
pip install impacket

# Or clone and install from source
git clone https://github.com/SecureAuthCorp/impacket.git
cd impacket
pip install .
```

On Kali Linux, Impacket is pre-installed or available via `apt install python3-impacket`.

## Basic Usage

```python
GetNPUsers.py -h
```

This displays help with all options.

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and exit |
| `-debug` | Turn DEBUG output ON |
| `-request` | Request TGT (instead of just AS-REP) |
| `-format FORMAT` | Output format (hashcat/jtr/raw, default: hashcat) |
| `-outputfile FILE` | Base output filename (stdout if not specified) |
| `-user USER` | User account to request ticket for (or file with list) |
| `-dc-ip IP` | IP Address of the domain controller |

## Examples

### Example 1: Basic Usage

Request AS-REP for a single user:

```python
GetNPUsers.py -user john.doe -format hashcat example.com
```

### Example 2: Brute Force with User List

Use a file containing usernames to check multiple accounts:

```python
GetNPUsers.py -user users.txt -dc-ip 192.168.1.10 -format hashcat -outputfile asreps.hash example.com
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[AS-REP Roasting]] Steal or Forge Kerberos Tickets: AS-REP Roasting

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic: Unusual Kerberos AS-REQ requests from non-domain joined systems to port 88
- Event logs: Kerberos authentication failures (Event ID 4768/4771) for users with pre-auth disabled
- Process monitoring: Python processes executing Impacket scripts (look for 'GetNPUsers.py' in command lines)
- Hash extraction attempts: Monitor for bulk AS-REP requests correlating with user enumeration

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
- [[tools/Hashcat]] (for cracking extracted hashes)
- [[tools/CrackMapExec]] (for broader AD enumeration)

## References

- Official Impacket GitHub: https://github.com/SecureAuthCorp/impacket
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1558/004/
- AS-REP Roasting Explanation: https://adsecurity.org/?p=1821
