---
id: 0342282d-a959-4d9d-a521-a6c2f747eb85
name: Create-PSCredential-Object-with-Secure-Password
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:31.116096+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Lateral Movement]]'
techniques:
  - '[[Valid Accounts]]'
  - '[[Use Alternate Authentication Material]]'
sub_techniques: []
tags:
  - powershell-credentials
  - powershell-remoting
  - windows-credentials
commands:
  - '[[commands/create-pscredential-from-plaintext-password]]'
platforms:
  - Windows
tools: []
validated: true
---

# Create-PSCredential-Object-with-Secure-Password

## Summary

This procedure demonstrates how to create a secure PSCredential object in PowerShell from a plaintext password, enabling authenticated remote command execution via PowerShell Remoting without repeated manual input. In offensive security contexts, this allows attackers to store and reuse credentials for lateral movement and persistence on Windows domains.

## Description

Creating a PSCredential object encapsulates a username and securely handles a password as a SecureString, which is essential for cmdlets like Invoke-Command that require authentication over PowerShell Remoting (WinRM). This technique is commonly used in red team operations to automate remote execution after obtaining credentials, reducing detection risk by avoiding interactive prompts. The process involves converting a plaintext password to a SecureString using ConvertTo-SecureString, then instantiating a PSCredential object with New-Object. This object can authenticate to remote systems, enabling command execution, file transfers, or further enumeration without exposing the password in logs or memory in plaintext form. Target environments include Active Directory domains where WinRM is enabled (default on Windows Server). Prerequisites include local PowerShell execution rights and valid domain credentials.

## Requirements

1. PowerShell 3.0 or later installed on a Windows system.
2. Valid domain username and plaintext password (obtained via prior credential access).
3. Network access to the target system with WinRM enabled (port 5985/5986).
4. Administrative or delegated rights on the target for remote execution.

## Defense

- Enforce least privilege: Limit WinRM access to authorized accounts and monitor for anomalous remote invocations via Event ID 5140/5141 in Windows Security logs.
- Use Just-In-Time (JIT) access and Privileged Access Workstations (PAW) to restrict credential usage.
- Enable PowerShell logging (Module, Script Block, and Transcription) to capture credential object creation and remote command details.
- Implement credential guard features like Windows Defender Credential Guard to protect against in-memory credential extraction.

## Objectives

1. Convert a plaintext password to a SecureString for secure handling.
2. Instantiate a PSCredential object with the username and SecureString.
3. Use the PSCredential object to authenticate and execute remote commands undetected.
4. Verify successful remote access without exposing credentials in command history.

## Instructions

### Step 1: Convert Plaintext Password to SecureString

**Context**: Start by transforming the plaintext password into a SecureString to prevent it from being stored or logged in clear text. This step uses the -AsPlainText and -Force parameters to allow conversion despite the insecure input source, which is common in scripted offensive scenarios where passwords are harvested dynamically.

**Command** ([[commands/create-pscredential-from-plaintext-password]]):

```powershell
$pass = ConvertTo-SecureString 'supersecurepassword' -AsPlainText -Force
```

> This command creates a SecureString variable $pass. The password 'supersecurepassword' is a placeholder—replace it with the actual harvested credential. Expected output is no visible response if successful, but you can verify with $pass.GetType() to confirm it's a SecureString. If the conversion fails (e.g., due to invalid characters), PowerShell will throw a conversion error.

### Step 2: Create PSCredential Object

**Context**: Use the SecureString to build the PSCredential object, specifying the username in DOMAIN\Username format for domain authentication. This object can now be passed to remoting cmdlets like Invoke-Command for lateral movement.

**Command** ([[commands/create-pscredential-from-plaintext-password]]):

```powershell
$cred = New-Object System.Management.Automation.PSCredential ('DOMAIN\Username', $pass)
```

> This instantiates $cred as a PSCredential object. Replace 'DOMAIN\Username' with the target account (e.g., 'CONTOSO\Administrator'). No output is produced on success. To verify, run $cred.UserName and $cred.Password (the latter returns a SecureString, not plaintext). Decision point: If targeting a local account, use 'ComputerName\Username' instead.

### Step 3: Test Remote Authentication (Optional Verification)

**Context**: Validate the credential by invoking a simple remote command, such as getting the target system's hostname. This confirms WinRM connectivity and credential validity without full exploitation.

**Instructions**: Use Invoke-Command with the $cred object:

```powershell
Invoke-Command -ComputerName TargetHost -Credential $cred -ScriptBlock { hostname }
```

> Expected output: The target's hostname (e.g., 'DC01'). If authentication fails, check WinRM configuration with Test-WSMan TargetHost. Success indicates the credential is usable for further actions like persistence via scheduled tasks.
