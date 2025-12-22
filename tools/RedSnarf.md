---
id: de1d8469-0fec-49df-af20-a29d81c1221a
type: tool
verified: true
created_at: '2019-08-28T21:17:38.985806+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - credential-access
  - lsass
  - red-team
  - dumping
url: 'https://github.com/sutoo/RedSnarf'
commands:
  - '[[commands/redsnarf-lsass-dump-remote]]'
  - '[[commands/redsnarf-extract-kerberos-tickets]]'
validated: true
---

# RedSnarf

**Status**: Unverified

## Overview

RedSnarf is a red teaming tool designed for remote credential dumping in Windows Active Directory environments. It allows operators to extract LSASS process memory from remote systems over SMB without needing to execute code on the target, making it stealthier than traditional methods like ProcDump. Commonly used for harvesting NTLM hashes, Kerberos tickets, and other credentials during lateral movement and privilege escalation phases.

## Description

RedSnarf leverages Windows APIs and SMB to access and dump the LSASS process remotely using provided domain credentials. It supports extraction of various credential types, including password hashes and service tickets, which can be cracked offline or reused in attacks like pass-the-hash or pass-the-ticket. The tool is particularly useful in environments where direct remote execution is restricted by defenses like AppLocker or constrained delegation. It requires administrative privileges on the target but can operate from a non-domain-joined attacker machine.

## Features

- Remote LSASS memory dumping via SMB
- Extraction of NTLM hashes, Kerberos tickets, and LSA secrets
- Support for ticket export in .kirbi format for offline analysis
- Configurable output directories for dumps and artifacts
- Minimal footprint: no binaries dropped on target
- Integration with tools like Mimikatz for further processing

## Installation

### Requirements

- Windows attacker machine with .NET Framework 4.5 or later
- Visual Studio or build tools to compile from source (C#)
- Domain credentials with admin rights on target

### Install Commands

```powershell
# Clone the repository
Invoke-WebRequest -Uri https://github.com/sutoo/RedSnarf/archive/refs/heads/master.zip -OutFile RedSnarf.zip
Expand-Archive RedSnarf.zip -DestinationPath .\RedSnarf

# Build using Visual Studio or MSBuild
msbuild RedSnarf.sln /p:Configuration=Release

# Or download pre-compiled binary from releases (if available)
# Note: Always verify binaries from trusted sources
```

For Linux/Kali usage, run via Wine or in a Windows VM, though native Windows is recommended.

## Basic Usage

```powershell
redsnarf.exe --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and options |
| -v, --verbose | Enable verbose logging |
| -o, --output | Specify output directory for dumps |
| -d | Domain name |
| -u | Username |
| -p | Password |
| -x | Target IP or hostname |
| -t | Extract Kerberos tickets |

## Examples

### Example 1: Basic Usage

```powershell
redsnarf.exe -d corp.local -u administrator -p P@ssw0rd -x 192.168.1.100
```

Dumps LSASS and extracts basic credentials.

### Example 2: Advanced Usage

```powershell
redsnarf.exe -d corp.local -u administrator -p P@ssw0rd -x 192.168.1.100 -t -o ./redsnarf_output -v
```

Includes ticket extraction, verbose output, and custom directory.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Credential Dumping]] OS Credential Dumping
- [[Steal or Forge Kerberos Tickets]] Steal or Forge Kerberos Tickets
- [[Unsecured Credentials]] Unsecured Credentials

### Tactics

- [[Credential Access]] Credential Access
- [[Lateral Movement]] Lateral Movement

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual SMB traffic (e.g., high volume to port 445) from admin accounts
- LSASS process access events in Windows Event Logs (Event ID 4657, 4663)
- File creation of .dmp files on admin shares (ADMIN$\Temp)
- Network logs showing authentication spikes followed by file transfers
- EDR alerts on remote process memory access or credential extraction patterns

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
- [[tools/ProcDump]]
- [[tools/Rubeus]]

## References

- Official GitHub: https://github.com/sutoo/RedSnarf
- NCC Group Blog: https://www.nccgroup.com/us/research-blog/redsnarf-remote-lsass-dumping-tool/
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1003/
