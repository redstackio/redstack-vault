---
id: c77c1279-0a41-4626-8e58-ff8b94405f0b
name: execute-powershell-commands-as-another-user-using-pssession
type: procedure
verified: true
submitted: true
created_at: '2020-04-01T05:10:21.541159+00:00'
updated_at: '2024-10-01T00:00:00Z'
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Remote Services|T1021.006 - Windows Remote Management]]'
sub_techniques: []
platforms:
  - Windows
tags:
  - '[[tags/Active Directory]]'
  - '[[tags/authentication]]'
  - '[[tags/powershell]]'
  - '[[tags/shell]]'
  - '[[tags/lateral-movement]]'
commands:
  - '[[commands/create-windows-pscredential-object]]'
  - '[[commands/create-pssession-and-execute-command]]'
tools: []
validated: true
---

# execute-powershell-commands-as-another-user-using-pssession

## Summary

This procedure uses PowerShell's built-in cmdlets to execute commands as another user without spawning a new interactive shell. It is particularly useful for attackers who have obtained credentials for a target account but cannot establish traditional remote sessions like PSEXEC or direct WinRM due to network restrictions or configuration issues. The technique creates a secure credential object and leverages PSSession for local or remote command execution via the Windows Remote Management (WinRM) protocol.

## Description

In scenarios involving lateral movement or privilege escalation within a Windows environment, such as Active Directory domains, attackers often need to impersonate users with higher privileges. This procedure outlines the process of authenticating with stolen or guessed credentials to run arbitrary commands in the context of the target user. Locally, it acts as a 'runas' equivalent without UI prompts; remotely, it requires WinRM to be enabled on the target. The approach minimizes footprint by avoiding full shell spawns and can be chained with credential dumping techniques. Success depends on valid credentials and WinRM configuration, making it stealthy in environments with relaxed remote access controls.

## Requirements

- PowerShell version 3.0 or higher installed on the attacker's machine
- Valid credentials (username and password) for the target user account
- For remote execution: WinRM service enabled and listener configured on the target (run 'winrm quickconfig' on target if accessible)
- Network connectivity to the target machine if performing remote execution (default WinRM port 5985 for HTTP, 5986 for HTTPS)
- Local administrator privileges on the target may be needed for certain commands like process creation
- Domain-joined environment for full functionality with domain accounts

## Defense

- Enable advanced auditing for WinRM events (Event IDs 4672 for privilege use, 5145 for network share access, and 4624 for logons)
- Configure PowerShell constrained language mode and script block logging to capture PSSession creations and Invoke-Command usage
- Restrict WinRM access via Group Policy to only trusted hosts and require HTTPS with certificate authentication
- Implement just-in-time privilege elevation and monitor for anomalous credential usage across sessions
- Use tools like Sysmon to log PowerShell process creations and network connections to WinRM ports

## Objectives

- Authenticate securely using provided credentials without exposing plaintext passwords in memory long-term
- Establish a temporary PowerShell session in the context of the target user for command execution
- Run arbitrary processes or scripts as the target user to achieve lateral movement, data access, or escalation

## Instructions

### Step 1: Create PSCredential Object

**Context**: Begin by constructing a PSCredential object, which securely stores the username and password for authentication. This step is essential to handle credentials without repeatedly prompting or hardcoding sensitive data, and it supports both local and domain accounts.

**Command** ([[commands/create-windows-pscredential-object]]):

```powershell
$Pass = ConvertTo-SecureString -String "$_PASSWORD" -AsPlainText -Force
$Cred = New-Object -TypeName System.Management.Automation.PSCredential -Argument "$_DOMAIN\$_USER", $Pass
```

This command first converts the plaintext password into a SecureString to protect it in memory. Then, it creates the PSCredential object using the domain-qualified username (e.g., "MEGABANK\jsmith" for domain accounts or "localhost\jsmith" for local). If no domain is needed, omit it and use just the username. Success is confirmed by no errors thrown; the $Cred variable can then be inspected with Get-Credential or used directly.

### Step 2: Create PSSession and Execute Command

**Context**: With the credential ready, establish a new PSSession to the target (local or remote) and invoke a command within it. This impersonates the target user for execution, allowing actions like launching processes or running scripts without a persistent shell.

**Command** ([[commands/create-pssession-and-execute-command]]):

```powershell
$Session = New-PSSession -ComputerName $_TARGET_IP -Credential $Cred
Invoke-Command -Session $Session -ScriptBlock {Start-Process $_CMD}
```

This creates a session using the provided credential and target IP (use "localhost" or omit -ComputerName for local execution). The Invoke-Command then runs a script block in the session, here using Start-Process to launch a command like "notepad.exe" or "cmd.exe /c whoami". Replace $_CMD with the desired executable or command string. After execution, remove the session with Remove-PSSession $Session to clean up. Expected output includes any stdout from the command, and errors indicate authentication failures or WinRM issues.
