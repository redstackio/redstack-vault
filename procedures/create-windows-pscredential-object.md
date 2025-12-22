---
id: f0b44a88-1014-49eb-9295-cb48a1efedc3
type: procedure
verified: true
submitted: false
created_at: '2020-03-13T23:31:09.355485+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
sub_techniques: []
tags:
  - '[[tags/authentication]]'
commands:
  - '[[commands/create-windows-secure-string]]'
  - '[[procedures/create-windows-pscredential-object]]'
platforms:
  - Windows
tools: []
validated: true
---

# Create Windows PSCredential Object

## Summary

This procedure creates a PSCredential object in PowerShell using a provided username and password. The PSCredential object encapsulates secure credentials that can be passed to various PowerShell cmdlets requiring authentication, enabling execution of commands under different user contexts or in scenarios where session credentials are not automatically propagated.

## Description

In Windows environments, PowerShell cmdlets such as Enter-PSSession, Invoke-Command, or New-PSSession often require explicit credentials for remote execution or authentication against services. This procedure converts a plaintext password into a secure string and then constructs a PSCredential object, which securely stores the username and encrypted password. This is particularly useful in red team operations for impersonating users, lateral movement, or accessing restricted resources without relying on the current session's identity. The technique aligns with using valid accounts to evade detection while maintaining operational flexibility. Prerequisites include running PowerShell with sufficient privileges to use the credentials (e.g., local admin for certain remote actions) and knowledge of the target username and password.

## Requirements

1. PowerShell 3.0 or later installed on a Windows system.
2. Valid username and password for the target account (domain format: DOMAIN\USER if applicable).
3. Local execution privileges to run PowerShell scripts or commands.
4. No external tools required; native PowerShell functionality is used.

## Defense

Defensive measures and detection strategies:

- Enable PowerShell logging (Module, Script Block, and Transcription) to capture credential creation events.
- Monitor for unusual SecureString conversions or PSCredential object instantiations in process execution logs.
- Implement application whitelisting to restrict unsigned scripts that handle credentials.
- Use tools like Sysmon to log PowerShell events with Event ID 4104 for suspicious credential usage.

## Objectives

1. Securely store username and password in a PSCredential object to prevent plaintext exposure in memory or logs.
2. Enable authentication to remote systems or services using alternative credentials.
3. Facilitate lateral movement or privilege escalation by passing the credential object to cmdlets like Invoke-Command.
4. Verify successful credential creation without triggering authentication attempts prematurely.

## Instructions

### Step 1: Convert Password to Secure String

**Context**: The password must first be converted to a SecureString to encrypt it in memory, preventing exposure in plaintext during script execution. This step uses the ConvertTo-SecureString cmdlet to handle the conversion securely.

**Command** ([[commands/create-windows-secure-string]]):
```powershell
$Pass = ConvertTo-SecureString -String "$_PASSWORD" -AsPlainText -Force
```

This command creates a SecureString object stored in the $Pass variable. The -AsPlainText parameter allows input of a plaintext string, while -Force suppresses prompts. Replace $_PASSWORD with the actual password (e.g., "P@ssw0rd123"). Expected behavior: No output if successful; the variable $Pass holds the encrypted string.

### Step 2: Create PSCredential Object

**Context**: Using the SecureString from Step 1, construct the PSCredential object by specifying the username and the secure password. This object can then be passed to cmdlets requiring credentials, such as for remote PowerShell sessions or WMI queries.

**Command** ([[procedures/create-windows-pscredential-object]]):
```powershell
$Cred = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList "$_USER", $Pass
```

This instantiates a new PSCredential object in $Cred, where $_USER is the username (e.g., "megabank\\dave" for domain accounts). The -ArgumentList passes the username as a string and $Pass as the secure password. Expected behavior: No output; $Cred now contains the usable credential object. To verify, run Get-Credential or use it in a test cmdlet like Test-NetConnection with -Credential $Cred.
