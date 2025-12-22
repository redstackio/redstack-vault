---
id: c8ab85f1-5286-4026-a858-9bf595c70776
type: tool
verified: true
created_at: '2019-08-28T21:17:32.386532+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - gpo
  - audit
  - powershell
  - discovery
url: 'https://github.com/PowerShellMafia/PowerSploit'
commands:
  - '[[commands/grouper-run-domain-audit]]'
  - '[[commands/grouper-audit-gpo-path]]'
validated: true
---

# Grouper

**Status**: Unverified

## Overview

Grouper is a PowerShell script designed for auditing Active Directory Group Policy Objects (GPOs) to identify misconfigurations and vulnerabilities that could be exploited for privilege escalation, lateral movement, or unauthorized access in Windows domain environments.

## Description

Grouper parses GPO XML files from SYSVOL and analyzes settings such as restricted groups, security filtering, delegation, and password policies. It is particularly useful in red team engagements for discovering paths to domain admin privileges through weak GPO configurations. The tool outputs human-readable reports highlighting high-risk settings, making it easier to chain with other AD attack techniques.

## Features

- Enumerates and audits all GPOs in a domain
- Checks for unrestricted group memberships (e.g., Domain Admins open to Everyone)
- Identifies weak security filtering and delegation
- Detects insecure password policies and registry settings
- Supports auditing specific GPO paths for targeted analysis
- Verbose output for detailed logging

## Installation

### Requirements

- PowerShell 3.0 or higher
- Domain-joined Windows machine with network access to SYSVOL
- Active Directory module (optional, for enhanced enumeration)

### Install Commands

```powershell
# Download from GitHub (PowerSploit repository)
Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/dev/Recon/Grouper.ps1' -OutFile 'Grouper.ps1'

# Or clone the repo
 git clone https://github.com/PowerShellMafia/PowerSploit.git
 cd PowerSploit/Recon
```

## Basic Usage

```powershell
.
Grouper.ps1 -Domain contoso.com
```

### Common Options

| Option | Description |
|--------|-------------|
| `-Domain <string>` | Specifies the target domain FQDN |
| `-Path <string>` | Path to a specific GPO XML file or directory |
| `-Verbose` | Enables detailed output |
| `-CheckUnrestricted` | Focuses on unrestricted groups only |

## Examples

### Example 1: Basic Usage

```powershell
.
Grouper.ps1 -Domain contoso.com
```

This runs a full audit of all GPOs in the contoso.com domain and reports potential issues.

### Example 2: Advanced Usage

```powershell
.
Grouper.ps1 -Path '\\dc01\SYSVOL\contoso.com\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}' -Verbose
```

Audits a specific GPO path with verbose logging.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1087.002]] Domain Groups
- [[Cloud Groups]] Permission Groups Discovery: Local Groups
- [[Group Policy Modification]] Domain Policy Modification

### Tactics

- [[Discovery]] Discovery
- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- PowerShell script block logging showing 'Grouper.ps1' execution
- Access to SYSVOL shares from non-admin accounts
- Anomalous file reads from GPO XML files (\SYSVOL\domain\Policies\{GUID}\*)
- Event ID 4104 in Windows Security logs for PowerShell activity

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

## References

- Official repository: https://github.com/PowerShellMafia/PowerSploit
- Author: @harmj0y (Will Schroeder)
- Related blog: https://blog.netspi.com/abusing-active-directory-group-policy-object-delegation-for-privilege-escalation/
