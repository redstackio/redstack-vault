---
id: a2ff76ae-b98d-44c1-a806-d6721e120bad
type: tool
verified: true
created_at: '2019-08-28T21:17:24.449525Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - Windows
tags:
  - Enumeration
  - rpc
  - samba
  - smb
url: 'https://github.com/CiscoCXSecurity/enum4linux'
commands:
  - '[[commands/enum4linux-enumerate-smb-rpc-services]]'
validated: true
---

# enum4linux

**Status**: Unverified

## Overview

enum4linux is a Perl-based tool for enumerating information from Windows and Samba systems. It automates common enumeration tasks by wrapping tools like smbclient, rpcclient, and nmblookup, making it ideal for reconnaissance in offensive security operations targeting SMB/RPC services.

## Description

enum4linux collects detailed information about target hosts, including user accounts, group memberships, shares, domain SIDs, OS versions, and password policies. It is particularly useful for identifying weak configurations or potential entry points in Active Directory or Samba environments without requiring authentication in many cases.

## Features

- RID cycling for user enumeration
- Listing of users and group memberships
- Share enumeration and access testing
- Domain and workgroup detection
- OS identification
- Password policy retrieval
- NetBIOS name resolution

## Installation

### Requirements

- Perl (version 5 or later)
- smbclient, rpcclient, and nmblookup (from Samba suite)

### Install Commands

```bash
# On Debian/Ubuntu (includes dependencies)
apt update && apt install enum4linux

# Manual install from GitHub
apt install git perl libnet-smb-perl smbclient
cd /opt && git clone https://github.com/CiscoCXSecurity/enum4linux.git
cd enum4linux && chmod +x enum4linux.pl
```

For Windows, use Cygwin or WSL with the above dependencies.

## Basic Usage

```bash
enum4linux --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -a | Perform all enumeration (default comprehensive scan) |
| -U | Enumerate users only |
| -G | Enumerate groups only |
| -S | Enumerate shares only |
| -P | Enumerate password policy |
| -o | Enumerate OS information |
| -i | Interactive mode for credentialed scans |

## Examples

### Example 1: Basic Usage

```bash
enum4linux 192.168.1.100
```

Performs a standard enumeration without the -a flag, focusing on basic info.

### Example 2: Advanced Usage

```bash
enum4linux -a -u username -p password 192.168.1.100
```

Uses provided credentials for a more thorough, authenticated enumeration.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Account Discovery]] Account Discovery
- [[Permission Groups Discovery]] Permission Groups Discovery
- [[External Remote Services]] Network Share Discovery

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to port 445 (SMB) or 139 (NetBIOS) with enumeration patterns
- Process monitoring for enum4linux.pl or wrapped tools like smbclient
- Log analysis for failed authentication attempts or RID cycling queries
- IDS rules for unusual RPC calls from external IPs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/smbclient]]
- [[tools/rpcclient]]
- [[tools/CrackMapExec]]

## References

- Official GitHub: https://github.com/CiscoCXSecurity/enum4linux
- Samba Documentation: https://www.samba.org/
- MITRE ATT&CK: https://attack.mitre.org/
