---
id: 21d8c278-abb6-4c9c-b2f7-19da2e6a0a47
name: Windows-Credential-Editor
type: tool
verified: true
created_at: '2020-03-04T20:57:18.799875+00:00'
updated_at: '2023-05-30T19:50:48.357211+00:00'
commands:
  - '[[commands/wce-list-logon-sessions]]'
platforms:
  - Windows
tags:
  - administrator
  - cryptography
  - ntlm
  - pass-the-hash
url: 'https://www.ampliasecurity.com/research/windows-credentials-editor/'
validated: true
---

# Windows-Credential-Editor

**Status**: ✓ Verified

## Overview

Windows Credential Editor (WCE) is a post-exploitation security tool designed to manage credentials in Windows logon sessions. It allows users to list existing logon sessions, add new credentials (including password hashes), modify existing ones, and delete them. WCE is particularly valuable in red team operations for extracting NTLM/LM hashes from memory, enabling pass-the-hash attacks or offline cracking without needing plaintext passwords. It supports Windows XP, 2003, Vista, 7, 2008, and 8.

## Description

WCE operates by interacting with the Windows Local Security Authority (LSA) to enumerate and manipulate credentials stored in active logon sessions. This makes it a key tool for credential access during privilege escalation or lateral movement. Common use cases include dumping hashes from interactive logons, service accounts, or network sessions for subsequent exploitation. Note that WCE requires administrative privileges to access protected sessions and does not persist changes across reboots.

## Features

- Feature 1: Enumerate all active logon sessions with associated credentials (usernames, domains, LM/NTLM hashes).
- Feature 2: Inject arbitrary credentials (plaintext or hashes) into sessions for pass-the-hash or pass-the-ticket attacks.
- Feature 3: Modify or clear credentials in specific sessions to evade detection or facilitate pivoting.
- Feature 4: Support for both 32-bit and 64-bit Windows architectures.

## Installation

### Requirements

- Administrative access on the target Windows machine.
- Compatible with Windows XP through 8 (32-bit or 64-bit).

### Install Commands

WCE is a standalone executable; no installation is required. Download the appropriate binary:

1. Visit the official research page: https://www.ampliasecurity.com/research/windows-credentials-editor/
2. Download the x86 (32-bit) or x64 (64-bit) version matching the target architecture.
3. Transfer the executable (wce.exe) to the target system via SMB, HTTP, or other means.
4. Run directly from the command line (e.g., in an elevated Command Prompt).

For Kali Linux (for compilation or testing):

```bash
# Clone the repository if source is available (note: binaries are pre-compiled)
git clone https://github.com/Apriorit/windows-credentials-editor
cd windows-credentials-editor
# Compile with Visual Studio (Windows required)
```

## Basic Usage

```cmd
wce.exe --help
```

This displays available options, including listing (-l), adding (-w for password, -h for hash), and session targeting.

### Common Options

| Option | Description |
|--------|-------------|
| `-l, --list` | List all logon sessions and credentials |
| `-w, --add-password` | Add a plaintext password to a session |
| `-h, --add-hash` | Add an NTLM hash to a session for pass-the-hash |
| `-c, --clear` | Clear credentials from a session |
| `--session <ID>` | Target a specific logon session ID |

## Examples

### Example 1: Basic Usage (List Sessions)

```cmd
wce.exe -l
```

This enumerates and displays all logon sessions with extracted credentials.

### Example 2: Advanced Usage (Inject Hash)

```cmd
wce.exe -w administrator_hash --session 0x123456
```

This injects an NTLM hash into a specific session for immediate use in network authentication.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Credential Dumping]] OS Credential Dumping
- [[Use Alternate Authentication Material]] Use Alternate Authentication Material
- [[Pass the Hash]] Pass the Hash

### Tactics

- [[Credential Access]] Credential Access
- [[Lateral Movement]] Lateral Movement

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for wce.exe execution via Sysmon Event ID 1 (process creation) or Windows Event Logs (Security ID 4688).
- Detection method 2: Look for anomalous LSA API calls (e.g., LsaLogonUser) using ETW logging or API monitoring tools like API Monitor.
- Detection method 3: Unusual credential modifications in memory; use tools like Volatility for post-incident analysis of memory dumps.
- Detection method 4: Network anomalies from pass-the-hash attempts, such as unexpected NTLM authentication spikes.

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

## References

- Official research page: https://www.ampliasecurity.com/research/windows-credentials-editor/
- GitHub mirror (if available): https://github.com/Apriorit/windows-credentials-editor
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1003/
