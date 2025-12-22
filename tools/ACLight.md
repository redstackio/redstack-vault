---
id: 73824499-e5c7-4d16-825a-bf54f60ced2d
type: tool
verified: true
created_at: '2019-08-28T21:17:39.068836+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - ad-enumeration
  - discovery
  - active-directory
  - privileged-accounts
  - shadow-admins
url: 'https://github.com/CrowdStrike/ACLight'
validated: true
---

# ACLight

**Status**: Unverified

## Overview

ACLight is a PowerShell-based tool developed by CrowdStrike for advanced enumeration of privileged accounts in Active Directory environments. It excels at discovering hidden or shadow administrators through group membership analysis, nested groups, and protected objects, making it invaluable for red team reconnaissance and blue team auditing of AD privilege structures.

## Description

ACLight automates the detection of domain privileged accounts that may not be immediately obvious, such as shadow admins who inherit privileges via indirect group memberships or AdminSDHolder protections. It queries LDAP for group enumerations, identifies paths to high-privilege groups like Domain Admins, and exports results for analysis. Commonly used in penetration testing to map attack paths in Windows/AD networks without requiring full domain admin access—anonymous binds often suffice for basic discovery.

## Features

- Feature 1: Enumerates direct and indirect (nested) memberships in privileged groups like Domain Admins, Enterprise Admins.
- Feature 2: Detects shadow admins by tracing privilege inheritance paths.
- Feature 3: Analyzes AdminSDHolder-protected objects to identify unintended privilege exposures.
- Feature 4: Exports detailed results to CSV for offline review and reporting.
- Feature 5: Supports both anonymous and authenticated modes for flexible deployment.

## Installation

### Requirements

- PowerShell 3.0 or later (Windows Server 2012+ or Windows 10+).
- Network access to a Domain Controller (ports 389/TCP for LDAP, 636/TCP for LDAPS).
- Optional: Active Directory module (Import-Module ActiveDirectory) for enhanced querying.

### Install Commands

```powershell
# Download from GitHub
Invoke-WebRequest -Uri "https://github.com/CrowdStrike/ACLight/archive/refs/heads/master.zip" -OutFile "ACLight.zip"

# Extract (using built-in Expand-Archive)
Expand-Archive -Path "ACLight.zip" -DestinationPath "C:\Tools"

# Navigate to the script directory
cd C:\Tools\ACLight-master
```

Alternatively, clone the repository if Git is available:

```powershell
git clone https://github.com/CrowdStrike/ACLight.git
cd ACLight
```

## Basic Usage

```powershell
.\ACLight.ps1 -Domain example.com
```

### Common Options

| Option | Description |
|--------|-------------|
| `-Domain` | Specifies the target AD domain (required). |
| `-Username` | Username for authenticated queries. |
| `-Password` | Password for the username (secure string or prompted). |
| `-ExportPath` | Directory to save CSV exports. |
| `-Verbose` | Enables detailed logging. |

## Examples

### Example 1: Basic Usage

```powershell
.\ACLight.ps1 -Domain corp.example.com
```

This performs anonymous enumeration and displays results in the console.

### Example 2: Advanced Usage

```powershell
.\ACLight.ps1 -Domain corp.example.com -Username recon-user -Password 'P@ssw0rd' -ExportPath C:\Results -Verbose
```

This uses credentials, exports to CSV, and provides verbose output.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Account Discovery]] Account Discovery
- [[Permission Groups Discovery]] Permission Groups Discovery

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor LDAP queries for unusual group enumeration patterns (e.g., frequent binds to privileged group OUs) via Windows Event Logs (ID 4624, 4768).
- Detection method 2: PowerShell script execution logs (Module Logging, Script Block Logging) showing ACLight.ps1 invocation or LDAP connections from non-admin hosts.
- Detection method 3: Network traffic to DCs on LDAP ports from unexpected sources; use tools like Zeek or Sysmon for anomaly detection.

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
- [[tools/BloodHound]]

## References

- Official GitHub: https://github.com/CrowdStrike/ACLight
- CrowdStrike Blog: https://www.crowdstrike.com/blog/hunting-hidden-admins/
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1087/
