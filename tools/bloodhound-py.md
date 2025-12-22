---
id: 22520ab7-7b7c-470d-ad9a-a1e80f8b0104
name: bloodhound-py
type: tool
verified: true
created_at: '2019-08-28T21:17:32.267021+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
commands:
  - '[[commands/bloodhound-py-enumerate-active-directory]]'
platforms:
  - Windows
  - Linux
tags:
  - active-directory
  - enumeration
url: 'https://github.com/BloodHoundAD/BloodHound.py'
validated: true
---

# bloodhound-py

**Status**: Unverified

## Overview

BloodHound.py is a Python-based data collector for Active Directory environments, built on the Impacket framework. It ingests domain information such as users, groups, computers, trusts, and sessions, producing JSON files that can be imported into the BloodHound GUI for graphing and analyzing attack paths in AD.

## Description

BloodHound.py enables security testers to map Active Directory structures remotely or locally. It supports authentication via username/password or Kerberos tickets and collects data over LDAP and SMB protocols. This tool is essential for identifying privilege escalation paths, such as excessive permissions or group memberships that lead to domain admin access. It can run on domain-joined systems without credentials or authenticate remotely to a domain controller.

## Features

- Feature 1: Comprehensive AD enumeration including users, groups, OUs, computers, trusts, and local admins
- Feature 2: Support for remote collection using Impacket for LDAP/SMB queries
- Feature 3: Output in BloodHound-compatible JSON format for visualization
- Feature 4: Configurable collection methods (e.g., All, GroupMembership, Trusts)
- Feature 5: Multi-threaded computer enumeration for efficiency

## Installation

### Requirements

- Python 3.7+ (updated from legacy Python 2 support)
- Impacket library
- LDAP and SMB access to the target domain

### Install Commands

```bash
# Clone the repository
git clone https://github.com/BloodHoundAD/BloodHound.py.git
cd BloodHound.py

# Install dependencies
pip3 install -r requirements.txt

# For Kali Linux (often pre-configured with Impacket)
apt update && apt install -y python3-impacket
```

On Windows, use Python from the Microsoft Store or Anaconda, and install via pip.

## Basic Usage

```bash
python bloodhound.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -c, --collectionmethod | Specify data to collect (e.g., All, Users, Groups) |
| -u, --username | Username for authentication |
| -p, --password | Password for authentication |
| -d, --domain | Target domain FQDN |
| -ns, --nameserver | Domain controller IP/hostname |
| -v, --verbose | Enable verbose logging |

## Examples

### Example 1: Basic Usage

Remote enumeration of full AD:

```bash
python bloodhound.py -c All -u bob -p s3cr3tpass -ns 10.10.10.10 -d megabank.local
```

### Example 2: Advanced Usage

Local collection on domain-joined host:

```bash
python bloodhound.py -c All -d megabank.local
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1087.002]] Domain Groups
- [[T1087.001]] Local Groups
- [[Domain Groups]] Permission Groups Discovery: Domain Groups

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor LDAP queries for unusual enumeration patterns (e.g., mass user/group fetches) using tools like Windows Event ID 4622 or Sysmon
- Detection method 2: Network traffic to domain controllers on ports 389 (LDAP), 445 (SMB) from non-domain tools
- Detection method 3: File creation of BloodHound JSON outputs on compromised hosts
- Detection method 4: Impacket library signatures in process memory or network payloads

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/BloodHound]]
- [[tools/Impacket]]

## References

- Official GitHub: https://github.com/BloodHoundAD/BloodHound.py
- BloodHound Documentation: https://bloodhound.readthedocs.io/en/latest/
- Impacket Framework: https://github.com/SecureAuthCorp/impacket
