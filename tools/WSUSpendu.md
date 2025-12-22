---
id: 2cd943ec-5e3f-49fa-bf70-54314c19c6c1
type: tool
verified: true
created_at: '2019-08-28T21:17:24.965851+00:00'
updated_at: '2023-10-01T12:00:00Z'
platforms:
  - Windows
tags:
  - wsus
  - lateral-movement
  - persistence
  - powershell
  - post-exploitation
url: 'https://github.com/nettitude/WSUSpendu'
commands:
  - '[[commands/wsuspendu-get-wsus-server]]'
  - '[[commands/wsuspendu-new-malicious-update]]'
  - '[[commands/wsuspendu-approve-update-for-clients]]'
validated: true
---

# WSUSpendu

**Status**: Unverified

## Overview

WSUSpendu is a PowerShell-based toolkit designed for extending compromises on Windows Server Update Services (WSUS) servers to domain-joined client machines. It enables attackers with administrative access to a WSUS server to create, package, and approve malicious updates that are automatically downloaded and installed by clients during routine update checks. Commonly used in red team engagements for lateral movement and persistence in Active Directory environments.

## Description

Once a WSUS server is compromised, WSUSpendu allows the creation of custom update metadata and payloads (typically in MSU format) that mimic legitimate Microsoft updates. These can include arbitrary executables, scripts, or implants. The tool interacts with the WSUS API to inject updates, approve them for specific computer groups, and monitor deployment. It requires domain admin privileges on the WSUS server and is particularly effective in enterprise networks where WSUS is used for patch management.

## Features

- Interact with WSUS server API to enumerate and manage updates
- Create malicious updates with custom titles, descriptions, and payloads
- Package payloads as signed or unsigned MSU files for stealth
- Approve updates for targeted computer groups or all clients
- Support for binary and non-binary update types
- Integration with PowerShell for scripting complex deployment scenarios

## Installation

### Requirements

- PowerShell 3.0 or later
- Administrative access to a WSUS server
- .NET Framework 4.0+ (typically present on Windows Server)
- Access to WSUS API (WSUS server role installed)

### Install Commands

```powershell
# Clone the repository from GitHub
Invoke-WebRequest -Uri https://github.com/nettitude/WSUSpendu/archive/master.zip -OutFile WSUSpendu.zip
Expand-Archive -Path WSUSpendu.zip -DestinationPath .\WSUSpendu

# Or use git if available
# git clone https://github.com/nettitude/WSUSpendu.git

# Import the module (run on the WSUS server)
Import-Module .\WSUSpendu\WSUSpendu.psm1
```

On Kali or Linux, use PowerShell Core (pwsh) for cross-platform testing, but full functionality requires Windows.

## Basic Usage

```powershell
# Import the module
Import-Module WSUSpendu.psm1

# View available commands
Get-Command -Module WSUSpendu
```

### Common Options

WSUSpendu functions typically use standard PowerShell parameters like -Verbose, -Debug, and custom ones for WSUS objects (e.g., -UpdateServer, -Title).

| Option | Description |
|--------|-------------|
| -Verbose | Enable verbose output for troubleshooting |
| -UpdateServer | Specify the WSUS server object |
| -ComputerGroup | Target specific WSUS computer groups |
| -Action | Approval action (e.g., Install, Detect) |

## Examples

### Example 1: Basic Usage

Connect to WSUS and list updates:

```powershell
$wsus = Get-WSUSServer
Get-WSUSUpdate -UpdateServer $wsus
```

### Example 2: Advanced Usage

Create and approve a malicious update (see related commands for details):

```powershell
$wsus = Get-WSUSServer
$update = New-WSUSMaliciousUpdate -UpdateServer $wsus -Title "Critical Security Patch" -MSUPath "C:\payload.msu"
Approve-WSUSUpdate -Update $update -Action Install -ComputerGroups "All Computers"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Supply Chain Compromise]] Supply Chain Compromise
- [[Remote File Copy]] Ingress Tool Transfer
- [[PowerShell]] PowerShell

### Tactics

- [[Lateral Movement]] Lateral Movement
- [[Persistence]] Persistence
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual PowerShell module imports on WSUS servers (monitor ScriptBlock logging for WSUSpendu.psm1)
- Anomalous update creations or approvals in WSUS console/logs (e.g., non-Microsoft publishers)
- Client-side: Unexpected MSU file downloads or installations from internal WSUS endpoints
- Network: Increased SMB/HTTP traffic to WSUS server during off-hours
- Event Logs: WSUS API calls (Event ID 10016 in Microsoft-Windows-WSUS) or PowerShell execution logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/PowerShell Empire]] (for payload generation)
- [[tools/Covenant]] (C2 framework integration)
- [[tools/Metasploit]] (MS17-010 for initial WSUS compromise)

## References

- Official GitHub Repository: https://github.com/nettitude/WSUSpendu
- Blog Post: https://www.nettitude.com/blog/wsuspendu-
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1195/
