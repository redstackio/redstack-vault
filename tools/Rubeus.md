---
id: 44df126a-caf9-4b77-887b-831fcd4868bc
type: tool
verified: true
created_at: '2019-08-28T21:17:19.894318+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Windows
tags:
  - kerberos
  - active-directory
  - post-exploitation
  - credential-access
url: 'https://github.com/GhostPack/Rubeus'
commands:
  - '[[commands/rubeus-kerberoast]]'
  - '[[commands/rubeus-asreproast]]'
  - '[[commands/rubeus-dump-tickets]]'
  - '[[commands/rubeus-pass-the-ticket]]'
  - '[[commands/rubeus-ask-tgt]]'
validated: true
---

# Rubeus

**Status**: Unverified

## Overview

Rubeus is a C# toolset designed for interacting with and abusing Kerberos in Active Directory environments. It provides functionality for common Kerberos attacks such as requesting and exporting service tickets for offline cracking (Kerberoasting), AS-REP roasting for users without pre-authentication, dumping cached tickets, and performing pass-the-ticket operations. Commonly used in red team engagements for credential access and lateral movement within Windows domains.

## Description

Rubeus is heavily adapted from Benjamin Delpy's Kekeo project and focuses on raw Kerberos protocol manipulation without relying on native Windows tools like Mimikatz in some cases. It supports actions like forging tickets, harvesting RC4 tickets, and injecting tickets into the current session. Ideal for post-exploitation scenarios where domain credentials need to be extracted or abused. It runs as a standalone executable on Windows systems with .NET Framework.

## Features

- **Kerberoasting**: Requests TGS tickets for service accounts and exports them for cracking.
- **AS-REP Roasting**: Targets users with 'Do not require Kerberos preauthentication' enabled to obtain crackable AS-REP responses.
- **Ticket Dumping**: Exports Kerberos tickets from the current LSA cache.
- **Pass-the-Ticket**: Injects tickets into the current session for impersonation.
- **TGT Requesting**: Requests Ticket Granting Tickets (TGTs) using provided credentials.
- **Ticket Harvesting**: Monitors and collects tickets over time.

## Installation

### Requirements

- Windows system with .NET Framework 4.0 or later.
- Compiled Rubeus.exe (source available on GitHub).
- Domain-joined machine or valid credentials for Kerberos operations.

### Install Commands

Rubeus is typically compiled from source or downloaded as a pre-built executable:

```powershell
# Clone and build from source (requires Visual Studio or .NET SDK)
git clone https://github.com/GhostPack/Rubeus.git
cd Rubeus
# Build using MSBuild or dotnet build (if .NET Core compatible fork)
msbuild Rubeus.sln
# Result: Rubeus.exe in bin/Debug or bin/Release
```

Alternatively, download pre-compiled binaries from trusted sources like the GhostPack releases.

## Basic Usage

```powershell
Rubeus.exe
```

This displays the help menu with all available actions (e.g., kerberoast, asreproast).

### Common Options

| Option | Description |
|--------|-------------|
| `/user:USERNAME` | Specifies a user for operations like AS-REP roasting. |
| `/domain:DOMAIN` | Targets a specific domain. |
| `/dc:DC_IP` | Specifies a domain controller IP. |
| `/outfile:FILE` | Exports output (e.g., hashes) to a file. |
| `/format:hashcat` | Formats output for tools like Hashcat. |
| `/nowrap` | Prevents wrapping long outputs. |

## Examples

### Example 1: Basic Usage

Run help to see actions:

```powershell
Rubeus.exe
```

### Example 2: Advanced Usage

Perform Kerberoasting and export to file:

```powershell
Rubeus.exe kerberoast /user:svc_account /domain:example.com /outfile:hashes.txt /format:hashcat
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Kerberoasting]] Kerberoasting
- [[AS-REP Roasting]] AS-REP Roasting
- [[Pass the Ticket]] Pass the Ticket
- [[Steal Application Access Token]] Steal or Forge Kerberos Tickets

### Tactics

- [[Credential Access]] Credential Access
- [[Lateral Movement]] Lateral Movement

## Detection

Indicators and methods for detecting this tool's usage:

- **Process Monitoring**: Look for Rubeus.exe execution or suspicious .NET processes making Kerberos API calls (e.g., LsaCallAuthenticationPackage).
- **Event Logs**: Windows Security Event ID 4769 (Kerberos Service Ticket Operations) with unusual service principal names or RC4 encryption.
- **Network Traffic**: Increased Kerberos traffic (ports 88/TCP, 445/TCP) to domain controllers, especially TGS requests for service accounts.
- **File Artifacts**: Presence of Rubeus.exe or exported .kirbi/.ccache files on disk.
- **EDR Signatures**: Heuristics for ticket dumping or injection behaviors.

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
- [[tools/Impacket]]
- [[tools/kekeo]]

## References

- [Official GitHub Repository](https://github.com/GhostPack/Rubeus)
- [GhostPack Documentation](https://github.com/GhostPack)
- MITRE ATT&CK: [Kerberoasting](https://attack.mitre.org/techniques/T1558/003/)
