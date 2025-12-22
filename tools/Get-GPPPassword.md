---
id: a618682c-4351-44ea-877f-0aeb63938383
name: Get-GPPPassword
type: tool
verified: true
created_at: '2019-08-28T21:17:38.226737+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - credential-access
  - gpp
  - active-directory
  - powershell
url: >-
  https://github.com/PowerShellMafia/PowerSploit/blob/master/Exfiltration/Get-GPPPassword.ps1
validated: true
---

# Get-GPPPassword

**Status**: Unverified

## Overview

Get-GPPPassword is a PowerShell script designed to retrieve and decrypt plaintext passwords stored in Group Policy Preferences (GPP) files within an Active Directory environment. It targets the SYSVOL share where GPP XML files are stored, exploiting a historical misconfiguration (pre-2014) where passwords were stored in an easily decryptable format using a static AES key. This tool is commonly used in red team engagements for credential access after initial domain access is gained.

## Description

The tool parses XML files in the SYSVOL directory (e.g., Groups.xml, Services.xml, ScheduledTasks.xml, DataSources.xml, and Drives.xml) for elements containing the 'cpassword' attribute. It uses Microsoft's known static AES key to decrypt these values, revealing usernames and passwords for service accounts, local admins, or scheduled tasks. While Microsoft removed this feature in 2014, legacy policies may still exist in many environments. The script requires domain-joined access or SMB access to SYSVOL and runs entirely in memory using native PowerShell, making it stealthy for post-exploitation.

## Features

- Feature 1: Automatic discovery and parsing of all relevant GPP XML files in SYSVOL.
- Feature 2: Decryption of cpassword attributes using the hardcoded Microsoft AES key.
- Feature 3: Output of structured data including username, password, and source file path for easy integration into further attacks.
- Feature 4: No external dependencies beyond PowerShell; runs on Windows domain-joined systems.

## Installation

### Requirements

- PowerShell 2.0 or later (native on Windows 7+).
- Domain user credentials with read access to SYSVOL (typically any authenticated domain user).
- Network access to the domain controller's SYSVOL share.

### Install Commands

Download and execute directly; no formal installation needed:

```powershell
# Download from GitHub
Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Exfiltration/Get-GPPPassword.ps1' -OutFile 'Get-GPPPassword.ps1'

# Import and run
. .\Get-GPPPassword.ps1
Get-GPPPassword
```

For Kali/Ubuntu (cross-platform via Wine or PS Core):

```bash
# Install PowerShell Core
sudo apt update && sudo apt install -y powershell

# Download script
wget https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Exfiltration/Get-GPPPassword.ps1

# Run in PowerShell
pwsh -File Get-GPPPassword.ps1
```

## Basic Usage

```powershell
Get-GPPPassword
```

This command scans the current domain's SYSVOL and outputs any discovered credentials.

### Common Options

| Option | Description |
|--------|-------------|
| None (function-based) | No CLI options; extend via PowerShell scripting (e.g., piping to Export-Csv). |
| Verbose output | Use PowerShell's -Verbose flag when calling the function. |

## Examples

### Example 1: Basic Usage

```powershell
# On a domain-joined Windows machine
. .\Get-GPPPassword.ps1
Get-GPPPassword
```

Outputs decrypted credentials if present.

### Example 2: Advanced Usage

```powershell
# Pipe to file for exfiltration
Get-GPPPassword | Out-File -Encoding ASCII gpp_creds.txt

# Or filter for specific files
Get-ChildItem \\domain.com\SYSVOL -Recurse -Filter "*.xml" | ForEach { if (Get-Content $_.FullName | Select-String 'cpassword') { Get-GPPPassword } }
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Group Policy Preferences]] Group Policy Preferences

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor PowerShell script block logging for imports of Get-GPPPassword.ps1 or execution of Get-GPPPassword function.
- Detection method 2: Audit SMB access to SYSVOL shares from non-admin accounts; look for XML parsing in process trees.
- Detection method 3: Enable Advanced Audit Policy for 'Audit Policy Change' to detect GPP modifications, though the tool is read-only.
- Detection method 4: Static AES key usage can be signatured in EDR rules for decryption attempts on cpassword fields.

## Related Procedures

- [[procedures/Enumerate-Domain-Credentials-via-GPP]]
- [[procedures/Dump-SYSVOL-for-Sensitive-Data]]

## Related Tools

- [[tools/PowerSploit]]
- [[tools/Impacket]]

## References

- Official repository: https://github.com/PowerShellMafia/PowerSploit
- Microsoft Security Advisory: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2014-1812
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1552/006/
