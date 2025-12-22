---
id: f584a53d-3aec-4474-b3e9-618d6e799169
name: PowerView
type: tool
verified: true
created_at: '2019-08-28T21:17:40.304206+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
commands:
  - '[[commands/powerview-add-domain-group-member]]'
platforms:
  - Windows
tags:
  - powerview
  - active-directory
  - reconnaissance
  - post-exploitation
url: 'https://github.com/PowerShellMafia/PowerSploit'
validated: true
---

# PowerView

**Status**: Unverified

## Overview

PowerView is a PowerShell-based tool designed for gaining network situational awareness on Windows domains. It provides pure PowerShell replacements for traditional Windows 'net *' commands, leveraging PowerShell Active Directory hooks and Win32 API functions to perform domain-related tasks such as enumeration, querying, and modification of Active Directory objects.

## Description

PowerView enables security professionals and red teams to perform comprehensive domain reconnaissance and manipulation without relying on native Windows tools that may be monitored or restricted. Common use cases include enumerating users, groups, computers, and permissions; querying domain trusts; and performing actions like adding users to groups for privilege escalation. It is particularly valuable in Active Directory environments for identifying attack paths and lateral movement opportunities.

## Features

- Feature 1: Domain object enumeration (users, groups, OUs, GPOs) using LDAP queries.
- Feature 2: Permission and ACL analysis to identify misconfigurations.
- Feature 3: Group membership management and session enumeration across the domain.
- Feature 4: Integration with Win32 APIs for low-level AD interactions.

## Installation

### Requirements

- PowerShell 2.0 or later (Windows environments).
- .NET Framework 3.5 or higher.
- Administrative privileges may be required for some functions.

### Install Commands

PowerView is part of the PowerSploit suite. Clone the repository from GitHub:

```powershell
# On Windows (using PowerShell)
Invoke-WebRequest -Uri https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/dev/Recon/PowerView.ps1 -OutFile PowerView.ps1
# Then import: . ./PowerView.ps1
```

For full PowerSploit:

```powershell
git clone https://github.com/PowerShellMafia/PowerSploit.git
cd PowerSploit/Recon
. ./PowerView.ps1
```

On Kali Linux (for cross-platform testing):

```bash
# Use wine or PowerShell Core
sudo apt install powershell
# Then download and import as above
```

## Basic Usage

```powershell
# Import the module
. ./PowerView.ps1

# Get help
Get-Help Get-DomainUser
```

### Common Options

| Option | Description |
|--------|-------------|
| -Credential | Specify alternate credentials for operations |
| -Domain | Target a specific domain |
| -SearchBase | Limit queries to a specific OU or container |
| -Verbose | Enable detailed output |

## Examples

### Example 1: Basic Usage

```powershell
Get-DomainUser
```

This enumerates all domain users.

### Example 2: Advanced Usage

```powershell
Get-DomainGroupMember -Identity 'Domain Admins' -Credential $Cred
```

This lists members of the Domain Admins group using provided credentials.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Account Discovery]] Account Discovery
- [[Permission Groups Discovery]] Permission Groups Discovery
- [[System Information Discovery]] System Information Discovery
- [[Domain Accounts]] Domain Accounts

### Tactics

- [[Discovery]] Discovery
- [[Lateral Movement]] Lateral Movement
- [[Privilege Escalation]] Privilege Escalation

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor PowerShell script block logging for imports of PowerView.ps1 or calls to functions like Get-DomainUser.
- Detection method 2: LDAP query anomalies (high volume of directory searches from unusual hosts).
- Detection method 3: Event ID 4624/4672 for suspicious logons tied to enumeration activities.
- Detection method 4: Network traffic to domain controllers showing unusual AD queries.

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
- [[tools/SharpHound]]

## References

- Official GitHub: https://github.com/PowerShellMafia/PowerSploit
- PowerView Documentation: https://powershellmafia.com/granddaddy-of-all-powershell-tools-powerview/
- Related resources: MITRE ATT&CK for Active Directory techniques.
