---
type: procedure
verified: true
submitted: true
tactics:
  - '[[Execution]]'
  - '[[Lateral Movement]]'
techniques:
  - '[[Windows Remote Management]]'
tags:
  - winrm
  - shell
  - lateral-movement
  - network
platforms:
  - Windows
commands:
  - '[[commands/evil-winrm-connect-to-winrm-server]]'
tools:
  - '[[tools/Evil-WinRM]]'
validated: true
---

# spawn-interactive-shell-with-winrm

## Summary

This procedure establishes an interactive PowerShell shell on a remote Windows machine using the WinRM protocol with stolen credentials, enabling command execution and lateral movement.

## Description

WinRM (Windows Remote Management) is enabled by default on many Windows servers for management. Tools like evil-winrm authenticate over HTTP/HTTPS (ports 5985/5986) to spawn shells without needing SMB or RDP. It's useful post-credential theft for persistence.

## Requirements

- Valid username:password for target
- WinRM service running on target (winrm quickconfig if needed)
- Network access to port 5985
- evil-winrm gem installed (gem install evil-winrm)

## Defense

- Disable WinRM if not needed (winrm delete winrm/config/listener)
- Use HTTPS-only and certificate auth
- Monitor WinRM logs (Event ID 91 for connections) and network traffic
- Implement just-in-time access for WinRM

## Objectives

- Establish stable remote shell
- Execute reconnaissance commands
- Maintain access for dumping or escalation

## Instructions

### Step 1: Verify WinRM Connectivity

**Context**: Test port reachability with nmap or telnet.

No specific command.

> Why: Confirms service availability before auth attempt.

### Step 2: Connect and Spawn Shell

**Context**: Use evil-winrm to authenticate and get PS prompt.

**Command** ([[commands/evil-winrm-connect-to-winrm-server]]):

```bash
evil-winrm -i $_TARGET_IP -u $_USERNAME -p $_PASSWORD
```

> Success shows PS prompt. Use 'ifconfig' or 'ipconfig' to verify.

### Step 3: Interact and Exit Safely

**Context**: Run commands like whoami; exit with 'exit'.

No command.

> Why: Validates access; avoid suspicious commands initially.
