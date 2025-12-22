---
id: f5d6aa79-9966-48d1-92f0-4ad8b2d5d602
type: tool
verified: true
created_at: '2019-08-28T21:17:20.530782+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - acl-enumeration
  - discovery
  - privilege-escalation
url: 'https://github.com/byt3bl33d3r/ADACLScanner'
validated: true
---

# ADACLScanner

**Status**: Unverified

## Overview

ADACLScanner is a PowerShell script designed to enumerate and analyze Access Control Lists (ACLs) in Active Directory environments. It helps identify misconfigured permissions, such as excessive rights granted to users or groups, which could enable privilege escalation or unauthorized access. Commonly used in red team engagements for Active Directory discovery and abuse potential assessment. Category: Discovery.

## Description

The tool scans AD objects for dangerous ACLs, including those allowing generic all rights, write DAC, or ownership changes. It supports resolving GUIDs to readable names and can target specific domains, OUs, or objects. Output is structured for easy parsing, highlighting risky configurations like 'Everyone' group having admin-like permissions. It's particularly useful in Windows domain environments to map out permission weaknesses without requiring domain admin rights—domain user credentials often suffice.

## Features

- Feature 1: Full domain ACL enumeration with Get-DomainACL
- Feature 2: Targeted OU or object scanning with Get-DomainObjectAcl
- Feature 3: GUID resolution for human-readable output
- Feature 4: Filtering for high-risk permissions (e.g., GenericAll, WriteOwner)
- Feature 5: Export capabilities to CSV for reporting

## Installation

### Requirements

- PowerShell 3.0 or later
- Active Directory module (RSAT-AD-PowerShell) or PowerView for underlying functions
- Domain-joined Windows machine or credentials with AD query access

### Install Commands

```powershell
# Download from GitHub
Invoke-WebRequest -Uri https://github.com/byt3bl33d3r/ADACLScanner/archive/master.zip -OutFile ADACLScanner.zip
Expand-Archive -Path ADACLScanner.zip -DestinationPath .\

# Or clone if Git is available
git clone https://github.com/byt3bl33d3r/ADACLScanner.git
```

Import the module before use:

```powershell
Import-Module .\ADACLScanner\ADACLScanner.ps1
```

## Basic Usage

```powershell
tool-name --help
```

Run a basic domain scan:

```powershell
Import-Module .\ADACLScanner.ps1; Get-DomainACL -DomainController dc01.example.com
```

### Common Options

| Option | Description |
|--------|-------------|
| -DomainController | Specifies the DC to query |
| -ResolveGUIDs | Translates GUIDs to names |
| -SearchBase | Limits scan to a specific OU or container |
| -FilterScript | Custom PowerShell filter for results |

## Examples

### Example 1: Basic Usage

```powershell
Import-Module .\ADACLScanner.ps1; Get-DomainACL -DomainController dc01.example.com -ResolveGUIDs
```

This performs a full domain scan and displays ACLs in a table format.

### Example 2: Advanced Usage

```powershell
Import-Module .\ADACLScanner.ps1; Get-DomainObjectAcl -SearchBase "OU=Domain Controllers,DC=example,DC=com" -ResolveGUIDs | Where-Object {$_.ActiveDirectoryRights -match "GenericAll"}
```

Scans a specific OU for GenericAll permissions and filters results.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1087.002]] Domain Groups
- [[Domain Groups]] Permission Groups Discovery: Domain Groups
- [[Account Discovery]] Account Discovery

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: PowerShell execution logs showing Import-Module ADACLScanner or Get-DomainACL invocations (enable Script Block Logging)
- Detection method 2: LDAP queries from non-admin accounts enumerating ACLs (monitor with Windows Event ID 4662)
- Detection method 3: Unusual CSV exports or file writes containing AD object data

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/PowerView]]
- [[tools/BloodHound]]
- [[tools/ADRecon]]

## References

- Official GitHub: https://github.com/byt3bl33d3r/ADACLScanner
- Blog post by author: https://byt3bl33d3r.github.io/privesc/active-directory/adaclscanner.html
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1087/
