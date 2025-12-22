---
id: cd12283c-7e6d-46d8-824f-462ca33d3ad0
type: tool
verified: true
created_at: '2019-08-28T21:17:29.556030+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - reconnaissance
  - ad-enumeration
url: 'https://github.com/sense-of-security/ADRecon'
validated: true
---

# ADRecon

**Status**: Unverified

## Overview

ADRecon is a PowerShell-based tool designed for reconnaissance in Active Directory (AD) environments. It collects comprehensive information about AD objects such as users, groups, computers, policies, and more, then generates a structured Microsoft Excel report with summary dashboards and metrics to aid in analysis during security assessments or audits.

## Description

ADRecon automates the extraction of key AD artifacts, making it easier to identify misconfigurations, weak permissions, or potential attack paths in domain environments. It's particularly useful in red team engagements for mapping the AD structure without manual querying. The tool supports modular collection, allowing users to target specific data types, and outputs everything into an Excel file with pivot tables and charts for quick visualization.

## Features

- **Modular Data Collection**: Gather info on users, groups, OUs, GPOs, trusts, and ACLs selectively or comprehensively.
- **Excel Reporting**: Generates a single .xlsx file with multiple sheets, summaries, and metrics (e.g., number of admin users, stale accounts).
- **Stealth Options**: Supports use of alternate credentials and domain controllers to minimize footprint.
- **Cross-Forest Support**: Can query remote domains if credentials are provided.
- **Customizable Scope**: Limit collection to specific OUs or object types to reduce noise.

## Installation

### Requirements

- PowerShell 3.0 or later (Windows Server 2008+ or Windows 7+).
- Active Directory PowerShell module (RSAT-AD-PowerShell feature).
- Microsoft Excel or LibreOffice for viewing reports (not required for generation).
- Domain user credentials with read access to AD objects.

### Install Commands

```powershell
# Download the ADRecon module from GitHub
Invoke-WebRequest -Uri "https://github.com/sense-of-security/ADRecon/archive/master.zip" -OutFile "ADRecon.zip"

# Extract the zip file
Expand-Archive -Path "ADRecon.zip" -DestinationPath "C:\Tools"

# Import the module (run from the extracted directory)
Import-Module .\ADRecon.ps1
```

Alternatively, clone the repository:

```powershell
# Using Git
git clone https://github.com/sense-of-security/ADRecon.git
cd ADRecon
Import-Module .\ADRecon.ps1
```

## Basic Usage

```powershell
Get-Help Invoke-ADRecon
```

### Common Options

| Option | Description |
|--------|-------------|
| `-DomainController` | Specifies the target domain controller (default: local DC). |
| `-ReportPath` | Output path for the Excel report (default: current directory). |
| `-Credential` | PSCredential object for alternate authentication. |
| `-Module` | Comma-separated list of modules to run (e.g., Users,Groups,Computers). |
| `-OU` | Restrict collection to a specific Organizational Unit. |
| `-Verbose` | Enable detailed logging. |

## Examples

### Example 1: Basic Usage

Run a full AD collection on the local domain and save to a report:

```powershell
Invoke-ADRecon -DomainController "dc01.domain.local" -ReportPath "C:\Reports\ADRecon_Report.xlsx"
```

### Example 2: Advanced Usage

Collect only user and group information using alternate credentials:

```powershell
$cred = Get-Credential
Invoke-ADRecon -Module "Users,Groups" -Credential $cred -ReportPath "C:\Reports\ADRecon_UsersGroups.xlsx" -Verbose
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1087.002]] Domain Trust Discovery
- [[T1087.001]] Account Discovery: Local Account
- [[Domain Groups]] Permission Groups Discovery: Domain Groups

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- PowerShell execution logs showing Import-Module ADRecon or Invoke-ADRecon.
- Network queries to domain controllers via LDAP (port 389/636) from unusual hosts.
- File creation of large Excel files with AD-related sheet names in temp or report directories.
- Event ID 4624 (logons) with PowerShell as the process, especially with domain read permissions.

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
- [[tools/SharpHound]]

## References

- Official GitHub: https://github.com/sense-of-security/ADRecon
- ADRecon Documentation: Included in the repository README
- MITRE ATT&CK: https://attack.mitre.org
