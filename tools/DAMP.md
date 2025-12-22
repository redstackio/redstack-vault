---
id: 7a314edf-b511-40a5-a26f-ab8562382b14
type: tool
verified: true
created_at: '2019-08-28T21:17:36.098280Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - persistence
  - acl-modification
  - post-exploitation
  - windows-security
url: 'https://github.com/example/damp-project'
validated: true
---

# DAMP

**Status**: Unverified

## Overview

DAMP (Discretionary ACL Modification Project) is a PowerShell-based tool designed for achieving persistence in Windows environments through targeted modifications to host-based security descriptors and discretionary access control lists (ACLs). It enables attackers to alter permissions on files, directories, registry keys, and services to maintain unauthorized access over time, often evading standard detection mechanisms.

Common use cases include granting hidden access to critical system objects during post-exploitation phases, such as modifying ACLs on scheduled tasks or service binaries to allow backdoor execution.

## Description

DAMP leverages Windows' native security APIs (via .NET classes like System.Security.AccessControl) to enumerate, inspect, and modify ACLs without requiring external dependencies beyond PowerShell. It supports operations on NTFS objects, registry hives, and WMI classes, making it suitable for red team persistence scenarios. The tool emphasizes stealth by applying minimal changes and supporting inheritance propagation to child objects.

Key capabilities:
- ACL enumeration and auditing
- Adding/removing custom access control entries (ACEs)
- Propagating changes recursively
- Logging modifications for audit trails (optional)

It maps to MITRE ATT&CK techniques like T1547 (Boot or Logon Autostart Execution) and T1133 (External Remotely Stored Data) by enabling persistent modifications to security configurations.

## Features

- **Enumeration**: List detailed ACLs for any securable object.
- **Modification**: Add, remove, or replace ACEs with fine-grained control over rights and inheritance.
- **Stealth Mode**: Apply changes without triggering unnecessary events (e.g., avoid full propagation if possible).
- **Validation**: Verify applied changes post-modification.
- **Cross-Context Support**: Works in local, domain, and remote contexts via PSRemoting.

## Installation

### Requirements

- PowerShell 5.1 or later (Windows 10/Server 2016+)
- Administrative privileges for ACL modifications
- .NET Framework 4.5+ (standard on modern Windows)

### Install Commands

```powershell
# Download and import the module from GitHub
Invoke-WebRequest -Uri "https://github.com/example/damp-project/releases/latest/download/DAMP.psm1" -OutFile "$env:USERPROFILE\Documents\DAMP.psm1"

# Or clone the repo and import
git clone https://github.com/example/damp-project.git
Import-Module .\damp-project\DAMP.psm1
```

For domain environments, distribute via Group Policy or lateral movement tools.

## Basic Usage

```powershell
Import-Module DAMP
Get-Command -Module DAMP  # List available cmdlets
Get-DampAcl -Path "C:\Windows"  # Basic enumeration
```

### Common Options

| Option | Description |
|--------|-------------|
| -Path | Target object path |
| -Principal | SID or name of security principal |
| -Rights | Access mask (e.g., GenericAll) |
| -Recurse | Apply to child objects |
| -WhatIf | Preview changes without applying |

## Examples

### Example 1: Basic Usage

Enumerate ACLs on a directory:

```powershell
Import-Module DAMP; Get-DampAcl -Path "C:\ProgramData"
```

### Example 2: Advanced Usage

Add persistent access for a user:

```powershell
Import-Module DAMP; Set-DampAcl -Path "C:\Windows\System32\config" -Principal "DOMAIN\backdoor_user" -Rights "FullControl" -Operation "Add" -Recurse
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Event Triggered Execution]] Event Triggered Execution
- [[Boot or Logon Autostart Execution]] Boot or Logon Autostart Execution
- [[External Remote Services]] External Remotely Stored Data

### Tactics

- [[Persistence]] Persistence
- [[Privilege Escalation]] Privilege Escalation

## Detection

Indicators and methods for detecting this tool's usage:

- PowerShell module imports or script block logging showing DAMP cmdlets.
- Unexpected ACL changes on critical paths (monitor via Sysmon Event ID 13 or File Integrity Monitoring).
- Audit policy events for SACL modifications (Event ID 5136/5137).
- Anomalous permissions granted to non-standard principals on system objects.

Enable advanced auditing for object access and review for propagation patterns.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/PowerSploit]]
- [[SharpACL]]

## References

- Official GitHub: https://github.com/example/damp-project
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1546/
- Windows Security Descriptor Documentation: https://docs.microsoft.com/en-us/windows/win32/secauthz/security-descriptors
