---
id: d70618c4-1eca-43cf-9a29-21a50fd74ad2
name: LAPSToolkit
type: tool
verified: true
created_at: '2019-08-28T21:17:43.250702+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - laps
  - active-directory
  - auditing
  - post-exploitation
url: 'https://github.com/microsoft/LAPS (or equivalent toolkit repo)'
validated: true
---

# LAPSToolkit

**Status**: Unverified

## Overview

LAPSToolkit is a PowerShell-based toolkit designed to audit, manage, and test Local Administrator Password Solution (LAPS) configurations in Active Directory environments. It helps security professionals assess LAPS deployment effectiveness, identify weak policies, and simulate attacks on local admin password management. Commonly used in red teaming for privilege escalation via LAPS misconfigurations.

## Description

The toolkit provides cmdlets for querying LAPS policies, extracting passwords, checking permissions, and reporting on compliance. LAPS itself randomizes and stores local admin passwords securely in AD, but LAPSToolkit exposes potential vulnerabilities like over-permissive access controls or outdated policies. It supports both auditing (blue team) and exploitation (red team) workflows without requiring native LAPS installation on the attacking machine.

## Features

- Feature 1: Policy auditing to verify password complexity, rotation intervals, and scope.
- Feature 2: Password extraction for authorized computers, supporting plain-text output for testing.
- Feature 3: Permission analysis on LAPS extended rights (e.g., ms-Mcs-AdmPwd attribute access).
- Feature 4: Reporting and export capabilities for compliance checks.
- Feature 5: Integration with Active Directory modules for domain-wide scans.

## Installation

### Requirements

- PowerShell 5.1 or later
- Active Directory PowerShell module (RSAT-AD-PowerShell)
- Domain-joined machine with read access to AD

### Install Commands

```powershell
# Install from PowerShell Gallery (if available as module)
Install-Module -Name LAPSToolkit -Force

# Or clone from GitHub
Invoke-WebRequest -Uri "https://github.com/example/LAPSToolkit/archive/main.zip" -OutFile laps.zip
Expand-Archive -Path laps.zip -DestinationPath C:\Tools
Import-Module C:\Tools\LAPSToolkit-main\LAPSToolkit.psm1
```

For Windows Server/Kali with PowerShell Core: Ensure RSAT tools are installed via `Add-WindowsCapability`.

## Basic Usage

```powershell
Get-Command -Module LAPSToolkit
```

### Common Options

| Option | Description |
|--------|-------------|
| -Domain | Specify target AD domain |
| -AsPlainText | Output passwords in clear text (high risk) |
| -Identity | Target user/group/computer for queries |
| -Export | Save results to CSV/JSON |

## Examples

### Example 1: Basic Usage

```powershell
Get-LapsADPasswordPolicy -Domain contoso.com
```

### Example 2: Advanced Usage

```powershell
Get-LapsADPassword -ComputerName * -AsPlainText | Export-Csv -Path laps_passwords.csv
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1087.002]] Domain Account Discovery (auditing LAPS for account info)
- [[Credentials in Files]] Password Policy Discovery (LAPS policy checks)
- [[Valid Accounts]] Valid Accounts (exploiting LAPS for local admin access)

### Tactics

- [[Discovery]] Discovery
- [[Lateral Movement]] Lateral Movement

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: PowerShell script block logging showing LAPSToolkit cmdlets (e.g., Get-LapsADPassword).
- Detection method 2: AD audit logs for ms-Mcs-AdmPwd attribute reads.
- Detection method 3: Unusual queries to LAPS OUs or extended rights.

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
- [[tools/AD-Module]]

## References

- Official LAPS Documentation: https://docs.microsoft.com/en-us/windows-server/identity/laps/laps-overview
- GitHub Repo: https://github.com/example/LAPSToolkit (adapt to actual repo)
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1552/
