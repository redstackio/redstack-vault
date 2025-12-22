---
id: ac5e765a-8406-494b-b93a-ea8f4f0e06cf
type: tool
verified: true
created_at: '2019-08-28T21:17:36.195531+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - privilege-escalation
  - token-manipulation
  - post-exploitation
  - powershell
url: 'https://github.com/S3cur3Th1sDud3/Tokenvator'
commands:
  - '[[commands/import-tokenvator-module]]'
  - '[[commands/get-winlogon-sessions]]'
  - '[[commands/impersonate-access-token]]'
validated: true
---

# Tokenvator

**Status**: Unverified

## Overview

Tokenvator is a PowerShell-based tool designed for Windows token manipulation and impersonation. It enables red team operators to duplicate and impersonate access tokens from existing processes, facilitating privilege escalation without the need for new process creation, which helps evade detection.

## Description

Tokenvator leverages Windows API calls to interact with logon sessions and access tokens. It is particularly useful in post-exploitation scenarios where an attacker has initial foothold and needs to impersonate a privileged user (e.g., SYSTEM or Administrator) to access restricted resources. The tool supports enumeration of logon sessions and seamless token duplication, making it a key component in lateral movement and persistence operations.

## Features

- Feature 1: Enumerate active WinLogon sessions to identify high-privilege tokens.
- Feature 2: Duplicate and impersonate tokens from running processes without spawning new executables.
- Feature 3: Supports targeting specific users or process IDs for precise escalation.

## Installation

### Requirements

- PowerShell 3.0 or later on Windows (Server 2008 R2+ or Windows 7+).
- Administrative privileges for token operations.
- .NET Framework 4.0+.

### Install Commands

```powershell
# Download from GitHub
Invoke-WebRequest -Uri "https://github.com/S3cur3Th1sDud3/Tokenvator/archive/master.zip" -OutFile "Tokenvator.zip"
Expand-Archive -Path "Tokenvator.zip" -DestinationPath "C:\Tools\"

# Or clone the repository if Git is available
# git clone https://github.com/S3cur3Th1sDud3/Tokenvator.git C:\Tools\Tokenvator
```

## Basic Usage

```powershell
tool-name --help
```
Import the module first using [[commands/import-tokenvator-module]], then enumerate sessions with [[commands/get-winlogon-sessions]].

### Common Options

| Option | Description |
|--------|-------------|
| -Force | Overwrite existing module if loaded |
| -Verbose | Enable verbose output for debugging |

## Examples

### Example 1: Basic Usage

```powershell
Import-Module C:\Tools\Tokenvator\Tokenvator.ps1
Get-WinLogon
```

### Example 2: Advanced Usage

```powershell
Import-Module Tokenvator.ps1
$adminSession = Get-WinLogon | Where-Object {$_.UserName -eq "Administrator"}
Invoke-TokenImpersonation -ProcessId $adminSession.ProcessId -UserName "Administrator"
# Now execute privileged commands
whoami /priv
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Access Token Manipulation]] Access Token Manipulation
- [[Token Impersonation-Theft]] Token Impersonation/Theft

### Tactics

- [[Privilege Escalation]] Privilege Escalation
- [[Lateral Movement]] Lateral Movement

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor PowerShell script block logging for imports of suspicious modules or API calls to OpenProcessToken/LogonUser.
- Detection method 2: Audit token duplication events in Windows Security logs (Event ID 4672, 4673) for unexpected privilege changes.
- Detection method 3: Behavioral analytics for processes accessing tokens of higher-privilege sessions without legitimate reasons.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Mimikatz]]
- [[tools/PowerSploit]]

## References

- Official GitHub Repository: https://github.com/S3cur3Th1sDud3/Tokenvator
- Author Blog: https://www.netspi.com/blog/entryid/2203/tokenvator-impersonating-users-with-access-tokens
