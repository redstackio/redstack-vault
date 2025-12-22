---
id: c0a1c1e5-c457-44c3-b371-b6962a6bfdd7
type: tool
verified: true
created_at: '2019-08-28T21:17:38.065570+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Windows
tags:
  - cryptography
  - extract
  - ntlm
  - pass-the-hash
  - credential-access
url: 'https://github.com/gentilkiwi/mimikatz'
commands:
  - '[[commands/extract-windows-lm-ntlm-hashes-from-lsass]]'
validated: true
---

# Mimikatz

**Status**: Unverified

## Overview

Mimikatz is a post-exploitation tool designed for extracting plaintext credentials, NTLM/LM hashes, PIN codes, and Kerberos tickets directly from Windows memory. It is widely used in penetration testing and red team operations to demonstrate flaws in Windows authentication, enabling attacks such as pass-the-hash, pass-the-ticket, and golden ticket creation.

## Description

Mimikatz interacts with Windows components like LSASS (Local Security Authority Subsystem Service) to dump sensitive authentication data. It supports modules for credential dumping, privilege escalation, and token manipulation. While powerful, its use requires administrative privileges and can trigger endpoint detection responses. It is categorized under Credential Access in offensive security workflows.

## Features

- Credential extraction from LSASS process memory (hashes and cleartext passwords)
- Kerberos ticket listing, forging, and injection (pass-the-ticket attacks)
- Dumping of SAM (Security Accounts Manager) hashes and LSA (Local Security Authority) secrets
- Over-the-shoulder keystroke logging and PIN code extraction
- Support for offline hash cracking preparation and alternate authentication material usage

## Installation

### Requirements

- Windows 10 or later (for compilation and execution)
- Microsoft Visual Studio 2013 (Community or Professional edition)
- Windows Driver Kit (WDK) 7.1 for building components
- Git for cloning the repository

### Install Commands

Mimikatz is typically compiled from source for security and compatibility. Precompiled binaries exist but are not recommended for production testing due to potential tampering.

1. Download and install Visual Studio 2013 from: https://visualstudio.microsoft.com/vs/older-downloads/

2. Download and install Windows Driver Kit 7.1 from Microsoft archives (search for "WDK 7.1 download" as official links may vary).

3. Clone the Mimikatz repository:

```cmd
git clone https://github.com/gentilkiwi/mimikatz.git
cd mimikatz
```

4. Open `mimikatz.sln` in Visual Studio 2013.

5. Set the Solution Platform to match the target architecture (x64 for 64-bit Windows or Win32 for 32-bit).

6. Go to Build > Rebuild Solution.

7. Compiled binaries (including `mimikatz.exe`) will be located in `\.\mimikatz\x64` or `\.\mimikatz\Win32`.

For execution, run as administrator. On Kali Linux, use Wine for compatibility, but native Windows is preferred.

## Basic Usage

```cmd
mimikatz.exe
```

This launches the interactive Mimikatz prompt. For non-interactive use:

```cmd
mimikatz.exe "command_here" exit
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Display help (limited in Mimikatz) |
| privilege::debug | Elevate to debug privileges (required for many modules) |
| /in:filename.txt | Run commands from a file |
| exit | Exit the Mimikatz session |

## Examples

### Example 1: Basic Usage (Interactive)

```cmd
mimikatz.exe
```

At the prompt: `sekurlsa::logonpasswords` to dump credentials.

### Example 2: Advanced Usage (Non-Interactive Credential Dump)

```cmd
mimikatz.exe "privilege::debug" "sekurlsa::logonpasswords" exit
```

This enables debug privileges and dumps logon passwords/hashes.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Credential Dumping]] OS Credential Dumping
- [[LSASS Memory]] LSASS Memory
- [[Use Alternate Authentication Material]] Use Alternate Authentication Material
- [[Pass the Hash]] Pass the Hash
- [[Steal or Forge Kerberos Tickets]] Steal or Forge Kerberos Tickets
- [[Golden Ticket]] Golden Ticket

### Tactics

- [[Credential Access]] Credential Access
- [[Persistence]] Persistence (via ticket manipulation)

## Detection

Indicators and methods for detecting this tool's usage:

- Process creation of `mimikatz.exe` or suspicious DLL loads
- Unauthorized access to LSASS process (Event ID 4657 in Windows logs)
- Anomalous memory reads from `lsass.exe` (via Sysmon or EDR tools)
- Network activity if used with remote execution (e.g., via PSEXEC)
- Hash values of known Mimikatz binaries in file integrity monitoring
- PowerShell or command-line arguments containing `sekurlsa`, `lsadump`, or `kerberos`

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Impacket]] (for pass-the-hash execution)
- [[tools/CrackMapExec]] (for credential testing)

## References

- Official GitHub Repository: https://github.com/gentilkiwi/mimikatz
- Blog Post by Author: https://blog.gentilkiwi.com
- MITRE ATT&CK Tool Page: https://attack.mitre.org/tools/T1003/
