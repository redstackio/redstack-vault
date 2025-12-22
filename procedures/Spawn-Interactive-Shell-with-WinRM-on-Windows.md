---
id: 924f8d76-db72-4b6e-8b11-65c701d32b9c
name: Spawn-Interactive-Shell-with-WinRM-on-Windows
type: procedure
verified: true
submitted: true
created_at: '2020-03-21T01:59:57.868009+00:00'
updated_at: '2023-05-25T19:53:46.374157+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Windows Remote Management|T1028 - Windows Remote Management]]'
sub_techniques: []
tags:
  - '[[tags/Network]]'
  - '[[tags/powershell]]'
  - '[[tags/shell]]'
commands:
  - '[[commands/create-windows-pscredential-object]]'
  - '[[commands/create-and-enter-powershell-session-with-credentials]]'
  - '[[commands/remove-powershell-session]]'
platforms:
  - Windows
tools: []
validated: true
---

# Spawn-Interactive-Shell-with-WinRM-on-Windows

## Summary

This procedure demonstrates how to establish an interactive PowerShell session on a remote Windows system using Windows Remote Management (WinRM). It is useful for lateral movement in a Windows domain environment where valid credentials are available, allowing attackers to execute commands remotely without needing additional tools like RDP or SMB.

## Description

Windows Remote Management (WinRM) is a Microsoft implementation of WS-Management protocol that enables remote PowerShell execution over HTTP/HTTPS. This technique is commonly used in post-exploitation scenarios to pivot between compromised hosts. The process involves creating a secure credential object from username and password, establishing a PowerShell session (PSSession) to the target, and entering the session for interactive command execution. Once complete, the session should be cleaned up to avoid leaving artifacts. This method requires WinRM to be enabled on the target (default on modern Windows servers) and firewall rules allowing ports 5985 (HTTP) or 5986 (HTTPS). It maps to MITRE ATT&CK techniques for execution and lateral movement in Windows environments.

## Requirements

1. Valid domain or local credentials (username and password) for the target system.
2. Network connectivity to the target on port 5985 (HTTP) or 5986 (HTTPS).
3. WinRM service enabled and configured on the target Windows machine (e.g., via `winrm quickconfig` if admin access is already available).
4. PowerShell execution policy allowing remote sessions (e.g., not Restricted).
5. Attacker machine with PowerShell (native on Windows; on Linux/macOS, use PowerShell Core).

## Defense

Defensive measures and detection strategies:

- Monitor WinRM authentication logs in Event Viewer (Event ID 4672 for privilege use, 5145 for network share access).
- Enable Windows Defender ATP or similar EDR to detect anomalous PSSession creation.
- Restrict WinRM to trusted hosts via Group Policy and use HTTPS with certificates.
- Implement just-in-time privilege elevation to limit credential reuse.
- Audit PowerShell remoting with Module Logging and Script Block Logging enabled.

## Objectives

1. Create a secure credential object to authenticate to the remote system.
2. Establish and enter an interactive PowerShell session for command execution.
3. Clean up the session to minimize detection and resource usage.
4. Achieve remote code execution equivalent to an interactive shell.

## Instructions

### Step 1: Create PSCredential Object

**Context**: This step authenticates the connection by converting the plain-text password into a secure string and building a PSCredential object. For domain accounts, prefix the username with the domain (e.g., DOMAIN\user). This object is used in subsequent session creation to pass credentials securely.

**Command** ([[commands/create-windows-pscredential-object]]):
```powershell
$Pass = ConvertTo-SecureString -String "$_PASSWORD" -AsPlainText -Force
$Cred = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList "$_USER", $Pass
```

> This command creates a secure credential from the provided username and password placeholders. Replace $_USER with the target username (e.g., "Administrator" or "DOMAIN\user") and $_PASSWORD with the actual password. The -AsPlainText -Force flags are used for simplicity in scripting but increase risk if logged; in production attacks, consider encrypted storage. Expected output is no visible response if successful, but $Cred can be verified with Get-Credential or error if invalid.

### Step 2: Create and Enter PSSession

**Context**: Using the credential object, this step initiates a new PowerShell session to the remote target and enters it, providing an interactive shell prompt on the remote system. This allows direct command execution as if logged in locally, enabling further enumeration or exploitation.

**Command** ([[commands/create-and-enter-powershell-session-with-credentials]]):
```powershell
$Session = New-PSSession -Credential $Cred -ComputerName $_TARGET_IP
Enter-PSSession $Session
```

> Replace $_TARGET_IP with the target's IP or hostname (e.g., 10.10.10.10). The New-PSSession command establishes the remote connection over WinRM, returning a session object stored in $Session. Enter-PSSession switches the local PowerShell context to the remote one, changing the prompt to indicate the remote location (e.g., [10.10.10.10]: PS C:\>). If authentication fails, it will error with Access Denied; success is indicated by the prompt change and ability to run remote commands like whoami.

### Step 3: Clean Up Session

**Context**: After completing actions in the remote session (e.g., exit with 'exit'), this optional step removes the PSSession to free resources and reduce forensic footprints. Leaving sessions open can lead to detection via active connections.

**Command** ([[commands/remove-powershell-session]]):
```powershell
Remove-PSSession $Session
```

> Run this after exiting the session. It terminates the connection and removes the session object. Expected output is no response on success; errors if $Session is invalid or already removed. This helps evade detection by closing WinRM ports and clearing memory.
