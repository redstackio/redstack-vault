---
id: ffff0a53-92ca-424a-b536-3ad4b414eb34
name: kekeo
type: tool
verified: true
created_at: '2019-08-28T21:17:40.246701+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - kerberos
  - active-directory
  - post-exploitation
  - ticket-manipulation
url: 'https://github.com/gentilkiwi/kekeo'
commands:
  - '[[commands/kekeo-tgt-ask]]'
  - '[[commands/kekeo-pac-view]]'
  - '[[commands/kekeo-golden-ask]]'
validated: true
---

# kekeo

**Status**: Unverified

## Overview

Kekeo is a C-based toolbox for manipulating Microsoft Kerberos tickets and structures on Windows systems. Developed by Philippe Saouter (gentilkiwi), it is commonly used in red team operations for Active Directory attacks, including ticket requesting, forging (Golden/Silver Tickets), PAC analysis, and pass-the-ticket techniques. It excels in offline ticket manipulation without requiring domain controller access.

## Description

Kekeo provides modules for interacting with Kerberos in ways that enable advanced post-exploitation, such as generating persistent access via forged tickets or analyzing captured tickets for privilege information. It is particularly valuable in environments where tools like Mimikatz are detected, as Kekeo offers similar functionality with a smaller footprint. Use cases include lateral movement, privilege escalation, and defense evasion in Windows/Active Directory networks.

## Features

- Feature 1: Ticket requesting (TGT, TGS) using hashes or certificates
- Feature 2: PAC (Privilege Attribute Certificate) viewing and modification
- Feature 3: Golden and Silver Ticket forging for domain persistence
- Feature 4: Over-Pass-The-Hash (OPTH) and S4U2Self/S4U2Proxy abuse
- Feature 5: Export/import of tickets in .kirbi format for compatibility with other tools

## Installation

### Requirements

- Windows system (x86 or x64)
- Visual Studio or MinGW for compilation (if building from source)
- Administrative privileges for ticket injection

### Install Commands

Kekeo is typically compiled from source or downloaded as pre-built binaries from the GitHub releases.

```cmd
# Clone the repository
 git clone https://github.com/gentilkiwi/kekeo.git

# Build using Visual Studio (nmake or msbuild)
 cd kekeo
 nmake -f makefile.vc

# Or download pre-built exe from releases
# Place kekeo.exe in your working directory
```

For Kali Linux cross-compilation or WSL, use MinGW-w64.

## Basic Usage

```cmd
kekeo.exe
```

This displays the help menu with available modules like tgt::ask, pac::view, golden::ask.

### Common Options

| Option | Description |
|--------|-------------|
| /in:FILE | Input file (e.g., ticket.kirbi) |
| /out:FILE | Output file for exported data |
| /user:NAME | Specify username |
| /domain:NAME | Specify domain |
| /ptt | Pass-the-ticket (inject to session) |
| /export | Export ticket to file |

## Examples

### Example 1: Basic Usage

Request a TGT and inject it:

```cmd
kekeo.exe "tgt::ask /user:targetuser /domain:lab.local /rc4:$_NTLM_HASH /ptt"
```

### Example 2: Advanced Usage

Forge a Golden Ticket:

```cmd
kekeo.exe "golden::ask /user:administrator /domain:lab.local /sid:S-1-5-21-... /krbtgt:$_KRBGTG_HASH /ptt"
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Pass the Ticket]] - Use Alternate Authentication Material: Pass the Ticket
- [[Golden Ticket]] - Steal or Forge Kerberos Tickets: Golden Ticket
- [[Silver Ticket]] - Steal or Forge Kerberos Tickets: Silver Ticket

### Tactics

- [[Persistence]] - Persistence
- [[Privilege Escalation]] - Privilege Escalation
- [[Exfiltration]] - Lateral Movement

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for kekeo.exe execution via Sysmon or EDR (process creation with command-line arguments containing 'tgt::ask' or 'golden::ask')
- Detection method 2: Kerberos event logs (Event ID 4768, 4769) for anomalous TGT/TGS requests or unusual ticket lifetimes
- Detection method 3: LSASS memory access patterns or ticket injection via API hooks (e.g., LsaLogonUser)
- Detection method 4: Network traffic to domain controllers with forged tickets (anomalous auth patterns)

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
- [[tools/Rubeus]]
- [[tools/Impacket]]

## References

- Official GitHub: https://github.com/gentilkiwi/kekeo
- Blog post by author: https://blog.gentilkiwi.com
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1558/
