---
id: 64be751a-9916-412c-8d0d-6d3f28b5a21a
name: Invoke-ACLpwn
type: tool
verified: true
created_at: '2019-08-28T21:17:26.853710+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - acl-abuse
  - privilege-escalation
  - post-exploitation
url: 'https://github.com/CyberArkLabs/ACL_Pwn'
validated: true
---

# Invoke-ACLpwn

**Status**: Unverified

## Overview

Invoke-ACLpwn is a PowerShell tool designed to automate the discovery and exploitation of misconfigured Access Control Lists (ACLs) in Active Directory environments. It helps identify unsafe ACL permissions that can be abused for privilege escalation, such as granting users excessive rights on sensitive objects like groups or OUs.

## Description

The tool scans Active Directory for ACLs where non-privileged users or groups have rights like GenericAll, WriteOwner, or ForceChangePassword, which can lead to domain compromise. Once identified, it can automatically exploit these misconfigurations to elevate privileges, making it a valuable asset for red teaming and penetration testing in Windows/AD environments. It integrates well with other AD attack tools like PowerView.

## Features

- Feature 1: Comprehensive ACL scanning across domain objects (users, groups, OUs, GPOs).
- Feature 2: GUID resolution for readable output of rights and SIDs.
- Feature 3: Automated exploitation of identified vulnerabilities (e.g., adding users to privileged groups).
- Feature 4: Support for remote domain controllers and alternate credentials.
- Feature 5: Output in structured format for further analysis or reporting.

## Installation

### Requirements

- PowerShell 2.0 or later (Windows Server 2008+ or Windows 7+).
- Active Directory module or RSAT tools for AD querying.
- Domain-joined machine or credentials with read access to AD.

### Install Commands

```powershell
# Download from GitHub
Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/CyberArkLabs/ACL_Pwn/master/Invoke-ACLpwn.ps1' -OutFile 'Invoke-ACLpwn.ps1'

# Load the script
. .\Invoke-ACLpwn.ps1
```

For full setup, clone the repository:

```powershell
git clone https://github.com/CyberArkLabs/ACL_Pwn.git
cd ACL_Pwn
. .\Invoke-ACLpwn.ps1
```

## Basic Usage

```powershell
Invoke-ACLpwn -ResolveGUIDs
```

### Common Options

| Option | Description |
|--------|-------------|
| `-ResolveGUIDs` | Resolve GUIDs to names for clearer output |
| `-DomainController` | Target a specific DC |
| `-Username`, `-Password` | Use alternate credentials |
| `-Object` | Specify a single object to check |
| `-Right` | Filter by specific right (e.g., GenericAll) |

## Examples

### Example 1: Basic Usage

Scan the domain for vulnerable ACLs:

```powershell
Invoke-ACLpwn -ResolveGUIDs
```

### Example 2: Advanced Usage

Exploit a specific ACL on the Domain Admins group:

```powershell
Invoke-ACLpwn -Object (Get-DomainObject -Identity 'Domain Admins') -Right GenericAll
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[T1087.002]] Domain Account Discovery
- [[Credentials in Files]] Modify Authentication Process: Password Policy Discovery

### Tactics

- [[Privilege Escalation]] Privilege Escalation
- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor PowerShell execution logs for 'Invoke-ACLpwn' script loads or command invocations.
- Detection method 2: Audit AD object modifications (e.g., unexpected group memberships) via Event ID 4728/4732.
- Detection method 3: Network logs showing LDAP queries from unusual hosts or accounts.
- Detection method 4: Enable Advanced Audit Policy for Directory Service Changes.

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
- [[tools/Impacket]]

## References

- Official GitHub: https://github.com/CyberArkLabs/ACL_Pwn
- Blog post: https://www.cyberark.com/resources/threat-research-blog/abusing-acls-in-active-directory
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1068/
