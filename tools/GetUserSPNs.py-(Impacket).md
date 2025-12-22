---
id: 0bd559ef-80fe-4ab2-b8a0-6937f6c6ff95
name: GetUserSPNs.py (Impacket)
type: tool
verified: true
created_at: '2020-03-06T21:48:07.585987+00:00'
updated_at: '2023-05-30T19:53:26.451873+00:00'
commands:
  - '[[commands/getuserspns-query-spns-and-request-tgs]]'
platforms:
  - Linux
  - Windows
tags:
  - '[[Active Directory]]'
  - '[[Enumeration]]'
  - '[[kerberoast]]'
url: 'https://github.com/SecureAuthCorp/impacket'
validated: true
---

# GetUserSPNs.py (Impacket)

**Status**: ✓ Verified

## Overview

GetUserSPNs.py is a Python script from the Impacket suite designed for Active Directory enumeration and Kerberoasting attacks. It queries domain controllers to identify Service Principal Names (SPNs) associated with regular user accounts (rather than dedicated service accounts), which can indicate misconfigurations. It can also automatically request Kerberos Ticket Granting Service (TGS) tickets for these SPNs, producing password hashes encrypted with the service account's password. These hashes can be cracked offline using tools like Hashcat or John the Ripper to recover plaintext passwords, enabling further privilege escalation in Active Directory environments.

Common use cases include reconnaissance during red team engagements, identifying weak service account passwords, and supporting credential access in Kerberoasting workflows.

## Description

The tool leverages LDAP queries to enumerate SPNs from the domain, filtering for those tied to user objects. When the -request flag is used, it performs AS-REP roasting or TGS requests to obtain enc-type 23 (RC4) hashes, which are vulnerable to brute-force attacks due to often weak service account passwords. It requires valid domain credentials for authenticated queries and supports output to files for post-processing. GetUserSPNs.py is particularly effective against environments with poor SPN management, where users have SPNs assigned without strong password policies.

## Features

- **SPN Enumeration**: Queries Active Directory for all SPNs and their associated accounts, including user details like memberOf groups, password last set, and last logon.
- **TGS Ticket Requesting**: Automatically requests Kerberos TGS tickets for discovered SPNs, outputting crackable hashes in Hashcat/John format.
- **Authenticated Queries**: Supports domain credentials for deeper enumeration beyond anonymous access.
- **Output Formatting**: Generates structured output with SPN details and hashes, suitable for piping or file saving.
- **Flexible Targeting**: Specifies domain controllers via IP and handles common Kerberos encryption types.

## Installation

### Requirements

- Python 3.6+
- Impacket library (includes dependencies like ldap3, pyasn1)
- For cracking outputs: Hashcat or John the Ripper (optional, post-enumeration)

### Install Commands

```bash
# Install Impacket via pip (recommended for latest version)
pip3 install impacket

# Or clone from GitHub and install
 git clone https://github.com/SecureAuthCorp/impacket.git
 cd impacket
 pip3 install .

# On Kali Linux (pre-built package)
apt update && apt install impacket-scripts
```

For Windows, use Python's pip in a virtual environment or install via chocolatey if available.

## Basic Usage

```bash
tool-name --help
```

GetUserSPNs.py -h

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -dc-ip IP | Specify the domain controller IP address |
| -request | Request TGS tickets for SPNs (Kerberoasting mode) |
| -outputfile FILE | Save output to a specified file |
| -usersfile FILE | Input file with users to query (for targeted enumeration) |

## Examples

### Example 1: Basic Usage

Enumerate SPNs with TGS requests using domain credentials:

```bash
GetUserSPNs.py 'corp.local/user:pass' -dc-ip 10.10.10.10 -request
```

### Example 2: Advanced Usage

Targeted output to file for offline cracking:

```bash
GetUserSPNs.py 'corp.local/user:pass' -dc-ip 10.10.10.10 -request -outputfile kerb_hashes.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Kerberoasting]] Kerberoasting
- [[T1087.002]] Domain Account Discovery (via SPN enumeration)

### Tactics

- [[Credential Access]] Credential Access
- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- **Network Traffic**: LDAP queries (port 389/636) or Kerberos requests (port 88) from unusual sources; look for TGS-REQ spikes targeting service accounts.
- **Event Logs**: Windows Event ID 4769 (Kerberos Service Ticket Operations) with RC4 encryption and requests for user SPNs.
- **Process Monitoring**: Python processes executing Impacket scripts; monitor for GetUserSPNs.py in command lines.
- **Hash Extraction**: Presence of $krb5tgs$ formatted files on attacker systems or unusual file writes.
- **Defensive Tools**: Enable Kerberos logging, restrict SPN assignments to service accounts, and use strong password policies for service accounts.

## Related Procedures

- [[procedures/Kerberoast-Service-Accounts]]

## Related Tools

- [[tools/Impacket]]
- [[tools/Hashcat]]
- [[tools/john-the-ripper]]

## References

- Official GitHub: https://github.com/SecureAuthCorp/impacket
- Impacket Documentation: https://www.secureauth.com/labs/impacket/
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1558/003/
