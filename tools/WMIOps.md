---
id: b1666240-c110-4ac1-be14-24d89cf682b5
name: WMIOps
type: tool
verified: true
created_at: '2019-08-28T21:17:38.492362+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - wmi
  - powershell
  - remote-execution
  - discovery
url: 'https://github.com/byt3bl33d3r/WMIOps'
validated: true
---

# WMIOps

**Status**: Unverified

## Overview

WMIOps is a PowerShell script that leverages Windows Management Instrumentation (WMI) to perform various actions on local or remote Windows hosts. It is particularly useful in penetration testing and red team engagements for tasks like process enumeration, service discovery, and remote command execution without traditional protocols like SMB or WinRM.

## Description

WMIOps provides a set of PowerShell functions to interact with WMI classes for offensive security operations. It allows attackers with valid credentials to query system information, execute commands, and manage resources remotely. The tool is lightweight and focuses on WMI's native capabilities to evade detection in environments where other remote access methods are monitored.

## Features

- Feature 1: Remote process and service enumeration via WMI queries.
- Feature 2: Command execution on remote hosts using WMI event consumers.
- Feature 3: Local system information gathering without external dependencies.
- Feature 4: Credential-based authentication for domain or local access.

## Installation

### Requirements

- PowerShell 3.0 or later on Windows.
- Administrative privileges for remote operations.
- Valid credentials for target hosts.

### Install Commands

```powershell
# Download the script from the repository
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/byt3bl33d3r/WMIOps/master/WMIOps.ps1" -OutFile "WMIOps.ps1"

# Or clone the repo if available
# git clone https://github.com/byt3bl33d3r/WMIOps.git
```

## Basic Usage

```powershell
tool-name --help
```

Load the script and use functions like Get-WMIProcess.

### Common Options

| Option | Description |
|--------|-------------|
| -ComputerName | Specify remote host |
| -Credential | Provide authentication credentials |
| -Namespace | WMI namespace (default: root\cimv2) |

## Examples

### Example 1: Basic Usage

```powershell
.\\WMIOps.ps1; Get-WMIProcess
```

### Example 2: Advanced Usage

```powershell
$cred = Get-Credential; .\\WMIOps.ps1; Invoke-WMICommand -ComputerName "target" -Credential $cred -Command "whoami"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Windows Management Instrumentation]] Windows Management Instrumentation
- [[PowerShell]] PowerShell

### Tactics

- [[Discovery]] Discovery
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor WMI queries via Event ID 5857 in Windows logs.
- Detection method 2: PowerShell script block logging for WMIOps function calls.
- Detection method 3: Unusual DCOM/WMI traffic to port 135.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Impacket]]
- [[tools/PowerSploit]]

## References

- Official GitHub: https://github.com/byt3bl33d3r/WMIOps
- WMI Documentation: https://docs.microsoft.com/en-us/windows/win32/wmisdk/wmi-start-page
