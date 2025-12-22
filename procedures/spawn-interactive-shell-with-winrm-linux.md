---
id: e732ce42-b42b-4f1e-9288-b71befcd80f1
name: spawn-interactive-shell-with-winrm-linux
type: procedure
verified: true
submitted: false
created_at: '2019-11-22T22:40:14.550466+00:00'
updated_at: '2023-05-25T19:42:05.411624+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Windows Remote Management|T1028 - Windows Remote Management]]'
sub_techniques:
  - '[[techniques/Windows Remote Management.T1028.001 - Remotely via WinRM]]'
tags:
  - network
  - remote-access
commands:
  - '[[commands/evil-winrm-connect-to-winrm-server]]'
platforms:
  - Windows
tools:
  - '[[tools/Evil-WinRM]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# spawn-interactive-shell-with-winrm-linux

## Summary

This procedure establishes an interactive PowerShell shell on a Windows target using WinRM (port 5985) from a Linux attacker machine, enabling command execution and file transfer post-credential acquisition.

## Description

WinRM is the Windows remote management protocol, often enabled for admin tasks. Evil-WinRM provides a Ruby-based client for shell access, supporting uploads and PowerShell execution without PsExec alternatives.

## Requirements

1. Valid username/password for target
2. WinRM enabled and port 5985 open
3. Evil-WinRM gem installed (gem install evil-winrm)

## Defense

- Disable WinRM if unused (winrm quickconfig -disable)
- Use HTTPS for WinRM and certificate auth
- Log WinRM events (ID 514) for anomalous logins

## Objectives

1. Gain remote shell access
2. Execute commands for enumeration/escalation
3. Transfer files for persistence

## Instructions

### Step 1: Verify WinRM Availability

**Context**: Confirm service from prior scan.

nmap -p 5985 $_TARGET_IP

> Should show open.

### Step 2: Connect Shell

**Context**: Authenticate and spawn PS session.

**Command** ([[commands/evil-winrm-connect-to-winrm-server]]):
```bash
evil-winrm -i $_TARGET_IP -u $_USERNAME -p $_PASSWORD
```

> Yields PS prompt; use upload localfile remotepath for transfers.

### Step 3: Interact and Exit

**Context**: Run whoami, then exit cleanly.

In shell: whoami; exit

> Success if commands execute as expected.
