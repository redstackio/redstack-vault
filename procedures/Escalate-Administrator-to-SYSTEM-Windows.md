---
id: 72ea53f8-52b3-431a-9d59-cbddcf10c0ca
name: Escalate-Administrator-to-SYSTEM-Windows
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
tactics:
  - '[[Execution]]'
techniques:
  - '[[Service Execution]]'
sub_techniques: []
tags:
  - administrator
  - privileges
commands:
  - '[[commands/psexec-spawn-powershell-as-system]]'
platforms:
  - Windows
tools:
  - '[[tools/PsExec]]'
validated: true
---

# Escalate-Administrator-to-SYSTEM-Windows

## Summary

This procedure uses PsExec.exe to elevate from an Administrator session to SYSTEM privileges on a Windows target. It is effective for local or RDP access scenarios where UAC is not a barrier, spawning a new process window with SYSTEM context to perform higher-privileged actions like service manipulation or deeper system access.

## Description

PsExec, part of the Sysinternals suite, allows execution of processes on remote or local systems under the SYSTEM account by leveraging the Windows service control manager. Starting from an Administrator session, this technique creates a temporary service to launch the specified process (e.g., PowerShell or CMD) as SYSTEM. It does not bypass UAC prompts but works when Administrator rights are already obtained. This is commonly used in post-exploitation for privilege escalation, enabling actions like dumping credentials or installing persistence mechanisms that require SYSTEM level. The target environment is Windows (Vista and later), assuming physical, RDP, or console access to run the tool.

## Requirements

1. Administrator privileges on the target Windows machine.
2. Local, RDP, or console access to execute binaries.
3. PsExec.exe binary downloaded from the official Sysinternals site and placed on the target (or accessible path).
4. No antivirus blocking PsExec execution (may require temporary disablement).

## Defense

- Enable Windows Defender or endpoint protection to block unsigned binaries like PsExec.
- Monitor for service creation events (Event ID 7045) and process launches from unexpected parents.
- Implement application whitelisting (AppLocker or WDAC) to restrict Sysinternals tools.
- Log PowerShell and CMD executions for anomalous privilege levels.

## Objectives

1. Obtain a shell or process running as SYSTEM from an Administrator context.
2. Verify elevation by checking the current user token.
3. Enable further post-exploitation actions requiring SYSTEM access, such as LSASS dumping.

## Instructions

### Step 1: Download and Prepare PsExec

**Context**: Obtain the PsExec executable and transfer it to the target machine to ensure it's available for execution. This step requires internet access or pre-staged binaries.

Download PsExec from the official Microsoft Sysinternals site using [[tools/PsExec]] documentation. Copy the PsExec.exe file to a writable directory on the target, such as C:\Windows\Temp.

> Verify the file integrity after transfer to ensure no corruption.

### Step 2: Execute PsExec to Spawn SYSTEM Shell

**Context**: Run PsExec to launch a PowerShell process as SYSTEM on the local machine. Use the local computer target (denoted by \\\.) to elevate privileges without remote execution.

**Command** ([[commands/psexec-spawn-powershell-as-system]]):

```command_prompt
PsExec.exe -accepteula \\. powershell.exe
```

> This command accepts the EULA on first run and targets the local machine (\\.), spawning a new PowerShell window as SYSTEM. If a CMD shell is preferred, replace 'powershell.exe' with 'cmd.exe'. The new window will indicate SYSTEM context upon launch.

### Step 3: Verify Elevation

**Context**: Confirm the process is running as SYSTEM to validate successful escalation.

In the spawned PowerShell window, run the following to check the current user:

```powershell
whoami
```

> Expected result: 'nt authority\system'. If not SYSTEM, check for execution errors or access restrictions.
