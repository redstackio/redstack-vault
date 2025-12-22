---
type: procedure
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Remote Desktop Protocol|T1076 - Remote Desktop Protocol]]'
  - '[[techniques/Remote File Copy|T1105 - Remote File Copy]]'
sub_techniques: []
tags:
  - '[[tags/RDP Remote Desktop Protocol]]'
  - '[[tags/Windows - Using credentials]]'
  - rdp
  - lateral-movement
  - remote-execution
commands:
  - '[[commands/rdesktop-connect-with-domain-credentials-and-share]]'
  - '[[commands/rdesktop-connect-with-local-credentials-and-share]]'
  - '[[commands/sharprdp-execute-remote-command]]'
  - '[[commands/freerdp-connect-with-credentials]]'
platforms:
  - Windows
  - Linux
tools:
  - '[[tools/rdesktop]]'
  - '[[tools/FreeRDP]]'
  - '[[tools/SharpRDP]]'
skill_level: intermediate
impact_level: high
detection_risk: high
verified: true
validated: true
---

# RDP-Remote-Code-Execution

## Summary

This procedure demonstrates how to use Remote Desktop Protocol (RDP) for remote code execution on a target Windows machine. It covers establishing an RDP connection using tools like rdesktop or FreeRDP with valid credentials, sharing resources for file transfer, and executing arbitrary commands remotely using SharpRDP, enabling lateral movement or post-exploitation in a network environment.

## Description

RDP Remote Code Execution leverages the Remote Desktop Protocol to connect to a target Windows system using stolen or brute-forced credentials. Once connected, attackers can interact with the desktop environment, transfer files via shared drives, or use specialized tools like SharpRDP to execute payloads without a full interactive session. This technique is commonly used for lateral movement after initial access, allowing control over remote systems to escalate privileges, exfiltrate data, or pivot to other hosts. It targets Windows environments where RDP is enabled (default port 3389) and requires administrative or RDP-authorized credentials. The approach combines valid account usage with remote service execution, making it stealthy if credentials are legitimate.

## Requirements

1. Valid domain or local credentials (username and password) for the target machine with RDP access permissions.
2. Network access to the target machine on port 3389 (RDP).
3. RDP client tools installed: rdesktop or FreeRDP on Linux/Kali, or SharpRDP on Windows/.NET environments.
4. For pass-the-hash variants, an administrative account not in the Remote Desktop Users group (applicable to Windows Server 2012 R2+).
5. Target machine running Windows with RDP enabled.

## Defense

- Enforce strong, unique passwords and multi-factor authentication (MFA) for RDP accounts.
- Monitor RDP logs for anomalous connections, failed logins, or logins from unusual IPs using tools like Windows Event Logs (ID 4624) or SIEM.
- Restrict RDP exposure: Use VPNs, firewalls to limit access to trusted IPs, and disable RDP where unnecessary (Group Policy: Computer Configuration > Administrative Templates > Windows Components > Remote Desktop Services).
- Implement endpoint detection for tools like FreeRDP or SharpRDP via behavioral analytics (e.g., unusual process spawning from RDP sessions).
- Enable Network Level Authentication (NLA) to require authentication before session establishment.

## Objectives

1. Establish a remote RDP connection to the target machine using provided credentials.
2. Share local resources for potential file transfer or payload staging during the session.
3. Execute arbitrary code or binaries on the remote system without requiring an interactive desktop.
4. Achieve lateral movement or persistence by leveraging the remote execution capabilities.

## Instructions

### Step 1: Connect to Target Using rdesktop with Domain Credentials and Shared Folder

**Context**: Use rdesktop to initiate an RDP session with domain credentials, specifying screen geometry and sharing a local folder for file transfer. This step establishes interactive access, allowing manual execution or setup for further actions. The shared drive enables ingress of tools or payloads.

**Command** ([[commands/rdesktop-connect-with-domain-credentials-and-share]]):
```bash
rdesktop -d $_DOMAIN -u $_USERNAME -p $_PASSWORD $_TARGET_IP -g $_GEOMETRY -r disk:share=$_SHARE_PATH
```

> This command connects to the target IP using domain authentication and mounts a local share. Replace placeholders with actual values (e.g., DOMAIN=corp, USERNAME=admin, PASSWORD=pass123, TARGET_IP=10.10.10.10, GEOMETRY=70%, SHARE_PATH=/home/user/myshare). Expected output includes a successful connection message and the RDP window opening. Verify by interacting with the remote desktop and checking if the shared drive appears in the file explorer.

### Step 2: Connect to Target Using rdesktop with Local Credentials and Shared Folder

**Context**: For non-domain environments, connect using local machine credentials. This variant omits the domain flag and uses percentage-based geometry for flexible screen sizing. It's useful when targeting standalone Windows systems.

**Command** ([[commands/rdesktop-connect-with-local-credentials-and-share]]):
```bash
rdesktop -u $_USERNAME -p $_PASSWORD -g $_GEOMETRY -r disk:share=$_SHARE_PATH $_TARGET_IP
```

> Execute this after ensuring no domain is required. Expected output: RDP session launches with the shared folder accessible on the remote side. Success is confirmed if the desktop loads without authentication errors and the share is visible (e.g., as a network drive).

### Step 3: Connect Using FreeRDP with Credentials and Optional Pass-the-Hash

**Context**: FreeRDP provides a cross-platform alternative for RDP connections, supporting features like clipboard sharing, certificate ignoring, and pass-the-hash for credentialless authentication in Restricted Admin mode. Use this when rdesktop is unavailable or for advanced options on Linux.

**Command** ([[commands/freerdp-connect-with-credentials]]):
```bash
xfreerdp /v:$_TARGET_IP /u:$_USERNAME /p:$_PASSWORD /d:$_DOMAIN +clipboard /cert-ignore /size:$_RESOLUTION /smart-sizing
```

> For pass-the-hash: Add `/pth:$_HASH` (requires admin account not in RDP Users group, works on Win 8.1+/Server 2012 R2+). Expected output: Connection success with RDP window; password prompt if omitted. Verify by checking clipboard functionality or remote desktop responsiveness. Install freerdp2-x11 for PTH support.

### Step 4: Execute Remote Code Using SharpRDP

**Context**: After obtaining credentials, use SharpRDP to execute a binary remotely via RDP without a full session. This is ideal for automated lateral movement, specifying the target, command, and credentials directly.

**Command** ([[commands/sharprdp-execute-remote-command]]):
```powershell
SharpRDP.exe -computername $_TARGET_HOST -command="$_REMOTE_PATH" -username $_USERNAME -password $_PASSWORD -domain $_DOMAIN
```

> Run on a Windows attacker machine with .NET. Expected output: Confirmation of execution (e.g., "Command executed successfully") and any stdout from the remote binary. If the command is a payload like file.exe, check for its effects (e.g., new process via Task Manager on target). Decision point: If connection fails, verify credentials and RDP service status.
