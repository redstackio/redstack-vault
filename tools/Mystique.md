---
type: tool
description: >-
  PowerShell module for interacting with Kerberos S4U extensions to audit and
  exploit delegation configurations.
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - kerberos
  - delegation
  - s4u
  - powershell
  - active-directory
url: 'https://github.com/FourCoreLabs/Mystique'
commands:
  - '[[commands/mystique-enumerate-risky-delegations]]'
  - '[[commands/mystique-request-s4u2self-ticket]]'
  - '[[commands/mystique-perform-s4u2proxy-impersonation]]'
validated: true
---

# Mystique

**Status**: Unverified

## Overview

Mystique is a PowerShell module designed for working with Kerberos S4U (Service for User) extensions. It helps blue teams audit risky Kerberos delegation settings in Active Directory environments and enables red teams to perform user impersonation attacks using Kerberos Constrained Delegation (KCD) with Protocol Transition. Common use cases include identifying unconstrained delegation, resource-based constrained delegation (RBCD) misconfigurations, and executing S4U2self/S4U2proxy flows for lateral movement.

## Description

The tool provides cmdlets to query domain controllers for delegation configurations and to generate Kerberos tickets via S4U extensions. S4U2self allows a service to obtain tickets on its own behalf, while S4U2proxy enables delegation to impersonate other users when protocol transition is allowed. This is particularly useful in Windows Active Directory environments for both defensive auditing (e.g., finding accounts with 'Trusted for Delegation') and offensive operations (e.g., privilege escalation from a compromised service account).

## Features

- Feature 1: Enumeration of risky delegation settings across users, computers, and groups.
- Feature 2: S4U2self ticket requests to enable protocol transition.
- Feature 3: S4U2proxy impersonation for accessing remote services as other users.
- Feature 4: Support for credential-based authentication and ticket export/import.

## Installation

### Requirements

- PowerShell 5.1 or later (Windows PowerShell or PowerShell Core).
- Access to an Active Directory domain controller.
- Appropriate permissions for LDAP queries and Kerberos requests.

### Install Commands

```powershell
# Clone from GitHub and import
Invoke-WebRequest -Uri https://github.com/FourCoreLabs/Mystique/archive/refs/heads/master.zip -OutFile Mystique.zip
Expand-Archive -Path Mystique.zip -DestinationPath .\Mystique
Import-Module .\Mystique\Mystique.psm1

# Alternative: If available via PowerShell Gallery (check for updates)
# Install-Module -Name Mystique -Force
# Import-Module Mystique
```

## Basic Usage

```powershell
Import-Module Mystique
Get-Command -Module Mystique
Get-Help Get-MystiqueRiskyDelegations -Full
```

### Common Options

| Option | Description |
|--------|-------------|
| -DomainController | Specifies the DC to query |
| -Domain | Target domain name |
| -Credential | Provides alternate credentials |
| -ServiceTicketPath | Path for exporting Kerberos tickets |

## Examples

### Example 1: Basic Usage

```powershell
Import-Module Mystique
Get-MystiqueRiskyDelegations -DomainController dc01.example.com -Domain example.com
```

### Example 2: Advanced Usage

```powershell
$cred = Get-Credential
$ticket = Request-S4U2self -ServicePrincipalName "HTTP/web.example.com" -UserPrincipalName "service@example.com" -Domain example.com -Credential $cred
Invoke-S4U2proxy -ServiceTicketPath $ticket.Path -TargetUser "admin@example.com" -TargetSPN "cifs/fileserver.example.com" -Domain example.com
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Steal or Forge Kerberos Tickets]] Steal or Forge Kerberos Tickets
- [[Application Access Token]] Application Access Token

### Tactics

- [[Lateral Movement]] Lateral Movement
- [[Persistence]] Persistence

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor PowerShell ScriptBlock logging for imports of 'Mystique' module or S4U-related cmdlets.
- Detection method 2: Audit Kerberos event logs (Event ID 4769 for TGS requests) for unusual S4U2self/S4U2proxy activity from service accounts.
- Detection method 3: LDAP query logs showing enumeration of msDS-AllowedToDelegateTo attributes.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Rubeus]]
- [[tools/PowerView]]

## References

- Official GitHub Repository: https://github.com/FourCoreLabs/Mystique
- Related Resources: Microsoft Docs on Kerberos S4U Extensions
