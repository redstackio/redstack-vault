---
id: aee0b0b2-8411-4b4e-ad04-563e0cb510df
name: Remote-Access-to-Windows-Machine-Using-Credentials
type: procedure
verified: true
submitted: false
created_at: '2023-01-12T07:48:43.933593+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Windows Remote Management|T1028 - Windows Remote Management]]'
sub_techniques: []
tags:
  - '[[tags/PowerShell-Remote]]'
  - '[[tags/WinRS]]'
commands:
  - '[[commands/WinRS-Open-CMD-on-Remote-Windows-Machine]]'
  - '[[commands/WinRS-Open-CMD-on-Remote-Windows-Machine-With-Credentials]]'
  - '[[commands/New-PSSession-to-Remote-Windows-Machine]]'
  - '[[commands/New-PSSession-to-Remote-Windows-Machine-With-Credentials]]'
platforms:
  - Windows
tools: []
validated: true
---

# Remote-Access-to-Windows-Machine-Using-Credentials

## Summary

This procedure enables remote access to a Windows machine by establishing a command prompt (CMD) or PowerShell session using Windows Remote Management (WinRM) via WinRS or PowerShell remoting. It supports scenarios with and without explicit credentials, allowing lateral movement or execution in a Windows domain environment where WinRM is enabled.

## Description

Windows Remote Management (WinRM) is a Microsoft implementation of WS-Management protocol that allows remote command execution over HTTP/HTTPS. This procedure leverages WinRS (a command-line tool for WinRM) and PowerShell's PSSession cmdlets to connect to a target Windows machine. It is useful in red team engagements for lateral movement after obtaining credentials or when implicit authentication (e.g., via Kerberos in a domain) is possible. The target must have WinRM configured and listening (default port 5985 for HTTP, 5986 for HTTPS), and firewall rules allowing inbound connections. Potential risks include detection through WinRM event logs if not configured for stealth.

## Requirements

1. Administrative or valid user credentials on the target Windows machine (for credentialed access).
2. WinRM service enabled and configured on the target (run `winrm quickconfig` on target if needed).
3. Network connectivity to the target on ports 5985 (HTTP) or 5986 (HTTPS).
4. PowerShell 3.0+ or WinRS tool available on the attacker's machine (native on Windows).
5. Domain-joined environment for implicit authentication, or explicit credentials for workgroup setups.

## Defense

- Monitor WinRM event logs (Event ID 91, 168 for connections) using Windows Event Forwarding or SIEM.
- Restrict WinRM access via Group Policy to trusted hosts/IPs and require HTTPS.
- Enable PowerShell transcription and module logging to capture remote session activity.
- Use Just-In-Time (JIT) access or Privileged Access Workstations (PAW) to limit lateral movement.
- Firewall rules to block unauthorized inbound WinRM traffic.

## Objectives

1. Establish a remote CMD or PowerShell session for command execution on the target.
2. Verify successful connection and interactive access.
3. Enable further post-exploitation actions like file transfer or privilege escalation.

## Instructions

### Step 1: Connect Using WinRS Without Credentials

**Context**: Use WinRS to open a CMD session on the target when implicit authentication (e.g., current user context in a domain) is sufficient. This assumes WinRM trusts the attacker's machine.

**Command** ([[commands/WinRS-Open-CMD-on-Remote-Windows-Machine]]):
```powershell
winrs -r:$_COMPUTER_NAME cmd
```

> This command initiates a remote CMD shell. Replace $_COMPUTER_NAME with the target's hostname or IP. Expected output includes a remote prompt like `C:\Windows\system32>` indicating success. If authentication fails, proceed to credentialed methods.

### Step 2: Connect Using WinRS With Credentials

**Context**: Provide explicit credentials for access when implicit auth fails, such as in workgroups or cross-domain scenarios. This uses local or domain credentials.

**Command** ([[commands/WinRS-Open-CMD-on-Remote-Windows-Machine-With-Credentials]]):
```powershell
winrs -r:$_COMPUTER_NAME -u:$_DOMAIN\$_USERNAME -p:$_PASSWORD cmd
```

> Substitute $_COMPUTER_NAME (target), $_DOMAIN (e.g., . for local), $_USERNAME, and $_PASSWORD. Success yields a remote CMD prompt. Use `-remote:HTTPS` for encrypted connections if configured.

### Step 3: Connect Using PowerShell Remoting Without Credentials

**Context**: Create a PSSession for interactive PowerShell access using implicit authentication, ideal for scripted or multi-command execution.

**Command** ([[commands/New-PSSession-to-Remote-Windows-Machine]]):
```powershell
$session = New-PSSession -ComputerName $_COMPUTER_NAME
Enter-PSSession $session
```

> This creates a session variable and enters it, showing a remote PS prompt like `[target]: PS C:\Users\>`. Use `Exit-PSSession` to disconnect. Verify with `Get-PSSession`.

### Step 4: Connect Using PowerShell Remoting With Credentials

**Context**: Securely pass credentials to New-PSSession for authenticated access, preventing plaintext password exposure in history.

**Command** ([[commands/New-PSSession-to-Remote-Windows-Machine-With-Credentials]]):
```powershell
$password = ConvertTo-SecureString $_PASSWORD -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential ($_USERNAME, $password)
$session = New-PSSession -ComputerName $_COMPUTER_NAME -Credential $cred
Enter-PSSession $session
```

> Replace $_USERNAME, $_PASSWORD, and $_COMPUTER_NAME. The secure string avoids logging plaintext. Success is indicated by the remote PS prompt. For domain creds, use `$_DOMAIN\$_USERNAME`.
