---
type: procedure
description: >-
  Configure and establish remote management access to a Windows target using
  WinRM for lateral movement or post-exploitation.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
tactics:
  - '[[Lateral Movement]]'
techniques:
  - '[[Windows Remote Management]]'
sub_techniques: []
tags:
  - winrm
  - remote-management
  - lateral-movement
  - windows
commands:
  - '[[commands/winrm-quickconfig]]'
  - '[[commands/winrm-enumerate-listeners]]'
  - '[[commands/winrm-get-service-config]]'
  - '[[commands/winrm-set-service-basic-auth]]'
  - '[[commands/winrm-set-service-allow-unencrypted]]'
  - '[[commands/winrm-set-service-cbt-hardening-relaxed]]'
  - '[[commands/winrm-get-client-config]]'
  - '[[commands/winrm-set-client-allow-unencrypted]]'
  - '[[commands/winrm-set-client-trustedhosts]]'
  - '[[commands/winrm-identify-basic]]'
  - '[[commands/enter-pssession-basic-auth]]'
platforms:
  - Windows
tools: []
validated: true
---

# windows-remoting-via-winrm

## Summary

This procedure configures Windows Remote Management (WinRM) on a target Windows system to enable remote access and management from an attacker-controlled system, allowing execution of commands, file transfers, and interactive sessions. It is commonly used in lateral movement scenarios after obtaining initial credentials, bypassing the need for SMB or RDP by leveraging HTTP-based remoting.

## Description

WinRM is a Microsoft implementation of WS-Management protocol, enabling remote PowerShell execution and management over HTTP/HTTPS. By default, WinRM is disabled or restricted on Windows systems for security. This procedure details enabling the WinRM listener on the target, configuring authentication and encryption settings to allow basic auth and unencrypted traffic (for testing in lab environments), and setting up the client side for connection. Once configured, an interactive PowerShell session can be established, facilitating command execution without physical access. This technique aligns with scenarios where an attacker has local admin credentials on the target but needs to pivot remotely. Note: In production, enabling unencrypted traffic increases risk; use HTTPS in real engagements.

## Requirements

1. Administrative privileges on the target Windows system (local or domain admin).
2. Network connectivity between attacker and target (default port 5985 for HTTP, 5986 for HTTPS).
3. Valid credentials (username/password) for the target system.
4. PowerShell 3.0+ on both target and attacker systems (WinRM client available on Windows, Linux/macOS via open-source tools like evil-winrm, but this focuses on native Windows client).
5. Firewall rules allowing inbound WinRM traffic on the target.

## Defense

- Monitor WinRM service startup via Event ID 2003 in Windows Event Logs (System channel).
- Enable WinRM auditing and restrict to Kerberos auth only; disable Basic auth and unencrypted traffic.
- Use Group Policy to enforce HTTPS-only WinRM and CBT hardening at 'Strict' level.
- Detect anomalous remote connections via network logs (port 5985) or PowerShell remoting events (Event ID 8004).
- Implement just-in-time admin access and monitor for winrm.exe process spawning from unusual parents.

## Objectives

1. Enable and configure WinRM service on the target for remote access.
2. Prepare the attacker system to connect securely or in a lab-unencrypted mode.
3. Establish an interactive remote PowerShell session for command execution.
4. Verify connectivity and session functionality for further operations.

## Instructions

### Target System Setup

#### Step 1: Enable Default WinRM Configuration

**Context**: This step initializes the WinRM service, creates a listener, and starts the service if not already running. It is the foundational setup required for remote access.

**Command** ([[commands/winrm-quickconfig]]):
```powershell
winrm quickconfig
```

> Run this as administrator. It will prompt for confirmation to enable the WinRM service and create an HTTP listener on port 5985. Expected: Confirmation message like "WinRM is already set up..." if previously configured, or success after enabling.

#### Step 2: Enumerate WinRM Listeners

**Context**: Verify the listener configuration, including ports and addresses, to ensure the service is listening correctly for incoming connections.

**Command** ([[commands/winrm-enumerate-listeners]]):
```powershell
winrm enumerate winrm/config/listener
```

> This displays active listeners. Expected output: Details of the HTTP listener on * (all addresses), port 5985, enabled=true.

#### Step 3: Check Service Authentication Configuration

**Context**: Inspect current auth settings to determine if Basic authentication is allowed, as it is required for simple credential-based access.

**Command** ([[commands/winrm-get-service-config]]):
```powershell
winrm get winrm/config/service
```

> Look for the Auth section. Expected: Output showing Basic = false initially; if true, skip to next steps.

#### Step 4: Enable Basic Authentication on Service

**Context**: Allows username/password authentication over the wire, necessary for non-Kerberos environments or cross-domain access.

**Command** ([[commands/winrm-set-service-basic-auth]]):
```powershell
winrm set winrm/config/service/auth @{Basic="true"}
```

> Expected: Confirmation "Config changed" and updated output from get command showing Basic = true.

#### Step 5: Enable Unencrypted Traffic on Service

**Context**: Permits HTTP (non-HTTPS) connections for lab testing; in production, configure HTTPS instead to avoid exposing credentials.

**Command** ([[commands/winrm-set-service-allow-unencrypted]]):
```powershell
winrm set winrm/config/service @{AllowUnencrypted="true"}
```

> Expected: Confirmation message; verify with winrm get winrm/config/service showing AllowUnencrypted = true.

#### Step 6: Set Channel Binding Token Hardening to Relaxed

**Context**: Reduces security checks for channel binding tokens, allowing connections in mixed environments; set to 'none' for broader compatibility but higher risk.

**Command** ([[commands/winrm-set-service-cbt-hardening-relaxed]]):
```powershell
winrm set winrm/config/service/auth @{CbtHardeningLevel="relaxed"}
```

> Expected: Updated auth config showing CbtHardeningLevel = relaxed.

### Attacker System Setup

#### Step 7: View Client Configuration

**Context**: Check the current WinRM client settings to ensure compatibility with the target.

**Command** ([[commands/winrm-get-client-config]]):
```powershell
winrm get winrm/config/client
```

> Expected: Output showing default settings, including AllowUnencrypted = false initially.

#### Step 8: Enable Unencrypted Traffic on Client

**Context**: Matches the server's unencrypted allowance for HTTP connections.

**Command** ([[commands/winrm-set-client-allow-unencrypted]]):
```powershell
winrm set winrm/config/client @{AllowUnencrypted="true"}
```

> Expected: Confirmation; verify with get command.

#### Step 9: Configure Trusted Hosts for External Domains

**Context**: If the target is not in the same domain or workgroup, add it to trusted hosts to bypass hostname verification.

**Command** ([[commands/winrm-set-client-trustedhosts]]):
```powershell
winrm set winrm/config/client @{TrustedHosts="target-hostname, target-ip"}
```

> Replace with actual target details. Expected: Updated TrustedHosts list.

#### Step 10: Test Connection to Target WinRM Service

**Context**: Validates credentials and connectivity before opening a full session.

**Command** ([[commands/winrm-identify-basic]]):
```powershell
winrm identify -r:http://$TARGET_IP:5985/wsman -auth:basic -u:$USERNAME -p:$PASSWORD -encoding:utf-8
```

> Use target IP, username, and password. Expected: Protocol version and product details (e.g., OS version) if successful; error if failed.

#### Step 11: Open Interactive PowerShell Session

**Context**: Establishes a remote session for executing commands on the target.

**Command** ([[commands/enter-pssession-basic-auth]]):
```powershell
$cred = Get-Credential
Enter-PSSession -ComputerName $TARGET_HOSTNAME -Credential $cred -Authentication Basic
```

> Prompts for credentials. Expected: PS prompt changes to remote session (e.g., [target]: PS C:\>); type Exit to close.
