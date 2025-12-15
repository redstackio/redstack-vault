---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - persistence
  - unprivileged-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Linux
  - macOS
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Registry Run Keys - Startup Folder]]'
updated_at: '2025-12-14T17:29:10.126Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Registry Run Keys - Startup Folder]]'
---
# Gain-Non-Privileged-Access-and-Run-Malicious-Process

## Summary

This procedure allows an unprivileged attacker to log into the victim's machine and start a persistent background process, setting the stage for further exploitation without requiring elevated privileges.

## Description

In the context of the Monero wallet attack, the attacker uses standard user login methods (local, SSH, or remote desktop) to access the system. They then launch a malicious process that runs detached from the session, ensuring it continues after logout. This is crucial for binding to the RPC port before the victim starts the legitimate service. The target environment is a multi-user system where the attacker shares access with the victim, such as a shared workstation or enabled remote access.

## Requirements

1. Valid unprivileged user credentials or access to the victim's session
2. Knowledge of the OS (Linux, macOS, or Windows) for persistence techniques
3. Pre-built malicious process (e.g., a script or binary) to run in background

## Defense

Defensive measures and detection strategies:

- Monitor for unusual logins via SSH or RDP (e.g., using fail2ban or Windows Event Logs)
- Use process monitoring tools like auditd (Linux) or Sysmon (Windows) to detect unexpected background processes
- Enforce least-privilege access and disable unnecessary remote logins

## Objectives

1. Establish foothold as unprivileged user
2. Persist a process for subsequent steps
3. Avoid detection by running detached

## Instructions

### Step 1: Log In as Unprivileged User

**Context**: Gain access to the victim's computer without privileges to avoid alerts.

On Linux/macOS: Use SSH if enabled.
```bash
ssh user@victim-host
```
On Windows: Use Remote Desktop or fast user switching.

> Successful login prompt or desktop session.

### Step 2: Launch and Persist Malicious Process

**Context**: Start the process in background to survive logout.

On Linux/macOS:
```bash
nohup ./malicious_process &
# Or use screen/tmux: screen -dmS session ./malicious_process
```
On Windows:
Use PowerShell to create a scheduled task:
```powershell
schtasks /create /tn "Malicious" /tr "C:\path\to\process.exe" /sc once /st 00:00 /ru user
```

> Process starts and PID is returned; verify with `ps aux` or Task Manager.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Registry Run Keys - Startup Folder]] Registry Run Keys / Startup Folder

### Sub-Techniques

- None

## Commands Used

- None specific

## Tools Used

- None

## Tags

- persistence
- unprivileged-access
