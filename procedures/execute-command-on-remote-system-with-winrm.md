---
id: 7eb51561-76d8-4ef5-9874-b3f9548be45e
name: execute-command-on-remote-system-with-winrm
type: procedure
verified: true
submitted: false
created_at: '2020-03-21T02:22:47.189795+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Windows-Remote-Management|T1021.006 - Windows Remote
    Management]]
sub_techniques: []
tags:
  - '[[tags/Network]]'
  - '[[tags/powershell]]'
  - '[[tags/shell]]'
commands:
  - '[[commands/create-windows-pscredential-object]]'
  - '[[commands/create-powershell-session-and-execute-command]]'
  - '[[commands/remove-powershell-session]]'
platforms:
  - Windows
tools: []
validated: true
---

# execute-command-on-remote-system-with-winrm

## Summary

This procedure demonstrates how to establish a PowerShell remoting session (PSSession) on a remote Windows system using Windows Remote Management (WinRM) and execute an arbitrary command. It is useful for lateral movement in Windows environments where WinRM is enabled, allowing attackers with valid credentials to run commands remotely without needing additional tools like RDP or SMB.

## Description

Windows Remote Management (WinRM) is a Microsoft implementation of WS-Management protocol that enables remote PowerShell execution over HTTP/HTTPS. This procedure creates a secure credential object from username and password, initiates a PSSession to the target, invokes a command via a script block, and optionally cleans up the session. It assumes the target has WinRM configured (e.g., via Enable-PSRemoting) and the attacker has network access and valid credentials. Success grants command execution on the target, potentially leading to further post-exploitation activities like privilege escalation or data exfiltration. This maps to MITRE ATT&CK techniques for execution and lateral movement in Active Directory environments.

## Requirements

1. PowerShell 3.0 or later on the attacker's machine.
2. Valid domain or local credentials (username and password) for the target system.
3. Network connectivity to the target on port 5985 (HTTP) or 5986 (HTTPS).
4. WinRM service enabled and configured on the target (listener active, authentication allowed).
5. Administrative privileges may be required for certain commands; basic user creds suffice for non-elevated execution.

## Defense

- Enable PowerShell remoting logging via Group Policy (Module Logging, Script Block Logging) to capture invoked commands.
- Monitor WinRM traffic with network IDS for anomalous connections (e.g., unusual source IPs or command patterns).
- Restrict WinRM access via firewalls to trusted hosts only and use HTTPS with certificate authentication.
- Implement just-in-time privilege elevation (e.g., via Privileged Access Workstations) to limit credential scope.
- Use tools like Sysmon or Windows Event Logs (Event ID 4104 for PowerShell) to detect remote execution.

## Objectives

1. Establish a secure remote PowerShell session to the target Windows system.
2. Execute an arbitrary command on the target to achieve execution or gather information.
3. Clean up the session to avoid detection and resource exhaustion.
4. Verify successful command execution through output or side effects on the target.

## Instructions

### Step 1: Create PSCredential Object

**Context**: Before connecting to the remote system, convert the plaintext password into a secure string and package it with the username into a PSCredential object. This is necessary for authentication over WinRM and prevents exposing the password in logs or memory.

**Command** ([[commands/create-windows-pscredential-object]]):
```powershell
$Pass = ConvertTo-SecureString -String "$_PASSWORD" -AsPlainText -Force
$Cred = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList "$_USER", $Pass
```

> This command creates a secure credential object usable for remoting. Replace $_USER with the target username (e.g., 'domain\user') and $_PASSWORD with the plaintext password. The -AsPlainText -Force flags are used for simplicity in testing but should be avoided in production for security reasons. Expected output is no visible response if successful; verify by piping $Cred to Get-Credential or checking for errors.

### Step 2: Create PSSession and Execute Command

**Context**: Use the credential to establish a new PSSession to the target IP, then invoke a script block to run the desired command. This step achieves remote execution. Note that using Start-Process runs the command asynchronously without returning output; remove it for interactive or output-capturing execution.

**Command** ([[commands/create-powershell-session-and-execute-command]]):
```powershell
$Session = New-PSSession -ComputerName $_TARGET_IP -Credential $Cred
Invoke-Command -Session $Session -ScriptBlock {Start-Process $_CMD}
```

> Replace $_TARGET_IP with the target's IP or hostname, $Cred with the object from Step 1, and $_CMD with the command (e.g., 'notepad.exe' or 'whoami'). If Start-Process is omitted, use {$_CMD} directly for synchronous execution and output capture. Expected output includes session ID confirmation and any command results if not backgrounded; errors indicate authentication or connectivity issues.

### Step 3: Clean Up PSSession

**Context**: After execution, remove the session to free resources and reduce forensic footprints. This prevents idle sessions from being detected or causing denial-of-service on the target.

**Command** ([[commands/remove-powershell-session]]):
```powershell
Remove-PSSession $Session
```

> This removes the active PSSession variable. Run it after invocation to close the connection. Expected output is a confirmation message like "Id Name ComputerName State" followed by the session details being cleared; no errors if the session exists.
