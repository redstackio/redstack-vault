---
id: 03b7977e-d7b6-4a64-a41b-61e90a648edb
name: dcom-shellexecute-calculator-execution
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:07.167035+00:00'
updated_at: '2023-04-10T20:25:47.007212+00:00'
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/DCOM Exploitation]]'
  - '[[tags/DCOM via ShellExecute]]'
commands:
  - '[[codes/powershell-dcom-shellexecute-calculator]]'
platforms:
  - Windows
tools: []
validated: true
---

# DCOM ShellExecute Calculator Execution

## Summary

This procedure demonstrates how to execute a remote process, such as the Windows Calculator, on a target Windows machine using the Distributed Component Object Model (DCOM) protocol via PowerShell. It leverages the ShellExecute method of the Windows Script Host Object to run commands remotely, enabling lateral movement in a network with authenticated access.

## Description

DCOM ShellExecute Calculator Execution involves instantiating a remote COM object (specifically the Windows Script Host Shell via its CLSID) on the target machine and invoking the ShellExecute function to launch 'calc.exe' through 'cmd.exe'. This technique requires valid credentials with sufficient privileges on the target and relies on DCOM being enabled (default on Windows). It is useful in Active Directory environments for lateral movement after initial access, allowing execution of arbitrary commands without relying on SMB or other common remote services. The execution runs in the context of the user invoking the DCOM call, typically hidden (SW_HIDE=0). Potential outcomes include successful remote command execution, but detection may occur via DCOM/RPC logs. This maps to MITRE ATT&CK T1021 for remote service execution in Windows environments.

## Requirements

1. Valid domain or local credentials with execute permissions on the target machine.
2. Network connectivity to the target over TCP port 135 (RPC endpoint mapper) and dynamic RPC ports (typically 49152-65535).
3. DCOM enabled on the target (default, but may be restricted via Group Policy).
4. PowerShell execution policy allowing script execution on the attacker's machine.
5. Target running Windows (tested on Windows 7+).

## Defense

- Disable or restrict DCOM for non-essential applications via dcomcnfg.exe or Group Policy (Computer Configuration > Administrative Templates > Windows Components > DCOM).
- Implement Least Privilege: Run DCOM services under low-privilege accounts and limit remote access.
- Monitor DCOM activation events (Event ID 10000-10016 in Microsoft-Windows-DistributedCOM/Operational log) and RPC traffic for anomalous calls to CLSID '9BA05972-F6A8-11CF-A442-00A0C90A8F39'.
- Use Windows Defender Application Control (WDAC) or AppLocker to block unsigned PowerShell scripts and unexpected process executions.
- Enable PowerShell logging (Module, Script Block, and Transcription) to capture remote invocations.

## Objectives

1. Remotely execute a benign process (Calculator) to validate DCOM access and lateral movement capability.
2. Demonstrate potential for arbitrary command execution in a compromised Active Directory environment.
3. Establish a foundation for more malicious payloads, such as reverse shells or persistence mechanisms.

## Instructions

### Step 1: Verify Network Access and Credentials

**Context**: Before executing the remote command, confirm connectivity to the target and test authentication. This ensures DCOM can establish a session without errors.

Use built-in PowerShell cmdlets to test RPC connectivity and authentication.

**Command** (use [[commands/test-netconnection-rpc]] if available, or inline):
```powershell
Test-NetConnection -ComputerName $_TARGET_IP -Port 135
```

> This command checks if the RPC endpoint mapper port is reachable. If it succeeds, proceed; otherwise, verify firewall rules or credentials.

### Step 2: Instantiate Remote DCOM Object and Execute Command

**Context**: Create an instance of the remote WScript.Shell COM object using its CLSID and invoke ShellExecute to run 'cmd.exe /c calc.exe' in the system32 directory. The operation is hidden to avoid visual indicators on the target.

**Command** ([[codes/powershell-dcom-shellexecute-calculator]]):
```powershell
$com = [Type]::GetTypeFromCLSID('9BA05972-F6A8-11CF-A442-00A0C90A8F39',"$_TARGET_IP")
$obj = [System.Activator]::CreateInstance($com)
$item = $obj.Item()
$item.Document.Application.ShellExecute("cmd.exe","/c calc.exe","C:\windows\system32",$null,0)
```

> This script remotely activates the Shell object on the target, then executes the Calculator. Replace $_TARGET_IP with the actual target IP. Run this in an elevated PowerShell session with domain credentials if needed (use Enter-PSSession or implicit remoting for auth).

### Step 3: Verify Execution on Target

**Context**: Confirm the command succeeded by checking for process creation or visual confirmation on the target (if accessible). Monitor for errors like access denied or CLSID not found.

Use remote querying if possible.

**Command** (use [[commands/get-process-remote]] if available, or inline):
```powershell
Get-WmiObject -Class Win32_Process -ComputerName $_TARGET_IP -Filter "Name='calc.exe'"
```

> This queries for the calc.exe process on the target. If it returns a process object, execution was successful. If no output or errors, check credentials and DCOM config.
