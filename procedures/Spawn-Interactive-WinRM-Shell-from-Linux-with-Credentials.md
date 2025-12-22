---
id: e732ce42-b42b-4f1e-9288-b71befcd80f1
name: Spawn-Interactive-WinRM-Shell-from-Linux-with-Credentials
type: procedure
verified: true
submitted: true
created_at: '2019-11-22T22:40:14.550466+00:00'
updated_at: '2023-05-25T19:42:05.411624+00:00'
tactics:
  - '[[Execution]]'
  - '[[Lateral Movement]]'
techniques:
  - '[[Windows Remote Management]]'
sub_techniques: []
tags:
  - network
  - shell
commands:
  - '[[commands/evil-winrm-rb-connect-with-credentials]]'
platforms:
  - Windows
tools:
  - '[[tools/Evil-WinRM]]'
validated: true
---

# Spawn-Interactive-WinRM-Shell-from-Linux-with-Credentials

## Summary

This procedure spawns an interactive PowerShell shell on a remote Windows system via WinRM using plaintext credentials obtained from cracking, enabling command execution for post-exploitation.

## Description

WinRM (port 5985) allows remote PowerShell remoting. Evil-WinRM provides a Ruby-based client for Linux attackers to connect and execute commands, ideal for lateral movement after credential recovery.

## Requirements

- WinRM enabled on target
- Valid username/password
- Evil-WinRM installed (gem install evil-winrm)
- Network access to port 5985

## Defense

- Disable WinRM if not needed
- Use HTTPS for WinRM and certificate auth
- Monitor WinRM logs for unauthorized access

## Objectives

1. Authenticate to WinRM service
2. Obtain interactive shell
3. Execute reconnaissance commands

## Instructions

### Step 1: Verify WinRM Availability

**Context**: Ensure port 5985 is open from prior scan.

No command; use nmap if needed.

### Step 2: Connect and Spawn Shell

**Context**: Use credentials to establish session.

**Command** ([[commands/evil-winrm-rb-connect-with-credentials]]):
```bash
evil-winrm.rb -i $_TARGET_IP -u $_USERNAME -p $_PASSWORD
```

> Establishes encrypted connection. Use 'ifconfig' or 'whoami' to verify.

### Step 3: Interact and Exit

**Context**: Run commands; exit with 'exit'.

**Expected Output**: Prompt '*Evil-WinRM* PS C:\>'.

## Expected Output

Evil-WinRM shell v2.3
Info: Establishing connection...
*Evil-WinRM* PS C:\Users\username\>
