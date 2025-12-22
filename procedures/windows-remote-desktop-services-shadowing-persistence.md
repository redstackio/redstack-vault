---
type: procedure
description: >-
  Establishes persistence on a Windows system by configuring Remote Desktop
  Services shadowing to allow unauthorized viewing of user sessions without
  consent.
verified: true
submitted: false
tactics:
  - '[[Lateral Movement]]'
techniques:
  - '[[Remote Desktop Protocol]]'
sub_techniques: []
tags:
  - elevated
  - remote-desktop-services-shadowing
  - windows-persistence
commands:
  - '[[commands/allow-remote-connections]]'
  - '[[commands/configure-terminal-services-shadowing]]'
  - '[[commands/disable-uac-remote-restriction]]'
  - '[[commands/shadow-remote-session]]'
platforms:
  - Windows
tools: []
validated: true
---

# windows-remote-desktop-services-shadowing-persistence

## Summary

This procedure configures Windows Remote Desktop Services to enable shadowing, allowing an administrator or attacker with elevated privileges to view and potentially control user sessions remotely without the user's knowledge or consent. It sets necessary registry keys to permit remote connections, disable restrictions, and initiate shadowing, providing a method for persistence and lateral movement while evading detection.

## Description

Remote Desktop Services Shadowing is a built-in Windows feature that permits administrators to remotely view active user sessions on a target machine without logging out the user. In an attack context, this can be abused for persistence by maintaining visibility into user activities post-compromise, enabling data theft, keystroke monitoring, or further lateral movement. The technique requires administrator-level access to the target system and modifies registry settings to allow remote access and bypass consent prompts. It is particularly effective in domain environments where Remote Desktop is enabled, and it maps to MITRE ATT&CK technique T1076 (Remote Desktop Protocol) under the Lateral Movement tactic. Once configured, the attacker can shadow sessions indefinitely, remaining stealthy as no new login events are generated.

## Requirements

1. Administrator-level privileges on the target Windows system (local or domain admin).
2. Network access to the target machine via RDP (port 3389 open).
3. Knowledge of the target's IP address or hostname and active session IDs (obtainable via tools like qwinsta or query session).
4. Windows Server 2012 or later, or Windows 10/11 with Remote Desktop Services enabled.

## Defense

- Restrict administrator privileges using the principle of least privilege; audit and limit RDP access.
- Monitor registry changes to keys under HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services and related paths using tools like Sysmon or Windows Event Logs (Event ID 4657 for registry modifications).
- Enable User Account Control (UAC) remote restrictions and require user consent for shadowing via Group Policy.
- Disable unnecessary Remote Desktop features if not required for business operations; use network segmentation to limit RDP exposure.
- Log and alert on anomalous RDP connections or shadowing attempts (Event IDs 1149, 1150 in Security logs).

## Objectives

1. Establish persistent remote visibility into user sessions without alerting the user.
2. Enable lateral movement or data collection from compromised systems.
3. Maintain access even after initial detection and partial remediation efforts.

## Instructions

### Step 1: Configure Terminal Services Shadowing

**Context**: This step enables the shadowing feature in the registry, setting it to allow viewing sessions without user permission (value 4). This is necessary to bypass consent requirements and prepare the system for remote shadowing.

**Command** ([[commands/configure-terminal-services-shadowing]]):
```cmd
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services" /v Shadow /t REG_DWORD /d 4
```

> This command creates or modifies the Shadow registry value to 4, which disables user consent prompts for shadowing. Run this from an elevated command prompt. If the key does not exist, it will be created.

### Step 2: Allow Remote Connections

**Context**: Remote Desktop connections must be enabled on the target to allow the shadowing session from a remote machine. This modifies the Terminal Server control set to permit incoming RDP connections.

**Command** ([[commands/allow-remote-connections]]):
```cmd
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
```

> Setting fDenyTSConnections to 0 enables RDP listener. The /f flag forces the change without prompting. Verify with `reg query` afterward; success is indicated by the value being 0.

### Step 3: Disable UAC Remote Restriction

**Context**: UAC can block remote administrative access for local accounts. Disabling this filter allows remote execution of privileged commands without full admin token elevation prompts.

**Command** ([[commands/disable-uac-remote-restriction]]):
```cmd
reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v LocalAccountTokenFilterPolicy /t REG_DWORD /d 1 /f
```

> This sets LocalAccountTokenFilterPolicy to 1, removing UAC restrictions for remote logons. It's crucial for non-domain admin accounts. Reboot may be required for full effect, but changes apply immediately for new sessions.

### Step 4: Shadow the Remote Session

**Context**: With configurations in place, initiate the shadowing connection to view the target user's desktop session. Obtain the session ID using `qwinsta` or `query session` on the target first.

**Command** ([[commands/shadow-remote-session]]):
```cmd
mstsc /v:$_TARGET_ADDRESS /shadow:$_SESSION_ID /noconsentprompt /prompt
```

> Replace $_TARGET_ADDRESS with the target's IP/hostname and $_SESSION_ID with the numeric session ID (e.g., 2). The /noconsentprompt bypasses permission requests, and /prompt allows credential entry. This launches the Remote Desktop client to shadow the session. If successful, you'll see the user's desktop without interrupting their activity.

### Step 5: Verify and Maintain Access

**Context**: Confirm the shadowing is active and monitor for persistence. Use built-in tools to list sessions and ensure configurations persist across reboots.

Run `qwinsta` on the target to list active sessions and confirm your connection. To make changes persistent, ensure Group Policy does not override the registry settings (check via `gpresult /h report.html`). If the target reboots, reapply registry changes if needed, or use scheduled tasks for automation.
