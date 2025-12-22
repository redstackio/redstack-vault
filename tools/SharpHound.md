---
id: 48e4a8ea-7aad-4a4a-a288-2e196a50e181
name: SharpHound
type: tool
verified: true
created_at: '2019-08-28T21:17:32.038105+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Windows
tags:
  - Active Directory
  - Enumeration
url: 'https://github.com/BloodHoundAD/BloodHound/tree/master/Ingestors'
validated: true
---

# SharpHound

**Status**: Unverified

## Overview

SharpHound is a C#-based data collector for BloodHound, designed to enumerate Active Directory environments. It gathers detailed information about users, groups, computers, trusts, and permissions, producing JSON files that can be imported into BloodHound for visualization of attack paths in AD.

## Description

Built on .NET 4.5, SharpHound runs with domain user privileges to query LDAP and other AD protocols. It supports various collection methods like user rights, group memberships, local admins, and session data. Output files include domain-specific JSONs (e.g., <DOMAIN>-users.json) that BloodHound processes to build graphs revealing privilege escalation paths, such as Kerberoasting or DCSync opportunities. Use it during red team engagements for AD reconnaissance without requiring high privileges.

## Features

- Feature 1: Comprehensive AD enumeration including ACLs, trusts, and sessions
- Feature 2: Stealthy collection options to minimize noise (e.g., loopback only)
- Feature 3: Support for remote execution via SMB or LDAP credentials
- Feature 4: Output in BloodHound-compatible JSON format

## Installation

### Requirements

- .NET Framework 4.5 or later
- Domain user credentials for authentication
- Access to target domain controllers via LDAP/SMB

### Install Commands

For pre-built binaries:

```powershell
# Download from GitHub releases
Invoke-WebRequest -Uri "https://github.com/BloodHoundAD/SharpHound/releases/latest/download/SharpHound.exe" -OutFile "SharpHound.exe"
```

For building from source on Windows:

1. Install Visual Studio Community with ".NET desktop development", "ASP.NET and web development", and ".NET Core cross-platform development" workloads.
2. Clone the repository:
   ```powershell
   git clone https://github.com/BloodHoundAD/SharpHound.git
   cd SharpHound
   ```
3. Open SharpHound.sln in Visual Studio.
4. Set configuration to "Release".
5. Build > Rebuild Solution.
6. Find SharpHound.exe in SharpHound/bin/Release/.

## Basic Usage

```powershell
SharpHound.exe --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-c, --CollectionMethod` | Specify collection methods (e.g., All, Group, ACL) |
| `-d, --Domain` | Target domain name |
| `--LDAPUsername` | LDAP username for authentication |
| `--LDAPPassword` | LDAP password |
| `--Loopback` | Collect only from local machine |
| `-dc, --DomainController` | Specify DC IP or hostname |

## Examples

### Example 1: Basic Usage

Run all collections on the current domain with provided credentials:

```powershell
SharpHound.exe -c All -d contoso.com --LDAPUsername user --LDAPPassword pass
```

### Example 2: Advanced Usage

Collect data remotely from a specific DC with stealth options:

```powershell
SharpHound.exe -c All -d contoso.com -dc 192.168.1.10 --LDAPUsername user --LDAPPassword pass --Loopback
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1087.002]] Domain Trust Discovery
- [[Domain Groups]] Permission Groups Discovery: Domain Groups
- [[T1087.001]] Account Discovery: Local Account

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for unusual LDAP queries from non-DC systems (e.g., high volume of dsGetDCName or samr queries)
- Detection method 2: File creation of JSON files with domain-specific names in temp directories
- Detection method 3: Process execution of SharpHound.exe or suspicious .NET binaries querying AD
- Detection method 4: Network traffic to port 389/636 (LDAP) from internal hosts without admin tools

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
- [[tools/PowerView]]

## References

- Official GitHub: https://github.com/BloodHoundAD/SharpHound
- BloodHound Documentation: https://bloodhound.readthedocs.io/en/latest/
